flat_light_mode_style = """
QWidget {
    background-color: #FFFFFF;
    color: #000000;
    border: none;
}

QPushButton {
    padding: 5px 10px;
    border-radius: 3px;
    background-color: #E0E0E0;
    color: #000000;
}

QPushButton:hover {
    background-color: #D3D3D3;
}

QPushButton:pressed {
    background-color: #C0C0C0;
}

QLineEdit {
    padding: 5px;
    border-radius: 3px;
    background-color: #F5F5F5;
    color: #000000;
    border: 1px solid #CCCCCC;
}

QLabel {
    color: #000000;
}

QCheckBox {
    spacing: 5px;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
}

QCheckBox::indicator:unchecked {
    background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
}

QCheckBox::indicator:checked {
    background-color: #000000;
    border: 1px solid #000000;
}

QComboBox {
    padding: 5px;
    border-radius: 3px;
    background-color: #F5F5F5;
    color: #000000;
    border: 1px solid #CCCCCC;
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
    background-color: #E0E0E0;
    height: 10px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #C0C0C0;
    width: 10px;
    margin-top: -3px;
    margin-bottom: -3px;
    border-radius: 3px;
}

QProgressBar {
    text-align: center;
    border: none;
    background-color: #E0E0E0;
}

QProgressBar::chunk {
    background-color: #C0C0C0;
}

QSpinBox {
    padding: 5px;
    border-radius: 3px;
    background-color: #F5F5F5;
    color: #000000;
    border: 1px solid #CCCCCC;
}

QScrollBar {
    background-color: #F5F5F5;
}

QScrollBar:horizontal {
    height: 12px;
}

QScrollBar:vertical {
    width: 12px;
}

QScrollBar::handle {
    background-color: #C0C0C0;
    border-radius: 6px;
}

QScrollBar::handle:hover {
    background-color: #D3D3D3;
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
"""
