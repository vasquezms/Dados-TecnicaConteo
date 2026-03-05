# Técnicas de Conteo - Dados

Aplicación de escritorio para calcular probabilidades y técnicas de conteo con dos dados distinguibles (azul y rojo).

## Descripción

Este proyecto implementa un programa en Python que genera el espacio muestral de dos dados y permite verificar automáticamente diferentes condiciones probabilísticas.

**Espacio muestral:** S = {(b,r) : b,r ∈ {1,...,6}}

## Estructura del Proyecto

```
Técnicas de conteo #2 Dados/

main.py                          # Punto de entrada de la aplicación
README.md                        # Documentación del proyecto
src/
    models/dados_model.py          # Lógica de cálculo (Modelo)
    views/dados_view.py           # Interfaz gráfica (Vista)
    controllers/dados_controller.py     # Controlador (MVC)
```

## Funcionalidades

1. **Total de resultados posibles** - Calcula el tamaño del espacio muestral
2. **Ambos muestran el mismo número** - Cuenta los dobles (1,1), (2,2), etc.
3. **Suma es 4** - Resultados donde la suma de ambos dados es 4
4. **Suma es 7 u 11** - Resultados donde la suma es 7 u 11
5. **Dado azul muestra 2** - Casos donde el dado azul es 2
6. **Al menos uno muestra 2** - Al menos un dado muestra 2
7. **Ninguno muestra 2** - Ningún dado muestra 2
8. **Suma es par** - Resultados con suma par

## Cómo ejecutar

```bash
python main.py
```

## Tecnologías

- **Python 3.x**
- **Tkinter** - Interfaz gráfica
- **Patrón MVC** - Arquitectura del proyecto

## Arquitectura

El proyecto sigue el patrón **MVC (Model-View-Controller)**:

- **Model** (`dados_model.py`): Contiene la lógica de negocio y cálculos
- **View** (`dados_view.py`): Maneja la interfaz gráfica
- **Controller** (`dados_controller.py`): Coordina el modelo y la vista

## Autores

Juan David Machado M
Jean Pierre Ortiz Arango
Santiago Muñoz vasquez
David Prada Quintero
Kevin Cardenas Rivillas
