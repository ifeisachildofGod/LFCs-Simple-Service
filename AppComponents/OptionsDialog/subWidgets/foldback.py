

from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu, QCheckBox, QPushButton,
    QStackedWidget, QTimeEdit, QDateTimeEdit
)
from PyQt6.QtCore import QPoint, Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

from UIComponents.TabView import TabView_2
from UIComponents.SideBar import SideBar

from helper_widgets import *

from AppComponents.OptionsDialog._base_widgets import *
from AppComponents.OptionsDialog.subWidgets.main_output import _Song, _Scripture


class _General(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        # --------------------------------------------------------------------------------------
        
        esfdf_widget = BaseWidget()
        esfdf_widget.addWidget(esfdf_cbx := QCheckBox("Enable support for display feedback (stage display)"))
        
        # --------------------------------------------------------------------------------------
        
        som_widget = BaseWidget()
        
        om_cb = QComboBox() ; om_cb.addItems(["Monitor 1 (Primary)", "Custom Position", "NDI Stream"])
        cp_widget = BaseWidget() ; cp_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        cp_widget.addWidget(LabeledWidget(LabeledWidget("Left", l_sb := QSpinBox()), LabeledWidget("Width", w_sb := QSpinBox())))
        cp_widget.addWidget(LabeledWidget(LabeledWidget("Right", r_sb := QSpinBox()), LabeledWidget("Height", h_sb := QSpinBox())))
        
        som_widget.addWidget(LabeledWidget("Output Monitor", om_cb))
        som_widget.addWidget(SeparatorLabel("Custom Position"))
        som_widget.addWidget(cp_widget)
        
        # --------------------------------------------------------------------------------------
        
        df_widget = BaseWidget() ; df_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        df_widget.addWidget(LabeledWidget("Default Font", FontEditor("Default Font")))
        
        # --------------------------------------------------------------------------------------
        
        ni_widget = BaseWidget() ; ni_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        ni_widget.addWidget(LabeledWidget(enii_cbx := QCheckBox("Enable next item info"), nif_fe := FontEditor("Next Item Font")))
        ni_widget.addWidget(LabeledWidget("Background Color", bc_ccb := ColorComboBox("grey")))
        ni_widget.addWidget(stl_cbx := QCheckBox("Show Two Lines"))
        
        # --------------------------------------------------------------------------------------
        
        sm_widget = BaseWidget() ; sm_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        sm_widget.addWidget(LabeledWidget(LabeledWidget("Left", l_sb_sm := QSpinBox()), LabeledWidget("Top", t_sb_sm := QSpinBox())))
        sm_widget.addWidget(LabeledWidget(LabeledWidget("Right", r_sb_sm := QSpinBox()), LabeledWidget("Bottom", b_sb_sm := QSpinBox())))
        
        # --------------------------------------------------------------------------------------
        
        self.addWidget(SeparatorLabel("Enable Display Foldback"))
        self.addWidget(esfdf_widget)
        self.addWidget(SeparatorLabel("Select Output Monitor"))
        self.addWidget(som_widget)
        self.addWidget(SeparatorLabel("Default Fonts"))
        self.addWidget(df_widget)
        self.addWidget(SeparatorLabel("Next Item Information"))
        self.addWidget(ni_widget)
        self.addWidget(SeparatorLabel("Screen Margins"))
        self.addWidget(sm_widget)
        self.addStretch()

class _Alerts_Clocks(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        # ------------------------------------------------------------------------------------------------------
        
        co_widget = BaseWidget() ; co_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        sc_cb = QComboBox() ; sc_cb.addItems(["Top Left", "Top Right", "Bottom Left", "Bottom Right"])
        f_cb = QComboBox() ; f_cb.addItems(["hh:nn:{ss}", "hh:nn:ss", "hh:nn", "nn:ss"])
        
        co_widget.addWidget(LabeledWidget(esi_cbx := QCheckBox("Enable Foldback Clock"), esi_fe := FontEditor("Clock Font")))
        co_widget.addWidget(LabeledWidget("Background Color", bc_ccb := ColorComboBox("grey")))
        co_widget.addWidget(LabeledWidget("Screen Location", sc_cb))
        co_widget.addWidget(LabeledWidget("Format", f_cb))
        
        # ------------------------------------------------------------------------------------------------------
        
        mao_widget = BaseWidget() ; mao_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        ena_cbx1 = QCheckBox("Enable Message Alert")
        nf_fe1 = FontEditor("Message Font")
        bc_ccb1 = ColorComboBox("red")
        bo_widget1 = BaseWidget(QHBoxLayout)
        bo_slider1 = QSlider(Qt.Orientation.Horizontal) ; bo_widget1.addWidget(bo_slider1)
        bo_sb1 = QSpinBox() ; bo_widget1.addWidget(bo_sb1)
        sl_sb1 = QComboBox() ; sl_sb1.addItems(["Top", "Bottom"])
        ss_slider = QSlider(Qt.Orientation.Horizontal)
        
        mao_widget.addWidget(LabeledWidget(ena_cbx1, nf_fe1))
        mao_widget.addWidget(LabeledWidget("Background Color", bc_ccb1))
        mao_widget.addWidget(LabeledWidget("Background Opacity", bo_widget1))
        mao_widget.addWidget(LabeledWidget("Screen Location", sl_sb1))
        mao_widget.addWidget(LabeledWidget("Scroll Speed", ss_slider))
        
        # ------------------------------------------------------------------------------------------------------
        
        self.addWidget(SeparatorLabel("Clock Options"))
        self.addWidget(co_widget)
        self.addWidget(SeparatorLabel("Message Alert Options"))
        self.addWidget(mao_widget)
        self.addStretch()


class Foldback(TabView_2):
    def __init__(self):
        content = {
            "General": _General(),
            "Song": _Song(),
            "Scripture": _Scripture(),
            "Alerts and Clocks": _Alerts_Clocks(),
        }
        
        super().__init__(content)
