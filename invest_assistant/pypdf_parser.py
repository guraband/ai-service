from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

loader = PyPDFLoader("./resource/bok_report.pdf")

text_splitter = CharacterTextSplitter(
    separator='.',
    chunk_size=500,
    chunk_overlap=100,
    length_function=len
)


# page 단위로 split
pages = loader.load_and_split()
text = pages[0].page_content
print(text)
print("=" * 50)
print(f"# total pages : {len(pages)}")
print(f"# 첫 페이지의 글자수 : {len(text)}")

texts = text_splitter.split_text(text)

print("=" * 50)
print(f"# 첫번째 chunk : {len(texts[0])}")
print(texts[0])
print("=" * 50)

# document 전체를 처리
document = loader.load()
texts = text_splitter.split_documents(document)
print(texts[0])
print(len(texts))
