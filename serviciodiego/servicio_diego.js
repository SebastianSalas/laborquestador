const express = require('express');
const app = express();
const port = 3002;

app.get('/servicio-diego', (req, res) => {
  res.json({ mensaje: "Hola me llamo Diego y estoy en séptimo semestre de ingeniería" });
});

app.listen(port, () => {
    console.log(`Servicio de Diego escuchando en http://localhost:${port}`);
});