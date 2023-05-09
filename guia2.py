import serial

class Comunicacion_serial:
    def __init__(self, port='/dev/ttyACM0', baudrate=9600):
        self.serial_port = serial.Serial(port, baudrate)
    def leer_datos(self):
        datos = self.serial_port.readline().decode().rstrip()
        return datos

class Arduino:
    def leer_datos(self):
        datos_recibidos = Comunicacion_serial().leer_datos()
        return datos_recibidos

if __name__ == '__main__':
    while True:
        datos = Arduino().leer_datos()
        if datos:
            print("Valor:", datos)
