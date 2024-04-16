from fastapi import FastAPI
import httpx

app = FastAPI()

# Endpoint en Servicio Orquetador para iniciar la orquestación
@app.get("/orquestar")
async def orquestar():
    async with httpx.AsyncClient() as client:
        try:
            respuesta_sebas = await client.get("http://servicio-sebas-service/servicio-sebas")
            data_sebas = respuesta_sebas.json()
        except httpx.RequestError:
            data_sebas = "El servicio de sebas no está disponible"
        try:
            respuesta_diego = await client.get("http://servicio-diego-service/servicio-diego")
            data_diego = respuesta_diego.json()
        except httpx.RequestError:
            data_diego = "El servicio de diego no está disponible"

    return {"respuesta_sebas": data_sebas, "respuesta_diego": data_diego}