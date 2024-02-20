from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings
import re

model_name = "BAAI/bge-small-en-v1.5"
encode_kwargs = {'normalize_embeddings': True}

embedding_function = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    encode_kwargs=encode_kwargs,
)

db = Chroma(persist_directory="./mockingjay-embeds", embedding_function=embedding_function)
page_content = db.similarity_search("What is the solution?")[0].page_content

flag = re.findall(r"CET24{(.*)}", page_content)[0]
print(f"ROT13 encoded flag: CET24{{{flag}}}")

rot = lambda n, m: ''.join(chr(ord(c)+n) if 'a' <= c.lower() <= chr(ord('z')-n) else chr(ord(c)+n-26) if chr(ord('z')-n) < c.lower() <= 'z' else c for c in m) if 0 < n < 27 else ''
print(f"ROT13 decoded flag: LNC24{{{rot(9, flag)}}}")