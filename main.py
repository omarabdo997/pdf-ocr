import sys
from main_window import MainWindow
from PySide2.QtWidgets import QApplication 

ui_file_path = "main_widget.ui"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow(ui_file_path)
    main_window.show()
    app.exec_()
    sys.exit(0)
