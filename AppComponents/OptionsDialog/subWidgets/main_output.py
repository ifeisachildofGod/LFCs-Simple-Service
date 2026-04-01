

from typing import Callable
from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout,
    QLabel, QMenu, QCheckBox, QPushButton,
    QStackedWidget, QComboBox, QSpinBox,
    QSlider
)
from PyQt6.QtCore import QPoint, Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

from UIComponents.TabView import TabView_2
from UIComponents.SideBar import SideBar

from helper_widgets import *

from AppComponents.OptionsDialog._base_widgets import *


class _General(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        # -----------------------------------------------------------
        
        som_widget = BaseWidget()
        som_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        om_cb = QComboBox(); om_cb.addItems(["Monitor 1 (Primary)", "Custom Position", "NDI Stream"])
        ac_cb = QComboBox(); ac_cb.addItems(["Disabled", "Monitor 1 (Primary)", "Custom Position"])
        
        som_widget.addWidget(LabeledWidget("Output Monitor", om_cb))
        som_widget.addWidget(LabeledWidget("Alpha Channel", ac_cb))
        
        # -----------------------------------------------------------
        
        op_widget = BaseWidget()
        op_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        l_sb = QSpinBox()
        r_sb = QSpinBox()
        w_sb = QSpinBox(); w_sb.setMinimum(0)
        h_sb = QSpinBox(); h_sb.setMinimum(0)
        
        lr_widget = BaseWidget(QHBoxLayout); lr_widget.setContentsMargins(0, 0, 0, 0)
        lr_widget.addWidget(LabeledWidget("Left", l_sb)); lr_widget.addWidget(LabeledWidget("Right", r_sb))
        wh_widget = BaseWidget(QHBoxLayout); wh_widget.setContentsMargins(0, 0, 0, 0)
        wh_widget.addWidget(LabeledWidget("Width", w_sb)); wh_widget.addWidget(LabeledWidget("Height", h_sb))
        
        op_widget.addWidget(lr_widget)
        op_widget.addWidget(wh_widget)
        
        # -----------------------------------------------------------
        
        sm_widget = BaseWidget()
        sm_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        l_sb = QSpinBox(); l_sb.setMinimum(0)
        r_sb = QSpinBox(); r_sb.setMinimum(0)
        t_sb = QSpinBox(); t_sb.setMinimum(0)
        b_sb = QSpinBox(); b_sb.setMinimum(0)
        
        ltrb_widget = BaseWidget(QHBoxLayout)
        ltrb_widget.addWidget(LabeledWidget("Left", l_sb))
        ltrb_widget.addWidget(LabeledWidget("Top", t_sb))
        ltrb_widget.addWidget(LabeledWidget("Right", r_sb))
        ltrb_widget.addWidget(LabeledWidget("Bottom", b_sb))
        
        ms_button = PushButton("Monitor Setup")
        
        sm_widget.addWidget(ltrb_widget)
        sm_widget.addWidget(ms_button)
        
        # -----------------------------------------------------------
        
        o_widget = BaseWidget() ; o_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        o_cb = FontEditor("Default")
        
        o_widget.addWidget(LabeledWidget("Default Font", o_cb))
        
        # -----------------------------------------------------------
        
        self.addWidget(SeparatorLabel("Select Output Monitor"))
        self.addWidget(som_widget)
        self.addWidget(SeparatorLabel("Output Position"))
        self.addWidget(op_widget)
        self.addWidget(SeparatorLabel("Screen Margins"))
        self.addWidget(sm_widget)
        self.addWidget(SeparatorLabel("Options"))
        self.addWidget(o_widget)
        self.addStretch()

class _Song(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        sl_widget = BaseWidget()
        sl_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        sl_widget.addWidget(LabeledWidget("Song Font", sf_fe := FontEditor("Song Font")))
        sl_widget.addWidget(LabeledWidget(QCheckBox("Show Verse/Chorus label"), lf_fe := FontEditor("Label Font")))
        
        self.addWidget(SeparatorLabel("Song Layout"))
        self.addWidget(sl_widget)
        
        self.addStretch()

class _Scripture(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        # ----------------------------------------------------------
        
        ess_widget = BaseWidget() ; ess_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        ess_widget.addWidget(ess_cb := QCheckBox("Enable support for displaying scripture"))
        
        # ----------------------------------------------------------
        
        svn_cbx = QCheckBox("Show verse numbers")
        sr_cbx = QCheckBox("Show Reference")
        sf_fe = FontEditor("Scripture Font")
        vf_fe = FontEditor("Verse Font")
        rf_fe = FontEditor("Reference Font")
        
        r_widget = BaseWidget() ; r_widget.setContentsMargins(10, 0, 10, 0)
        aes_cb = QComboBox() ; aes_cb.addItems(["Before Each Slide", "After Each Slide", "After Each Passage"])
        scp_cbx = QCheckBox("Show Complete Passage")
        ri_cbx = QCheckBox("Reference Indent")
        abn_cbx = QCheckBox("Abbreviate Book Names")
        als_cbx = QCheckBox("Additional Line Spacing")
        sro_cbx = QCheckBox("Show Reference Only (Hide Scripture Text)")
        
        r_widget.addWidget(LabeledWidget("Reference Location", aes_cb))
        r_widget.addWidget(scp_cbx)
        r_widget.addWidget(ri_cbx)
        r_widget.addWidget(abn_cbx)
        r_widget.addWidget(als_cbx)
        r_widget.addWidget(sro_cbx)
        
        bonv_cbx = QCheckBox("Break on new verse")
        afsoms_cbx = QCheckBox("Automatically Flow Scripture on Multiple Slides")
        mfsbbs_sb = QSpinBox()
        
        sl_widget = BaseWidget() ; sl_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        sl_widget.addWidget(LabeledWidget("Scripture Font", sf_fe))
        sl_widget.addWidget(LabeledWidget(svn_cbx, vf_fe))
        sl_widget.addWidget(LabeledWidget(sr_cbx, rf_fe))
        sl_widget.addWidget(r_widget)
        sl_widget.addWidget(bonv_cbx)
        sl_widget.addWidget(afsoms_cbx)
        sl_widget.addWidget(LabeledWidget("Minimum font size before breaking slide", mfsbbs_sb))
        
        # ----------------------------------------------------------
        
        self.addWidget(SeparatorLabel("Enable Scripture Support"))
        self.addWidget(ess_widget)
        self.addWidget(SeparatorLabel("Scripture Layout"))
        self.addWidget(sl_widget)
        self.addStretch()

class _Presentation(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        tf_fe = FontEditor("Title Font")
        stf_fe = FontEditor("SubTitle Font")
        cf_fe = FontEditor("Content Font")
        
        pl_widget = BaseWidget() ; pl_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        pl_widget.addWidget(LabeledWidget("Title Font", tf_fe))
        pl_widget.addWidget(LabeledWidget("SubTitle Font                                   ", stf_fe))
        pl_widget.addWidget(LabeledWidget("Content Font", cf_fe))
        
        self.addWidget(SeparatorLabel("Presentation Layout"))
        self.addWidget(pl_widget)
        
        self.addStretch()

class _Transition(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        st_cb = QComboBox()
        bt_cb = QComboBox()
        ct_cb = QComboBox()
        lt_cb = QComboBox()
        
        t_widget = BaseWidget() ; t_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        t_widget.addWidget(LabeledWidget("Slide Transition                           ", st_cb))
        t_widget.addWidget(LabeledWidget("Black Transition", bt_cb))
        t_widget.addWidget(LabeledWidget("Clear Transition", ct_cb))
        t_widget.addWidget(LabeledWidget("Logo Transition", lt_cb))
        
        self.addWidget(t_widget)
        
        self.addStretch()

class _Alerts(BaseScrollWidget):
    def __init__(self):
        super().__init__()
        
        self.setProperty("class", "OptionsMainBG")
        
        # ----------------------------------------------------------------------------------------------------------
        
        ena_cbx = QCheckBox("Enable Nursery Alert")
        nf_fe = FontEditor("Nursery Font")
        bc_ccb = ColorComboBox("red")
        bo_widget = BaseWidget(QHBoxLayout)
        bo_slider = QSlider(Qt.Orientation.Horizontal) ; bo_widget.addWidget(bo_slider)
        bo_sb = QSpinBox() ; bo_widget.addWidget(bo_sb)
        sl_sb = QComboBox() ; sl_sb.addItems(["Top Right", "Top Left", "Bottom Right", "Bottom Left"])
        
        ar_widget = BaseWidget() ; ar_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        a_sb = QSpinBox()
        ar_widget.addWidget(LabeledWidget("After", a_sb))
        
        nao_widget = BaseWidget() ; nao_widget.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        
        nao_widget.addWidget(LabeledWidget(ena_cbx, nf_fe))
        nao_widget.addWidget(LabeledWidget("Background Color", bc_ccb))
        nao_widget.addWidget(LabeledWidget("Background Opacity", bo_widget))
        nao_widget.addWidget(LabeledWidget("Screen Location", sl_sb))
        nao_widget.addWidget(ar_cbx := QCheckBox("Automatically Remove"))
        nao_widget.addWidget(ar_widget)
        
        # ----------------------------------------------------------------------------------------------------------
        
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
        
        # ----------------------------------------------------------------------------------------------------------
        
        self.addWidget(SeparatorLabel("Nursery Alert Options"))
        self.addWidget(nao_widget)
        self.addWidget(SeparatorLabel("Message Alert Options"))
        self.addWidget(mao_widget)
        
        self.addStretch()


class MainOutput(TabView_2):
    def __init__(self):
        content = {
            "General": _General(),
            "Song": _Song(),
            "Scripture": _Scripture(),
            "Presentation": _Presentation(),
            "Transition": _Transition(),
            "Alerts": _Alerts(),
        }
        
        super().__init__(content)


