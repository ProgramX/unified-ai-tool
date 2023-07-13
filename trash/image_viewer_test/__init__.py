import sys
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QImage, QPixmap, QContextMenuEvent, QPainter, QPen
from PySide6.QtCore import Qt, QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

from editor.core import *

class WebImageViewer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_url = None
        self.image_data = None
        self.scene = QGraphicsScene()
        self.zoom_factor = 1.0
        self.grid_visible = False
        self.grid_pen = QPen(Qt.gray, 1, Qt.DotLine)

        self.setScene(self.scene)

    def set_image_url(self, url):
        self.image_url = QUrl(url)
        self.download_image()

    def download_image(self):
        if not self.image_url:
            return

        manager = QNetworkAccessManager(self)
        request = QNetworkRequest(self.image_url)
        reply = manager.get(request)
        reply.finished.connect(self.on_image_download_finished)

    def on_image_download_finished(self):
        reply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            self.image_data = reply.readAll()
            self.load_image()
        reply.deleteLater()

    def load_image(self):
        if not self.image_data:
            return

        image = QImage.fromData(self.image_data)
        pixmap = QPixmap.fromImage(image)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene.clear()
        self.scene.addItem(pixmap_item)
        self.setScene(self.scene)

    def zoom_in(self):
        self.zoom_factor *= 1.2
        self.update_view()

    def zoom_out(self):
        self.zoom_factor /= 1.2
        self.update_view()

    def update_view(self):
        self.resetTransform()
        self.scale(self.zoom_factor, self.zoom_factor)

    def toggle_grid(self):
        self.grid_visible = not self.grid_visible
        self.update()

    def contextMenuEvent(self, event: QContextMenuEvent):
        menu = self.createStandardContextMenu()
        menu.addAction("Toggle Grid", self.toggle_grid)
        menu.exec_(event.globalPos())

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.grid_visible:
            painter = QPainter(self.viewport())
            painter.setPen(self.grid_pen)
            painter.drawRect(self.sceneRect())


class ImageViewerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.viewer = WebImageViewer(self)
        self.layout.addWidget(self.viewer)

    def set_image_url(self, url):
        self.viewer.set_image_url(url)

    def zoom_in(self):
        self.viewer.zoom_in()

    def zoom_out(self):
        self.viewer.zoom_out()


class IVW(Module):
    def on_ready(self, window: MainWindow):
        iv = ImageViewerWidget(window)
        iv.set_image_url("https://www.w3schools.com/html/pic_trulli.jpg")
        window.set_inner_widget(iv)


ivw = IVW("image_viewer_widget")
print("image module instanced")