# EtheriaVR Backend

Servidor backend para EtheriaVR - Sistema de aprendizaje musical en realidad virtual.

## 🚀 Descripción

API REST desarrollada con FastAPI que gestiona:
- Usuarios y autenticación
- Catálogo de canciones y artistas
- Sesiones de práctica y progreso del usuario
- Configuraciones de usuario

## 📋 Requisitos

- Python 3.8+
- PostgreSQL (o base de datos compatible con SQLAlchemy)

## 🔧 Instalación

```bash
# Instalar dependencias
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic[email]

# Configurar base de datos (si usas Docker)
cd etheriavr_backend
docker-compose up -d
```

## ▶️ Ejecución

```bash
# Desde la raíz del proyecto
cd etheriavr_backend
python main.py
```

El servidor estará disponible en:
- API: http://localhost:8000
- Documentación interactiva: http://localhost:8000/docs
- Documentación alternativa: http://localhost:8000/redoc

## 📁 Estructura del Proyecto

```
etheriavr_backend/
├── main.py                 # Punto de entrada del servidor
├── docker-compose.yml      # Configuración de Docker
├── schema.sql             # Esquema de base de datos
├── application/           # Casos de uso (lógica de negocio)
├── domain/                # Entidades y repositorios (interfaces)
├── infrastructure/        # Implementaciones concretas (BD, etc.)
└── presentation/          # Controladores y DTOs (API REST)
```

## 🏗️ Arquitectura

El proyecto sigue Clean Architecture (Arquitectura Hexagonal):
- **Domain**: Entidades de negocio e interfaces de repositorios
- **Application**: Casos de uso (lógica de aplicación)
- **Infrastructure**: Implementaciones técnicas (base de datos, etc.)
- **Presentation**: Capa de API REST con FastAPI

## 🔌 Endpoints Principales

- `GET /` - Estado del servidor
- `GET /health` - Health check
- `POST /users/register` - Registro de usuario
- (Más endpoints según tus controllers)

## 🐳 Docker

Para ejecutar con Docker:

```bash
docker-compose up -d
```

Esto levantará la base de datos PostgreSQL configurada.
