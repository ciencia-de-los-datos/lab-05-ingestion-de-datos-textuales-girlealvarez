import pandas as pd
import os

# Función para leer archivos de texto y extraer las frases y sentimientos
def read_files_and_generate_dataframe(directory):
    phrases = []
    sentiments = []

    # Recorrer los subdirectorios en el directorio dado
    for subdir in os.listdir(directory):
        subdirectory = os.path.join(directory, subdir)
        if os.path.isdir(subdirectory):
            # Recorrer los archivos en el subdirectorio
            for file in os.listdir(subdirectory):
                if file.endswith(".txt"):
                    # Leer el archivo de texto
                    with open(os.path.join(subdirectory, file), "r", encoding="utf-8") as f:
                        # Leer cada línea como una frase
                        for line in f:
                            phrases.append(line.strip())  # Eliminar espacios en blanco al inicio y al final
                            # El sentimiento se determina por el nombre del subdirectorio
                            sentiment = subdir
                            sentiments.append(sentiment)

    # Crear un DataFrame
    df = pd.DataFrame({"phrase": phrases, "sentiment": sentiments})
    return df

# Directorio donde se encuentran los datos de entrenamiento y prueba
train_directory = "data/train"
test_directory = "data/test"

# Leer los datos de entrenamiento y prueba y crear DataFrames
train_df = read_files_and_generate_dataframe(train_directory)
test_df = read_files_and_generate_dataframe(test_directory)

# Imprimir los DataFrames para verificar si contienen datos
print("DataFrame de entrenamiento:")
print(train_df.head())
print("\nDataFrame de prueba:")
print(test_df.head())

# Contar el número de frases para cada categoría de sentimiento en el DataFrame de entrenamiento
train_sentiment_counts = train_df['sentiment'].value_counts()

# Contar el número de frases para cada categoría de sentimiento en el DataFrame de prueba
test_sentiment_counts = test_df['sentiment'].value_counts()

print("\nNúmero de frases por categoría de sentimiento en el DataFrame de entrenamiento:")
print(train_sentiment_counts)
print("\nNúmero de frases por categoría de sentimiento en el DataFrame de prueba:")
print(test_sentiment_counts)

# Guardar los DataFrames en archivos CSV
train_df.to_csv("train_dataset.csv", index=False)
test_df.to_csv("test_dataset.csv", index=False)






