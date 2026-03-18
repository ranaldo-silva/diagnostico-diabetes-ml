from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Carrega o modelo treinado (Random Forest - Acurácia: 75.32%)
# O arquivo modelo_diabetes.pkl deve estar na mesma pasta
with open("modelo_diabetes.pkl", "rb") as f:
    modelo = pickle.load(f)

app = Flask(__name__)

# Mapeamento dos resultados numéricos para labels legíveis
CLASSES = {
    0: "Negativo para Diabetes",
    1: "Positivo para Diabetes"
}

@app.route("/predict", methods=["POST"])
def predict():
    """
    Endpoint de predição.
    Recebe um JSON com os 8 atributos biomédicos e retorna o diagnóstico.

    Exemplo de body:
    [
        {
            "Pregnancies": 6,
            "Glucose": 148,
            "BloodPressure": 72,
            "SkinThickness": 35,
            "Insulin": 0,
            "BMI": 33.6,
            "DiabetesPedigreeFunction": 0.627,
            "Age": 50
        }
    ]
    """
    dados = request.json
    df = pd.DataFrame(dados)
    pred = modelo.predict(df)

    return jsonify({
        "predicao": pred.tolist(),
        "diagnostico": [CLASSES[int(p)] for p in pred]
    })

@app.route("/", methods=["GET"])
def health():
    """Endpoint de verificação de status da API."""
    return jsonify({
        "status": "ok",
        "message": "API de diagnóstico de Diabetes rodando!",
        "modelo": "Random Forest",
        "acuracia": "75.32%"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
