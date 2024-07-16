# Sentiment Analysis using BERT and Hugging Face Transformers

## Overview
This project aims to perform sentiment analysis using the BERT model and Transformers by Hugging Face. The project includes the following key components:
- Scraping data from Google Play
- Preprocessing the data
- Building and training a sentiment classifier
- Creating a REST API for sentiment analysis

## Setup and Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/CruiseDevice/Sentiment-Analysis-using-BERT.git
   cd sentiment_analyzer
   ```

2. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Download and prepare the pre-trained model:**
    Ensure the best_model_state.bin is placed in the ./models directory or adjust the path in config.json.

## Running the API

To run the API, use the following command:
```sh
uvicorn sentiment_analyzer.api:app --reload
```
This will start the server on http://localhost:8000.

## Testing the API Endpoint

You can test the API endpoint using the following URL: http://localhost:8000/predict`

## Request Body

To predict the sentiment of a text, send a POST request with the following JSON body:

```json
{
    "text": "This app is a total waste of time!"
}
```

## Sanple output

The API will respond with a JSON object containing the predicted sentiment, the confidence score, and the probabilities for each sentiment class:
```json
{
    "sentiment": "negative",
    "confidence": 0.9952511787414551,
    "probabilities": {
        "negative": 0.9952511787414551,
        "neutral": 0.0025495770387351513,
        "positive": 0.002199336187914014
    }
}
```