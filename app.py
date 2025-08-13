﻿import os
from flask import Flask, jsonify
app = Flask(__name__)
@app.get("/")
def hello():
    return jsonify(message="¡Hola Mundo desde Flask + Docker! 🚀")
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
