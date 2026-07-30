from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__volume_b4_mute = 0

        #TODO: lambda? functions for buttons
        self.button_power.clicked.connect(self.power)


    def power(self):
        """
        Turns the television on and off.
        """
        if not self.__status:
            self.__status = True
            #TODO: turn ON volume bar and graphics
            self.label_volume.setText("On") #TODO: Delete

        else:
            self.__status = False
            # TODO: turn OFF volume bar and graphics
            self.label_volume.setText("Off") #TODO: Delete