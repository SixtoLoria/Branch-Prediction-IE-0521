class pshared:
    def __init__(self, bits_to_index, local_history_size):
        #Escriba aquí el init de la clase
        self.bits_to_index = bits_to_index                                          # bimodal, bits de entrada.
        self.size_of_branch_table = 2**bits_to_index                                # bimodal
        self.local_history_size= local_history_size                                 # bit de entrada
        self.size_of_local_history= 2**local_history_size                           # Tamaño de la tabla, 2^m
        self.branch_table = [0 for i in range(self.size_of_branch_table)]           # Segunda tabla, tamaño de la tabla de la historia local. 
        self.branch_table_patrones=[0 for i in range(self.size_of_local_history)]   # Tercer tabla.
        
        self.local_history = 0
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0
    # Informacion a imprimir.
    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\tP-shared")
        print("\tEntradas en el History table:\t\t\t\t\t"+str(2**self.bits_to_index))
        print("\tTamaño de los registros de historia local:\t\t\t"+str(self.local_history_size))
        print("\tEntradas en el pattern table:\t\t\t\t\t"+str(2**self.local_history_size))

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

    def predict(self, PC):
        #Escriba aquí el código para predecir
        #La siguiente línea es solo para que funcione la prueba
        #Quítela para implementar su código
        return "T"
  

    def update(self, PC, result, prediction):
        #Escriba aquí el código para actualizar
        #La siguiente línea es solo para que funcione la prueba
        #Quítela para implementar su código
        a = PC
