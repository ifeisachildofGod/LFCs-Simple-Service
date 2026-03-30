

from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu
)
from PyQt6.QtCore import QPoint, Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

from UIComponents.SideBar import SideBar

from base_widgets import *
from helper_widgets import *


class OptionsDialog(BaseDialogWidget):
    def __init__(self):
        super().__init__("Options", QHBoxLayout)
        
        self.addWidget(
            SideBar(
                [
                    ("Media Output", print),
                    ("Alternate Output", print),
                    ("Foldback", print),
                    None,
                    ("Service Intervals", print),
                    None,
                    ("Advanced", print),
                ]
            )
        )


