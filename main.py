import sys
from main_widget import MainWidget
from PySide2.QtWidgets import QApplication 

ui_file_path = "main_widget.ui"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_widget = MainWidget(ui_file_path)
    main_widget.show()
    app.exec_()
    sys.exit(0)
