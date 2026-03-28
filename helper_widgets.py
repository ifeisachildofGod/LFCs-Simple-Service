
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPainter, QPixmap


class Image(QLabel):
    def __init__(self, path: str, width: int | None = None, height: int | None = None):
        super().__init__()
        
        pixmap = QPixmap(path)
        
        if width is not None or height is not None:
            if height is not None and width is None:
                self.setFixedSize(int(height * pixmap.size().width() / pixmap.size().height()), height)
            elif width is not None and height is None:
                self.setFixedSize(width, int(width * pixmap.size().height() / pixmap.size().width()))
            else:
                self.setFixedSize(width, height)
        
        self.setScaledContents(True)  # Optional: scale image to fit self
        scaled_pixmap = pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.setPixmap(scaled_pixmap)


class RotatableLabel(QLabel):
    def __init__(self, text, angle: int = 0, parent=None):
        super().__init__(text, parent)
        self.angle = angle  # Angle in degrees to rotate the text
        self.setProperty("class", "Arrow")
    
    def rotate(self, angle: int):
        self.angle = angle
        self.update()  # Trigger a repaint
    
    def paintEvent(self, _):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Save the painter's current state
        painter.save()

        # Translate to the center of the label
        center = self.rect().center()
        painter.translate(center)

        # Rotate the painter
        painter.rotate(self.angle)

        # Translate back and draw the text
        center.setX(center.x() + (2 if self.angle >= 180 else -1))
        painter.translate(-center)
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text())

        # Restore the painter's state
        painter.restore()

