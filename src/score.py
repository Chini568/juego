class Score:
    _instance = None  

    def __new__(self):
        if self._instance is None:
            self._instance = super(Score, self).__new__(self)
            self._instance.puntaje = 200  
        return self._instance

    def obtener_puntaje(self):
        return self.puntaje

    def sumar_puntaje(self, cantidad):
        self.puntaje += cantidad

    def restar_puntaje(self, cantidad):
        self.puntaje -= cantidad
        if self.puntaje < 0:
            self.puntaje = 0  


    def resetear_puntaje(self):
        self.score = 0
