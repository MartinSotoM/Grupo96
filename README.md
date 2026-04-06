# Grupo96
Grupo laboratorio programación 2. EIE434

Integrantes

1. Francisco Figueroa
2. Dhana Tapia
3. Martín Soto

### Arquitectura y Modularidad del Sistema

Este proyecto fue diseñado aplicando una arquitectura modular basada en paquetes de Python. Los principios técnicos básicos son:

* **Separación de Responsabilidades (SoC):** El ecosistema está segmentado en tres órganos independientes:
    * `data/`: Aislamiento exclusivo para la extracción y simulación de señales crudas.
    * `processing/`: El motor matemático. Contiene los modelos cinemáticos y el cálculo de métricas de error sin interactuar con el exterior.
    * `visualization/`: Módulo estrictamente dedicado al renderizado de datos mediante Matplotlib.

* **Orquestación Centralizada (`main.py`):** Actúa únicamente como el controlador (entry point). No ejecuta cálculos ni contiene lógica dura; su única función es importar los módulos mediante **rutas absolutas**, inyectar los datos y delegar los procesos respetando el flujo de ejecución.

* **Definición de Paquetes Formales:** Las carpetas internas han sido estructuradas con archivos `__init__.py` para que Python las reconozca como paquetes importables y no como simples directorios del sistema operativo.

* **Higiene del Repositorio:** Se ha configurado un `.gitignore` para bloquear la subida de binarios compilados de Python (`__pycache__/`), garantizando que el control de versiones en GitHub mantenga un historial limpio y enfocado exclusivamente en el código fuente.