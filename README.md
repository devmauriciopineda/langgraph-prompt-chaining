# Agente de Resumen y Traducción con LangGraph

Este proyecto implementa un agente simple construido con LangGraph que realiza dos tareas secuenciales: resumir un texto en inglés y luego traducir el resumen resultante al español.

El agente utiliza el modelo `gemini-1.5-flash` de Google para ambas tareas de procesamiento de lenguaje.

## Características

- **Resumen de texto**: Genera un resumen conciso de un texto dado.
- **Traducción**: Traduce el resumen generado al español.
- **Orquestación con LangGraph**: Define un flujo de trabajo claro y secuencial (`resumen` -> `traducción`).
- **Configuración Centralizada**: Gestiona las claves de API y configuraciones a través de un archivo `.env`.

## Requisitos

- Python 3.9+
- `pip` para la gestión de paquetes

## Instalación

1.  **Clonar el repositorio** (si aplica) o descargar los archivos del proyecto.

2.  **Navegar al directorio**:
    ```bash
    cd ruta/del/proyecto
    ```

3.  **Crear un entorno virtual**:
    ```bash
    python -m venv env
    ```

4.  **Activar el entorno virtual**:
    - En Windows:
      ```bash
      .\env\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      source env/bin/activate
      ```

5.  **Instalar las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1.  Dentro del directorio root, cree un archivo llamado `.env`.

2.  Añada su clave de API de Google al archivo `.env`. El proyecto también está preconfigurado para usar Azure OpenAI, por lo que puede añadir esas claves si desea cambiar de modelo.

    ```env
    # Clave para Google GenAI (actualmente en uso)
    google_api_key="TU_API_KEY_DE_GOOGLE"

    # Claves para Azure OpenAI (opcional)
    azure_openai_api_key="TU_API_KEY_DE_AZURE"
    azure_openai_endpoint="TU_ENDPOINT_DE_AZURE"
    openai_api_version="TU_VERSION_DE_API"
    ```
    **Nota**: Para la ejecución actual, solo se requiere la `google_api_key`.

## Uso

Una vez que haya instalado las dependencias y configurado su archivo `.env`, puede ejecutar la aplicación.

1.  Asegúrese de que su entorno virtual esté activado.

2.  Desde el directorio root, ejecute el script principal:
    ```bash
    python app/main.py
    ```

3.  La salida en la consola mostrará el resumen del texto original y su posterior traducción al español.

## Estructura del Proyecto

```
root/
├── app/
│   ├── main.py             # Punto de entrada de la aplicación
│   ├── agents/
│   │   ├── graph.py        # Definición del grafo de LangGraph y los nodos
│   │   └── state.py        # Definición del estado del grafo
│   └── core/
│       └── config.py       # Carga de la configuración y variables de entorno
├── .env                    # Archivo para las claves de API (debe ser creado)
├── requirements.txt        # Dependencias de Python
└── README.md               # Este archivo
```
