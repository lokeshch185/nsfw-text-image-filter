from PIL import Image
from transformers import pipeline

img = Image.open('./normal1.jpg')
classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
print(classifier(img))

pipe = pipeline("text-classification", model="eliasalbouzidi/distilroberta-nsfw-text-classifier")
print(pipe("I love porn"))
