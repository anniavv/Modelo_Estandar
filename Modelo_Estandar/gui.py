from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QWidget, QLabel
)
from PyQt5.QtGui import QPixmap
import os
from .ejemplos_particulas import standard_model_particles

class ParticleViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modelo Estándar")
        self.setGeometry(100, 100, 800, 600)

        # Configuración principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Logo en la parte superior 
        self.logo_label = QLabel(self)
        logo_path = self.get_logo_path()  
        pixmap = QPixmap(logo_path)

        if not pixmap.isNull():
            original_width = pixmap.width()
            original_height = pixmap.height()
            max_height = 160  
            aspect_ratio = original_width / original_height

            adjusted_width = int(max_height * aspect_ratio) 
            self.logo_label.setPixmap(pixmap.scaled(adjusted_width, max_height))  
        else:
            self.logo_label.setText("Error: No se pudo cargar el logo.")  

        # Centrar el logo usando un QHBoxLayout
        logo_layout = QHBoxLayout()
        logo_layout.addStretch()  
        logo_layout.addWidget(self.logo_label)
        logo_layout.addStretch()  
        layout.addLayout(logo_layout)

        # Tabla para las partículas
        self.table = QTableWidget()
        layout.addWidget(self.table)

        # Cargar datos
        self.load_particles()

    def get_logo_path(self):
        """
        Obtiene la ruta del archivo logo.png
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, "logo.png")

    def load_particles(self):
        # Obtener las partículas del modelo estándar
        particles = standard_model_particles()

        # Configurar la tabla
        self.table.setRowCount(len(particles))
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Nombre", "Carga", "Masa (GeV)", "Posición (x, y, z)", "Spin",
            "Vida media (s)", "Ancho (GeV)", "Quarks"
        ])

        # Agregar partículas a la tabla
        for row, (name, particle) in enumerate(particles.items()):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(str(particle.charge)))
            self.table.setItem(row, 2, QTableWidgetItem(str(particle.mass)))
            self.table.setItem(row, 3, QTableWidgetItem(
                f"({particle.position['x']}, {particle.position['y']}, {particle.position['z']})"
            ))
            self.table.setItem(row, 4, QTableWidgetItem(str(particle.spin)))
            self.table.setItem(row, 5, QTableWidgetItem(str(particle.half_life)))
            self.table.setItem(row, 6, QTableWidgetItem(str(particle.width)))
            self.table.setItem(row, 7, QTableWidgetItem(str(particle.quarks)))

def main():
    app = QApplication([])
    viewer = ParticleViewer()
    viewer.show()
    app.exec_()

if __name__ == "__main__":
    main()
