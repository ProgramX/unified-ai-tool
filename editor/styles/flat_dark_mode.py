flat_dark_mode_style = """
QWidget {
    background-color: #0e0218;
    color: #FFFFFF;
    border: none;
}

QPushButton {
    padding: 5px 10px;
    border-radius: 3px;
    background-color: #1E0A2C;
    color: #FFFFFF;
}

QPushButton:hover {
    background-color: #3D1449;
}

QPushButton:pressed {
    background-color: #50195B;
}

QLineEdit {
    padding: 5px;
    border-radius: 3px;
    background-color: #1E0A2C;
    color: #FFFFFF;
    border: 1px solid #50195B;
}

QLabel {
    color: #FFFFFF;
}

QCheckBox {
    spacing: 5px;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
}

QCheckBox::indicator:unchecked {
    background-color: #0e0218;
    border: 1px solid #50195B;
}

QCheckBox::indicator:checked {
    background-color: #FFFFFF;
    border: 1px solid #FFFFFF;
}

QComboBox {
    padding: 5px;
    border-radius: 3px;
    background-color: #1E0A2C;
    color: #FFFFFF;
    border: 1px solid #50195B;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 0px;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    image: url(down_arrow.png);
}

QSlider {
    padding: 5px;
}

QSlider::groove:horizontal {
    background-color: #1E0A2C;
    height: 10px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #50195B;
    width: 10px;
    margin-top: -3px;
    margin-bottom: -3px;
    border-radius: 3px;
}

QProgressBar {
    text-align: center;
    border: none;
    background-color: #1E0A2C;
}

QProgressBar::chunk {
    background-color: #50195B;
}

QSpinBox {
    padding: 5px;
    border-radius: 3px;
    background-color: #1E0A2C;
    color: #FFFFFF;
    border: 1px solid #50195B;
}

QScrollBar {
    background-color: #1E0A2C;
}

QScrollBar:horizontal {
    height: 12px;
}

QScrollBar:vertical {
    width: 12px;
}

QScrollBar::handle {
    background-color: #50195B;
    border-radius: 6px;
}

QScrollBar::handle:hover {
    background-color: #3D1449;
}

QScrollBar::add-page, QScrollBar::sub-page {
    background-color: none;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background-color: none;
    width: 0px;
    height: 0px;
}

QScrollBar::add-line:horizontal {
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical {
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QSplitter::handle {
    background-color: #3D1449;
    width: 8px;
    border: none;
}
"""
