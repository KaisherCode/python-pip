# Curso de Python: PIP y Entornos Virtuales

## Instalación de Python en Windows (WSL) y Linux en un entorno pro

- verificamos si tenemos isntalado Python `python --version` 0 `python3 --version`

- Actualizamos `sudo apt update`

- Le damos upgrade `sudo apt -y upgrade`

- Instalar gestor de paquetes de dependencias `sudo apt install -y python3-pip` y verificamos con `pip3 -V`

- Otras dependencias para instalar: `sudo apt install -y build-essential libssl-dev libffi-dev python3-dev`

## Instalación en MAC

- Ìnstalar las herramientas de código antes de instalar python `sudo xcode-select --install`

- Instalar python `brew install python3`

## Python con VSCode

- Instalar extensiones: `Extension  de python`
- Si estamos instalando en WSL tambien se necesta `ext wsl`

## Python con Git y GitHub

- Creamos un repositorio en nuestra cuenta en github. `curso-python-pip`
- Luego estando en la terminal dentro de nuestro proyecto inicializamos git con `git init`
- Enlazamos nuestro proyecto local con el repositorio remoto en GitHub con el sgte comando : `git remote add origin git@github.com/nombre_usuario/nombre_repo.git`

- Una vez realizado el enlace verifiacmos `git remote -v`

- Agregamos los archivos en el stege `git add *`
- Subir los cambios al repositorio remoto `git push origin main`
- Configuracion del archivo `.gitignore` en el navegador ingresamos `gitignore.io` alli ingresamos `Windows`, `Linux`,`macOS` y `python` fianlmente le damos en crear. Y copiar y pegar contenido en el archivo `.gitignore`que se encuentra dentro del proyecto.
- Buen proyecto tambien necesita un archivo `README.md` aqui ponemos las instrucciones de como leventar el proyecto.









