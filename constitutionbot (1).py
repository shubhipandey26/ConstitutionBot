!pip install llama-index
!pip install google-generativeai
!pip install pinecone-client

!pip install llama-index-llms-gemini
!pip install llama-index-embeddings-gemini
!pip install llama-index-vector-stores-pinecone

import os
from pinecone import Pinecone
from llama_index.llms.gemini import Gemini
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import StorageContext, VectorStoreIndex, download_loader
from llama_index.core import Settings

GOOGLE_API_KEY = "google_api_key"
PINECONE_API_KEY = "pinecone_api_key"

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

llm = Gemini()
embed_model=GeminiEmbedding(model_name="models/embedding-001")
Settings.llm=llm
Settings.embed_model=embed_model
Settings.chunk_size=1024

pinecone_client = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

import os
from pinecone import Pinecone, ServerlessSpec, Index

# Step 1: Create an instance of the Pinecone class
pinecone_client = Pinecone(
    api_key="pinecone_api_key"  # Replace with your API key
)

# Step 2: Check if the index already exists
index_name = "cbotindex"
if index_name not in pinecone_client.list_indexes().names():
    # Step 3: Create the index
    pinecone_client.create_index(
        name=index_name,
        dimension=128,  # Set the vector dimension
        metric="cosine",  # Set the distance metric
        spec=ServerlessSpec(
            cloud="aws",  # Cloud provider
            region="us-east-1"  # Region
        )
    )
    print(f"Index '{index_name}' created successfully!")
else:
    print(f"Index '{index_name}' already exists.")

# Step 4: List all indexes
print("Available indexes:", pinecone_client.list_indexes().names())

# Step 5: Connect to the created index
index = Index(name=index_name, api_key="pinecone_api_key", host="host_id")
print(f"Connected to index: {index_name}")

print(pinecone_client.list_indexes())

for index in pinecone_client.list_indexes():
  print( index['name'])

index_description= pinecone_client.describe_index("cbotindex")
print(index_description)

import os
import shutil

# Define the directory path
directory_path = "data"

# Create the directory if it doesn't exist
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Path to your PDF file
pdf_file_path = "/content/ConstitutionOfIndia.pdf"

# Copy the PDF file into the "data" directory
shutil.copy(pdf_file_path, directory_path)

print(f"PDF file copied to {directory_path}")

from llama_index.core import SimpleDirectoryReader

# Load documents from the "data" directory
documents = SimpleDirectoryReader("data").load_data()

# Check the first few loaded documents (prints the text)
print(documents[0].text)

pip install pdfplumber

import pdfplumber

# Function to extract text from a PDF and save it as a .txt file
def pdf_to_text(pdf_path, text_file_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    with open(text_file_path, 'w') as f:
        f.write(text)

# Define paths
pdf_path = "/content/ConstitutionOfIndia.pdf"
text_file_path = "data/ConstitutionOfIndia.txt"

# Extract text and save to text file
pdf_to_text(pdf_path, text_file_path)
print(f"Text extracted and saved to {text_file_path}")

from llama_index.core import SimpleDirectoryReader

# Load the extracted text document from the "data" directory
documents = SimpleDirectoryReader("data").load_data()

# Print the loaded text from the document
print(documents[0].text)

pinecone_client = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
pinecone_index = pinecone_client.Index("cbotindex")

print(pinecone_client.describe_index("cbotindex"))

pinecone_index=pinecone_client.Index("cbotindex")
vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(documents,storage_context=storage_context)

chat_engine = index.as_chat_engine()
while True:
    text_input = input("User: ")
    if text_input.lower() == "exit":
        break
    try:
        response = chat_engine.chat(text_input)

        print(f"Agent: {response.response}")

    except Exception as e:
        print(f"Error during query: {str(e)}")

pip install gradio

import gradio as gr

# Set up API keys
GOOGLE_API_KEY = "google_api_key"
PINECONE_API_KEY = "pinecone_api_key"

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Initialize LLM and embedding model
#llm = Gemini()
#embed_model = GeminiEmbedding(model_name="models/embedding-001")

# Load the Pinecone client
pinecone_client = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

# Load documents
documents = SimpleDirectoryReader("data").load_data()

# Create chat engine
chat_engine = index.as_chat_engine()

# Define the response generation function for Gradio
def generate_response(prompt):
    try:
        response = chat_engine.chat(prompt)
        return response.response
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio interface
interface = gr.Interface(
    fn=generate_response,  # Function to call for generating responses
    inputs="text",         # User input type
    outputs="text",        # Output type
    title="Constitution Chatbot",  # Title for the Gradio app
    description="Engage in an intelligent conversation with a Knowledge Agent fueled by cutting-edge Pinecone and Llama-Index technology. Your questions, smarter answers!"  # Short description
)

# Launch the Gradio app
interface.launch(share=True)
