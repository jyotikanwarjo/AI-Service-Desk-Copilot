import os
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from google import genai
from google.genai import types


# ---------------------------------------------------------
# PROJECT PATHS
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
KB_DIR = BASE_DIR / "knowledge_base"
ENV_PATH = BASE_DIR / ".env"


# ---------------------------------------------------------
# LOAD API KEY
# ---------------------------------------------------------

load_dotenv(ENV_PATH)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY was not found in the .env file."
    )


# ---------------------------------------------------------
# GEMINI CLIENT
# ---------------------------------------------------------

client = genai.Client(api_key=API_KEY)


# ---------------------------------------------------------
# LOAD KB DOCUMENTS
# ---------------------------------------------------------

def load_kb_documents():

    documents = []

    for file_path in sorted(KB_DIR.glob("*.md")):

        text = file_path.read_text(
            encoding="utf-8"
        ).strip()

        if text:

            documents.append(
                {
                    "file_name": file_path.name,
                    "text": text,
                }
            )

    if not documents:

        raise RuntimeError(
            "No .md knowledge-base files were found."
        )

    return documents


# ---------------------------------------------------------
# CREATE DOCUMENT EMBEDDING
# ---------------------------------------------------------

def create_document_embedding(text):

    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT"
        ),
    )

    return np.array(
        result.embeddings[0].values,
        dtype=np.float32
    )


# ---------------------------------------------------------
# CREATE QUERY EMBEDDING
# ---------------------------------------------------------

def create_query_embedding(text):

    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        ),
    )

    return np.array(
        result.embeddings[0].values,
        dtype=np.float32
    )


# ---------------------------------------------------------
# COSINE SIMILARITY
# ---------------------------------------------------------

def cosine_similarity(vector_a, vector_b):

    denominator = (
        np.linalg.norm(vector_a)
        * np.linalg.norm(vector_b)
    )

    if denominator == 0:
        return 0.0

    return float(
        np.dot(vector_a, vector_b)
        / denominator
    )


# ---------------------------------------------------------
# RETRIEVE KBs
# ---------------------------------------------------------

def retrieve_kb(query, top_k=3):

    documents = load_kb_documents()

    query_embedding = create_query_embedding(query)

    results = []

    for document in documents:

        document_embedding = create_document_embedding(
            document["text"]
        )

        score = cosine_similarity(
            query_embedding,
            document_embedding
        )

        results.append(
            {
                "file_name": document["file_name"],
                "text": document["text"],
                "score": score,
            }
        )

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:top_k]


# ---------------------------------------------------------
# BEST KB
# ---------------------------------------------------------

BEST_KB_THRESHOLD = 0.74


def get_best_kb(query):

    results = retrieve_kb(query, top_k=3)

    if not results:
        return {
            "accepted": False,
            "best_match": None,
            "score": 0.0,
            "reason": "No knowledge-base documents were retrieved.",
        }

    best = results[0]

    if best["score"] < BEST_KB_THRESHOLD:
        return {
            "accepted": False,
            "best_match": best,
            "score": best["score"],
            "reason": (
                "Best KB similarity score is below "
                "the retrieval threshold."
            ),
        }

    return {
        "accepted": True,
        "best_match": best,
        "score": best["score"],
        "reason": "Best KB similarity score meets the retrieval threshold.",
    }

# ---------------------------------------------------------
# TEST THE RETRIEVAL
# ---------------------------------------------------------

if __name__ == "__main__":

    test_query = (
        "User cannot connect to VPN after "
        "changing their corporate password."
    )

    print("\nRETRIEVAL RESULTS")
    print("=" * 60)

    results = retrieve_kb(test_query)

    for index, result in enumerate(results, start=1):

        print(
            f"{index}. "
            f"{result['file_name']} "
            f"→ score: {result['score']:.4f}"
        )

    print("\nBEST MATCH DECISION")
    print("=" * 60)

    decision = get_best_kb(test_query)

    print(f"Accepted: {decision['accepted']}")
    print(f"Score: {decision['score']:.4f}")
    print(f"Reason: {decision['reason']}")

    if decision["best_match"]:

        print(
            f"Best KB: "
            f"{decision['best_match']['file_name']}"
        )