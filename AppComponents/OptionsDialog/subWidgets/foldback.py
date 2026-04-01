

from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu, QCheckBox, QPushButton,
    QStackedWidget
)
from PyQt6.QtCore import QPoint, Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

from UIComponents.TabView import TabView_2
from UIComponents.SideBar import SideBar

from helper_widgets import *

from AppComponents.OptionsDialog._base_widgets import *
from AppComponents.OptionsDialog.subWidgets.main_output import _Song, _Scripture


class _General(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        self.addWidget(SeparatorLabel("Enable Display Foldback"))
        self.addWidget(SeparatorLabel("Select Output Monitor"))
        self.addWidget(SeparatorLabel("Default Fonts"))
        self.addWidget(SeparatorLabel("Next Item Information"))
        self.addWidget(SeparatorLabel("Screen Margins"))
        self.addStretch()

class _Alerts_Clocks(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        self.addWidget(SeparatorLabel("Clock Options"))
        self.addWidget(SeparatorLabel("Service Interval Options"))
        self.addWidget(SeparatorLabel("Message Alert Options"))
        self.addStretch()


class Foldback(TabView_2):
    def __init__(self):
        content = {
            "General": _General(),
            "Song": _Song(),
            "Scripture": _Scripture(),
            "Alerts and Clocks": _Alerts_Clocks(),
        }
        
        super().__init__(content)
