# Crear una cadena de texto de ejemplo
text = "Hello, World! sss"

# Abrir un archivo de texto en modo escritura
with open('example.txt', 'w') as file:
    # Escribir la cadena de texto en el archivo
    file.write(text+'\n')
    file.write(text)

with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()