from flask import Flask, request, render_template_string
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")
NAMES = ["setosa", "versicolor", "virginica"]

PAGE = """
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ML Model on AWS</title>
  <style>
    body { font-family: Arial, sans-serif; background:#eef2f7; text-align:center; padding:50px 20px; }
    .card { max-width:500px; margin:auto; padding:30px; background:white; border-radius:12px; box-shadow:0 4px 16px #0002; }
    h1 { color:#1565c0; }
    input { width:80%; padding:8px; margin:6px 0; }
    button { padding:10px 24px; background:#1565c0; color:white; border:none; border-radius:6px; cursor:pointer; }
    .result { margin-top:20px; font-size:20px; color:#2e7d32; font-weight:bold; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Iris Flower Predictor</h1>
    <p>Docker + GitHub + CodePipeline + CodeDeploy</p>
    <p>Version: 1.0</p>
    <form method="post">
      <input name="sl" type="number" step="0.1" placeholder="Sepal length (cm)" required><br>
      <input name="sw" type="number" step="0.1" placeholder="Sepal width (cm)" required><br>
      <input name="pl" type="number" step="0.1" placeholder="Petal length (cm)" required><br>
      <input name="pw" type="number" step="0.1" placeholder="Petal width (cm)" required><br><br>
      <button type="submit">Predict</button>
    </form>
    {% if result %}<div class="result">{{ result }}</div>{% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        vals = [float(request.form[k]) for k in ("sl", "sw", "pl", "pw")]
        idx = int(model.predict([vals])[0])
        conf = model.predict_proba([vals])[0][idx] * 100
        result = f"{NAMES[idx]} ({conf:.1f}% confidence)"
    return render_template_string(PAGE, result=result)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
