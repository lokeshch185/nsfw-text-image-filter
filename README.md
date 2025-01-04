# NSFW Content Classifier

This project provides a web service that allows users to classify both text and images for NSFW (Not Safe For Work) content. It uses the Hugging Face Transformers library for text classification and a pre-trained model for image classification.

## Features

- **Text Classification**: Classifies a given text and identifies whether it's NSFW or not using a pre-trained model.
- **Image Classification**: Classifies a given image and detects NSFW content using an image classification model.
- **REST API**: Exposes two endpoints for text and image classification.

## Technologies Used

- **Flask**: Lightweight web framework for building the API.
- **Transformers**: Hugging Face library for loading pre-trained models for text and image classification.
- **PIL (Pillow)**: Library for handling image processing.
- **Python**: The core programming language used for development.

## Prerequisites

Before you start, ensure you have the following installed on your system:

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/nsfw-classifier.git
   cd nsfw-classifier
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the Flask server**:

   Run the following command to start the Flask application:

   ```bash
   python main.py
   ```

   The server will be running locally on `http://127.0.0.1:5000`.

2. **Endpoints**:

   - **Classify Text**:
     - **URL**: `/classify-text`
     - **Method**: `POST`
     - **Request**: JSON with the text field:
       ```json
       {
         "text": "Your text content here"
       }
       ```
     - **Response**: JSON with classification result:
       ```json
       [
         {
           "label": "NSFW",
           "score": 0.98
         }
       ]
       ```

   - **Classify Image**:
     - **URL**: `/classify-image`
     - **Method**: `POST`
     - **Request**: A multipart/form-data request with the image file:
       ```bash
       curl -X POST -F "image=@path_to_image.jpg" http://127.0.0.1:5000/classify-image
       ```
     - **Response**: JSON with classification result:
       ```json
       [
         {
           "label": "NSFW",
           "score": 0.97
         }
       ]
       ```

## Error Handling

- If the `text` field is missing in the `/classify-text` request, you will receive a 400 error:
  ```json
  {
    "error": "Missing 'text' field in request."
  }
  ```

- If no image is provided in the `/classify-image` request, you will receive a 400 error:
  ```json
  {
    "error": "No image file provided."
  }
  ```

- For any unexpected errors, the server will return a 500 error with the error message:
  ```json
  {
    "error": "An error occurred: <error_message>"
  }
  ```

## Models Used

- **Text Classifier**: `eliasalbouzidi/distilbert-nsfw-text-classifier`
- **Image Classifier**: `Falconsai/nsfw_image_detection`

These models are pre-trained and available from the Hugging Face Model Hub.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License.