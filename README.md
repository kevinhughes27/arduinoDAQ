ArduinoDAQ
==========

by: Kevin Hughes, June 2013


![usage](https://kevinhughes27.files.wordpress.com/2013/06/arduino_daq_test.png)

Description
-----------

usage:
load the ArduinoDAQ program on the Arduino then run the main python program:
  python daq.py

An Arduino program which reads the analog pins and sends the data over the serial port to the computer. A GUI written in python is provided for viewing the data from the arduino in real-time and saving the data to hard disk as csv.


Requirements
------------

wx python
  sudo apt-get install python-wx

py serial
  sudo apt-get install python-serial

matplotlib
  sudo apt-get install python-matplotlib


OSX Install Instructions:
http://rwsarduino.blogspot.ca/2013/07/python-arduino-daq-on-mac.html
