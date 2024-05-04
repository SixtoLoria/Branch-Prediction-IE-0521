# Branch-Prediction-IE-0521

**Estudiantes:** 
- Edwin Camacho Mora B21304
- Sixto Loría Villagra C04417

## Instrucciones para correr el código de cada branch prediction.

### Para correr los codigos del P-share y del perceptron

Escriba en su terminal el comando: **python3 branch_predictor.py -n 4 --bp 2 -g 2**

Para Windows seria usar: python branch_predictor.py -n 4 --bp 2 -g 2 

Donde:
- **-n:** Numero de Bits del PC para indexar
- **-bp:** Predictor de saltos que desea utilizar: 2 para el P-share, 3 para el perceptron 
- **-g:** Tamaño de la historia global

Alterne entre esos valores según sea el caso que desee.


### Para correr el código para branch predictor propuesto Ie0521 

Para correr el codigo propuesto que en nuestro caso es un torneo entre el P-share
y el perceptron (P-share Vs perceptron). Intrese el siguiente comando en la terminal. 

- **python3 branch_predictor.py -n 9 –bp 4 -g 7**

- Para Windows usar: python branch_predictor.py -n 9 –bp 4 -g 7

Con este comando se seleccionan los valores correspondientes para correr correctamente
el predictor propuesto considerando el margen de presupuesto de 32Kb.

Nota: Recuerde siempre estar en el directorio en donde esten los archivos.
Nota2: las pruebas fueron hechas en linux, porfavor probarlo también ahi si es posible



