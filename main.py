from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

pipe = pipeline("text-classification", model="eliasalbouzidi/distilbert-nsfw-text-classifier")

@app.route("/classify", methods=["POST"])
def classify_text():
    try:
        data = request.get_json()
        if "text" not in data:
            return jsonify({"error": "Missing 'text' field in request."}), 400
        text = data["text"]
        result = pipe(text)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
