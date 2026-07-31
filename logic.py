from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 0
    MAX_CHANNEL = 9

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.graphics_view_channel.setScene(self.scene)

        self.__graphics = "graphics/abcLogo.svg"

        pixmap = QPixmap(self.__graphics)
        pixmap = pixmap.scaled(
            self.graphics_view_channel.viewport().size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.scene.addPixmap(pixmap)

        self.__status = False
        self.__muted = False
        self.__volume = Logic.MIN_VOLUME
        self.__channel = Logic.MIN_CHANNEL
        self.__volume_b4_mute = 0

        #TODO: lambda? functions for buttons
        self.button_power.clicked.connect(self.power)
        self.button_mute.clicked.connect(self.mute)
        self.button_channel_up.clicked.connect(self.channel_up)
        self.button_channel_down.clicked.connect(self.channel_down)
        self.button_volume_up.clicked.connect(self.volume_up)
        self.button_volume_down.clicked.connect(self.volume_down)


    def power(self):
        """
        Turns the television on and off.
        """
        if not self.__status:
            self.__status = True
            #TODO: turn ON graphics
            self.progress_bar_volume.setValue(self.__volume)

        else:
            self.__status = False
            # TODO: turn OFF graphics
            self.progress_bar_volume.setValue(0)


    def mute(self):
        """
        Mutes the television.
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__volume_b4_mute = self.__volume
                self.__volume = Logic.MIN_VOLUME
                self.progress_bar_volume.setValue(self.__volume)

            else:
                self.__muted = False
                self.__volume = self.__volume_b4_mute
                self.progress_bar_volume.setValue(self.__volume)


    def channel_up(self):
        """
        Turns the channel up.
        """
        if self.__status:
            if self.__channel == Logic.MAX_CHANNEL:
                self.__channel = Logic.MIN_CHANNEL
                #TODO: change graphic

            else:
                self.__channel += 1
                # TODO: change graphic


    def channel_down(self):
        """
        Turns the channel down.
        """
        if self.__status:
            if self.__channel == Logic.MIN_CHANNEL:
                self.__channel = Logic.MAX_CHANNEL
                # TODO: change graphic

            else:
                self.__channel -= 1
                # TODO: change graphic


    def volume_up(self):
        """
        Turns the volume up.
        """
        if self.__status:
            if self.__muted:
                self.mute()

            if self.__volume < Logic.MAX_VOLUME:
                self.__volume += 1
                self.progress_bar_volume.setValue(self.__volume)


    def volume_down(self):
        """
        Turns the volume down.
        """
        if self.__status:
            if self.__muted:
                self.mute()

            if self.__volume > Logic.MIN_VOLUME:
                self.__volume -= 1
                self.progress_bar_volume.setValue(self.__volume)