

from typing import Callable
from PyQt6.QtWidgets import (
    QComboBox, QSizePolicy, QSlider, QSpinBox, QWidget, QHBoxLayout,
    QLabel, QFontComboBox, QMenu, QCheckBox, QPushButton, QTextEdit,
    QStackedWidget, QColorDialog, QDial, QRadioButton
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
        self.addStretch()

class _OutlineSection(BaseWidget):
    def __init__(self):
        super().__init__()

        self.setProperty("class", "OptionsMainBG")
        
        # -----------------------------------------------------------------------------------------------------------
        
        ou_widget = BaseWidget() ; ou_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        s_cb = QComboBox() ; s_cb.addItems(["None", "Outer", "Center", "Inner"])
        c_ccb = ColorComboBox("black")
        j_cb = QComboBox() ; j_cb.addItems(["Round", "Square", "Bevel"])
        s_widget = BaseWidget(QHBoxLayout)
        s_widget.addWidget(s_slider := QSlider(Qt.Orientation.Horizontal))
        s_widget.addWidget(s_sb := QSpinBox())
        o_widget = BaseWidget(QHBoxLayout)
        o_widget.addWidget(o_slider := QSlider(Qt.Orientation.Horizontal))
        o_widget.addWidget(o_sb := QSpinBox())
        
        ou_widget.addWidget(LabeledWidget("Style", s_cb))
        ou_widget.addWidget(LabeledWidget("Color", c_ccb))
        ou_widget.addWidget(LabeledWidget("Join", j_cb))
        ou_widget.addWidget(LabeledWidget("Size", s_widget))
        ou_widget.addWidget(LabeledWidget("Opacity", o_widget))
        
        # -----------------------------------------------------------------------------------------------------------
        
        self.addWidget(SeparatorLabel("Outline"))
        self.addWidget(ou_widget)
        self.addStretch()

class _ShadowSection(BaseWidget):
    def __init__(self):
        super().__init__()

        self.setProperty("class", "OptionsMainBG")
        
        # -----------------------------------------------------------------------------------------------------------
        
        sh_widget = BaseWidget() ; sh_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        s_cb = QComboBox() ; s_cb.addItems(["None", "Outer", "Center", "Inner"])
        c_ccb = ColorComboBox("black")
        a_widget = BaseWidget(QHBoxLayout) ; a_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        a_widget.addWidget(a_dial := QDial())
        a_widget.addWidget(a_sb := QSpinBox())
        off_widget = BaseWidget(QHBoxLayout)
        off_widget.addWidget(off_slider := QSlider(Qt.Orientation.Horizontal))
        off_widget.addWidget(off_sb := QSpinBox())
        b_widget = BaseWidget(QHBoxLayout)
        b_widget.addWidget(b_slider := QSlider(Qt.Orientation.Horizontal))
        b_widget.addWidget(b_sb := QSpinBox())
        o_widget = BaseWidget(QHBoxLayout)
        o_widget.addWidget(o_slider := QSlider(Qt.Orientation.Horizontal))
        o_widget.addWidget(o_sb := QSpinBox())
        
        sh_widget.addWidget(LabeledWidget("Style", s_cb))
        sh_widget.addWidget(LabeledWidget("Color", c_ccb))
        sh_widget.addWidget(LabeledWidget("Angle", a_widget))
        sh_widget.addWidget(LabeledWidget("Offset", off_widget))
        sh_widget.addWidget(LabeledWidget("Blur", b_widget))
        sh_widget.addWidget(LabeledWidget("Opacity", o_widget))
        
        # -----------------------------------------------------------------------------------------------------------
        
        self.addWidget(SeparatorLabel("Shadow"))
        self.addWidget(sh_widget)
        self.addStretch()

class _MarginsSection(BaseWidget):
    def __init__(self):
        super().__init__()

        self.setProperty("class", "OptionsMainBG")
        
        # -----------------------------------------------------------------------------------------------------------
        
        m_widget = BaseWidget() ; m_widget.setSpacing(10)
        
        m_widget.addWidget(LabeledWidget(LabeledWidget("Left", l_sb := QSpinBox()), LabeledWidget("Top", t_sb := QSpinBox())))
        m_widget.addWidget(LabeledWidget(LabeledWidget("Right", r_sb := QSpinBox()), LabeledWidget("Bottom", b_sb := QSpinBox())))
        
        # -----------------------------------------------------------------------------------------------------------
        
        self.addWidget(SeparatorLabel("Margins"))
        self.addWidget(m_widget)
        self.addStretch()

class _FormatSection(BaseWidget):
    def __init__(self):
        super().__init__()

        self.setProperty("class", "OptionsMainBG")
        
        # -----------------------------------------------------------------------------------------------------------
        
        as_widget = BaseWidget()
        
        as_widget.addWidget(dnast_rb := QRadioButton("Do not auto size text"))
        as_widget.addWidget(rttfe_rb := QRadioButton("Resize text to fit element"))
        ntsas_widget = BaseWidget() ; ntsas_widget.addWidget(ntsas_cb := QCheckBox("Normalize text size across slides"))
        
        # -----------------------------------------------------------------------------------------------------------
        
        fmt_widget = BaseWidget()
        
        fmt_widget.addWidget(ww_cb := QCheckBox("Word Wrapping"))
        fmt_widget.addWidget(caw_cb := QCheckBox("Capitalize all words"))
        fmt_widget.addWidget(cfwoel_cb := QCheckBox("Capitalize first word of each line"))
        fmt_widget.addWidget(acfcotw_cb := QCheckBox("Automatically capitalize first character of these words"))
        acfcotw_widget = BaseWidget() ; acfcotw_widget.addWidget(acfcotw_te := QTextEdit())
        fmt_widget.addWidget(acfcotw_widget)
        
        # -----------------------------------------------------------------------------------------------------------
        
        self.addWidget(SeparatorLabel("Auto Sizing"))
        self.addWidget(as_widget)
        self.addWidget(SeparatorLabel("Formatting"))
        self.addWidget(fmt_widget)
        self.addStretch()


class ColorComboBox(IconToolBarOption):
    def __init__(self, color: QColor | str):
        color = QColor(color)
        
        self.selected_color_display = QWidget()
        self.selected_color_display.setFixedSize(50, 15)
        
        color_picker = QColorDialog()
        color_picker.colorSelected.connect(self._setColor)
        
        color_picker.setCurrentColor(color)
        self._setColor(color)
        
        super().__init__(None, None, None, 10, color_picker, self.selected_color_display)
        
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
        
        super().__init__(None, None, None, 10, content_widget, name)
        
        self.setProperty("class", "MyWidget")
        

