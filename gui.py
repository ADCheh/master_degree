from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QLineF,QRectF
from PyQt5.QtGui import QPainter,QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 528)

        self.timer = QtCore.QTimer()
        self.clock = QtCore.QTimer()
        self.painter = QPainter()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 131, 281))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        self.groupBox.setPalette(palette)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.agents_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.agents_spinBox.setGeometry(QtCore.QRect(10, 40, 81, 22))
        self.agents_spinBox.setProperty("value", 3)
        self.agents_spinBox.setObjectName("agents_spinBox")

        self.steps_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.steps_spinBox.setGeometry(QtCore.QRect(10, 90, 81, 22))
        self.steps_spinBox.setProperty("value", 20)
        self.steps_spinBox.setObjectName("steps_spinBox")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.population_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.population_spinBox.setGeometry(QtCore.QRect(10, 190, 81, 22))
        self.population_spinBox.setMaximum(250)
        self.population_spinBox.setProperty("value", 10)
        self.population_spinBox.setObjectName("population_spinBox")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.mutation_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.mutation_doubleSpinBox.setGeometry(QtCore.QRect(10, 140, 81, 22))
        self.mutation_doubleSpinBox.setSingleStep(0.05)
        self.mutation_doubleSpinBox.setProperty("value", 2)
        self.mutation_doubleSpinBox.setObjectName("mutation_doubleSpinBox")

        self.speed_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.speed_doubleSpinBox.setGeometry(QtCore.QRect(10, 240, 81, 22))
        self.speed_doubleSpinBox.setSingleStep(0.1)
        self.speed_doubleSpinBox.setProperty("value", 0.1)
        self.speed_doubleSpinBox.setObjectName("speed_doubleSpinBox")

        #self.waiting_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        #self.waiting_checkBox.setGeometry(QtCore.QRect(20, 292, 121, 21))
        #self.waiting_checkBox.setObjectName("waiting_checkBox")

        self.obstacle_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.obstacle_checkBox.setGeometry(QtCore.QRect(20, 292, 121, 21))
        self.obstacle_checkBox.setObjectName("obstacle_checkBox")

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 342, 131, 41))
        self.startButton.setObjectName("startButton")

        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(10, 392, 131, 41))
        self.stopButton.setObjectName("stopButton")

        self.restartButton = QtWidgets.QPushButton(self.centralwidget)
        self.restartButton.setGeometry(QtCore.QRect(10, 442, 131, 41))
        self.restartButton.setObjectName("restartButton")

        self.log = QtWidgets.QTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(620, 30, 193, 453))
        self.log.setObjectName("log")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(620, -1, 191, 31))
        self.label_6.setObjectName("label_6")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(160, 30, 453, 453))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene()

        self.graphicsView.setScene(self.scene)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, -1, 191, 31))
        self.label_7.setObjectName("label_7")

        self.label_clock = QtWidgets.QLabel(self.centralwidget)
        self.label_clock.setGeometry(QtCore.QRect(160, 550, 191, 31))
        self.label_clock.setObjectName("label_clock")


        self.random_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.random_checkBox.setGeometry(QtCore.QRect(20, 312, 121, 21))
        self.random_checkBox.setObjectName("random_checkBox")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.brushes = {
            0: QtGui.QBrush(Qt.green),  # green
            1: QtGui.QBrush(Qt.red),  # red
            2: QtGui.QBrush(Qt.blue),  # blue
            3: QtGui.QBrush(Qt.yellow),  # yellow
            4: QtGui.QBrush(Qt.magenta),  # magenta
            5: QtGui.QBrush(QtGui.QColor(255,128,0)),  # orange
            6: QtGui.QBrush(QtGui.QColor(102,0,204)),  # purple
            7: QtGui.QBrush(QtGui.QColor(102,178,255)),  # lightBlue
            8: QtGui.QBrush(QtGui.QColor(255,153,204)),  # pink
            9: QtGui.QBrush(Qt.black)  # black
        }

        self.pens = {
            0: QtGui.QPen(Qt.green,2),
            1: QtGui.QPen(Qt.red,2),
            2: QtGui.QPen(Qt.blue,2),
            3: QtGui.QPen(Qt.yellow,2),
            4: QtGui.QPen(Qt.magenta,2),
            5: QtGui.QPen(QtGui.QColor(255, 128, 0),2),
            6: QtGui.QPen(QtGui.QColor(102, 0, 204),2),
            7: QtGui.QPen(QtGui.QColor(102, 178, 255),2),
            8: QtGui.QPen(QtGui.QColor(255, 153, 204),2),
            9: QtGui.QPen(Qt.black,2)
        }



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шувалов Т.А. КРМО-01-18, Бесконфликтное движение группы мобильных роботов, 2020 г."))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры алгоритма"))
        self.label.setText(_translate("MainWindow", "Количество агентов"))
        self.label_2.setText(_translate("MainWindow", "Количество шагов"))
        self.label_3.setText(_translate("MainWindow", "Величина мутации"))
        self.label_4.setText(_translate("MainWindow", "Величина популяции"))
        self.label_5.setText(_translate("MainWindow", "Скорость агентов"))
        #self.waiting_checkBox.setText(_translate("MainWindow", "Ожидание"))
        self.obstacle_checkBox.setText(_translate("MainWindow", "Препятствие"))

        self.startButton.setText(_translate("MainWindow", "Старт"))
        self.stopButton.setText(_translate("MainWindow", "Остановка"))
        self.restartButton.setText(_translate("MainWindow", "Перезапуск"))
        self.label_6.setText(_translate("MainWindow", "Текстовый журнал"))
        self.label_7.setText(_translate("MainWindow", "Графическое окно"))
        self.random_checkBox.setText(_translate("MainWindow", "Случайный финиш"))

    def show_time(self,time):
        self.label_clock.setText(str(time))

    def add_text(self,text):
        s = self.log.toPlainText()
        s += text
        self.log.setText(s)
        self.log.verticalScrollBar().setValue(self.log.verticalScrollBar().maximum())
