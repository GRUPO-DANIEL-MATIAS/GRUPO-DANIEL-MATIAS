import serial
puerto_serie = serial.Serial("/dev/ttyACM0", 9600)

while True:
    linea = puerto_serie.readline().decode().strip()
    print(linea)
