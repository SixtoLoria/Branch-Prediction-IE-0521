import matplotlib.pyplot as plt

fig, ax = plt.subplots()
Combinacion = ['H2-PC4', 'H2-PC8', 'H2-PC12', 'H2-PC16', 'H2-PC20', 
        'H6-PC4', 'H6-PC8', 'H6-PC12', 'H6-PC16', 'H6-PC20',
        'H8-PC4', 'H8-PC8', 'H8-PC12', 'H8-PC16', 'H8-PC20',
        'H16-PC4', 'H16-PC8', 'H16-PC12', 'H16-PC16', 'H16-PC20',
        'H20-PC4', 'H20-PC8', 'H20-PC12', 'H20-PC16', 'H20-PC20']
prediction_percentage = {'Pshare':[2,3,16,15,28.5, 30.5, 31, 30, 28, 27.5, 5, 8.5,36,12,18,25.5, 26.5, 25, 26.5,30.5,30, 28, 27.5, 30.5,1],
                         'Perceptron':[24.5, 8.5,36,12,18,25.5, 26.5, 25, 26.5,2,3,16,15,28.5, 30.5, 31, 30, 28, 27.5, 24.5, 25,30, 28, 27.5, 30.5]}
ax.plot(Combinacion, prediction_percentage['Pshare'],label="Pshare")
ax.plot(Combinacion, prediction_percentage['Perceptron'],label="Perceptron")
ax.set_title('Curvas de los porcentajes de predicción', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
plt.xlabel('Combinaciones entre Hitorial Global y Bits PC')
plt.xticks(rotation=90)# Ajusta la rotación de las etiquetas del eje x
plt.tight_layout()  # Ajusta los márgenes del gráfico para evitar que las etiquetas se corten
plt.ylabel('Porcentajes de precisión (%)')
plt.legend()
plt.show()