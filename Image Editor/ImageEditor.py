# -*- coding: utf-8 -*-

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QInputDialog, QWidget
import cv2 as cv


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.OutputImage = QtWidgets.QLabel(self.centralwidget)
        self.OutputImage.setMinimumSize(QtCore.QSize(300, 300))
        self.OutputImage.setScaledContents(True)
        self.OutputImage.setText("")
        self.OutputImage.setObjectName("OutputImage")

        self.gridLayout_4.addWidget(self.OutputImage, 1, 2, 1, 1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setMaximumSize(QtCore.QSize(1210, 50))

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignTop)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setMaximumSize(QtCore.QSize(1210, 50))

        self.gridLayout_4.addWidget(self.label_2, 0, 2, 1, 1, QtCore.Qt.AlignTop)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setMaximumSize(QtCore.QSize(50, 16777215))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")

        self.horizontalLayout.addWidget(self.verticalSlider)

        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 3, 3, 1)

        self.InputImage = QtWidgets.QLabel(self.centralwidget)
        self.InputImage.setMinimumSize(QtCore.QSize(300, 300))
        self.InputImage.setText("")
        self.InputImage.setObjectName("InputImage")
        self.InputImage.setScaledContents(True)

        self.gridLayout_4.addWidget(self.InputImage, 1, 0, 1, 1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setEnabled(True)
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.applyChanges)
        self.verticalLayout_2.addWidget(self.applyButton)

        self.gridLayout_4.addLayout(self.verticalLayout_2, 3, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setCheckable(False)
        self.actionSave.setObjectName("actionSave")

        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")

        self.actionBlur_Image = QtWidgets.QAction(MainWindow)
        self.actionBlur_Image.setObjectName("actionBlur_Image")

        self.actionGrayScale_Image = QtWidgets.QAction(MainWindow)
        self.actionGrayScale_Image.setObjectName("actionGrayScale_Image")

        self.actionCrop_Image = QtWidgets.QAction(MainWindow)
        self.actionCrop_Image.setObjectName("actionCrop_Image")

        self.actionFlip = QtWidgets.QAction(MainWindow)
        self.actionFlip.setObjectName("actionFlip")

        self.actionMirror = QtWidgets.QAction(MainWindow)
        self.actionMirror.setObjectName("actionMirror")

        self.actionRotate = QtWidgets.QAction(MainWindow)
        self.actionRotate.setObjectName("actionRotate")

        self.actionReverse_Color = QtWidgets.QAction(MainWindow)
        self.actionReverse_Color.setObjectName("actionReverse_Color")

        self.actionAdjust_Brightness = QtWidgets.QAction(MainWindow)
        self.actionAdjust_Brightness.setObjectName("actionAdjust_Brightness")

        self.actionAdjust_Contrast = QtWidgets.QAction(MainWindow)
        self.actionAdjust_Contrast.setObjectName("actionAdjust_Contrast")

        self.actionAdjust_Saturation = QtWidgets.QAction(MainWindow)
        self.actionAdjust_Saturation.setObjectName("actionAdjust_Saturation")

        self.actionAdd_Noise = QtWidgets.QAction(MainWindow)
        self.actionAdd_Noise.setObjectName("actionAdd_Noise")

        self.actionDetect_Edges = QtWidgets.QAction(MainWindow)
        self.actionDetect_Edges.setObjectName("actionDetect_Edges")

        self.actionChange_Color_Balance = QtWidgets.QAction(MainWindow)
        self.actionChange_Color_Balance.setObjectName("actionChange_Color_Balance")

        self.retranslateUi(MainWindow)

        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad)
        self.menuEdit.addAction(self.actionBlur_Image)
        self.menuEdit.addAction(self.actionGrayScale_Image)
        self.menuEdit.addAction(self.actionCrop_Image)
        self.menuEdit.addAction(self.actionFlip)
        self.menuEdit.addAction(self.actionMirror)
        self.menuEdit.addAction(self.actionRotate)
        self.menuEdit.addAction(self.actionReverse_Color)
        self.menuEdit.addAction(self.actionAdjust_Brightness)
        self.menuEdit.addAction(self.actionAdjust_Contrast)
        self.menuEdit.addAction(self.actionAdjust_Saturation)
        self.menuEdit.addAction(self.actionAdd_Noise)
        self.menuEdit.addAction(self.actionDetect_Edges)
        self.menuEdit.addAction(self.actionChange_Color_Balance)

        self.menubar.addAction(self.menuFile.menuAction())

        self.filename = None
        self.image = None
        self.modified = None
        self.redValue = 1
        self.greenValue = 1
        self.blueValue = 1

        # Calling methods for actions
        self.actionSave.triggered.connect(self.saveImage)
        self.actionLoad.triggered.connect(self.loadImage)
        self.actionBlur_Image.triggered.connect(self.connectorBlur)
        self.actionGrayScale_Image.triggered.connect(lambda: self.grayscale())
        self.actionCrop_Image.triggered.connect(lambda: self.crop())
        self.actionFlip.triggered.connect(lambda: self.flip(0))
        self.actionMirror.triggered.connect(lambda: self.flip(1))
        self.actionRotate.triggered.connect(lambda: self.rotate())
        self.actionReverse_Color.triggered.connect(lambda: self.invertColors())
        self.actionAdjust_Brightness.triggered.connect(self.connectorBrightness)
        self.actionAdjust_Contrast.triggered.connect(self.connectorContrast)
        self.actionAdjust_Saturation.triggered.connect(self.connectorSaturation)
        self.actionAdd_Noise.triggered.connect(lambda: self.addNoise(1))
        self.actionChange_Color_Balance.triggered.connect(lambda: self.changeColorBalance())
        self.actionDetect_Edges.triggered.connect(self.connectorDetectEdges)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def connectorBlur(self):
        try:
            self.verticalSlider.valueChanged['int'].disconnect()
        except Exception:
            pass
        self.verticalSlider.valueChanged['int'].connect(self.changeBlur)

    def connectorBrightness(self):
        try:
            self.verticalSlider.valueChanged['int'].disconnect()
        except Exception:
            pass
        self.verticalSlider.valueChanged['int'].connect(self.changeBrightness)

    def connectorContrast(self):
        try:
            self.verticalSlider.valueChanged['int'].disconnect()
        except Exception:
            pass
        self.verticalSlider.valueChanged['int'].connect(self.changeContrast)

    def connectorSaturation(self):
        try:
            self.verticalSlider.valueChanged['int'].disconnect()
        except Exception:
            pass
        self.verticalSlider.valueChanged['int'].connect(self.changeSaturation)

    def connectorDetectEdges(self):
        try:
            self.verticalSlider.valueChanged['int'].disconnect()
        except Exception:
            pass
        self.verticalSlider.valueChanged['int'].connect(self.detectEdges)

    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        if self.filename == "":
            return
        self.image = cv.imread(self.filename)
        self.menubar.addAction(self.menuEdit.menuAction())
        self.setInputPhoto(self.image)

    def setInputPhoto(self, image):
        self.image = image
        frame = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.InputImage.setPixmap(QtGui.QPixmap.fromImage(image))
        self.OutputImage.setPixmap(QtGui.QPixmap.fromImage(image))

    def setOutputPhoto(self, image):
        self.modified = image
        frame = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.OutputImage.setPixmap(QtGui.QPixmap.fromImage(image))

    def changeBrightness(self, value):
        if self.image.ndim < 3:
            self.showGrayscaleWarning()
            return
        imgHSV = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)
        imgHSV[:, :, 2] = cv.multiply(imgHSV[:, :, 2], (value / 50))
        newImg = cv.cvtColor(imgHSV, cv.COLOR_HSV2BGR)
        self.setOutputPhoto(newImg)

    def changeBlur(self, value):
        kernel_size = (value + 1, value + 1)
        tempImage = cv.blur(self.image, kernel_size)
        self.setOutputPhoto(tempImage)

    def applyChanges(self):
        self.image = self.modified

    def saveImage(self):
        newFilename = QFileDialog.getSaveFileName(
            filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        if newFilename == "":
            return
        cv.imwrite(newFilename, self.image)
        print("Image saved as:", newFilename)

    def showGrayscaleWarning(self):
        message = QMessageBox()
        message.setWindowTitle("Warning")
        message.setText("This is a grayscale image")
        message.setIcon(QMessageBox.Warning)
        message.exec_()

    def grayscale(self):
        if self.image.ndim < 3:
            self.showGrayscaleWarning()
            return
        self.image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        self.setOutputPhoto(self.image)

    def crop(self):
        r = cv.selectROI("select then press enter", self.image, False)
        if r != (0, 0, 0, 0):
            self.image = self.image[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
            self.setOutputPhoto(self.image)
        cv.destroyWindow('select then press enter')

    # flip number; 0: vertical, 1: horizontal, -1: both
    def flip(self, flipNumber):
        self.image = cv.flip(self.image, flipNumber)
        self.setOutputPhoto(self.image)

    def rotate(self):
        self.image = cv.rotate(self.image, cv.ROTATE_90_CLOCKWISE)
        self.setOutputPhoto(self.image)

    def invertColors(self):
        self.image = cv.bitwise_not(self.image)
        self.setOutputPhoto(self.image)

    def changeColorBalance(self):
        if self.image.ndim < 3:
            self.showGrayscaleWarning()
            return

        red, ok = QInputDialog.getDouble(self, "Write the RGB Values", "Enter Red value (Default: 1.0)")
        if ok:
            self.redValue = float(red)

        green, oke = QInputDialog.getDouble(self, "Write the RGB Values", "Enter Green value (Default: 1.0)")
        if oke:
            self.greenValue = float(green)

        blue, okey = QInputDialog.getDouble(self, "Write the RGB Values", "Enter Blue value (Default: 1.0)")
        if okey:
            self.blueValue = float(blue)

        newImg = np.copy(self.image)
        newImg[:, :, 0] = np.clip(newImg[:, :, 0] * self.blueValue, 0, 255)
        newImg[:, :, 1] = np.clip(newImg[:, :, 1] * self.greenValue, 0, 255)
        newImg[:, :, 2] = np.clip(newImg[:, :, 2] * self.redValue, 0, 255)
        self.setOutputPhoto(newImg)

    def changeSaturation(self, satModifier):
        if self.image.ndim < 3:
            self.showGrayscaleWarning()
            return
        imgHSV = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)
        imgHSV[:, :, 1] = cv.multiply(imgHSV[:, :, 1], (satModifier / 50))
        saturated = cv.cvtColor(imgHSV, cv.COLOR_HSV2BGR)
        self.setOutputPhoto(saturated)

    def addNoise(self, noiseType):
        if self.image.ndim < 3:
            self.showGrayscaleWarning()
            return
        row, col, rgb = self.image.shape
        if noiseType == 0:
            gaussianNoise = np.random.normal(0, 0.2, size=(row, col, rgb))
            self.image = self.image + gaussianNoise
            self.setOutputPhoto(self.image)
            return

        newImg = np.copy(self.image)
        saltThres = 0.05
        pepperThres = 1 - 0.05
        for i in range(row):
            for j in range(col):
                random = np.random.random()
                if random < saltThres:
                    newImg[i, j] = [255, 255, 255]
                elif random > pepperThres:
                    newImg[i, j] = [0, 0, 0]
        self.image = newImg
        self.setOutputPhoto(self.image)

    def changeContrast(self, conModifier):
        if self.image.ndim < 3:
            self.showGrayscaleWarning()
            return
        changedImage = cv.convertScaleAbs(self.image, alpha=(conModifier / 50))
        self.setOutputPhoto(changedImage)

    def detectEdges(self, value):
        edgeImg = cv.Canny(self.image, value * 2 + 50, value * 4 + 75)
        self.setOutputPhoto(edgeImg)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Editor"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:18pt;\">Output</span></p></body></html>"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:18pt;\">Input</span></p></body></html>"))
        self.applyButton.setText(_translate("MainWindow", "Apply Change"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionSave.setText(_translate("MainWindow", "Save Image"))
        self.actionLoad.setText(_translate("MainWindow", "Load Image"))
        self.actionBlur_Image.setText(_translate("MainWindow", "Blur Image"))
        self.actionGrayScale_Image.setText(_translate("MainWindow", "GrayScale Image"))
        self.actionCrop_Image.setText(_translate("MainWindow", "Crop "))
        self.actionFlip.setText(_translate("MainWindow", "Flip"))
        self.actionMirror.setText(_translate("MainWindow", "Mirror"))
        self.actionRotate.setText(_translate("MainWindow", "Rotate"))
        self.actionReverse_Color.setText(_translate("MainWindow", "Reverse Color"))
        self.actionAdjust_Brightness.setText(_translate("MainWindow", "Adjust Brightness"))
        self.actionAdjust_Contrast.setText(_translate("MainWindow", "Adjust Contrast"))
        self.actionAdjust_Saturation.setText(_translate("MainWindow", "Adjust Saturation"))
        self.actionAdd_Noise.setText(_translate("MainWindow", "Add Noise"))
        self.actionDetect_Edges.setText(_translate("MainWindow", "Detect Edges"))
        self.actionChange_Color_Balance.setText(_translate("MainWindow", "Change Color Balance"))
