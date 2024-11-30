import json
import pickle
from typing import List
from openai import Client
import os
from pydantic import BaseModel
from tqdm import tqdm
from langchain_core.output_parsers import PydanticOutputParser

from prompt_template import prompt_template
from download_data import get_image_urls

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
client = Client(api_key=OPENAI_API_KEY)


class QA(BaseModel):
    question: str
    answer: str


class Output(BaseModel):
    qa_list: List[QA]


output_parser = PydanticOutputParser(pydantic_object=Output)


def inference(urls):
    prompt = prompt_template.format(
        format_instructions=output_parser.get_format_instructions())
    content = [
        {"type": "text", "text": prompt}
    ]
    for url in urls:
        content.append({"type": "image_url", "image_url": {"url": url}})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": content}],
        max_tokens=1000,
        response_format={"type": "json_object"}
    )
    output = response.choices[0].message.content
    output_json = json.loads(output)
    return output_json


if __name__ == "__main__":
    urls = get_image_urls()

    result = inference(urls)
    print("="*50)
    print(json.dumps(result, indent=2, ensure_ascii=False))

    with open("../faq.pkl", "wb") as f:
        pickle.dump(result, f)
