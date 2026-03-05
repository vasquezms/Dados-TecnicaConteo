import tkinter as tk
from tkinter import messagebox, ttk

class DadosView:
    """Vista para la interfaz gráfica de la aplicación de dados"""
    
    # Puntos (centros) normalizados en una grilla 3x3
    PIPS = {
        1: [(1, 1)],
        2: [(0, 0), (2, 2)],
        3: [(0, 0), (1, 1), (2, 2)],
        4: [(0, 0), (2, 0), (0, 2), (2, 2)],
        5: [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2)],
        6: [(0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2)],
    }

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_ventana()
        self.crear_interfaz()
    
    def configurar_ventana(self):
        self.root.title("🎲 Técnicas de Conteo - Simulador de Dados")
        self.root.geometry("800x750")
        self.root.configure(bg="#f3f4f6")
    
    def crear_interfaz(self):
        # Notebook para pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 1: Análisis Teórico
        self.tab_teorico = tk.Frame(self.notebook, bg="#2c3e50")
        self.notebook.add(self.tab_teorico, text="Análisis Teórico")
        self.crear_interfaz_teorica()

        # Pestaña 2: Simulador Interactivo
        self.tab_simulador = tk.Frame(self.notebook, bg="#f3f4f6")
        self.notebook.add(self.tab_simulador, text="Simulador Interactivo")
        self.crear_interfaz_simulador()

    def crear_interfaz_teorica(self):
        # Título
        titulo = tk.Label(self.tab_teorico, text="EJERCICIO: DADOS", 
                         font=("Arial", 24, "bold"), bg="#2c3e50", fg="#ecf0f1")
        titulo.pack(pady=20)
        
        subtitulo = tk.Label(self.tab_teorico, text="Espacio muestral: S = {(b,r) : b,r ∈ {1,...,6}}", 
                            font=("Arial", 12), bg="#2c3e50", fg="#bdc3c7")
        subtitulo.pack(pady=5)
        
        # Frame para botones
        frame_botones = tk.Frame(self.tab_teorico, bg="#2c3e50")
        frame_botones.pack(pady=20, padx=20, fill="both", expand=True)
        
        opciones = [
            ("Total de resultados posibles", "total"),
            ("Ambos muestran el mismo número", "dobles"),
            ("Suma es 4", "suma_4"),
            ("Suma es 7 u 11", "suma_7_u_11"),
            ("Dado azul muestra 2", "azul_2"),
            ("Al menos uno muestra 2", "al_menos_uno_2"),
            ("Ninguno muestra 2", "ninguno_2"),
            ("Suma es par", "suma_par")
        ]
        
        for texto, clave in opciones:
            btn = tk.Button(frame_botones, text=texto, 
                          command=lambda k=clave, t=texto: self.controller.mostrar_resultado_teorico(k, t),
                          font=("Arial", 11), bg="#3498db", fg="white",
                          activebackground="#2980b9", relief="raised",
                          cursor="hand2", width=35, height=1)
            btn.pack(pady=5)
        
        # Botón ver todos
        btn_todos = tk.Button(self.tab_teorico, text="Ver Todos los Resultados", 
                            command=self.controller.mostrar_todos_teorico,
                            font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
                            activebackground="#229954", cursor="hand2", width=30)
        btn_todos.pack(pady=10)

        # Botón Salir
        btn_salir = tk.Button(self.tab_teorico, text="Salir", 
                            command=self.root.quit,
                            font=("Arial", 12, "bold"), bg="#e74c3c", fg="white",
                            activebackground="#c0392b", cursor="hand2", width=30)
        btn_salir.pack(pady=10)

    def crear_interfaz_simulador(self):
        # Encabezado
        tk.Label(self.tab_simulador, text="Simulador de Lanzamiento", font=("Arial", 18, "bold"), bg="#f3f4f6").pack(pady=10)

        # Marco superior (dados + botones)
        frame_top = tk.Frame(self.tab_simulador, bg="#f3f4f6")
        frame_top.pack(pady=5)

        # Canvases de dados
        frame_dados = tk.Frame(frame_top, bg="#f3f4f6")
        frame_dados.grid(row=0, column=0, padx=15)

        tk.Label(frame_dados, text="Dado Azul", font=("Arial", 12, "bold"), fg="#1d4ed8", bg="#f3f4f6").grid(row=0, column=0, pady=5)
        tk.Label(frame_dados, text="Dado Rojo", font=("Arial", 12, "bold"), fg="#dc2626", bg="#f3f4f6").grid(row=0, column=1, pady=5)

        self.canvas_azul = tk.Canvas(frame_dados, width=170, height=170, bg="#ffffff", highlightthickness=0)
        self.canvas_azul.grid(row=1, column=0, padx=12)

        self.canvas_rojo = tk.Canvas(frame_dados, width=170, height=170, bg="#ffffff", highlightthickness=0)
        self.canvas_rojo.grid(row=1, column=1, padx=12)

        # Panel de estado suma
        frame_estado = tk.Frame(frame_top, bg="#f3f4f6")
        frame_estado.grid(row=0, column=1, padx=15, sticky="n")

        self.label_suma = tk.Label(frame_estado, text="Suma: ?", font=("Arial", 16, "bold"), bg="#f3f4f6")
        self.label_suma.pack(pady=10)

        self.label_mensaje = tk.Label(frame_estado, text="", font=("Arial", 12), fg="green", bg="#f3f4f6")
        self.label_mensaje.pack(pady=6)

        self.boton_lanzar = tk.Button(frame_estado, text="🎲 Lanzar Dados", font=("Arial", 12), width=16, 
                                     command=self.controller.lanzar_dados)
        self.boton_lanzar.pack(pady=10)

        tk.Button(frame_estado, text="📌 Ver espacio muestral (S)", 
                  command=self.controller.mostrar_espacio_muestral).pack(pady=5)

        # Separador
        tk.Frame(self.tab_simulador, height=2, bg="#d1d5db").pack(fill="x", padx=20, pady=10)

        # Verificación
        tk.Label(self.tab_simulador, text="Verificación de incisos (para el lanzamiento actual):", 
                 font=("Arial", 12, "bold"), bg="#f3f4f6").pack(pady=5)

        self.frame_check = tk.Frame(self.tab_simulador, bd=1, relief="groove", bg="white")
        self.frame_check.pack(padx=18, pady=6, fill="x")

        self.estados = {}
        self.estados["dobles"] = self.crear_fila_verificacion("• Ambos dados muestran el mismo número (dobles)", 0)
        self.estados["suma_4"] = self.crear_fila_verificacion("• La suma es 4", 1)
        self.estados["suma_7_u_11"] = self.crear_fila_verificacion("• La suma es 7 u 11", 2)
        self.estados["azul_2"] = self.crear_fila_verificacion("• El dado azul muestra 2", 3)
        self.estados["al_menos_uno_2"] = self.crear_fila_verificacion("• Al menos uno muestra 2", 4)
        self.estados["ninguno_2"] = self.crear_fila_verificacion("• Ninguno muestra 2", 5)
        self.estados["suma_par"] = self.crear_fila_verificacion("• La suma es par", 6)

        # Separador
        tk.Frame(self.tab_simulador, height=2, bg="#d1d5db").pack(fill="x", padx=20, pady=10)

        # Conteos del espacio muestral
        tk.Label(self.tab_simulador, text="Conteos (sobre el espacio muestral de 36 resultados):", 
                 font=("Arial", 12, "bold"), bg="#f3f4f6").pack(pady=5)

        self.frame_counts = tk.Frame(self.tab_simulador, bg="#f3f4f6")
        self.frame_counts.pack(pady=5)
        
        self.actualizar_conteos(self.controller.obtener_resumen_modelo())

    def crear_fila_verificacion(self, texto, row):
        tk.Label(self.frame_check, text=texto, font=("Arial", 11), bg="white").grid(row=row, column=0, padx=12, pady=7, sticky="w")
        estado = tk.Label(self.frame_check, text="—", font=("Arial", 12, "bold"), bg="white")
        estado.grid(row=row, column=1, padx=12, pady=7, sticky="e")
        return estado

    def dibujar_dado(self, canvas, valor, borde_color):
        canvas.delete("all")
        w = int(canvas["width"])
        h = int(canvas["height"])
        padding = 10
        radius = 18
        canvas.create_rectangle(padding, padding, w - padding, h - padding, outline=borde_color, width=6, fill="white")
        inner_left, inner_top = padding + 25, padding + 25
        inner_right, inner_bottom = w - padding - 25, h - padding - 25
        xs = [inner_left, (inner_left + inner_right) / 2, inner_right]
        ys = [inner_top, (inner_top + inner_bottom) / 2, inner_bottom]
        for (gx, gy) in self.PIPS[valor]:
            cx, cy = xs[gx], ys[gy]
            canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, fill="black", outline="black")

    def marcar(self, valor: bool) -> str:
        return "✅" if valor else "❌"

    def actualizar_verificaciones(self, a, r, verificaciones):
        s = a + r
        self.label_suma.config(text=f"Suma: {s}")
        self.label_mensaje.config(text="🎉 ¡Salieron dobles!" if a == r else "", fg="green")
        for clave, valor in verificaciones.items():
            if clave in self.estados:
                color = "#16a34a" if valor else "#dc2626"  # Verde o Rojo
                self.estados[clave].config(text=self.marcar(valor), fg=color)

    def actualizar_conteos(self, resumen):
        for widget in self.frame_counts.winfo_children():
            widget.destroy()
        etiquetas = [
            ("Total resultados posibles", "total"), ("Dobles", "dobles"), ("Suma = 4", "suma_4"),
            ("Suma = 7 u 11", "suma_7_u_11"), ("Azul = 2", "azul_2"), ("Al menos un 2", "al_menos_uno_2"),
            ("Ninguno muestra 2", "ninguno_2"), ("Suma par", "suma_par"),
        ]
        for i, (nombre, clave) in enumerate(etiquetas):
            valor = resumen.get(clave, 0)
            tk.Label(self.frame_counts, text=f"{nombre}:", font=("Arial", 10), bg="#f3f4f6").grid(row=i, column=0, padx=10, pady=2, sticky="w")
            tk.Label(self.frame_counts, text=str(valor), font=("Arial", 10, "bold"), bg="#f3f4f6").grid(row=i, column=1, padx=10, pady=2, sticky="e")

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def crear_ventana_resumen(self, resultados):
        ventana = tk.Toplevel(self.root)
        ventana.title("Todos los Resultados")
        ventana.geometry("700x550")
        ventana.configure(bg="#34495e")
        
        tk.Label(ventana, text="RESUMEN COMPLETO", 
                font=("Arial", 16, "bold"), bg="#34495e", fg="#ecf0f1").pack(pady=15)
        
        frame = tk.Frame(ventana, bg="#34495e")
        frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        explicaciones = {
            "total": "FÓRMULA: |S| = n × m\n\nPrincipio de multiplicación: 6 × 6 = 36",
            "dobles": "FÓRMULA: |A| = n\n\nCasos: {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}\nTotal: 6 casos",
            "suma_4": "Casos: {(1,3), (2,2), (3,1)}\nTotal: 3 casos",
            "suma_7_u_11": "Suma 7: 6 casos\nSuma 11: 2 casos\nTotal: 8 casos",
            "azul_2": "Casos: {(2,1), (2,2), (2,3), (2,4), (2,5), (2,6)}\nTotal: 6 casos",
            "al_menos_uno_2": "Azul=2 (6) + Rojo=2 (6) - Ambos=2 (1) = 11 casos",
            "ninguno_2": "Complemento: 36 - 11 = 25 casos",
            "suma_par": "Ambos pares (9) + Ambos impares (9) = 18 casos"
        }
        
        resultados_texto = [
            ("1. Total de resultados posibles:", resultados["total"], "total"),
            ("2. Ambos muestran el mismo número:", resultados["dobles"], "dobles"),
            ("3. Suma es 4:", resultados["suma_4"], "suma_4"),
            ("4. Suma es 7 u 11:", resultados["suma_7_u_11"], "suma_7_u_11"),
            ("5. Dado azul muestra 2:", resultados["azul_2"], "azul_2"),
            ("6. Al menos uno muestra 2:", resultados["al_menos_uno_2"], "al_menos_uno_2"),
            ("7. Ninguno muestra 2:", resultados["ninguno_2"], "ninguno_2"),
            ("8. Suma es par:", resultados["suma_par"], "suma_par")
        ]
        
        for texto, valor, clave in resultados_texto:
            frame_item = tk.Frame(frame, bg="#34495e")
            frame_item.pack(fill="x", pady=5)
            lbl = tk.Label(frame_item, text=f"{texto} {valor}", font=("Arial", 11, "bold"), bg="#34495e", fg="#ecf0f1", anchor="w")
            lbl.pack(side="left", fill="x", expand=True)
            btn_info = tk.Button(frame_item, text="?", command=lambda c=clave: self.mostrar_mensaje("Explicación", explicaciones[c]),
                               font=("Arial", 9, "bold"), bg="#3498db", fg="white", width=3)
            btn_info.pack(side="right")
        
        tk.Button(ventana, text="Regresar", command=ventana.destroy, font=("Arial", 10, "bold"), bg="#e67e22", fg="white", width=15).pack(pady=15)