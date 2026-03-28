
from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu
)
from PyQt6.QtCore import QPoint, Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

from base_widgets import *
from helper_widgets import *


class _SubSectionOption(BaseWidget):
    CLICKED_STYLESHEET = """
        QWidget._SubSectionOption {
            background-color: darkcyan
        }
    """
    
    UNCLICKED_STYLESHEET = """
        QWidget._SubSectionOption {
            background-color: transparent
        }
        
        QWidget._SubSectionOption:hover {
            background-color: cyan
        }
    """
    
    clicked = pyqtSignal()
    
    def __init__(self, icon_path: str | None, text: str, do_action: Callable):
        super().__init__(QHBoxLayout)
        
        self.do_action = do_action
        
        self.getWidget().setProperty("class", "_SubSectionOption")
        self.getWidget().setStyleSheet(self.UNCLICKED_STYLESHEET)
        
        self.getWidget().setFixedHeight(25)
        self.getLayout().setContentsMargins(20, 3, 3, 3)
        
        if icon_path:
            self.addWidget(Image(icon_path, height=15), alignment=Qt.AlignmentFlag.AlignVCenter)
        else:
            self.getLayout().addSpacing(32)
        
        self.addWidget(QLabel(text), alignment=Qt.AlignmentFlag.AlignVCenter)
        
        self.getWidget().mousePressEvent = lambda _: self.clicked.emit()
    
    def setState(self, state: bool):
        if state and self.getWidget().styleSheet() != self.CLICKED_STYLESHEET:
            self.getWidget().setStyleSheet(self.CLICKED_STYLESHEET)
            self.do_action()
        elif not state:
            self.getWidget().setStyleSheet(self.UNCLICKED_STYLESHEET)


class SectionWidget(BaseWidget):
    STYLESHEET = """
        QWidget.SectionWidget QWidget._TopSection {
            background-color: transparent;
        }
        
        QWidget.SectionWidget QWidget._BottomSection {
            background-color: transparent;
        }
        
        QWidget.SectionWidget QWidget._TopSection QLabel {
            font-weight: bold;
            color: white;
        }
    """
    
    def __init__(self, content: dict[str, list[tuple[str | None, str, Callable]]]):
        super().__init__()
        
        fontSize = 20
        
        self.getWidget().setProperty("class", "SectionWidget")
        self.getWidget().setStyleSheet(self.STYLESHEET)
        
        self.getLayout().setContentsMargins(0, 0, 0, 0)
        self.getLayout().setSpacing(0)
        
        for i, ((sectionName, isDP), subSectionOptions) in enumerate(content.items()):
            main_label = QLabel(sectionName)
            main_label.setStyleSheet(f"font-size: {fontSize}px")
            
            topSection = BaseWidget(QHBoxLayout)
            topSection.getWidget().setProperty("class", "_TopSection")
            topSection.getWidget().setFixedHeight(40)
            topSection.getLayout().setContentsMargins(10, 5, 0, 5)
            
            subSectionWidget = BaseWidget()
            subSectionWidget.getWidget().setProperty("class", "_BottomSection")
            subSectionWidget.getLayout().setSpacing(1)
            subSectionWidget.getLayout().setContentsMargins(0, 0, 0, 0)
            
            for j, subOption in enumerate(subSectionOptions):
                sso = _SubSectionOption(*subOption)
                sso.clicked.connect(self._mf_sub_section_set(sso))
                
                subSectionWidget.addWidget(sso)
                
                if i + j == 0:
                    sso.clicked.emit()
            
            if isDP:
                open_signal_label = RotatableLabel("▼")
                open_signal_label.setStyleSheet(f"font-size: {fontSize - 8}px")
                
                topSection.addWidget(open_signal_label, alignment=Qt.AlignmentFlag.AlignVCenter)
                
                func = self._mf_section_dp_func(open_signal_label, subSectionWidget)
                
                topSection.getWidget().mousePressEvent = func
                func(None)
            
            topSection.addWidget(main_label, alignment=Qt.AlignmentFlag.AlignVCenter)
            topSection.addStretch()
            
            self.addWidget(topSection)
            self.addWidget(subSectionWidget)
        
        self.addStretch()
    
    def _mf_section_dp_func(self, label: RotatableLabel, ssw: BaseWidget):
        def func(_):
            label.rotate(270 if ssw.isVisible() else 0)
            ssw.setVisible(not ssw.isVisible())
        
        return func
    
    def _mf_sub_section_set(self, sso: _SubSectionOption):
        def func():
            if hasattr(self, "curr_sso"):
                self.curr_sso.setState(False)
            
            sso.setState(True)
            
            self.curr_sso = sso
        
        return func

