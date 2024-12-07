from .Particle import Particle

def standard_model_particles():
    """Crea un diccionario con partículas del modelo estándar."""
    particles = {
        "proton": Particle(
            charge=1,
            mass=1,  # GeV
            position={'x': 1, 'y': 2, 'z': 3},
            spin=0.5,
            half_life='Estable',
            width=0,  # GeV
            decay_length=float('inf'),  # Longitud infinita
            magnetic_moment=2.79 * 2.85e-13,  # e·cm
            quarks=['u', 'u', 'd']
        ),
        "electron": Particle(
            charge=-1,
            mass=0.000511,  # GeV
            position={'x': 1, 'y': 3, 'z': 3},
            spin=0.5,
            half_life='Estable',
            width=0,
            decay_length=float('inf'),
            magnetic_moment=1.001159652 * 2.85e-13,  # e·cm
            quarks='No está formado de quarks'
        ),
        "neutron": Particle(
            charge=0,
            mass=1,  # GeV
            position={'x': 0, 'y': 0, 'z': 0},
            spin=0.5,
            half_life=880,  # segundos
            width=1.0e-24,  # Ejemplo aproximado en GeV
            decay_length=10.0,  # metros
            magnetic_moment=-0.967 * 2.85e-13,  # e·cm
            quarks=['u', 'd', 'd']
        ),
        "muon": Particle(
            charge=-1,
            mass=0.105,  # GeV
            position={'x': 2, 'y': 2, 'z': 1},
            spin=0.5,
            half_life=2.2e-6,  # segundos
            width=2.99e-10,  # En GeV
            decay_length=658.7,  # metros
            magnetic_moment=4.490 * 2.85e-13,  # e·cm
            quarks='No está formado de quarks'
        ),
        "tau": Particle(
            charge=-1,
            mass=1.777,  # GeV
            position={'x': 3, 'y': 1, 'z': 2},
            spin=0.5,
            half_life=2.9e-13,  # segundos
            width=2.27e-12,  # GeV
            decay_length=87.11e-9,  # metros
            magnetic_moment=-0.00168 * 2.85e-13,  # e·cm
            quarks='No está formado de quarks'
        ),
        "neutrino_electron": Particle(
            charge=0,
            mass=0.000000511,  # GeV
            position={'x': 0, 'y': 0, 'z': 0},
            spin=0.5,
            half_life='Estable',
            width=0,
            decay_length=float('inf'),
            magnetic_moment=0.064e-10,  # e·cm
            quarks='No está formado de quarks'
        ),
        "neutrino_muon": Particle(
            charge=0,
            mass=0.000106,  # GeV
            position={'x': 1, 'y': 1, 'z': 1},
            spin=0.5,
            half_life='Estable',
            width=0,
            decay_length=float('inf'),
            magnetic_moment=0.064e-10,  # e·cm
            quarks='No está formado de quarks'
        ),
        "neutrino_tau": Particle(
            charge=0,
            mass=0.0001,  # GeV
            position={'x': 2, 'y': 2, 'z': 2},
            spin=0.5,
            half_life='Estable',
            width=0,
            decay_length=float('inf'),
            magnetic_moment=0.064e-10,  # e·cm
            quarks='No está formado de quarks'
        ),
        "foton": Particle(
            charge=0,
            mass=0,  # GeV (prácticamente sin masa)
            position={'x': 2, 'y': 1, 'z': 2},
            spin=1,
            half_life='Estable',
            width=0,
            decay_length=float('inf'),
            magnetic_moment=0,
            quarks='No está formado de quarks'
        ),
        "gluon": Particle(
            charge=0,
            mass=0,  # GeV
            position={'x': 2, 'y': 3, 'z': 1},
            spin=1,
            half_life='Estable',
            width=0,
            decay_length=float('inf'),
            magnetic_moment=0,
            quarks='No está formado de quarks'
        ),
        "Z": Particle(
            charge=0,
            mass=91.1,  # GeV
            position={'x': 3, 'y': 2, 'z': 2},
            spin=1,
            half_life=3.0e-25,  # segundos
            width=2.49,  # GeV
            decay_length=0.01,  # metros
            magnetic_moment=0,
            quarks='No está formado de quarks'
        ),
        "Higgs": Particle(
            charge=0,
            mass=125.2,  # GeV
            position={'x': 1, 'y': 2, 'z': 2},
            spin=0,
            half_life=1.6e-22,  # segundos
            width=4.07e-3,  # GeV
            decay_length=1.56e-3,  # metros
            magnetic_moment=0,
            quarks='No está formado de quarks'
        ),
        "W+": Particle(
            charge=1,
            mass=80.36,  # GeV
            position={'x': 2, 'y': 2, 'z': 3},
            spin=1,
            half_life=3.0e-25,  # segundos
            width=2.085,  # GeV
            decay_length=0.01,  # metros
            magnetic_moment=0,
            quarks='No está formado de quarks'
        ),
        "W-": Particle(
            charge=-1,
            mass=80.36,  # GeV
            position={'x': 2, 'y': 2, 'z': 3},
            spin=1,
            half_life=3.0e-25,  # segundos
            width=2.085,  # GeV
            decay_length=0.01,  # metros
            magnetic_moment=0,
            quarks='No está formado de quarks'
        ),
    }
    return particles
