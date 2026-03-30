
import time
from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu
)
from PyQt6.QtCore import QPoint, QTimer, Qt

from base_widgets import *
from helper_widgets import *


class IconToolBarOption(BaseWidget):
    def __init__(self, icon_path: str, width: Optional[int], height: Optional[int], font_size: Optional[int], content: Callable | dict[str, Callable | dict[str, Callable]] | tuple[QWidget, float], title: str | None = None):
        super().__init__()
        
        self.content = content
        
        self.HOVER_STYLESHEET = """
            QWidget.IconToolBarOption:hover {
                background-color: #31456b
            }
        """
        
        self.STYLESHEET = f"""
            QWidget.IconToolBarOption {{
                background-color: transparent
            }}
            
            {self.HOVER_STYLESHEET}
            
            QWidget.IconToolBarOption QWidget._TopWidget QLabel {{
                font-size: {font_size}px
            }}
            QWidget.IconToolBarOption QLabel {{
                color: white;
                font-size: {font_size}px
            }}
        """
        
        self.getLayout().setSpacing(0)
        self.getLayout().setContentsMargins(15, 5, 15, 5)
        
        self.getWidget().setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.getWidget().setProperty("class", "IconToolBarOption")
        self.getWidget().setStyleSheet(self.STYLESHEET)
        
        topWidget = BaseWidget(QHBoxLayout)
        topWidget.getLayout().setContentsMargins(0, 0, 0, 0)
        topWidget.setProperty("class", "_TopWidget")
        topWidget.addWidget(Image(icon_path, width, height))
        if not isinstance(content, Callable):
            topWidget.addWidget(QLabel("▼"))
        
        self.addWidget(topWidget)
        if title is not None:
            self.addWidget(QLabel(title), alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.getWidget().mousePressEvent = self._clicked
        
        if not isinstance(self.content, Callable) and not isinstance(self.content, dict):
            widget, _ = self.content
            
            def hide_event(_):
                self.getWidget().setStyleSheet(self.STYLESHEET)
                self.update()
            
            widget.hideEvent = hide_event
    
    def _clicked(self, a0):
        pos = self.mapToGlobal(QPoint(self.getWidget().x(), self.getWidget().y() + self.getWidget().rect().height() - self.getWidget().contentsMargins().bottom()))
        
        if isinstance(self.content, Callable):
            return self.content()
        else:
            self.getWidget().setStyleSheet(self.STYLESHEET.replace(self.HOVER_STYLESHEET, "") + "QWidget.IconToolBarOption {background-color: #30446a}")
            self.update()
            
            if isinstance(self.content, dict):
                menu = self._getMenu(self, self.content)
                
                menu.exec(pos)
                
                self.getWidget().setStyleSheet(self.STYLESHEET)
                self.update()
            else:
                widget, offset_factor = self.content
                offset = widget.rect().width() - self.getWidget().width()
                
                widget.setWindowFlags(Qt.WindowType.Popup)
                
                widget.move(pos - QPoint(int(offset - offset * (offset_factor + 1) / 2), 0))
                widget.show()
    
    def _getMenu(self, parent: QMenu | BaseWidget, content: dict, name: Optional[str] = None):
        args = [parent]
        if name is not None:
            args.insert(0, name)
        
        menu = QMenu(*args)
        
        for optionName, optionAction in content.items():
            if optionName is None:
                menu.addSeparator()
            elif isinstance(optionAction, Callable):
                menu.addAction(optionName, optionAction)
            else:
                menu.addMenu(self._getMenu(menu, optionAction, optionName))
        
        return menu
        
    
    


