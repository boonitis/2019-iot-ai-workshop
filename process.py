from __future__ import absolute_import, division, print_function

import os
import subprocess

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import PIL.Image as Image
import os
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

command = "ssh -t boon@192.168.11.12 'rm -rf /home/boon/Desktop/2019-iot-ai-workshop/training/*'"
os.system(command)
result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
data_root = tf.keras.utils.get_file(
    'flower_photos','/home/boon/Desktop/2019-iot-ai-workshop/training/',
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

feature_extractor_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/feature_vector/2" #@param {type:"string"}

def feature_extractor(x):
    feature_extractor_module = hub.Module(feature_extractor_url)
    return feature_extractor_module(x)

IMAGE_SIZE = hub.get_expected_image_size(hub.Module(feature_extractor_url))

image_data = image_generator.flow_from_directory(str(data_root), target_size=IMAGE_SIZE)
for image_batch,label_batch in image_data:
    print("Image batch shape: ", image_batch.shape)
    print("Labe batch shape: ", label_batch.shape)
    break

image_data = image_generator.flow_from_directory(str(data_root), target_size=IMAGE_SIZE)
for image_batch,label_batch in image_data:
    print("Image batch shape: ", image_batch.shape)
    print("Labe batch shape: ", label_batch.shape)
    break

features_extractor_layer = layers.Lambda(feature_extractor, input_shape=IMAGE_SIZE+[3])

features_extractor_layer.trainable = False

model = tf.keras.Sequential([
  features_extractor_layer,
  layers.Dense(image_data.num_classes, activation='softmax')
])
model.summary()

init = tf.global_variables_initializer()
sess.run(init)

result = model.predict(image_batch)
result.shape

model.compile(
    optimizer=tf.train.AdamOptimizer(), 
    loss='categorical_crossentropy',
    metrics=['accuracy'])

class CollectBatchStats(tf.keras.callbacks.Callback):
    def __init__(self):
        self.batch_losses = []
        self.batch_acc = []
    
    def on_batch_end(self, batch, logs=None):
        self.batch_losses.append(logs['loss'])
        self.batch_acc.append(logs['acc'])

steps_per_epoch = image_data.samples//image_data.batch_size
batch_stats = CollectBatchStats()
model.fit((item for item in image_data), epochs=1, 
                    steps_per_epoch=steps_per_epoch,
                    callbacks = [batch_stats])

label_names = sorted(image_data.class_indices.items(), key=lambda pair:pair[1])
label_names = np.array([key.title() for key, value in label_names])
label_names

result_batch = model.predict(image_batch)

labels_batch = label_names[np.argmax(result_batch, axis=-1)]
labels_batch

export_path = tf.contrib.saved_model.save_keras_model(model, "./saved_models")
export_path