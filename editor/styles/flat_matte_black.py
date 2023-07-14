flat_matte_black_style = """
QWidget {
    background-color: #000000;
    color: #FFFFFF;
    border: none;
}

QPlainTextEdit {
    background-color: #202020;
}

QPushButton {
    padding: 5px 10px;
    border-radius: 3px;
    background-color: #202020;
    color: #FFFFFF;
}

QPushButton:hover {
    background-color: #404040;
}

QPushButton:pressed {
    background-color: #606060;
}

QLineEdit {
    padding: 5px;
    border-radius: 3px;
    background-color: #202020;
    color: #FFFFFF;
    border: 1px solid #606060;
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
    background-color: #000000;
    border: 1px solid #606060;
}

QCheckBox::indicator:checked {
    background-color: #FFFFFF;
    border: 1px solid #FFFFFF;
}

QComboBox {
    padding: 5px;
    border-radius: 3px;
    background-color: #202020;
    color: #FFFFFF;
    border: 1px solid #606060;
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
    background-color: #202020;
    height: 10px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #606060;
    width: 10px;
    margin-top: -3px;
    margin-bottom: -3px;
    border-radius: 3px;
}

QProgressBar {
    text-align: center;
    border: none;
    background-color: #202020;
}

QProgressBar::chunk {
    background-color: #606060;
}

QSpinBox {
    padding: 5px;
    border-radius: 3px;
    background-color: #202020;
    color: #FFFFFF;
    border: 1px solid #606060;
}

QScrollBar {
    background-color: #202020;
}

QScrollBar:horizontal {
    height: 12px;
}

QScrollBar:vertical {
    width: 12px;
}

QScrollBar::handle {
    background-color: #606060;
    border-radius: 6px;
}

QScrollBar::handle:hover {
    background-color: #404040;
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
    background-color: #404040;
    width: 8px;
    border: none;
}

QToolBar QToolButton {
    border: none;
    background-color: #202020;
    border-radius: 15px;
    padding: 5px;
}

QToolBar QToolButton:hover {
    border: 2px solid #FFFFFF;
}
"""
