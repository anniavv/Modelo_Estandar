from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
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

        # Tabla para las partículas
        self.table = QTableWidget()
        layout.addWidget(self.table)

        # Cargar datos
        self.load_particles()

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
