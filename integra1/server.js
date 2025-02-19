const express = require("express");
const app = express();
const port = process.env.PORT || 3000;

// Servir archivos estáticos (como index.html)
app.use(express.static("public"));

// Ruta API de ejemplo
app.get("/api/saludo", (req, res) => {
  res.json({ mensaje: "¡Hola desde el servidor!" });
});

// Iniciar servidor
app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
