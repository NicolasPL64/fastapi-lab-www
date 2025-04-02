# FastAPI CRUD API

Este proyecto es una API RESTful desarrollada con FastAPI que implementa operaciones CRUD (Create, Read, Update, Delete) sobre un recurso de productos. La API incluye documentación automática y está preparada para ser desplegada en la nube.

## 👥 Integrantes

- Kevin Estiven Gil Salcedo - 2159863
- Nicolás Prado León - 2160073

## 📌 Características

- Desarrollo del backend con **FastAPI**
- Validación de datos con **Pydantic**
- Almacenamiento en un **diccionario en memoria**
- **Documentación interactiva** en `/docs` y `/redoc`
- Preparado para **despliegue en la nube**

## 🚀 Instalación y Ejecución Local

### 1️⃣ Requisitos

- Python 3.8 o superior
- `pip` instalado

### 2️⃣ Clonar el repositorio

```sh
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

### 3️⃣ Instalar dependencias

```sh
pip install -r requirements.txt
```

### 4️⃣ Ejecutar la aplicación

```sh
fastapi dev main.py
```

La API estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📚 Documentación

FastAPI genera documentación automática en los siguientes endpoints:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🔗 Endpoints

| Método  | Ruta               | Descripción                      |
|---------|--------------------|----------------------------------|
| `POST`  | `/items/`          | Crear un nuevo producto         |
| `GET`   | `/items/`          | Listar todos los productos      |
| `GET`   | `/items/{id}`      | Obtener un producto por ID      |
| `PUT`   | `/items/{id}`      | Actualizar un producto          |
| `DELETE`| `/items/{id}`      | Eliminar un producto            |

## ☁️ Despliegue en la Nube

La API ha sido desplegada en **Vercel** y está disponible en:

- **URL del despliegue:** [Enlace a la API](https://fastapi-lab-www.vercel.app)
- **URL de la documentación:** [Enlace a la documentación](https://fastapi-lab-www.vercel.app/docs)

## 🛠 Tecnologías Utilizadas

- **FastAPI** - Framework para APIs en Python
- **Pydantic** - Validación de datos

---
✏️ **Universidad del Valle - Sede Tuluá**
📌 **Ingeniería de Sistemas - Aplicaciones en el Web y Redes Inalámbricas**
