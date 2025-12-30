from flask import Flask, request, jsonify
from LLaMA import Main_Pipeline

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return {"status": "ok"}


@app.route("/inference", methods=["POST"])
def inference():
    data = request.get_json()
    print(data)
    result = Main_Pipeline(data['medical_record'])
    return {'response': result}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)