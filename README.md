# real_time_face_recognition
This project can realize real-time face recognition

下面是如何使用该项目的文件：

1.首先在本地搭建好tensorflow深度学习框架，安装opencv3;

2.git clone本项目到本地：git clone https://github.com/wanggs950730/real_time_face_recognition.git;

3.将要识别的人的图片（30张，数目越多识别越精确）放入以该人名命名的文件夹中，再将这些（多个人就将多个文件夹）放入picture文件夹中;

4.在终端执行python classifier.py TRAIN  /20180402-114759 /picture /myclassifier.py 
(训练人脸识别分类器，picture文件夹中有几个人，之后将会识别到几个人（即按人名分类）

5.在终端执行 python real_time_face_recognition.py 进行人脸实时识别。（人脸检测模型及识别模型都已训练好）
（opencv3安装无误，就会出现opencv调用的视频框，在视频框中识别出现的人脸）
