from fastapi import FastAPI
from services import fetch_webpage, search_topics, chunk_text
from dotenv import load_dotenv
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

client = OpenAI()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():
    return {"message": "AI Research Assistant is running"}


@app.get("/research")
def research(topic: str):

    result = search_topics(topic)

    search_result = result["query"]["search"]

    sources = []

    for item in search_result:

        title = item["title"]
        title = title.replace(" ", "_")

        pageid = item["pageid"]

        url = f"https://en.wikipedia.org/wiki/{title}"

        page_text = fetch_webpage(url)

        chunks = chunk_text(page_text)

        # Embed all chunks in one API call
        embedding_response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunks
        )

        embedded_chunks = []

        # Match each chunk with its embedding
        for chunk, data in zip(chunks, embedding_response.data):

            embedded_chunks.append({
                "text": chunk,
                "embedding": data.embedding
            })

        source = {
            "pageid": pageid,
            "title": title,
            "url": url,
            "content": embedded_chunks
        }

        sources.append(source)


    # Embed the user's question
    query_embedding_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=topic
    )

    query_embedding = query_embedding_response.data[0].embedding
    scored_chunks = []

    for source in sources:

        for item in source["content"]:

            chunk_embedding = item["embedding"]
            score = cosine_similarity([query_embedding],[chunk_embedding])[0][0]

 
            scored_chunks.append({
                "text": item["text"],
                "similarity": score,
                "title": source["title"],
                "url": source["url"]
            })
    scored_chunks.sort(key=lambda x:x["similarity"],reverse=True)
    top_chunks=scored_chunks[:5]
    context="\n\n".join(chunk["text"]for chunk in top_chunks)
    prompt=f"""
    Research question:{topic}
    Answer the question using only the following research:{context}"""

    #sending prompt to gpt
    response=client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )
    answer=response.output_text
    return {
    "topic": topic,
    "answer": answer,
    "sources": top_chunks
    }   