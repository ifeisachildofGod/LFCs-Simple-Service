
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel

from base_widgets import *


class TitledWidget(BaseWidget):
    STYLESHEET = """
    QWidget.TitleArea {
        background-color: #2d2d2d;
    }
    
    QLabel.Title {
        color: #9b9b9b;
    }
    
    QWidget.Body {
        background-color: #202020;
    }
    """
    
    def __init__(self, title: str | QWidget, widget: QWidget, *extra_title_widgets: QWidget, scrollable: bool = False):
        super().__init__()
        self.getWidget().setProperty("class", "TitledWidget")
        self.getWidget().setStyleSheet(self.STYLESHEET)
        
        self.getLayout().setContentsMargins(0, 0, 0, 0)
        self.getLayout().setSpacing(0)
        
        # Title Area
        titleArea = QWidget()
        titleArea.setProperty("class", "TitleArea")
        titleArea.setFixedHeight(30)
        titleAreaLayout = QHBoxLayout(titleArea)
        titleAreaLayout.setContentsMargins(5, 0, 0, 0)
        
        if isinstance(title, str):
            titleWidget = QLabel(title)
            titleWidget.setProperty("class", "Title")
        else:
            titleWidget = title
        
        titleAreaLayout.addWidget(titleWidget)
        titleAreaLayout.addStretch()
        for et_widget in extra_title_widgets:
            titleAreaLayout.addWidget(et_widget)
        
        # Widget Area
        bodyWidget = BaseScrollWidget() if scrollable else BaseWidget()
        bodyWidget.getWidget().setProperty("class", "Body")
        bodyWidget.getLayout().setContentsMargins(0, 0, 0, 0)
        bodyWidget.getLayout().setSpacing(0)
        bodyWidget.addWidget(widget)
        
        self.addWidget(titleArea)
        self.addWidget(bodyWidget)

