from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtGui import QWindow
from PySide2.QtCore import Qt
from PySide2.QtUiTools import QUiLoader
from controller import controller
import subprocess


class MainWidget(QWidget):
    def __init__(self, ui_file_path):
        super(MainWidget, self).__init__()
        self._imported_pdf = None
        self.ui_file_path = ui_file_path
        self._setup_ui(ui_file_path)
        self._ui.setWindowTitle("PDF-OCR")

    def _load_ui_file(self, ui_file_path):
        loader = QUiLoader()
        self._ui = loader.load(ui_file_path)
    
    def _setup_ui(self, ui_file_path):
        self._load_ui_file(ui_file_path)
        self._ui.export_button.setDisabled(True)
        self._ui.import_button.clicked.connect(self._on_import_button_clicked)
        self._ui.export_button.clicked.connect(self._on_export_button_clicked)

    def _load_pdf(self, pdf_file_path):
        subprocess.Popen(["xdg-open {}".format(pdf_file_path)], shell=True)
    
    def _color_label(self, label, color):
        label.setStyleSheet("color: {}".format(color))
    
    def _on_import_button_clicked(self):
        pdf, _ = QFileDialog.getOpenFileUrl(self, "Import PDF", "", "PDF Files (*.pdf)")
        pdf_path = pdf.path()
        print("the pdf_path is",pdf_path)
        if not pdf_path:
            self._ui.import_label.setText("PDF file not loaded!")
            self._color_label(self._ui.import_label, "red")
            return
        self._ui.import_label.setText("PDF file loaded successfully!")
        self._color_label(self._ui.import_label, "blue")
        self._ui.export_label.setText("")
        self._ui.export_button.setDisabled(False)
        self._imported_pdf = pdf_path
    
    def _on_export_button_clicked(self):
        pdf_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        print("the new pdf_path is",pdf_path)
        if not pdf_path:
            self._ui.export_label.setText("PDF file not saved!")
            self._color_label(self._ui.export_label, "red")
            return
        self._ui.export_label.setText("PDF file saved successfully!")
        self._color_label(self._ui.export_label, "blue")
        self._ui.export_button.setDisabled(True)
        self._exported_pdf = pdf_path + ".pdf"
        controller(self._imported_pdf, self._exported_pdf)
        self._load_pdf(self._exported_pdf)
    
    def show(self):
        self._ui.show()






