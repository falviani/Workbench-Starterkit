# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basicValues.ui',
# licensing of 'basicValues.ui' applies.
#
# Created: Mon Nov 29 14:57:43 2021
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 746)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(21, 11, 457, 691))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerlabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.headerlabel.setFont(font)
        self.headerlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerlabel.setObjectName("headerlabel")
        self.verticalLayout_2.addWidget(self.headerlabel)
        self.mmnote = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.mmnote.setFont(font)
        self.mmnote.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.mmnote.setObjectName("mmnote")
        self.verticalLayout_2.addWidget(self.mmnote)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Box_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Box_label.sizePolicy().hasHeightForWidth())
        self.Box_label.setSizePolicy(sizePolicy)
        self.Box_label.setFrameShape(QtWidgets.QFrame.Box)
        self.Box_label.setObjectName("Box_label")
        self.verticalLayout.addWidget(self.Box_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boxW = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxW.sizePolicy().hasHeightForWidth())
        self.boxW.setSizePolicy(sizePolicy)
        self.boxW.setObjectName("boxW")
        self.horizontalLayout.addWidget(self.boxW)
        self.boxW_val = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxW_val.sizePolicy().hasHeightForWidth())
        self.boxW_val.setSizePolicy(sizePolicy)
        self.boxW_val.setMinimum(1)
        self.boxW_val.setMaximum(1000)
        self.boxW_val.setObjectName("boxW_val")
        self.horizontalLayout.addWidget(self.boxW_val)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.inside_chk = QtWidgets.QCheckBox(self.widget)
        self.inside_chk.setObjectName("inside_chk")
        self.horizontalLayout_2.addWidget(self.inside_chk)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.boxY = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxY.sizePolicy().hasHeightForWidth())
        self.boxY.setSizePolicy(sizePolicy)
        self.boxY.setObjectName("boxY")
        self.horizontalLayout_3.addWidget(self.boxY)
        self.boxY_val = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxY_val.sizePolicy().hasHeightForWidth())
        self.boxY_val.setSizePolicy(sizePolicy)
        self.boxY_val.setMinimum(1)
        self.boxY_val.setMaximum(1000)
        self.boxY_val.setObjectName("boxY_val")
        self.horizontalLayout_3.addWidget(self.boxY_val)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.boxZ = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxZ.sizePolicy().hasHeightForWidth())
        self.boxZ.setSizePolicy(sizePolicy)
        self.boxZ.setObjectName("boxZ")
        self.gridLayout_2.addWidget(self.boxZ, 0, 0, 1, 1)
        self.boxZ_val = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxZ_val.sizePolicy().hasHeightForWidth())
        self.boxZ_val.setSizePolicy(sizePolicy)
        self.boxZ_val.setMinimum(1)
        self.boxZ_val.setMaximum(1000)
        self.boxZ_val.setObjectName("boxZ_val")
        self.gridLayout_2.addWidget(self.boxZ_val, 0, 1, 1, 1)
        self.coord_note = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coord_note.sizePolicy().hasHeightForWidth())
        self.coord_note.setSizePolicy(sizePolicy)
        self.coord_note.setObjectName("coord_note")
        self.gridLayout_2.addWidget(self.coord_note, 0, 3, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.slotFitLbl = QtWidgets.QLabel(self.widget)
        self.slotFitLbl.setObjectName("slotFitLbl")
        self.horizontalLayout_18.addWidget(self.slotFitLbl)
        self.slotFit_val = QtWidgets.QDoubleSpinBox(self.widget)
        self.slotFit_val.setMaximum(1.0)
        self.slotFit_val.setSingleStep(0.1)
        self.slotFit_val.setObjectName("slotFit_val")
        self.horizontalLayout_18.addWidget(self.slotFit_val)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem3)
        self.slotFit_comment = QtWidgets.QLabel(self.widget)
        self.slotFit_comment.setObjectName("slotFit_comment")
        self.horizontalLayout_18.addWidget(self.slotFit_comment)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Stock_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Stock_label.sizePolicy().hasHeightForWidth())
        self.Stock_label.setSizePolicy(sizePolicy)
        self.Stock_label.setFrameShape(QtWidgets.QFrame.Box)
        self.Stock_label.setObjectName("Stock_label")
        self.verticalLayout_4.addWidget(self.Stock_label)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.stockX = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stockX.sizePolicy().hasHeightForWidth())
        self.stockX.setSizePolicy(sizePolicy)
        self.stockX.setObjectName("stockX")
        self.horizontalLayout_7.addWidget(self.stockX)
        self.stockX_val = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stockX_val.sizePolicy().hasHeightForWidth())
        self.stockX_val.setSizePolicy(sizePolicy)
        self.stockX_val.setMinimum(1)
        self.stockX_val.setMaximum(1000)
        self.stockX_val.setObjectName("stockX_val")
        self.horizontalLayout_7.addWidget(self.stockX_val)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.stockY = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stockY.sizePolicy().hasHeightForWidth())
        self.stockY.setSizePolicy(sizePolicy)
        self.stockY.setObjectName("stockY")
        self.horizontalLayout_9.addWidget(self.stockY)
        self.stockY_val = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stockY_val.sizePolicy().hasHeightForWidth())
        self.stockY_val.setSizePolicy(sizePolicy)
        self.stockY_val.setMinimum(1)
        self.stockY_val.setMaximum(1000)
        self.stockY_val.setObjectName("stockY_val")
        self.horizontalLayout_9.addWidget(self.stockY_val)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.stockZ = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stockZ.sizePolicy().hasHeightForWidth())
        self.stockZ.setSizePolicy(sizePolicy)
        self.stockZ.setObjectName("stockZ")
        self.horizontalLayout_11.addWidget(self.stockZ)
        self.stockZ_val = QtWidgets.QDoubleSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stockZ_val.sizePolicy().hasHeightForWidth())
        self.stockZ_val.setSizePolicy(sizePolicy)
        self.stockZ_val.setDecimals(1)
        self.stockZ_val.setMinimum(1.0)
        self.stockZ_val.setMaximum(50.0)
        self.stockZ_val.setSingleStep(0.1)
        self.stockZ_val.setObjectName("stockZ_val")
        self.horizontalLayout_11.addWidget(self.stockZ_val)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.precision_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.precision_label.sizePolicy().hasHeightForWidth())
        self.precision_label.setSizePolicy(sizePolicy)
        self.precision_label.setObjectName("precision_label")
        self.horizontalLayout_12.addWidget(self.precision_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stockMarginLbl = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stockMarginLbl.sizePolicy().hasHeightForWidth())
        self.stockMarginLbl.setSizePolicy(sizePolicy)
        self.stockMarginLbl.setObjectName("stockMarginLbl")
        self.horizontalLayout_5.addWidget(self.stockMarginLbl)
        self.stockMargin_val = QtWidgets.QDoubleSpinBox(self.widget)
        self.stockMargin_val.setMaximum(10.0)
        self.stockMargin_val.setObjectName("stockMargin_val")
        self.horizontalLayout_5.addWidget(self.stockMargin_val)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.stockMargin_comment = QtWidgets.QLabel(self.widget)
        self.stockMargin_comment.setObjectName("stockMargin_comment")
        self.horizontalLayout_5.addWidget(self.stockMargin_comment)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.endMill = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endMill.sizePolicy().hasHeightForWidth())
        self.endMill.setSizePolicy(sizePolicy)
        self.endMill.setFrameShape(QtWidgets.QFrame.Box)
        self.endMill.setObjectName("endMill")
        self.verticalLayout_3.addWidget(self.endMill)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.emDia = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emDia.sizePolicy().hasHeightForWidth())
        self.emDia.setSizePolicy(sizePolicy)
        self.emDia.setObjectName("emDia")
        self.horizontalLayout_13.addWidget(self.emDia)
        self.emDia_val = QtWidgets.QDoubleSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emDia_val.sizePolicy().hasHeightForWidth())
        self.emDia_val.setSizePolicy(sizePolicy)
        self.emDia_val.setDecimals(1)
        self.emDia_val.setMinimum(0.5)
        self.emDia_val.setMaximum(12.5)
        self.emDia_val.setSingleStep(0.1)
        self.emDia_val.setObjectName("emDia_val")
        self.horizontalLayout_13.addWidget(self.emDia_val)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem8)
        self.downcut = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downcut.sizePolicy().hasHeightForWidth())
        self.downcut.setSizePolicy(sizePolicy)
        self.downcut.setObjectName("downcut")
        self.horizontalLayout_14.addWidget(self.downcut)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.extraMM = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extraMM.sizePolicy().hasHeightForWidth())
        self.extraMM.setSizePolicy(sizePolicy)
        self.extraMM.setObjectName("extraMM")
        self.horizontalLayout_16.addWidget(self.extraMM)
        self.extra_val = QtWidgets.QDoubleSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extra_val.sizePolicy().hasHeightForWidth())
        self.extra_val.setSizePolicy(sizePolicy)
        self.extra_val.setDecimals(1)
        self.extra_val.setMinimum(0.0)
        self.extra_val.setMaximum(2.0)
        self.extra_val.setSingleStep(0.1)
        self.extra_val.setProperty("value", 0.0)
        self.extra_val.setObjectName("extra_val")
        self.horizontalLayout_16.addWidget(self.extra_val)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem9)
        self.extra_comment = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extra_comment.sizePolicy().hasHeightForWidth())
        self.extra_comment.setSizePolicy(sizePolicy)
        self.extra_comment.setObjectName("extra_comment")
        self.horizontalLayout_17.addWidget(self.extra_comment)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.toolwarning = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.toolwarning.setFont(font)
        self.toolwarning.setStyleSheet("color: red")
        self.toolwarning.setObjectName("toolwarning")
        self.gridLayout.addWidget(self.toolwarning, 4, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.testLbl = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testLbl.sizePolicy().hasHeightForWidth())
        self.testLbl.setSizePolicy(sizePolicy)
        self.testLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.testLbl.setObjectName("testLbl")
        self.verticalLayout_6.addWidget(self.testLbl)
        self.test1Button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test1Button.sizePolicy().hasHeightForWidth())
        self.test1Button.setSizePolicy(sizePolicy)
        self.test1Button.setFlat(False)
        self.test1Button.setObjectName("test1Button")
        self.verticalLayout_6.addWidget(self.test1Button)
        self.gridLayout.addLayout(self.verticalLayout_6, 5, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem10)
        self.cancelBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_15.addWidget(self.cancelBtn)
        self.useBtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.useBtn.sizePolicy().hasHeightForWidth())
        self.useBtn.setSizePolicy(sizePolicy)
        self.useBtn.setDefault(True)
        self.useBtn.setObjectName("useBtn")
        self.horizontalLayout_15.addWidget(self.useBtn)
        self.gridLayout.addLayout(self.horizontalLayout_15, 6, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Box Dimensions", None, -1))
        self.headerlabel.setText(QtWidgets.QApplication.translate("Dialog", "Tabbed Box Workbench", None, -1))
        self.mmnote.setText(QtWidgets.QApplication.translate("Dialog", "[All dimensions are in mm]", None, -1))
        self.Box_label.setText(QtWidgets.QApplication.translate("Dialog", "Box Dimensions", None, -1))
        self.boxW.setText(QtWidgets.QApplication.translate("Dialog", "Width (X) ", None, -1))
        self.inside_chk.setText(QtWidgets.QApplication.translate("Dialog", "Inside Size", None, -1))
        self.boxY.setText(QtWidgets.QApplication.translate("Dialog", "Depth (Y) ", None, -1))
        self.boxZ.setText(QtWidgets.QApplication.translate("Dialog", "Height (Z) ", None, -1))
        self.coord_note.setText(QtWidgets.QApplication.translate("Dialog", "values match standard\n"
"3D view", None, -1))
        self.slotFitLbl.setText(QtWidgets.QApplication.translate("Dialog", "Slot Fit", None, -1))
        self.slotFit_comment.setText(QtWidgets.QApplication.translate("Dialog", "Space added to slot to\n"
"\'loosen\' fit of tab", None, -1))
        self.Stock_label.setText(QtWidgets.QApplication.translate("Dialog", "Stock Dimensions", None, -1))
        self.stockX.setText(QtWidgets.QApplication.translate("Dialog", "Stock Width (X) ", None, -1))
        self.stockY.setText(QtWidgets.QApplication.translate("Dialog", "Stock Depth (Y)", None, -1))
        self.stockZ.setText(QtWidgets.QApplication.translate("Dialog", "Stock Thickness (Z)", None, -1))
        self.precision_label.setText(QtWidgets.QApplication.translate("Dialog", "Be very precise in measuring\n"
"stock thickness", None, -1))
        self.stockMarginLbl.setText(QtWidgets.QApplication.translate("Dialog", "Stock Margin", None, -1))
        self.stockMargin_comment.setText(QtWidgets.QApplication.translate("Dialog", "Inset from stock stock size\n"
"Plates will never intersect this", None, -1))
        self.endMill.setText(QtWidgets.QApplication.translate("Dialog", "End Mill Data", None, -1))
        self.emDia.setText(QtWidgets.QApplication.translate("Dialog", "End Mill Diameter", None, -1))
        self.downcut.setText(QtWidgets.QApplication.translate("Dialog", "downcut strongly\n"
"recommended", None, -1))
        self.extraMM.setText(QtWidgets.QApplication.translate("Dialog", "Extra Depth ", None, -1))
        self.extra_comment.setText(QtWidgets.QApplication.translate("Dialog", "extra added to depth to\n"
"ensure full cut", None, -1))
        self.toolwarning.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p>The endmill must already exist in Freecad and be configured.</p><p>This workbench will NOT create it.</p></body></html>", None, -1))
        self.testLbl.setText(QtWidgets.QApplication.translate("Dialog", "Presets", None, -1))
        self.test1Button.setText(QtWidgets.QApplication.translate("Dialog", "3mm plywood", None, -1))
        self.cancelBtn.setText(QtWidgets.QApplication.translate("Dialog", "Cancel", None, -1))
        self.useBtn.setText(QtWidgets.QApplication.translate("Dialog", "Use This", None, -1))
