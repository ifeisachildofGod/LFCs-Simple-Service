
import time
from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu
)
from PyQt6.QtCore import QPoint, QTimer, Qt

from helper_widgets import *


class IconToolBarOption(BaseWidget):
    def __init__(self, icon_path: Optional[str], width: Optional[int], height: Optional[int], font_size: Optional[int], content: Callable | list[tuple[str, Callable | dict[str, Callable] | tuple[Callable, Callable]]] | tuple[QWidget, float] | tuple[QWidget, float, float], title: str | None = None):
        super().__init__()
        
        self.content = content
        
        self.HOVER_STYLESHEET = F"""
            QWidget.IconToolBarOption:hover {{
                background-color: {PALETTE["hover-1"]}
            }}
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
                color: {PALETTE["text-1"]};
                font-size: {font_size}px
            }}
        """
        
        self.setSpacing(0)
        self.setContentsMargins(15, 5, 15, 5)
        
        self.getWidget().setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.setProperty("class", "IconToolBarOption")
        self.setStyleSheet(self.STYLESHEET)
        
        title_label = QLabel(title) if isinstance(title, str) else title
        
        topWidget = BaseWidget(QHBoxLayout)
        topWidget.setContentsMargins(0, 0, 0, 0)
        topWidget.setProperty("class", "_TopWidget")
        if icon_path is not None:
            topWidget.addWidget(Image(icon_path, width, height))
        elif title is not None:
            topWidget.addWidget(title_label)
        
        if not isinstance(content, Callable):
            topWidget.addWidget(QLabel("▼"))
        
        self.addWidget(topWidget)
        if title is not None and icon_path is not None:
            self.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.getWidget().mousePressEvent = self._clicked
        
        if not isinstance(self.content, Callable) and not isinstance(self.content, list):
            widget = self.content[0]
            
            def hide_event(_):
                self.setStyleSheet(self.STYLESHEET)
                self.update()
            
            widget.hideEvent = hide_event
    
    def _clicked(self, a0):
        pos = self.mapToGlobal(QPoint(self.getWidget().x(), self.getWidget().y() + self.getWidget().rect().height() - self.getWidget().contentsMargins().bottom()))
        
        if isinstance(self.content, Callable):
            return self.content()
        else:
            self.setStyleSheet(self.STYLESHEET.replace(self.HOVER_STYLESHEET, "") + "QWidget.IconToolBarOption {background-color: #30446a}")
            self.update()
            
            if isinstance(self.content, list):
                menu = self._getMenu(self, self.content)
                
                menu.exec(pos)
                
                self.setStyleSheet(self.STYLESHEET)
                self.update()
            else:
                widget, offset_x_factor, offset_y_factor = self.content if len(self.content) == 3 else list(self.content) + [1]
                
                left_most = widget.rect().width() - self.getWidget().width()
                top_most = widget.rect().height()
                
                offset_x = int(left_most - left_most * (offset_x_factor + 1) / 2)
                offset_y = int(top_most - top_most * (offset_y_factor + 1) / 2)
                
                widget.setWindowFlags(Qt.WindowType.Popup)
                
                widget.move(pos - QPoint(offset_x, offset_y))
                widget.show()
    
    def _getMenu(self, parent: QMenu | BaseWidget, content: list, name: Optional[str] = None):
        args = [parent]
        if name is not None:
            args.insert(0, name)
        
        menu = QMenu(*args)
        
        for optionName, optionData in content:
            if optionName is None:
                menu.addSeparator()
            elif isinstance(optionData, (Callable, tuple)):
                optionAction, disableAction = (optionData, None) if isinstance(optionData, Callable) else optionData
                
                action = menu.addAction(optionName, optionAction)
                
                action.setDisabled(disableAction() if disableAction else False)
            elif isinstance(optionData, list):
                menu.addMenu(self._getMenu(menu, optionData, optionName))
            else:
                raise
        
        return menu
        
    
    


