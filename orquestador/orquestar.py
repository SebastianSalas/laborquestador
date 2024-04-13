from fastapi import FastAPI
import httpx

app = FastAPI()

# Endpoint en Servicio Orquetador para iniciar la orquestación
@app.get("/orquestar")
async def orquestar():
    async with httpx.AsyncClient() as client:
        try:
            respuesta_a = await client.get("http://servicio-sebas-service/servicio-sebas")
            data_a = respuesta_a.json()
        except httpx.RequestError:
            data_a = "El servicio de sebas no está disponible"

    return {"respuesta_a": data_a}