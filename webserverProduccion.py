import asyncio
import json
import websockets
from pruebaAccionador import ejecutarComandos
from condicionInicial import EnableThread
import serial
import time
import tkinter as tk

cashlessVendRequest = 0
cashlessVendSuccess = 0
ser = serial.Serial()
self = None

pruebaEnable = 0
prueba = EnableThread(sleep_interval=1)

class servidorSOPAX(object):

    def activarDatafonoServidor(self):

        activarSerial = ejecutarComandos.serialSet(ser)
        ejecutarComandos.resetDevice(activarSerial)
        ejecutarComandos.disableDevice(activarSerial)
        activado = ejecutarComandos.enableDevice(activarSerial)
        time.sleep(5)
        ejecutarComandos.disableDevice(activarSerial)
        ejecutarComandos.resetDevice(activarSerial)
        ejecutarComandos.cierraSerial(activarSerial)

    def generarVenta(self, producto, monto, medioPago):

        if (producto == "imagineing.com"):
            producto = 10
        elif (producto == "Producto 2"):
            producto = 25
        elif (producto == "Producto 3"):
            producto = 36

        if medioPago == "01":
            medioPago = 2
            respuestaGV = servidorSOPAX.ejecutarDatafonoCash(self, producto, monto)
            return respuestaGV
        else:
            medioPago = 1
            respuestaGV = servidorSOPAX.ejecutarDatafonoCashless(self, producto, monto)
            return respuestaGV
    def ejecutarDatafonoCash(self, producto, monto):

        variablesProducto = ejecutarComandos.ingresoValoresCash(producto, monto)
        ejecucionVenta = ejecutarComandos.serialSet(ser)
        if ejecucionVenta == False:
            respuestaCash = "puerto_desconectado"
        else:
            ejecutarComandos.resetDevice(ejecucionVenta)
            ejecutarComandos.disableDevice(ejecucionVenta)
            ejecutarComandos.vendRequestCash(ejecucionVenta,variablesProducto[0])
            ejecutarComandos.disableDevice(ejecucionVenta)
            ejecutarComandos.resetDevice(ejecucionVenta)
            ejecutarComandos.cierraSerial(ser)

            prueba = EnableThread(sleep_interval=1)
            prueba.start()

            respuestaCash = "efectivo_aceptado"

        return respuestaCash

    def ejecutarDatafonoCashless(self, producto, monto):

        variablesProducto = ejecutarComandos.ingresoValores(producto, monto)
        ejecucionVenta = ejecutarComandos.serialSet(ser)

        if ejecucionVenta == False:
            respuestaCashLess = "puerto_desconectado"
            return respuestaCashLess

        else:
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
                ejecutarComandos.cierraSerial(ser)

                prueba = EnableThread(sleep_interval=1)
                prueba.start()

                respuestaCashLess = "venta_aprobada"
                return respuestaCashLess

            else:

                ejecutarComandos.vendCancel(ejecucionVenta)
                ejecutarComandos.resetDevice(ejecucionVenta)
                ejecutarComandos.pollDevice(ejecucionVenta)
                ejecutarComandos.disableDevice(ejecucionVenta)
                ejecutarComandos.cierraSerial(ser)

                prueba = EnableThread(sleep_interval=1)
                prueba.start()

                respuestaCashLess = "venta_denegada"
                return respuestaCashLess

    def activarReset(self):
        # Define variables y se ejecutan

        ejecucionVenta = ejecutarComandos.serialSet(ser)

        ejecutarComandos.disableDevice(ejecucionVenta)
        ejecutarComandos.pollDevice(ejecucionVenta)
        ejecutarComandos.resetDevice(ejecucionVenta)
        ejecutarComandos.cierraSerial(ser)

        prueba = EnableThread(sleep_interval=1)
        prueba.start()

async def response(websocket, path):

    message = await websocket.recv()
    print("Message client: " + message)

    respJSON = json.loads(message)

    productoCanal = respJSON["name"]
    precioCanal = respJSON["price"]
    metodoPago = respJSON["medio"]

    prueba.kill()

    messageResp = servidorSOPAX.generarVenta(self, productoCanal, precioCanal, metodoPago)

    await websocket.send("I can confirm I got your message is: " + messageResp)
    print(messageResp)

fields = "Direccion ip:"


def show_entry_fields():

    #ingreso_ip = str(e1.get())
    ingresoIPv4 = 'localhost' #os.popen('ip addr show wlo1').read().split("inet ")[1].split("/")[0]
    print(ingresoIPv4)
    #master.destroy()
    start_server = websockets.serve(response, ingresoIPv4, 8180)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

#Procesos de arranca sistema

prueba.start()

show_entry_fields() # inicializa ingreso ip automatico

#master = tk.Tk()

#tk.Label(master,
#         text=fields).grid(row=0)
#e1 = tk.Entry(master)
#e1.grid(row=0, column=1)
#tk.Button(master,
#          text='OK', command=show_entry_fields).grid(row=3,
#                                                       column=1,
#                                                       sticky=tk.W,
#                                                       pady=4)


#tk.mainloop()
