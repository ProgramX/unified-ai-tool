
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

    def open_file_dialogue(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            file = open(file_name, "r")
            with file:
                text = file.read()
                self.image_viewer.setPlainText(text)

    # TODO: MAKE IT FOR IMAGES RAHTER THAN TEXT
    def save_text_editor_content(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            text_content = self.image_viewer.toPlainText()
            with open(file_name, "w") as file:
                file.write(text_content)

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
        image_generator_input = QPlainTextEdit()
        image_generator_input.setPlaceholderText("Enter text to generate image")
        image_generator_input.setFixedHeight(3 * image_generator_input.fontMetrics().lineSpacing())
        window.right_sidebar.widgets.addWidget(image_generator_input)

        image_generation_button = QPushButton("\U0001F5BC\ufe0f Generate Image")
        image_generation_button.setStyleSheet("background-color: orange")
        image_generation_button.clicked.connect(lambda: self.generate_image(image_generator_input))
        window.right_sidebar.widgets.addWidget(image_generation_button)

        # Add some tools to the right sidebar for image editing
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(32, 32))
        toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        pencil_action = QAction("\u270F\ufe0f pencil", toolbar)
        toolbar.addAction(pencil_action)

        eraser_action = QAction("\U0001FA78 eraser", toolbar)
        toolbar.addAction(eraser_action)

        selection_action = QAction("\U0001F33E selection", toolbar)
        toolbar.addAction(selection_action)

        bucket_fill_action = QAction("\U0001F9EA bucket fill", toolbar)
        toolbar.addAction(bucket_fill_action)

        background_remover_action = QAction("\U0001F533 background remover", toolbar)
        toolbar.addAction(background_remover_action)

        window.right_sidebar.widgets.addWidget(toolbar)



    def create_toolbar_entry(self, window: MainWindow):
        action = window.toolbar.addAction("\U0001F58C\ufe0f Image Editor")
        action.triggered.connect(lambda: self.open_provider_window(window))

    def on_window(self, window: MainWindow):
        self.create_toolbar_entry(window)


image_provider = ImageProvider("image_provider")
print("image_provider loaded")
