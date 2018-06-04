ArduinoDAQ
==========

by: Kevin Hughes, June 2013
updated by: Victor H. Martin, June 2018


![usage](http://kevinhughes.ca/images/posts/arduino_daq_test.png)

Description
-----------
Updated for running with Python 3.

usage:
load the ArduinoDAQ program on the Arduino then run the main python program:
  python daq.py

An Arduino program which reads the analog pins and sends the data over the serial port to the computer. A GUI written in python is provided for viewing the data from the arduino in real-time and saving the data to hard disk as csv.


Requirements
------------

Dependencies file requirement.txt is provided for easy installation of dependencies using PiP. If you have pip installed
run the next command in python command line:

pip install -r requirements.txt

The main packages required (dependencies of these libraries would be automatically installed) are the following:

wx python
  sudo apt-get install python-wx

py serial
  sudo apt-get install python-serial

matplotlib
  sudo apt-get install python-matplotlib


OSX Install Instructions:
http://rwsarduino.blogspot.ca/2013/07/python-arduino-daq-on-mac.html
