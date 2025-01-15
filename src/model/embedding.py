from src.conf import configuration

import openai
openai.api_key = configuration.api_key
# Set your OpenAI API key

# Function to get embeddings
def get_embeddings(text):
    response = openai.Embedding.create(
        model="text-embedding-3-small",
        input=text
    )
    return response['data'][0]['embedding']

