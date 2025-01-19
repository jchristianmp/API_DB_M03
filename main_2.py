from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

# from pyngrok import ngrok
# import nest_asyncio

# Configurar la base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./predictions.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

# Cargar la tabla existente
items = Table("predictions", metadata, autoload_with=engine)

# Configurar la sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definir los modelos Pydantic
# 
# # Inicializar la aplicación FastAPI
app = FastAPI()

@app.get("/connection")
def check_connection():
    return {"status": "healthy", "message": "Connected to the database successfully."}

## para ejecutar uvicorn main:app --reload