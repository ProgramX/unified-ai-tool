
# TODO: IMAGE PROVIDER IS BROUGHT FROM TEXT PROVIDER SO IT STILL HAS SOME TEXT RELATED CODE THAT NEEDS TO BE CHANGED

from editor.core import *
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import numpy as np



from PySide6.QtCore import Qt, QPointF, QRectF, QSizeF
from PySide6.QtGui import QPainter, QPixmap, QTransform, QWheelEvent
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem

class FancyImageViewer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.image_item = QGraphicsPixmapItem()
        self.scene.addItem(self.image_item)

        self.zoom_factor = 1.1
        self.setMinimumSize(200, 200)

    def loadImage(self, image_path):
        self.image_item.setPixmap(QPixmap(image_path))
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)

    def wheelEvent(self, event: QWheelEvent):
        # Zoom in/out based on wheel scroll
        zoom_in = event.angleDelta().y() > 0
        if zoom_in:
            self.scale(self.zoom_factor, self.zoom_factor)
        else:
            self.scale(1 / self.zoom_factor, 1 / self.zoom_factor)

    def mousePressEvent(self, event):
        # Enable dragging of the image using mouse clicks
        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self.setInteractive(False)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # Reset dragging mode after releasing mouse button
        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.NoDrag)
            self.setInteractive(True)
        super().mouseReleaseEvent(event)



class ImageProvider(Module):
    image_viewer: FancyImageViewer = None

    def generate_image(self, input: QPlainTextEdit):
        text = input.toPlainText()
        if text:
            pass # use OpenAI API to generate image or use own model

    def clear_provider_window(self, window: MainWindow):
        # Clear inner window
        window.set_inner_widget(QWidget())
        # Clear right sidebar
        window.clear_right_sidebar()
        # Remove copilot button
        copilot_button = window.findChild(QPushButton, "copilot_button")
        if copilot_button:
            window.status_bar.removeWidget(copilot_button)
            copilot_button.deleteLater()

    def open_provider_window(self, window: MainWindow):
        self.clear_provider_window(window)
        if self.image_viewer is None:
            self.image_viewer = FancyImageViewer()
            self.image_viewer.loadImage("C:/Users/USER/Desktop/testlogo.jpg")
        window.set_inner_widget(self.image_viewer)

        # Add a image generator tools gui to right sidebar
        generate_image_label = QLabel("Generate Image")
        generate_image_label.setStyleSheet("font-weight: bold")
        window.right_sidebar.widgets.addWidget(generate_image_label)

        image_generator_input = QPlainTextEdit()
        image_generator_input.setPlaceholderText("Enter text to generate image")
        image_generator_input.setFixedHeight(3 * image_generator_input.fontMetrics().lineSpacing())
        window.right_sidebar.widgets.addWidget(image_generator_input)

        image_generation_button = QPushButton("\U0001F5BC\ufe0f Generate Image")
        image_generation_button.setStyleSheet("background-color: orange")
        image_generation_button.clicked.connect(lambda: self.generate_image(image_generator_input))
        window.right_sidebar.widgets.addWidget(image_generation_button)

        # Add some tools to the right sidebar for image editing
        tools_label = QLabel("Tools")
        tools_label.setStyleSheet("font-weight: bold")
        window.right_sidebar.widgets.addWidget(tools_label)

        button_grid = QGridLayout()
        button_grid.setSpacing(2)
        button_grid.setHorizontalSpacing(0)

        emoji_codes = ["\u270F\ufe0f", "\U0001FA78", "\U0001F33E", "\U0001F9EA", "\U0001F533", "\U0001F4BE", "\U0001F4DD", "\U0001F4E1", "\U0001F4E5", "\U0001F4F7", "\U0001F5C3", "\U0001F4BB", "\U0001F4CA", "\U0001F4C1", "\U0001F4C4", "\U0001F4C5", "\U0001F4C6", "\U0001F4D6", "\U0001F4DC", "\U0001F4DD", "\U0001F4DE", "\U0001F4E2", "\U0001F4E3", "\U0001F4E4", "\U0001F4E8", "\U0001F4EC", "\U0001F4EF", "\U0001F4F0", "\U0001F4F1", "\U0001F4F2", "\U0001F4F3", "\U0001F4F4", "\U0001F4F5", "\U0001F4F6", "\U0001F4F8", "\U0001F4F9", "\U0001F4FA", "\U0001F4FB", "\U0001F4FC", "\U0001F4FD", "\U0001F4FE", "\U0001F4FF", "\U0001F500", "\U0001F501", "\U0001F502"]
        for i, emoji_code in enumerate(emoji_codes):
            button = QPushButton(emoji_code)
            button.setFixedSize(40, 40)
            button.setStyleSheet("font-size: 18px")
            button_grid.addWidget(button, i // 6, i % 6)

        window.right_sidebar.widgets.addLayout(button_grid)



    def create_toolbar_entry(self, window: MainWindow):
        action = window.toolbar.addAction("\U0001F58C\ufe0f Image Editor")
        action.triggered.connect(lambda: self.open_provider_window(window))

    def on_ready(self, window: MainWindow):
        self.create_toolbar_entry(window)

    def on_notif(self, notif: Notif):
        if notif.command == "open_file":
            image_provider.image_viewer.loadImage(notif.data)


image_provider = ImageProvider("image_provider")
print("image_provider loaded")
