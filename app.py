from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Lista inicial de inversiones
inversiones = [
    {
        "nombre": "TechCorp",
        "rendimiento_historico": 0.08,
        "inversion_minima": 10000,
        "calificacion_riesgo": 3,
        "rentabilidad_anual_esperada": 0.07
    },
    {
        "nombre": "InnovaSoft",
        "rendimiento_historico": 0.10,
        "inversion_minima": 20000,
        "calificacion_riesgo": 4,
        "rentabilidad_anual_esperada": 0.09
    },
    {
        "nombre": "NanoTec",
        "rendimiento_historico": 0.20,
        "inversion_minima": 15000,
        "calificacion_riesgo": 2,
        "rentabilidad_anual_esperada": 0.19
    },
    {
        "nombre": "BioG",
        "rendimiento_historico": 0.30,
        "inversion_minima": 11000,
        "calificacion_riesgo": 1,
        "rentabilidad_anual_esperada": 0.11
    },
    {
        "nombre": "iTechSolutions",
        "rendimiento_historico": 0.15,
        "inversion_minima": 18000,
        "calificacion_riesgo": 3,
        "rentabilidad_anual_esperada": 0.12
    },
    {
        "nombre": "WebWizards",
        "rendimiento_historico": 0.12,
        "inversion_minima": 25000,
        "calificacion_riesgo": 2,
        "rentabilidad_anual_esperada": 0.10
    },
    {
        "nombre": "CloudEc",
        "rendimiento_historico": 0.18,
        "inversion_minima": 22000,
        "calificacion_riesgo": 4,
        "rentabilidad_anual_esperada": 0.15
    }
    # Puedes agregar más inversiones aquí si es necesario
]

# Convierte la lista de diccionarios a DataFrame
df = pd.DataFrame(inversiones)

def formatear_columnas(df):
    # Formatea la columna "rendimiento_historico" como porcentaje
    df['rendimiento_historico'] = (df['rendimiento_historico'] * 100).apply(lambda x: f"{x:.2f}%")
    
    # La columna "rentabilidad_anual_esperada" se deja como número para ordenarla
    return df

def ordenar_por_rentabilidad(df):
    # Ordena el DataFrame por rentabilidad anual esperada en orden descendente
    df = df.sort_values(by='rentabilidad_anual_esperada', ascending=False)

    # Después de ordenar, formatea la columna "rentabilidad_anual_esperada" como porcentaje
    df['rentabilidad_anual_esperada'] = df['rentabilidad_anual_esperada'].apply(lambda x: f"{x * 100:.2f}%")
    return df

@app.route('/', methods=['GET', 'POST'])
def mostrar_resultados():
    global df  # Usa la variable global df

    if request.method == 'POST':
        # Recoge los datos del formulario
        nueva_inversion = {
            "nombre": request.form['nombre'],
            "rendimiento_historico": float(request.form['rendimiento']) / 100,
            "inversion_minima": int(request.form['inversion_minima']),
            "calificacion_riesgo": int(request.form['riesgo']),
            "rentabilidad_anual_esperada": float(request.form['rentabilidad']) / 100
        }
        # Añade la nueva inversión a la lista y actualiza el DataFrame
        inversiones.append(nueva_inversion)
        df = pd.DataFrame(inversiones)

    # Formatea y ordena el DataFrame antes de pasarlo a la plantilla
    df_formateado = formatear_columnas(df.copy())
    df_ordenado = ordenar_por_rentabilidad(df_formateado)

    return render_template('resultado.html', df=df_ordenado.to_html(classes='dataframe', index=False))

if __name__ == '__main__':
        app.run(debug=True)