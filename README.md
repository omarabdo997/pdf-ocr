# PDF-OCR Project

## Project Description

This project aims to make unsearchable scanned pdfs searchable be doing OCR on the pdf that contains pictures and cannot be searched.
This project is the Data Image Process project.

## Project Dependencies

Python 3.6 or higher - (https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

Virtual Enviroment - its recommended to have it installed when working with a python project (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

create a virutal env by running the following command:
```bash
virtualenv -p python3 env
```

activate the env using the following command in the same directory that you have setup the env in:
```bash
source env/bin/activate
```

navigate to the project directory where the requirements.txt file is located and run the following command:
```bash
pip install -r requirements.txt
```

and then install ghost script using the following commands:
```bash
sudo apt-get update -y
sudo apt-get install -y ghostscript-x
```

and then install tesseract using the following command:
```bash
apt-get install tesseract-ocr
```

to run the project after installing the dependecies in the activated enviroment go to the project directory where the main.py file is located and run:
```bash
python main.py
```