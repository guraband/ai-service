from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from search_faq import search_faq


def generate_answer(question: str, k: int = 3) -> str:
    # FAQ 검색
    search_results = search_faq(question, k=k)

    # 검색 결과로부터 컨텍스트 구성
    contexts = []
    for doc in search_results:
        contexts.append(f"질문: {doc.metadata['question']}\n답변: {
                        doc.metadata['answer']}")
    context_text = "\n\n".join(contexts)

    # 프롬프트 템플릿 구성
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """
        당신은 친절한 AI 도우미입니다. 
        주어진 컨텍스트를 바탕으로 사용자의 질문에 답변해주세요.
        컨텍스트에 없는 내용은 답변하지 마세요.
        답변은 친절하고 자연스러운 한국어로 작성해주세요.
        """),
        ("user", """
        컨텍스트:
        {context}
        
        질문: {question}
        """)
    ])

    # ChatGPT 모델 초기화
    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )

    # 답변 생성
    chain = prompt_template | chat
    response = chain.invoke({
        "context": context_text,
        "question": question
    })

    return response.content


if __name__ == "__main__":
    print("FAQ 도우미입니다. 질문을 입력해주세요.")
    print("종료하려면 'q' 또는 'quit'를 입력하세요.")
    print("-" * 50)

    while True:
        question = input("\n질문을 입력하세요: ").strip()

        if question.lower() in ['q', 'quit']:
            print("\n프로그램을 종료합니다. 감사합니다!")
            break

        if not question:
            print("질문을 입력해주세요!")
            continue

        print("\n답변을 생성 중입니다...")
        try:
            answer = generate_answer(question)
            print(f"\n답변: {answer}")
        except Exception as e:
            print(f"\n오류가 발생했습니다: {str(e)}")

        print("-" * 50)
