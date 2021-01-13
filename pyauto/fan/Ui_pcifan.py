# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1201, 775)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../PCILib/assets/PCIicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 1161, 641))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tableWidget_book = QtWidgets.QTableWidget(self.tab_10)
        self.tableWidget_book.setGeometry(QtCore.QRect(10, 20, 1131, 501))
        self.tableWidget_book.setDragEnabled(False)
        self.tableWidget_book.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_book.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_book.setObjectName("tableWidget_book")
        self.tableWidget_book.setColumnCount(8)
        self.tableWidget_book.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_book.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_book.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_book.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_book.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_book.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_book.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_book.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_book.setHorizontalHeaderItem(7, item)
        self.groupBox_1 = QtWidgets.QGroupBox(self.tab_10)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 530, 981, 71))
        self.groupBox_1.setObjectName("groupBox_1")
        self.bookButton_4 = QtWidgets.QPushButton(self.groupBox_1)
        self.bookButton_4.setGeometry(QtCore.QRect(370, 20, 101, 28))
        self.bookButton_4.setObjectName("bookButton_4")
        self.bookButton_2 = QtWidgets.QPushButton(self.groupBox_1)
        self.bookButton_2.setGeometry(QtCore.QRect(130, 20, 101, 28))
        self.bookButton_2.setObjectName("bookButton_2")
        self.bookButton_3 = QtWidgets.QPushButton(self.groupBox_1)
        self.bookButton_3.setGeometry(QtCore.QRect(250, 20, 101, 28))
        self.bookButton_3.setObjectName("bookButton_3")
        self.bookButton_1 = QtWidgets.QPushButton(self.groupBox_1)
        self.bookButton_1.setGeometry(QtCore.QRect(10, 20, 101, 28))
        self.bookButton_1.setObjectName("bookButton_1")
        self.lineEdit_book_1 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_book_1.setGeometry(QtCore.QRect(510, 20, 191, 24))
        self.lineEdit_book_1.setObjectName("lineEdit_book_1")
        self.magnetButton_1 = QtWidgets.QPushButton(self.groupBox_1)
        self.magnetButton_1.setGeometry(QtCore.QRect(720, 20, 181, 28))
        self.magnetButton_1.setObjectName("magnetButton_1")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tableWidget_reader = QtWidgets.QTableWidget(self.tab_11)
        self.tableWidget_reader.setGeometry(QtCore.QRect(10, 20, 1131, 501))
        self.tableWidget_reader.setDragEnabled(False)
        self.tableWidget_reader.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_reader.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_reader.setObjectName("tableWidget_reader")
        self.tableWidget_reader.setColumnCount(6)
        self.tableWidget_reader.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reader.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reader.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reader.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reader.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reader.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_reader.setHorizontalHeaderItem(5, item)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_11)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 530, 1111, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.readerButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.readerButton_4.setGeometry(QtCore.QRect(370, 20, 101, 28))
        self.readerButton_4.setObjectName("readerButton_4")
        self.readerButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.readerButton_3.setGeometry(QtCore.QRect(250, 20, 101, 28))
        self.readerButton_3.setObjectName("readerButton_3")
        self.readerButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.readerButton_2.setGeometry(QtCore.QRect(130, 20, 101, 28))
        self.readerButton_2.setObjectName("readerButton_2")
        self.readerButton_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.readerButton_1.setGeometry(QtCore.QRect(10, 20, 101, 28))
        self.readerButton_1.setObjectName("readerButton_1")
        self.lineEdit_reader_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_reader_1.setGeometry(QtCore.QRect(490, 20, 191, 24))
        self.lineEdit_reader_1.setObjectName("lineEdit_reader_1")
        self.lineEdit_reader_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_reader_2.setEnabled(False)
        self.lineEdit_reader_2.setGeometry(QtCore.QRect(700, 20, 191, 24))
        self.lineEdit_reader_2.setObjectName("lineEdit_reader_2")
        self.lineEdit_reader_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_reader_3.setEnabled(False)
        self.lineEdit_reader_3.setGeometry(QtCore.QRect(910, 20, 191, 24))
        self.lineEdit_reader_3.setObjectName("lineEdit_reader_3")
        self.tabWidget.addTab(self.tab_11, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 30, 391, 16))
        self.label_3.setObjectName("label_3")
        self.label_hint_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_hint_1.setGeometry(QtCore.QRect(610, 30, 391, 16))
        self.label_hint_1.setObjectName("label_hint_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 26))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        self.menu_V = QtWidgets.QMenu(self.menubar)
        self.menu_V.setObjectName("menu_V")
        self.menu = QtWidgets.QMenu(self.menu_V)
        self.menu.setObjectName("menu")
        self.menu_A = QtWidgets.QMenu(self.menubar)
        self.menu_A.setObjectName("menu_A")
        self.menu_B = QtWidgets.QMenu(self.menubar)
        self.menu_B.setObjectName("menu_B")
        self.menu_R = QtWidgets.QMenu(self.menubar)
        self.menu_R.setObjectName("menu_R")
        self.menu_T = QtWidgets.QMenu(self.menubar)
        self.menu_T.setObjectName("menu_T")
        self.menu_W = QtWidgets.QMenu(self.menubar)
        self.menu_W.setObjectName("menu_W")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_N = QtWidgets.QAction(MainWindow)
        self.action_N.setObjectName("action_N")
        self.action_O = QtWidgets.QAction(MainWindow)
        self.action_O.setObjectName("action_O")
        self.action_X = QtWidgets.QAction(MainWindow)
        self.action_X.setObjectName("action_X")
        self.action_A = QtWidgets.QAction(MainWindow)
        self.action_A.setObjectName("action_A")
        self.action_H = QtWidgets.QAction(MainWindow)
        self.action_H.setObjectName("action_H")
        self.actionFullScreen = QtWidgets.QAction(MainWindow)
        self.actionFullScreen.setObjectName("actionFullScreen")
        self.actionZen_Mode = QtWidgets.QAction(MainWindow)
        self.actionZen_Mode.setObjectName("actionZen_Mode")
        self.actionPCI_tools_set = QtWidgets.QAction(MainWindow)
        self.actionPCI_tools_set.setObjectName("actionPCI_tools_set")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionDebug_D = QtWidgets.QAction(MainWindow)
        self.actionDebug_D.setObjectName("actionDebug_D")
        self.actionRun_R = QtWidgets.QAction(MainWindow)
        self.actionRun_R.setObjectName("actionRun_R")
        self.actionBuild_B = QtWidgets.QAction(MainWindow)
        self.actionBuild_B.setObjectName("actionBuild_B")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.action_Delete = QtWidgets.QAction(MainWindow)
        self.action_Delete.setObjectName("action_Delete")
        self.action_Select_all = QtWidgets.QAction(MainWindow)
        self.action_Select_all.setObjectName("action_Select_all")
        self.action_Find = QtWidgets.QAction(MainWindow)
        self.action_Find.setObjectName("action_Find")
        self.action_Replace = QtWidgets.QAction(MainWindow)
        self.action_Replace.setObjectName("action_Replace")
        self.actionSLayout = QtWidgets.QAction(MainWindow)
        self.actionSLayout.setObjectName("actionSLayout")
        self.actionLLayout = QtWidgets.QAction(MainWindow)
        self.actionLLayout.setObjectName("actionLLayout")
        self.actionNotice = QtWidgets.QAction(MainWindow)
        self.actionNotice.setObjectName("actionNotice")
        self.actionLayoutWH = QtWidgets.QAction(MainWindow)
        self.actionLayoutWH.setObjectName("actionLayoutWH")
        self.menu_F.addAction(self.action_N)
        self.menu_F.addAction(self.action_O)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.action_X)
        self.menu_E.addAction(self.actionUndo)
        self.menu_E.addAction(self.actionRedo)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.actionCut)
        self.menu_E.addAction(self.actionCopy)
        self.menu_E.addAction(self.actionPaste)
        self.menu_E.addAction(self.action_Delete)
        self.menu_E.addAction(self.action_Select_all)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.action_Find)
        self.menu_E.addAction(self.action_Replace)
        self.menu.addAction(self.actionFullScreen)
        self.menu.addAction(self.actionZen_Mode)
        self.menu_V.addAction(self.menu.menuAction())
        self.menu_B.addAction(self.actionBuild_B)
        self.menu_R.addAction(self.actionDebug_D)
        self.menu_R.addAction(self.actionRun_R)
        self.menu_T.addAction(self.actionPCI_tools_set)
        self.menu_W.addAction(self.actionSLayout)
        self.menu_W.addAction(self.actionLLayout)
        self.menu_W.addSeparator()
        self.menu_W.addAction(self.actionNotice)
        self.menu_W.addAction(self.actionLayoutWH)
        self.menu_H.addAction(self.action_H)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_A)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_V.menuAction())
        self.menubar.addAction(self.menu_A.menuAction())
        self.menubar.addAction(self.menu_B.menuAction())
        self.menubar.addAction(self.menu_R.menuAction())
        self.menubar.addAction(self.menu_T.menuAction())
        self.menubar.addAction(self.menu_W.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome to PCI"))
        self.tableWidget_book.setSortingEnabled(True)
        item = self.tableWidget_book.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_book.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "名称"))
        item = self.tableWidget_book.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ISBN"))
        item = self.tableWidget_book.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "出版社"))
        item = self.tableWidget_book.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "出版年月"))
        item = self.tableWidget_book.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "作者"))
        item = self.tableWidget_book.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "标签"))
        item = self.tableWidget_book.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "库存"))
        self.groupBox_1.setTitle(_translate("MainWindow", "操作"))
        self.bookButton_4.setText(_translate("MainWindow", "导出信息"))
        self.bookButton_2.setText(_translate("MainWindow", "增加信息"))
        self.bookButton_3.setText(_translate("MainWindow", "删除信息"))
        self.bookButton_1.setText(_translate("MainWindow", "导入信息"))
        self.lineEdit_book_1.setPlaceholderText(_translate("MainWindow", "查询格式(column:regex)"))
        self.magnetButton_1.setText(_translate("MainWindow", "导出选中的磁力链接"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "番剧信息"))
        self.tableWidget_reader.setSortingEnabled(True)
        item = self.tableWidget_reader.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_reader.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "名称"))
        item = self.tableWidget_reader.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "类型"))
        item = self.tableWidget_reader.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "联系电话"))
        item = self.tableWidget_reader.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "在借图书"))
        item = self.tableWidget_reader.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "借阅历史"))
        self.groupBox_2.setTitle(_translate("MainWindow", "操作"))
        self.readerButton_4.setText(_translate("MainWindow", "导出信息"))
        self.readerButton_3.setText(_translate("MainWindow", "删除信息"))
        self.readerButton_2.setText(_translate("MainWindow", "增加信息"))
        self.readerButton_1.setText(_translate("MainWindow", "导入信息"))
        self.lineEdit_reader_1.setPlaceholderText(_translate("MainWindow", "查询格式(column:regex)"))
        self.lineEdit_reader_2.setPlaceholderText(_translate("MainWindow", "借书ID,自动确定"))
        self.lineEdit_reader_3.setPlaceholderText(_translate("MainWindow", "还书ID,自动确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "保留备用"))
        self.label.setText(_translate("MainWindow", "PCI看番神器"))
        self.label_3.setText(_translate("MainWindow", "警告:删除后将无法恢复;在查询界面修改数据将不会保存"))
        self.label_hint_1.setText(_translate("MainWindow", "提示"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_E.setTitle(_translate("MainWindow", "编辑(&E)"))
        self.menu_V.setTitle(_translate("MainWindow", "视图(&V)"))
        self.menu.setTitle(_translate("MainWindow", "外观"))
        self.menu_A.setTitle(_translate("MainWindow", "分析(&Z)"))
        self.menu_B.setTitle(_translate("MainWindow", "构建(&B)"))
        self.menu_R.setTitle(_translate("MainWindow", "运行(&R)"))
        self.menu_T.setTitle(_translate("MainWindow", "工具(&T)"))
        self.menu_W.setTitle(_translate("MainWindow", "窗口(&W)"))
        self.menu_H.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.action_N.setText(_translate("MainWindow", "新建(&N)"))
        self.action_O.setText(_translate("MainWindow", "打开(&O)"))
        self.action_X.setText(_translate("MainWindow", "退出(&X)"))
        self.action_X.setShortcut(_translate("MainWindow", "Alt+X"))
        self.action_A.setText(_translate("MainWindow", "关于(&A)"))
        self.action_H.setText(_translate("MainWindow", "帮助(&H)"))
        self.actionFullScreen.setText(_translate("MainWindow", "FullScreen"))
        self.actionFullScreen.setShortcut(_translate("MainWindow", "F11"))
        self.actionZen_Mode.setText(_translate("MainWindow", "Zen Mode"))
        self.actionPCI_tools_set.setText(_translate("MainWindow", "Tools Set"))
        self.actionUndo.setText(_translate("MainWindow", "&Undo"))
        self.actionRedo.setText(_translate("MainWindow", "&Redo"))
        self.actionDebug_D.setText(_translate("MainWindow", "Debug(&D)"))
        self.actionRun_R.setText(_translate("MainWindow", "Run(&R)"))
        self.actionBuild_B.setText(_translate("MainWindow", "Build(&B)"))
        self.actionCut.setText(_translate("MainWindow", "Cu&t"))
        self.actionCopy.setText(_translate("MainWindow", "&Copy"))
        self.actionPaste.setText(_translate("MainWindow", "&Paste"))
        self.action_Delete.setText(_translate("MainWindow", "&Delete"))
        self.action_Select_all.setText(_translate("MainWindow", "&Select all"))
        self.action_Find.setText(_translate("MainWindow", "&Find"))
        self.action_Replace.setText(_translate("MainWindow", "&Replace"))
        self.actionSLayout.setText(_translate("MainWindow", "保存当前布局"))
        self.actionLLayout.setText(_translate("MainWindow", "加载布局"))
        self.actionNotice.setText(_translate("MainWindow", "通知"))
        self.actionLayoutWH.setText(_translate("MainWindow", "显示窗口大小"))
