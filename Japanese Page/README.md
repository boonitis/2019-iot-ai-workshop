# Instruction for 2019 IOT and AI for Engineers workshop

本講座ではRaspberry Pi, PIRセンサー、Piカメラ、TensorFlow深層学習モジュールを用いてIoT画像認識システムを開発します。
PIRセンサーやPiカメラの操作のためにPython言語のプログラムを開発します。
短時間に効率よく学習させるために既に学習させたモジュール及び転移学習を利用します。そして、そのモジュールをカスタマイズします。

## Prerequisites

TensorFlowはバージョン1.9からラスベリパイのために多く利用されているのOS、Raspbianをサポートしている。今回の講座で以下のものを利用されます。

* Raspberry Pi
* Minimum 16GB SD Card
* Raspberry Pi Camera Modoule
* a PIR sensor Module
* Electronic Components
  * Jumpers
  * (Optionally) Breadboard
* Raspbian 9 (Stretch)
* Python 3.4 
* Tensorflow

## Assembling your Pi

この段階では電源アダプターをソケットに入れないでください。

1. センサーなどをラスベリパイに繋ぐために複数のポートがあります。その内、インプット・アウトプット関係のポートはGPIOポートと呼ばれます。これらを図に示されています。図に示されたようにラスベリパイにはGPIOポート以外も5V,3V,GNDなどのポートがあります。

    ![Connect a Pi Camera](https://projects-static.raspberrypi.org/projects/getting-started-with-picamera/e76b8fa9dd33f22cb9fb38908f3c01348e245447/en/images/connect-camera.jpg)

2. Using jumper cables, connect a PIR sensor to GPIO pins. Make sure that you follow the diagram accordingly. 

    ![Wiring a PIR sensor](https://projects-static.raspberrypi.org/projects/physical-computing-with-scratch/702273e5f1211f7041b6d1dc3939944cf0b99409/en/images/pir_wiring.png)

    以下の図の通りにPIRセンサーをジャンパーケーブルをラスベリパイにつなげてください

    1. Vccを5Vのポートに繋いでてください
    2. GNDを「GND」ポートに繋いでください
    3. OutをGPIO4に繋いでください
    
    ![GPIO](https://www.eletimes.com/wp-content/uploads/2017/03/Fig-9.jpg)

3. 以下の図の通りにPiカメラをシリアルインターフェイスにつなげてください

## Install and update essential packages

1. ラスベリーパイに電源を入れてください。また、ラスベリーパイをインターネットにつなげてください（WiFiを利用します）。
   
2. 以下のコマンドを利用し、Pi OSやパケッジーをアップデートしてください。

        sudo apt update
        sudo apt upgrade

3. Pythonのバージョンを確認するために以下のコマンドを利用してください。本システムのためにPython 3.4以上のインストール必要です。

        python3 --version

4. 次は TensorFlowを利用するため、 libatlasをダウンロードします。

        sudo apt install libatlas-base-dev

5. Pip3を用いてTensorFlowをインストールします。

        pip3 install tensorflow

## Setup your IoT Image Recognition System

1. GitHubからプロジェクトリポジトリをダウンロードします。

        git clone https://github.com/boonitis/2019-iot-ai-workshop.git

2. ターミナルからダウンロードフォルダに入ります

        cd /home/pi/2019-iot-ai-workshop/

3. PIRセンサーの動作を確認するためにmotion.pyプログラムを実行します。

        python3 test/motion.py

4. 次はPiカメラの動作をチェックします。

        python3 test/camera.py

5. 以下のプログラムを用いてテストします。

        python3 test/recognition.py test.jpg

   別なイメージをテストすると結果が変わる可能性があります。

        python3 test/recognition.py [path/to/image]

6. 以下のコマンドを用いて画像認識プログラムを実行させます。

        python3 run.py
    
    結果を確認してください。

## Train your own custom model

カスタマイズされた学習を行うために学習データが必要です。このURLからDownload Training Dataをクリックしてダウンロードしてください（この講座のために/home/pi/2019-iot-ai-workshop/datasetフォルダにも学習データがダウンロードされました）

早く学習させるため、既に学習させたモジュール及び転移学習を用いられます

1. ダウンロードされたファイルを/home/pi/2019-iot-ai-workshop/dataset フォルダにextractしてください。

        cd /home/pi/2019-iot-ai-workshop/
        ls
   
2. datasetフォルダに複数のサブフォルダが入ってます。各サブフォルダは人種類の動物の画像を保管しています。例： ataset/dog/は犬の画像保管しています。このようなすべてのサブフォルダを確認してください。

        ls dataset/

3. 自分のカスタマイズされたモジュールを作成するために関連クラスのデータをtrainingフォルダに移転させます。例えば、以下のコマンドを利用することによって犬の画像がtrainingフォルダに移転されます。

        mv dataset/dog training/

4. 以下のスクリプト(train.py)を用いてカスタマイズモジュールを作成できます。

        python3 train.py training/

    このコマンドを実行する時にtraining/フォルダにあるデータを利用して学習する。.

5. 学習の結果はmodels/というフォルダに保管されます。

6. IDEを用いてtrain.pyを修正することができます。これで違う種類の学習を行うことができます。以下のコマンドを利用してモデルをテストすることができます。
        python3 test/recognition

    パラメータを変えて最適なモデルを開発するために挑戦してください。
