class ie0521_bp:
    def __init__(self, bits_to_index, global_history_size):
        self.bits_to_index = bits_to_index
        self.global_history_size = global_history_size
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0
        self.predictor_table = [2] * (2 ** bits_to_index)  # Inicializa la tabla con un sesgo hacia la toma

    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\tPredictor de bifurcación basado en contador saturado de dos bits")
        print("\tBits de PC para indexar:\t\t\t" + str(self.bits_to_index))
        print("\tTamaño del registro de historia global:\t\t" + str(self.global_history_size))

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
        # Convierte PC a un entero si es un string
        if isinstance(PC, str):
            PC = int(PC)

        index = PC & (len(self.predictor_table) - 1)
        return "T" if self.predictor_table[index] >= 2 else "N"

    def update(self, PC, result, prediction):
        # Convierte PC a un entero si es un string
        if isinstance(PC, str):
            PC = int(PC)
        index = PC & (len(self.predictor_table) - 1)
        if result == "T":
            self.predictor_table[index] = min(self.predictor_table[index] + 1, 3)
        else:
            self.predictor_table[index] = max(self.predictor_table[index] - 1, 0)

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