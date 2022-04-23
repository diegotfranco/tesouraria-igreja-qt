# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ui_mainlCUgNd.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtcore import*

class LineEdit(QLineEdit):
	def __init__(self, parent):
		super().__init__(parent)
		self._parent = parent

	def focusInEvent(self, event) -> None:
		self.setStyleSheet("border-top-right-radius:0px; border-bottom-right-radius:0px; border-right:1px solid #5EA2FA; padding-left: 14px")
		self._parent.setStyleSheet("QFrame{border: 1px solid #5EA2FA; background-color: #FFF; border-radius: 19px} QLineEdit{border-radius: 18px; background-color: #fff}")
		return super().focusInEvent(event)

	def focusOutEvent(self, event) -> None:
		self.setStyleSheet("border-top-right-radius:0px; border-bottom-right-radius:0px; border-right:1px solid #E2E2E2; padding-left: 14px")
		self._parent.setStyleSheet("QFrame{border: 1px solid #E2E2E2; background-color: #FFF; border-radius: 19px} QLineEdit{border-radius: 18px; background-color: #fff}")
		return super().focusOutEvent(event)


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		if not MainWindow.objectName():
			MainWindow.setObjectName(u"MainWindow")

		MainWindow.resize(1336, 768)
		font = QFont()
		font.setPointSize(16)

		MainWindow.setFont(font)
		self.centralwidget = QWidget(MainWindow)
		self.centralwidget.setObjectName(u"centralwidget")
		self.centralwidget.setStyleSheet(
										"QScrollArea{border: none;}"
										"QScrollBar:vertical{border: none; background-color: #EFF4F4; width: 10px;}"
										"QScrollBar::handle:vertical{border-radius: 4px; background: #B6B9BC;}"
										"QScrollBar::handle:vertical:hover {background: #888888;}"
										"QScrollBar::handle:vertical:pressed{background: #888888;}"
										"QScrollBar::add-line:vertical{background: none; border: none;}"
										"QScrollBar::sub-line:vertical{background: none; border: none;}"
										"QScrollBar::add-page:vertical{background-color: #E0E0E0; border: none;}"
										"QScrollBar::sub-page:vertical{background-color: #E0E0E0; border: none;}"
										"QScrollBar:horizontal{border: none; background-color: #EFF4F4; height: 10px;}"
										"QScrollBar::handle:horizontal{border-radius: 4px; background: #B6B9BC;}"
										"QScrollBar::handle:horizontal:hover {background: #888888;}"
										"QScrollBar::handle:horizontal:pressed{ background: #888888; }"
										"QScrollBar::add-line:horizontal{height: 0px; subcontrol-position: bottom;subcontrol-origin: margin;}"
										"QScrollBar::sub-line:horizontal{height: 0px; subcontrol-position: top;subcontrol-origin: margin;}"
										"QScrollBar::add-page:horizontal{background-color: #E0E0E0; border: none;}" 
										"QScrollBar::sub-page:horizontal{background-color: #E0E0E0; border: none;}"
										)
		self.centralwidget.setFont(font)
		self.verticalLayout_74 = QVBoxLayout(self.centralwidget)
		self.verticalLayout_74.setSpacing(0)
		self.verticalLayout_74.setObjectName(u"verticalLayout_74")
		self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
		self.inicio = QStackedWidget(self.centralwidget)
		self.inicio.setObjectName(u"inicio")
		self.login = QWidget()
		self.login.setObjectName(u"login")
		self.horizontalLayout_33 = QHBoxLayout(self.login)
		self.horizontalLayout_33.setSpacing(0)
		self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
		self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
		self.loginArea = QFrame(self.login)
		self.loginArea.setObjectName(u"loginArea")
		self.loginArea.setMaximumSize(QSize(590, 16777215))
		self.loginArea.setStyleSheet(u"#loginArea{background:qlineargradient(spread:pad, x1:1, y1:1, x2:0.074, y2:0.113636, stop:0.0232558 rgba(40, 69, 127, 255), stop:0.186047 rgba(46, 80, 128, 255), stop:0.365751 rgba(63, 108, 127, 255), stop:0.463002 rgba(67, 117, 126, 255), stop:0.54334 rgba(66, 119, 127, 255), stop:0.710359 rgba(63, 125, 120, 255), stop:0.809725 rgba(56, 125, 106, 255), stop:0.97463 rgba(48, 125, 83, 255))}")
		self.loginArea.setFrameShape(QFrame.StyledPanel)
		self.loginArea.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_30 = QHBoxLayout(self.loginArea)
		self.horizontalLayout_30.setSpacing(0)
		self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
		self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
		self.horizontalSpacer_25 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_30.addItem(self.horizontalSpacer_25)

		self.frame_20 = QFrame(self.loginArea)
		self.frame_20.setObjectName(u"frame_20")
		self.frame_20.setMinimumSize(QSize(350, 0))
		self.frame_20.setFrameShape(QFrame.StyledPanel)
		self.frame_20.setFrameShadow(QFrame.Raised)
		self.verticalLayout_26 = QVBoxLayout(self.frame_20)
		self.verticalLayout_26.setSpacing(0)
		self.verticalLayout_26.setObjectName(u"verticalLayout_26")
		self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
		self.verticalSpacer_8 = QSpacerItem(20, 328, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.verticalLayout_26.addItem(self.verticalSpacer_8)

		self.frame_18 = QFrame(self.frame_20)
		self.frame_18.setObjectName(u"frame_18")
		self.frame_18.setMinimumSize(QSize(0, 372))
		self.frame_18.setFrameShape(QFrame.StyledPanel)
		self.frame_18.setFrameShadow(QFrame.Raised)
		self.verticalLayout_27 = QVBoxLayout(self.frame_18)
		self.verticalLayout_27.setSpacing(0)
		self.verticalLayout_27.setObjectName(u"verticalLayout_27")
		self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
		self.frame_19 = QFrame(self.frame_18)
		self.frame_19.setObjectName(u"frame_19")
		self.frame_19.setFrameShape(QFrame.StyledPanel)
		self.frame_19.setFrameShadow(QFrame.Raised)
		self.verticalLayout_28 = QVBoxLayout(self.frame_19)
		self.verticalLayout_28.setSpacing(0)
		self.verticalLayout_28.setObjectName(u"verticalLayout_28")
		self.verticalLayout_28.setContentsMargins(0, 16, 0, 16)
		self.label_login = QLabel(self.frame_19)
		self.label_login.setObjectName(u"label_login")
		self.label_login.setMinimumSize(QSize(0, 64))
		font1 = QFont()
		font1.setPointSize(36)
		font1.setBold(True)
		self.label_login.setFont(font1)
		self.label_login.setLayoutDirection(Qt.LeftToRight)
		self.label_login.setStyleSheet(u"color:#fff")
		self.label_login.setAlignment(Qt.AlignCenter)

		self.verticalLayout_28.addWidget(self.label_login)

		self.verticalLayout_27.addWidget(self.frame_19)

		self.frame_21 = QFrame(self.frame_18)
		self.frame_21.setObjectName(u"frame_21")
		self.frame_21.setMinimumSize(QSize(0, 122))
		self.frame_21.setFrameShape(QFrame.StyledPanel)
		self.frame_21.setFrameShadow(QFrame.Raised)
		self.verticalLayout_29 = QVBoxLayout(self.frame_21)
		self.verticalLayout_29.setSpacing(24)
		self.verticalLayout_29.setObjectName(u"verticalLayout_29")
		self.verticalLayout_29.setContentsMargins(32, 0, 32, 0)
		self.lineEdit_email_login = QLineEdit(self.frame_21)
		self.lineEdit_email_login.setObjectName(u"lineEdit_email_login")
		self.lineEdit_email_login.setMinimumSize(QSize(0, 44))
		font2 = QFont()
		font2.setPointSize(14)
		self.lineEdit_email_login.setFont(font2)
		self.lineEdit_email_login.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_email_login.setStyleSheet(u"QLineEdit:hover{border-width: 1px;border-style: solid; border-color: #28A745;}\n"
	"QLineEdit:focus{border-width: 1px;border-style: solid; border-color: #28A745;}\n"
	"QLineEdit{border-radius: 22px; padding-left:16px}")

		######################################################
		self.lineEdit_email_login.setInputMethodHints(Qt.ImhNone)
		self.lineEdit_email_login.setMaxLength(255)
		######################################################

		self.verticalLayout_29.addWidget(self.lineEdit_email_login)

		self.lineEdit_senha_login = QLineEdit(self.frame_21)
		self.lineEdit_senha_login.setObjectName(u"lineEdit_senha_login")
		self.lineEdit_senha_login.setMinimumSize(QSize(0, 44))
		self.lineEdit_senha_login.setFont(font2)
		self.lineEdit_senha_login.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_senha_login.setStyleSheet(u"QLineEdit:hover{border-width: 1px;border-style: solid; border-color: #28A745;}\n"
	"QLineEdit:focus{border-width: 1px;border-style: solid; border-color: #28A745;}\n"
	"QLineEdit{border-radius: 22px; padding-left:16px}")

		######################################################
		self.lineEdit_senha_login.setMaxLength(255)
		######################################################

		self.verticalLayout_29.addWidget(self.lineEdit_senha_login)

		self.verticalLayout_27.addWidget(self.frame_21)

		self.label_avisos = QLabel(self.frame_18)
		self.label_avisos.setObjectName(u"label_avisos")
		self.label_avisos.setMaximumSize(QSize(16777215, 25))
		font3 = QFont()
		font3.setPointSize(11)
		self.label_avisos.setFont(font3)
		self.label_avisos.setStyleSheet(u"color: #9D2632")
		self.label_avisos.setAlignment(Qt.AlignCenter)

		self.verticalLayout_27.addWidget(self.label_avisos)

		self.frame_22 = QFrame(self.frame_18)
		self.frame_22.setObjectName(u"frame_22")
		self.frame_22.setMaximumSize(QSize(16777215, 80))
		self.frame_22.setFrameShape(QFrame.StyledPanel)
		self.frame_22.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_31 = QHBoxLayout(self.frame_22)
		self.horizontalLayout_31.setSpacing(0)
		self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
		self.horizontalLayout_31.setContentsMargins(0, 0, 0, 32)
		self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_31.addItem(self.horizontalSpacer_26)

		self.frame_23 = QFrame(self.frame_22)
		self.frame_23.setObjectName(u"frame_23")
		self.frame_23.setMinimumSize(QSize(138, 38))
		self.frame_23.setMaximumSize(QSize(138, 38))
		self.frame_23.setFrameShape(QFrame.StyledPanel)
		self.frame_23.setFrameShadow(QFrame.Raised)
		self.verticalLayout_30 = QVBoxLayout(self.frame_23)
		self.verticalLayout_30.setSpacing(3)
		self.verticalLayout_30.setObjectName(u"verticalLayout_30")
		self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
		self.pushButton_entrar = QPushButton(self.frame_23)
		self.pushButton_entrar.setObjectName(u"pushButton_entrar")
		self.pushButton_entrar.setMinimumSize(QSize(0, 36))
		self.pushButton_entrar.setMaximumSize(QSize(120, 36))
		font4 = QFont()
		font4.setPointSize(14)
		font4.setBold(True)
		self.pushButton_entrar.setFont(font4)
		self.pushButton_entrar.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_entrar.setStyleSheet(u"QPushButton:hover{background: #198754; color: #fff; border-radius:5px}QPushButton{background: #28A745; color: #fff; border-radius:5px}\n"
	"")
		self.pushButton_entrar.setFlat(False)

		self.verticalLayout_30.addWidget(self.pushButton_entrar)

		palette = QPalette()
		brush = QBrush(QColor(255, 255, 255, 255))
		brush.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
		brush1 = QBrush(QColor(240, 240, 240, 255))
		brush1.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.Button, brush1)
		palette.setBrush(QPalette.Active, QPalette.Light, brush)
		brush2 = QBrush(QColor(227, 227, 227, 255))
		brush2.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
		brush3 = QBrush(QColor(160, 160, 160, 255))
		brush3.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
		palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
		palette.setBrush(QPalette.Active, QPalette.Text, brush)
		palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
		palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
		palette.setBrush(QPalette.Active, QPalette.Base, brush)
		palette.setBrush(QPalette.Active, QPalette.Window, brush1)
		brush4 = QBrush(QColor(105, 105, 105, 255))
		brush4.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.Shadow, brush4)
		brush5 = QBrush(QColor(0, 120, 215, 255))
		brush5.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.Highlight, brush5)
		palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
		brush6 = QBrush(QColor(0, 0, 255, 255))
		brush6.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.Link, brush6)
		brush7 = QBrush(QColor(255, 0, 255, 255))
		brush7.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush7)
		brush8 = QBrush(QColor(245, 245, 245, 255))
		brush8.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
		brush9 = QBrush(QColor(0, 0, 0, 255))
		brush9.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.NoRole, brush9)
		brush10 = QBrush(QColor(255, 255, 220, 255))
		brush10.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
		palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush9)
	#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
	#endif
		palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
		palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
		palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
		palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
		palette.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
		palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
		palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
		palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
		palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
		palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
		palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
		palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush4)
		palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
		palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush9)
		palette.setBrush(QPalette.Inactive, QPalette.Link, brush6)
		palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush7)
		palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
		brush11 = QBrush(QColor(0, 0, 0, 255))
		brush11.setStyle(Qt.NoBrush)
		palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush11)
		palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
		palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush9)
	#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
	#endif
		palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
		palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
		palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
		brush12 = QBrush(QColor(247, 247, 247, 255))
		brush12.setStyle(Qt.SolidPattern)
		palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
		palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
		palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
		palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
		palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
		palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
		palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
		palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
		palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush9)
		palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush5)
		palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
		palette.setBrush(QPalette.Disabled, QPalette.Link, brush6)
		palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush7)
		palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
		brush13 = QBrush(QColor(0, 0, 0, 255))
		brush13.setStyle(Qt.NoBrush)
		palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush13)
		palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
		palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush9)
	#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
		palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
	#endif
		
		self.horizontalLayout_31.addWidget(self.frame_23)

		self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_31.addItem(self.horizontalSpacer_27)

		self.verticalLayout_27.addWidget(self.frame_22)

		self.verticalLayout_26.addWidget(self.frame_18)

		self.verticalSpacer_9 = QSpacerItem(20, 328, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.verticalLayout_26.addItem(self.verticalSpacer_9)

		self.horizontalLayout_30.addWidget(self.frame_20)

		self.horizontalSpacer_28 = QSpacerItem(131, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_30.addItem(self.horizontalSpacer_28)

		self.horizontalLayout_33.addWidget(self.loginArea)

		self.background_login = QFrame(self.login)
		self.background_login.setObjectName(u"background_login")
		self.background_login.setAutoFillBackground(False)
		self.background_login.setStyleSheet(u"#background{background:#EFF4F4}")
		self.background_login.setFrameShape(QFrame.StyledPanel)
		self.background_login.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_27 = QHBoxLayout(self.background_login)
		self.horizontalLayout_27.setSpacing(0)
		self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
		self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
		self.horizontalSpacer_18 = QSpacerItem(159, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_27.addItem(self.horizontalSpacer_18)

		self.frame_6 = QFrame(self.background_login)
		self.frame_6.setObjectName(u"frame_6")
		self.frame_6.setMinimumSize(QSize(613, 0))
		self.frame_6.setFrameShape(QFrame.StyledPanel)
		self.frame_6.setFrameShadow(QFrame.Raised)
		self.verticalLayout_24 = QVBoxLayout(self.frame_6)
		self.verticalLayout_24.setSpacing(0)
		self.verticalLayout_24.setObjectName(u"verticalLayout_24")
		self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
		self.verticalSpacer_6 = QSpacerItem(20, 379, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.verticalLayout_24.addItem(self.verticalSpacer_6)

		self.frame_13 = QFrame(self.frame_6)
		self.frame_13.setObjectName(u"frame_13")
		self.frame_13.setMinimumSize(QSize(0, 207))
		font6 = QFont()
		self.frame_13.setFont(font6)
		self.frame_13.setFrameShape(QFrame.StyledPanel)
		self.frame_13.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_28 = QHBoxLayout(self.frame_13)
		self.horizontalLayout_28.setSpacing(0)
		self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
		self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
		self.frame_14 = QFrame(self.frame_13)
		self.frame_14.setObjectName(u"frame_14")
		self.frame_14.setMinimumSize(QSize(192, 0))
		font7 = QFont()
		font7.setPointSize(48)
		self.frame_14.setFont(font7)
		self.frame_14.setFrameShape(QFrame.StyledPanel)
		self.frame_14.setFrameShadow(QFrame.Raised)
		self.verticalLayout_25 = QVBoxLayout(self.frame_14)
		self.verticalLayout_25.setSpacing(0)
		self.verticalLayout_25.setObjectName(u"verticalLayout_25")
		self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
		self.label_4 = QLabel(self.frame_14)
		self.label_4.setObjectName(u"label_4")
		self.label_4.setFont(font7)
		self.label_4.setStyleSheet(u"color: #3A4B5E")

		self.verticalLayout_25.addWidget(self.label_4)

		self.horizontalLayout_28.addWidget(self.frame_14)

		self.frame_16 = QFrame(self.frame_13)
		self.frame_16.setObjectName(u"frame_16")
		self.frame_16.setMinimumSize(QSize(421, 0))
		self.frame_16.setFont(font6)
		self.frame_16.setFrameShape(QFrame.StyledPanel)
		self.frame_16.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_29 = QHBoxLayout(self.frame_16)
		self.horizontalLayout_29.setSpacing(0)
		self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
		self.horizontalLayout_29.setContentsMargins(0, 0, 20, 0)
		self.frame_17 = QFrame(self.frame_16)
		self.frame_17.setObjectName(u"frame_17")
		self.frame_17.setMinimumSize(QSize(401, 0))
		self.frame_17.setFrameShape(QFrame.StyledPanel)
		self.frame_17.setFrameShadow(QFrame.Raised)
		self.label_6 = QLabel(self.frame_17)
		self.label_6.setObjectName(u"label_6")
		self.label_6.setGeometry(QRect(0, 50, 401, 61))
		font8 = QFont()
		font8.setPointSize(48)
		font8.setBold(True)
		self.label_6.setFont(font8)
		self.label_6.setStyleSheet(u"color: #3A4B5E")
		self.line = QFrame(self.frame_17)
		self.line.setObjectName(u"line")
		self.line.setGeometry(QRect(10, 170, 361, 16))
		self.line.setFont(font6)
		self.line.setStyleSheet(u"color: #3A4B5E")
		self.line.setFrameShadow(QFrame.Plain)
		self.line.setLineWidth(2)
		self.line.setFrameShape(QFrame.HLine)
		self.label_7 = QLabel(self.frame_17)
		self.label_7.setObjectName(u"label_7")
		self.label_7.setGeometry(QRect(50, 110, 221, 61))
		self.label_7.setFont(font8)
		self.label_7.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_29.addWidget(self.frame_17)

		self.horizontalLayout_28.addWidget(self.frame_16)

		self.verticalLayout_24.addWidget(self.frame_13)

		self.verticalSpacer_7 = QSpacerItem(20, 379, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.verticalLayout_24.addItem(self.verticalSpacer_7)

		self.horizontalLayout_27.addWidget(self.frame_6)

		self.horizontalSpacer_24 = QSpacerItem(158, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_27.addItem(self.horizontalSpacer_24)

		self.horizontalLayout_33.addWidget(self.background_login)

		self.inicio.addWidget(self.login)
		self.main = QWidget()
		self.main.setObjectName(u"main")
		self.verticalLayout_31 = QVBoxLayout(self.main)
		self.verticalLayout_31.setSpacing(0)
		self.verticalLayout_31.setObjectName(u"verticalLayout_31")
		self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
		self.header = QFrame(self.main)
		self.header.setObjectName(u"header")
		self.header.setMinimumSize(QSize(0, 64))
		self.header.setMaximumSize(QSize(16777215, 84))
		self.header.setFont(font7)
		self.header.setStyleSheet(u"background-color: #3A4B5E")
		self.header.setFrameShape(QFrame.StyledPanel)
		self.header.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_2 = QHBoxLayout(self.header)
		self.horizontalLayout_2.setSpacing(0)
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.title = QFrame(self.header)
		self.title.setObjectName(u"title")
		self.title.setFont(font7)
		self.title.setFrameShape(QFrame.StyledPanel)
		self.title.setFrameShadow(QFrame.Raised)
		self.verticalLayout_2 = QVBoxLayout(self.title)
		self.verticalLayout_2.setSpacing(0)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.verticalLayout_2.setContentsMargins(16, 0, 0, 0)
		self.label = QLabel(self.title)
		self.label.setObjectName(u"label")
		font9 = QFont()
		font9.setPointSize(28)
		font9.setBold(False)
		self.label.setFont(font9)
		self.label.setAutoFillBackground(False)
		self.label.setStyleSheet(u"color: #ffffff")

		self.verticalLayout_2.addWidget(self.label)

		self.horizontalLayout_2.addWidget(self.title)

		self.userArea = QFrame(self.header)
		self.userArea.setObjectName(u"userArea")
		self.userArea.setFont(font)
		self.userArea.setFrameShape(QFrame.StyledPanel)
		self.userArea.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_3 = QHBoxLayout(self.userArea)
		self.horizontalLayout_3.setSpacing(0)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.horizontalLayout_3.setContentsMargins(0, 0, 16, 0)
		self.horizontalSpacer = QSpacerItem(597, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_3.addItem(self.horizontalSpacer)

		self.pushButton_sair = QPushButton(self.userArea)
		self.pushButton_sair.setObjectName(u"pushButton_sair")
		self.pushButton_sair.setMaximumSize(QSize(16777215, 16777215))
		font10 = QFont()
		font10.setPointSize(12)
		self.pushButton_sair.setFont(font10)
		self.pushButton_sair.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_sair.setFocusPolicy(Qt.NoFocus)
		self.pushButton_sair.setStyleSheet(u"QPushButton:hover{text-decoration: underline} QPushButton{color: #fff; border-style: hidden}")
		icon = QIcon()
		icon.addFile(u"icons/logout_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_sair.setIcon(icon)
		self.pushButton_sair.setIconSize(QSize(24, 24))
		self.pushButton_sair.setFlat(False)

		self.horizontalLayout_3.addWidget(self.pushButton_sair)

		self.horizontalLayout_2.addWidget(self.userArea)

		self.verticalLayout_31.addWidget(self.header)

		self.body = QFrame(self.main)
		self.body.setObjectName(u"body")
		self.body.setFont(font)
		self.body.setFrameShape(QFrame.StyledPanel)
		self.body.setFrameShadow(QFrame.Raised)
		self.horizontalLayout = QHBoxLayout(self.body)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.menu = QFrame(self.body)
		self.menu.setObjectName(u"menu")
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
		self.menu.setSizePolicy(sizePolicy)
		self.menu.setMinimumSize(QSize(0, 0))
		self.menu.setMaximumSize(QSize(200, 16777215))
		font11 = QFont()
		font11.setPointSize(32)
		self.menu.setFont(font11)
		self.menu.setStyleSheet(u"QFrame{background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.074, y2:0.113636, stop:0.0232558 rgba(40, 69, 127, 255), stop:0.186047 rgba(46, 80, 128, 255), stop:0.365751 rgba(63, 108, 127, 255), stop:0.463002 rgba(67, 117, 126, 255), stop:0.54334 rgba(66, 119, 127, 255), stop:0.710359 rgba(63, 125, 120, 255), stop:0.809725 rgba(56, 125, 106, 255), stop:0.97463 rgba(48, 125, 83, 255))}")
		self.menu.setFrameShape(QFrame.StyledPanel)
		self.menu.setFrameShadow(QFrame.Raised)
		self.verticalLayout_3 = QVBoxLayout(self.menu)
		self.verticalLayout_3.setSpacing(0)
		self.verticalLayout_3.setObjectName(u"verticalLayout_3")
		self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
		self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.pushButton_home = QPushButton(self.menu)
		self.pushButton_home.setObjectName(u"pushButton_home")
		sizePolicy.setHeightForWidth(self.pushButton_home.sizePolicy().hasHeightForWidth())
		self.pushButton_home.setSizePolicy(sizePolicy)
		self.pushButton_home.setMinimumSize(QSize(0, 0))
		font12 = QFont()
		font12.setPointSize(24)
		self.pushButton_home.setFont(font12)
		self.pushButton_home.setFocusPolicy(Qt.StrongFocus)
		self.pushButton_home.setStyleSheet(u"QPushButton:hover{font-weight: 550}\n"
	"QPushButton{color:#fff; border-width: 0px 0px 1px 0px; border-style: solid hidden solid hidden; border-color: #fff}")

		self.verticalLayout_3.addWidget(self.pushButton_home)

		self.pushButton_cadastro = QPushButton(self.menu)
		self.pushButton_cadastro.setObjectName(u"pushButton_cadastro")
		sizePolicy.setHeightForWidth(self.pushButton_cadastro.sizePolicy().hasHeightForWidth())
		self.pushButton_cadastro.setSizePolicy(sizePolicy)
		self.pushButton_cadastro.setMinimumSize(QSize(0, 0))
		self.pushButton_cadastro.setFont(font12)
		self.pushButton_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_cadastro.setFocusPolicy(Qt.StrongFocus)
		self.pushButton_cadastro.setStyleSheet(u"QPushButton:hover{font-weight: 550}\n"
	"QPushButton{color:#fff; border-width: 0px 0px 1px 0px; border-style: solid hidden solid hidden; border-color: #fff}")
		self.pushButton_cadastro.setFlat(True)

		self.verticalLayout_3.addWidget(self.pushButton_cadastro)

		self.pushButton_membros = QPushButton(self.menu)
		self.pushButton_membros.setObjectName(u"pushButton_membros")
		sizePolicy.setHeightForWidth(self.pushButton_membros.sizePolicy().hasHeightForWidth())
		self.pushButton_membros.setSizePolicy(sizePolicy)
		self.pushButton_membros.setMinimumSize(QSize(0, 0))
		self.pushButton_membros.setFont(font12)
		self.pushButton_membros.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_membros.setFocusPolicy(Qt.StrongFocus)
		self.pushButton_membros.setStyleSheet(u"QPushButton:hover{font-weight: 550}\n"
	"QPushButton{color:#fff; border-width: 0px 0px 1px 0px; border-style: solid hidden solid hidden; border-color: #fff}")
		self.pushButton_membros.setFlat(True)

		self.verticalLayout_3.addWidget(self.pushButton_membros)

		self.pushButton_entradas = QPushButton(self.menu)
		self.pushButton_entradas.setObjectName(u"pushButton_entradas")
		sizePolicy.setHeightForWidth(self.pushButton_entradas.sizePolicy().hasHeightForWidth())
		self.pushButton_entradas.setSizePolicy(sizePolicy)
		self.pushButton_entradas.setMinimumSize(QSize(0, 0))
		self.pushButton_entradas.setFont(font12)
		self.pushButton_entradas.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_entradas.setFocusPolicy(Qt.StrongFocus)
		self.pushButton_entradas.setStyleSheet(u"QPushButton:hover{font-weight: 550}\n"
	"QPushButton{color:#fff; border-width: 0px 0px 1px 0px; border-style: solid hidden solid hidden; border-color: #fff}")
		self.pushButton_entradas.setFlat(True)

		self.verticalLayout_3.addWidget(self.pushButton_entradas)

		self.pushButton_saidas = QPushButton(self.menu)
		self.pushButton_saidas.setObjectName(u"pushButton_saidas")
		sizePolicy.setHeightForWidth(self.pushButton_saidas.sizePolicy().hasHeightForWidth())
		self.pushButton_saidas.setSizePolicy(sizePolicy)
		self.pushButton_saidas.setMinimumSize(QSize(0, 0))
		self.pushButton_saidas.setFont(font12)
		self.pushButton_saidas.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_saidas.setFocusPolicy(Qt.StrongFocus)
		self.pushButton_saidas.setStyleSheet(u"QPushButton:hover{font-weight: 550}\n"
	"QPushButton{color:#fff; border-width: 0px 0px 1px 0px; border-style: solid hidden solid hidden; border-color: #fff}")
		self.pushButton_saidas.setFlat(True)

		self.verticalLayout_3.addWidget(self.pushButton_saidas)

		self.pushButton_financeiro = QPushButton(self.menu)
		self.pushButton_financeiro.setObjectName(u"pushButton_financeiro")
		sizePolicy.setHeightForWidth(self.pushButton_financeiro.sizePolicy().hasHeightForWidth())
		self.pushButton_financeiro.setSizePolicy(sizePolicy)
		self.pushButton_financeiro.setMinimumSize(QSize(0, 0))
		self.pushButton_financeiro.setFont(font12)
		self.pushButton_financeiro.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_financeiro.setFocusPolicy(Qt.StrongFocus)
		self.pushButton_financeiro.setStyleSheet(u"QPushButton:hover{font-weight: 550}\n"
	"QPushButton{color:#fff;}")
		self.pushButton_financeiro.setFlat(True)

		self.verticalLayout_3.addWidget(self.pushButton_financeiro)


		self.horizontalLayout.addWidget(self.menu)

		self.scrollArea = QScrollArea(self.body)
		self.scrollArea.setObjectName(u"scrollArea")
		sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
		self.scrollArea.setSizePolicy(sizePolicy)
		self.scrollArea.setWidgetResizable(True)
		self.scrollAreaWidgetContents = QWidget()
		self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
		self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1140, 1042))
		self.verticalLayout_55 = QVBoxLayout(self.scrollAreaWidgetContents)
		self.verticalLayout_55.setSpacing(0)
		self.verticalLayout_55.setObjectName(u"verticalLayout_55")
		self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
		self.pages = QStackedWidget(self.scrollAreaWidgetContents)
		self.pages.setObjectName(u"pages")
		self.pages.setMaximumSize(QSize(1140, 16777215))
		self.pages.setFont(font)
		self.home = QWidget()
		self.home.setObjectName(u"home")
		self.home.setFont(font)
		self.verticalLayout_5 = QVBoxLayout(self.home)
		self.verticalLayout_5.setSpacing(0)
		self.verticalLayout_5.setObjectName(u"verticalLayout_5")
		self.verticalLayout_5.setContentsMargins(0, 160, 0, 0)
		self.area_principal = QFrame(self.home)
		self.area_principal.setObjectName(u"area_principal")
		self.area_principal.setMinimumSize(QSize(0, 238))
		self.area_principal.setFont(font)
		self.area_principal.setFrameShape(QFrame.StyledPanel)
		self.area_principal.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_4 = QHBoxLayout(self.area_principal)
		self.horizontalLayout_4.setSpacing(0)
		self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
		self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
		self.horizontalSpacer_3 = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

		self.principal_esq = QFrame(self.area_principal)
		self.principal_esq.setObjectName(u"principal_esq")
		self.principal_esq.setFont(font)
		self.principal_esq.setFrameShape(QFrame.StyledPanel)
		self.principal_esq.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_5 = QHBoxLayout(self.principal_esq)
		self.horizontalLayout_5.setSpacing(0)
		self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
		self.horizontalLayout_5.setContentsMargins(24, 0, 32, 0)
		self.box_dizimo = QFrame(self.principal_esq)
		self.box_dizimo.setObjectName(u"box_dizimo")
		self.box_dizimo.setMinimumSize(QSize(314, 0))
		self.box_dizimo.setFont(font)
		self.box_dizimo.setFrameShape(QFrame.StyledPanel)
		self.box_dizimo.setFrameShadow(QFrame.Raised)
		self.verticalLayout_6 = QVBoxLayout(self.box_dizimo)
		self.verticalLayout_6.setSpacing(0)
		self.verticalLayout_6.setObjectName(u"verticalLayout_6")
		self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
		self.label_dizimo = QLabel(self.box_dizimo)
		self.label_dizimo.setObjectName(u"label_dizimo")
		self.label_dizimo.setMinimumSize(QSize(0, 0))
		self.label_dizimo.setMaximumSize(QSize(312, 16777215))
		self.label_dizimo.setFont(font12)
		self.label_dizimo.setStyleSheet(u"color: #3A4B5E; padding-left: 16px; padding-bottom: 8px")

		self.verticalLayout_6.addWidget(self.label_dizimo)

		self.frame_dizimo = QFrame(self.box_dizimo)
		self.frame_dizimo.setObjectName(u"frame_dizimo")
		self.frame_dizimo.setMinimumSize(QSize(312, 185))
		self.frame_dizimo.setStyleSheet(u"QFrame#frame_dizimo{background-color: #fff; color: #3A4B5E; border-radius: 15px; border-width: 1px; border-style: solid; border-color: #c4c4c4}")
		self.frame_dizimo.setFrameShape(QFrame.StyledPanel)
		self.frame_dizimo.setFrameShadow(QFrame.Raised)
		self.verticalLayout_65 = QVBoxLayout(self.frame_dizimo)
		self.verticalLayout_65.setSpacing(0)
		self.verticalLayout_65.setObjectName(u"verticalLayout_65")
		self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
		self.label_10 = QLabel(self.frame_dizimo)
		self.label_10.setObjectName(u"label_10")
		font13 = QFont()
		font13.setPointSize(38)
		font13.setBold(True)
		self.label_10.setFont(font13)
		self.label_10.setStyleSheet(u"color: #3A4B5E; border-radius: 15px; border-width: 1px; border-style: hidden; ")
		self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

		self.verticalLayout_65.addWidget(self.label_10)

		self.label_11 = QLabel(self.frame_dizimo)
		self.label_11.setObjectName(u"label_11")
		self.label_11.setFont(font)
		self.label_11.setStyleSheet(u"color: #3A4B5E; border-radius: 15px; border-width: 1px; border-style: hidden; ")
		self.label_11.setAlignment(Qt.AlignCenter)

		self.verticalLayout_65.addWidget(self.label_11)

		self.label_12 = QLabel(self.frame_dizimo)
		self.label_12.setObjectName(u"label_12")
		font14 = QFont()
		font14.setPointSize(13)
		self.label_12.setFont(font14)
		self.label_12.setLayoutDirection(Qt.LeftToRight)
		self.label_12.setStyleSheet(u"color: #3A4B5E; border-radius: 15px; border-width: 1px; border-style: hidden; ")
		self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.verticalLayout_65.addWidget(self.label_12)

		self.verticalLayout_6.addWidget(self.frame_dizimo)

		self.horizontalLayout_5.addWidget(self.box_dizimo)

		self.horizontalLayout_4.addWidget(self.principal_esq)

		self.horizontalSpacer_20 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_4.addItem(self.horizontalSpacer_20)

		self.principal_dir = QFrame(self.area_principal)
		self.principal_dir.setObjectName(u"principal_dir")
		self.principal_dir.setFont(font)
		self.principal_dir.setFrameShape(QFrame.StyledPanel)
		self.principal_dir.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_6 = QHBoxLayout(self.principal_dir)
		self.horizontalLayout_6.setSpacing(0)
		self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
		self.horizontalLayout_6.setContentsMargins(32, 0, 24, 0)
		self.box_oferta = QFrame(self.principal_dir)
		self.box_oferta.setObjectName(u"box_oferta")
		self.box_oferta.setMinimumSize(QSize(313, 0))
		self.box_oferta.setFont(font)
		self.box_oferta.setFrameShape(QFrame.StyledPanel)
		self.box_oferta.setFrameShadow(QFrame.Raised)
		self.verticalLayout_7 = QVBoxLayout(self.box_oferta)
		self.verticalLayout_7.setSpacing(0)
		self.verticalLayout_7.setObjectName(u"verticalLayout_7")
		self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
		self.label_oferta = QLabel(self.box_oferta)
		self.label_oferta.setObjectName(u"label_oferta")
		self.label_oferta.setMinimumSize(QSize(0, 0))
		self.label_oferta.setMaximumSize(QSize(312, 16777215))
		self.label_oferta.setFont(font12)
		self.label_oferta.setStyleSheet(u"color: #3A4B5E; padding-left: 16px; padding-bottom: 8px")

		self.verticalLayout_7.addWidget(self.label_oferta)

		self.frame_ofertas = QFrame(self.box_oferta)
		self.frame_ofertas.setObjectName(u"frame_ofertas")
		self.frame_ofertas.setMinimumSize(QSize(312, 185))
		self.frame_ofertas.setStyleSheet(u"QFrame#frame_ofertas{background-color: #fff; color: #3A4B5E; border-radius: 15px; border-width: 1px; border-style: solid; border-color: #c4c4c4}")
		self.frame_ofertas.setFrameShape(QFrame.StyledPanel)
		self.frame_ofertas.setFrameShadow(QFrame.Raised)
		self.verticalLayout_66 = QVBoxLayout(self.frame_ofertas)
		self.verticalLayout_66.setSpacing(0)
		self.verticalLayout_66.setObjectName(u"verticalLayout_66")
		self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
		self.label_13 = QLabel(self.frame_ofertas)
		self.label_13.setObjectName(u"label_13")
		self.label_13.setFont(font13)
		self.label_13.setStyleSheet(u"color: #3A4B5E; border-radius: 15px; border-width: 1px; border-style: hidden; ")
		self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

		self.verticalLayout_66.addWidget(self.label_13)

		self.label_14 = QLabel(self.frame_ofertas)
		self.label_14.setObjectName(u"label_14")
		self.label_14.setFont(font)
		self.label_14.setStyleSheet(u"color: #3A4B5E; border-radius: 15px; border-width: 1px; border-style: hidden; ")
		self.label_14.setAlignment(Qt.AlignCenter)

		self.verticalLayout_66.addWidget(self.label_14)

		self.label_15 = QLabel(self.frame_ofertas)
		self.label_15.setObjectName(u"label_15")
		self.label_15.setFont(font14)
		self.label_15.setLayoutDirection(Qt.LeftToRight)
		self.label_15.setStyleSheet(u"color: #3A4B5E; border-radius: 15px; border-width: 1px; border-style: hidden; ")
		self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.verticalLayout_66.addWidget(self.label_15)


		self.verticalLayout_7.addWidget(self.frame_ofertas)


		self.horizontalLayout_6.addWidget(self.box_oferta)


		self.horizontalLayout_4.addWidget(self.principal_dir)

		self.horizontalSpacer_5 = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


		self.verticalLayout_5.addWidget(self.area_principal)

		self.verticalSpacer_2 = QSpacerItem(20, 537, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.verticalLayout_5.addItem(self.verticalSpacer_2)

		##########################################################
		#VALIDADOR INTEIRO
		self.validaInteiro = QRegularExpressionValidator(QRegularExpression("[0-9]+"))
		#VALIDADOR CEP
		self.validaCep = QRegularExpressionValidator(QRegularExpression("[0-9]{5}-[0-9]{3}"))
		#VALIDADOR DINHEIRO
		self.validaValor = QRegularExpressionValidator(QRegularExpression("[0-9]+,?[0-9]{0,2}"))
		#VALIDADOR TEXTO
		self.validaTexto = QRegularExpressionValidator(QRegularExpression("[a-zA-z0-9 çáàãâéíóôõúÇÁÀÃÂÉÍÓÔÕÚ\\.-]+"))
		#VALIDADOR DATA
		self.validaData = QRegularExpressionValidator(QRegularExpression("([0-9]{2}/){2}[0-9]{4}"))
		#VALIDADADOR TELEFONE
		self.validaTelefone = QRegularExpressionValidator(QRegularExpression("[0-9]{2} [0-9]{4,5}-[0-9]{4}"))
		#VALIDADOR NOME
		self.validaNome = QRegularExpressionValidator(QRegularExpression("[a-zA-z çáàãâéíóôõúÇÁÀÃÂÉÍÓÔÕÚ-]+"))
		#VALIDADOR EMAIL
		self.validaEmail = QRegularExpressionValidator(QRegularExpression("([a-z0-9]+[.-_])*[a-z0-9]+@[a-z]+(\\.[a-z]{2,})+"))
		##########################################################        

		self.pages.addWidget(self.home)
		self.membros = QWidget()
		self.membros.setObjectName(u"membros")
		self.membros.setFont(font)
		self.verticalLayout_58 = QVBoxLayout(self.membros)
		self.verticalLayout_58.setSpacing(0)
		self.verticalLayout_58.setObjectName(u"verticalLayout_58")
		self.verticalLayout_58.setContentsMargins(56, 64, 56, 64)
		self.main_membros = QFrame(self.membros)
		self.main_membros.setObjectName(u"main_membros")
		self.main_membros.setFont(font)
		self.main_membros.setStyleSheet(u"#main_membros{background-color: #fff; border-radius:15px;}")
		self.main_membros.setFrameShape(QFrame.StyledPanel)
		self.main_membros.setFrameShadow(QFrame.Raised)
		self.verticalLayout_57 = QVBoxLayout(self.main_membros)
		self.verticalLayout_57.setSpacing(0)
		self.verticalLayout_57.setObjectName(u"verticalLayout_57")
		self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
		self.superior_membros = QFrame(self.main_membros)
		self.superior_membros.setObjectName(u"superior_membros")
		self.superior_membros.setMaximumSize(QSize(16777215, 105))
		font15 = QFont()
		font15.setPointSize(32)
		font15.setBold(True)
		self.superior_membros.setFont(font15)
		self.superior_membros.setFrameShape(QFrame.StyledPanel)
		self.superior_membros.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_37 = QHBoxLayout(self.superior_membros)
		self.horizontalLayout_37.setSpacing(0)
		self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
		self.horizontalLayout_37.setContentsMargins(0, 40, 24, 0)
		self.label_9 = QLabel(self.superior_membros)
		self.label_9.setObjectName(u"label_9")
		self.label_9.setMaximumSize(QSize(16777215, 16777215))
		self.label_9.setFont(font15)
		self.label_9.setStyleSheet(u"color: #3A4B5E")
		self.label_9.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_37.addWidget(self.label_9)

		self.searchbox = QFrame(self.superior_membros)
		self.searchbox.setObjectName(u"searchbox")
		self.searchbox.setMinimumSize(QSize(0, 0))
		self.searchbox.setMaximumSize(QSize(220, 38))
		self.searchbox.setFocusPolicy(Qt.StrongFocus)
		self.searchbox.setStyleSheet(u"QFrame#searchbox{border-radius: 19px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:14px}")
		self.searchbox.setFrameShape(QFrame.StyledPanel)
		self.searchbox.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_38 = QHBoxLayout(self.searchbox)
		self.horizontalLayout_38.setSpacing(6)
		self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
		self.horizontalLayout_38.setContentsMargins(0, 0, 8, 0)
		self.lineEdit_busca_membro = LineEdit(self.searchbox)
		self.lineEdit_busca_membro.setObjectName(u"lineEdit_busca_membro")
		self.lineEdit_busca_membro.setMinimumSize(QSize(0, 36))
		self.lineEdit_busca_membro.setFont(font14)
		self.lineEdit_busca_membro.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_busca_membro.setStyleSheet(u"QLineEdit{border-bottom-right-radius: 0px ; border-top-right-radius: 0px ;border-right: 1px solid #c4c4c4;}")

		self.horizontalLayout_38.addWidget(self.lineEdit_busca_membro)

		self.toolButton_busca_membro = QToolButton(self.searchbox)
		self.toolButton_busca_membro.setObjectName(u"toolButton_busca_membro")
		self.toolButton_busca_membro.setStyleSheet("background-color:#fff; border:hidden")
		self.toolButton_busca_membro.setCursor(QCursor(Qt.PointingHandCursor))
		self.toolButton_busca_membro.setFocusPolicy(Qt.StrongFocus)
		icon1 = QIcon()
		icon1.addFile(u"icons/search_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
		self.toolButton_busca_membro.setIcon(icon1)
		self.toolButton_busca_membro.setIconSize(QSize(24, 24))

		self.horizontalLayout_38.addWidget(self.toolButton_busca_membro)

		self.horizontalLayout_37.addWidget(self.searchbox)

		self.verticalLayout_57.addWidget(self.superior_membros)

		self.meio_membros = QFrame(self.main_membros)
		self.meio_membros.setObjectName(u"meio_membros")
		self.meio_membros.setMinimumSize(QSize(0, 660))
		self.meio_membros.setFont(font)
		self.meio_membros.setFrameShape(QFrame.StyledPanel)
		self.meio_membros.setFrameShadow(QFrame.Raised)
		self.verticalLayout_59 = QVBoxLayout(self.meio_membros)
		self.verticalLayout_59.setSpacing(0)
		self.verticalLayout_59.setObjectName(u"verticalLayout_59")
		self.verticalLayout_59.setContentsMargins(40, 0, 40, 48)
		self.meio_membros_2 = QFrame(self.meio_membros)
		self.meio_membros_2.setObjectName(u"meio_membros_2")
		self.meio_membros_2.setStyleSheet("background-color:#fff; border:hidden")
		self.meio_membros_2.setMinimumSize(QSize(0, 0))
		self.meio_membros_2.setMaximumSize(QSize(16777215, 16777215))
		self.meio_membros_2.setFont(font)
		self.meio_membros_2.setFrameShape(QFrame.StyledPanel)
		self.meio_membros_2.setFrameShadow(QFrame.Raised)
		self.verticalLayout_60 = QVBoxLayout(self.meio_membros_2)
		self.verticalLayout_60.setSpacing(0)
		self.verticalLayout_60.setObjectName(u"verticalLayout_60")
		self.verticalLayout_60.setContentsMargins(0, 80, 0, 0)
		self.tableWidget_membros = QTableWidget(self.meio_membros_2)
		if (self.tableWidget_membros.columnCount() < 4):
			self.tableWidget_membros.setColumnCount(4)

		font16 = QFont()
		font16.setPointSize(18)
		font16.setUnderline(True)

		__qtablewidgetitem99 = QTableWidgetItem()
		__qtablewidgetitem99.setFont(font16);
		__qtablewidgetitem99.setForeground(QColor('#3A4B5E'))
		self.tableWidget_membros.setHorizontalHeaderItem(0, __qtablewidgetitem99)
		__qtablewidgetitem = QTableWidgetItem()
		__qtablewidgetitem.setTextAlignment(Qt.AlignLeft)
		__qtablewidgetitem.setFont(font16);
		__qtablewidgetitem.setForeground(QColor('#3A4B5E'))
		self.tableWidget_membros.setHorizontalHeaderItem(1, __qtablewidgetitem)
		__qtablewidgetitem1 = QTableWidgetItem()
		__qtablewidgetitem1.setFont(font16);
		__qtablewidgetitem1.setForeground(QColor('#3A4B5E'))
		self.tableWidget_membros.setHorizontalHeaderItem(2, __qtablewidgetitem1)
		__qtablewidgetitem2 = QTableWidgetItem()
		__qtablewidgetitem2.setFont(font16);
		__qtablewidgetitem2.setForeground(QColor('#3A4B5E'))
		self.tableWidget_membros.setHorizontalHeaderItem(3, __qtablewidgetitem2)
		self.tableWidget_membros.setObjectName(u"tableWidget_membros")
		self.tableWidget_membros.setFont(font2)
		self.tableWidget_membros.setStyleSheet(u"QTableView{color: #3A4B5E; border:hidden} QTableView::item:focus{outline:0}")
		self.tableWidget_membros.setFocusPolicy(Qt.ClickFocus)
		self.tableWidget_membros.horizontalHeader().setStyleSheet(u"QHeaderView::Section:first{padding-left: 62px} QHeaderView::Section{padding-bottom: 24px; background-color: #fff; border:hidden}")
		self.tableWidget_membros.horizontalHeader().setHighlightSections(False)
		self.tableWidget_membros.setEditTriggers(QAbstractItemView.SelectedClicked|QAbstractItemView.AnyKeyPressed)
		self.tableWidget_membros.setSelectionMode(QAbstractItemView.SingleSelection)
		self.tableWidget_membros.setAlternatingRowColors(True)
		self.tableWidget_membros.setShowGrid(False)
		self.tableWidget_membros.setSortingEnabled(True)
		self.tableWidget_membros.horizontalHeader().setCascadingSectionResizes(False)
		self.tableWidget_membros.horizontalHeader().setStretchLastSection(False)
		self.tableWidget_membros.verticalHeader().setVisible(True)
		self.tableWidget_membros.verticalHeader().setStretchLastSection(False)

		self.verticalLayout_60.addWidget(self.tableWidget_membros)

		self.verticalLayout_59.addWidget(self.meio_membros_2)

		self.verticalLayout_57.addWidget(self.meio_membros)

		self.verticalLayout_58.addWidget(self.main_membros)

		self.pages.addWidget(self.membros)
		self.hist_membros = QWidget()
		self.hist_membros.setObjectName(u"hist_membros")
		self.hist_membros.setFont(font)
		self.verticalLayout_64 = QVBoxLayout(self.hist_membros)
		self.verticalLayout_64.setSpacing(0)
		self.verticalLayout_64.setObjectName(u"verticalLayout_64")
		self.verticalLayout_64.setContentsMargins(56, 64, 56, 64)
		self.main_historico = QFrame(self.hist_membros)
		self.main_historico.setObjectName(u"main_historico")
		self.main_historico.setFont(font)
		self.main_historico.setStyleSheet(u"#main_historico{background-color: #fff; border-radius:15px;}")
		self.main_historico.setFrameShape(QFrame.StyledPanel)
		self.main_historico.setFrameShadow(QFrame.Raised)
		self.verticalLayout_61 = QVBoxLayout(self.main_historico)
		self.verticalLayout_61.setSpacing(0)
		self.verticalLayout_61.setObjectName(u"verticalLayout_61")
		self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
		self.superior_historico = QFrame(self.main_historico)
		self.superior_historico.setObjectName(u"superior_historico")
		self.superior_historico.setMaximumSize(QSize(16777215, 105))
		self.superior_historico.setFont(font15)
		self.superior_historico.setFrameShape(QFrame.StyledPanel)
		self.superior_historico.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_39 = QHBoxLayout(self.superior_historico)
		self.horizontalLayout_39.setSpacing(0)
		self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
		self.horizontalLayout_39.setContentsMargins(0, 40, 0, 0)
		self.label_hist_nome_membro = QLabel(self.superior_historico)
		self.label_hist_nome_membro.setObjectName(u"label_hist_nome_membro")
		self.label_hist_nome_membro.setMaximumSize(QSize(16777215, 16777215))
		font17 = QFont()
		font17.setPointSize(30)
		font17.setBold(True)
		self.label_hist_nome_membro.setFont(font17)
		self.label_hist_nome_membro.setStyleSheet(u"color: #3A4B5E")
		self.label_hist_nome_membro.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_39.addWidget(self.label_hist_nome_membro)

		self.verticalLayout_61.addWidget(self.superior_historico)

		self.meio_historico = QFrame(self.main_historico)
		self.meio_historico.setObjectName(u"meio_historico")
		self.meio_historico.setMinimumSize(QSize(0, 660))
		self.meio_historico.setFont(font)
		self.meio_historico.setFrameShape(QFrame.StyledPanel)
		self.meio_historico.setFrameShadow(QFrame.Raised)
		self.verticalLayout_62 = QVBoxLayout(self.meio_historico)
		self.verticalLayout_62.setSpacing(0)
		self.verticalLayout_62.setObjectName(u"verticalLayout_62")
		self.verticalLayout_62.setContentsMargins(40, 0, 40, 48)
		self.meio_historico_2 = QFrame(self.meio_historico)
		self.meio_historico_2.setObjectName(u"meio_historico_2")
		self.meio_historico_2.setStyleSheet("background-color:#fff")
		self.meio_historico_2.setMinimumSize(QSize(0, 0))
		self.meio_historico_2.setMaximumSize(QSize(16777215, 16777215))
		self.meio_historico_2.setFont(font)
		self.meio_historico_2.setFrameShape(QFrame.StyledPanel)
		self.meio_historico_2.setFrameShadow(QFrame.Raised)
		self.verticalLayout_63 = QVBoxLayout(self.meio_historico_2)
		self.verticalLayout_63.setSpacing(0)
		self.verticalLayout_63.setObjectName(u"verticalLayout_63")
		self.verticalLayout_63.setContentsMargins(0, 80, 0, 0)
		self.tableWidget_historico = QTableWidget(self.meio_historico_2)
		if (self.tableWidget_historico.columnCount() < 6):
			self.tableWidget_historico.setColumnCount(6)
		__qtablewidgetitem3 = QTableWidgetItem()
		__qtablewidgetitem3.setFont(font16);
		__qtablewidgetitem3.setForeground(QColor('#3A4B5E'))
		self.tableWidget_historico.setHorizontalHeaderItem(0, __qtablewidgetitem3)
		__qtablewidgetitem4 = QTableWidgetItem()
		__qtablewidgetitem4.setFont(font16);
		__qtablewidgetitem4.setForeground(QColor('#3A4B5E'))
		self.tableWidget_historico.setHorizontalHeaderItem(1, __qtablewidgetitem4)
		__qtablewidgetitem5 = QTableWidgetItem()
		__qtablewidgetitem5.setFont(font16);
		__qtablewidgetitem5.setForeground(QColor('#3A4B5E'))
		self.tableWidget_historico.setHorizontalHeaderItem(2, __qtablewidgetitem5)
		__qtablewidgetitem6 = QTableWidgetItem()
		__qtablewidgetitem6.setFont(font16);
		__qtablewidgetitem6.setForeground(QColor('#3A4B5E'))
		self.tableWidget_historico.setHorizontalHeaderItem(3, __qtablewidgetitem6)
		__qtablewidgetitem7 = QTableWidgetItem()
		__qtablewidgetitem7.setFont(font16);
		__qtablewidgetitem7.setForeground(QColor('#3A4B5E'))
		self.tableWidget_historico.setHorizontalHeaderItem(4, __qtablewidgetitem7)
		__qtablewidgetitem8 = QTableWidgetItem()
		__qtablewidgetitem8.setFont(font16);
		__qtablewidgetitem8.setForeground(QColor('#3A4B5E'))
		self.tableWidget_historico.setHorizontalHeaderItem(5, __qtablewidgetitem8)
		self.tableWidget_historico.horizontalHeader().setStyleSheet(u"QHeaderView::Section{padding-bottom:24px; background-color:#fff; border:hidden}")
		self.tableWidget_historico.setObjectName(u"tableWidget_historico")
		self.tableWidget_historico.setEnabled(True)
		self.tableWidget_historico.setFont(font2)
		self.tableWidget_historico.setFocusPolicy(Qt.NoFocus)
		self.tableWidget_historico.setStyleSheet(u"QTableView{color:#3A4B5E; border:hidden} QTableView::item:focus{outline:0} QTableView::item{padding-left:8px; padding-right:8px}")
		self.tableWidget_historico.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_historico.setSelectionMode(QAbstractItemView.NoSelection)
		self.tableWidget_historico.setAlternatingRowColors(True)
		self.tableWidget_historico.setShowGrid(False)
		self.tableWidget_historico.setSortingEnabled(False)
		self.tableWidget_historico.horizontalHeader().setCascadingSectionResizes(False)
		self.tableWidget_historico.horizontalHeader().setStretchLastSection(False)
		self.tableWidget_historico.verticalHeader().setVisible(True)
		self.tableWidget_historico.verticalHeader().setStretchLastSection(False)

		self.verticalLayout_63.addWidget(self.tableWidget_historico)

		self.verticalLayout_62.addWidget(self.meio_historico_2)

		self.verticalLayout_61.addWidget(self.meio_historico)

		self.verticalLayout_64.addWidget(self.main_historico)

		self.pages.addWidget(self.hist_membros)
		self.cadastro = QWidget()
		self.cadastro.setObjectName(u"cadastro")
		self.cadastro.setFont(font)
		self.cadastro.setContextMenuPolicy(Qt.ActionsContextMenu)
		self.verticalLayout_8 = QVBoxLayout(self.cadastro)
		self.verticalLayout_8.setSpacing(0)
		self.verticalLayout_8.setObjectName(u"verticalLayout_8")
		self.verticalLayout_8.setContentsMargins(56, 64, 56, 64)
		self.main_cadastro = QFrame(self.cadastro)
		self.main_cadastro.setObjectName(u"main_cadastro")
		self.main_cadastro.setMaximumSize(QSize(1299, 16777215))
		self.main_cadastro.setFont(font)
		self.main_cadastro.setLayoutDirection(Qt.LeftToRight)
		self.main_cadastro.setStyleSheet(u"background-color: #fff; border-radius: 15px")
		self.main_cadastro.setFrameShape(QFrame.StyledPanel)
		self.main_cadastro.setFrameShadow(QFrame.Raised)
		self.verticalLayout_10 = QVBoxLayout(self.main_cadastro)
		self.verticalLayout_10.setSpacing(0)
		self.verticalLayout_10.setObjectName(u"verticalLayout_10")
		self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
		self.superior_cadastro = QFrame(self.main_cadastro)
		self.superior_cadastro.setObjectName(u"superior_cadastro")
		self.superior_cadastro.setMaximumSize(QSize(16777215, 105))
		self.superior_cadastro.setFont(font15)
		self.superior_cadastro.setFrameShape(QFrame.StyledPanel)
		self.superior_cadastro.setFrameShadow(QFrame.Raised)
		self.verticalLayout_11 = QVBoxLayout(self.superior_cadastro)
		self.verticalLayout_11.setSpacing(0)
		self.verticalLayout_11.setObjectName(u"verticalLayout_11")
		self.verticalLayout_11.setContentsMargins(0, 40, 0, 0)
		self.label_2 = QLabel(self.superior_cadastro)
		self.label_2.setObjectName(u"label_2")
		self.label_2.setMaximumSize(QSize(16777215, 16777215))
		self.label_2.setFont(font15)
		self.label_2.setStyleSheet(u"color: #3A4B5E")
		self.label_2.setAlignment(Qt.AlignCenter)

		self.verticalLayout_11.addWidget(self.label_2)

		self.verticalLayout_10.addWidget(self.superior_cadastro)

		self.meio_cadastro = QFrame(self.main_cadastro)
		self.meio_cadastro.setObjectName(u"meio_cadastro")
		self.meio_cadastro.setFont(font)
		self.meio_cadastro.setFrameShape(QFrame.StyledPanel)
		self.meio_cadastro.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_21 = QHBoxLayout(self.meio_cadastro)
		self.horizontalLayout_21.setSpacing(0)
		self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
		self.horizontalLayout_21.setContentsMargins(40, 0, 40, 0)
		self.horizontalSpacer_4 = QSpacerItem(27, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_21.addItem(self.horizontalSpacer_4)

		self.meio_cadastro_2 = QFrame(self.meio_cadastro)
		self.meio_cadastro_2.setObjectName(u"meio_cadastro_2")
		self.meio_cadastro_2.setMaximumSize(QSize(1028, 16777215))
		self.meio_cadastro_2.setFont(font)
		self.meio_cadastro_2.setFrameShape(QFrame.StyledPanel)
		self.meio_cadastro_2.setFrameShadow(QFrame.Raised)
		self.verticalLayout_12 = QVBoxLayout(self.meio_cadastro_2)
		self.verticalLayout_12.setSpacing(4)
		self.verticalLayout_12.setObjectName(u"verticalLayout_12")
		self.verticalLayout_12.setContentsMargins(0, 64, 0, 0)
		self.frame_7 = QFrame(self.meio_cadastro_2)
		self.frame_7.setObjectName(u"frame_7")
		self.frame_7.setFont(font)
		self.frame_7.setFrameShape(QFrame.StyledPanel)
		self.frame_7.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
		self.horizontalLayout_9.setSpacing(16)
		self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
		self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
		self.frame_27 = QFrame(self.frame_7)
		self.frame_27.setObjectName(u"frame_27")
		self.frame_27.setFrameShape(QFrame.StyledPanel)
		self.frame_27.setFrameShadow(QFrame.Raised)
		self.verticalLayout_39 = QVBoxLayout(self.frame_27)
		self.verticalLayout_39.setSpacing(4)
		self.verticalLayout_39.setObjectName(u"verticalLayout_39")
		self.verticalLayout_39.setContentsMargins(0, 0, 0, 2)
		self.label_aviso_nome_cad = QLabel(self.frame_27)
		self.label_aviso_nome_cad.setObjectName(u"label_aviso_nome_cad")
		font18 = QFont()
		font18.setPointSize(10)
		self.label_aviso_nome_cad.setFont(font18)
		self.label_aviso_nome_cad.setStyleSheet(u"color: red; padding-left: 18px")

		self.verticalLayout_39.addWidget(self.label_aviso_nome_cad)

		self.lineEdit_nome_cad = QLineEdit(self.frame_27)
		self.lineEdit_nome_cad.setObjectName(u"lineEdit_nome_cad")
		self.lineEdit_nome_cad.setMinimumSize(QSize(0, 44))
		self.lineEdit_nome_cad.setFont(font2)
		self.lineEdit_nome_cad.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_nome_cad.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		######################################################
		self.lineEdit_nome_cad.setValidator(self.validaNome)
		self.lineEdit_nome_cad.setMaxLength(255)
		######################################################

		self.verticalLayout_39.addWidget(self.lineEdit_nome_cad)

		self.horizontalLayout_9.addWidget(self.frame_27)

		self.frame_33 = QFrame(self.frame_7)
		self.frame_33.setObjectName(u"frame_33")
		self.frame_33.setMaximumSize(QSize(206, 16777215))
		self.frame_33.setFrameShape(QFrame.StyledPanel)
		self.frame_33.setFrameShadow(QFrame.Raised)
		self.verticalLayout_40 = QVBoxLayout(self.frame_33)
		self.verticalLayout_40.setSpacing(4)
		self.verticalLayout_40.setObjectName(u"verticalLayout_40")
		self.verticalLayout_40.setContentsMargins(0, 0, 0, 2)
		self.label_aviso_data_nasc = QLabel(self.frame_33)
		self.label_aviso_data_nasc.setObjectName(u"label_aviso_data_nasc")
		self.label_aviso_data_nasc.setFont(font18)
		self.label_aviso_data_nasc.setStyleSheet(u"color: red;")
		self.label_aviso_data_nasc.setAlignment(Qt.AlignCenter)

		self.verticalLayout_40.addWidget(self.label_aviso_data_nasc)

		self.lineEdit_data_nasc = QLineEdit(self.frame_33)
		self.lineEdit_data_nasc.setObjectName(u"lineEdit_data_nasc")
		self.lineEdit_data_nasc.setMinimumSize(QSize(0, 44))
		self.lineEdit_data_nasc.setMaximumSize(QSize(206, 16777215))
		self.lineEdit_data_nasc.setFont(font2)
		self.lineEdit_data_nasc.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_data_nasc.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		#######################################################
		self.lineEdit_data_nasc.setValidator(self.validaData)
		self.lineEdit_data_nasc.setMaxLength(10)
		self.lineEdit_data_nasc.setInputMethodHints(Qt.ImhDate)
		#######################################################

		self.verticalLayout_40.addWidget(self.lineEdit_data_nasc)

		self.horizontalLayout_9.addWidget(self.frame_33)

		self.verticalLayout_12.addWidget(self.frame_7)

		self.frame_8 = QFrame(self.meio_cadastro_2)
		self.frame_8.setObjectName(u"frame_8")
		self.frame_8.setFont(font)
		self.frame_8.setFrameShape(QFrame.StyledPanel)
		self.frame_8.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
		self.horizontalLayout_10.setSpacing(16)
		self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
		self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
		self.frame_34 = QFrame(self.frame_8)
		self.frame_34.setObjectName(u"frame_34")
		self.frame_34.setFrameShape(QFrame.StyledPanel)
		self.frame_34.setFrameShadow(QFrame.Raised)
		self.verticalLayout_41 = QVBoxLayout(self.frame_34)
		self.verticalLayout_41.setSpacing(4)
		self.verticalLayout_41.setObjectName(u"verticalLayout_41")
		self.verticalLayout_41.setContentsMargins(0, 3, 0, 2)
		self.label_aviso_endereco = QLabel(self.frame_34)
		self.label_aviso_endereco.setObjectName(u"label_aviso_endereco")
		self.label_aviso_endereco.setFont(font18)
		self.label_aviso_endereco.setStyleSheet(u"color: red; padding-left: 14px")

		self.verticalLayout_41.addWidget(self.label_aviso_endereco)

		self.lineEdit_endereco = QLineEdit(self.frame_34)
		self.lineEdit_endereco.setObjectName(u"lineEdit_endereco")
		self.lineEdit_endereco.setMinimumSize(QSize(0, 44))
		self.lineEdit_endereco.setFont(font2)
		self.lineEdit_endereco.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_endereco.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		######################################################
		self.lineEdit_endereco.setValidator(self.validaTexto)
		self.lineEdit_endereco.setMaxLength(255)
		######################################################

		self.verticalLayout_41.addWidget(self.lineEdit_endereco)

		self.horizontalLayout_10.addWidget(self.frame_34)

		self.frame_35 = QFrame(self.frame_8)
		self.frame_35.setObjectName(u"frame_35")
		self.frame_35.setMaximumSize(QSize(206, 16777215))
		self.frame_35.setFrameShape(QFrame.StyledPanel)
		self.frame_35.setFrameShadow(QFrame.Raised)
		self.verticalLayout_42 = QVBoxLayout(self.frame_35)
		self.verticalLayout_42.setSpacing(4)
		self.verticalLayout_42.setObjectName(u"verticalLayout_42")
		self.verticalLayout_42.setContentsMargins(0, 3, 0, 2)
		self.label_aviso_numero = QLabel(self.frame_35)
		self.label_aviso_numero.setObjectName(u"label_aviso_numero")
		self.label_aviso_numero.setFont(font18)
		self.label_aviso_numero.setStyleSheet(u"color: red;")
		self.label_aviso_numero.setAlignment(Qt.AlignCenter)

		self.verticalLayout_42.addWidget(self.label_aviso_numero)

		self.lineEdit_numero = QLineEdit(self.frame_35)
		self.lineEdit_numero.setObjectName(u"lineEdit_numero")
		self.lineEdit_numero.setMinimumSize(QSize(0, 44))
		self.lineEdit_numero.setMaximumSize(QSize(206, 16777215))
		self.lineEdit_numero.setFont(font2)
		self.lineEdit_numero.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_numero.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		######################################################
		self.lineEdit_numero.setValidator(self.validaInteiro)
		self.lineEdit_numero.setMaxLength(10)
		self.lineEdit_numero.setInputMethodHints(Qt.ImhDigitsOnly)
		######################################################

		self.verticalLayout_42.addWidget(self.lineEdit_numero)

		self.horizontalLayout_10.addWidget(self.frame_35)

		self.verticalLayout_12.addWidget(self.frame_8)

		self.frame_9 = QFrame(self.meio_cadastro_2)
		self.frame_9.setObjectName(u"frame_9")
		self.frame_9.setFont(font)
		self.frame_9.setFrameShape(QFrame.StyledPanel)
		self.frame_9.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
		self.horizontalLayout_11.setSpacing(16)
		self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
		self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
		self.frame_36 = QFrame(self.frame_9)
		self.frame_36.setObjectName(u"frame_36")
		self.frame_36.setFrameShape(QFrame.StyledPanel)
		self.frame_36.setFrameShadow(QFrame.Raised)
		self.verticalLayout_43 = QVBoxLayout(self.frame_36)
		self.verticalLayout_43.setSpacing(5)
		self.verticalLayout_43.setObjectName(u"verticalLayout_43")
		self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_complemento = QLabel(self.frame_36)
		self.label_aviso_complemento.setObjectName(u"label_aviso_complemento")
		self.label_aviso_complemento.setFont(font18)
		self.label_aviso_complemento.setStyleSheet(u"color: red; padding-left: 14px")

		self.verticalLayout_43.addWidget(self.label_aviso_complemento)

		self.lineEdit_complemento = QLineEdit(self.frame_36)
		self.lineEdit_complemento.setObjectName(u"lineEdit_complemento")
		self.lineEdit_complemento.setMinimumSize(QSize(0, 44))
		self.lineEdit_complemento.setFont(font2)
		self.lineEdit_complemento.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_complemento.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		######################################################
		self.lineEdit_complemento.setValidator(self.validaTexto)
		self.lineEdit_complemento.setMaxLength(255)
		######################################################

		self.verticalLayout_43.addWidget(self.lineEdit_complemento)

		self.horizontalLayout_11.addWidget(self.frame_36)

		self.frame_37 = QFrame(self.frame_9)
		self.frame_37.setObjectName(u"frame_37")
		self.frame_37.setMaximumSize(QSize(400, 16777215))
		self.frame_37.setFrameShape(QFrame.StyledPanel)
		self.frame_37.setFrameShadow(QFrame.Raised)
		self.verticalLayout_44 = QVBoxLayout(self.frame_37)
		self.verticalLayout_44.setSpacing(5)
		self.verticalLayout_44.setObjectName(u"verticalLayout_44")
		self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_bairro = QLabel(self.frame_37)
		self.label_aviso_bairro.setObjectName(u"label_aviso_bairro")
		self.label_aviso_bairro.setFont(font18)
		self.label_aviso_bairro.setStyleSheet(u"color: red; padding-left: 14px")

		self.verticalLayout_44.addWidget(self.label_aviso_bairro)

		self.lineEdit_bairro = QLineEdit(self.frame_37)
		self.lineEdit_bairro.setObjectName(u"lineEdit_bairro")
		self.lineEdit_bairro.setMinimumSize(QSize(0, 44))
		self.lineEdit_bairro.setMaximumSize(QSize(400, 16777215))
		self.lineEdit_bairro.setFont(font2)
		self.lineEdit_bairro.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_bairro.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		######################################################
		self.lineEdit_bairro.setValidator(self.validaTexto)
		self.lineEdit_bairro.setMaxLength(255)
		######################################################

		self.verticalLayout_44.addWidget(self.lineEdit_bairro)

		self.horizontalLayout_11.addWidget(self.frame_37)

		self.verticalLayout_12.addWidget(self.frame_9)

		self.frame_10 = QFrame(self.meio_cadastro_2)
		self.frame_10.setObjectName(u"frame_10")
		self.frame_10.setFont(font)
		self.frame_10.setFrameShape(QFrame.StyledPanel)
		self.frame_10.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
		self.horizontalLayout_12.setSpacing(16)
		self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
		self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
		self.frame_40 = QFrame(self.frame_10)
		self.frame_40.setObjectName(u"frame_40")
		self.frame_40.setStyleSheet(u"")
		self.frame_40.setFrameShape(QFrame.StyledPanel)
		self.frame_40.setFrameShadow(QFrame.Raised)
		self.verticalLayout_47 = QVBoxLayout(self.frame_40)
		self.verticalLayout_47.setSpacing(4)
		self.verticalLayout_47.setObjectName(u"verticalLayout_47")
		self.verticalLayout_47.setContentsMargins(0, 3, 0, 2)
		self.label_17 = QLabel(self.frame_40)
		self.label_17.setObjectName(u"label_17")

		self.verticalLayout_47.addWidget(self.label_17)

		self.comboBox_uf = QComboBox(self.frame_40)
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.addItem("")
		self.comboBox_uf.setObjectName(u"comboBox_uf")
		self.comboBox_uf.setMinimumSize(QSize(85, 44))
		self.comboBox_uf.setMaximumSize(QSize(16777215, 16777215))
		self.comboBox_uf.setFont(font2)
		self.comboBox_uf.setStyleSheet(u'''QComboBox:hover{border-color:#28A745;}
	QComboBox:focus{border-color:#28A745;}QComboBox{color: #848484; border-radius: 10px; border-width: 1px; border-style: solid; border-color:#c4c4c4; padding-left: 10px;}
	QComboBox:drop-down:hover{background-color:#eeeeee}
	QComboBox:drop-down{width: 24px; border-top-right-radius:9px; border-bottom-right-radius:9px; border-top-left-radius:1px; border-bottom-left-radius:1px;}
	QComboBox:down-arrow{image: url(icons/expand_more_blue_18dp.svg); width: 18px; height: 18px;}
	''')
		self.comboBox_uf.setCursor(QCursor(Qt.PointingHandCursor))

		self.verticalLayout_47.addWidget(self.comboBox_uf)

		self.horizontalLayout_12.addWidget(self.frame_40)

		self.frame_38 = QFrame(self.frame_10)
		self.frame_38.setObjectName(u"frame_38")
		self.frame_38.setStyleSheet(u"")
		self.frame_38.setFrameShape(QFrame.StyledPanel)
		self.frame_38.setFrameShadow(QFrame.Raised)
		self.verticalLayout_45 = QVBoxLayout(self.frame_38)
		self.verticalLayout_45.setSpacing(4)
		self.verticalLayout_45.setObjectName(u"verticalLayout_45")
		self.verticalLayout_45.setContentsMargins(0, 3, 0, 2)
		self.label_aviso_cidade = QLabel(self.frame_38)
		self.label_aviso_cidade.setObjectName(u"label_aviso_cidade")
		self.label_aviso_cidade.setFont(font18)
		self.label_aviso_cidade.setStyleSheet(u"color: red; padding-left: 14px")

		self.verticalLayout_45.addWidget(self.label_aviso_cidade)

		self.lineEdit_cidade = QLineEdit(self.frame_38)
		self.lineEdit_cidade.setObjectName(u"lineEdit_cidade")
		self.lineEdit_cidade.setMinimumSize(QSize(0, 44))
		self.lineEdit_cidade.setMaximumSize(QSize(16777215, 16777215))
		self.lineEdit_cidade.setFont(font2)
		self.lineEdit_cidade.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_cidade.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		######################################################
		self.lineEdit_cidade.setValidator(self.validaTexto)
		self.lineEdit_cidade.setMaxLength(255)
		######################################################

		self.verticalLayout_45.addWidget(self.lineEdit_cidade)

		self.horizontalLayout_12.addWidget(self.frame_38)

		self.frame_39 = QFrame(self.frame_10)
		self.frame_39.setObjectName(u"frame_39")
		self.frame_39.setMaximumSize(QSize(255, 16777215))
		self.frame_39.setStyleSheet(u"")
		self.frame_39.setFrameShape(QFrame.StyledPanel)
		self.frame_39.setFrameShadow(QFrame.Raised)
		self.verticalLayout_46 = QVBoxLayout(self.frame_39)
		self.verticalLayout_46.setSpacing(4)
		self.verticalLayout_46.setObjectName(u"verticalLayout_46")
		self.verticalLayout_46.setContentsMargins(0, 3, 0, 2)
		self.label_aviso_cep = QLabel(self.frame_39)
		self.label_aviso_cep.setObjectName(u"label_aviso_cep")
		self.label_aviso_cep.setFont(font18)
		self.label_aviso_cep.setStyleSheet(u"color: red; padding-left: 14px")

		self.verticalLayout_46.addWidget(self.label_aviso_cep)

		self.lineEdit_cep = QLineEdit(self.frame_39)
		self.lineEdit_cep.setObjectName(u"lineEdit_cep")
		self.lineEdit_cep.setMinimumSize(QSize(0, 44))
		self.lineEdit_cep.setMaximumSize(QSize(255, 16777215))
		self.lineEdit_cep.setFont(font2)
		self.lineEdit_cep.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_cep.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		######################################################
		self.lineEdit_cep.setValidator(self.validaCep)
		self.lineEdit_cep.setMaxLength(9)
		self.lineEdit_cep.setInputMethodHints(Qt.ImhDigitsOnly)
		######################################################

		self.verticalLayout_46.addWidget(self.lineEdit_cep)

		self.horizontalLayout_12.addWidget(self.frame_39)

		self.verticalLayout_12.addWidget(self.frame_10)

		self.frame_11 = QFrame(self.meio_cadastro_2)
		self.frame_11.setObjectName(u"frame_11")
		self.frame_11.setFont(font)
		self.frame_11.setFrameShape(QFrame.StyledPanel)
		self.frame_11.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_13 = QHBoxLayout(self.frame_11)
		self.horizontalLayout_13.setSpacing(16)
		self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
		self.horizontalLayout_13.setContentsMargins(0, 3, 0, 24)
		self.frame_41 = QFrame(self.frame_11)
		self.frame_41.setObjectName(u"frame_41")
		self.frame_41.setFrameShape(QFrame.StyledPanel)
		self.frame_41.setFrameShadow(QFrame.Raised)
		self.verticalLayout_48 = QVBoxLayout(self.frame_41)
		self.verticalLayout_48.setSpacing(4)
		self.verticalLayout_48.setObjectName(u"verticalLayout_48")
		self.verticalLayout_48.setContentsMargins(0, 2, 0, 0)
		self.label_aviso_email_cadastro = QLabel(self.frame_41)
		self.label_aviso_email_cadastro.setObjectName(u"label_aviso_email_cadastro")
		self.label_aviso_email_cadastro.setFont(font18)
		self.label_aviso_email_cadastro.setStyleSheet(u"color: red; padding-left: 14px")

		self.verticalLayout_48.addWidget(self.label_aviso_email_cadastro)

		self.lineEdit_email_cadastro = QLineEdit(self.frame_41)
		self.lineEdit_email_cadastro.setObjectName(u"lineEdit_email_cadastro")
		self.lineEdit_email_cadastro.setMinimumSize(QSize(0, 44))
		self.lineEdit_email_cadastro.setMaximumSize(QSize(16777215, 16777215))
		self.lineEdit_email_cadastro.setFont(font2)
		self.lineEdit_email_cadastro.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_email_cadastro.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		###########################################################################
		self.lineEdit_email_cadastro.setValidator(self.validaEmail)
		self.lineEdit_email_cadastro.setMaxLength(255)
		self.lineEdit_email_cadastro.setInputMethodHints(Qt.ImhEmailCharactersOnly)
		###########################################################################

		self.verticalLayout_48.addWidget(self.lineEdit_email_cadastro)

		self.horizontalLayout_13.addWidget(self.frame_41)

		self.frame_42 = QFrame(self.frame_11)
		self.frame_42.setObjectName(u"frame_42")
		self.frame_42.setMaximumSize(QSize(380, 16777215))
		self.frame_42.setFrameShape(QFrame.StyledPanel)
		self.frame_42.setFrameShadow(QFrame.Raised)
		self.verticalLayout_49 = QVBoxLayout(self.frame_42)
		self.verticalLayout_49.setSpacing(4)
		self.verticalLayout_49.setObjectName(u"verticalLayout_49")
		self.verticalLayout_49.setContentsMargins(0, 2, 0, 0)
		self.label_aviso_celular = QLabel(self.frame_42)
		self.label_aviso_celular.setObjectName(u"label_aviso_celular")
		self.label_aviso_celular.setFont(font18)
		self.label_aviso_celular.setStyleSheet(u"color: red; padding-left: 18px")

		self.verticalLayout_49.addWidget(self.label_aviso_celular)

		self.lineEdit_celular = QLineEdit(self.frame_42)
		self.lineEdit_celular.setObjectName(u"lineEdit_celular")
		self.lineEdit_celular.setMinimumSize(QSize(0, 44))
		self.lineEdit_celular.setMaximumSize(QSize(380, 16777215))
		self.lineEdit_celular.setFont(font2)
		self.lineEdit_celular.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_celular.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		######################################################
		self.lineEdit_celular.setValidator(self.validaTelefone)
		self.lineEdit_celular.setMaxLength(13)
		self.lineEdit_celular.setInputMethodHints(Qt.ImhDigitsOnly)
		######################################################

		self.verticalLayout_49.addWidget(self.lineEdit_celular)


		self.horizontalLayout_13.addWidget(self.frame_42)


		self.verticalLayout_12.addWidget(self.frame_11)

		self.meio_baixo_cadastro = QFrame(self.meio_cadastro_2)
		self.meio_baixo_cadastro.setObjectName(u"meio_baixo_cadastro")
		self.meio_baixo_cadastro.setMinimumSize(QSize(0, 0))
		self.meio_baixo_cadastro.setFont(font)
		self.meio_baixo_cadastro.setFrameShape(QFrame.StyledPanel)
		self.meio_baixo_cadastro.setFrameShadow(QFrame.Raised)
		self.verticalLayout_9 = QVBoxLayout(self.meio_baixo_cadastro)
		self.verticalLayout_9.setSpacing(0)
		self.verticalLayout_9.setObjectName(u"verticalLayout_9")
		self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
		self.frame_5 = QFrame(self.meio_baixo_cadastro)
		self.frame_5.setObjectName(u"frame_5")
		self.frame_5.setFont(font)
		self.frame_5.setFrameShape(QFrame.StyledPanel)
		self.frame_5.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
		self.horizontalLayout_8.setSpacing(0)
		self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
		self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
		self.comboBox_privilegios = QComboBox(self.frame_5)
		self.comboBox_privilegios.addItem("")
		self.comboBox_privilegios.addItem("")
		self.comboBox_privilegios.setObjectName(u"comboBox_privilegios")
		self.comboBox_privilegios.setMinimumSize(QSize(145, 44))
		self.comboBox_privilegios.setFont(font2)
		self.comboBox_privilegios.setStyleSheet(u'''QComboBox:hover{border-color:#28A745;}
	QComboBox:focus{border-color:#28A745;}QComboBox{color: #848484; border-radius: 10px; border-width: 1px; border-style: solid; border-color:#c4c4c4; padding-left: 10px;}
	QComboBox:drop-down:hover{background-color:#eeeeee}
	QComboBox:drop-down{width: 24px; border-top-right-radius:9px; border-bottom-right-radius:9px; border-top-left-radius:1px; border-bottom-left-radius:1px;}
	QComboBox:down-arrow{image: url(icons/expand_more_blue_18dp.svg); width: 18px; height: 18px;}
	''')
		self.comboBox_privilegios.setCursor(QCursor(Qt.PointingHandCursor))
		self.horizontalLayout_8.addWidget(self.comboBox_privilegios)

		self.horizontalSpacer_13 = QSpacerItem(937, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_8.addItem(self.horizontalSpacer_13)


		self.verticalLayout_9.addWidget(self.frame_5)

		self.verticalSpacer_3 = QSpacerItem(20, 269, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.verticalLayout_9.addItem(self.verticalSpacer_3)


		self.verticalLayout_12.addWidget(self.meio_baixo_cadastro)

		self.horizontalLayout_21.addWidget(self.meio_cadastro_2)

		self.horizontalSpacer_12 = QSpacerItem(27, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_21.addItem(self.horizontalSpacer_12)

		self.verticalLayout_10.addWidget(self.meio_cadastro)

		self.inferior_cadastro = QFrame(self.main_cadastro)
		self.inferior_cadastro.setObjectName(u"inferior_cadastro")
		self.inferior_cadastro.setMinimumSize(QSize(0, 156))
		self.inferior_cadastro.setMaximumSize(QSize(16777215, 156))
		font19 = QFont()
		font19.setPointSize(20)
		self.inferior_cadastro.setFont(font19)
		self.inferior_cadastro.setFrameShape(QFrame.StyledPanel)
		self.inferior_cadastro.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_22 = QHBoxLayout(self.inferior_cadastro)
		self.horizontalLayout_22.setSpacing(0)
		self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
		self.horizontalLayout_22.setContentsMargins(24, 0, 24, 0)
		self.horizontalSpacer_14 = QSpacerItem(26, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_22.addItem(self.horizontalSpacer_14)

		self.inferior_cadastro_2 = QFrame(self.inferior_cadastro)
		self.inferior_cadastro_2.setObjectName(u"inferior_cadastro_2")
		self.inferior_cadastro_2.setMinimumSize(QSize(0, 156))
		self.inferior_cadastro_2.setMaximumSize(QSize(1028, 156))
		font20 = QFont()
		font20.setPointSize(20)
		font20.setBold(True)
		self.inferior_cadastro_2.setFont(font20)
		self.inferior_cadastro_2.setFrameShape(QFrame.StyledPanel)
		self.inferior_cadastro_2.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_7 = QHBoxLayout(self.inferior_cadastro_2)
		self.horizontalLayout_7.setSpacing(0)
		self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
		self.horizontalLayout_7.setContentsMargins(0, 0, 24, 48)
		self.horizontalSpacer_2 = QSpacerItem(887, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

		self.btn_salvar_cadastro = QPushButton(self.inferior_cadastro_2)
		self.btn_salvar_cadastro.setObjectName(u"btn_salvar_cadastro")
		self.btn_salvar_cadastro.setEnabled(True)
		self.btn_salvar_cadastro.setMinimumSize(QSize(160, 50))
		self.btn_salvar_cadastro.setFont(font20)
		self.btn_salvar_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_salvar_cadastro.setStyleSheet(u"QPushButton:hover{background: #198754;} QPushButton{background-color: #28A745; color: #fff;  border-radius: 22px;}")

		self.horizontalLayout_7.addWidget(self.btn_salvar_cadastro)


		self.horizontalLayout_22.addWidget(self.inferior_cadastro_2)

		self.horizontalSpacer_19 = QSpacerItem(26, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_22.addItem(self.horizontalSpacer_19)


		self.verticalLayout_10.addWidget(self.inferior_cadastro)


		self.verticalLayout_8.addWidget(self.main_cadastro, 0, Qt.AlignHCenter|Qt.AlignVCenter)

		self.pages.addWidget(self.cadastro)
		self.entradas = QWidget()
		self.entradas.setObjectName(u"entradas")
		self.entradas.setFont(font)
		self.verticalLayout_17 = QVBoxLayout(self.entradas)
		self.verticalLayout_17.setSpacing(0)
		self.verticalLayout_17.setObjectName(u"verticalLayout_17")
		self.verticalLayout_17.setContentsMargins(56, 64, 56, 64)
		self.main_entrada = QFrame(self.entradas)
		self.main_entrada.setObjectName(u"main_entrada")
		self.main_entrada.setMaximumSize(QSize(1299, 16777215))
		self.main_entrada.setFont(font)
		self.main_entrada.setStyleSheet(u"background-color: #fff; border-radius: 15px")
		self.main_entrada.setFrameShape(QFrame.StyledPanel)
		self.main_entrada.setFrameShadow(QFrame.Raised)
		self.verticalLayout_13 = QVBoxLayout(self.main_entrada)
		self.verticalLayout_13.setSpacing(0)
		self.verticalLayout_13.setObjectName(u"verticalLayout_13")
		self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
		self.superior_entrada = QFrame(self.main_entrada)
		self.superior_entrada.setObjectName(u"superior_entrada")
		self.superior_entrada.setMinimumSize(QSize(0, 0))
		self.superior_entrada.setMaximumSize(QSize(16777215, 105))
		self.superior_entrada.setFont(font15)
		self.superior_entrada.setFrameShape(QFrame.StyledPanel)
		self.superior_entrada.setFrameShadow(QFrame.Raised)
		self.verticalLayout_14 = QVBoxLayout(self.superior_entrada)
		self.verticalLayout_14.setSpacing(0)
		self.verticalLayout_14.setObjectName(u"verticalLayout_14")
		self.verticalLayout_14.setContentsMargins(0, 40, 0, 0)
		self.label_3 = QLabel(self.superior_entrada)
		self.label_3.setObjectName(u"label_3")
		self.label_3.setMaximumSize(QSize(16777215, 16777215))
		self.label_3.setFont(font15)
		self.label_3.setStyleSheet(u"color: #3A4B5E")
		self.label_3.setAlignment(Qt.AlignCenter)

		self.verticalLayout_14.addWidget(self.label_3)


		self.verticalLayout_13.addWidget(self.superior_entrada)

		self.meio_entrada = QFrame(self.main_entrada)
		self.meio_entrada.setObjectName(u"meio_entrada")
		self.meio_entrada.setFont(font)
		self.meio_entrada.setFrameShape(QFrame.StyledPanel)
		self.meio_entrada.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_18 = QHBoxLayout(self.meio_entrada)
		self.horizontalLayout_18.setSpacing(0)
		self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
		self.horizontalLayout_18.setContentsMargins(40, 0, 40, 0)
		self.horizontalSpacer_6 = QSpacerItem(61, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_18.addItem(self.horizontalSpacer_6)

		self.meio_entrada_2 = QFrame(self.meio_entrada)
		self.meio_entrada_2.setObjectName(u"meio_entrada_2")
		self.meio_entrada_2.setFont(font)
		self.meio_entrada_2.setFrameShape(QFrame.StyledPanel)
		self.meio_entrada_2.setFrameShadow(QFrame.Raised)
		self.verticalLayout_15 = QVBoxLayout(self.meio_entrada_2)
		self.verticalLayout_15.setSpacing(3)
		self.verticalLayout_15.setObjectName(u"verticalLayout_15")
		self.verticalLayout_15.setContentsMargins(0, 80, 0, 0)
		self.frame_12 = QFrame(self.meio_entrada_2)
		self.frame_12.setObjectName(u"frame_12")
		self.frame_12.setFont(font)
		self.frame_12.setFrameShape(QFrame.StyledPanel)
		self.frame_12.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_34 = QHBoxLayout(self.frame_12)
		self.horizontalLayout_34.setSpacing(16)
		self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
		self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
		self.frame_43 = QFrame(self.frame_12)
		self.frame_43.setObjectName(u"frame_43")
		self.frame_43.setFrameShape(QFrame.StyledPanel)
		self.frame_43.setFrameShadow(QFrame.Raised)
		self.verticalLayout_50 = QVBoxLayout(self.frame_43)
		self.verticalLayout_50.setSpacing(4)
		self.verticalLayout_50.setObjectName(u"verticalLayout_50")
		self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_nome_entrada = QLabel(self.frame_43)
		self.label_aviso_nome_entrada.setObjectName(u"label_aviso_nome_entrada")
		self.label_aviso_nome_entrada.setFont(font18)
		self.label_aviso_nome_entrada.setAutoFillBackground(False)
		self.label_aviso_nome_entrada.setStyleSheet(u"color: red; padding-left:18px")

		self.verticalLayout_50.addWidget(self.label_aviso_nome_entrada)

		self.lineEdit_nome_entrada = QLineEdit(self.frame_43)
		self.lineEdit_nome_entrada.setObjectName(u"lineEdit_nome_entrada")
		self.lineEdit_nome_entrada.setMinimumSize(QSize(0, 44))
		self.lineEdit_nome_entrada.setFont(font2)
		self.lineEdit_nome_entrada.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_nome_entrada.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		########################################################
		self.lineEdit_nome_entrada.setValidator(self.validaNome)
		self.lineEdit_nome_entrada.setMaxLength(255)
		########################################################

		self.verticalLayout_50.addWidget(self.lineEdit_nome_entrada)

		self.horizontalLayout_34.addWidget(self.frame_43)

		self.frame_44 = QFrame(self.frame_12)
		self.frame_44.setObjectName(u"frame_44")
		self.frame_44.setMinimumSize(QSize(206, 0))
		self.frame_44.setMaximumSize(QSize(206, 16777215))
		self.frame_44.setFrameShape(QFrame.StyledPanel)
		self.frame_44.setFrameShadow(QFrame.Raised)
		self.verticalLayout_51 = QVBoxLayout(self.frame_44)
		self.verticalLayout_51.setSpacing(4)
		self.verticalLayout_51.setObjectName(u"verticalLayout_51")
		self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_data_ref_entrada = QLabel(self.frame_44)
		self.label_aviso_data_ref_entrada.setObjectName(u"label_aviso_data_ref_entrada")
		self.label_aviso_data_ref_entrada.setMaximumSize(QSize(206, 16777215))
		self.label_aviso_data_ref_entrada.setFont(font18)
		self.label_aviso_data_ref_entrada.setStyleSheet(u"color: red;")
		self.label_aviso_data_ref_entrada.setAlignment(Qt.AlignCenter)

		self.verticalLayout_51.addWidget(self.label_aviso_data_ref_entrada)

		self.lineEdit_data_ref = QLineEdit(self.frame_44)
		self.lineEdit_data_ref.setObjectName(u"lineEdit_data_ref")
		self.lineEdit_data_ref.setMinimumSize(QSize(0, 44))
		self.lineEdit_data_ref.setMaximumSize(QSize(206, 16777215))
		self.lineEdit_data_ref.setFont(font2)
		self.lineEdit_data_ref.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_data_ref.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		##########################################################
		self.lineEdit_data_ref.setValidator(self.validaData)
		self.lineEdit_data_ref.setMaxLength(10)
		self.lineEdit_data_ref.setInputMethodHints(Qt.ImhDate)
		##########################################################

		self.verticalLayout_51.addWidget(self.lineEdit_data_ref)

		self.horizontalLayout_34.addWidget(self.frame_44)

		self.frame_45 = QFrame(self.frame_12)
		self.frame_45.setObjectName(u"frame_45")
		self.frame_45.setMinimumSize(QSize(206, 0))
		self.frame_45.setMaximumSize(QSize(206, 16777215))
		self.frame_45.setFrameShape(QFrame.StyledPanel)
		self.frame_45.setFrameShadow(QFrame.Raised)
		self.verticalLayout_52 = QVBoxLayout(self.frame_45)
		self.verticalLayout_52.setSpacing(4)
		self.verticalLayout_52.setObjectName(u"verticalLayout_52")
		self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_data_dep_entrada = QLabel(self.frame_45)
		self.label_aviso_data_dep_entrada.setObjectName(u"label_aviso_data_dep_entrada")
		self.label_aviso_data_dep_entrada.setMaximumSize(QSize(206, 16777215))
		self.label_aviso_data_dep_entrada.setFont(font18)
		self.label_aviso_data_dep_entrada.setStyleSheet(u"color: red;")
		self.label_aviso_data_dep_entrada.setAlignment(Qt.AlignCenter)

		self.verticalLayout_52.addWidget(self.label_aviso_data_dep_entrada)

		self.lineEdit_data_dep = QLineEdit(self.frame_45)
		self.lineEdit_data_dep.setObjectName(u"lineEdit_data_dep")
		self.lineEdit_data_dep.setMinimumSize(QSize(0, 44))
		self.lineEdit_data_dep.setMaximumSize(QSize(206, 16777215))
		self.lineEdit_data_dep.setFont(font2)
		self.lineEdit_data_dep.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_data_dep.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		######################################################
		self.lineEdit_data_dep.setValidator(self.validaData)
		self.lineEdit_data_dep.setMaxLength(10)
		self.lineEdit_data_dep.setInputMethodHints(Qt.ImhDate)
		######################################################

		self.verticalLayout_52.addWidget(self.lineEdit_data_dep)

		self.horizontalLayout_34.addWidget(self.frame_45)

		self.verticalLayout_15.addWidget(self.frame_12)

		self.frame_15 = QFrame(self.meio_entrada_2)
		self.frame_15.setObjectName(u"frame_15")
		self.frame_15.setFont(font)
		self.frame_15.setFrameShape(QFrame.StyledPanel)
		self.frame_15.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
		self.horizontalLayout_15.setSpacing(16)
		self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
		self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
		self.frame_28 = QFrame(self.frame_15)
		self.frame_28.setObjectName(u"frame_28")
		self.frame_28.setFrameShape(QFrame.StyledPanel)
		self.frame_28.setFrameShadow(QFrame.Raised)
		self.verticalLayout_35 = QVBoxLayout(self.frame_28)
		self.verticalLayout_35.setSpacing(5)
		self.verticalLayout_35.setObjectName(u"verticalLayout_35")
		self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_dizimo_entrada = QLabel(self.frame_28)
		self.label_aviso_dizimo_entrada.setObjectName(u"label_aviso_dizimo_entrada")
		self.label_aviso_dizimo_entrada.setMinimumSize(QSize(0, 0))
		self.label_aviso_dizimo_entrada.setFont(font18)
		self.label_aviso_dizimo_entrada.setStyleSheet(u"color: red;")
		self.label_aviso_dizimo_entrada.setAlignment(Qt.AlignCenter)

		self.verticalLayout_35.addWidget(self.label_aviso_dizimo_entrada)

		self.lineEdit_dizimo_entrada = QLineEdit(self.frame_28)
		self.lineEdit_dizimo_entrada.setObjectName(u"lineEdit_dizimo_entrada")
		self.lineEdit_dizimo_entrada.setMinimumSize(QSize(0, 44))
		self.lineEdit_dizimo_entrada.setMaximumSize(QSize(16777215, 16777215))
		self.lineEdit_dizimo_entrada.setFont(font2)
		self.lineEdit_dizimo_entrada.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_dizimo_entrada.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		###########################################################################
		#self.lineEdit_dizimo_entrada.setValidator(self.validaValor)
		self.lineEdit_dizimo_entrada.setMaxLength(9)
		self.lineEdit_dizimo_entrada.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
		###########################################################################

		self.verticalLayout_35.addWidget(self.lineEdit_dizimo_entrada)

		self.horizontalLayout_15.addWidget(self.frame_28)

		self.frame_29 = QFrame(self.frame_15)
		self.frame_29.setObjectName(u"frame_29")
		self.frame_29.setFrameShape(QFrame.StyledPanel)
		self.frame_29.setFrameShadow(QFrame.Raised)
		self.verticalLayout_34 = QVBoxLayout(self.frame_29)
		self.verticalLayout_34.setSpacing(5)
		self.verticalLayout_34.setObjectName(u"verticalLayout_34")
		self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_terenos_entrada = QLabel(self.frame_29)
		self.label_aviso_terenos_entrada.setObjectName(u"label_aviso_terenos_entrada")
		self.label_aviso_terenos_entrada.setMinimumSize(QSize(0, 0))
		self.label_aviso_terenos_entrada.setFont(font18)
		self.label_aviso_terenos_entrada.setStyleSheet(u"color: red;")
		self.label_aviso_terenos_entrada.setAlignment(Qt.AlignCenter)

		self.verticalLayout_34.addWidget(self.label_aviso_terenos_entrada)

		self.lineEdit_terenos_entrada = QLineEdit(self.frame_29)
		self.lineEdit_terenos_entrada.setObjectName(u"lineEdit_terenos_entrada")
		self.lineEdit_terenos_entrada.setMinimumSize(QSize(0, 44))
		self.lineEdit_terenos_entrada.setMaximumSize(QSize(16777215, 16777215))
		self.lineEdit_terenos_entrada.setFont(font2)
		self.lineEdit_terenos_entrada.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_terenos_entrada.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		#############################################################################
		# self.lineEdit_terenos_entrada.setValidator(self.validaValor)
		self.lineEdit_terenos_entrada.setMaxLength(9)
		self.lineEdit_terenos_entrada.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
		#############################################################################

		self.verticalLayout_34.addWidget(self.lineEdit_terenos_entrada)

		self.horizontalLayout_15.addWidget(self.frame_29)

		self.frame_30 = QFrame(self.frame_15)
		self.frame_30.setObjectName(u"frame_30")
		self.frame_30.setFrameShape(QFrame.StyledPanel)
		self.frame_30.setFrameShadow(QFrame.Raised)
		self.verticalLayout_33 = QVBoxLayout(self.frame_30)
		self.verticalLayout_33.setSpacing(5)
		self.verticalLayout_33.setObjectName(u"verticalLayout_33")
		self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_missoes_entrada = QLabel(self.frame_30)
		self.label_aviso_missoes_entrada.setObjectName(u"label_aviso_missoes_entrada")
		self.label_aviso_missoes_entrada.setMinimumSize(QSize(0, 0))
		self.label_aviso_missoes_entrada.setFont(font18)
		self.label_aviso_missoes_entrada.setStyleSheet(u"color: red;")
		self.label_aviso_missoes_entrada.setAlignment(Qt.AlignCenter)

		self.verticalLayout_33.addWidget(self.label_aviso_missoes_entrada)

		self.lineEdit_missoes_entrada = QLineEdit(self.frame_30)
		self.lineEdit_missoes_entrada.setObjectName(u"lineEdit_missoes_entrada")
		self.lineEdit_missoes_entrada.setMinimumSize(QSize(0, 44))
		self.lineEdit_missoes_entrada.setMaximumSize(QSize(16777215, 16777215))
		self.lineEdit_missoes_entrada.setFont(font2)
		self.lineEdit_missoes_entrada.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_missoes_entrada.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		#############################################################################
		# self.lineEdit_missoes_entrada.setValidator(self.validaValor)
		self.lineEdit_missoes_entrada.setMaxLength(9)
		self.lineEdit_missoes_entrada.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
		#############################################################################


		self.verticalLayout_33.addWidget(self.lineEdit_missoes_entrada)


		self.horizontalLayout_15.addWidget(self.frame_30)

		self.frame_31 = QFrame(self.frame_15)
		self.frame_31.setObjectName(u"frame_31")
		self.frame_31.setFrameShape(QFrame.StyledPanel)
		self.frame_31.setFrameShadow(QFrame.Raised)
		self.verticalLayout_32 = QVBoxLayout(self.frame_31)
		self.verticalLayout_32.setSpacing(5)
		self.verticalLayout_32.setObjectName(u"verticalLayout_32")
		self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_pam_entrada = QLabel(self.frame_31)
		self.label_aviso_pam_entrada.setObjectName(u"label_aviso_pam_entrada")
		self.label_aviso_pam_entrada.setMinimumSize(QSize(0, 0))
		self.label_aviso_pam_entrada.setFont(font18)
		self.label_aviso_pam_entrada.setStyleSheet(u"color: red;")
		self.label_aviso_pam_entrada.setAlignment(Qt.AlignCenter)

		self.verticalLayout_32.addWidget(self.label_aviso_pam_entrada)

		self.lineEdit_pam_entrada = QLineEdit(self.frame_31)
		self.lineEdit_pam_entrada.setObjectName(u"lineEdit_pam_entrada")
		self.lineEdit_pam_entrada.setMinimumSize(QSize(0, 44))
		self.lineEdit_pam_entrada.setFont(font2)
		self.lineEdit_pam_entrada.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_pam_entrada.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		#########################################################################
		# self.lineEdit_pam_entrada.setValidator(self.validaValor)
		self.lineEdit_pam_entrada.setMaxLength(9)
		self.lineEdit_pam_entrada.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
		#########################################################################

		self.verticalLayout_32.addWidget(self.lineEdit_pam_entrada)

		self.horizontalLayout_15.addWidget(self.frame_31)

		self.frame = QFrame(self.frame_15)
		self.frame.setObjectName(u"frame")
		self.verticalLayout_36 = QVBoxLayout(self.frame)
		self.verticalLayout_36.setSpacing(5)
		self.verticalLayout_36.setObjectName(u"verticalLayout_36")
		self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
		self.label_8 = QLabel(self.frame)
		self.label_8.setObjectName(u"label_8")
		self.label_8.setFont(font18)
		self.label_8.setAlignment(Qt.AlignCenter)

		self.verticalLayout_36.addWidget(self.label_8)

		self.comboBox_tipo_entrada = QComboBox(self.frame)
		self.comboBox_tipo_entrada.addItem("")
		self.comboBox_tipo_entrada.addItem("")
		self.comboBox_tipo_entrada.setObjectName(u"comboBox_tipo_entrada")
		self.comboBox_tipo_entrada.setMinimumSize(QSize(140, 44))
		self.comboBox_tipo_entrada.setFont(font2)
		self.comboBox_tipo_entrada.setCursor(QCursor(Qt.PointingHandCursor))
		self.comboBox_tipo_entrada.setLayoutDirection(Qt.LeftToRight)
		self.comboBox_tipo_entrada.setStyleSheet(u'''QComboBox:hover{border-color:#28A745;}
	QComboBox:focus{border-color:#28A745;}QComboBox{color: #848484; border-radius: 10px; border-width: 1px; border-style: solid; border-color:#c4c4c4; padding-left: 10px;}
	QComboBox:drop-down:hover{background-color:#eeeeee}
	QComboBox:drop-down{width: 24px; border-top-right-radius:9px; border-bottom-right-radius:9px; border-top-left-radius:1px; border-bottom-left-radius:1px;}
	QComboBox:down-arrow{image: url(icons/expand_more_blue_18dp.svg); width: 18px; height: 18px;}
	''')
		self.comboBox_tipo_entrada.setCursor(QCursor(Qt.PointingHandCursor))
		self.verticalLayout_36.addWidget(self.comboBox_tipo_entrada)

		self.horizontalLayout_15.addWidget(self.frame)

		self.verticalLayout_15.addWidget(self.frame_15)

		self.frame_2 = QFrame(self.meio_entrada_2)
		self.frame_2.setObjectName(u"frame_2")
		self.frame_2.setFont(font)
		self.frame_2.setFrameShape(QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_17 = QHBoxLayout(self.frame_2)
		self.horizontalLayout_17.setSpacing(0)
		self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
		self.horizontalLayout_17.setContentsMargins(0, 36, 0, 5)
		self.btn_extra = QPushButton(self.frame_2)
		self.btn_extra.setObjectName(u"btn_extra")
		self.btn_extra.setMaximumSize(QSize(85, 16777215))
		self.btn_extra.setFont(font)
		self.btn_extra.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_extra.setFocusPolicy(Qt.StrongFocus)
		self.btn_extra.setLayoutDirection(Qt.RightToLeft)
		self.btn_extra.setStyleSheet(u"QPushButton:hover{color: #3A4B5E; } QPushButton{color: #848484;}")
		icon2 = QIcon()
		icon2.addFile(u"icons/expand_more_blue_18dp.svg", QSize(), QIcon.Normal, QIcon.Off)
		self.btn_extra.setIcon(icon2)
		self.btn_extra.setIconSize(QSize(18, 18))

		self.horizontalLayout_17.addWidget(self.btn_extra)

		self.horizontalSpacer_9 = QSpacerItem(693, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_17.addItem(self.horizontalSpacer_9)

		self.verticalLayout_15.addWidget(self.frame_2)

		self.meio_baixo_entrada = QFrame(self.meio_entrada_2)
		self.meio_baixo_entrada.setObjectName(u"meio_baixo_entrada")
		self.meio_baixo_entrada.setMinimumSize(QSize(0, 0))
		self.meio_baixo_entrada.setFont(font)
		self.meio_baixo_entrada.setFrameShape(QFrame.StyledPanel)
		self.meio_baixo_entrada.setFrameShadow(QFrame.Raised)
		self.verticalLayout_16 = QVBoxLayout(self.meio_baixo_entrada)
		self.verticalLayout_16.setSpacing(0)
		self.verticalLayout_16.setObjectName(u"verticalLayout_16")
		self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
		self.extra_entrada = QFrame(self.meio_baixo_entrada)
		self.extra_entrada.setObjectName(u"extra_entrada")
		self.extra_entrada.setMaximumSize(QSize(16777215, 0))
		self.extra_entrada.setFont(font)
		self.extra_entrada.setStyleSheet(u"QFrame#extra_entrada{border-radius: 15px; border-width: 1px; border-style: solid; border-color: #c4c4c4}")
		self.extra_entrada.setFrameShape(QFrame.StyledPanel)
		self.extra_entrada.setFrameShadow(QFrame.Raised)
		self.verticalLayout_18 = QVBoxLayout(self.extra_entrada)
		self.verticalLayout_18.setSpacing(4)
		self.verticalLayout_18.setObjectName(u"verticalLayout_18")
		self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
		self.frame_3 = QFrame(self.extra_entrada)
		self.frame_3.setObjectName(u"frame_3")
		self.frame_3.setFont(font)
		self.frame_3.setStyleSheet(u"")
		self.frame_3.setFrameShape(QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_16 = QHBoxLayout(self.frame_3)
		self.horizontalLayout_16.setSpacing(0)
		self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
		self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
		self.frame_26 = QFrame(self.frame_3)
		self.frame_26.setObjectName(u"frame_26")
		self.frame_26.setFont(font18)
		self.frame_26.setFrameShape(QFrame.StyledPanel)
		self.frame_26.setFrameShadow(QFrame.Raised)
		self.verticalLayout_37 = QVBoxLayout(self.frame_26)
		self.verticalLayout_37.setSpacing(3)
		self.verticalLayout_37.setObjectName(u"verticalLayout_37")
		self.verticalLayout_37.setContentsMargins(24, 6, 16, 30)
		self.label_aviso_campanha_nome_entrada = QLabel(self.frame_26)
		self.label_aviso_campanha_nome_entrada.setObjectName(u"label_aviso_campanha_nome_entrada")
		self.label_aviso_campanha_nome_entrada.setFont(font18)
		self.label_aviso_campanha_nome_entrada.setStyleSheet(u"color: red; padding-left: 14px")

		self.verticalLayout_37.addWidget(self.label_aviso_campanha_nome_entrada)

		self.lineEdit_campanha_nome_entrada = QLineEdit(self.frame_26)
		self.lineEdit_campanha_nome_entrada.setObjectName(u"lineEdit_campanha_nome_entrada")
		self.lineEdit_campanha_nome_entrada.setMinimumSize(QSize(0, 44))
		self.lineEdit_campanha_nome_entrada.setMaximumSize(QSize(16777215, 16777215))
		self.lineEdit_campanha_nome_entrada.setFont(font2)
		self.lineEdit_campanha_nome_entrada.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_campanha_nome_entrada.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		#################################################################
		self.lineEdit_campanha_nome_entrada.setValidator(self.validaNome)
		self.lineEdit_campanha_nome_entrada.setMaxLength(255)
		#################################################################

		self.verticalLayout_37.addWidget(self.lineEdit_campanha_nome_entrada)

		self.horizontalLayout_16.addWidget(self.frame_26)

		self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

		self.frame_32 = QFrame(self.frame_3)
		self.frame_32.setObjectName(u"frame_32")
		self.frame_32.setFont(font18)
		self.frame_32.setFrameShape(QFrame.StyledPanel)
		self.frame_32.setFrameShadow(QFrame.Raised)
		self.verticalLayout_38 = QVBoxLayout(self.frame_32)
		self.verticalLayout_38.setSpacing(3)
		self.verticalLayout_38.setObjectName(u"verticalLayout_38")
		self.verticalLayout_38.setContentsMargins(16, 6, 24, 30)
		self.label_aviso_campanha_valor_entrada = QLabel(self.frame_32)
		self.label_aviso_campanha_valor_entrada.setObjectName(u"label_aviso_campanha_valor_entrada")
		self.label_aviso_campanha_valor_entrada.setFont(font18)
		self.label_aviso_campanha_valor_entrada.setStyleSheet(u"color: red;")
		self.label_aviso_campanha_valor_entrada.setAlignment(Qt.AlignCenter)

		self.verticalLayout_38.addWidget(self.label_aviso_campanha_valor_entrada)

		self.lineEdit_campanha_valor_entrada = QLineEdit(self.frame_32)
		self.lineEdit_campanha_valor_entrada.setObjectName(u"lineEdit_campanha_valor_entrada")
		self.lineEdit_campanha_valor_entrada.setMinimumSize(QSize(0, 44))
		self.lineEdit_campanha_valor_entrada.setMaximumSize(QSize(190, 16777215))
		self.lineEdit_campanha_valor_entrada.setFont(font2)
		self.lineEdit_campanha_valor_entrada.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_campanha_valor_entrada.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		####################################################################################
		# self.lineEdit_campanha_valor_entrada.setValidator(self.validaValor)
		self.lineEdit_campanha_valor_entrada.setMaxLength(9)
		self.lineEdit_campanha_valor_entrada.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
		####################################################################################

		self.verticalLayout_38.addWidget(self.lineEdit_campanha_valor_entrada)

		self.horizontalLayout_16.addWidget(self.frame_32)

		self.horizontalLayout_16.setStretch(0, 9)
		self.horizontalLayout_16.setStretch(1, 1)
		self.horizontalLayout_16.setStretch(2, 3)

		self.verticalLayout_18.addWidget(self.frame_3)

		self.verticalLayout_16.addWidget(self.extra_entrada)

		self.verticalSpacer_4 = QSpacerItem(20, 269, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.verticalLayout_16.addItem(self.verticalSpacer_4)

		self.verticalLayout_15.addWidget(self.meio_baixo_entrada)

		self.horizontalLayout_18.addWidget(self.meio_entrada_2)

		self.horizontalSpacer_8 = QSpacerItem(61, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_18.addItem(self.horizontalSpacer_8)

		self.verticalLayout_13.addWidget(self.meio_entrada)

		self.inferior_entrada = QFrame(self.main_entrada)
		self.inferior_entrada.setObjectName(u"inferior_entrada")
		self.inferior_entrada.setMinimumSize(QSize(0, 156))
		self.inferior_entrada.setMaximumSize(QSize(16777215, 156))
		self.inferior_entrada.setFont(font)
		self.inferior_entrada.setFrameShape(QFrame.StyledPanel)
		self.inferior_entrada.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_19 = QHBoxLayout(self.inferior_entrada)
		self.horizontalLayout_19.setSpacing(0)
		self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
		self.horizontalLayout_19.setContentsMargins(24, 0, 24, 0)
		self.horizontalSpacer_10 = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_19.addItem(self.horizontalSpacer_10)

		self.inferior_entrada_2 = QFrame(self.inferior_entrada)
		self.inferior_entrada_2.setObjectName(u"inferior_entrada_2")
		self.inferior_entrada_2.setMinimumSize(QSize(0, 156))
		self.inferior_entrada_2.setMaximumSize(QSize(1026, 156))
		self.inferior_entrada_2.setFont(font20)
		self.inferior_entrada_2.setFrameShape(QFrame.StyledPanel)
		self.inferior_entrada_2.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_20 = QHBoxLayout(self.inferior_entrada_2)
		self.horizontalLayout_20.setSpacing(0)
		self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
		self.horizontalLayout_20.setContentsMargins(32, 0, 32, 48)
		self.btn_visualizar_entrada = QPushButton(self.inferior_entrada_2)
		self.btn_visualizar_entrada.setObjectName(u"btn_visualizar_entrada")
		self.btn_visualizar_entrada.setEnabled(True)
		self.btn_visualizar_entrada.setMinimumSize(QSize(160, 50))
		self.btn_visualizar_entrada.setFont(font20)
		self.btn_visualizar_entrada.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_visualizar_entrada.setStyleSheet(u"QPushButton:hover{background: #5F7A99; color: #fff;} QPushButton{background-color: #fff; color: #5F7A99;  border-radius: 22px; border:2px solid #5F7A99}")

		self.horizontalLayout_20.addWidget(self.btn_visualizar_entrada)

		self.horizontalSpacer_11 = QSpacerItem(887, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_20.addItem(self.horizontalSpacer_11)

		self.btn_salvar_entrada = QPushButton(self.inferior_entrada_2)
		self.btn_salvar_entrada.setObjectName(u"btn_salvar_entrada")
		self.btn_salvar_entrada.setEnabled(True)
		self.btn_salvar_entrada.setMinimumSize(QSize(160, 50))
		self.btn_salvar_entrada.setFont(font20)
		self.btn_salvar_entrada.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_salvar_entrada.setStyleSheet(u"QPushButton:hover{background: #198754;} QPushButton{background-color: #28A745; color: #fff;  border-radius: 22px;}")

		self.horizontalLayout_20.addWidget(self.btn_salvar_entrada)

		self.horizontalLayout_19.addWidget(self.inferior_entrada_2)

		self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_19.addItem(self.horizontalSpacer_29)

		self.verticalLayout_13.addWidget(self.inferior_entrada)

		self.verticalLayout_17.addWidget(self.main_entrada)

		self.pages.addWidget(self.entradas)
		self.saidas = QWidget()
		self.saidas.setObjectName(u"saidas")
		self.saidas.setFont(font)
		self.verticalLayout_19 = QVBoxLayout(self.saidas)
		self.verticalLayout_19.setSpacing(0)
		self.verticalLayout_19.setObjectName(u"verticalLayout_19")
		self.verticalLayout_19.setContentsMargins(56, 64, 56, 64)
		self.main_saida = QFrame(self.saidas)
		self.main_saida.setObjectName(u"main_saida")
		self.main_saida.setFont(font)
		self.main_saida.setStyleSheet(u"background-color: #fff; border-radius:15px;")
		self.main_saida.setFrameShape(QFrame.StyledPanel)
		self.main_saida.setFrameShadow(QFrame.Raised)
		self.verticalLayout_20 = QVBoxLayout(self.main_saida)
		self.verticalLayout_20.setSpacing(0)
		self.verticalLayout_20.setObjectName(u"verticalLayout_20")
		self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
		self.superior_saida = QFrame(self.main_saida)
		self.superior_saida.setObjectName(u"superior_saida")
		self.superior_saida.setMaximumSize(QSize(16777215, 105))
		self.superior_saida.setFont(font15)
		self.superior_saida.setFrameShape(QFrame.StyledPanel)
		self.superior_saida.setFrameShadow(QFrame.Raised)
		self.verticalLayout_21 = QVBoxLayout(self.superior_saida)
		self.verticalLayout_21.setSpacing(0)
		self.verticalLayout_21.setObjectName(u"verticalLayout_21")
		self.verticalLayout_21.setContentsMargins(0, 40, 0, 0)
		self.label_5 = QLabel(self.superior_saida)
		self.label_5.setObjectName(u"label_5")
		self.label_5.setMaximumSize(QSize(16777215, 16777215))
		self.label_5.setFont(font15)
		self.label_5.setStyleSheet(u"color: #3A4B5E")
		self.label_5.setAlignment(Qt.AlignCenter)

		self.verticalLayout_21.addWidget(self.label_5)

		self.verticalLayout_20.addWidget(self.superior_saida)

		self.meio_saida = QFrame(self.main_saida)
		self.meio_saida.setObjectName(u"meio_saida")
		self.meio_saida.setMinimumSize(QSize(0, 660))
		self.meio_saida.setFont(font)
		self.meio_saida.setFrameShape(QFrame.StyledPanel)
		self.meio_saida.setFrameShadow(QFrame.Raised)
		self.verticalLayout_56 = QVBoxLayout(self.meio_saida)
		self.verticalLayout_56.setSpacing(0)
		self.verticalLayout_56.setObjectName(u"verticalLayout_56")
		self.verticalLayout_56.setContentsMargins(40, 0, 40, 0)
		self.meio_saida_2 = QFrame(self.meio_saida)
		self.meio_saida_2.setObjectName(u"meio_saida_2")
		self.meio_saida_2.setMinimumSize(QSize(0, 0))
		self.meio_saida_2.setMaximumSize(QSize(16777215, 16777215))
		self.meio_saida_2.setFont(font)
		self.meio_saida_2.setFrameShape(QFrame.StyledPanel)
		self.meio_saida_2.setFrameShadow(QFrame.Raised)
		self.verticalLayout_22 = QVBoxLayout(self.meio_saida_2)
		self.verticalLayout_22.setSpacing(0)
		self.verticalLayout_22.setObjectName(u"verticalLayout_22")
		self.verticalLayout_22.setContentsMargins(0, 80, 0, 0)
		self.frame1 = QFrame(self.meio_saida_2)
		self.frame1.setObjectName(u"frame1")
		self.frame1.setFont(font)
		self.frame1.setFrameShape(QFrame.StyledPanel)
		self.frame1.setFrameShadow(QFrame.Raised)
		self.verticalLayout_53 = QVBoxLayout(self.frame1)
		self.verticalLayout_53.setSpacing(4)
		self.verticalLayout_53.setObjectName(u"verticalLayout_53")
		self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_destino_saida = QLabel(self.frame1)
		self.label_aviso_destino_saida.setObjectName(u"label_aviso_destino_saida")
		self.label_aviso_destino_saida.setFont(font18)
		self.label_aviso_destino_saida.setStyleSheet(u"color: red; padding-left:18px")

		self.verticalLayout_53.addWidget(self.label_aviso_destino_saida)

		self.lineEdit_destino_saida = QLineEdit(self.frame1)
		self.lineEdit_destino_saida.setObjectName(u"lineEdit_destino_saida")
		self.lineEdit_destino_saida.setMinimumSize(QSize(0, 44))
		self.lineEdit_destino_saida.setFont(font2)
		self.lineEdit_destino_saida.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_destino_saida.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		##########################################################
		self.lineEdit_destino_saida.setValidator(self.validaTexto)
		self.lineEdit_destino_saida.setMaxLength(255)
		##########################################################

		self.verticalLayout_53.addWidget(self.lineEdit_destino_saida)

		self.verticalLayout_22.addWidget(self.frame1)

		self.frame_24 = QFrame(self.meio_saida_2)
		self.frame_24.setObjectName(u"frame_24")
		self.frame_24.setFrameShape(QFrame.StyledPanel)
		self.frame_24.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_32 = QHBoxLayout(self.frame_24)
		self.horizontalLayout_32.setSpacing(24)
		self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
		self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)

		self.verticalLayout_22.addWidget(self.frame_24)

		self.frame_4 = QFrame(self.meio_saida_2)
		self.frame_4.setObjectName(u"frame_4")
		self.frame_4.setFont(font)
		self.frame_4.setFrameShape(QFrame.StyledPanel)
		self.frame_4.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_14 = QHBoxLayout(self.frame_4)
		self.horizontalLayout_14.setSpacing(16)
		self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
		self.horizontalLayout_14.setContentsMargins(0, 8, 0, 0)
		self.frame_25 = QFrame(self.frame_4)
		self.frame_25.setObjectName(u"frame_25")
		self.frame_25.setMaximumSize(QSize(206, 16777215))
		self.frame_25.setFrameShape(QFrame.StyledPanel)
		self.frame_25.setFrameShadow(QFrame.Raised)
		self.verticalLayout_23 = QVBoxLayout(self.frame_25)
		self.verticalLayout_23.setSpacing(4)
		self.verticalLayout_23.setObjectName(u"verticalLayout_23")
		self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_data_ref_saida = QLabel(self.frame_25)
		self.label_aviso_data_ref_saida.setObjectName(u"label_aviso_data_ref_saida")
		self.label_aviso_data_ref_saida.setMinimumSize(QSize(0, 0))
		self.label_aviso_data_ref_saida.setFont(font18)
		self.label_aviso_data_ref_saida.setStyleSheet(u"color: red;")
		self.label_aviso_data_ref_saida.setAlignment(Qt.AlignCenter)

		self.verticalLayout_23.addWidget(self.label_aviso_data_ref_saida)

		self.lineEdit_data_saida = QLineEdit(self.frame_25)
		self.lineEdit_data_saida.setObjectName(u"lineEdit_data_saida")
		self.lineEdit_data_saida.setMinimumSize(QSize(0, 44))
		self.lineEdit_data_saida.setMaximumSize(QSize(206, 16777215))
		self.lineEdit_data_saida.setFont(font2)
		self.lineEdit_data_saida.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_data_saida.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		######################################################
		self.lineEdit_data_saida.setValidator(self.validaData)
		self.lineEdit_data_saida.setMaxLength(10)
		self.lineEdit_data_saida.setInputMethodHints(Qt.ImhDate)
		########################################################

		self.verticalLayout_23.addWidget(self.lineEdit_data_saida)

		self.horizontalLayout_14.addWidget(self.frame_25)

		self.frame_46 = QFrame(self.frame_4)
		self.frame_46.setObjectName(u"frame_46")
		self.frame_46.setMaximumSize(QSize(206, 16777215))
		self.frame_46.setFrameShape(QFrame.StyledPanel)
		self.frame_46.setFrameShadow(QFrame.Raised)
		self.verticalLayout_54 = QVBoxLayout(self.frame_46)
		self.verticalLayout_54.setSpacing(4)
		self.verticalLayout_54.setObjectName(u"verticalLayout_54")
		self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_valor_saida = QLabel(self.frame_46)
		self.label_aviso_valor_saida.setObjectName(u"label_aviso_valor_saida")
		self.label_aviso_valor_saida.setMinimumSize(QSize(0, 0))
		self.label_aviso_valor_saida.setFont(font18)
		self.label_aviso_valor_saida.setStyleSheet(u"color: red;")
		self.label_aviso_valor_saida.setAlignment(Qt.AlignCenter)

		self.verticalLayout_54.addWidget(self.label_aviso_valor_saida)

		self.lineEdit_valor_saida = QLineEdit(self.frame_46)
		self.lineEdit_valor_saida.setObjectName(u"lineEdit_valor_saida")
		self.lineEdit_valor_saida.setMinimumSize(QSize(0, 44))
		self.lineEdit_valor_saida.setMaximumSize(QSize(206, 16777215))
		self.lineEdit_valor_saida.setFont(font2)
		self.lineEdit_valor_saida.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_valor_saida.setStyleSheet(u"QLineEdit:hover{border-color: #28A745}\n"
	"QLineEdit:focus{border-color: #28A745}\n"
	"QLineEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")

		########################################################
		# self.lineEdit_valor_saida.setValidator(self.validaValor)
		self.lineEdit_valor_saida.setMaxLength(9)
		self.lineEdit_valor_saida.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
		########################################################

		self.verticalLayout_54.addWidget(self.lineEdit_valor_saida)

		self.horizontalLayout_14.addWidget(self.frame_46)

		self.horizontalSpacer_21 = QSpacerItem(581, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_14.addItem(self.horizontalSpacer_21)

		self.verticalLayout_22.addWidget(self.frame_4)

		self.verticalSpacer_5 = QSpacerItem(20, 415, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.verticalLayout_22.addItem(self.verticalSpacer_5)

		self.verticalLayout_56.addWidget(self.meio_saida_2)

		self.verticalLayout_20.addWidget(self.meio_saida)

		self.inferior_saida = QFrame(self.main_saida)
		self.inferior_saida.setObjectName(u"inferior_saida")
		self.inferior_saida.setMinimumSize(QSize(0, 156))
		self.inferior_saida.setMaximumSize(QSize(16777215, 156))
		self.inferior_saida.setFont(font20)
		self.inferior_saida.setFrameShape(QFrame.StyledPanel)
		self.inferior_saida.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_24 = QHBoxLayout(self.inferior_saida)
		self.horizontalLayout_24.setSpacing(0)
		self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
		self.horizontalLayout_24.setContentsMargins(32, 0, 32, 0)
		self.inferior_saida_2 = QFrame(self.inferior_saida)
		self.inferior_saida_2.setObjectName(u"inferior_saida_2")
		self.inferior_saida_2.setMinimumSize(QSize(0, 156))
		self.inferior_saida_2.setMaximumSize(QSize(1028, 156))
		self.inferior_saida_2.setFont(font20)
		self.inferior_saida_2.setFrameShape(QFrame.StyledPanel)
		self.inferior_saida_2.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_25 = QHBoxLayout(self.inferior_saida_2)
		self.horizontalLayout_25.setSpacing(0)
		self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
		self.horizontalLayout_25.setContentsMargins(24, 0, 24, 48)
		self.btn_visualizar_saida = QPushButton(self.inferior_saida_2)
		self.btn_visualizar_saida.setObjectName(u"btn_visualizar_saida")
		self.btn_visualizar_saida.setEnabled(True)
		self.btn_visualizar_saida.setMinimumSize(QSize(160, 50))
		self.btn_visualizar_saida.setFont(font20)
		self.btn_visualizar_saida.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_visualizar_saida.setStyleSheet(u"QPushButton:hover{background: #5F7A99; color: #fff;} QPushButton{background-color: #fff; color: #5F7A99;  border-radius: 22px; border:2px solid #5F7A99}")

		self.horizontalLayout_25.addWidget(self.btn_visualizar_saida)
		
		self.horizontalSpacer_17 = QSpacerItem(678, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_25.addItem(self.horizontalSpacer_17)

		self.btn_salvar_saida = QPushButton(self.inferior_saida_2)
		self.btn_salvar_saida.setObjectName(u"btn_salvar_saida")
		self.btn_salvar_saida.setMinimumSize(QSize(160, 50))
		self.btn_salvar_saida.setFont(font20)
		self.btn_salvar_saida.setStyleSheet(u"QPushButton:hover{background: #198754;} QPushButton{background-color: #28A745; color: #fff;  border-radius: 22px;}")

		self.horizontalLayout_25.addWidget(self.btn_salvar_saida)

		self.horizontalLayout_24.addWidget(self.inferior_saida_2)

		self.verticalLayout_20.addWidget(self.inferior_saida)

		self.verticalLayout_19.addWidget(self.main_saida)

		self.pages.addWidget(self.saidas)
		self.financeiro = QWidget()
		self.financeiro.setObjectName(u"financeiro")
		self.financeiro.setFont(font)
		self.verticalLayout = QVBoxLayout(self.financeiro)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.verticalLayout.setContentsMargins(56, 64, 56, 64)
		self.main_financeiro = QFrame(self.financeiro)
		self.main_financeiro.setObjectName(u"main_financeiro")
		self.main_financeiro.setFont(font)
		self.main_financeiro.setStyleSheet(u"background-color: #fff; border-radius:15px;")
		self.main_financeiro.setFrameShape(QFrame.StyledPanel)
		self.main_financeiro.setFrameShadow(QFrame.Raised)
		self.verticalLayout_67 = QVBoxLayout(self.main_financeiro)
		self.verticalLayout_67.setSpacing(0)
		self.verticalLayout_67.setObjectName(u"verticalLayout_67")
		self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
		self.superior_financeiro = QFrame(self.main_financeiro)
		self.superior_financeiro.setObjectName(u"superior_financeiro")
		self.superior_financeiro.setMaximumSize(QSize(16777215, 105))
		self.superior_financeiro.setFont(font15)
		self.superior_financeiro.setFrameShape(QFrame.StyledPanel)
		self.superior_financeiro.setFrameShadow(QFrame.Raised)
		self.verticalLayout_68 = QVBoxLayout(self.superior_financeiro)
		self.verticalLayout_68.setSpacing(0)
		self.verticalLayout_68.setObjectName(u"verticalLayout_68")
		self.verticalLayout_68.setContentsMargins(0, 40, 0, 0)
		self.label_16 = QLabel(self.superior_financeiro)
		self.label_16.setObjectName(u"label_16")
		self.label_16.setMaximumSize(QSize(16777215, 16777215))
		self.label_16.setFont(font15)
		self.label_16.setStyleSheet(u"color: #3A4B5E")
		self.label_16.setAlignment(Qt.AlignCenter)

		self.verticalLayout_68.addWidget(self.label_16)

		self.verticalLayout_67.addWidget(self.superior_financeiro)

		self.meio_financeiro = QFrame(self.main_financeiro)
		self.meio_financeiro.setObjectName(u"meio_financeiro")
		self.meio_financeiro.setMinimumSize(QSize(0, 660))
		self.meio_financeiro.setFont(font)
		self.meio_financeiro.setFrameShape(QFrame.StyledPanel)
		self.meio_financeiro.setFrameShadow(QFrame.Raised)
		self.verticalLayout_69 = QVBoxLayout(self.meio_financeiro)
		self.verticalLayout_69.setSpacing(0)
		self.verticalLayout_69.setObjectName(u"verticalLayout_69")
		self.verticalLayout_69.setContentsMargins(40, 0, 40, 40)
		self.meio_financeiro_2 = QFrame(self.meio_financeiro)
		self.meio_financeiro_2.setObjectName(u"meio_financeiro_2")
		self.meio_financeiro_2.setMinimumSize(QSize(0, 0))
		self.meio_financeiro_2.setMaximumSize(QSize(16777215, 16777215))
		self.meio_financeiro_2.setFont(font)
		self.meio_financeiro_2.setFrameShape(QFrame.StyledPanel)
		self.meio_financeiro_2.setFrameShadow(QFrame.Raised)
		self.verticalLayout_70 = QVBoxLayout(self.meio_financeiro_2)
		self.verticalLayout_70.setSpacing(0)
		self.verticalLayout_70.setObjectName(u"verticalLayout_70")
		self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
		self.meio_financeiro_busca = QFrame(self.meio_financeiro_2)
		self.meio_financeiro_busca.setObjectName(u"meio_financeiro_busca")
		self.meio_financeiro_busca.setMinimumSize(QSize(0, 0))
		self.meio_financeiro_busca.setMaximumSize(QSize(16777215, 166))
		self.meio_financeiro_busca.setFrameShape(QFrame.StyledPanel)
		self.meio_financeiro_busca.setFrameShadow(QFrame.Raised)
		self.verticalLayout_78 = QVBoxLayout(self.meio_financeiro_busca)
		self.verticalLayout_78.setSpacing(12)
		self.verticalLayout_78.setObjectName(u"verticalLayout_78")
		self.verticalLayout_78.setContentsMargins(0, 40, 0, 0)
		self.label_18 = QLabel(self.meio_financeiro_busca)
		self.label_18.setObjectName(u"label_18")
		self.label_18.setMaximumSize(QSize(100, 16))
		self.label_18.setFont(font2)
		self.label_18.setStyleSheet(u"color: #3A4B5E; padding-left: 14px")

		self.verticalLayout_78.addWidget(self.label_18)

		self.frame_47 = QFrame(self.meio_financeiro_busca)
		self.frame_47.setObjectName(u"frame_47")
		self.frame_47.setMaximumSize(QSize(16777215, 100))
		self.frame_47.setFont(font)
		self.frame_47.setStyleSheet(u"QFrame#frame_47{border-radius: 15px; border-width: 1px; border-style: solid; border-color: #c4c4c4}")
		self.frame_47.setFrameShape(QFrame.StyledPanel)
		self.frame_47.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_35 = QHBoxLayout(self.frame_47)
		self.horizontalLayout_35.setSpacing(16)
		self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
		self.horizontalLayout_35.setContentsMargins(24, 6, 24, 24)
		self.frame_50 = QFrame(self.frame_47)
		self.frame_50.setObjectName(u"frame_50")
		self.frame_50.setMinimumSize(QSize(206, 0))
		self.frame_50.setMaximumSize(QSize(256, 16777215))
		self.frame_50.setFrameShape(QFrame.StyledPanel)
		self.frame_50.setFrameShadow(QFrame.Raised)
		self.verticalLayout_72 = QVBoxLayout(self.frame_50)
		self.verticalLayout_72.setSpacing(4)
		self.verticalLayout_72.setObjectName(u"verticalLayout_72")
		self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_financ_data_inicio = QLabel(self.frame_50)
		self.label_aviso_financ_data_inicio.setObjectName(u"label_aviso_financ_data_inicio")
		self.label_aviso_financ_data_inicio.setMinimumSize(QSize(0, 0))
		self.label_aviso_financ_data_inicio.setFont(font18)
		self.label_aviso_financ_data_inicio.setStyleSheet(u"color: red;")
		self.label_aviso_financ_data_inicio.setAlignment(Qt.AlignCenter)

		self.verticalLayout_72.addWidget(self.label_aviso_financ_data_inicio)

		self.lineEdit_financ_data_inicio = QDateEdit(self.frame_50)
		self.lineEdit_financ_data_inicio.setObjectName(u"lineEdit_financ_data_inicio")
		self.lineEdit_financ_data_inicio.setMinimumSize(QSize(0, 44))
		self.lineEdit_financ_data_inicio.setMaximumSize(QSize(16777215, 16777215))
		self.lineEdit_financ_data_inicio.setFont(font2)
		self.lineEdit_financ_data_inicio.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_financ_data_inicio.setStyleSheet(u"QDateEdit:hover{border-color: #28A745}\n"
	"QDateEdit:focus{border-color: #28A745}\n"
	"QDateEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")
		self.lineEdit_financ_data_inicio.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.lineEdit_financ_data_inicio.setProperty("showGroupSeparator", False)

		self.verticalLayout_72.addWidget(self.lineEdit_financ_data_inicio)

		self.horizontalLayout_35.addWidget(self.frame_50)

		self.frame_53 = QFrame(self.frame_47)
		self.frame_53.setObjectName(u"frame_53")
		self.frame_53.setMinimumSize(QSize(206, 0))
		self.frame_53.setMaximumSize(QSize(256, 16777215))
		self.frame_53.setFrameShape(QFrame.StyledPanel)
		self.frame_53.setFrameShadow(QFrame.Raised)
		self.verticalLayout_73 = QVBoxLayout(self.frame_53)
		self.verticalLayout_73.setSpacing(4)
		self.verticalLayout_73.setObjectName(u"verticalLayout_73")
		self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
		self.label_aviso_financ_data_fim = QLabel(self.frame_53)
		self.label_aviso_financ_data_fim.setObjectName(u"label_aviso_financ_data_fim")
		self.label_aviso_financ_data_fim.setMinimumSize(QSize(0, 0))
		self.label_aviso_financ_data_fim.setFont(font18)
		self.label_aviso_financ_data_fim.setStyleSheet(u"color: red;")
		self.label_aviso_financ_data_fim.setAlignment(Qt.AlignCenter)

		self.verticalLayout_73.addWidget(self.label_aviso_financ_data_fim)

		self.lineEdit_financ_data_fim = QDateEdit(self.frame_53)
		self.lineEdit_financ_data_fim.setObjectName(u"lineEdit_financ_data_fim")
		self.lineEdit_financ_data_fim.setMinimumSize(QSize(0, 44))
		self.lineEdit_financ_data_fim.setMaximumSize(QSize(16777215, 16777215))
		self.lineEdit_financ_data_fim.setFont(font2)
		self.lineEdit_financ_data_fim.setFocusPolicy(Qt.StrongFocus)
		self.lineEdit_financ_data_fim.setStyleSheet(u"QDateEdit:hover{border-color: #28A745}\n"
	"QDateEdit:focus{border-color: #28A745}\n"
	"QDateEdit{border-radius: 22px; border-width: 1px; border-style: solid; border-color: #c4c4c4; padding-left:16px}")
		self.lineEdit_financ_data_fim.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.lineEdit_financ_data_fim.setProperty("showGroupSeparator", False)

		self.verticalLayout_73.addWidget(self.lineEdit_financ_data_fim)

		self.horizontalLayout_35.addWidget(self.frame_53)

		self.frame_54 = QFrame(self.frame_47)
		self.frame_54.setObjectName(u"frame_54")
		self.frame_54.setMaximumSize(QSize(178, 16777215))
		self.frame_54.setFrameShape(QFrame.StyledPanel)
		self.frame_54.setFrameShadow(QFrame.Raised)
		self.verticalLayout_75 = QVBoxLayout(self.frame_54)
		self.verticalLayout_75.setSpacing(4)
		self.verticalLayout_75.setObjectName(u"verticalLayout_75")
		self.verticalLayout_75.setContentsMargins(8, 0, 0, 0)
		self.label_31 = QLabel(self.frame_54)
		self.label_31.setObjectName(u"label_31")

		self.verticalLayout_75.addWidget(self.label_31)

		self.comboBox_financeiro = QComboBox(self.frame_54)
		self.comboBox_financeiro.addItem("")
		self.comboBox_financeiro.addItem("")
		self.comboBox_financeiro.addItem("")
		self.comboBox_financeiro.setObjectName(u"comboBox_financeiro")
		self.comboBox_financeiro.setMinimumSize(QSize(156, 44))
		self.comboBox_financeiro.setFont(font2)
		self.comboBox_financeiro.setStyleSheet(u'''QComboBox:hover{border-color:#28A745;}
	QComboBox:focus{border-color:#28A745;}QComboBox{color: #848484; border-radius: 10px; border-width: 1px; border-style: solid; border-color:#c4c4c4; padding-left: 10px;}
	QComboBox:drop-down:hover{background-color:#eeeeee}
	QComboBox:drop-down{width: 24px; border-top-right-radius:9px; border-bottom-right-radius:9px; border-top-left-radius:1px; border-bottom-left-radius:1px;}
	QComboBox:down-arrow{image: url(icons/expand_more_blue_18dp.svg); width: 18px; height: 18px;}
	''')
		self.comboBox_financeiro.setCursor(QCursor(Qt.PointingHandCursor))
		self.verticalLayout_75.addWidget(self.comboBox_financeiro)

		self.horizontalLayout_35.addWidget(self.frame_54)

		self.frame_56 = QFrame(self.frame_47)
		self.frame_56.setObjectName(u"frame_56")
		self.frame_56.setMaximumSize(QSize(138, 16777215))
		self.frame_56.setFrameShape(QFrame.StyledPanel)
		self.frame_56.setFrameShadow(QFrame.Raised)
		self.verticalLayout_76 = QVBoxLayout(self.frame_56)
		self.verticalLayout_76.setSpacing(0)
		self.verticalLayout_76.setObjectName(u"verticalLayout_76")
		self.verticalLayout_76.setContentsMargins(24, 20, 0, 0)
		self.pushButton_buscar_financeiro = QPushButton(self.frame_56)
		self.pushButton_buscar_financeiro.setObjectName(u"pushButton_buscar_financeiro")
		self.pushButton_buscar_financeiro.setMinimumSize(QSize(0, 44))
		font21 = QFont()
		font21.setPointSize(14)
		font21.setBold(True)
		self.pushButton_buscar_financeiro.setFont(font21)
		self.pushButton_buscar_financeiro.setStyleSheet(u"QPushButton:hover{color:#fff;  background-color: #5F7A99; border-color: #5F7A99;}\n"
	"QPushButton{color:#5F7A99; border-radius: 16px; border-width: 1px; border-style: solid; border-color: #5F7A99;}")
		self.pushButton_buscar_financeiro.setCursor(QCursor(Qt.PointingHandCursor))

		self.verticalLayout_76.addWidget(self.pushButton_buscar_financeiro)

		self.horizontalLayout_35.addWidget(self.frame_56)

		self.verticalLayout_78.addWidget(self.frame_47)

		self.verticalLayout_70.addWidget(self.meio_financeiro_busca)

		self.frame_48 = QFrame(self.meio_financeiro_2)
		self.frame_48.setObjectName(u"frame_48")
		self.frame_48.setMaximumSize(QSize(16777215, 0))
		self.frame_48.setFrameShape(QFrame.StyledPanel)
		self.frame_48.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_42 = QHBoxLayout(self.frame_48)
		self.horizontalLayout_42.setSpacing(0)
		self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
		self.horizontalLayout_42.setContentsMargins(0, 40, 0, 0)
		self.pagFinanceiro = QStackedWidget(self.frame_48)
		self.pagFinanceiro.setObjectName(u"pagFinanceiro")
		self.tabela_entrada = QWidget()
		self.tabela_entrada.setObjectName(u"tabela_entrada")
		self.verticalLayout_79 = QVBoxLayout(self.tabela_entrada)
		self.verticalLayout_79.setSpacing(0)
		self.verticalLayout_79.setObjectName(u"verticalLayout_79")
		self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
		self.tableWidget_entrada = QTableWidget(self.tabela_entrada)
		if (self.tableWidget_entrada.columnCount() < 6):
			self.tableWidget_entrada.setColumnCount(6)
		__qtablewidgetitem9 = QTableWidgetItem()
		__qtablewidgetitem9.setFont(font16);
		__qtablewidgetitem9.setForeground(QColor('#3A4B5E'))
		self.tableWidget_entrada.setHorizontalHeaderItem(0, __qtablewidgetitem9)
		__qtablewidgetitem10 = QTableWidgetItem()
		__qtablewidgetitem10.setFont(font16);
		__qtablewidgetitem10.setForeground(QColor('#3A4B5E'))
		self.tableWidget_entrada.setHorizontalHeaderItem(1, __qtablewidgetitem10)
		__qtablewidgetitem11 = QTableWidgetItem()
		__qtablewidgetitem11.setFont(font16);
		__qtablewidgetitem11.setForeground(QColor('#3A4B5E'))
		self.tableWidget_entrada.setHorizontalHeaderItem(2, __qtablewidgetitem11)
		__qtablewidgetitem12 = QTableWidgetItem()
		__qtablewidgetitem12.setFont(font16);
		__qtablewidgetitem12.setForeground(QColor('#3A4B5E'))
		self.tableWidget_entrada.setHorizontalHeaderItem(3, __qtablewidgetitem12)
		__qtablewidgetitem13 = QTableWidgetItem()
		__qtablewidgetitem13.setFont(font16);
		__qtablewidgetitem13.setForeground(QColor('#3A4B5E'))
		self.tableWidget_entrada.setHorizontalHeaderItem(4, __qtablewidgetitem13)
		__qtablewidgetitem14 = QTableWidgetItem()
		__qtablewidgetitem14.setFont(font16);
		__qtablewidgetitem14.setForeground(QColor('#3A4B5E'))
		self.tableWidget_entrada.setHorizontalHeaderItem(5, __qtablewidgetitem14)
		self.tableWidget_entrada.setObjectName(u"tableWidget_entrada")
		self.tableWidget_entrada.setFont(font2)
		self.tableWidget_entrada.setStyleSheet(u"QTableView{color: #3A4B5E;}")
		self.tableWidget_entrada.horizontalHeader().setStyleSheet(u"QHeaderView::Section{background-color:#fff; border:hidden}")
		self.tableWidget_entrada.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_entrada.setAlternatingRowColors(True)
		self.tableWidget_entrada.setShowGrid(True)
		self.tableWidget_entrada.setGridStyle(Qt.SolidLine)
		self.tableWidget_entrada.setSortingEnabled(False)
		self.tableWidget_entrada.horizontalHeader().setCascadingSectionResizes(False)
		self.tableWidget_entrada.horizontalHeader().setStretchLastSection(False)
		self.tableWidget_entrada.verticalHeader().setVisible(False)
		self.tableWidget_entrada.verticalHeader().setStretchLastSection(False)
		self.tableWidget_entrada.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

		self.verticalLayout_79.addWidget(self.tableWidget_entrada)

		self.frame_55 = QFrame(self.tabela_entrada)
		self.frame_55.setObjectName(u"frame_55")
		self.frame_55.setFrameShape(QFrame.StyledPanel)
		self.frame_55.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_44 = QHBoxLayout(self.frame_55)
		self.horizontalLayout_44.setSpacing(0)
		self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
		self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
		self.label_20 = QLabel(self.frame_55)
		self.label_20.setObjectName(u"label_20")
		font22 = QFont()
		font22.setPointSize(18)
		font22.setBold(True)
		self.label_20.setFont(font22)
		self.label_20.setStyleSheet(u"color: #3A4B5E")
		self.label_20.setAlignment(Qt.AlignCenter)
		self.label_20.setMaximumWidth(100)
		self.horizontalLayout_44.addWidget(self.label_20)

		#self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		#self.horizontalLayout_44.addItem(self.horizontalSpacer_22)

		self.total_financeiro_saida_1 = QLabel(self.frame_55)
		self.total_financeiro_saida_1.setObjectName(u"total_financeiro_saida_1")
		font23 = QFont()
		font23.setPointSize(18)
		self.total_financeiro_saida_1.setFont(font23)
		self.total_financeiro_saida_1.setStyleSheet(u"color: #3A4B5E")
		self.total_financeiro_saida_1.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_44.addWidget(self.total_financeiro_saida_1)

		#self.horizontalSpacer_30 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		#self.horizontalLayout_44.addItem(self.horizontalSpacer_30)

		self.total_financeiro_saida_2 = QLabel(self.frame_55)
		self.total_financeiro_saida_2.setObjectName(u"total_financeiro_saida_2")
		self.total_financeiro_saida_2.setFont(font23)
		self.total_financeiro_saida_2.setStyleSheet(u"color: #3A4B5E")
		self.total_financeiro_saida_2.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_44.addWidget(self.total_financeiro_saida_2)

		#self.horizontalSpacer_31 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		#self.horizontalLayout_44.addItem(self.horizontalSpacer_31)

		self.total_financeiro_saida_3 = QLabel(self.frame_55)
		self.total_financeiro_saida_3.setObjectName(u"total_financeiro_saida_3")
		self.total_financeiro_saida_3.setFont(font23)
		self.total_financeiro_saida_3.setStyleSheet(u"color: #3A4B5E")
		self.total_financeiro_saida_3.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_44.addWidget(self.total_financeiro_saida_3)

		#self.horizontalSpacer_32 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		#self.horizontalLayout_44.addItem(self.horizontalSpacer_32)

		self.total_financeiro_saida_4 = QLabel(self.frame_55)
		self.total_financeiro_saida_4.setObjectName(u"total_financeiro_saida_4")
		self.total_financeiro_saida_4.setFont(font23)
		self.total_financeiro_saida_4.setStyleSheet(u"color: #3A4B5E")
		self.total_financeiro_saida_4.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_44.addWidget(self.total_financeiro_saida_4)

		#self.horizontalSpacer_33 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		#self.horizontalLayout_44.addItem(self.horizontalSpacer_33)

		self.total_financeiro_saida_5 = QLabel(self.frame_55)
		self.total_financeiro_saida_5.setObjectName(u"total_financeiro_saida_5")
		self.total_financeiro_saida_5.setFont(font23)
		self.total_financeiro_saida_5.setStyleSheet(u"color: #3A4B5E")
		self.total_financeiro_saida_5.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_44.addWidget(self.total_financeiro_saida_5)

		self.verticalLayout_79.addWidget(self.frame_55)

		self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
		self.verticalLayout_79.addItem(self.verticalSpacer)

		self.pagFinanceiro.addWidget(self.tabela_entrada)
		self.tabela_saida = QWidget()
		self.tabela_saida.setObjectName(u"tabela_saida")
		self.verticalLayout_80 = QVBoxLayout(self.tabela_saida)
		self.verticalLayout_80.setSpacing(0)
		self.verticalLayout_80.setObjectName(u"verticalLayout_80")
		self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
		self.tableWidget_saida = QTableWidget(self.tabela_saida)
		if (self.tableWidget_saida.columnCount() < 3):
			self.tableWidget_saida.setColumnCount(3)
		__qtablewidgetitem15 = QTableWidgetItem()
		__qtablewidgetitem15.setFont(font16);
		__qtablewidgetitem15.setForeground(QColor('#3A4B5E'))
		self.tableWidget_saida.setHorizontalHeaderItem(0, __qtablewidgetitem15)
		__qtablewidgetitem16 = QTableWidgetItem()
		__qtablewidgetitem16.setFont(font16);
		__qtablewidgetitem16.setForeground(QColor('#3A4B5E'))
		self.tableWidget_saida.setHorizontalHeaderItem(1, __qtablewidgetitem16)
		__qtablewidgetitem17 = QTableWidgetItem()
		__qtablewidgetitem17.setFont(font16);
		__qtablewidgetitem17.setForeground(QColor('#3A4B5E'))
		self.tableWidget_saida.setHorizontalHeaderItem(2, __qtablewidgetitem17)
		self.tableWidget_saida.setObjectName(u"tableWidget_saida")
		self.tableWidget_saida.setFont(font2)
		self.tableWidget_saida.setStyleSheet(u"QTableView{color: #3A4B5E;}")
		self.tableWidget_saida.horizontalHeader().setStyleSheet(u"QHeaderView::Section{background-color:#fff; border:hidden}")
		self.tableWidget_saida.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tableWidget_saida.setAlternatingRowColors(True)
		self.tableWidget_saida.setShowGrid(True)
		self.tableWidget_saida.setGridStyle(Qt.SolidLine)
		self.tableWidget_saida.setSortingEnabled(False)
		self.tableWidget_saida.horizontalHeader().setCascadingSectionResizes(False)
		self.tableWidget_saida.horizontalHeader().setStretchLastSection(False)
		self.tableWidget_saida.verticalHeader().setVisible(False)
		self.tableWidget_saida.verticalHeader().setStretchLastSection(False)
		self.tableWidget_saida.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

		self.verticalLayout_80.addWidget(self.tableWidget_saida)

		self.frame_52 = QFrame(self.tabela_saida)
		self.frame_52.setObjectName(u"frame_52")
		self.frame_52.setFrameShape(QFrame.StyledPanel)
		self.frame_52.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_43 = QHBoxLayout(self.frame_52)
		self.horizontalLayout_43.setSpacing(0)
		self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
		self.horizontalLayout_43.setContentsMargins(0, 32, 0, 0)
		self.label_19 = QLabel(self.frame_52)
		self.label_19.setObjectName(u"label_19")
		self.label_19.setFont(font22)
		self.label_19.setStyleSheet(u"color: #3A4B5E")
		self.label_19.setMinimumWidth(95)
		self.label_19.setAlignment(Qt.AlignCenter)
		self.horizontalLayout_43.addWidget(self.label_19)

		self.horizontalSpacer_16 = QSpacerItem(767, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_43.addItem(self.horizontalSpacer_16)

		self.total_financeiro_saida = QLabel(self.frame_52)
		self.total_financeiro_saida.setObjectName(u"total_financeiro_saida")
		self.total_financeiro_saida.setFont(font23)
		self.total_financeiro_saida.setStyleSheet(u"color: #3A4B5E")
		self.total_financeiro_saida.setMinimumWidth(130)

		self.horizontalLayout_43.addWidget(self.total_financeiro_saida)


		self.verticalLayout_80.addWidget(self.frame_52)

		self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
		self.verticalLayout_80.addItem(self.verticalSpacer_10)

		self.pagFinanceiro.addWidget(self.tabela_saida)
		self.tabela_entrada_saida = QWidget()
		self.tabela_entrada_saida.setObjectName(u"tabela_entrada_saida")
		self.verticalLayout_77 = QVBoxLayout(self.tabela_entrada_saida)
		self.verticalLayout_77.setSpacing(0)
		self.verticalLayout_77.setObjectName(u"verticalLayout_77")
		self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
		self.scrollArea_2 = QScrollArea(self.tabela_entrada_saida)
		self.scrollArea_2.setObjectName(u"scrollArea_2")
		self.scrollArea_2.setWidgetResizable(True)
		self.scrollAreaWidgetContents_2 = QWidget()
		self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
		self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 948, 455))
		self.verticalLayout_71 = QVBoxLayout(self.scrollAreaWidgetContents_2)
		self.verticalLayout_71.setSpacing(0)
		self.verticalLayout_71.setObjectName(u"verticalLayout_71")
		self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
		self.frame_58 = QFrame(self.scrollAreaWidgetContents_2)
		self.frame_58.setObjectName(u"frame_58")
		self.frame_58.setMinimumSize(QSize(0, 40))
		self.frame_58.setStyleSheet(u"QFrame#frame_58{border-radius: 0px; border-bottom: 1px solid #c4c4c4;}")
		self.frame_58.setFrameShape(QFrame.StyledPanel)
		self.frame_58.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_23 = QHBoxLayout(self.frame_58)
		self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
		self.label_45 = QLabel(self.frame_58)
		self.label_45.setObjectName(u"label_45")
		self.label_45.setMinimumSize(QSize(0, 24))
		self.label_45.setFont(font2)
		self.label_45.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_23.addWidget(self.label_45)

		self.label_46 = QLabel(self.frame_58)
		self.label_46.setObjectName(u"label_46")
		self.label_46.setMinimumSize(QSize(0, 24))
		self.label_46.setMaximumSize(QSize(160, 16777215))
		self.label_46.setFont(font2)
		self.label_46.setStyleSheet(u"color: #3A4B5E")
		self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_23.addWidget(self.label_46)


		self.verticalLayout_71.addWidget(self.frame_58)

		self.frame_63 = QFrame(self.scrollAreaWidgetContents_2)
		self.frame_63.setObjectName(u"frame_63")
		self.frame_63.setMinimumSize(QSize(0, 40))
		self.frame_63.setStyleSheet(u"QFrame#frame_63{border-radius: 0px; border-top: 1px solid #c4c4c4;}")
		self.frame_63.setFrameShape(QFrame.StyledPanel)
		self.frame_63.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_45 = QHBoxLayout(self.frame_63)
		self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
		self.label_21 = QLabel(self.frame_63)
		self.label_21.setObjectName(u"label_21")
		self.label_21.setMinimumSize(QSize(0, 24))
		self.label_21.setFont(font2)
		self.label_21.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_45.addWidget(self.label_21)

		self.label_22 = QLabel(self.frame_63)
		self.label_22.setObjectName(u"label_22")
		self.label_22.setMinimumSize(QSize(0, 24))
		self.label_22.setMaximumSize(QSize(160, 16777215))
		self.label_22.setFont(font2)
		self.label_22.setStyleSheet(u"color: #3A4B5E")
		self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_45.addWidget(self.label_22)


		self.verticalLayout_71.addWidget(self.frame_63)

		self.frame_49 = QFrame(self.scrollAreaWidgetContents_2)
		self.frame_49.setObjectName(u"frame_49")
		self.frame_49.setMinimumSize(QSize(0, 40))
		self.frame_49.setFrameShape(QFrame.StyledPanel)
		self.frame_49.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_46 = QHBoxLayout(self.frame_49)
		self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
		self.label_23 = QLabel(self.frame_49)
		self.label_23.setObjectName(u"label_23")
		self.label_23.setMinimumSize(QSize(0, 24))
		self.label_23.setFont(font2)
		self.label_23.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_46.addWidget(self.label_23)

		self.label_24 = QLabel(self.frame_49)
		self.label_24.setObjectName(u"label_24")
		self.label_24.setMinimumSize(QSize(0, 24))
		self.label_24.setMaximumSize(QSize(160, 16777215))
		self.label_24.setFont(font2)
		self.label_24.setStyleSheet(u"color: #3A4B5E")
		self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_46.addWidget(self.label_24)


		self.verticalLayout_71.addWidget(self.frame_49)

		self.frame_62 = QFrame(self.scrollAreaWidgetContents_2)
		self.frame_62.setObjectName(u"frame_62")
		self.frame_62.setMinimumSize(QSize(0, 40))
		self.frame_62.setFrameShape(QFrame.StyledPanel)
		self.frame_62.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_47 = QHBoxLayout(self.frame_62)
		self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
		self.label_25 = QLabel(self.frame_62)
		self.label_25.setObjectName(u"label_25")
		self.label_25.setMinimumSize(QSize(0, 24))
		self.label_25.setFont(font2)
		self.label_25.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_47.addWidget(self.label_25)

		self.label_26 = QLabel(self.frame_62)
		self.label_26.setObjectName(u"label_26")
		self.label_26.setMinimumSize(QSize(0, 24))
		self.label_26.setMaximumSize(QSize(160, 16777215))
		self.label_26.setFont(font2)
		self.label_26.setStyleSheet(u"color: #3A4B5E")
		self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_47.addWidget(self.label_26)

		self.verticalLayout_71.addWidget(self.frame_62)

		self.frame_59 = QFrame(self.scrollAreaWidgetContents_2)
		self.frame_59.setObjectName(u"frame_59")
		self.frame_59.setMinimumSize(QSize(0, 40))
		self.frame_59.setFrameShape(QFrame.StyledPanel)
		self.frame_59.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_48 = QHBoxLayout(self.frame_59)
		self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
		self.label_27 = QLabel(self.frame_59)
		self.label_27.setObjectName(u"label_27")
		self.label_27.setMinimumSize(QSize(0, 24))
		self.label_27.setFont(font2)
		self.label_27.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_48.addWidget(self.label_27)

		self.label_28 = QLabel(self.frame_59)
		self.label_28.setObjectName(u"label_28")
		self.label_28.setMinimumSize(QSize(0, 24))
		self.label_28.setMaximumSize(QSize(160, 16777215))
		self.label_28.setFont(font2)
		self.label_28.setStyleSheet(u"color: #3A4B5E")
		self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_48.addWidget(self.label_28)

		self.verticalLayout_71.addWidget(self.frame_59)

		self.frame_64 = QFrame(self.scrollAreaWidgetContents_2)
		self.frame_64.setObjectName(u"frame_64")
		self.frame_64.setMinimumSize(QSize(0, 40))
		self.frame_64.setFrameShape(QFrame.StyledPanel)
		self.frame_64.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_49 = QHBoxLayout(self.frame_64)
		self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
		self.label_29 = QLabel(self.frame_64)
		self.label_29.setObjectName(u"label_29")
		self.label_29.setMinimumSize(QSize(0, 24))
		self.label_29.setFont(font2)
		self.label_29.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_49.addWidget(self.label_29)

		self.label_30 = QLabel(self.frame_64)
		self.label_30.setObjectName(u"label_30")
		self.label_30.setMinimumSize(QSize(0, 24))
		self.label_30.setMaximumSize(QSize(160, 16777215))
		self.label_30.setFont(font2)
		self.label_30.setStyleSheet(u"color: #3A4B5E")
		self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_49.addWidget(self.label_30)

		self.verticalLayout_71.addWidget(self.frame_64)

		self.frame_65 = QFrame(self.scrollAreaWidgetContents_2)
		self.frame_65.setObjectName(u"frame_65")
		self.frame_65.setMinimumSize(QSize(0, 40))
		self.frame_65.setStyleSheet(u"QFrame#frame_65{border-radius: 0px; border-bottom: 1px solid #c4c4c4;}")
		self.frame_65.setFrameShape(QFrame.StyledPanel)
		self.frame_65.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_51 = QHBoxLayout(self.frame_65)
		self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
		self.label_33 = QLabel(self.frame_65)
		self.label_33.setObjectName(u"label_33")
		self.label_33.setMinimumSize(QSize(0, 24))
		self.label_33.setFont(font2)
		self.label_33.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_51.addWidget(self.label_33)

		self.label_34 = QLabel(self.frame_65)
		self.label_34.setObjectName(u"label_34")
		self.label_34.setMinimumSize(QSize(0, 24))
		self.label_34.setMaximumSize(QSize(160, 16777215))
		self.label_34.setFont(font2)
		self.label_34.setStyleSheet(u"color: #3A4B5E")
		self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_51.addWidget(self.label_34)

		self.verticalLayout_71.addWidget(self.frame_65)

		self.frame_60 = QFrame(self.scrollAreaWidgetContents_2)
		self.frame_60.setObjectName(u"frame_60")
		self.frame_60.setMinimumSize(QSize(0, 40))
		self.frame_60.setStyleSheet(u"QFrame#frame_60{border-radius: 0px; border-top: 1px solid #c4c4c4;}")
		self.frame_60.setFrameShape(QFrame.StyledPanel)
		self.frame_60.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_52 = QHBoxLayout(self.frame_60)
		self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
		self.label_35 = QLabel(self.frame_60)
		self.label_35.setObjectName(u"label_35")
		self.label_35.setMinimumSize(QSize(0, 24))
		self.label_35.setFont(font2)
		self.label_35.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_52.addWidget(self.label_35)

		self.label_36 = QLabel(self.frame_60)
		self.label_36.setObjectName(u"label_36")
		self.label_36.setMinimumSize(QSize(0, 24))
		self.label_36.setMaximumSize(QSize(160, 16777215))
		self.label_36.setFont(font2)
		self.label_36.setStyleSheet(u"color: #3A4B5E")
		self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_52.addWidget(self.label_36)

		self.verticalLayout_71.addWidget(self.frame_60)

		self.frame_51 = QFrame(self.scrollAreaWidgetContents_2)
		self.frame_51.setObjectName(u"frame_51")
		self.frame_51.setMinimumSize(QSize(0, 40))
		self.frame_51.setStyleSheet(u"QFrame#frame_51{border-radius: 0px; border-bottom: 1px solid #c4c4c4;}")
		self.frame_51.setFrameShape(QFrame.StyledPanel)
		self.frame_51.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_53 = QHBoxLayout(self.frame_51)
		self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
		self.label_37 = QLabel(self.frame_51)
		self.label_37.setObjectName(u"label_37")
		self.label_37.setMinimumSize(QSize(0, 24))
		self.label_37.setFont(font2)
		self.label_37.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_53.addWidget(self.label_37)

		self.label_38 = QLabel(self.frame_51)
		self.label_38.setObjectName(u"label_38")
		self.label_38.setMinimumSize(QSize(0, 24))
		self.label_38.setMaximumSize(QSize(160, 16777215))
		self.label_38.setFont(font2)
		self.label_38.setStyleSheet(u"color: #3A4B5E")
		self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_53.addWidget(self.label_38)

		self.verticalLayout_71.addWidget(self.frame_51)

		self.frame_66 = QFrame(self.scrollAreaWidgetContents_2)
		self.frame_66.setObjectName(u"frame_66")
		self.frame_66.setMinimumSize(QSize(0, 40))
		self.frame_66.setStyleSheet(u"QFrame#frame_66{border-radius: 0px; border-top: 1px solid #c4c4c4;}")
		self.frame_66.setFrameShape(QFrame.StyledPanel)
		self.frame_66.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_54 = QHBoxLayout(self.frame_66)
		self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
		self.label_39 = QLabel(self.frame_66)
		self.label_39.setObjectName(u"label_39")
		self.label_39.setMinimumSize(QSize(0, 24))
		self.label_39.setFont(font2)
		self.label_39.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_54.addWidget(self.label_39)

		self.label_40 = QLabel(self.frame_66)
		self.label_40.setObjectName(u"label_40")
		self.label_40.setMinimumSize(QSize(0, 24))
		self.label_40.setMaximumSize(QSize(160, 16777215))
		self.label_40.setFont(font2)
		self.label_40.setStyleSheet(u"color: #3A4B5E")
		self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_54.addWidget(self.label_40)

		self.verticalLayout_71.addWidget(self.frame_66)

		self.frame_61 = QFrame(self.scrollAreaWidgetContents_2)
		self.frame_61.setObjectName(u"frame_61")
		self.frame_61.setMinimumSize(QSize(0, 40))
		self.frame_61.setFrameShape(QFrame.StyledPanel)
		self.frame_61.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_55 = QHBoxLayout(self.frame_61)
		self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
		self.label_41 = QLabel(self.frame_61)
		self.label_41.setObjectName(u"label_41")
		self.label_41.setMinimumSize(QSize(0, 24))
		self.label_41.setFont(font2)
		self.label_41.setStyleSheet(u"color: #3A4B5E")

		self.horizontalLayout_55.addWidget(self.label_41)

		self.label_42 = QLabel(self.frame_61)
		self.label_42.setObjectName(u"label_42")
		self.label_42.setMinimumSize(QSize(0, 24))
		self.label_42.setMaximumSize(QSize(160, 16777215))
		self.label_42.setFont(font2)
		self.label_42.setStyleSheet(u"color: #3A4B5E")
		self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_55.addWidget(self.label_42)

		self.verticalLayout_71.addWidget(self.frame_61)

		self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

		self.verticalLayout_77.addWidget(self.scrollArea_2)

		self.pagFinanceiro.addWidget(self.tabela_entrada_saida)

		self.horizontalLayout_42.addWidget(self.pagFinanceiro)

		self.verticalLayout_70.addWidget(self.frame_48)

		self.verticalLayout_69.addWidget(self.meio_financeiro_2)

		self.verticalLayout_67.addWidget(self.meio_financeiro)

		self.inferior_financeiro = QFrame(self.main_financeiro)
		self.inferior_financeiro.setObjectName(u"inferior_financeiro")
		self.inferior_financeiro.setMinimumSize(QSize(0, 156))
		self.inferior_financeiro.setMaximumSize(QSize(16777215, 156))
		self.inferior_financeiro.setFont(font20)
		self.inferior_financeiro.setFrameShape(QFrame.StyledPanel)
		self.inferior_financeiro.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_26 = QHBoxLayout(self.inferior_financeiro)
		self.horizontalLayout_26.setSpacing(0)
		self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
		self.horizontalLayout_26.setContentsMargins(32, 0, 32, 0)
		self.inferior_financeiro_2 = QFrame(self.inferior_financeiro)
		self.inferior_financeiro_2.setObjectName(u"inferior_financeiro_2")
		self.inferior_financeiro_2.setMinimumSize(QSize(0, 156))
		self.inferior_financeiro_2.setMaximumSize(QSize(1028, 156))
		self.inferior_financeiro_2.setFont(font20)
		self.inferior_financeiro_2.setFrameShape(QFrame.StyledPanel)
		self.inferior_financeiro_2.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_36 = QHBoxLayout(self.inferior_financeiro_2)
		self.horizontalLayout_36.setSpacing(24)
		self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
		self.horizontalLayout_36.setContentsMargins(16, 0, 24, 48)
		self.btn_fechar_caixa = QPushButton(self.inferior_financeiro_2)
		self.btn_fechar_caixa.setObjectName(u"btn_fechar_caixa")
		self.btn_fechar_caixa.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_fechar_caixa.setMinimumSize(QSize(180, 50))
		font23 = QFont()
		font23.setPointSize(19)
		font23.setBold(True)
		self.btn_fechar_caixa.setFont(font23)
		self.btn_fechar_caixa.setStyleSheet(u"QPushButton:hover{background: #4E647E; color: #fff}\n"
		"QPushButton{background-color: #fff; color: #4E647E;  border-radius: 22px; border: 2px solid #4E647E}")

		self.horizontalLayout_36.addWidget(self.btn_fechar_caixa)

		self.btn_exportar_pdf = QPushButton(self.inferior_financeiro_2)
		self.btn_exportar_pdf.setObjectName(u"btn_exportar_pdf")
		self.btn_exportar_pdf.setMinimumSize(QSize(160, 50))
		self.btn_exportar_pdf.setFont(font20)
		self.btn_exportar_pdf.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_exportar_pdf.setStyleSheet(u"QPushButton:hover{background: #AE4547; color: #fff}\n"
		"QPushButton{background-color: #fff; color: #AE4547;  border-radius: 22px; border: 2px solid #AE4547}")
		self.horizontalLayout_36.addWidget(self.btn_exportar_pdf)

		self.horizontalSpacer_23 = QSpacerItem(678, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.horizontalLayout_36.addItem(self.horizontalSpacer_23)

		self.btn_voltar_financeiro = QPushButton(self.inferior_financeiro_2)
		self.btn_voltar_financeiro.setObjectName(u"btn_voltar_financeiro")
		self.btn_voltar_financeiro.setMinimumSize(QSize(160, 50))
		self.btn_voltar_financeiro.setFont(font20)
		self.btn_voltar_financeiro.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_voltar_financeiro.setStyleSheet(u"QPushButton:hover{background: #198754;} QPushButton{background-color: #28A745; color: #fff;  border-radius: 22px;}")

		self.horizontalLayout_36.addWidget(self.btn_voltar_financeiro)

		self.horizontalLayout_26.addWidget(self.inferior_financeiro_2)

		self.verticalLayout_67.addWidget(self.inferior_financeiro)

		self.verticalLayout.addWidget(self.main_financeiro)

		self.pages.addWidget(self.financeiro)
		self.lista_entrada = QWidget()
		self.lista_entrada.setObjectName(u"lista_entrada")
		self.lista_entrada.setFont(font)
		self.verticalLayout_84 = QVBoxLayout(self.lista_entrada)
		self.verticalLayout_84.setSpacing(0)
		self.verticalLayout_84.setObjectName(u"verticalLayout_84")
		self.verticalLayout_84.setContentsMargins(56, 64, 56, 64)
		self.main_lista_entrada = QFrame(self.lista_entrada)
		self.main_lista_entrada.setObjectName(u"main_lista_entrada")
		self.main_lista_entrada.setFont(font)
		self.main_lista_entrada.setStyleSheet(u"#main_lista_entrada{background-color: #fff; border-radius:15px;}")
		self.main_lista_entrada.setFrameShape(QFrame.StyledPanel)
		self.main_lista_entrada.setFrameShadow(QFrame.Raised)
		self.verticalLayout_81 = QVBoxLayout(self.main_lista_entrada)
		self.verticalLayout_81.setSpacing(0)
		self.verticalLayout_81.setObjectName(u"verticalLayout_81")
		self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
		self.superior_lista_entrada = QFrame(self.main_lista_entrada)
		self.superior_lista_entrada.setObjectName(u"superior_lista_entrada")
		self.superior_lista_entrada.setMaximumSize(QSize(16777215, 105))
		self.superior_lista_entrada.setFont(font15)
		self.superior_lista_entrada.setFrameShape(QFrame.StyledPanel)
		self.superior_lista_entrada.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_40 = QHBoxLayout(self.superior_lista_entrada)
		self.horizontalLayout_40.setSpacing(0)
		self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
		self.horizontalLayout_40.setContentsMargins(0, 40, 40, 0)
		self.label_32 = QLabel(self.superior_lista_entrada)
		self.label_32.setObjectName(u"label_32")
		self.label_32.setMaximumSize(QSize(16777215, 16777215))
		self.label_32.setFont(font15)
		self.label_32.setStyleSheet(u"color: #3A4B5E")
		self.label_32.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_40.addWidget(self.label_32)

		self.comboBox_lista_entrada = QComboBox(self.superior_lista_entrada)
		self.comboBox_lista_entrada.addItem("")
		self.comboBox_lista_entrada.addItem("")
		self.comboBox_lista_entrada.setObjectName(u"comboBox_lista_entrada")
		self.comboBox_lista_entrada.setMinimumSize(QSize(0, 0))
		self.comboBox_lista_entrada.setMaximumSize(QSize(160, 38))
		self.comboBox_lista_entrada.setFont(font14)
		self.comboBox_lista_entrada.setStyleSheet(u'''QComboBox:hover{border-color:#28A745;}
		QComboBox:focus{border-color:#28A745;}                                        
		QComboBox:drop-down:hover{background-color:#eeeeee}
		QComboBox:drop-down{width: 24px; border-top-right-radius:12px; border-bottom-right-radius:12px; border-top-left-radius:1px; border-bottom-left-radius:1px;}
		QComboBox:down-arrow{image: url(icons/expand_more_blue_18dp.svg); width: 18px; height: 18px;}
		QComboBox{padding-left:8px; color: #848484; border-radius: 12px; border-width: 1px; border-style: solid; border-color:#c4c4c4;}''')

		self.comboBox_lista_entrada.setCursor(QCursor(Qt.PointingHandCursor))
		self.horizontalLayout_40.addWidget(self.comboBox_lista_entrada)

		self.verticalLayout_81.addWidget(self.superior_lista_entrada)

		self.meio_lista_entrada = QFrame(self.main_lista_entrada)
		self.meio_lista_entrada.setObjectName(u"meio_lista_entrada")
		self.meio_lista_entrada.setMinimumSize(QSize(0, 660))
		self.meio_lista_entrada.setFont(font)
		self.meio_lista_entrada.setFrameShape(QFrame.StyledPanel)
		self.meio_lista_entrada.setFrameShadow(QFrame.Raised)
		self.verticalLayout_82 = QVBoxLayout(self.meio_lista_entrada)
		self.verticalLayout_82.setSpacing(0)
		self.verticalLayout_82.setObjectName(u"verticalLayout_82")
		self.verticalLayout_82.setContentsMargins(40, 0, 40, 48)
		self.meio_lista_entrada_2 = QFrame(self.meio_lista_entrada)
		self.meio_lista_entrada_2.setObjectName(u"meio_lista_entrada_2")
		self.meio_lista_entrada_2.setStyleSheet("background-color:#fff; border:hidden")
		self.meio_lista_entrada_2.setMinimumSize(QSize(0, 0))
		self.meio_lista_entrada_2.setMaximumSize(QSize(16777215, 0))
		self.meio_lista_entrada_2.setFont(font)
		self.meio_lista_entrada_2.setFrameShape(QFrame.StyledPanel)
		self.meio_lista_entrada_2.setFrameShadow(QFrame.Raised)
		self.verticalLayout_83 = QVBoxLayout(self.meio_lista_entrada_2)
		self.verticalLayout_83.setSpacing(0)
		self.verticalLayout_83.setObjectName(u"verticalLayout_83")
		self.verticalLayout_83.setContentsMargins(0, 80, 0, 0)
		self.tableWidget_lista_entrada = QTableWidget(self.meio_lista_entrada_2)

		if (self.tableWidget_lista_entrada.columnCount() < 11):
			self.tableWidget_lista_entrada.setColumnCount(11)

		__qtablewidgetitem98 = QTableWidgetItem()
		__qtablewidgetitem98.setFont(font16);
		__qtablewidgetitem98.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_entrada.setHorizontalHeaderItem(0, __qtablewidgetitem98)
		__qtablewidgetitem18 = QTableWidgetItem()
		__qtablewidgetitem18.setFont(font16);
		__qtablewidgetitem18.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_entrada.setHorizontalHeaderItem(1, __qtablewidgetitem18)
		__qtablewidgetitem19 = QTableWidgetItem()
		__qtablewidgetitem19.setFont(font16);
		__qtablewidgetitem19.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_entrada.setHorizontalHeaderItem(2, __qtablewidgetitem19)
		__qtablewidgetitem20 = QTableWidgetItem()
		__qtablewidgetitem20.setFont(font16);
		__qtablewidgetitem20.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_entrada.setHorizontalHeaderItem(3, __qtablewidgetitem20)
		__qtablewidgetitem21 = QTableWidgetItem()
		__qtablewidgetitem21.setFont(font16);
		__qtablewidgetitem21.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_entrada.setHorizontalHeaderItem(4, __qtablewidgetitem21)
		__qtablewidgetitem22 = QTableWidgetItem()
		__qtablewidgetitem22.setFont(font16);
		__qtablewidgetitem22.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_entrada.setHorizontalHeaderItem(5, __qtablewidgetitem22)
		__qtablewidgetitem23 = QTableWidgetItem()
		__qtablewidgetitem23.setFont(font16);
		__qtablewidgetitem23.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_entrada.setHorizontalHeaderItem(6, __qtablewidgetitem23)
		__qtablewidgetitem24 = QTableWidgetItem()
		__qtablewidgetitem24.setFont(font16);
		__qtablewidgetitem24.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_entrada.setHorizontalHeaderItem(7, __qtablewidgetitem24)
		__qtablewidgetitem25 = QTableWidgetItem()
		__qtablewidgetitem25.setFont(font16);
		__qtablewidgetitem25.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_entrada.setHorizontalHeaderItem(8, __qtablewidgetitem25)
		__qtablewidgetitem26 = QTableWidgetItem()
		__qtablewidgetitem26.setFont(font16);
		__qtablewidgetitem26.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_entrada.setHorizontalHeaderItem(9, __qtablewidgetitem26)
		__qtablewidgetitem27 = QTableWidgetItem()
		__qtablewidgetitem27.setFont(font16);
		__qtablewidgetitem27.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_entrada.setHorizontalHeaderItem(10, __qtablewidgetitem27)
		self.tableWidget_lista_entrada.setObjectName(u"tableWidget_lista_entrada")
		self.tableWidget_lista_entrada.setFont(font2)
		self.tableWidget_lista_entrada.setStyleSheet(u"QTableView{color: #3A4B5E; border:hidden} QTableView::item:focus{outline:0}")
		self.tableWidget_lista_entrada.setFocusPolicy(Qt.ClickFocus)
		self.tableWidget_lista_entrada.horizontalHeader().setStyleSheet(u"QHeaderView::Section:first{padding-left: 62px} QHeaderView::Section{padding-bottom: 24px; background-color: #fff; border:hidden}")
		self.tableWidget_lista_entrada.setSelectionMode(QAbstractItemView.SingleSelection)
		self.tableWidget_lista_entrada.setEditTriggers(QAbstractItemView.SelectedClicked|QAbstractItemView.AnyKeyPressed)
		self.tableWidget_lista_entrada.horizontalHeader().setHighlightSections(False)
		self.tableWidget_lista_entrada.setAlternatingRowColors(True)
		self.tableWidget_lista_entrada.setShowGrid(False)
		self.tableWidget_lista_entrada.setSortingEnabled(False)
		self.tableWidget_lista_entrada.horizontalHeader().setCascadingSectionResizes(False)
		self.tableWidget_lista_entrada.horizontalHeader().setStretchLastSection(False)
		self.tableWidget_lista_entrada.verticalHeader().setVisible(True)
		self.tableWidget_lista_entrada.verticalHeader().setStretchLastSection(False)

		self.verticalLayout_83.addWidget(self.tableWidget_lista_entrada)


		self.verticalLayout_82.addWidget(self.meio_lista_entrada_2)


		self.verticalLayout_81.addWidget(self.meio_lista_entrada)


		self.verticalLayout_84.addWidget(self.main_lista_entrada)

		self.pages.addWidget(self.lista_entrada)
		self.lista_saida = QWidget()
		self.lista_saida.setObjectName(u"lista_saida")
		self.lista_saida.setFont(font)
		self.verticalLayout_88 = QVBoxLayout(self.lista_saida)
		self.verticalLayout_88.setSpacing(0)
		self.verticalLayout_88.setObjectName(u"verticalLayout_88")
		self.verticalLayout_88.setContentsMargins(56, 64, 56, 64)
		self.main_lista_saida = QFrame(self.lista_saida)
		self.main_lista_saida.setObjectName(u"main_lista_saida")
		self.main_lista_saida.setFont(font)
		self.main_lista_saida.setStyleSheet(u"#main_lista_saida{background-color: #fff; border-radius:15px;}")
		self.main_lista_saida.setFrameShape(QFrame.StyledPanel)
		self.main_lista_saida.setFrameShadow(QFrame.Raised)
		self.verticalLayout_85 = QVBoxLayout(self.main_lista_saida)
		self.verticalLayout_85.setSpacing(0)
		self.verticalLayout_85.setObjectName(u"verticalLayout_85")
		self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
		self.superior_lista_saida = QFrame(self.main_lista_saida)
		self.superior_lista_saida.setObjectName(u"superior_lista_saida")
		self.superior_lista_saida.setMaximumSize(QSize(16777215, 105))
		self.superior_lista_saida.setFont(font15)
		self.superior_lista_saida.setFrameShape(QFrame.StyledPanel)
		self.superior_lista_saida.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_41 = QHBoxLayout(self.superior_lista_saida)
		self.horizontalLayout_41.setSpacing(0)
		self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
		self.horizontalLayout_41.setContentsMargins(0, 40, 24, 0)
		self.label_43 = QLabel(self.superior_lista_saida)
		self.label_43.setObjectName(u"label_43")
		self.label_43.setMaximumSize(QSize(16777215, 16777215))
		self.label_43.setFont(font15)
		self.label_43.setStyleSheet(u"color: #3A4B5E")
		self.label_43.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_41.addWidget(self.label_43)

		self.comboBox_lista_saida = QComboBox(self.superior_lista_saida)
		self.comboBox_lista_saida.addItem("")
		self.comboBox_lista_saida.addItem("")
		self.comboBox_lista_saida.setObjectName(u"comboBox_lista_saida")
		self.comboBox_lista_saida.setMinimumSize(QSize(0, 0))
		self.comboBox_lista_saida.setMaximumSize(QSize(160, 38))
		self.comboBox_lista_saida.setFont(font14)
		self.comboBox_lista_saida.setStyleSheet(u'''QComboBox:hover{border-color:#28A745;}
		QComboBox:focus{border-color:#28A745;}                                        
		QComboBox:drop-down:hover{background-color:#eeeeee}
		QComboBox:drop-down{width: 24px; border-top-right-radius:12px; border-bottom-right-radius:12px; border-top-left-radius:1px; border-bottom-left-radius:1px;}
		QComboBox:down-arrow{image: url(icons/expand_more_blue_18dp.svg); width: 18px; height: 18px;}
		QComboBox{padding-left:8px; color: #848484; border-radius: 12px; border-width: 1px; border-style: solid; border-color:#c4c4c4;}''')

		self.comboBox_lista_saida.setCursor(QCursor(Qt.PointingHandCursor))
		self.horizontalLayout_41.addWidget(self.comboBox_lista_saida)


		self.verticalLayout_85.addWidget(self.superior_lista_saida)

		self.meio_lista_saida = QFrame(self.main_lista_saida)
		self.meio_lista_saida.setObjectName(u"meio_lista_saida")
		self.meio_lista_saida.setMinimumSize(QSize(0, 660))
		self.meio_lista_saida.setFont(font)
		self.meio_lista_saida.setFrameShape(QFrame.StyledPanel)
		self.meio_lista_saida.setFrameShadow(QFrame.Raised)
		self.verticalLayout_86 = QVBoxLayout(self.meio_lista_saida)
		self.verticalLayout_86.setSpacing(0)
		self.verticalLayout_86.setObjectName(u"verticalLayout_86")
		self.verticalLayout_86.setContentsMargins(40, 0, 40, 48)
		self.meio_lista_saida_2 = QFrame(self.meio_lista_saida)
		self.meio_lista_saida_2.setObjectName(u"meio_lista_saida_2")
		self.meio_lista_saida_2.setStyleSheet("background-color:#fff; border:hidden")
		self.meio_lista_saida_2.setMinimumSize(QSize(0, 0))
		self.meio_lista_saida_2.setMaximumSize(QSize(16777215, 0))
		self.meio_lista_saida_2.setFont(font)
		self.meio_lista_saida_2.setFrameShape(QFrame.StyledPanel)
		self.meio_lista_saida_2.setFrameShadow(QFrame.Raised)
		self.verticalLayout_87 = QVBoxLayout(self.meio_lista_saida_2)
		self.verticalLayout_87.setSpacing(0)
		self.verticalLayout_87.setObjectName(u"verticalLayout_87")
		self.verticalLayout_87.setContentsMargins(0, 80, 0, 0)

		self.tableWidget_lista_saida = QTableWidget(self.meio_lista_saida_2)
		if (self.tableWidget_lista_saida.columnCount() < 4):
			self.tableWidget_lista_saida.setColumnCount(4)

		__qtablewidgetitem28 = QTableWidgetItem()
		__qtablewidgetitem28.setFont(font16);
		__qtablewidgetitem28.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_saida.setHorizontalHeaderItem(0, __qtablewidgetitem28)
		__qtablewidgetitem29 = QTableWidgetItem()
		__qtablewidgetitem29.setFont(font16);
		__qtablewidgetitem29.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_saida.setHorizontalHeaderItem(1, __qtablewidgetitem29)
		__qtablewidgetitem30 = QTableWidgetItem()
		__qtablewidgetitem30.setFont(font16);
		__qtablewidgetitem30.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_saida.setHorizontalHeaderItem(2, __qtablewidgetitem30)
		__qtablewidgetitem31 = QTableWidgetItem()
		__qtablewidgetitem31.setFont(font16);
		__qtablewidgetitem31.setForeground(QColor('#3A4B5E'))
		self.tableWidget_lista_saida.setHorizontalHeaderItem(3, __qtablewidgetitem31)
		self.tableWidget_lista_saida.setObjectName(u"tableWidget_lista_saida")
		self.tableWidget_lista_saida.setFont(font2)
		self.tableWidget_lista_saida.setStyleSheet(u"QTableView{color: #3A4B5E; border:hidden} QTableView::item:focus{outline:0}")
		self.tableWidget_lista_saida.setFocusPolicy(Qt.ClickFocus)
		self.tableWidget_lista_saida.horizontalHeader().setStyleSheet(u"QHeaderView::Section{padding-bottom: 24px; background-color: #fff; border:hidden}")
		self.tableWidget_lista_saida.setEditTriggers(QAbstractItemView.SelectedClicked|QAbstractItemView.AnyKeyPressed)
		self.tableWidget_lista_saida.setSelectionMode(QAbstractItemView.SingleSelection)
		self.tableWidget_lista_saida.horizontalHeader().setHighlightSections(False)
		self.tableWidget_lista_saida.setAlternatingRowColors(True)
		self.tableWidget_lista_saida.setShowGrid(False)
		self.tableWidget_lista_saida.setSortingEnabled(False)
		self.tableWidget_lista_saida.horizontalHeader().setCascadingSectionResizes(False)
		self.tableWidget_lista_saida.horizontalHeader().setStretchLastSection(False)
		self.tableWidget_lista_saida.verticalHeader().setVisible(True)
		self.tableWidget_lista_saida.verticalHeader().setStretchLastSection(False)
		self.verticalLayout_87.addWidget(self.tableWidget_lista_saida)


		self.verticalLayout_86.addWidget(self.meio_lista_saida_2)


		self.verticalLayout_85.addWidget(self.meio_lista_saida)


		self.verticalLayout_88.addWidget(self.main_lista_saida)

		self.pages.addWidget(self.lista_saida)

		self.verticalLayout_55.addWidget(self.pages, 0, Qt.AlignHCenter)

		self.scrollArea.setWidget(self.scrollAreaWidgetContents)

		self.horizontalLayout.addWidget(self.scrollArea)

		self.background_main = QFrame(self.body)
		self.background_main.setObjectName(u"background_main")
		sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.background_main.sizePolicy().hasHeightForWidth())
		self.background_main.setSizePolicy(sizePolicy1)
		self.background_main.setFont(font)
		self.background_main.setStyleSheet(u"background-color: #EFF4F4")
		self.background_main.setFrameShape(QFrame.StyledPanel)
		self.background_main.setFrameShadow(QFrame.Raised)
		self.verticalLayout_4 = QVBoxLayout(self.background_main)
		self.verticalLayout_4.setSpacing(0)
		self.verticalLayout_4.setObjectName(u"verticalLayout_4")
		self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

		self.horizontalLayout.addWidget(self.background_main)

		self.verticalLayout_31.addWidget(self.body)

		self.inicio.addWidget(self.main)

		self.verticalLayout_74.addWidget(self.inicio)

		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)

		self.inicio.setCurrentIndex(0)
		self.pushButton_entrar.setDefault(True)
		self.pages.setCurrentIndex(0)
		self.pagFinanceiro.setCurrentIndex(0)

		QMetaObject.connectSlotsByName(MainWindow)
		# setupUi

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tesouraria IBANJE", None))
		self.frame_18.setStyleSheet(QCoreApplication.translate("MainWindow", u"border-radius: 22px", None))
		self.label_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
		#if QT_CONFIG(statustip)
		self.lineEdit_email_login.setStatusTip("")
		#endif // QT_CONFIG(statustip)
		#if QT_CONFIG(whatsthis)
		self.lineEdit_email_login.setWhatsThis("")
		#endif // QT_CONFIG(whatsthis)
		self.lineEdit_email_login.setInputMask("")
		self.lineEdit_email_login.setText("")
		self.lineEdit_email_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
		self.lineEdit_senha_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
		self.label_avisos.setText("")
		self.pushButton_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
		self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"icons/church_black_192dp.svg\"/></p></body></html>", None))
		self.label_6.setText(QCoreApplication.translate("MainWindow", u"TESOURARIA", None))
		self.label_7.setText(QCoreApplication.translate("MainWindow", u"IBANJE", None))
		self.label.setText(QCoreApplication.translate("MainWindow", u"IGREJA BASTISTA NOVA JERUSAL\u00c9M", None))
		self.pushButton_sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
		self.pushButton_home.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
		self.pushButton_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
		self.pushButton_membros.setText(QCoreApplication.translate("MainWindow", u"Membros", None))
		self.pushButton_entradas.setText(QCoreApplication.translate("MainWindow", u"Entradas", None))
		self.pushButton_saidas.setText(QCoreApplication.translate("MainWindow", u"Sa\u00eddas", None))
		self.pushButton_financeiro.setText(QCoreApplication.translate("MainWindow", u"Financeiro", None))
		self.label_dizimo.setText(QCoreApplication.translate("MainWindow", u"D\u00edzimo", None))
		self.label_10.setText(QCoreApplication.translate("MainWindow", u"0%", None))
		self.label_11.setText(QCoreApplication.translate("MainWindow", u"dos membros contribuiram", None))
		self.label_12.setText(QCoreApplication.translate("MainWindow", u"nos \u00faltimos seis meses.", None))
		self.label_oferta.setText(QCoreApplication.translate("MainWindow", u"Oferta", None))
		self.label_13.setText(QCoreApplication.translate("MainWindow", u"0%", None))
		self.label_14.setText(QCoreApplication.translate("MainWindow", u"dos membros contribuiram", None))
		self.label_15.setText(QCoreApplication.translate("MainWindow", u"nos \u00faltimos seis meses.", None))
		self.label_9.setText(QCoreApplication.translate("MainWindow", u"                      Membros", None))
		self.lineEdit_busca_membro.setText("")
		self.lineEdit_busca_membro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
		self.toolButton_busca_membro.setText("")
		___qtablewidgetitem99 = self.tableWidget_membros.horizontalHeaderItem(0)
		___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"id", None));
		___qtablewidgetitem = self.tableWidget_membros.horizontalHeaderItem(1)
		___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
		___qtablewidgetitem1 = self.tableWidget_membros.horizontalHeaderItem(2)
		___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
		___qtablewidgetitem2 = self.tableWidget_membros.horizontalHeaderItem(3)
		___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Data Nasc", None));
		self.label_hist_nome_membro.setText(QCoreApplication.translate("MainWindow", u"Nome do Membro", None))
		___qtablewidgetitem3 = self.tableWidget_historico.horizontalHeaderItem(0)
		___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"M\u00eas", None));
		___qtablewidgetitem4 = self.tableWidget_historico.horizontalHeaderItem(1)
		___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"D\u00edzimo", None));
		___qtablewidgetitem5 = self.tableWidget_historico.horizontalHeaderItem(2)
		___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Terenos", None));
		___qtablewidgetitem6 = self.tableWidget_historico.horizontalHeaderItem(3)
		___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Miss\u00f5es", None));
		___qtablewidgetitem7 = self.tableWidget_historico.horizontalHeaderItem(4)
		___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"P.A.M", None));
		___qtablewidgetitem8 = self.tableWidget_historico.horizontalHeaderItem(5)
		___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Campanha", None));
		self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Membro", None))
		self.label_aviso_nome_cad.setText("")
		self.lineEdit_nome_cad.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Completo", None))
		self.label_aviso_data_nasc.setText("")
		self.lineEdit_data_nasc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None))
		self.label_aviso_endereco.setText("")
		self.lineEdit_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
		self.label_aviso_numero.setText("")
		self.lineEdit_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
		self.label_aviso_complemento.setText("")
		self.lineEdit_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
		self.label_aviso_bairro.setText("")
		self.lineEdit_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
		self.label_17.setText("")
		self.comboBox_uf.setItemText(0, QCoreApplication.translate("MainWindow", u"AC", None))
		self.comboBox_uf.setItemText(1, QCoreApplication.translate("MainWindow", u"AL", None))
		self.comboBox_uf.setItemText(2, QCoreApplication.translate("MainWindow", u"AM", None))
		self.comboBox_uf.setItemText(3, QCoreApplication.translate("MainWindow", u"AP", None))
		self.comboBox_uf.setItemText(4, QCoreApplication.translate("MainWindow", u"BA", None))
		self.comboBox_uf.setItemText(5, QCoreApplication.translate("MainWindow", u"CE", None))
		self.comboBox_uf.setItemText(6, QCoreApplication.translate("MainWindow", u"DF", None))
		self.comboBox_uf.setItemText(7, QCoreApplication.translate("MainWindow", u"ES", None))
		self.comboBox_uf.setItemText(8, QCoreApplication.translate("MainWindow", u"GO", None))
		self.comboBox_uf.setItemText(9, QCoreApplication.translate("MainWindow", u"MA", None))
		self.comboBox_uf.setItemText(10, QCoreApplication.translate("MainWindow", u"MT", None))
		self.comboBox_uf.setItemText(11, QCoreApplication.translate("MainWindow", u"MS", None))
		self.comboBox_uf.setItemText(12, QCoreApplication.translate("MainWindow", u"MG", None))
		self.comboBox_uf.setItemText(13, QCoreApplication.translate("MainWindow", u"PA", None))
		self.comboBox_uf.setItemText(14, QCoreApplication.translate("MainWindow", u"PB", None))
		self.comboBox_uf.setItemText(15, QCoreApplication.translate("MainWindow", u"PR", None))
		self.comboBox_uf.setItemText(16, QCoreApplication.translate("MainWindow", u"PE", None))
		self.comboBox_uf.setItemText(17, QCoreApplication.translate("MainWindow", u"PI", None))
		self.comboBox_uf.setItemText(18, QCoreApplication.translate("MainWindow", u"RJ", None))
		self.comboBox_uf.setItemText(19, QCoreApplication.translate("MainWindow", u"RN", None))
		self.comboBox_uf.setItemText(20, QCoreApplication.translate("MainWindow", u"RS", None))
		self.comboBox_uf.setItemText(21, QCoreApplication.translate("MainWindow", u"RO", None))
		self.comboBox_uf.setItemText(22, QCoreApplication.translate("MainWindow", u"RR", None))
		self.comboBox_uf.setItemText(23, QCoreApplication.translate("MainWindow", u"SC", None))
		self.comboBox_uf.setItemText(24, QCoreApplication.translate("MainWindow", u"SP", None))
		self.comboBox_uf.setItemText(25, QCoreApplication.translate("MainWindow", u"SE", None))
		self.comboBox_uf.setItemText(26, QCoreApplication.translate("MainWindow", u"TO", None))

		self.label_aviso_cidade.setText("")
		self.lineEdit_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
		self.label_aviso_cep.setText("")
		self.lineEdit_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
		self.label_aviso_email_cadastro.setText("")
		self.lineEdit_email_cadastro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
		self.label_aviso_celular.setText("")
		self.lineEdit_celular.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Celular", None))
		self.comboBox_privilegios.setItemText(0, QCoreApplication.translate("MainWindow", u"Membro", None))
		self.comboBox_privilegios.setItemText(1, QCoreApplication.translate("MainWindow", u"Diretoria", None))

		self.btn_salvar_cadastro.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
		self.label_3.setText(QCoreApplication.translate("MainWindow", u"Registro de Entrada", None))
		self.label_aviso_nome_entrada.setText("")
		self.lineEdit_nome_entrada.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Completo", None))
		self.label_aviso_data_ref_entrada.setText("")
		self.lineEdit_data_ref.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Refer\u00eancia", None))
		self.label_aviso_data_dep_entrada.setText("")
		self.lineEdit_data_dep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Dep\u00f3sito", None))
		self.label_aviso_dizimo_entrada.setText("")
		self.lineEdit_dizimo_entrada.setPlaceholderText(QCoreApplication.translate("MainWindow", u"D\u00edzimo", None))
		self.label_aviso_terenos_entrada.setText("")
		self.lineEdit_terenos_entrada.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Terenos", None))
		self.label_aviso_missoes_entrada.setText("")
		self.lineEdit_missoes_entrada.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Miss\u00f5es", None))
		self.label_aviso_pam_entrada.setText("")
		self.lineEdit_pam_entrada.setPlaceholderText(QCoreApplication.translate("MainWindow", u"P.A.M", None))
		self.label_8.setText("")
		self.comboBox_tipo_entrada.setItemText(0, QCoreApplication.translate("MainWindow", u"Transf. Banc.", None))
		self.comboBox_tipo_entrada.setItemText(1, QCoreApplication.translate("MainWindow", u"Gazofil\u00e1cio", None))

		self.btn_extra.setText(QCoreApplication.translate("MainWindow", u"Extras", None))
		self.label_aviso_campanha_nome_entrada.setText("")
		self.lineEdit_campanha_nome_entrada.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Campanha", None))
		self.label_aviso_campanha_valor_entrada.setText("")
		self.lineEdit_campanha_valor_entrada.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor", None))
		self.btn_visualizar_entrada.setText(QCoreApplication.translate("MainWindow", u"Listar", None))
		self.btn_salvar_entrada.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
		self.label_5.setText(QCoreApplication.translate("MainWindow", u"Registro de Sa\u00edda", None))
		self.label_aviso_destino_saida.setText("")
		self.lineEdit_destino_saida.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Destino", None))
		self.label_aviso_data_ref_saida.setText("")
		self.lineEdit_data_saida.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Refer\u00eancia", None))
		self.label_aviso_valor_saida.setText("")
		self.lineEdit_valor_saida.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor", None))
		self.btn_visualizar_saida.setText(QCoreApplication.translate("MainWindow", u"Listar", None))
		self.btn_salvar_saida.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
		self.label_16.setText(QCoreApplication.translate("MainWindow", u"Financeiro", None))
		self.label_18.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
		self.label_aviso_financ_data_inicio.setText("")
		self.label_aviso_financ_data_fim.setText("")
		self.label_31.setText("")
		self.comboBox_financeiro.setItemText(0, QCoreApplication.translate("MainWindow", u"Entrada", None))
		self.comboBox_financeiro.setItemText(1, QCoreApplication.translate("MainWindow", u"Sa\u00edda", None))
		self.comboBox_financeiro.setItemText(2, QCoreApplication.translate("MainWindow", u"Entrada/Sa\u00edda", None))

		self.pushButton_buscar_financeiro.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
		___qtablewidgetitem9 = self.tableWidget_entrada.horizontalHeaderItem(0)
		___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Data", None));
		___qtablewidgetitem10 = self.tableWidget_entrada.horizontalHeaderItem(1)
		___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"D\u00edzimo", None));
		___qtablewidgetitem11 = self.tableWidget_entrada.horizontalHeaderItem(2)
		___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Terenos", None));
		___qtablewidgetitem12 = self.tableWidget_entrada.horizontalHeaderItem(3)
		___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Miss\u00f5es", None));
		___qtablewidgetitem13 = self.tableWidget_entrada.horizontalHeaderItem(4)
		___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"P.A.M", None));
		___qtablewidgetitem14 = self.tableWidget_entrada.horizontalHeaderItem(5)
		___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Campanhas", None));
		self.label_20.setText(QCoreApplication.translate("MainWindow", u"Total", None))
		self.total_financeiro_saida_1.setText(QCoreApplication.translate("MainWindow", u"R$ 444,00", None))
		self.total_financeiro_saida_2.setText(QCoreApplication.translate("MainWindow", u"R$ 444,00", None))
		self.total_financeiro_saida_3.setText(QCoreApplication.translate("MainWindow", u"R$ 444,00", None))
		self.total_financeiro_saida_4.setText(QCoreApplication.translate("MainWindow", u"R$ 444,00 ", None))
		self.total_financeiro_saida_5.setText(QCoreApplication.translate("MainWindow", u"R$ 444,00", None))
		___qtablewidgetitem15 = self.tableWidget_saida.horizontalHeaderItem(0)
		___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Data", None));
		___qtablewidgetitem16 = self.tableWidget_saida.horizontalHeaderItem(1)
		___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Destino", None));
		___qtablewidgetitem17 = self.tableWidget_saida.horizontalHeaderItem(2)
		___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
		self.label_19.setText(QCoreApplication.translate("MainWindow", u"Total", None))
		self.total_financeiro_saida.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.label_45.setText(QCoreApplication.translate("MainWindow", u"Total Entrada:", None))
		self.label_46.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.label_21.setText(QCoreApplication.translate("MainWindow", u"D\u00edzimo", None))
		self.label_22.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.label_23.setText(QCoreApplication.translate("MainWindow", u"Terenos", None))
		self.label_24.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.label_25.setText(QCoreApplication.translate("MainWindow", u"Miss\u00f5es", None))
		self.label_26.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.label_27.setText(QCoreApplication.translate("MainWindow", u"P.A.M", None))
		self.label_28.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.label_29.setText(QCoreApplication.translate("MainWindow", u"Campanhas", None))
		self.label_30.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.label_33.setText(QCoreApplication.translate("MainWindow", u"Total Sa\u00edda:", None))
		self.label_34.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.label_35.setText(QCoreApplication.translate("MainWindow", u"Saldo Anterior", None))
		self.label_36.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.label_37.setText(QCoreApplication.translate("MainWindow", u"Saldo Atual", None))
		self.label_38.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.label_39.setText(QCoreApplication.translate("MainWindow", u"Caixa Igreja", None))
		self.label_40.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.label_41.setText(QCoreApplication.translate("MainWindow", u"Caixa Terenos", None))
		self.label_42.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
		self.btn_fechar_caixa.setText(QCoreApplication.translate("MainWindow", u"Fechar Caixa", None))
		self.btn_exportar_pdf.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
		self.btn_voltar_financeiro.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
		self.label_32.setText(QCoreApplication.translate("MainWindow", u"             Entradas", None))
		self.comboBox_lista_entrada.setItemText(0, QCoreApplication.translate("MainWindow", u"Ult. entradas", None))
		self.comboBox_lista_entrada.setItemText(1, QCoreApplication.translate("MainWindow", u"Entr. do m\u00eas", None))

		self.comboBox_lista_entrada.setCurrentText(QCoreApplication.translate("MainWindow", u"Ult. entradas", None))
		___qtablewidgetitem98 = self.tableWidget_lista_entrada.horizontalHeaderItem(0)
		___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"id", None));
		___qtablewidgetitem18 = self.tableWidget_lista_entrada.horizontalHeaderItem(1)
		___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
		___qtablewidgetitem18.setTextAlignment(Qt.AlignLeft)
		___qtablewidgetitem19 = self.tableWidget_lista_entrada.horizontalHeaderItem(2)
		___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Data Ref.", None));
		___qtablewidgetitem20 = self.tableWidget_lista_entrada.horizontalHeaderItem(3)
		___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Data Dep.", None));
		___qtablewidgetitem21 = self.tableWidget_lista_entrada.horizontalHeaderItem(4)
		___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"D\u00edzimo", None));
		___qtablewidgetitem22 = self.tableWidget_lista_entrada.horizontalHeaderItem(5)
		___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Terenos", None));
		___qtablewidgetitem23 = self.tableWidget_lista_entrada.horizontalHeaderItem(6)
		___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Miss\u00f5es", None));
		___qtablewidgetitem24 = self.tableWidget_lista_entrada.horizontalHeaderItem(7)
		___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"P.A.M", None));
		___qtablewidgetitem25 = self.tableWidget_lista_entrada.horizontalHeaderItem(8)
		___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Campanha", None));
		___qtablewidgetitem26 = self.tableWidget_lista_entrada.horizontalHeaderItem(9)
		___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"C. Valor", None));
		___qtablewidgetitem27 = self.tableWidget_lista_entrada.horizontalHeaderItem(10)
		___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
		self.label_43.setText(QCoreApplication.translate("MainWindow", u"                Sa\u00eddas", None))
		self.comboBox_lista_saida.setItemText(0, QCoreApplication.translate("MainWindow", u"Ult. sa\u00eddas", None))
		self.comboBox_lista_saida.setItemText(1, QCoreApplication.translate("MainWindow", u"Sa\u00eddas do m\u00eas", None))
		self.comboBox_lista_saida.setCurrentText(QCoreApplication.translate("MainWindow", u"Ult. sa\u00eddas", None))
		___qtablewidgetitem28 = self.tableWidget_lista_saida.horizontalHeaderItem(0)
		___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"id", None));
		___qtablewidgetitem29 = self.tableWidget_lista_saida.horizontalHeaderItem(1)
		___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Data", None));
		___qtablewidgetitem30 = self.tableWidget_lista_saida.horizontalHeaderItem(2)
		___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Destino", None));
		___qtablewidgetitem31 = self.tableWidget_lista_saida.horizontalHeaderItem(3)
		___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
		# retranslateUi'