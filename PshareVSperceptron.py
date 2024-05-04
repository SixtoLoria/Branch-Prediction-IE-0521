from perceptron import *       # Importanción de lo spredictores para usar variables internas
from pshared import *       

class PshareVSperceptron:
    def __init__(self, bits_to_index, global_history_size):  #Se traen las variables de los predictores GShared y PShared.
        self.bits_to_index = bits_to_index
        self.global_history_size = global_history_size        #Esta variable pertenece al GShared
                #Esta variable pertenece al PShared
        self.predictor_count = 0
        self.perceptron_global = perceptron(bits_to_index,global_history_size) #Se utiliza para poder la respectiva comparación con el pshared.
        self.pshare_local = pshared(bits_to_index,global_history_size)   #Se utiliza para poder la respectiva comparación con el perceptron.
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0
    #Información de los predictores pshare, perceptron y PshareVsPerceptron
    def print_info(self):
        print("Parámetros del predictor:")
        print("Tipo de predictor: PshareVSperceptron")
        print("Sobre el predictor Global:")
        print("\tEntradas del predictor global:\t\t\t\t\t"+str(2**self.bits_to_index))
        print("\tTamaño de los registros de historia global:\t\t\t"+str(self.global_history_size))
        print("Sobre el predictor Local:")
        print("\tEntradas en el History Table:\t\t\t\t\t"+str(2**self.bits_to_index))
        print("\tTamaño de los registros de historia local:\t\t\t"+str(self.global_history_size))
        print("\tEntradas en el Pattern Table: \t\t\t\t\t"+ str(2**self.global_history_size))
        
   #Se imprimen las estadisticas  
    def print_stats(self):
        print("Resultados de la simulación")
        print("\t# branches:\t\t\t\t\t\t"+str(self.total_predictions))
        print("\t# branches tomados predichos correctamente:\t\t"+str(self.total_taken_pred_taken))
        print("\t# branches tomados predichos incorrectamente:\t\t"+str(self.total_taken_pred_not_taken))
        print("\t# branches no tomados predichos correctamente:\t\t"+str(self.total_not_taken_pred_not_taken))
        print("\t# branches no tomados predichos incorrectamente:\t"+str(self.total_not_taken_pred_taken))
        perc_correct = 100*(self.total_taken_pred_taken+self.total_not_taken_pred_not_taken)/self.total_predictions
        formatted_perc = "{:.3f}".format(perc_correct)
        print("\t% predicciones correctas:\t\t\t\t"+str(formatted_perc)+"%")

    def predict_and_update(self, PC, result):
        #Obtención de las prediciones obtenidas por cada metodo
        predict_pshare_local = self.pshare_local.predict(PC)     
        predict_perceptron_global = self.perceptron_global.predict(PC)   

        #Determina que predictor es el que va a seguir utilizandose.
        #Se usa un contador, para determinar las condiciones donde se va a sumar o restar. 
        #Si el contador esta en el intervalo de 0 a 1 , la variable prediction es ahora pshare_loca, sino el perceptron_global.
        if self.predictor_count in [0,1]:    
            prediction = predict_pshare_local             
        else:
            prediction = predict_perceptron_global
   
        #A continuación se hace actualización dependiendo del resultado del predictor.
        self.pshare_local.update(PC,result, predict_pshare_local)
        self.perceptron_global.update(PC,result, predict_perceptron_global)
        #Se evalua  si el predic  del psahre_local es igual a result
        #result y si perceptron_global es diferente de result, se comprueba si el contador es distinto de 0 
        # el salto no se toma y el contador va a restar 1.
        if predict_pshare_local == result and predict_perceptron_global != result:
            if self.predictor_count !=0:
                self.predictor_count -= 1 
        #Si self.predict_pshare_local  es distinto de result y self.predict_perceptron_global igual que result 
        #Entonces si el contador es distinta a tomado (por eso un 3), de ser así, el contador suma una unidad.
        elif predict_pshare_local != result and predict_perceptron_global == result:
            if self.predictor_count !=3:
                self.predictor_count += 1 

        #Update stats
        # La misma lógica que se usa en bimodal
        if result == "T" and result == prediction:
            self.total_taken_pred_taken += 1
        elif result == "T" and result != prediction:
            self.total_taken_pred_not_taken += 1
        elif result == "N" and result == prediction:
            self.total_not_taken_pred_not_taken += 1
        else:
            self.total_not_taken_pred_taken += 1

        self.total_predictions += 1