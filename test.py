import numpi
class Punto(object):
    """Representa un punto sobre un plano con sus coordenadas cartesianas"""

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def punto_to_string(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        dist = (dx**2 + dy**2)**0.5
        return dist

    def acimut(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        acimut_rad = numpy.arctan2(dx, dy)
        acimut_gra = (acimut_rad * 200) / numpy.pi
        return (acimut_gra)

p = Punto(5.0, 2.5)
q = Punto(15.0, 32.5)

print(p.punto_to_string())

print(p.distancia(q))