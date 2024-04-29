import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Supongamos que tienes un DataFrame llamado 'datos' con las columnas: 'cigarrillos_por_dia', 'duracion_habito', 'cancer_de_pulmon'

# Cargar datos
# Por ejemplo, aquí creamos un DataFrame de ejemplo
datos = pd.DataFrame({
    'cigarrillos_por_dia': [10, 20, 5, 15, 8, 12, 7, 25, 30, 40],
    'duracion_habito': [5, 10, 3, 8, 6, 7, 4, 12, 15, 20],
    'cancer_de_pulmon': [1, 1, 0, 1, 0, 1, 0, 1, 1, 1]  # 1 para sí desarrollaron cáncer, 0 para no
})

# Separar datos en características (variables independientes) y etiquetas (variable dependiente)
X = datos[['cigarrillos_por_dia', 'duracion_habito']]
y = datos['cancer_de_pulmon']

# Dividir datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar un modelo de regresión logística
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = modelo.predict(X_test)
print(f"y_pred: {y_pred} ")
# Calcular la precisión del modelo
precision = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", precision)
