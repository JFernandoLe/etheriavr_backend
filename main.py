"""
Punto de entrada principal del servidor EtheriaVR Backend.
Este servidor provee APIs REST para la gestión de usuarios, canciones, artistas y sesiones de práctica.
"""
import uvicorn
from fastapi import FastAPI
from etheriavr_backend.presentation.controllers import user_controller

app = FastAPI(
    title="EtheriaVR Backend",
    version="1.0",
    description="API Backend para EtheriaVR - Sistema de aprendizaje musical en VR"
)

# Registrar routers
app.include_router(user_controller.router)

@app.get("/")
def root():
    return {
        "message": "Servidor EtheriaVR Backend activo",
        "version": "1.0",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}


def main():
    """Inicia el servidor FastAPI"""
    print("=" * 50)
    print("Iniciando EtheriaVR Backend Server")
    print("=" * 50)
    print("API disponible en: http://localhost:8000")
    print("Documentación en: http://localhost:8000/docs")
    print("=" * 50)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True  # Activar auto-reload para desarrollo
    )


if __name__ == "__main__":
    main()
