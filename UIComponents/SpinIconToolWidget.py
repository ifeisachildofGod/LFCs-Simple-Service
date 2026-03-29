
from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu
)
from PyQt6.QtCore import QPoint, Qt

from base_widgets import *
from helper_widgets import *


class SpinIconToolWidget(BaseWidget):
    def __init__(self, icons_data: list[tuple[str, Callable]] | str, height: Optional[int], content: Optional[dict[str, Callable | dict[str, Callable]] | tuple[QWidget, float]]):
        super().__init__(QHBoxLayout)
        
        STYLESHEET = f"""
            QWidget.SpinIconToolWidget {{
                background-color: transparent
            }}
            {
                """
                QWidget.SpinIconToolWidget:hover {
                    background-color: #31456b;
                }
                """
                if not isinstance(icons_data, str) else
                ""
            }
            QWidget.SpinIconToolWidget QLabel {{
                color: #9b9b9b;
            }}
        """
        
        self.index = 0
        self.content = content
        self.icons_data = icons_data
        
        self.getLayout().setSpacing(7)
        self.getLayout().setContentsMargins(4, 4, 4, 4)
        
        self.getWidget().setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.getWidget().setProperty("class", "SpinIconToolWidget")
        self.getWidget().setStyleSheet(STYLESHEET)
        
        if isinstance(self.icons_data, str):
            init_path = self.icons_data
        else:
            init_path, init_func = self.icons_data[0]
        
        self.icon = Image(init_path, None, height)
        icon_widget = QWidget()
        icon_widget_layout = QHBoxLayout(icon_widget)
        icon_widget_layout.setContentsMargins(0, 0, 0, 0)
        icon_widget_layout.addWidget(self.icon)
        
        self.addWidget(icon_widget)
        
        if not isinstance(self.icons_data, str):
            init_func()
        
            icon_widget.mousePressEvent = self._spin
        
        if self.content is not None:
            dp_widget = QWidget()
            dp_widget_layout = QHBoxLayout(dp_widget)
            dp_widget_layout.setContentsMargins(0, 0, 0, 0)
            dp_widget_layout.addWidget(QLabel("▼"))
            
            self.addWidget(dp_widget)
            dp_widget.mousePressEvent = self._clicked
            
            if not isinstance(self.content, Callable) and not isinstance(self.content, dict):
                widget, _ = self.content
                
                widget.hideEvent = lambda _: self.update()
    
    def _spin(self, a0):
        self.index = (self.index + 1) % len(self.icons_data)
            
        path, func = self.icons_data[self.index]
        
        func()
        
        if len(self.icons_data) == 1:
            self._clicked(a0)
        else:
            self.icon.setImagePath(path)
    
    def _clicked(self, a0):
        pos = self.mapToGlobal(QPoint(self.getWidget().x(), self.getWidget().y() + self.getWidget().rect().height() - self.getWidget().contentsMargins().bottom()))
        
        if isinstance(self.content, dict):
            menu = self._getMenu(self, self.content)
            
            menu.exec(pos)
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
        
    
    


