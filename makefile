Tarea1: PShare  Perceptron 
Pshare:
        		@echo Ingrese los parámetros para ejecutar el predictor PShare:\
        #@read -p "Número de bits para indexar: " bits_to_index && \
        read -p "Tamaño del registro de historia global: " global_history_size && \#
				python3 ./branch_predictor.py -n 2 --bp 2 -g 4

Perceptron:
        #@echo "Ingrese los parámetros para ejecutar el predictor Perceptron:"
       # @read -p "Número de bits para indexar: " bits_to_index && \
        read -p "Tamaño del registro de historia global: " global_history_size && \#
        #python3 ./branch_predictor.py -n $$bits_to_index --bp 3 -g $$global_history_size#
				python3 ./branch_predictor.py -n 2 --bp 3 -g 4