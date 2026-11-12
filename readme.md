# PYTHON - NOTES

Repositorio de repaso y prácticas de Python utilizando un entorno virtual con **Python 3.14**.

---

## 🚀 Configuración del Entorno Virtual (Primera vez)

Si clonas el repositorio en una nueva máquina o vuelves a crear el entorno desde cero, asegúrate de tener instalado Python 3.14 en el sistema y ejecuta:

## 0. En caso de no saber la version

### Version
```bash
python --version
```
### Si no se tiene 3.14 (primera vez)
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.14 python3.14-venv python3.14-dev
```

## 1. Crear el entorno virtual con Python 3.14 (primera vez)
```bash
python3.14 -m venv venv
```

## 2. Actualizar pip dentro del entorno (opcional pero recomendado)

###  Activar el entorno virt
```bash
source venv/bin/activate
```

###  Actualizar el instalador de paquetes (opcional)
```bash
pip install --upgrade pip
```

## 3. Desactivar el entorno virt
```bash
deactivate
```