const WebSocket = require('ws');
 
const ws = new WebSocket('ws://localhost:8080');
 
ws.on('open', function open() {
  ws.send('Producto 3.4458.card'); //Aqui va el requerimiento de las peticiones a sopax (canal, precio, metodoPago)
});
 
ws.on('message', function incoming(data) {
  console.log(data);
});