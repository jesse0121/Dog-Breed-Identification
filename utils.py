from keras.applications import *


train_path = 'D:\\Competition\\Dog-Breed-Identification\\Data\\train'
test_path = 'D:\\Competition\\Dog-Breed-Identification\\Data\\test'
sample_submission_path = 'D:\\Competition\\Dog-Breed-Identification\\Data\\sample_submission.csv'
label_path = 'D:\\Competition\\Dog-Breed-Identification\\Data\\labels.csv'
Data_path = 'D:\\competition\\Dog-Breed-Identification\\Data'
h5_path = 'D:\\competition\\Dog-Breed-Identification\\Data\\h5'

gap_list = {'VGG16': (VGG16, (224, 224)),
            'VGG19': (VGG19, (224, 224)),
            'ResNet50': (ResNet50, (224, 224)),
            'Xception': (Xception, (299, 299)),
            'InceptionV3': (InceptionV3, (299, 299)),
            'InceptionResNetV2': (InceptionResNetV2, (299, 299)),
            'NASNetLarge': (NASNetLarge, (331, 331)),
            'DenseNet121': (DenseNet121, (224, 224)),
            'DenseNet169': (DenseNet169, (224, 224)),
            'DenseNet201': (DenseNet201, (224, 224)),
            'MobileNet': (MobileNet, (224, 224)),
            'NASNetMobile': (NASNetMobile, (224, 224))}