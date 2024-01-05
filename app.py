from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def mostrar_resultados():
    # Define tus datos aquí dentro de la función
    inversion_1 = {
        "nombre": "Empresa A",
        "rendimiento_historico": 0.08,
        "capitalizacion_mercado": 500e6,
        "calificacion_riesgo": 3
    }

    inversion_2 = {
        "nombre": "Empresa B",
        "rendimiento_historico": 0.10,
        "capitalizacion_mercado": 800e6,
        "calificacion_riesgo": 4
    }

    df = pd.DataFrame([inversion_1, inversion_2])

    mejor_rendimiento = df[df['rendimiento_historico'] == df['rendimiento_historico'].max()]['nombre'].iloc[0]

    # Asegúrate de pasar la variable df a render_template
    return render_template('resultado.html', df=df.to_html(classes='dataframe'), mejor_rendimiento=mejor_rendimiento)

if __name__ == '__main__':
    app.run(debug=True)
