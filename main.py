import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QSplitter, QToolBar,
    QVBoxLayout, QWidget, QPushButton, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QCheckBox, QScrollArea,
    QFrame, QStackedWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from components.TabView import TabView
from components.TitledWidget import TitledWidget
from components.IconToolOption import IconToolOption
from components.SectionWidget import SectionWidget

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self._init()
        self._initMenuBar()
        self._initToolBar()
        
        widg1 = QWidget()
        lyt1 = QVBoxLayout(widg1)
        widg1.setProperty("class", "Widg1")
        widg1.setStyleSheet("QWidget.Widg1{background-color: red;}")
        widg2 = QWidget()
        widg2.setStyleSheet("background-color: yellow;")
        widg3 = QWidget()
        widg3.setStyleSheet("background-color: blue;")
        widg4 = QWidget()
        widg4.setStyleSheet("background-color: green;")
        
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setStyleSheet("QSplitter::handle{background-color: black}")
        
        splitter.addWidget(TitledWidget("Title", widg1))
        splitter.addWidget(TabView({"Song": widg2, "Scriptures": widg3, "Media": widg4}))
        
        lyt1.addWidget(SectionWidget({
            ("ife", False): [
                    ("ico.png", "Ife", print),
                    ("ico.png", "Ife", print),
                    (None, "Ife", print)
                ],
            ("atu", True): [
                    ("ico.png", "Ife", print),
                    ("ico.png", "Ife", print),
                    ("ico.png", "Ife", print)
                ]
            }))
        
        self.main_layout.addWidget(splitter)
    
    def _init(self):
        self.container = QWidget()
        self.main_layout = QVBoxLayout(self.container)
        
        self.setCentralWidget(self.container)
        
        width = 1000
        height = 500
        screen = self.screen().geometry()
        
        self.setGeometry(int(screen.width() / 2 - width / 2), int(screen.height() / 2 - height / 2), int(width), int(height))
        self.setWindowTitle("Simple Service")

    def _initMenuBar(self):
        menu_bar = self.menuBar()
        
        file = menu_bar.addMenu("File")
        edit = menu_bar.addMenu("Edit")
        live = menu_bar.addMenu("Live")
        view = menu_bar.addMenu("View")
        help = menu_bar.addMenu("Help")
        
        # File
        new = file.addMenu("New")
        file.addAction("Open Schedule")
        file.addSeparator()
        file.addActions([QAction("Save Schedule", file), QAction("Save Schedule As", file), QAction("Close Schedule", file)])
        new.addSeparator()
        file.addMenu("Reopen")
        new.addSeparator()
        file.addMenu("Exit")
        
        new.addActions([QAction("New Schedule", new), QAction("New Song", new), QAction("New Presentation", new)])
        new.addSeparator()
        new.addAction("New Song from Song Selection")
        
        # Edit
        edit.addActions([QAction("Cut", edit), QAction("Copy", edit), QAction("Paste", edit), QAction("Delete", edit), QAction("Select All", edit)])
        edit.addSeparator()
        edit.addAction("Options")
        
        # Live
        live.addActions([QAction("Go Live", live), QAction("Go Back", live)])
        live.addSeparator()
        live.addActions([QAction("Logo on Live Output", live), QAction("Black on Live Output", live), QAction("Clear Text on Live Output", live)])
        live.addSeparator()
        live.addAction("Show Live Output", )
        
        # View
        view.addAction("Preview and Live", )
        view.addAction("Preview and Live Combined", )
        view.addAction("Live with Resource Preview", )
        
        # Help
        help.addAction("About")
        help.addAction("Website")
    
    def _initToolBar(self):
        menu_tool_bar = QToolBar()
        
        new_content = {
            "New Schedule": print,
            "New Song": print,
            "New Presentation": print,
            None: None,
            "New Song from SongSelect": print
        }
        alert_content = QWidget()
        alert_content.setStyleSheet("background-color: purple")
        alert_content.setFixedWidth(300)
        alert_content.setFixedHeight(130)
        
        menu_tool_bar.addWidget(IconToolOption("ico.png", 50, None, 15, new_content, "New"))
        menu_tool_bar.addWidget(IconToolOption("ico.png", 50, None, 15, {"Browse": print}, "Open"))
        menu_tool_bar.addWidget(IconToolOption("ico.png", 50, None, 15, print, "Save"))
        menu_tool_bar.addWidget(IconToolOption("ico.png", 50, None, 15, print, "Store"))
        
        self.addToolBar(menu_tool_bar)
        
        live_tools_bar = QToolBar()
        
        live_tools_bar.addWidget(IconToolOption("ico.png", 50, None, 15, print, "Go Live"))
        live_tools_bar.addSeparator()
        live_tools_bar.addWidget(IconToolOption("ico.png", 50, None, 15, (alert_content, -1), "Alerts"))
        live_tools_bar.addSeparator()
        live_tools_bar.addWidget(IconToolOption("ico.png", 50, None, 15, print, "Logo"))
        live_tools_bar.addWidget(IconToolOption("ico.png", 50, None, 15, print, "Black"))
        live_tools_bar.addWidget(IconToolOption("ico.png", 50, None, 15, print, "Clear"))
        live_tools_bar.addSeparator()
        live_tools_bar.addWidget(IconToolOption("ico.png", 50, None, 15, print, "Live"))
        
        self.addToolBar(live_tools_bar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    sys.exit(app.exec())


