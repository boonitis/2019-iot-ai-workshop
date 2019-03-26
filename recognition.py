from __future__ import absolute_import, division, print_function

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import PIL.Image as Image
from tensorflow.keras import layers

##################################################################################
"""call this module to setup your python packages via pip"""

from pip._internal import main as pip

pip_install_argument = "install"

# packages to install
packages_to_install = [
        "numpy",        # math magic 1
        "scipy",        # math magic 2
        "tensorflow_hub",
        ]

def install(packages):
    """installes given packages via pip

    Args:
        package names as list

    Returns:
        None

    """
    global pip_install_argument
    for package in packages:
        pip([pip_install_argument, package])

install(packages_to_install)

###########################################################


data_root = tf.keras.utils.get_file(
    'flower_photos','/home/boon/Desktop/2019-iot-ai-workshop/flower_photos/',
    untar=True)

image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
image_data = image_generator.flow_from_directory(str(data_root))

for image_batch,label_batch in image_data:
    print("Image batch shape: ", image_batch.shape)
    print("Labe batch shape: ", label_batch.shape)
    break

classifier_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/2" #@param {type:"string"}

def classifier(x):
    classifier_module = hub.Module(classifier_url)
    return classifier_module(x)
  
IMAGE_SIZE = hub.get_expected_image_size(hub.Module(classifier_url))

classifier_layer = layers.Lambda(classifier, input_shape = IMAGE_SIZE+[3])
classifier_model = tf.keras.Sequential([classifier_layer])
classifier_model.summary()

image_data = image_generator.flow_from_directory(str(data_root), target_size=IMAGE_SIZE)
for image_batch,label_batch in image_data:
    print("Image batch shape: ", image_batch.shape)
    print("Labe batch shape: ", label_batch.shape)
    break

import tensorflow.keras.backend as K
sess = K.get_session()
init = tf.global_variables_initializer()

sess.run(init)



########################################################

grace_hopper = tf.keras.utils.get_file('monkey.jpg','file://home/boon/Desktop/2019-iot-ai-workshop/test/')
grace_hopper = Image.open(grace_hopper).resize(IMAGE_SIZE)
grace_hopper 

grace_hopper = np.array(grace_hopper)/255.0
grace_hopper.shape

result = classifier_model.predict(grace_hopper[np.newaxis, ...])
result.shape

predicted_class = np.argmax(result[0], axis=-1)
predicted_acc = str(100)
predicted_class

labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())


result = imagenet_labels[predicted_class] + " : " + predicted_acc

print("\nClassification Result")
print(result)