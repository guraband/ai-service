import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def search_faq(question, k=3, with_score=False):
    db = FAISS.load_local(
        "faq.index",
        OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY),
        allow_dangerous_deserialization=True
    )
    if with_score:
        results = db.similarity_search_with_score(question, k=k)
    else:
        results = db.similarity_search(question, k=k)

    return results


if __name__ == "__main__":
    results = search_faq("입문자용 교육자료는?", k=3, with_score=True)

    for doc, score in results:
        print(f"유사도 점수: {score}")
        print(f"검색 결과: {doc}")
        print("-"*50)

    print("="*50)
    results = search_faq("입문자용 교육자료는?", k=3, with_score=False)
    for doc in results:
        print(doc)
