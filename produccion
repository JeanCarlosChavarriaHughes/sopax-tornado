import asyncio
import websockets
from pruebaAccionador import ejecutarComandos
import serial
import time

cashlessVendRequest = 0
cashlessVendSuccess = 0
ser = serial.Serial()
self = None

class servidorSOPAX(object):

    def activarDatafonoServidor(self):

        # The window will stay open until this function call ends.

        activarSerial = ejecutarComandos.serialSet(ser)
        ejecutarComandos.resetDevice(activarSerial)
        ejecutarComandos.disableDevice(activarSerial)
        activado = ejecutarComandos.enableDevice(activarSerial)
        time.sleep(5)
        ejecutarComandos.disableDevice(activarSerial)
        ejecutarComandos.resetDevice(activarSerial)
        ejecutarComandos.cierraSerial(activarSerial)

    def generarVenta(self, producto, monto, medioPago):

            # The window will stay open until this function call ends.

            if (producto == "Producto 1"):
                producto = 12
            elif (producto == "Producto 2"):
                producto = 25
            elif (producto == "Producto 3"):
                producto = 36

            if medioPago == "Efectivo":
                medioPago = 2
                servidorSOPAX.ejecutarDatafonoCash(self, producto, monto)
            else:
                medioPago = 1
                servidorSOPAX.ejecutarDatafonoCashless(self, producto, monto)

    def ejecutarDatafonoCash(self, producto, monto):

        variablesProducto = ejecutarComandos.ingresoValoresCash(producto, monto)
        ejecucionVenta = ejecutarComandos.serialSet(ser)
        ejecutarComandos.resetDevice(ejecucionVenta)
        ejecutarComandos.disableDevice(ejecucionVenta)
        ejecutarComandos.vendRequestCash(ejecucionVenta,variablesProducto[0])
        ejecutarComandos.disableDevice(ejecucionVenta)
        ejecutarComandos.resetDevice(ejecucionVenta)
        ejecucionVenta = ejecutarComandos.cierraSerial(ser)


    def ejecutarDatafonoCashless(self, producto, monto):

        variablesProducto = ejecutarComandos.ingresoValores(producto, monto)
        ejecucionVenta = ejecutarComandos.serialSet(ser)

        ejecutarComandos.resetDevice(ejecucionVenta)
        ejecutarComandos.disableDevice(ejecucionVenta)
        ejecutarComandos.enableDevice(ejecucionVenta)
        ejecutarComandos.pollEnableDevice(ejecucionVenta)

        ejecutarComandos.vendRequest(ejecucionVenta,variablesProducto[0])
        ventaExitosa = ejecutarComandos.pollDeviceVendRequest(ejecucionVenta)

        if (ventaExitosa):

            ejecutarComandos.vendSuccess(ejecucionVenta,variablesProducto[1])
            ejecutarComandos.pollDevice(ejecucionVenta)
            ejecutarComandos.disableDevice(ejecucionVenta)
            ejecutarComandos.resetDevice(ejecucionVenta)

        else:

            ejecutarComandos.vendCancel(ejecucionVenta)
            ejecutarComandos.resetDevice(ejecucionVenta)
            ejecutarComandos.pollDevice(ejecucionVenta)
            ejecutarComandos.disableDevice(ejecucionVenta)

        ejecucionVenta = ejecutarComandos.cierraSerial(ser)

    def activarReset(self):

        # The window will stay open until this function call ends.

        # Define variables y se ejecutan

        ejecucionVenta = ejecutarComandos.serialSet(ser)

        ejecutarComandos.disableDevice(ejecucionVenta)
        ejecutarComandos.pollDevice(ejecucionVenta)
        ejecutarComandos.resetDevice(ejecucionVenta)

        ejecucionVenta = ejecutarComandos.cierraSerial(ser)



async def response(websocket, path):

    message = await websocket.recv()
    print("Message client: " + message)
    dividirPP = str(message).split(".")

    productoCanal = dividirPP[0]
    precioCanal = dividirPP[1]
    metodoPago = dividirPP[2]

    servidorSOPAX.generarVenta(self, productoCanal, precioCanal, metodoPago)

    await websocket.send("I can confirm I got your message is: " + message)
    print("Send Message")

start_server = websockets.serve(response, 'localhost', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
