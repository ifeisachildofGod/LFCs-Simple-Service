

from typing import Callable
from PyQt6.QtWidgets import (
    QComboBox, QSizePolicy, QSlider, QSpinBox, QWidget, QHBoxLayout,
    QLabel, QFontComboBox, QMenu, QCheckBox, QPushButton,
    QStackedWidget, QColorDialog
)
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt, pyqtSignal

from UIComponents.TabView import TabView_2
from UIComponents.IconToolBarOption import IconToolBarOption

from helper_widgets import *


class _FontSection(BaseWidget):
    def __init__(self):
        super().__init__()

        self.setProperty("class", "OptionsMainBG")
        
        # -----------------------------------------------------------------------------------------------------------
        
        f_widget = BaseWidget() ; f_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        fn_cb = QFontComboBox()
        s_sb = QSpinBox()
        c_cb = ColorComboBox("red")
        st_cb = QComboBox() ; st_cb.addItems(["Regular", "Bold", "Italic", "Bold Italic"])
        uss_widget = BaseWidget(QHBoxLayout) ; uss_widget.setContentsMargins(0, 5, 0, 5)
        uss_widget.addWidget(u_cb := QCheckBox("Underline"))
        uss_widget.addWidget(sp_cb := QCheckBox("Superscript"))
        uss_widget.addWidget(sb_cb := QCheckBox("Subscript"))
        o_widget = BaseWidget(QHBoxLayout)
        o_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        o_widget.setContentsMargins(0, 0, 0, 0)
        o_widget.addWidget(o_slider := QSlider(Qt.Orientation.Horizontal))
        o_widget.addWidget(o_sb := QSpinBox())
        
        f_widget.addWidget(LabeledWidget("Font Name", fn_cb))
        f_widget.addWidget(LabeledWidget("Size", s_sb))
        f_widget.addWidget(LabeledWidget("Color", c_cb))
        f_widget.addWidget(LabeledWidget("Style", st_cb))
        f_widget.addWidget(uss_widget)
        f_widget.addWidget(LabeledWidget("Opacity", o_widget))
        
        # -----------------------------------------------------------------------------------------------------------
        
        a_widget = BaseWidget() ; a_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        ta_cb = QComboBox() ; ta_cb.addItems(["Left", "Center", "Right"])
        va_cb = QComboBox() ; va_cb.addItems(["Left", "Center", "Right"])
        
        a_widget.addWidget(LabeledWidget("Text Alignment", ta_cb))
        a_widget.addWidget(LabeledWidget("Vertical Alignment", va_cb))
        
        # -----------------------------------------------------------------------------------------------------------
        
        self.addWidget(SeparatorLabel("Font"))
        self.addWidget(f_widget)
        self.addWidget(SeparatorLabel("Alignment"))
        self.addWidget(a_widget)

class _OutlineSection(BaseWidget):
    def __init__(self):
        super().__init__()

        self.setProperty("class", "OptionsMainBG")

class _ShadowSection(BaseWidget):
    def __init__(self):
        super().__init__()

        self.setProperty("class", "OptionsMainBG")

class _MarginsSection(BaseWidget):
    def __init__(self):
        super().__init__()

        self.setProperty("class", "OptionsMainBG")

class _FormatSection(BaseWidget):
    def __init__(self):
        super().__init__()

        self.setProperty("class", "OptionsMainBG")


class ColorComboBox(IconToolBarOption):
    def __init__(self, initial_color: str):
        color = QColor(initial_color)
        
        self.selected_color_display = QWidget()
        self.selected_color_display.setFixedSize(50, 15)
        
        color_picker = QColorDialog()
        color_picker.colorSelected.connect(self._setColor)
        
        color_picker.setCurrentColor(color)
        self._setColor(color)
        
        super().__init__(None, None, None, 10, (color_picker, 1), self.selected_color_display)
        
        self.setContentsMargins(5, 5, 5, 5)
        
        self.setProperty("class", "MyWidget")
    
    def _colorToHex(self, color: QColor):
        r = hex(color.red()).replace("0x", "")
        g = hex(color.green()).replace("0x", "")
        b = hex(color.blue()).replace("0x", "")
        
        return f"#{"0" + r if len(r) == 1 else r}{"0" + g if len(g) == 1 else g}{"0" + b if len(b) == 1 else b}"
    
    def _setColor(self, color: QColor):
        self.selected_color_display.setStyleSheet(f"background-color: {self._colorToHex(color)};")

class SeparatorLabel(BaseWidget):
    def __init__(self, text: str):
        super().__init__(QHBoxLayout)
        
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)
        
        label = QLabel(text)
        label.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        label.setContentsMargins(0, 0, 5, 0)
        
        sep_widget = SeperatorWidget(Qt.Orientation.Vertical, 0, None, 1, "#1c1c1c")
        sep_widget.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sep_widget.setContentsMargins(0, 7, 0, 0)
        
        self.addWidget(label)
        self.addWidget(sep_widget)

class LabeledWidget(BaseWidget):
    def __init__(self, starter: str | QWidget, widget: QWidget):
        super().__init__(QHBoxLayout)
        
        self.setContentsMargins(0, 0, 0, 0)
        
        self.addWidget(QLabel(starter) if isinstance(starter, str) else starter, alignment=Qt.AlignmentFlag.AlignLeft)
        self.addSpacing(10)
        self.addWidget(widget, alignment=Qt.AlignmentFlag.AlignRight)

class FontEditor(IconToolBarOption):
    def __init__(self, name: str):
        content_widget = TabView_2(
            {
                "FONT": _FontSection(),
                "OUTLINE": _OutlineSection(),
                "SHADOW": _ShadowSection(),
                "MARGINS": _MarginsSection(),
                "FORMAT": _FormatSection()
            }
        )
        content_widget.setProperty("class", "Section")
        
        super().__init__(None, None, None, 10, (content_widget, 1, -1), name)
        
        self.setProperty("class", "MyWidget")
        

