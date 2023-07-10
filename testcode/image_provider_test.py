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

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    viewer = FancyImageViewer()
    viewer.loadImage("C:/Users/USER/Desktop/testlogo.jpg")
    viewer.show()

    sys.exit(app.exec())
