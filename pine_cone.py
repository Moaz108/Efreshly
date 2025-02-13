import os
import time

from dotenv import load_dotenv
from pinecone import ServerlessSpec
from pinecone.grpc import PineconeGRPC as Pinecone

load_dotenv()
api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=api_key)

data = [
    {
        "id": "vec1",
        "text": "Apple is a popular fruit known for its sweetness and crisp texture.",
    },
    {
        "id": "vec2",
        "text": "The tech company Apple is known for its innovative products like the iPhone.",
    },
    {"id": "vec3", "text": "Many people enjoy eating apples as a healthy snack."},
    {
        "id": "vec4",
        "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.",
    },
    {"id": "vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},
    {
        "id": "vec6",
        "text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership.",
    },
]
embeddings = pc.inference.embed(
    model="multilingual-e5-large",
    inputs=[d["text"] for d in data],
    parameters={"input_type": "passage", "truncate": "END"},
)

print(embeddings)
