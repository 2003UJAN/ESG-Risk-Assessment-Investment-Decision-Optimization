from transformers import pipeline
import os

# Load BERT sentiment model
sentiment_pipeline = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_esg_sentiment(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    result = sentiment_pipeline(text[:512])  # Limit to 512 tokens
    return result

# Example usage
file_path = "data/infosys_esg.txt"
if os.path.exists(file_path):
    sentiment = analyze_esg_sentiment(file_path)
    print(f"ESG Sentiment for ExampleCorp: {sentiment}")
