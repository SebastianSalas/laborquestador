from fastapi import FastAPI

app = FastAPI()

@app.get('/servicio-sebas')
async def servicio_sebas():
    return {"mensaje": "Hola soy sebastian"}