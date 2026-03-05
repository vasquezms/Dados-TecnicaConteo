class DadosModel:
    """Modelo para calcular resultados del espacio muestral de dos dados"""
    
    def __init__(self):
        self.dado_a = [1, 2, 3, 4, 5, 6]
        self.dado_r = [1, 2, 3, 4, 5, 6]
        self.espacio_muestral = [(b, r) for b in self.dado_a for r in self.dado_r]
    
    def total_resultados(self):
        return len(self.espacio_muestral)
    
    def ambos_mismo_numero(self):
        return sum(1 for b, r in self.espacio_muestral if b == r)
    
    def suma_igual_a(self, valor):
        return sum(1 for b, r in self.espacio_muestral if b + r == valor)
    
    def suma_en_valores(self, *valores):
        return sum(1 for b, r in self.espacio_muestral if b + r in valores)
    
    def dado_azul_muestra(self, valor):
        return sum(1 for b, r in self.espacio_muestral if b == valor)
    
    def al_menos_uno_muestra(self, valor):
        return sum(1 for b, r in self.espacio_muestral if b == valor or r == valor)
    
    def ninguno_muestra(self, valor):
        return sum(1 for b, r in self.espacio_muestral if b != valor and r != valor)
    
    def suma_par(self):
        return sum(1 for b, r in self.espacio_muestral if (b + r) % 2 == 0)
    
    def obtener_todos_resultados(self):
        return {
            "total": self.total_resultados(),
            "dobles": self.ambos_mismo_numero(),
            "suma_4": self.suma_igual_a(4),
            "suma_7_u_11": self.suma_en_valores(7, 11),
            "azul_2": self.dado_azul_muestra(2),
            "al_menos_uno_2": self.al_menos_uno_muestra(2),
            "ninguno_2": self.ninguno_muestra(2),
            "suma_par": self.suma_par()
        }

    def verificar_lanzamiento(self, a, r):
        """Verifica las condiciones para un lanzamiento específico"""
        s = a + r
        return {
            "dobles": a == r,
            "suma_4": s == 4,
            "suma_7_u_11": s in (7, 11),
            "azul_2": a == 2,
            "al_menos_uno_2": a == 2 or r == 2,
            "ninguno_2": a != 2 and r != 2,
            "suma_par": s % 2 == 0
        }
