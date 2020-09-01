import threading
from pruebaAccionador import ejecutarComandos
import serial

ser = serial.Serial()
ejecucionVenta = ejecutarComandos.serialSetInicial(ser)
ejecutarComandos.cierraSerial(ser)
class EnableThread(threading.Thread):

    def __init__(self, sleep_interval=1):
        super().__init__()
        self._kill = threading.Event()
        self._interval = sleep_interval

    def run(self):

        ejecucionVenta = ejecutarComandos.serialSetInicial(ser)

        while True:
            print("Ejecutando")
            ejecutarComandos.alwaysEnable(ejecucionVenta)
            # If no kill signal is set, sleep for the interval,
            # If kill signal comes in while sleeping, immediately
            #  wake up and handle
            is_killed = self._kill.wait(self._interval)
            if is_killed:
                break

        print("Killing Thread")


    def kill(self):
        ejecutarComandos.cierraSerial(ejecucionVenta)
        self._kill.set()
