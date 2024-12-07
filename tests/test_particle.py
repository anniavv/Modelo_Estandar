import unittest
from Modelo_Estandar.Particle import Particle
from Modelo_Estandar.ejemplos_particulas import standard_model_particles

class TestParticle(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        self.particle = Particle(
            charge=1,
            mass=1.0,
            position={'x': 0, 'y': 0, 'z': 0},
            spin=0.5,
            half_life='Estable',
            width=0,
            decay_length=float('inf'),
            magnetic_moment=0,
            quarks=['u', 'u', 'd']
        )

    def test_particle_creation(self):
        # Prueba la creación de una partícula
        self.assertEqual(self.particle.charge, 1)
        self.assertEqual(self.particle.mass, 1.0)
        self.assertEqual(self.particle.spin, 0.5)
        self.assertEqual(self.particle.quarks, ['u', 'u', 'd'])

    def test_particle_position(self):
        # Prueba la posición inicial
        self.assertEqual(self.particle.position, {'x': 0, 'y': 0, 'z': 0})

    def test_standard_model_particles(self):
        # Verifica que las partículas del modelo estándar estén definidas correctamente
        particles = standard_model_particles()
        self.assertIn("proton", particles)
        self.assertIn("electron", particles)
        self.assertAlmostEqual(particles["proton"].mass, 1.0, places=2)

if __name__ == "__main__":
    unittest.main()
