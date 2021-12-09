import PyQt5
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class NMGApp():
    def __init__(self, parent = None):
        self.fen = QWidget()
        self.fen.setWindowTitle("NMG - Normal Map Generator")
        self.fen.resize(900,480)
        self.fen.move(0,0)
        self.fen.show()  
        self.label_import_pic = QLabel(self.fen)
        self.import_pic = QPixmap("resources/grid.png")
        self.label_import_pic.setPixmap(self.import_pic)
        self.label_import_pic.move(150,100)
        self.label_import_pic.show()
        self.import_btn = QPushButton("Import a texture", self.fen)
        self.import_btn.setToolTip("Click to import a texture")
        self.import_btn.move(200,400)
        self.import_btn.clicked.connect(self.openFile)
        self.import_btn.show()
        self.save_btn = QPushButton("Save normal map", self.fen)
        self.save_btn.setToolTip("Click to save the file")
        self.save_btn.move(600,400)
        self.save_btn.show()

    def openFile(self) :
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
            
def main() :
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    nmg_instance = NMGApp()
    app.exec_()

if __name__ == "__main__" :
    main()
