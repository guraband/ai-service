import gradio as gr
from faq_bot import generate_answer


def answer_question(question: str) -> str:
    if not question.strip():
        return "질문을 입력해주세요!"
    try:
        return generate_answer(question)
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"


# Gradio 인터페이스 생성
demo = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.Textbox(
            lines=3,
            placeholder="질문을 입력하세요...",
            label="질문"
        )
    ],
    outputs=[
        gr.Textbox(
            lines=5,
            label="답변"
        )
    ],
    title="AI FAQ 도우미",
    description="질문을 입력하시면 관련 FAQ를 기반으로 답변해드립니다.",
    examples=[
        ["강의 가격은 언제 인상되나요?"],
        ["입문자를 위한 교육 자료는 무엇이 있나요?"],
        ["GPT-4 사용에 대해 알려주세요"],
    ],
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    demo.launch(share=False)
