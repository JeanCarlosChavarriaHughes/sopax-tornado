import serial
import time
import serial.tools.list_ports

ser = serial.Serial() #variable inicial del serial

class ejecutarComandos(object):

    def from_hex(hexdigits):

        return int(hexdigits, 16)

    def ingresoValores(posicion, precio):

        ########################
        #Suma valores para crc #
        ########################

        #sumatoria en hex
        def from_hex(self):

            return int(self, 16)

        ## Variables iniciales

        precioHex = str(hex(int(precio)))
        posicionHex = str(hex(int(posicion)))

        print([precioHex,posicionHex])

        if len(precioHex)==5 or len(precioHex)==6:

            f = 0
            for i in precioHex:

                if len(precioHex)==5:
                    if f == 2:
                        numHex = "0x0"+i
                    elif f == 3:
                        numHex2 = "0x"+i
                    elif f == 4:
                        numHex3 = numHex2+i
                        print(numHex +" "+numHex3+" "+posicionHex)
                        crc = hex(from_hex("0x13") + from_hex(numHex)+from_hex(numHex3)+from_hex(posicionHex))
                        crc2 = hex(from_hex("0x13") + from_hex("0x02") + from_hex(posicionHex))
                        if len(crc)==5 or len(crc)==6:
                            c=0
                            for j in crc:
                                if len(crc)==5 and c==3:
                                    numCrc = "0x" + j
                                elif len(crc)==5 and c==4:
                                    crc = numCrc + j
                                    print("crc: "+crc+" y el precio:" + numHex +","+numHex3 + " posicion: "
                                          +posicionHex)
                                    cashlessVendRequest = [0x13,0x00,int(numHex,16),int(numHex3,16),0x00,
                                                           int(posicionHex,16)
                                        ,int(crc,16)]
                                    cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                                    print(cashlessVendRequest)
                                    print(cashlessVendSuccess)
                                    break
                                elif len(crc)==6 and c==4:
                                    numCrc = "0x" + j
                                elif len(crc)==6 and c==5:
                                    crc = numCrc + j
                                    print("crc: "+crc +" y el precio:" + numHex +","+numHex3 + " posicion: "
                                          +posicionHex)
                                    cashlessVendRequest = [0x13,0x00,int(numHex,16),int(numHex3,16),0x00
                                        ,int(posicionHex,16)
                                        ,int(crc,16)]
                                    cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                                    print(cashlessVendRequest)
                                    print(cashlessVendSuccess)
                                    break
                                c += 1
                        else:
                            print("crc: "+crc +" y el precio:" + numHex +","+numHex3 + " posicion: "+posicionHex)
                            cashlessVendRequest = [0x13,0x00,int(numHex,16),int(numHex3,16),0x00,int(posicionHex,16),
                                                   int(crc,16)]
                            cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                            print(cashlessVendRequest)
                            print(cashlessVendSuccess)
                            break
                elif len(precioHex) == 6:
                    if f == 2:
                        numHex= "0x"+i

                    elif f == 3:
                        numHex2= numHex+i

                    elif f == 4:
                        numHex3= "0x"+i

                    elif f == 5:
                        numHex4= numHex3+i
                        print(numHex2 +" "+numHex4+" "+posicionHex)
                        crc = hex(from_hex("0x13") + from_hex(numHex2) + from_hex(numHex4) + from_hex(posicionHex))
                        crc2 = hex(from_hex("0x13") + from_hex("0x02") + from_hex(posicionHex))
                        if len(crc)==5 or len(crc)==6:
                            c=0
                            for j in crc:
                                if len(crc)==5 and c==3:
                                    numCrc = "0x" + j
                                elif len(crc)==5 and c==4:
                                    crc = numCrc + j
                                    print("crc: "+crc)
                                    cashlessVendRequest = [0x13,0x00,int(numHex2,16),int(numHex4,16),0x00,
                                                           int(posicionHex,16),int(crc,16)]
                                    cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                                    print(cashlessVendRequest)
                                    print(cashlessVendSuccess)
                                    break
                                elif len(crc)==6 and c==4:
                                    numCrc = "0x" + j
                                elif len(crc)==6 and c==5:
                                    crc = numCrc + j
                                    print("crc: "+crc+" y el precio:" + numHex2 +","+numHex4 + " posicion: "
                                          +posicionHex)
                                    cashlessVendRequest = [0x13,0x00,int(numHex2,16),int(numHex4,16),0x00,
                                                           int(posicionHex,16),int(crc,16)]
                                    cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                                    print(cashlessVendRequest)
                                    print(cashlessVendSuccess)
                                    break
                                c += 1
                        else:
                            print("crc: "+crc+" y el precio:" + numHex2 +","+numHex4 + " posicion: "+posicionHex)
                            cashlessVendRequest = [0x13,0x00,int(numHex2,16),int(numHex4,16),0x00,
                                                   int(posicionHex,16),int(crc,16)]
                            cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                            print(cashlessVendRequest)
                            print(cashlessVendSuccess)
                            break
                f += 1

        else:

            crc = hex(from_hex("0x13") + from_hex(precioHex) + from_hex(posicionHex))
            crc2 = hex(from_hex("0x13") + from_hex("0x02") + from_hex(posicionHex))
            cashlessVendRequest = [0x13,0x00,0x00,int(precioHex,16),0x00,int(posicionHex,16),int(crc,16)]
            cashlessVendSuccess = [0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
            print(cashlessVendRequest)
            print(cashlessVendSuccess)
        return (cashlessVendRequest,cashlessVendSuccess)

    def ingresoValoresCash(posicion, precio):

        ########################
        #Suma valores para crc #
        ########################

        #sumatoria en hex
        def from_hex(self):
            return int(self, 16)

        ## Variables iniciales

        precioHex = str(hex(int(precio)))
        posicionHex = str(hex(int(posicion)))

        print([precioHex,posicionHex])

        if len(precioHex)==5 or len(precioHex)==6:

            f = 0
            for i in precioHex:

                if len(precioHex)==5:
                    if f == 2:
                        numHex = "0x0"+i
                    elif f == 3:
                        numHex2 = "0x"+i
                    elif f == 4:
                        numHex3 = numHex2+i
                        print(numHex +" "+numHex3+" "+posicionHex)
                        crc = hex(from_hex("0x13")+ from_hex("0x05") + from_hex(numHex)+from_hex(numHex3)+from_hex(posicionHex))
                        crc2 = hex(from_hex("0x13") + from_hex("0x02") + from_hex(posicionHex))
                        if len(crc)==5 or len(crc)==6:
                            c=0
                            for j in crc:
                                if len(crc)==5 and c==3:
                                    numCrc = "0x" + j
                                elif len(crc)==5 and c==4:
                                    crc = numCrc + j
                                    print("crc: "+crc+" y el precio:" + numHex +","+numHex3 + " posicion: "
                                          +posicionHex)
                                    cashlessVendRequest = [0x13,0x05,int(numHex,16),int(numHex3,16),0x00,
                                                           int(posicionHex,16)
                                        ,int(crc,16)]
                                    cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                                    print(cashlessVendRequest)
                                    print(cashlessVendSuccess)
                                    break
                                elif len(crc)==6 and c==4:
                                    numCrc = "0x" + j
                                elif len(crc)==6 and c==5:
                                    crc = numCrc + j
                                    print("crc: "+crc +" y el precio:" + numHex +","+numHex3 + " posicion: "
                                          +posicionHex)
                                    cashlessVendRequest = [0x13,0x05,int(numHex,16),int(numHex3,16),0x00
                                        ,int(posicionHex,16)
                                        ,int(crc,16)]
                                    cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                                    print(cashlessVendRequest)
                                    print(cashlessVendSuccess)
                                    break
                                c += 1
                        else:
                            print("crc: "+crc +" y el precio:" + numHex +","+numHex3 + " posicion: "+posicionHex)
                            cashlessVendRequest = [0x13,0x05,int(numHex,16),int(numHex3,16),0x00,int(posicionHex,16),
                                                   int(crc,16)]
                            cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                            print(cashlessVendRequest)
                            print(cashlessVendSuccess)
                            break
                elif len(precioHex) == 6:
                    if f == 2:
                        numHex= "0x"+i

                    elif f == 3:
                        numHex2= numHex+i

                    elif f == 4:
                        numHex3= "0x"+i

                    elif f == 5:
                        numHex4= numHex3+i
                        print(numHex2 +" "+numHex4+" "+posicionHex)
                        crc = hex(from_hex("0x13") + from_hex("0x05") + from_hex(numHex2) + from_hex(numHex4) + from_hex(posicionHex))
                        crc2 = hex(from_hex("0x13") + from_hex("0x02") + from_hex(posicionHex))
                        if len(crc)==5 or len(crc)==6:
                            c=0
                            for j in crc:
                                if len(crc)==5 and c==3:
                                    numCrc = "0x" + j
                                elif len(crc)==5 and c==4:
                                    crc = numCrc + j
                                    print("crc: "+crc)
                                    cashlessVendRequest = [0x13,0x05,int(numHex2,16),int(numHex4,16),0x00,
                                                           int(posicionHex,16),int(crc,16)]
                                    cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                                    print(cashlessVendRequest)
                                    print(cashlessVendSuccess)
                                    break
                                elif len(crc)==6 and c==4:
                                    numCrc = "0x" + j
                                elif len(crc)==6 and c==5:
                                    crc = numCrc + j
                                    print("crc: "+crc+" y el precio:" + numHex2 +","+numHex4 + " posicion: "
                                          +posicionHex)
                                    cashlessVendRequest = [0x13,0x05,int(numHex2,16),int(numHex4,16),0x00,
                                                           int(posicionHex,16),int(crc,16)]
                                    cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                                    print(cashlessVendRequest)
                                    print(cashlessVendSuccess)
                                    break
                                c += 1
                        else:
                            print("crc: "+crc+" y el precio:" + numHex2 +","+numHex4 + " posicion: "+posicionHex)
                            cashlessVendRequest = [0x13,0x05,int(numHex2,16),int(numHex4,16),0x00,
                                                   int(posicionHex,16),int(crc,16)]
                            cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                            print(cashlessVendRequest)
                            print(cashlessVendSuccess)
                            break
                f += 1

        else:

            crc = hex(from_hex("0x13") + from_hex("0x05") + from_hex(precioHex) + from_hex(posicionHex))
            crc2 = hex(from_hex("0x13") + from_hex("0x02") + from_hex(posicionHex))
            cashlessVendRequest = [0x13,0x05,0x00,int(precioHex,16),0x00,int(posicionHex,16),int(crc,16)]
            cashlessVendSuccess = [0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
            print(cashlessVendRequest)
            print(cashlessVendSuccess)
        return (cashlessVendRequest,cashlessVendSuccess)


    ###################################################
    # Defino configuracion del serial del controlador #
    ###################################################

    #variablesHex.ingresoValores
    def serialSet(ser):

        ports = serial.tools.list_ports.comports(include_links=False)
        portSer = None
        
        portSer = ports[0].device
        #for port in ports:
            #print(port.device)
            #portSer = port.device

        ser.baudrate = 9600
        ser.port = portSer #importante se debe cambiar en RPI por '/dev/ttyUSB0' literlamente entre comillas simples
        ser.parity = 'N'
        ser.bytesize = 8
        ser.stopbits = 1
        ser.rtscts = False
        ser.timeout = 0
        ser.xonxoff = False
        try:
            ser.open()
        except Exception:
            return False

        return (ser)

    #variablesHex ingresoValores CondicionesIniciales
    def serialSetInicial(ser):

        while True: #conectarse a puerto serial
            ports = serial.tools.list_ports.comports(include_links=False)
            portSer = None
            
            portSer = ports[0].device
            print(port.device)
            #for port in ports:
             #   print(port.device)
             #   portSer = port.device
            #if portSer != None:
             #   break

        ser.baudrate = 9600         
        ser.port = portSer 
        ser.parity = 'N'
        ser.bytesize = 8
        ser.stopbits = 1
        ser.rtscts = False
        ser.timeout = 0
        ser.xonxoff = False
        try:
            ser.open()
        except Exception:
            return False

        return (ser)

        #########################
        #Definicion de comandos##
        #########################

        cashlessCashSale = [0x13, 0x05, 0x00, 0x01, 0x00, 0x01, 0x16]

    #################################
    #################################
    # #Envio parametros al datafono #
    #################################
    #################################

    def resetDevice(ser):

        cashlessReset = [0x10, 0x10]
        ser.write(cashlessReset)

        #######################
        #Respuesta del datafono
        #######################

        time.sleep(2) #tiempo de respuesta
        read_Reset = ser.read(size=128)
        print("Reset: " + str(read_Reset))


    def disableDevice(ser):

        cashlessDisable = [0x14, 0x00, 0x14]
        ser.write(cashlessDisable)

        #######################
        #Respuesta del datafono
        #######################

        time.sleep(2)
        read_Disable = ser.read(size=128)
        print("Disable: " + str(read_Disable))


    def enableDevice(ser):

        cashlessEnable = [0x14, 0x01, 0x15]
        ser.write(cashlessEnable)

        #######################
        #Respuesta del datafono
        #######################

        read_Poll = ser.read(size=128)
        print("Poll: " + str(read_Poll))
        read_PollStr = str(read_Poll)

        while read_PollStr == "b''" or read_PollStr.__contains__("'00"):

            ser.write(cashlessEnable)
            read_Poll = ser.read(size=128)
            read_PollStr = str(read_Poll)
            print("Enable: " + str(read_Poll))
            time.sleep(1)
            if read_PollStr != "b''":
                if read_PollStr.__contains__("03"):
                #if read_PollStr[6] == str(3):
                    break

    def pollDevice(ser):

        cashlessPoll = [0x12, 0x12]
        ser.write(cashlessPoll)

        #######################
        #Respuesta del datafono
        #######################

        time.sleep(2)
        read_Poll = ser.read(size=128)
        print("Poll: " + str(read_Poll))

        ser.write(cashlessPoll)


    def vendRequest(ser,cashlessVendRequest):

        while True:

            ser.write(cashlessVendRequest)
            time.sleep(3)
            read_Poll = ser.read(size=128)
            read_PollStr = str(read_Poll)
            print("VendRequest: " + str(read_Poll))
            time.sleep(4)
            if read_PollStr != "b''":
                if read_PollStr.__contains__("05"):
                    return True
                elif read_PollStr.__contains__("06"):
                    return False

    def vendRequestCash(ser,cashlessVendRequest):

        ser.write(cashlessVendRequest)

        #######################
        #Respuesta del datafono
        #######################

        time.sleep(2)
        read_VendRequest = ser.read(size=128)
        print("VendRequest: " + str(read_VendRequest))
        time.sleep(2)

    def vendSuccess(ser, cashlessVendSuccess):

        ser.write(cashlessVendSuccess)

        #######################
        #Respuesta del datafono
        #######################

        time.sleep(2)
        read_VendSuccess = ser.read(size=128)
        print("VendSuccess: " + str(read_VendSuccess))


    def vendCancel(ser):

        cashlessVendCancel = [0x13, 0x01, 0x14]
        ser.write(cashlessVendCancel)

        #######################
        #Respuesta del datafono
        #######################

        time.sleep(2)
        read_VendCancel = ser.read(size=128)
        print("VendSuccess: " + str(read_VendCancel))

    def alwaysEnable(ser):

        cashlessReset = [0x10, 0x10]
        ser.write(cashlessReset)
        time.sleep(1)
        cashlessDisable = [0x14,0x00,0x14]
        ser.write(cashlessDisable)
        time.sleep(1)
        cashlessEnable = [0x14,0x01,0x15]
        ser.write(cashlessEnable)
        time.sleep(240)

    ###############
    #Cierra serial#
    ###############

    def cierraSerial(ser):

        ser.close()
        return (ser)
