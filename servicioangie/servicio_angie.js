const express = require('express');
const app = express();
const port = 3002;

app.get('/servicio-angie', (reg, res) => {
    res.json({mensaje: "Hola me llamo Angie estudio ingenieria y me encanta ver peliculas"});
});

app.listen(port, () =>{
    console.log('Servicio Angie escuchando en http://localhost:${port}');
});
