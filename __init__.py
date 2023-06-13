import time
import matplotlib.pyplot as plt
import pandas as pd

class Tank:
    def __init__(self, volumen):
        self.volumen = volumen
        self.nivel = 0
        self.niveles = []
        self.estados = []
        self.tiempos = []
    
    def llenar_descargar(self, tasa_llenado, tasa_descarga, duracion):
        tiempo_inicial = time.time()
        
        while time.time() - tiempo_inicial < duracion:
            self.nivel += tasa_llenado
            if self.nivel > self.volumen:
                self.nivel = self.volumen
            self.niveles.append(self.nivel)
            self.estados.append(self.obtener_estado())
            self.tiempos.append(time.time() - tiempo_inicial)
            self.mostrar_grafica()
            time.sleep(1)
            
            self.nivel -= tasa_descarga
            if self.nivel < 0:
                self.nivel = 0
            self.niveles.append(self.nivel)
            self.estados.append(self.obtener_estado())
            self.tiempos.append(time.time() - tiempo_inicial)
            self.mostrar_grafica()
            time.sleep(1)
    
    def mostrar_grafica(self):
        plt.clf()  # Limpiar la figura anterior
        plt.bar(0, self.volumen, color='blue', alpha=0.5)  # Tanque lleno
        plt.bar(0, self.nivel, color='green', alpha=0.7)  # Nivel actual del tanque
        plt.ylim(0, self.volumen)
        plt.xlim(-1, 1)
        plt.xticks([])
        plt.ylabel('Volumen (litros)')
        plt.title('Simulación del tanque de agua')
        
        # Mostrar el nivel y el estado actual del tanque en la visualización
        plt.text(0, self.volumen * 0.8, f"Nivel: {self.nivel} litros\nEstado: {self.estados[-1]}")
        
        plt.draw()
        plt.pause(0.01)
    
    def obtener_estado(self):
        if self.nivel == self.volumen:
            return "Lleno"
        elif self.nivel > self.volumen:
            return "Desbordado"
        else:
            return "Mantiene"
    
    def mostrar_resultados(self):
        data = {
            'Tiempo (s)': self.tiempos,
            'Nivel (litros)': self.niveles,
            'Estado': self.estados
        }
        df = pd.DataFrame(data)
        print(df)
        
        plt.figure()
        plt.plot(self.tiempos, self.niveles)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Nivel (litros)')
        plt.title('Comportamiento del tanque de agua')
        plt.show()


# Configuración del tanque
volumen_tanque = 100  # Volumen del tanque en litros
tasa_llenado = 5      # Tasa de llenado en litros por segundo
tasa_descarga = 5     # Tasa de descarga en litros por segundo
duracion_simulacion = 30  # Duración estimada de la simulación en segundos

# Crear instancia del tanque
tanque = Tank(volumen_tanque)

# Llenar y descargar el tanque durante la duración de la simulación
tanque.llenar_descargar(tasa_llenado, tasa_descarga, duracion_simulacion)

# Mostrar resultados
tanque.mostrar_resultados()












