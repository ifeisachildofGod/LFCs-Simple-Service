
from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu
)
from PyQt6.QtCore import QPoint, Qt

from base_widgets import *
from helper_widgets import *


class IconToolOption(BaseWidget):
    def __init__(self, icon_path: str, width: Optional[int], height: Optional[int], font_size: Optional[int], content: Callable | dict[str, Callable | dict[str, Callable]] | tuple[QWidget, float], title: str | None = None):
        super().__init__()
        
        self.content = content
        
        STYLESHEET = f"""
            QWidget.IconToolOption {{
                background-color: transparent
            }}
            
            QWidget.IconToolOption:pressed {{
                background-color: #f0f50f
            }}
            
            QWidget.IconToolOption:hover {{
                background-color: #0f5ff0
            }}
            
            QWidget.IconToolOption QWidget._TopWidget QLabel {{
                font-size: {font_size}px
            }}
            QWidget.IconToolOption QLabel {{
                font-size: {font_size}px
            }}
        """
        self.getLayout().setContentsMargins(5, 10, 5, 10)
        
        self.getWidget().setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.getWidget().setProperty("class", "IconToolOption")
        self.getWidget().setStyleSheet(STYLESHEET)
        
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
    
    def _clicked(self, a0):
        pos = self.mapToGlobal(QPoint(self.getWidget().x(), self.getWidget().y() + self.getWidget().rect().height() - self.getWidget().contentsMargins().bottom()))
        
        if isinstance(self.content, Callable):
            return self.content()
        elif isinstance(self.content, dict):
            menu = self._getMenu(self, self.content)
            
            menu.exec(pos)
        else:
            widget, offset_factor = self.content
            offset = widget.rect().width() - self.getWidget().width()
            
            widget.setWindowFlags(Qt.WindowType.Popup)
            
            widget.move(pos - QPoint(int(offset - offset * (offset_factor + 1) / 2), 0))
            widget.show()
        
        self.update()
    
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
        
    
    


