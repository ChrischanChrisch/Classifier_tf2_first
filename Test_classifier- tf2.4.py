import numpy as np
import glob
import os
import tensorflow as tf
from keras.preprocessing import image as k_image

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)
# loading the best perfoming model
model = tf.keras.models.load_model(r'C:\Tensorflow2\workspace\Classifier\models\model_stripes.h5')

# Getting test accuracy and loss
#test_loss, test_acc = model.evaluate(test_generator)
#print('Test loss: {} Test Acc: {}'.format(test_loss, test_acc))

Folder = ['Empty', 'Full']  # all Categories-Folders
for fo in Folder:
    pfad = os.path.join(r'C:\Tensorflow2\workspace\Classifier\Training_imgs\test', fo, '*.jpg')
    test_images = glob.glob(pfad)
    # print(test_images)
    for image in test_images:
        test_image = k_image.load_img(image, target_size=(180, 25))

        # convert image to numpy array
        images = k_image.img_to_array(test_image)
        # expand dimension of image
        images = np.expand_dims(images, axis=0)
        # making prediction with model
        prediction = model.predict(images)

        if prediction == 0:
            print(image, ' detected as Empty')
        else:
            print(image, ' detected as Full')