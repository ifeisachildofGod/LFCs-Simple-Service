

from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu, QCheckBox, QPushButton,
    QStackedWidget
)
from PyQt6.QtCore import QPoint, Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

from UIComponents.TabView import TabView_2

from helper_widgets import *

from AppComponents.OptionsDialog._base_widgets import *
from AppComponents.OptionsDialog.subWidgets.main_output import _General, _Song, _Scripture, _Presentation, _Transition, _Alerts

class _A_General(_General):
    def __init__(self):
        super().__init__()
        
        esfdao_widget = BaseWidget()
        esfdao_cbx = QCheckBox("Enable Support for display Alternate Output") ; esfdao_widget.addWidget(esfdao_cbx)
        
        self.insertWidget(0, esfdao_widget)
        self.insertWidget(0, SeparatorLabel("Enable Display Alternate Output"))

class AltenateOutput(TabView_2):
    def __init__(self):
        content = {
            "General": _A_General(),
            "Song": _Song(),
            "Scripture": _Scripture(),
            "Presentation": _Presentation(),
            "Transition": _Transition(),
            "Alerts": _Alerts(),
        }
        
        super().__init__(content)

