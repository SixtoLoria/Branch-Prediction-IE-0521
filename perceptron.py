"""
Tarea01 Branch predictor.
Estudiantes: 
            Sixto Loria Villagra.         C04417
            Edwin Camacho Mora.           B21304

Grupo: 12
"""

# Importacion de librerias.
import math
import numpy as np

class perceptron:
    """ Clase que se encarga de definir los metodos y objetos
        necesarios para el funcionamiento del predictor por perceptron.     
        """
    def __init__(self, bits_to_index, global_history_size):
        
        self.bits_to_index = bits_to_index
        self.global_history_size = global_history_size
        self.size_perceptrons_table = 2**bits_to_index

        self.perceptrons_table = [[] for _ in range(2**bits_to_index)]
        for i in range(self.size_perceptrons_table):
            self.perceptrons_table[i] = [0]*(global_history_size + 1)
        #Creando tabla de historia global con bits inicializados a 0
        self.global_history_table = ""
        for i in range(global_history_size):
            self.global_history_table += "0"       
        #calculando el umbral de acuerdo a tamaño de la historial global
        self.threshold = math.floor(1.93 * global_history_size + 14)               
        # Para contear estadisticas.
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

    def print_info(self):
        """Se encarga de imprimir informacion general del predictor.
        
        Tales como los valores elegidos de tamaño de registros de historia y bits
        del PC de index.
        
        Esta funcion no retorna ningun valor ni recibe ningun parametro.
        """
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\t\tPerceptron")
        print("\tBits de PC para indexar:\t\t\t" + str(self.bits_to_index))
        print("\tTamaño del registro de historia global:\t\t" + str(self.global_history_size))

    def print_stats(self):
        """Funcion que se encarga de imprimir los resultados del predictor
        
        Imprime los resultados mas releventes como los saltos tomados, todal de predicciones,
        porcentaje de aciertos y entre otros.
        
        Esta funcion no retorna ningun valor ni recibe ningun parametro.
        """
        print("Resultados de la simulación")
        print("\t# branches:\t\t\t\t\t\t"+str(self.total_predictions))
        print("\t# branches tomados predichos correctamente:\t\t"+str(self.total_taken_pred_taken))
        print("\t# branches tomados predichos incorrectamente:\t\t"+str(self.total_taken_pred_not_taken))
        print("\t# branches no tomados predichos correctamente:\t\t"+str(self.total_not_taken_pred_not_taken))
        print("\t# branches no tomados predichos incorrectamente:\t"+str(self.total_not_taken_pred_taken))
        perc_correct = 100*(self.total_taken_pred_taken+self.total_not_taken_pred_not_taken)/self.total_predictions
        formatted_perc = "{:.3f}".format(perc_correct)
        print("\t% predicciones correctas:\t\t\t\t"+str(formatted_perc)+"%")

    def predict(self, PC):
        """  implementa el algoritmo de prediccion.
    
        Parameters
        ----------
        PC : int
            Valor de bits del PC para indexar.
        Returns
        -------
        T
            String que indica que el salto fue tomado.
        N
            String que indica que el salto no fue tomado.
        """
        index = int(PC) % self.size_perceptrons_table
        perceptron_weights = self.perceptrons_table[index]
        
        #Obteniendo w0
        self.y = perceptron_weights[0]*1
        for i in range(1,self.global_history_size+1):
            self.y += perceptron_weights[i]*self.reg(self.global_history_table[-i]) #y=w0 +wi*xi (i=0 hasta globlal_history_size))
        # Prediccion de se toma o no se toma
        if self.y >= 0:
            return "T"
        else:
            return "N"
 
    def update(self, PC, result, prediction):
        """ Se encarga de actualizar los valores del predictor.
        
        Parameters
        ----------
        PC : int
            Valor de bits del PC para indexar.
        result : String
            Contiene el resultado de si se tomo o no el salto
        prediction : String
            Contiene el valor de N o T que eligio nuestro algorito para predecir.
        
        Returns
        -------
            No retorna ningun valor por variable, solo actualiza valores.
        """
        # Calcular el índice de la tabla de perceptrones
        index = int(PC) % self.size_perceptrons_table
        # Obtener los pesos del perceptrón correspondiente
        self.perceptron_weights = self.perceptrons_table[index]
        # Convertir "T" a 1 y "N" a -1
        if result == "T":
            t=1
        else:
            t=-1
        # Verificar si se debe actualizar el peso del perceptrón
        sing_y =1 if self.y >= 0 else -1
        if (sing_y != t ) or (abs(self.y) <= self.threshold):
            # Actualizar los pesos del perceptrón
            self.perceptron_weights[0] = self.perceptron_weights[0] + t*1

            for i in range(1,self.global_history_size+1):
                self.perceptron_weights[i] +=  t * self.reg(self.global_history_table[-i])
        # Actualizar la historia global 
        if result == "T":
            self.global_history_table = self.global_history_table[-self.global_history_size+1:] + "1"
        else:
            self.global_history_table = self.global_history_table[-self.global_history_size+1:] + "0"    
        # Actualizar las estadísticas
       
        if result == "T" and prediction == "T":
            self.total_taken_pred_taken += 1
        elif result == "T" and prediction == "N":
            self.total_taken_pred_not_taken += 1
        elif result == "N" and prediction == "T":
                self.total_not_taken_pred_taken += 1
        elif result == "N" and prediction == "N":
            self.total_not_taken_pred_not_taken += 1
        self.total_predictions += 1

    def reg(self, bit):
        if bit == "1":
            return 1
        elif bit == "0":
            return -1