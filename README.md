# Instruction for 2019 IOT and AI for Engineers workshop

In this workshop, we use Raspberry Pi with a motion sensor and a camera to create IoT image recognition system. 

We use Python to control GPIO that connects a motion sensor (PIR Sensor) and a camera module (Pi Camera). 

Image recognition is handled by TensorFlow.

## Prerequisites

The TensorFlow announced official support for Raspberry Pi, from Version 1.9 it will support Raspberry Pi using pip package installation. We will see how to install it on our Raspberry Pi in this tutorial.

* Raspberry Pi
* Minimum 16GB SD Card
* Raspberry Pi Camera Modoule
* PIR Sensor Module
* Electronic Components
  * Jumpers
  * (Optionally) Breadboard
* Raspbian 9 (Stretch)
* Python 3.4 
* Tensorflow

## Assembling your Pi

DO NOT POWER UP YOUR PI DURING THIS SECTION.

1. 

## Installing Raspbian 9 and essential packages

We have to install Raspbian 9 (Stretch) and setup working environment. 

1. Insert prepared SD card to your Rasppbery Pi and connect a power supply to turn it on.

2. Install Raspbian 9 with [NOOBS Installer](https://www.raspberrypi.org/downloads/noobs/) downloaded from the official website. 

3. When the installation finish, you'll arrive at the desktop. Open the terminal.
   
4. Update your Pi and its packages. Using the following commands.

        sudo apt update
        sudo apt upgrade

5. Ensure that you have latest Python version, using the following command. 

        python3 --version

    At least Python 3.4 is recommended.

6. Install *libatlas* library. Which is required by Tensorflow.

        sudo apt install libatlas-base-dev

7. Install TensorFlow using Pip3.

        pip3 install tensorflow

## IoT Image Recognition System

1. Download [the project repository from GitHub](https://github.com/boonitis/2019-iot-ai-workshop), or clone it using the command. 

        git clone https://github.com/boonitis/2019-iot-ai-workshop.git

2. In the terminal, go to the downloaded directory.

        cd /home/pi/2019-iot-ai-workshop/

3. Run the following command test the motion sensor.

        python3 test/motion.py

4. Run the following command to test the camera module.

        python3 test/camera.py

5. Run this command to test the model prediction.

        python3 test/recognition.py test.jpg

    You can try this command on other images to see different results.

        python3 test/recognition.py [path/to/image]

6. Finally, run the image recognition system using this command.

        python3 run.py
    
    Check the results.

## Training your own model

To train a custom model, first of all, you need training data. Go to this link and click on **DOWNLOAD TRAINING DATA**. (NOTED: During the workshop, the training data are already provided at */home/pi/2019-iot-ai-workshop/dataset*)

Using pre-trained MobileNet and Transfer Learning, we can train a new custom model very quickly.

1. Extract the downloaded file to */home/pi/2019-iot-ai-workshop/dataset*. Go to the project directory.

        cd /home/pi/2019-iot-ai-workshop/
        ls
   
2. Each directory in *dataset/* is a target class and should contain related images. For example *dataset/dog/* is for *dog* class and it should contain only dog images. Try listing every directory using this command.

        ls dataset/

3. To train a custom model, you can use provided script.

        python3 train.py

    This command will use training data in *dataset/* to train a model.

4. The training output will be available at *models/*

5. Using any IDE, open train.py and modify its *PARAMETERS* to train different type of model. Rembember that you can test the model with this command.

    python3 test/recognition

