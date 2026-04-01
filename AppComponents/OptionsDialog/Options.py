

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

from AppComponents.OptionsDialog.subWidgets.main_output import MainOutput
from AppComponents.OptionsDialog.subWidgets.alternate_output import AltenateOutput
from AppComponents.OptionsDialog.subWidgets.foldback import Foldback
from AppComponents.OptionsDialog.subWidgets.service_intervals import ServiceIntervals
from AppComponents.OptionsDialog.subWidgets.advanced import Advanced

from helper_widgets import *


class OptionsDialog(BaseDialogWidget):
    STYLESHEET = f""" """
    
    def __init__(self):
        super().__init__("Options", QVBoxLayout)
        
        self._initGeom()
        
        self.setProperty("class", "OptionsDialog")
        self.setStyleSheet(self.STYLESHEET)
        
        central_widget = QStackedWidget()
        
        central_widget.addWidget(MainOutput())
        central_widget.addWidget(AltenateOutput())
        central_widget.addWidget(Foldback())
        central_widget.addWidget(ServiceIntervals())
        central_widget.addWidget(Advanced())
        
        main_widget = BaseWidget(QHBoxLayout)
        base_widget = BaseWidget(QHBoxLayout)
        
        main_widget.addWidget(
            SideBar(
                [
                    ("Media Output", lambda: central_widget.setCurrentIndex(0)),
                    ("Alternate Output", lambda: central_widget.setCurrentIndex(1)),
                    ("Foldback", lambda: central_widget.setCurrentIndex(2)),
                    None,
                    ("Service Intervals", lambda: central_widget.setCurrentIndex(3)),
                    None,
                    ("Advanced", lambda: central_widget.setCurrentIndex(4)),
                ]
            )
        )
        main_widget.addWidget(central_widget)
        
        preview = QCheckBox("Preview Output")
        ok_button = PushButton("OK")
        cancel_button = PushButton("Cancel")
        
        base_widget.addWidget(preview)
        base_widget.addStretch()
        base_widget.addWidget(ok_button)
        base_widget.addWidget(cancel_button)
        
        self.addWidget(main_widget)
        self.addWidget(base_widget)
    
    def _initGeom(self):
        width = 800
        height = 500
        
        screen_geom = self.screen().geometry()
        
        self.setGeometry(int(screen_geom.width() / 2 - width / 2), int(screen_geom.height() / 2 - height / 2), width, height)


