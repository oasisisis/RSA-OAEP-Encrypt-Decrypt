import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from functools import partial

import encryptui
import decryptui
import keygenui
import md4gen
import keygen
import rsagen_n

from encryptui import Ui_MainWindow as Encrypt_Ui 
from decryptui import Ui_MainWindow as Decrypt_Ui
from keygenui import Ui_MainWindow as Keygen_Ui
from helloui import Ui_MainWindow as Hello_Ui

#欢迎窗口
class HelloWindow(QMainWindow, Hello_Ui):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    def __init__(self):
        super(HelloWindow, self).__init__()
        self.setupUi(self)
        self.to_encrypt_button.clicked.connect(self.go_encrypt)
        self.to_decrypt_button.clicked.connect(self.go_decrypt)
        self.to_gen_button.clicked.connect(self.go_gen)
    def go_encrypt(self):
        self.switch_window1.emit()
    def go_decrypt(self):
        self.switch_window2.emit()
    def go_gen(self):
        self.switch_window3.emit()

#加密窗口
class EncryptWindow(QMainWindow, Encrypt_Ui):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super(EncryptWindow, self).__init__()
        self.setupUi(self)
        self.pushButtonEn.clicked.connect(lambda:self.enc())
        self.pushButtonBc.clicked.connect(self.cancel)


    def enc(self):
        #从输入框获取输入传递给input
        inputPlain = self.plainText.toPlainText()
        inputPubE = self.pubE.toPlainText()
        inputPubN = self.pubN.toPlainText()
        result = rsagen_n.rsa_oaep_encrypt(inputPlain,int(inputPubE),int(inputPubN))
        self.cipherTextBrowser.setText(str(result))
    
    def cancel(self):
        self.switch_window.emit()

#解密窗口
class DecryptWindow(QMainWindow, Decrypt_Ui):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super(DecryptWindow, self).__init__()
        self.setupUi(self)
        self.pushButtonDe.clicked.connect(lambda:self.de())
        self.pushButtonBc.clicked.connect(self.cancel)  
    
    def de(self):
        inputCipher = self.cipherText.toPlainText()
        inputPubP = self.priP.toPlainText()
        inputPubN = self.priN.toPlainText()
        result = rsagen_n.rsa_oaep_decrypt(inputCipher,int(inputPubP),int(inputPubN))
        self.plainTextBrowser.setText(str(result))

    def cancel(self):
        self.switch_window.emit()

#密钥生成窗口
class KeygenWindow(QMainWindow, Keygen_Ui):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super(KeygenWindow, self).__init__()
        self.setupUi(self)
        self.gen_key_button.clicked.connect(self.gen)

    #调用密钥生成算法，将公钥和私钥分别显示在两个窗口上
    def gen(self):
        pub,pri = keygen.generate_key()
        self.pubkey_browser.setText(str(pub))
        self.prikey_browser.setText(str(pri))
    

    

class Controller:
    def __init__(self):
        self.hello = HelloWindow()
        self.encrypt = EncryptWindow()
        self.decrypt = DecryptWindow()
        self.keygen = KeygenWindow()
    def show_hello(self):
        self.hello = HelloWindow()
        self.hello.switch_window1.connect(self.show_encrypt)
        self.hello.switch_window2.connect(self.show_decrypt)
        self.hello.switch_window3.connect(self.show_gen)
        self.hello.show()
        self.encrypt.close()
        self.decrypt.close()
    def show_encrypt(self):
        self.encrypt = EncryptWindow()
        self.encrypt.switch_window.connect(self.show_hello)
        self.encrypt.show()
        self.hello.close()
        self.decrypt.close()
    def show_decrypt(self):
        self.decrypt = DecryptWindow()
        self.decrypt.switch_window.connect(self.show_hello)
        self.decrypt.show()
        self.hello.close()
        self.encrypt.close()
    def show_gen(self):
        self.keygen = KeygenWindow()
        self.keygen.switch_window.connect(self.show_hello)
        self.keygen.show()
    

def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_hello()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

