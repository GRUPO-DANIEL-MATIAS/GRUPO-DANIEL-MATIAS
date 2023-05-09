import time
import datetime
import serial

#Comunicacion serial entre el arduino y la raspberry
class Comunicacion_serial:
    def __init__(self, port='/dev/ttyACM0', baudrate=9600):
        self.serial_port = serial.Serial(port, baudrate)
    def leer_datos(self):
        datos = self.serial_port.readline().decode().rstrip()
        return datos

#Leemos los datos y hacemos el calculo
class Arduino:
    def leer_datos(self):
        datos_recibidos = Comunicacion_serial().leer_datos()
        return datos_recibidos

    def calculo(self):
        temperaturas = []
        tiempo_inicial = datetime.datetime.now()
        while True:
            # Leer temperatura
            temperatura = Arduino().leer_datos()
            # Guardar temperatura en un arreglo
            temperaturas.append(float(temperatura))
            # Mostramos la temperatura actual
            print("Temperatura actual: ",temperatura)
            # Espera de 30 seg
            time.sleep(30)
            # Vemos si han pasado 5 min
            paso_del_tiempo = datetime.datetime.now() - tiempo_inicial
            if paso_del_tiempo.total_seconds() >= 300:
                # Calcular temperatura promedio
                promedio = sum(temperaturas) / len(temperaturas)
                # Mostrar temperatura promedio por consola
                print("Temperatura promedio:", promedio)
                # Guardar temperatura promedio en archivo de texto
                with open("temperaturas.txt", "a") as f:
                    f.write(str(promedio)+"\n")
                # Reiniciar lista de temperaturas y tiempo de inicio
                temperaturas = []
                tiempo_inicial = datetime.datetime.now()

Arduino().calculo()
