"""
识别模型主代码
"""
from keras.models import *
from keras.layers import *
from keras.preprocessing.image import *
from keras.applications import *
from keras import optimizers

from sklearn.utils import shuffle
from sklearn.preprocessing import OneHotEncoder

from utils import *

import h5py

def write_gap(pre_model, image_size, lambda_func=None):
    """

    :param pre_model:
    :param image_size:
    :param lambda_func:
    :return:
    """
    width = image_size[0]
    height = image_size[1]
    input_tensor = Input(shape=(width, height, 3))
    x = input_tensor
    if lambda_func:
        x = Lambda(lambda_func)(x)

    base_model = pre_model(include_top=False, weights='imagenet', input_tensor=x)
    model = Model(inputs=base_model.input, outputs=GlobalAveragePooling2D()(base_model.output))

    gen = ImageDataGenerator(samplewise_std_normalization=True, rescale=1./255)

    train_generator = gen.flow_from_directory(directory=train_path, target_size=image_size,
                                              class_mode='categorical', shuffle=False)
    test_generator = gen.flow_from_directory(directory=test_path, target_size=image_size,
                                             class_mode=None, shuffle=False)

    train_predict = model.predict_generator(train_generator)
    test_predict = model.predict_generator(test_generator)
    label = train_generator.classes
    with h5py.File(h5_path+'\\gap_%s.h5'%pre_model.__name__) as h:
        h.create_dataset('train', data=train_predict)
        h.create_dataset('test', data=test_predict)
        h.create_dataset('label', data=label)
    print('Done')
    return None


def build_model(input_shape, units=256, seed=2018):
    """

    :param input_shape:
    :param units:
    :param seed:
    :return:
    """
    input_tensor = Input(shape=input_shape)
    np.random.seed(seed)
    x = Dense(units=units, activation='relu')(input_tensor)
    x = Dropout(0.5)(x)
    x = Dense(120, activation='softmax')(x)
    model = Model(inputs=input_tensor, outputs=x)
    return model


def load_gap(gap_name, seed=2018):
    """

    :param gap_name:
    :param seed:
    :return:
    """
    np.random.seed(seed)
    with h5py.File(name=h5_path+'\\gap_'+gap_name+'.h5', mode='r') as h:
        x_train = np.array(h['train'])
        x_test = np.array(h['test'])
        y_train = np.array(h['label'])
    x_train, y_train = shuffle(x_train, y_train)
    y_train = OneHotEncoder().fit_transform(y_train.reshape(-1, 1))
    return x_train, y_train, x_test


def transfer_learning(gap_name, units=256, Optimizer='Adam', ifwrite_gap=False, image_size=None):
    """

    :param gap_name:
    :param units:
    :return:
    """
    if ifwrite_gap:
        write_gap(gap_list[gap_name][0], image_size=image_size)
    x_train, y_train, x_test = load_gap(gap_name)
    model = build_model(input_shape=x_train.shape[1:], units=units)
    model.compile(optimizer=Optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, batch_size=128, epochs=500, validation_split=0.2, verbose=2)
    return model

def write_all_gap(gap_list):
    """

    :param gap_list:
    :return:
    """
    for i in gap_list.values():
        write_gap(i[0], i[1])
    print('Done')
    return None




#adam = optimizers.Adam(lr=1e-4, decay=1e-5)