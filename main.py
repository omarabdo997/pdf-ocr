import sys
from main_window import MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
    sys.exit(0)
