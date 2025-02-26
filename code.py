# Función para unir los nombres y apellidos
def unir_nombres_apellidos(columnas):
    email_idx = next((i for i, v in enumerate(columnas) if '@' in v), len(columnas) - 1)
    columnas[1:email_idx] = [' '.join(columnas[1:email_idx])]
    return columnas  # Devolvemos la columna modificada

# Función para generar la línea con el número adecuado de columnas
def generar_linea(columnas, max_columnas):
    id_ = columnas[0]
    email_idx = next((i for i, v in enumerate(columnas) if '@' in v), len(columnas) - 1)
    nombre_completo = columnas[1]
    email = columnas[email_idx]
    extra_data = columnas[email_idx + 1:]
 
    nueva_linea = f"{id_};{nombre_completo};{email};" + ";".join(extra_data)
    num_actual_columnas = nueva_linea.count(";") + 1 
    
    # Añadimos los puntos y comas necesarios
    if num_actual_columnas < max_columnas:
        nueva_linea += ";" * (max_columnas - num_actual_columnas)
    
    return nueva_linea

# Leemos el archivo csv
with open('file.csv', 'r', encoding='utf-8') as f_in:
    lineas = [linea.strip().split(';') for linea in f_in.readlines()]

# Unimos los nombres y apellidos
lineas = [unir_nombres_apellidos(columnas) for columnas in lineas]

# Calculamos el número máximo de columnas
max_columnas = max(len(linea) for linea in lineas)

# Definimos los colores para impresión
BLACK_GREEN = "\033[30;42m"
RED_GREEN = "\033[31;42m"
RESET = "\033[0m"

# Escribimos las líneas modificas en el nuevo archivo
with open('output_file.csv', 'w', encoding='utf-8') as f_out:
    for columnas in lineas:
        nueva_linea = generar_linea(columnas, max_columnas)
        num_puntos_comas = nueva_linea.count(';')

        # Imprimimos la línea con los colores por terminal
        print(f"{BLACK_GREEN}{nueva_linea}{RED_GREEN}{num_puntos_comas}{RESET}") 

        # Escribimos la línea modificada en el fichero
        f_out.write(nueva_linea + "\n")
    