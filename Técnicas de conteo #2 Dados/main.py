import tkinter as tk
import sys
from pathlib import Path

# Agregar el directorio src al path
sys.path.append(str(Path(__file__).parent / "src"))

from models.dados_model import DadosModel
from views.dados_view import DadosView
from controllers.dados_controller import DadosController

def main():
    """Función principal para iniciar la aplicación"""
    root = tk.Tk()
    
    # Crear instancias del patrón MVC
    model = DadosModel()
    controller = DadosController(model)
    view = DadosView(root, controller)
    controller.set_view(view)
    
    root.mainloop()

if __name__ == "__main__":
    main()
