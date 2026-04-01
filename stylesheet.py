import json

with open("palette.json") as file:
    PALETTE = json.load(file)

STYLESHEET = f"""
    QWidget.ToolBar {{
        background-color: {PALETTE["toolbar-bg"]};
    }}
    
    QWidget.SettingsWidget {{
        background-color: {PALETTE["bg-1"]};
    }}
    
    QWidget.OptionsMainBG, QWidget.SC_Bordeless {{
        border: none;
    }}
    
    QWidget.OptionsMainBG {{
        background-color: transparent;
    }}
    
    QWidget.MyWidget {{
        color: {PALETTE["text-main"]};
        background-color: {PALETTE["widget-bg-1"]};
        border: 1px solid {PALETTE["text-2"]};
    }}
    
    QMenuBar {{
        color: white;
        background-color: {PALETTE["section-bg"]};
    }}

    QMenuBar::item:selected {{
        background-color: {PALETTE["hover-1"]};
    }}

    QMenu {{
        color: white;
        background-color: {PALETTE["bg-1"]};
    }}

    QMenu::item:selected {{
        background-color: {PALETTE["hover-1"]};
    }}
    
    QSplitter::handle {{
        width: 2px;
        background-color: {PALETTE["border"]};
    }}
    
    QLabel {{
        color: {PALETTE["text-main"]};
    }}
    
    QLineEdit, QTextEdit {{
        border: 1px solid {PALETTE["border"]};
        color: {PALETTE["text-main"]};
        background-color: {PALETTE["header-bg-2"]};
    }}
    
    QCheckBox, QRadioButton {{
        spacing: 6px;
        color: {PALETTE["text-main"]};
    }}

    QCheckBox::indicator {{
        width: 10px;
        height: 10px;
        
        border: 1px solid {PALETTE["text-2"]};
    }}

    QCheckBox::indicator:unchecked {{
        background-color: {PALETTE["widget-bg-1"]};
    }}

    QCheckBox::indicator:checked {{
        background-color: {PALETTE["selected"]};
        border: 1px solid {PALETTE["selected"]};
    }}

    QCheckBox::indicator:hover {{
        border-color: {PALETTE["selected"]};
    }}
    
    QPushButton {{
        padding: 4px 10px;
        color: {PALETTE["text-main"]};
        background-color: {PALETTE["widget-bg-1"]};
        border: 1px solid {PALETTE["text-2"]};
    }}
    
    QSpinBox {{
        color: {PALETTE["text-main"]};
        background-color: {PALETTE["widget-bg-1"]};
        border: 1px solid {PALETTE["border"]};
    }}
    
    QComboBox {{
        background-color: {PALETTE["widget-bg-1"]};
        color: {PALETTE["text-main"]};
        border: 1px solid {PALETTE["border"]};
        padding: 6px;
        min-width: 120px;
    }}
    
    QComboBox::drop-down {{
        border: none;
        padding-right: 6px;
    }}
    
    QComboBox::down-arrow {{
        image: none;
        border: none;
        width: 12px;
        height: 12px;
        background-color: {PALETTE["selected"]};
        border-radius: 100%;
    }}
    
    QComboBox::down-arrow:hover {{
        background-color: {PALETTE["hover-1"]};
    }}
    
    QComboBox QAbstractItemView {{
        color: {PALETTE["text-main"]};
        background-color: {PALETTE["widget-bg-1"]};
        border: 1px solid {PALETTE["border"]};
        selection-background-color: {PALETTE["hover-1"]};
        selection-color: {PALETTE["text-main"]};
    }}
    
    QColorDialog, QDialog, QWidget.Section {{
        background-color: {PALETTE["section-bg"]}
    }}
    
"""

