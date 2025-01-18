# WebApp Dockerizada - Análisis de Imágenes con API SaaS de Imagga

Este proyecto es una WebApp simple que analiza imágenes utilizando la API SaaS de Imagga. La aplicación está dockerizada para facilitar su despliegue y ejecución.

## Funcionalidades
- Muestra tres imágenes con un botón "Analizar" para cada una.
- Conecta con la API de Imagga para realizar análisis de etiquetas.
- Muestra las etiquetas más relevantes junto con su nivel de confianza.

---

## Requisitos
Antes de ejecutar este proyecto, asegúrate de tener lo siguiente:
1. **Docker** instalado en tu sistema.
2. **Claves de acceso a la API de Imagga**:
   - Obtén una cuenta en [Imagga](https://imagga.com/) y accede a tu API Key y Secret.

---

## Instrucciones de Ejecución
Sigue estos pasos para ejecutar la WebApp:

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
2. **Agrega tus claves de Imagga**

Abre el archivo app.py.
Reemplaza los valores de IMAGGA_API_KEY y IMAGGA_API_SECRET con tus credenciales de la API.

3. **Construye la imagen Docker**
    ```bash
    docker build -t imagga-webapp .
    
4. **Ejecuta el contenedor Docker**
    ```bash
    docker run -p 5000:5000 imagga-webapp
    
5. **Accede a la aplicación**
Desde esta direccion: http://127.0.0.1:5000.
