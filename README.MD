## Indicaciones
Launcher de minecraft que permite instalar tanto versiones normales como versiones de Forge.
- Si tienes una carpeta .minecraft instalada en tu carpeta appdata, te recomiendo eliminarla (y hacer respaldo de tus mundos) antes de utilizar el launcher

## Como usar el Launcher
1) Necesitas tener python instalado, una vez instalado, crear entorno virtual con `python -m venv .venv` o `python3 -m venv .venv`

2) una vez creado el entorno virtual, acceder con `.venv/scripts/activate` con windows o `. .venv/bin/activate` con linux.

3) dentro del entorno virtual instalar dependencias con `pip install -r requirements.txt`

4) una vez instaladas las dependencias, ejecutar launcher con `python main.py`

debe iniciar el entorno virtual cada vez que se desee iniciar el launcher, si no desea utilizar el entorno virtual, se salta la creacion de virtualenv, pero puede correr el riesgo de tener problemas de compatibilidad entre las librerias.
