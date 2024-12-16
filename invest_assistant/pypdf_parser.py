from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader("./resource/bok_report.pdf")
pages = loader.load_and_split()

text = pages[0].page_content
print(text)
print("=" * 50)
print(f"# total pages : {len(pages)}")
print(f"# 첫 페이지의 글자수 : {len(text)}")

text_splitter = CharacterTextSplitter(
    separator='.',
    chunk_size=500,
    chunk_overlap=100,
    length_function=len
)

texts = text_splitter.split_text(text)

print("=" * 50)
print(f"# 첫번째 chunk : {len(texts[0])}")
print(texts[0])
print("=" * 50)
