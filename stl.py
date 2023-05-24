stylesheet = """
QTableWidget {
font-family: "Segoe UI";
font-size: 12pt;
background-color: #000000;
alternate-background-color: #FFFFFF;
selection-background-color: #DAE4F4;
selection-color: #1E2D5F;
border: none;
}

QPushButton {
font-family: "Segoe UI";
font-size: 12pt;
font-weight: bold;
background-color: #000000;
color: #FFFFFF;
border: none;
border-radius: 4px;
padding: 8px 16px;
}

QPushButton:hover {
background-color: #0C1A3B;
}

QLabel {
font-family: "Segoe UI";
font-size: 12pt;
color: #000000;
}

QLineEdit {
font-family: "Segoe UI";
font-size: 12pt;
background-color: #000000;
color: #1E2D5F;
border: none;
border-bottom: 2px solid #1E2D5F;
padding: 3px;
}

QLineEdit:focus {
border-bottom-color: #0C1A3B;
}

/* Additional styling for gold elements */
QTableWidget::item:selected {
background-color: #FFD700;
}

QPushButton:disabled {
background-color: #696969;
color: #A9A9A9;
}

QLineEdit:disabled {
background-color: #A9A9A9;
}
"""




