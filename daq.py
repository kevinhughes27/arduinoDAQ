#!/usr/bin/env python

import os, platform
import time
import numpy as np
import wx
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
from arduino import Arduino

local_platf = platform.system()

if local_platf == 'Linux':
    arduino_port = '/dev/ttyACM0'
if local_platf == 'Windows':
    # For Windows
    arduino_port = 'COM4'
else:
    # Error windows. No Mac version yet

    print ("No Mac version implemented yet. Default to Linux.")
    arduino_port = '/dev/ttyACM0'

class MainWindow(wx.Frame):
    """ Main frame of the application
    """

    title = 'Data Acquisition'


    def __init__(self):
        wx.Frame.__init__(self, None, title=self.title, size=(650,570))

        local_platf = platform.system()
        if local_platf == 'Linux':
            arduino_port = '/dev/ttyACM0'
        if local_platf == 'Windows':
            # For Windows
            arduino_port = 'COM4'
        else:
            # Error windows. No Mac version yet
            msg = wx.MessageDialog(self, 'No Mac version implemented yet. Default to Linux.', 'Warning', wx.OK | wx.ICON_WARNING)
            msg.ShowModal() == wx.ID_YES
            msg.Destroy()
            arduino_port = '/dev/ttyACM0'

        # Try Arduino
        try:
            self.arduino = Arduino(arduino_port, 115200)
        except:
            msg = wx.MessageDialog(self, 'Unable to connect to arduino. Check port or connection.', 'Error', wx.OK | wx.ICON_ERROR)
            msg.ShowModal() == wx.ID_YES
            msg.Destroy()

        self.create_main_panel()

        self.recording = False
        self.output_file = ''

        time.sleep(1)

        # Timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.rate = 500
        self.timer.Start(self.rate)


    def create_main_panel(self):

        # Panels
        self.plots_panel = wx.Panel(self)
        self.record_panel = wx.Panel(self)

        # Init Plots
        self.init_plots()
        self.PlotsCanvas = FigCanvas(self.plots_panel, wx.ID_ANY, self.fig)

        # Recording
        self.btn_record = wx.Button(self.record_panel, wx.ID_ANY, label="Record", pos=(500,20), size=(100,30))
        self.Bind(wx.EVT_BUTTON, self.on_btn_record, self.btn_record)
        self.Bind(wx.EVT_UPDATE_UI, self.on_update_btn_record, self.btn_record)

        self.txt_output_file = wx.TextCtrl(self.record_panel, wx.ID_ANY, pos=(20,20), size=(440,30))

        # Sizers
        vertical = wx.BoxSizer(wx.VERTICAL)
        vertical.Add(self.plots_panel, 0 , wx.ALL, 5)
        vertical.Add(self.record_panel, 0 , wx.ALL, 5)

        # Layout
        self.SetAutoLayout(True)
        self.SetSizer(vertical)
        self.Layout()


    def init_plots(self):
        self.plotMem = 50 # how much data to keep on the plot
        self.plotData = [[0] * (6)] * self.plotMem # mem storage for plot

        self.fig = Figure((8,6))
        self.fig.subplots_adjust(hspace=.5) # sub plot spacing

        self.axes = [] # subplot list
        for i in range(1,7):
            self.axes.append(self.fig.add_subplot(3,2,i, xticks=[], yticks=[0, 500, 1000]))


    def poll(self):
        self.dataRow = self.arduino.poll()


    def save(self):
        file = open(self.output_file, 'a')
        for i in range(0,5):
            file.write(str(self.dataRow[i]) + ',')
        file.write(str(self.dataRow[5]) + '\n')
        file.close()


    def draw(self):
        self.plotData.append(self.dataRow) # adds to the end of the list
        self.plotData.pop(0) # remove the first item in the list, ie the oldest

        # Plot
        x = np.asarray(self.plotData)

        for (i, ax) in enumerate(self.axes):
            ax.plot(range(0,self.plotMem), x[:,i],'k')
            ax.set_title('CH A'+str(i))
            ax.set_ylim(0,1000)
            ax.set_yticks([0, 250, 500, 750, 1000])
            ax.set_xticks([])
            ax.hold(False)

        # draw
        self.PlotsCanvas.draw()


    def on_timer(self, event):
        self.poll()

        if self.recording:
            self.save()

        self.draw()


    def on_update_btn_record(self, event):
        label = "Stop" if self.recording else "Record"
        self.btn_record.SetLabel(label)

    def on_btn_record(self, event):

        # pause timer
        self.timer.Stop()

        # switch state
        self.recording = not self.recording

        # if recording
        if self.recording:

            # check that a dir has been specified
            if self.txt_output_file.IsEmpty():

                msg = wx.MessageDialog(self, 'Specify the Output Directory', 'Error', wx.OK | wx.ICON_ERROR)
                msg.ShowModal() == wx.ID_YES
                msg.Destroy()

                self.recording = False

            else:
                self.output_file = self.txt_output_file.GetLineText(0)

                # check if file exists - ie may be saving over data
                if os.path.isfile(self.output_file):
                    msg = wx.MessageDialog(self, 'Output File %s Exists - Overwrite Data?' %self.output_file, 'Yes or No', wx.YES_NO | wx.ICON_QUESTION)
                    result = msg.ShowModal() == wx.ID_YES
                    msg.Destroy()

                    # overwrite the data
                    if result == True:

                        # delete the file
                        os.remove(self.output_file)

                        # make new file
                        open(self.output_file, 'w').close()

                    # do not overwrite the data
                    else: # result == False
                        self.recording = False
                        self.txt_output_file.SetFocus()

                # no file so make one
                else:
                    open(self.output_file, 'w').close()

        # un pause timer
        self.timer.Start(self.rate)

        return


    def on_exit(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    app.frame = MainWindow()
    app.frame.Show()
    app.MainLoop()
