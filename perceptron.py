class perceptron:
    def __init__(self, num_features):
        # Inicialización de pesos y sesgo
        self.num_features = num_features        # Numero de caracteristicas que tendra el percertron
        self.weights = [0] * num_features       # Inicializando pesos
        self.bias = 0
        
        # Inicialización de estadísticas
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

    def print_info(self):
        # Información sobre el predictor
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\tPerceptron")

    def print_stats(self):
        # Estadísticas de la simulación
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
        # Predicción basada en el producto punto de pesos y PC
        dot_product = sum(w*f for w, f in zip(self.weights, PC)) + self.bias
        return "T" if dot_product > 0 else "N"

    def update(self, PC, result, prediction):
        # Actualización de estadísticas
        if result == "T" and prediction == "T":
            self.total_taken_pred_taken += 1
        elif result == "T" and prediction == "N":
            self.total_taken_pred_not_taken += 1
        elif result == "N" and prediction == "T":
            self.total_not_taken_pred_taken += 1
        elif result == "N" and prediction == "N":
            self.total_not_taken_pred_not_taken += 1
    
        self.total_predictions += 1

        # Actualización de pesos y sesgo si la predicción fue incorrecta
        if result != prediction:
            for i in range(self.num_features):
                self.weights[i] += PC[i] if result == "T" else -PC[i]
            self.bias += 1 if result == "T" else -1
