from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def mostrar_resultados():
    # Define tus datos aquí dentro de la función
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

    df = pd.DataFrame(inversiones)

    # Aplica formateo a las columnas
    df = formatear_columnas(df)
    
    # Ordena el DataFrame por rentabilidad anual esperada
    df = ordenar_por_rentabilidad(df)

    # Pasa esta información a la plantilla
    return render_template('resultado.html', df=df.to_html(classes='dataframe'))

def formatear_columnas(df):
    # Formatea las columnas "rendimiento_historico" y "rentabilidad_anual_esperada" como porcentajes
    df['rendimiento_historico'] = (df['rendimiento_historico'] * 100).apply(lambda x: f"{x:.2f}%")
    df['rentabilidad_anual_esperada'] = (df['rentabilidad_anual_esperada'] * 100).apply(lambda x: f"{x:.2f}%")
    
    # Formatea la columna "inversion_minima" como moneda
    df['inversion_minima'] = df['inversion_minima'].apply(lambda x: f"${x:,.0f}")  # Sin decimales
    
    return df

def ordenar_por_rentabilidad(df):
    # Elimina el signo de porcentaje y convierte la columna "rentabilidad_anual_esperada" a valores numéricos
    df['rentabilidad_anual_esperada'] = df['rentabilidad_anual_esperada'].str.rstrip('%').astype(float)
    
    # Ordena el DataFrame por rentabilidad anual esperada en orden descendente
    df = df.sort_values(by='rentabilidad_anual_esperada', ascending=False)
    
    return df

if __name__ == '__main__':
    app.run(debug=True)
