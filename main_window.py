from PySide2.QtWidgets import QWidget
from PySide2.QtUiTools import QUiLoader


class MainWindow(QWidget):
    def __init__(self, ui_file_path):
        super(MainWindow, self).__init__()
        self._setup_ui(ui_file_path)
        self._ui.setWindowTitle("PDF-OCR")

    def _load_ui_file(self, ui_file_path):
        loader = QUiLoader()
        self._ui = loader.load(ui_file_path)
    
    def _setup_ui(self, ui_file_path):
        self._load_ui_file(ui_file_path)
    
    def show(self):
        self._ui.show()






