from dotenv import load_dotenv
from ai import get_personality_analysis

load_dotenv()

print("# AI 관상가입니다. 얼굴 특징을 입력해주시면 성격과 미래를 전망해드릴게요.")
line = input("얼굴 특징 : ").strip()

if not line: # 빈 문자열이라면
    print("얼굴 특징을 입력하지 않으셨습니다.")

else:
    print("입력하신 얼굴 특징", line)
    print("분석 중 ...")
    result = get_personality_analysis(line)
    print("분석 완료!")
    print(result)

#print(repr(line))
#print(get_personality_analysis("못생김"))

#openai가 답변을 완전히 생성하기까지 기다려야 함.
# streaming 을 사용하면 중간 결과물을 보여줌(chunk 사용, openai도 지원)