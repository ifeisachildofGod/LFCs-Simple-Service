
from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QStackedWidget
)
from PyQt6.QtCore import Qt, pyqtSignal
from base_widgets import *

class _Tab_1(BaseWidget):
    tab_selected = pyqtSignal()
    
    SELECTED_STYLE = """
        QWidget {
            background-color: #9f9f9f;
            
            border-top-right-radius: 5px;
            border-top-left-radius: 5px;
        }
        
        QLabel {
            color: black;
        }
    """
    UN_SELECTED_STYLE = """
        QWidget {
            background-color: transparent;
        }
        
        QLabel {
            color: white;
        }
    """
    
    def __init__(self, name: str):
        super().__init__()
        self.setFixedHeight(35)
        
        self.setSpacing(0)
        self.setContentsMargins(10, 0, 10, 15)
        
        self.name = name
        
        self.tab_selected.connect(lambda: self.setState(True))
        self.setState(False)
        
        self.addWidget(QLabel(self.name))
    
    def setState(self, state):
        if state:
            self.container.setStyleSheet(self.SELECTED_STYLE)
        else:
            self.container.setStyleSheet(self.UN_SELECTED_STYLE)
    
    def mousePressEvent(self, a0):
        self.tab_selected.emit()
        
        return super().mousePressEvent(a0)

class _Tab_2(_Tab_1):
    tab_selected = pyqtSignal()
    
    SELECTED_STYLE = """
        QWidget {
            background-color: transparent;
        }
        
        QLabel {
            color: blue;
            font-wieght: bold;
        }
    """
    UN_SELECTED_STYLE = """
        QWidget {
            background-color: transparent;
        }
        
        QLabel {
            color: white;
        }
    """

class TabView_1(BaseWidget):
    TAB = _Tab_1
    
    STYLESHEET = """
        QWidget.TabWidget {
            background-color: #565656;
            border-bottom: 8px solid #9f9f9f;
        }
    """
    
    def __init__(self, tabs: dict[str, QWidget], *extra_title_widgets: QWidget):
        super().__init__()
        
        self.setProperty("class", "TabView")
        
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)
        
        self.tabs = tabs
        self.extra_title_widgets = extra_title_widgets
        
        self.tabWidget = QWidget()
        self.tabWidget.setProperty("class", "TabWidget")
        self.tabWidget.setFixedHeight(40)
        self.tabWidget.setStyleSheet(self.STYLESHEET)
        self.tabWidgetLayout = QHBoxLayout()
        self.tabWidgetLayout.setContentsMargins(10, 10, 10, 0)
        self.tabWidget.setLayout(self.tabWidgetLayout)
        
        self.bodyWidget = QStackedWidget()
        
        self._initTabs()
        
        self.main_layout.addWidget(self.tabWidget)
        self.main_layout.addWidget(self.bodyWidget)
    
    def _mf_tab_changed(self, tab, index: int):
        def func():
            if hasattr(self, "curr_tab"):
                self.curr_tab.setState(False)
            
            self.curr_tab = tab
            
            self.bodyWidget.setCurrentIndex(index)
        
        return func
    
    def _initTabs(self):
        for tab_index, (tab_name, widget) in enumerate(self.tabs.items()):
            tab = self.TAB(tab_name)
            func = self._mf_tab_changed(tab, tab_index)
            
            if tab_index == 0:
                func()
                tab.setState(True)
            
            tab.tab_selected.connect(func)
            
            self.tabWidgetLayout.addWidget(tab)
            self.bodyWidget.addWidget(widget)
        
        self.tabWidgetLayout.addStretch()
        
        for et_widget in self.extra_title_widgets:
            self.tabWidgetLayout.addWidget(et_widget)

class TabView_2(TabView_1):
    TAB = _Tab_2
    
    STYLESHEET = """
        QWidget.TabView {
            background-color: #363636;
        }
         
        QWidget.TabWidget {
            background-color: transparent;
            border-bottom: 1px solid #9f9f9f;
        }
    """
    
    def __init__(self, tabs, *extra_title_widgets):
        super().__init__(tabs, *extra_title_widgets)
        
        self.tabWidgetLayout.setContentsMargins(10, 10, 10, 10)
