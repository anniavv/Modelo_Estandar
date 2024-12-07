class Particle():
  '''Una particula es un constituyente fundamental del universo. Esta clase representa partículas del modelo estándar.
  Propiedades:
  ----------

  c: carga de la partícula en unidades de [e]
  m: masa de la partícula [GeV]
  r: posición en unidades de [metros]
  s: espín de la partícula
  v: vida media [segundos]. 'None' si la partícula es estable.
  w: ancho de desintegració [GeV]
  l: longitud de desintegración [m]
  m: momento magnético [e·cm]
  q: quarks. Representa de qué quarks están hechas las partículas.
  '''

  type = 'Particle'

  def __init__(self, charge, mass, position, spin, half_life, quarks, width, decay_length, magnetic_moment):
        self.charge = charge
        self.mass = mass
        self.position = position
        self.spin = spin
        self.half_life = half_life
        self.quarks = quarks
        self.width = width
        self.decay_length = decay_length
        self.magnetic_moment = magnetic_moment
        """Identifica si una partícula es un boson o fermion"""
        self.is_fermion = bool(spin % 1.0)
        self.is_boson = not self.is_fermion

  def properties(self):
    """  Imprime las propiedades de la partícula de una manera organizada:
        - Carga, masa y espín.
        - Posición en el espacio.
        - Vida media.
        - Ancho de desintegración.
        - Longitud de desintegración.
        - Momento magnético.
        - Composición en quarks.
        """
    r = self.r
    str_properties = f'tipo: {self.type}\n' + (
            f'Carga: {str(self.charge)} e \n' +
            f'Masa: {str(self.mass)} GeV \n' +
            f'Posicion: x={r["x"]}, y={r["y"]}, z={r["z"]} \n' +
            f'Spin: {str(self.spin)}\n' +
            f'Vida media: {str(self.half_life)} s \n' +
            f'Ancho de desintegración: {str(self.width)} GeV \n' +
            f'Longitud de desintegración: {str(self.decay_length)}  \n' +
            f'Momento magnético: {str(self.magnetic_moment)}  e·cm \n' +
            f'Quarks de los que está formado: {str(self.quarks)}'
        )

    print(str_properties)