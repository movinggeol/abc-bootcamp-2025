from openai import OpenAI
import os


def get_personality_analysis(face_desc: str) -> str: # 인자 문자열 -> 문자열 반환이란 뜻
    """
    인자로 얼굴 설명을 받아, OpenAI LLM API를 활용하여 성격과 미래를 분석합니다.
    """
    #doc string 문법(윗줄)

    # 원하는 어떠한 형태로든 지시문 문자열을 생성하실 수 있습니다.
    prompt = "당신은 전문 관상가입니다. "
    prompt += "사람들의 얼굴 특징을 보고 성격과 미래를 친근하게 분석해주세요."
    prompt += "\n 얼굴 특징 : " + face_desc
    
    # API_KEY = os.environ["OPENAI_API_KEY"]
    client = OpenAI()  # OPENAI_API_KEY 환경변수 지정이 필요 (.env에 이 이름으로 환경변수를 만들어뒀다면 따로 지정하지 않아도 됨)

    #  OpenAI 모델로부터 응답(텍스트, JSON 등)을 생성하는 메서드입니다.
    # -> 텍스트, 이미지, 툴 등을 입력으로 주고 → 응답을 받아올 수 있는 인터페이스입니다.
    response = client.responses.create(
        model="gpt-4o",  # 사용할 모델 지정
        input=prompt,
    )
    print("usage :", response.usage)

    return response.output_text