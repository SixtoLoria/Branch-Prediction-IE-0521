class pshared:
    def __init__(self,bits_to_index, global_history_size):
        #Escriba aquí el init de la clase
        self.bits_to_index = bits_to_index     #Bits del PC
        self.global_history_size = global_history_size #bits de los registros de la tabla de historia global
        self.size_global_history_table = 2**global_history_size #Tamaño de la tabla global
        self.size_of_branch_table = 2**bits_to_index #Tamaño de la tabla del branch
        
        # Crear la tabla de ramas (branch table) con registros del tamaño de la historia global inicializados en ceros
        self.branch_table = [0 for i in range(self.size_of_branch_table)]
        self.global_history_table = [0 for i in range(self.size_global_history_table)]
        

        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\tP-Share")
        print("\tTamaño de la tabla de patrones:\t" + str(self.size_of_branch_table))
        print("\tTamaño del registro de historia global:\t" + str(self.global_history_size))
        print("\tTamaño de la tabla de la historia global:\t" + str(self.size_global_history_table))

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
        index = int(PC) % self.size_of_branch_table
        branch_table_entry = self.branch_table[index]
        global_table_entry = self.global_history_table[branch_table_entry]
        if global_table_entry in [2,3]:
            return "T"
        else:
            return "N"

    def update(self, PC, result,prediction):
        index = int(PC) % self.size_of_branch_table
        branch_table_entry = self.branch_table[index]
        global_table_entry = self.global_history_table[branch_table_entry]

        # Update table
        if (result == "N" and global_table_entry != 0 ):
            updated_global_table_entry = global_table_entry - 1
        
                       
        elif (result == "T" and global_table_entry ==3):
            updated_global_table_entry = global_table_entry

        elif (result == "N" and global_table_entry == 0):

            updated_global_table_entry = global_table_entry
        else:
            updated_global_table_entry = global_table_entry + 1
        #Actualizo la tabla de historia global con los resultados anteriores
        self.global_history_table[branch_table_entry] = updated_global_table_entry 

        # Update stats
    #Update stats
        if result == "T" and result == prediction:
            self.total_taken_pred_taken += 1
            self.branch_table[index] =self.branch_table[index] << 1
            self.branch_table[index] += 1

        elif result == "T" and result != prediction:
            self.total_taken_pred_not_taken += 1
            self.branch_table[index] =self.branch_table[index] << 1
            self.branch_table[index] += 1

        elif result == "N" and result == prediction:
            self.total_not_taken_pred_not_taken += 1
            self.branch_table[index] =self.branch_table[index] << 1
            

        else:
            self.total_not_taken_pred_taken += 1
            self.branch_table[index] =self.branch_table[index] << 1

        self.total_predictions += 1
        self.branch_table[index]=self.branch_table[index]%self.size_global_history_table
 