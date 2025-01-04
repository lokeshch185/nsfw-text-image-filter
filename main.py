from flask import Flask, request, jsonify
from transformers import pipeline
from PIL import Image

app = Flask(__name__)

text_pipeline = pipeline("text-classification", model="eliasalbouzidi/distilbert-nsfw-text-classifier")
image_pipeline = pipeline("image-classification", model="Falconsai/nsfw_image_detection")

@app.route("/classify-text", methods=["POST"])
def classify_text():
    try:
        data = request.get_json()
        if "text" not in data:
            return jsonify({"error": "Missing 'text' field in request."}), 400
        text = data["text"]
        result = text_pipeline(text)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/classify-image", methods=["POST"])
def classify_image():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided."}), 400

        image_file = request.files["image"]
        image = Image.open(image_file.stream)

        result = image_pipeline(image)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
