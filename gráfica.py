import matplotlib.pyplot as plt


# Datos de la tabla
tamanio_historia = [2, 6, 8, 16, 20]
bits_4 = [71.496, 74.266, 74.783, 76.459, 77.019]
bits_8 = [84.303, 90.029, 91.282, 93.697, 94.154]
bits_12 = [90.859, 93.665, 94.306, 95.942, 96.242]
bits_16 = [91.466, 93.847, 94.445, 96.062, 96.369]
bits_20 = [91.480, 93.860, 94.455, 96.070, 96.377]

# Gráfico combinado
plt.figure(figsize=(10, 6))

plt.plot(tamanio_historia, bits_4, marker='o', label='Bits del PC = 4')
plt.plot(tamanio_historia, bits_8, marker='o', label='Bits del PC = 8')
plt.plot(tamanio_historia, bits_12, marker='o', label='Bits del PC = 12')
plt.plot(tamanio_historia, bits_16, marker='o', label='Bits del PC = 16')
plt.plot(tamanio_historia, bits_20, marker='o', label='Bits del PC = 20')

plt.title('Porcentaje de precisión del Perceptron variando los bits de Hiotoria')
plt.xlabel('Tamaño de historia')
plt.ylabel('Porcentaje de precisión')
plt.legend()
plt.grid(True)
plt.xticks(tamanio_historia)
plt.subplots_adjust(left=0.08, bottom=0.08, right=0.98, top=0.95)

# Guardar el gráfico como un archivo PDF
plt.savefig('grafico_perceptron.pdf')
plt.show()

# Datos de la nueva tabla (P-share)
tamanio_historia_pshare = [2, 6, 8, 16, 20]
bits_4_pshare = [66.836, 68.543, 69.710, 84.616, 87.913]
bits_8_pshare = [74.220, 76.427, 77.388, 85.820, 86.464]
bits_12_pshare = [84.939, 88.027, 89.109, 92.497, 92.391]
bits_16_pshare = [86.597, 89.488, 90.518, 93.507, 93.401]
bits_20_pshare = [86.692, 89.581, 90.589, 93.559, 93.447]

# Gráfico combinado solo para P-share
plt.figure(figsize=(10, 6))

plt.plot(tamanio_historia_pshare, bits_4_pshare, marker='o', label='Bits del PC = 4')
plt.plot(tamanio_historia_pshare, bits_8_pshare, marker='o', label='Bits del PC = 8')
plt.plot(tamanio_historia_pshare, bits_12_pshare, marker='o', label='Bits del PC = 12')
plt.plot(tamanio_historia_pshare, bits_16_pshare, marker='o', label='Bits del PC = 16')
plt.plot(tamanio_historia_pshare, bits_20_pshare, marker='o', label='Bits del PC = 20')

plt.title('Porcentaje de precisión del P-share variando los bits de Historia')
plt.xlabel('Tamaño de historia')
plt.ylabel('Porcentaje de precisión')
plt.legend()
plt.grid(True)
plt.xticks(tamanio_historia_pshare)
# Ajustar los márgenes
plt.subplots_adjust(left=0.08, bottom=0.08, right=0.98, top=0.95)

# Guardar el gráfico como un archivo PDF
plt.savefig('grafico_pshare.pdf')
plt.show()


# Datos de la tabla
tamanio_pc = [4, 8, 12, 16, 20]
bits_2 = [71.496, 84.303, 90.859, 91.466, 91.480]
bits_6 = [74.266, 90.029, 93.665, 93.847, 93.860]
bits_8 = [74.783, 91.282, 94.306, 94.445, 94.455]
bits_16= [76.459, 93.697, 95.942, 96.062, 96.070]
bits_20= [77.019, 94.154, 96.242, 96.369, 96.377]

# Gráfico combinado
plt.figure(figsize=(10, 6))

plt.plot(tamanio_pc, bits_2, marker='o', label='Bits de Historia = 2')
plt.plot(tamanio_pc, bits_6, marker='o', label='Bits de Historia = 6')
plt.plot(tamanio_pc, bits_8, marker='o', label='Bits de Historia = 8')
plt.plot(tamanio_pc, bits_16, marker='o', label='Bits de Historia = 16')
plt.plot(tamanio_pc, bits_20, marker='o', label='Bits de Historia= 20')

plt.title('Porcentaje de precisión del Perceptron variando los bits del PC ')
plt.xlabel('Tamaño de PC')
plt.ylabel('Porcentaje de precisión')
plt.legend()
plt.grid(True)
plt.xticks(tamanio_historia)
plt.subplots_adjust(left=0.08, bottom=0.08, right=0.98, top=0.95)

# Guardar el gráfico como un archivo PDF
plt.savefig('grafico_perceptron2.pdf')
plt.show()


# Datos de la tabla
tamanio_pc = [4, 8, 12, 16, 20]
bits_2 = [66.836, 74.220, 84.939, 86.597, 86.692]
bits_6 = [68.543, 76.427, 88.027, 89.488, 89.581]
bits_8 = [69.710, 77.388, 89.109, 90.518, 90.589]
bits_16= [84.616, 85.820, 92.497, 93.507, 93.559]
bits_20= [86.464, 87.913, 92.391, 93.401, 93.447]


# Gráfico combinado
plt.figure(figsize=(10, 6))

plt.plot(tamanio_pc, bits_2, marker='o', label='Bits de Historia = 2')
plt.plot(tamanio_pc, bits_6, marker='o', label='Bits de Historia = 6')
plt.plot(tamanio_pc, bits_8, marker='o', label='Bits de Historia = 8')
plt.plot(tamanio_pc, bits_16, marker='o', label='Bits de Historia = 16')
plt.plot(tamanio_pc, bits_20, marker='o', label='Bits de Historia= 20')

plt.title('Porcentaje de precisión del P-Share variando los bits del PC ')
plt.xlabel('Tamaño de PC')
plt.ylabel('Porcentaje de precisión')
plt.legend()
plt.grid(True)
plt.xticks(tamanio_historia)
plt.subplots_adjust(left=0.08, bottom=0.08, right=0.98, top=0.95)

# Guardar el gráfico como un archivo PDF
plt.savefig('grafico_pshare2.pdf')
plt.show()