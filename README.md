# Asignación 3 - Creación y Despliegue de una API con Base de Datos

## Configuración de BD local:
```
SQLALCHEMY_DATABASE_URL = "sqlite:///./predictions.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()
```

![Local Image](images/DB.png)

## App corriendo de forma local:

![Local Image](images/app_online.png)

## Endpoint 1: status de conexiónde BD:

![Local Image](images/db_check.png)


## Endpoint 2: predicción:

![Local Image](images/predecir.png)
![Local Image](images/predict_status.png)


## Endpoint 2: predicción insertada en BD:

![Local Image](images/database_predicciones.png)