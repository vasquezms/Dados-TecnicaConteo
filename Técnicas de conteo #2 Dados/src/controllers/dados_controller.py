import random

class DadosController:
    """Controlador para manejar la lógica entre el modelo y la vista"""
    
    def __init__(self, model, view=None):
        self.model = model
        self.view = view
        self.animando = False
        self.pasos_animacion = 12
        self.delay_ms = 70
        self.resultados_teoricos = self.model.obtener_todos_resultados()
    
    def set_view(self, view):
        self.view = view
        # Al inicio no se dibuja nada en el simulador hasta el primer lanzamiento
        self.view.canvas_azul.delete("all")
        self.view.canvas_rojo.delete("all")
        self.view.label_suma.config(text="Suma: ?")
        self.view.label_mensaje.config(text="")

    # --- Métodos para Análisis Teórico ---
    def mostrar_resultado_teorico(self, clave, titulo):
        valor = self.resultados_teoricos[clave]
        mensaje = f"{titulo}\n\n✅ Total: {valor} resultados"
        self.view.mostrar_mensaje("Resultado Teórico", mensaje)
    
    def mostrar_todos_teorico(self):
        self.view.crear_ventana_resumen(self.resultados_teoricos)

    # --- Métodos para Simulador Interactivo ---
    def obtener_resumen_modelo(self):
        return self.model.obtener_todos_resultados()

    def mostrar_espacio_muestral(self):
        S = self.model.espacio_muestral
        texto = "S = {(a,r): a,r ∈ {1,...,6}}\n\n"
        texto += ", ".join([f"({a},{r})" for a, r in S])
        self.view.mostrar_mensaje("Espacio muestral (36 resultados)", texto)

    def lanzar_dados(self):
        if self.animando:
            return
        self.animando = True
        self.view.boton_lanzar.config(state="disabled")
        a_final = random.randint(1, 6)
        r_final = random.randint(1, 6)
        self.animar_lanzamiento(0, a_final, r_final)

    def animar_lanzamiento(self, paso, a_final, r_final):
        if paso < self.pasos_animacion:
            a_tmp = random.randint(1, 6)
            r_tmp = random.randint(1, 6)
            self.view.dibujar_dado(self.view.canvas_azul, a_tmp, "#1d4ed8")
            self.view.dibujar_dado(self.view.canvas_rojo, r_tmp, "#dc2626")
            self.view.label_suma.config(text="Suma: ...")
            self.view.label_mensaje.config(text="🎲 Rodando...", fg="blue")
            self.view.root.after(self.delay_ms, lambda: self.animar_lanzamiento(paso + 1, a_final, r_final))
        else:
            self.view.dibujar_dado(self.view.canvas_azul, a_final, "#1d4ed8")
            self.view.dibujar_dado(self.view.canvas_rojo, r_final, "#dc2626")
            self.actualizar_verificaciones_simulador(a_final, r_final)
            self.animando = False
            self.view.boton_lanzar.config(state="normal")

    def actualizar_verificaciones_simulador(self, a, r):
        verificaciones = self.model.verificar_lanzamiento(a, r)
        self.view.actualizar_verificaciones(a, r, verificaciones)