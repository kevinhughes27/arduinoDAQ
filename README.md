ArduinoDAQ
==========

by: Kevin Hughes, June 2013


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
