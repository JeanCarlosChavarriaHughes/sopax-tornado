import asyncio
import json
import socket

import websockets
from pruebaAccionador import ejecutarComandos
import serial
import time
import os


import tkinter as tk

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
            ejecucionVenta = ejecutarComandos.cierraSerial(ser)
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
                respuestaCashLess = "venta_aprobada"
                ejecucionVenta = ejecutarComandos.cierraSerial(ser)
                return respuestaCashLess

            else:

                ejecutarComandos.vendCancel(ejecucionVenta)
                ejecutarComandos.resetDevice(ejecucionVenta)
                ejecutarComandos.pollDevice(ejecucionVenta)
                ejecutarComandos.disableDevice(ejecucionVenta)
                respuestaCashLess = "venta_denegada"
                ejecucionVenta = ejecutarComandos.cierraSerial(ser)
                return respuestaCashLess

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

    respJSON = json.loads(message)

    #dividirPP = str(message).split(",")

    #productoCanal = dividirPP[0]
    #precioCanal = dividirPP[1]
    #metodoPago = dividirPP[2]

    productoCanal = respJSON["name"]
    precioCanal = respJSON["price"]
    metodoPago = respJSON["medio"]

    messageResp = servidorSOPAX.generarVenta(self, productoCanal, precioCanal, metodoPago)

    await websocket.send("I can confirm I got your message is: " + messageResp)
    print("Send Message")


fields = "Direccion ip:"

def show_entry_fields():

    #ingreso_ip = str(e1.get())
    ingresoIPv4 = os.popen('ip addr show wlo1').read().split("inet ")[1].split("/")[0]
    print(ingresoIPv4)
    #master.destroy()
    start_server = websockets.serve(response, ingresoIPv4, 8180)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


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
