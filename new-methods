import serial
import time


########################
#Suma valores para crc #
########################

#sumatoria en hex

def from_hex(hexdigits):
    return int(hexdigits, 16)

## Variables iniciales

precio = input("ingrese precio en colones")
posicion = input("ingrese el canal del producto")
tipoDePago = input("Seleccione Efectivo o Tarjeta")

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
                            print("crc: "+crc+" y el precio:" + numHex +","+numHex3 + " posicion: "+posicionHex)
                            cashlessVendRequest = [0x13,0x00,int(numHex,16),int(numHex3,16),0x00,int(posicionHex,16)
                                ,int(crc,16)]
                            cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]
                            print(cashlessVendRequest)
                            print(cashlessVendSuccess)
                            break
                        elif len(crc)==6 and c==4:
                            numCrc = "0x" + j
                        elif len(crc)==6 and c==5:
                            crc = numCrc + j
                            print("crc: "+crc +" y el precio:" + numHex +","+numHex3 + " posicion: "+posicionHex)
                            cashlessVendRequest = [0x13,0x00,int(numHex,16),int(numHex3,16),0x00,int(posicionHex,16)
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
                            print("crc: "+crc+" y el precio:" + numHex2 +","+numHex4 + " posicion: "+posicionHex)
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
    cashlessVendSuccess=[0x13,0x02,0x00,int(posicionHex,16),int(crc2,16)]


###################################################
# Defino configuracion del serial del controlador #
###################################################



ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM5'
ser.parity = 'N'
ser.bytesize = 8
ser.stopbits = 1
ser.rtscts = True
ser.timeout = 0
ser.xonxoff = False

ser.open()

#########################
#Definicion de comandos##
#########################

cashlessReset = [0x10, 0x10]
cashlessDisable = [0x14, 0x00, 0x14]
cashlessEnable = [0x14, 0x01, 0x15]
cashlessPoll = [0x12, 0x12]
cashlessCashSale = [0x13, 0x05, 0x00, 0x01, 0x00, 0x01, 0x16]

#################################
#################################
# #Envio parametros al datafono #
#################################
#################################

ser.write(cashlessReset)

#######################
#Respuesta del datafono
#######################

time.sleep(2) #tiempo de respuesta
read_Reset = ser.read(size=128)
print("Reset: " + str(read_Reset))


ser.write(cashlessDisable)

#######################
#Respuesta del datafono
#######################

time.sleep(2)
read_Disable = ser.read(size=128)
print("Disable: " + str(read_Disable))



ser.write(cashlessEnable)

#######################
#Respuesta del datafono
#######################

time.sleep(2)
read_Enable = ser.read(size=128)
print("Enable: " + str(read_Enable))
time.sleep(20)

ser.write(cashlessPoll)

#######################
#Respuesta del datafono
#######################

time.sleep(2)
read_Poll = ser.read(size=128)
print("Poll: " + str(read_Poll))
time.sleep(1)

ser.write(cashlessPoll)

#######################
#Respuesta del datafono
#######################

time.sleep(2)
read_Poll = ser.read(size=128)
print("Poll: " + str(read_Poll))
time.sleep(5)

ser.write(cashlessVendRequest)

#######################
#Respuesta del datafono
#######################

time.sleep(2)
read_VendRequest = ser.read(size=128)
print("VendRequest: " + str(read_VendRequest))
time.sleep(2)

ser.write(cashlessPoll)

#######################
#Respuesta del datafono
#######################

time.sleep(2)
read_Poll = ser.read(size=128)
print("Poll: " + str(read_Poll))

ser.write(cashlessVendSuccess)

#######################
#Respuesta del datafono
#######################

time.sleep(2)
read_VendSuccess = ser.read(size=128)
print("VendSuccess: " + str(read_VendSuccess))

ser.write(cashlessPoll)

#######################
#Respuesta del datafono
#######################

time.sleep(2)
read_Poll = ser.read(size=128)
print("Poll: " + str(read_Poll))

ser.write(cashlessDisable)

#######################
#Respuesta del datafono
#######################

time.sleep(2)
read_Disable = ser.read(size=128)
print("Disable: " + str(read_Disable))

###############
#Cierra serial#
###############

ser.close()
