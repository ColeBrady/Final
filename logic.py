from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    #Class constants
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 0
    MAX_CHANNEL = 9

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        #Sets up graphics view widget
        self.scene = QGraphicsScene()
        self.graphics_view_channel.setScene(self.scene)

        #list of graphics
        self.__graphics = [
            'graphics/abcLogo.svg',
            'graphics/FoodNetworkLogo.svg',
            'graphics/TBSLogo.svg',
            'graphics/DiscoveryChannelLogo.png',
            'graphics/NBCLogo.jpeg',
            'graphics/HistoryChannelLogo.svg',
            'graphics/FoxLogo.svg',
            'graphics/CartoonNetworkLogo.png',
            'graphics/NickelodeonLogo.jpg',
            'graphics/TNTLogo.svg'
        ]

        #Set initial values
        self.__status = False
        self.__muted = False
        self.__volume = Logic.MIN_VOLUME
        self.__channel = Logic.MIN_CHANNEL
        self.__volume_b4_mute = 0

        #Specify what to do when buttons are clicked
        self.button_power.clicked.connect(self.power)
        self.button_mute.clicked.connect(self.mute)
        self.button_channel_up.clicked.connect(self.channel_up)
        self.button_channel_down.clicked.connect(self.channel_down)
        self.button_volume_up.clicked.connect(self.volume_up)
        self.button_volume_down.clicked.connect(self.volume_down)


    def power(self) -> None:
        """
        Turns the television on and off.
        """
        if not self.__status:
            self.__status = True
            self.update_channel_graphic()
            self.progress_bar_volume.setValue(self.__volume)

        else:
            self.__status = False
            self.scene.clear()
            self.progress_bar_volume.setValue(0)


    def mute(self) -> None:
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


    def channel_up(self) -> None:
        """
        Turns the channel up.
        """
        if self.__status:
            if self.__channel == Logic.MAX_CHANNEL:
                self.__channel = Logic.MIN_CHANNEL
                self.update_channel_graphic()

            else:
                self.__channel += 1
                self.update_channel_graphic()


    def channel_down(self) -> None:
        """
        Turns the channel down.
        """
        if self.__status:
            if self.__channel == Logic.MIN_CHANNEL:
                self.__channel = Logic.MAX_CHANNEL
                self.update_channel_graphic()

            else:
                self.__channel -= 1
                self.update_channel_graphic()


    def volume_up(self) -> None:
        """
        Turns the volume up.
        """
        if self.__status:
            if self.__muted:
                self.mute()

            if self.__volume < Logic.MAX_VOLUME:
                self.__volume += 1
                self.progress_bar_volume.setValue(self.__volume)


    def volume_down(self) -> None:
        """
        Turns the volume down.
        """
        if self.__status:
            if self.__muted:
                self.mute()

            if self.__volume > Logic.MIN_VOLUME:
                self.__volume -= 1
                self.progress_bar_volume.setValue(self.__volume)


    def update_channel_graphic(self) -> None:
        """
        Changes the channel graphic
        """
        self.scene.clear()

        graphic = QPixmap(self.__graphics[self.__channel])

        graphic = graphic.scaled(
            self.graphics_view_channel.viewport().size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.scene.addPixmap(graphic)