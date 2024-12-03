# Constitution Chatbot using RAG (Retrieval-Augmented Generation)

## Overview

This repository hosts the **Constitution Chatbot**, an advanced AI-powered conversational agent designed to provide intelligent answers based on constitutional documents. By leveraging **Retrieval-Augmented Generation (RAG)** with Pinecone, Llama-Index, and Gradio, the chatbot can efficiently retrieve and generate precise answers from indexed documents. This project is particularly useful for legal professionals, students, and anyone interested in constitutional knowledge.

## Features

- **Retrieval-Augmented Generation (RAG):** Combines document retrieval with language model generation for accurate responses.
- **Document Integration:** Supports multiple constitutional documents in PDF format.
- **Pinecone Vector Store:** Efficient indexing and retrieval of document embeddings.
- **Gradio Interface:** User-friendly web-based interface for interactions.
- **Expandable Design:** Add more documents and scale easily with Pinecone and Llama-Index.

---

## Technology Stack

- **Python**: Core programming language.
- **Pinecone**: Vector database for fast and scalable document retrieval.
- **Llama-Index**: Framework for document ingestion and embedding generation.
- **Gradio**: Interface for seamless user interactions.
- **pdfplumber**: Utility for extracting text from PDFs.

---

## Installation

### Prerequisites

- Python 3.10+
- Pinecone API key (sign up at [Pinecone](https://www.pinecone.io/))
- Google Generative AI API key (sign up at [Google Cloud](https://cloud.google.com/))
- Access to required constitutional documents in PDF format.

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/constitution-chatbot.git
   cd constitution-chatbot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**
   Replace placeholders in the code with your API keys:
   - `GOOGLE_API_KEY`
   - `PINECONE_API_KEY`

4. **Prepare Documents**
   Place your PDF documents in the `data` folder.

5. **Run the Chatbot**
   ```bash
   python ConstitutionBot.py
   ```

6. **Access the Interface**
   The Gradio interface will provide a URL for interaction.

---

## Usage

1. Add PDF documents to the `data` directory.
2. Start the chatbot using `python ConstitutionBot.py`.
3. Interact via the Gradio interface and ask questions based on the uploaded documents.

---

## Adding More Documents

1. Place additional PDF files in the `data` directory.
2. Extract text from the PDF using `pdfplumber`:
   ```python
   pdf_to_text("path/to/your/document.pdf", "data/document.txt")
   ```
3. Reload the documents:
   ```python
   documents = SimpleDirectoryReader("data").load_data()
   ```

---

## Example Queries

- "What is Article 19 of the Constitution?"
- "Explain the preamble in detail."
- "What are the fundamental rights?"

---

## Gradio Interface

The chatbot comes with an easy-to-use Gradio web interface:

- **Input:** Type your query in plain text.
- **Output:** Receive an intelligent response based on the indexed documents.

---

## Troubleshooting

- **ReadTimeout Errors**: Ensure proper connectivity to Pinecone and increase the timeout settings if necessary.
- **Missing API Keys**: Ensure both Google Generative AI and Pinecone API keys are set as environment variables.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For inquiries or issues, please contact [pandeyshubhi2605@gmail.com].
