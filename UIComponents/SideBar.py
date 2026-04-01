
from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu
)
from PyQt6.QtCore import QPoint, Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

from helper_widgets import *


class _SideBarOption(BaseWidget):
    SELECTED_STYLESHEET = f"""
        QWidget.SideBarOption {{
            background-color: {PALETTE["selected"]};
        }}
        
        QLabel {{
            color: {PALETTE["text-1"]};
            font-weight: 500;
        }}
    """
    
    UNSELECTED_STYLESHEET = f"""
        QWidget.SideBarOption {{
            background-color: transparent;
        }}
        
        QWidget.SideBarOption:hover {{
            background-color: {PALETTE["hover-2"]};
        }}
        
        QLabel {{
            color: {PALETTE["text-main"]};
        }}
    """
    
    def __init__(self, name: str, do_action: Callable):
        super().__init__(QHBoxLayout)
        
        self.setProperty("class", "SideBarOption")
        self.setStyleSheet(self.UNSELECTED_STYLESHEET)
        
        self.setSpacing(0)
        self.setContentsMargins(10, 8, 10, 8)
        
        self.do_action = do_action
        
        self.addWidget(QLabel(name))
        self.getWidget().mousePressEvent = lambda _: self._clicked(True)
    
    def _clicked(self, do: bool):
        if do:
            self.setStyleSheet(self.SELECTED_STYLESHEET)
            self.do_action()
        else:
            self.setStyleSheet(self.UNSELECTED_STYLESHEET)


class SideBar(BaseWidget):
    STYLESHEET = """
        QWidget.SideBar {
            background-color: #2c2c2c;
        }
    """
    
    def __init__(self, content: list[tuple[str | None, Callable] | None]):
        super().__init__()
        
        self.widgets = []
        
        self.setFixedWidth(210)
        
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)
        self.setProperty("class", "SideBar")
        self.setStyleSheet(self.STYLESHEET)
        
        for index, data in enumerate(content):
            name, action = data if data is not None else (None, None)
            
            option = (
                _SideBarOption(name, self._mf_option_changed(index, action))
                if name is not None else
                SeperatorWidget(Qt.Orientation.Vertical, 10, None, 1, "#9b9b9b")
            )
                
            self.widgets.append(option)
            self.addWidget(option)
        
        for widget in self.widgets:
            if isinstance(widget, _SideBarOption):
                widget._clicked(True)
                
                break
        
        self.addStretch()
    
    def _mf_option_changed(self, index: int, action: Callable):
        def func():
            action()
            
            if hasattr(self, "curr_widget"):
                self.curr_widget._clicked(False)
            
            self.curr_widget = self.widgets[index]
        
        return func


