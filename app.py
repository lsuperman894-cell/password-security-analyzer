
from flask import Flask, render_template
import os

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY", "development-only-change-before-deployment"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "online"}

if __name__ == "__main__":
    app.run(debug=True)
  
