# AI Research Assistant

An end-to-end AI research assistant that searches Wikipedia, retrieves relevant information using embeddings and cosine similarity, and generates an answer using an LLM.

## Features

* Wikipedia-based research
* Webpage extraction and text chunking
* OpenAI embeddings for semantic search
* Cosine similarity for retrieving relevant chunks
* GPT-5-mini for answer generation
* FastAPI backend
* Next.js frontend

## Architecture

```text
User Question
      ↓
Wikipedia Search
      ↓
Fetch Web Pages
      ↓
Text Chunking
      ↓
Generate Embeddings
      ↓
Cosine Similarity
      ↓
Top Relevant Chunks
      ↓
GPT-5-mini
      ↓
Generated Answer
      ↓
Next.js Frontend
```

## Tech Stack

**Backend**

* Python
* FastAPI
* OpenAI API
* BeautifulSoup
* scikit-learn

**Frontend**

* Next.js
* React
* TypeScript

## Setup

### Backend

Clone the repository and install the Python dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

### Frontend

Go into the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run the development server:

```bash
npm run dev
```

Open:

```text
http://localhost:3000
```

## Note

This project was built as a learning project to understand how retrieval-augmented AI applications work end-to-end.

AI assistance was used during development, including for parts of the Next.js frontend.


