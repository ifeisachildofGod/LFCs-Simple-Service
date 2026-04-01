import sys
from typing import Optional
from PyQt6.QtWidgets import (
    QLayout, QMainWindow, QApplication, QSplitter, QToolBar,
    QVBoxLayout, QWidget, QPushButton, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QCheckBox, QScrollArea,
    QFrame, QStackedWidget, QColorDialog, QSpacerItem,
    QSpinBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QCursor

from UIComponents.TabView import TabView_1
from UIComponents.TitledWidget import TitledWidget
from UIComponents.SectionWidget import SectionWidget
from UIComponents.IconToolBarOption import IconToolBarOption
from UIComponents.SpinIconToolWidget import SpinIconToolWidget

from AppComponents.OptionsDialog.Options import OptionsDialog

from helper_widgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self._init()
        self._initMenuBar()
        self._initToolBar()
        
        schedules = TitledWidget(
            "Schedule",
            QWidget(),
            SpinIconToolWidget([("UIComponents/icons/pc1.png", print), ("UIComponents/icons/pc2.png", print), ("UIComponents/icons/pc1.png", print), ("UIComponents/icons/pc2.png", print)], 20, (QWidget(), 1)),
            SeperatorWidget(Qt.Orientation.Horizontal, 0, 2, 15, "#9b9b9b"),
            SpinIconToolWidget(
                [("UIComponents/icons/pc1.png", print)],
                20,
                [
                    (
                        "Add Items", [
                            ("Import Schedule File", print),
                            None,
                            ("New Blank Presentation", print),
                            None,
                            ("Edit Item", print),
                            ("Edit Item", print),
                            ("Edit Item", print)   
                        ]
                    ),
                    ("Edit Item", print),
                    None,
                    ("Edit Title", print),
                    ("Edit Note", print),
                    None,
                    ("Move Item Up", print),
                    ("Move Item Down", print),
                    None,
                    ("Expand All Items", print),
                    ("Collapse All Items", print),
                    None,
                    ("Auto-Expan Items When Dragging", print),
                    None,
                    (
                        "View", [
                            ("Large Items", print),
                            ("Medium Items", print),
                            ("Small Items", print),
                            None,
                            ("Summary View", print),
                        ]
                    ),
                ]
            )
        )
        
        preview = TitledWidget(
            "Preview - Psalm 137:1 (HCBS)",
            QWidget(),
            SpinIconToolWidget([("UIComponents/icons/pc1.png", print), ("UIComponents/icons/pc2.png", print), ("UIComponents/icons/pc1.png", print), ("UIComponents/icons/pc2.png", print)], 20, (QWidget(), -1))
        )
        live = TitledWidget(
            "Live - Psalm 137:1 (KJV)",
            QWidget(),
            SpinIconToolWidget([("UIComponents/icons/pc1.png", print), ("UIComponents/icons/pc2.png", print), ("UIComponents/icons/pc1.png", print), ("UIComponents/icons/pc2.png", print)], 20, (QWidget(), -1))
        )
        preview_output = TitledWidget("Preview Output", QWidget())
        live_output = TitledWidget("Live Output", QWidget())
        
        top_left_view = self.getSplitView(
            Qt.Orientation.Horizontal,
            self.getSplitView(Qt.Orientation.Vertical, preview, preview_output),
            self.getSplitView(Qt.Orientation.Vertical, live, live_output)
        )
        
        upper_view = self.getSplitView(Qt.Orientation.Horizontal, schedules, top_left_view)
        base_tabview = TabView_1(self.getTabSettingParams())
        
        self.main_layout.addWidget(self.getSplitView(Qt.Orientation.Vertical, upper_view, base_tabview))
        
        # self.main_layout.addWidget(Image(r"C:\Users\User\Pictures\Screenshots\Screenshot (207).png", height=250))
        # self.main_layout.addWidget(QColorDialog())
    
    def _init(self):
        self.container = QWidget()
        self.main_layout = QVBoxLayout(self.container)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.setCentralWidget(self.container)
        
        width = 1000
        height = 500
        screen = self.screen().geometry()
        
        self.setGeometry(int(screen.width() / 2 - width / 2), int(screen.height() / 2 - height / 2), int(width), int(height))
        self.setWindowTitle("Simple Service")

    def _initMenuBar(self):
        options_dialog = OptionsDialog()
        
        menu_bar = self.menuBar()
        
        file = menu_bar.addMenu("File")
        edit = menu_bar.addMenu("Edit")
        live = menu_bar.addMenu("Live")
        view = menu_bar.addMenu("View")
        help = menu_bar.addMenu("Help")
        
        # File
        new = file.addMenu("New")
        file.addAction("Open Schedule")
        file.addAction("Load Presentation")
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
        edit.addAction("Options", lambda: options_dialog.exec())
        
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
        menu_tool_bar = QWidget()
        menu_tool_bar.setProperty("class", "ToolBar")
        menu_tool_bar_layout = QHBoxLayout(menu_tool_bar)
        menu_tool_bar_layout.setSpacing(0)
        menu_tool_bar_layout.setContentsMargins(10, 5, 10, 5)
        
        new_content = [
            ("New Schedule", print),
            ("New Song", print),
            ("New Presentation", print),
            None,
            ("New Song from SongSelect", print)
        ]
        alert_content = QWidget()
        alert_content.setStyleSheet("background-color: purple")
        alert_content.setFixedWidth(300)
        alert_content.setFixedHeight(130)
        
        menu_tool_bar_layout.addWidget(IconToolBarOption("UIComponents/icons/pc1.png", None, 35, 15, new_content, "New"))
        menu_tool_bar_layout.addWidget(IconToolBarOption("UIComponents/icons/pc1.png", None, 35, 15, [("Browse", print)], "Open"))
        menu_tool_bar_layout.addWidget(IconToolBarOption("UIComponents/icons/pc1.png", None, 35, 15, print, "Save"))
        menu_tool_bar_layout.addWidget(IconToolBarOption("UIComponents/icons/pc1.png", None, 35, 15, print, "Store"))
        
        menu_tool_bar_layout.addStretch()
        
        menu_tool_bar_layout.addWidget(IconToolBarOption("UIComponents/icons/pc1.png", None, 35, 15, print, "Go Live"))
        menu_tool_bar_layout.addWidget(SeperatorWidget(Qt.Orientation.Horizontal, 10, 2, 30, "#9b9b9b"))
        menu_tool_bar_layout.addWidget(IconToolBarOption("UIComponents/icons/pc1.png", None, 35, 15, (alert_content, -1), "Alerts"))
        menu_tool_bar_layout.addWidget(SeperatorWidget(Qt.Orientation.Horizontal, 10, 2, 30, "#9b9b9b"))
        menu_tool_bar_layout.addWidget(IconToolBarOption("UIComponents/icons/pc1.png", None, 35, 15, print, "Logo"))
        menu_tool_bar_layout.addWidget(IconToolBarOption("UIComponents/icons/pc1.png", None, 35, 15, print, "Black"))
        menu_tool_bar_layout.addWidget(IconToolBarOption("UIComponents/icons/pc1.png", None, 35, 15, print, "Clear"))
        menu_tool_bar_layout.addWidget(SeperatorWidget(Qt.Orientation.Horizontal, 10, 2, 30, "#9b9b9b"))
        menu_tool_bar_layout.addWidget(IconToolBarOption("UIComponents/icons/pc1.png", None, 35, 15, print, "Live"))
        
        self.main_layout.addWidget(menu_tool_bar)
    
    def _getSearchIcon(self, edit: QLineEdit):
        return SpinIconToolWidget(
            [("UIComponents/icons/pc1.png", print)],
            20,
            [
                ("Any Field", print),
                None,
                ("Title", print),
                ("Author", print),
                ("Copyright", print),
                ("Description", print),
                ("Tags", print),
                ("Filename", print),
                ("Directory", print)
            ]
        )
    
    def getSplitView(self, orientation: Qt.Orientation, *sub_widgets: QWidget):
        splitter = QSplitter(orientation)
        
        sub_widgets = sub_widgets if sub_widgets else [QWidget(), QWidget()]
        
        for widget in sub_widgets:
            base_widget = BaseScrollWidget()
            base_widget.setSpacing(0)
            base_widget.setContentsMargins(0, 0, 0, 0)
            base_widget.setProperty("class", "SC_Bordeless")
            
            base_widget.addWidget(widget)
            
            splitter.addWidget(base_widget)
        
        return splitter

    def getTabSettingParams(self):
        # Left
        ss_icon = SpinIconToolWidget("UIComponents/icons/pc1.png", 20, None)
        ss_edit = QLineEdit()
        ss_edit.setPlaceholderText("Search")
        ss_edit.setFixedHeight(30)
        song_search_widget = BaseWidget(QHBoxLayout)
        song_search_widget.setContentsMargins(0, 0, 0, 0)
        song_search_widget.addWidget(ss_icon)
        song_search_widget.addWidget(ss_edit)
        
        sc_s_edit = QLineEdit()
        sc_s_edit.setPlaceholderText("Search")
        sc_s_edit.setFixedHeight(30)
        scriptures_search_widget = BaseWidget(QHBoxLayout)
        scriptures_search_widget.setContentsMargins(0, 0, 0, 0)
        scriptures_search_widget.addWidget(SpinIconToolWidget([("UIComponents/icons/pc1.png", print), ("UIComponents/icons/pc2.png", print)], 20, None))
        scriptures_search_widget.addWidget(sc_s_edit)
        
        ms_edit = QLineEdit()
        ms_edit.setPlaceholderText("Search Any Field")
        ms_edit.setFixedHeight(30)
        media_search_widget = BaseWidget(QHBoxLayout)
        media_search_widget.setContentsMargins(0, 0, 0, 0)
        media_search_widget.addWidget(self._getSearchIcon(ms_edit))
        media_search_widget.addWidget(ms_edit)
        
        ps_edit = QLineEdit()
        ps_edit.setPlaceholderText("Search Any Field")
        ps_edit.setFixedHeight(30)
        presentations_search_widget = BaseWidget(QHBoxLayout)
        presentations_search_widget.setContentsMargins(0, 0, 0, 0)
        presentations_search_widget.addWidget(self._getSearchIcon(ps_edit))
        presentations_search_widget.addWidget(ps_edit)
        
        ts_edit = QLineEdit()
        ts_edit.setPlaceholderText("Search Any Field")
        ts_edit.setFixedHeight(30)
        themes_search_widget = BaseWidget(QHBoxLayout)
        themes_search_widget.setContentsMargins(0, 0, 0, 0)
        themes_search_widget.addWidget(self._getSearchIcon(ts_edit))
        themes_search_widget.addWidget(ts_edit)
        # -----------------------------------------------------------------------
        
        song_options = SectionWidget(
            {
                ("SONGS", False): [("UIComponents/icons/pc1.png", "All Songs", print)],
                ("ONLINE", False): [("UIComponents/icons/pc1.png", "SongSelect", print)],
                ("COLLECTIONS", True): [],
                ("MY COLLECTIONS", True): [],
            }
        )
        scriptures_options = SectionWidget(
            {
                ("SCRIPTURES", False): [
                    ("UIComponents/icons/pc1.png", "HCBS", print),
                    ("UIComponents/icons/pc1.png", "KJV", print),
                    ("UIComponents/icons/pc1.png", "RVA", print),
                    (None, "More Available", print),
                ],
                ("COLLECTIONS", True): [],
                ("MY COLLECTIONS", True): []
            }
        )
        media_options = SectionWidget(
            {
                ("MEDIA", False): [
                    ("UIComponents/icons/pc1.png", "Video", print),
                    ("UIComponents/icons/pc1.png", "Images", print),
                    ("UIComponents/icons/pc1.png", "Feeds", print),
                    ("UIComponents/icons/pc1.png", "DVD", print),
                    ("UIComponents/icons/pc1.png", "Audio", print),
                ],
                ("ONLINE", False): [("UIComponents/icons/pc1.png", "Premium Media", print)],
                ("COLLECTIONS", True): [],
                ("MY COLLECTIONS", True): [],
            }
        )
        presentations_options = SectionWidget(
            {
                ("PRESENTATIONS", False): [("UIComponents/icons/pc1.png", "All Presentations", print)],
                ("COLLECTIONS", True): [],
                ("MY COLLECTIONS", True): [],
            }
        )
        themes_options = SectionWidget(
            {
                ("THEMES", False): [
                    ("UIComponents/icons/pc1.png", "Song", print),
                    ("UIComponents/icons/pc1.png", "Scriptures", print),
                    ("UIComponents/icons/pc1.png", "Presentation", print),
                ],
                ("COLLECTIONS", True): [],
                ("MY COLLECTIONS", True): [],
            }
        )
        
        song_widget = BaseWidget()
        song_widget.setProperty("class", "SettingsWidget")
        song_widget.setSpacing(0)
        song_widget.setContentsMargins(0, 0, 0, 0)
        song_widget.addWidget(song_search_widget)
        song_widget.addWidget(song_options)
        song_widget.addStretch()

        scriptures_widget = BaseWidget()
        scriptures_widget.setProperty("class", "SettingsWidget")
        scriptures_widget.setSpacing(0)
        scriptures_widget.setContentsMargins(0, 0, 0, 0)
        scriptures_widget.addWidget(scriptures_search_widget)
        scriptures_widget.addWidget(scriptures_options)
        scriptures_widget.addStretch()

        media_widget = BaseWidget()
        media_widget.setProperty("class", "SettingsWidget")
        media_widget.setSpacing(0)
        media_widget.setContentsMargins(0, 0, 0, 0)
        media_widget.addWidget(media_search_widget)
        media_widget.addWidget(media_options)
        media_widget.addStretch()

        presentations_widget = BaseWidget()
        presentations_widget.setProperty("class", "SettingsWidget")
        presentations_widget.setSpacing(0)
        presentations_widget.setContentsMargins(0, 0, 0, 0)
        presentations_widget.addWidget(presentations_search_widget)
        presentations_widget.addWidget(presentations_options)
        presentations_widget.addStretch()

        themes_widget = BaseWidget()
        themes_widget.setProperty("class", "SettingsWidget")
        themes_widget.setSpacing(0)
        themes_widget.setContentsMargins(0, 0, 0, 0)
        themes_widget.addWidget(themes_search_widget)
        themes_widget.addWidget(themes_options)
        themes_widget.addStretch()

        # Right
        song_target = QWidget()
        scriptures_target = QWidget()
        media_target = QWidget()
        presentations_target = QWidget()
        themes_target = QWidget()
        
        return {
            "Song": self.getSplitView(Qt.Orientation.Horizontal, song_widget, song_target),
            "Scriptures": self.getSplitView(Qt.Orientation.Horizontal, scriptures_widget, scriptures_target),
            "Media": self.getSplitView(Qt.Orientation.Horizontal, media_widget, media_target),
            "Presentation": self.getSplitView(Qt.Orientation.Horizontal, presentations_widget, presentations_target),
            "Themes": self.getSplitView(Qt.Orientation.Horizontal, themes_widget, themes_target)
        }


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLESHEET)
    
    window = Window()
    window.showMaximized()
    
    sys.exit(app.exec())


