
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPainter, QPixmap

from base_widgets import *

class Image(QLabel):
    def __init__(self, path: str, width: int | None = None, height: int | None = None):
        super().__init__()
        
        self._width = width
        self._height = height
        
        self.setImagePath(path)
    
    def setImagePath(self, path: str):
        pixmap = QPixmap(path)
        
        if self._width is not None or self._height is not None:
            if self._height is not None and self._width is None:
                self.setFixedSize(int(self._height * pixmap.size().width() / pixmap.size().height()), self._height)
            elif self._width is not None and self._height is None:
                self.setFixedSize(self._width, int(self._width * pixmap.size().height() / pixmap.size().width()))
            else:
                self.setFixedSize(self._width, self._height)
        
        self.setScaledContents(True)  # Optional: scale image to fit self
        scaled_pixmap = pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.setPixmap(scaled_pixmap)
        # self.update()


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


class SeperatorWidget(BaseWidget):
    def __init__(self, orientation: Qt.Orientation, spacing: int, width: Optional[int] = None, height: Optional[int] = None, color: Optional[str] = None):
        super().__init__()
        
        x_spacing = spacing // 2 if orientation == Qt.Orientation.Horizontal else 0
        y_spacing = spacing // 2 if orientation == Qt.Orientation.Vertical else 0
        
        self.setContentsMargins(x_spacing, y_spacing, x_spacing, y_spacing)
        
        widget = BaseWidget()
        
        if width:
            widget.setFixedWidth(width)
        if height:
            widget.setFixedHeight(height)
        
        widget.setStyleSheet(f"background-color: {color or PALETTE["border"]};")
        
        self.addWidget(widget)

