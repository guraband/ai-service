import pickle
import os

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

    # FEISS.from_texts(faq_data)
