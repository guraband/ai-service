import pickle
import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":
    with open("./faq.pkl", "rb") as f:
        qa_list = pickle.load(f)

    faq_data = qa_list["qa_list"]

    questions = [qa["question"] for qa in faq_data]
    for question in questions:
        print(question)
        # print(qa["answer"])
        print("-"*50)

    db = FAISS.from_texts(
        questions,
        embedding=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY),
        metadatas=faq_data
    )

    db.save_local("faq.index")
