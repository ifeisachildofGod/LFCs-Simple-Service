import sys
from typing import Optional
from PyQt6.QtWidgets import (
    QScrollArea, QVBoxLayout, QWidget, QHBoxLayout
)
from PyQt6.QtCore import Qt


class BaseWidget(QWidget):
    def __init__(self, layout_type: Optional[type[QVBoxLayout] | type[QHBoxLayout]] = None):
        super().__init__()
        
        self.layout_type = layout_type or QVBoxLayout
        self._init()
    
    def _init(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(layout)
        
        self.container = QWidget()
        self.main_layout = self.layout_type(self.container)
        
        layout.addWidget(self.container)
    
    def addWidget(self, widget: QWidget, stretch: Optional[int] = None, alignment: Optional[Qt.AlignmentFlag] = None):
        kwargs = {}
        
        if stretch is not None:
            kwargs["stretch"] = stretch
        if alignment is not None:
            kwargs["alignment"] = alignment
        
        self.main_layout.addWidget(widget, **kwargs)
    
    def insertWidget(self, index: int, widget: Optional[QWidget], stretch: Optional[int] = None, alignment: Optional[Qt.AlignmentFlag] = None):
        kwargs = {}
        
        if stretch is not None:
            kwargs["stretch"] = stretch
        if alignment is not None:
            kwargs["alignment"] = alignment
        
        self.main_layout.insertWidget(index, widget, **kwargs)
    
    def addStretch(self, stretch: Optional[int] = None):
        args = []
        
        if stretch is not None:
            args.append(stretch)
        
        self.main_layout.addStretch(*args)
    
    def insertStretch(self, index: int, stretch: Optional[int] = None):
        args = [index]
        
        if stretch is not None:
            args.append(stretch)
        
        self.main_layout.insertStretch(*args)

    def getWidget(self):
        return self.container
    
    def getLayout(self):
        return self.main_layout

class BaseScrollWidget(BaseWidget):
    def __init__(self, layout_type = None):
        super().__init__(layout_type)
    
    def _init(self):
        self.scroll_widget = QScrollArea()
        self.scroll_widget.setWidgetResizable(True)
        
        self.container = QWidget()
        self.scroll_widget.setWidget(self.container)
        self.main_layout = QVBoxLayout(self.container)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(layout)
        
        layout.addWidget(self.scroll_widget)

