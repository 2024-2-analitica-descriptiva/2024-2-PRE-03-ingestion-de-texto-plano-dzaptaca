"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    import pandas as pd

    # Ruta al archivo de entrada
    file_path = "files/input/clusters_report.txt"

    # Listas para almacenar los datos procesados
    clusters = []
    cantidad_palabras = []
    porcentajes = []
    palabras_clave = []

    # Abrir y procesar el archivo
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Procesar cada línea del archivo
    palabras_clave_temp = []
    for i, line in enumerate(lines):
        # Omitir encabezados y separadores
        if i < 4 or line.startswith('-'):
            continue

        try:
            # Intentar convertir los primeros caracteres en un número
            cluster_num = int(line.strip()[:3])
            # Si tenemos palabras clave acumuladas, guardarlas antes de continuar
            if palabras_clave_temp:
                palabras_clave.append(" ".join(palabras_clave_temp).strip())
                palabras_clave_temp = []
            
            # Extraer datos del cluster actual
            parts = lines[i].split()
            clusters.append(int(parts[0]))
            cantidad_palabras.append(int(parts[1]))
            porcentajes.append(float(parts[2].replace(",",".")))
            palabras_clave_temp.append((" ".join(parts[4:])).replace("  "," ").strip())
        except ValueError:
            # Si no es un número, acumular palabras clave
            palabras_clave_temp.append(line.strip())

    # Añadir las últimas palabras clave acumuladas
    if palabras_clave_temp:
        palabras_clave.append(" ".join(palabras_clave_temp).strip())

    # Verificar que todas las listas tengan la misma longitud
    ##assert len(clusters) == len(cantidad_palabras) == len(porcentajes) == len(palabras_clave), \
        ##"Las listas no tienen la misma longitud."

    # Crear el DataFrame
    df = pd.DataFrame({
        "cluster": clusters,
        "cantidad_de_palabras_clave": cantidad_palabras,
        "porcentaje_de_palabras_clave": porcentajes,
        "principales_palabras_clave": palabras_clave
    })
    def transformar_palabras_clave(palabras_clave):
        # Reemplazar puntos y dividir por coma y espacio
        palabras = palabras_clave.replace(".", "").replace("  "," ").replace("   "," ").strip().split(", ")
        
        # Crear una lista con coma y espacio en todos los elementos excepto el último
        palabras_con_coma = [el.strip() + ", " for el in palabras[:-1]] + [palabras[-1]]  # Último elemento sin coma
        
        # Convertir la lista en una tupla
        return ("".join((palabras_con_coma)).replace("  "," "))

    # Aplicar la transformación a toda la columna
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(transformar_palabras_clave)

    return(df)

if __name__ == "__main__":
    print(pregunta_01())

    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
