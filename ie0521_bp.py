class ie0521_bp:
    def __init__(self):
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0
        self.branch_history_table = {}  # Tabla para almacenar el historial de las predicciones
        

    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\tPredictor de bifurcación de dos bits")

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
        if PC not in self.branch_history_table:
            return "T"  # Predice que se tomará si no hay historial
        elif self.branch_history_table[PC] > 1:
            return "T"  # Predice que se tomará si el contador es 2 o 3
        else:
            return "N"  # Predice que no se tomará si el contador es 0 o 1
  

    def update(self, PC, result, prediction):
        if PC not in self.branch_history_table:
            self.branch_history_table[PC] = 2 if result == "T" else 0
        else:
            if result == "T":
                if self.branch_history_table[PC] < 3:
                    self.branch_history_table[PC] += 1
            else:
                if self.branch_history_table[PC] > 0:
                    self.branch_history_table[PC] -= 1

        self.total_predictions += 1
        if result == "T":
            if prediction == "T":
                self.total_taken_pred_taken += 1
            else:
                self.total_taken_pred_not_taken += 1
        else:
            if prediction == "T":
                self.total_not_taken_pred_taken += 1
            else:
                self.total_not_taken_pred_not_taken += 1
