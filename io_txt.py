from pathlib import Path   # 1- 100 째 까지 불러오는

def read_document():    # 리뷰 디큐먼트 직관적으로 만드는게 좋음
    return Path("data/git_기초.txt").read_text(encoding="utf-8") # 리드 텍스트 문자 그대로 텍스트를 읽겠어 어디서 ? 우리가 가져오는 깃허브 에서
# 결과 값을 다시 되돌려 주는 걸 리턴이라고 함.
def save_preview(preview):    #내가 읽어드린 내가 파일을 다시 내 보내겠다라는 뜻  # 디파인 멀 만들겠다.괄호를 사용하는건 다 함수
    output_dir = Path("outputs") # 경로를 설정하고
    output_dir.mkdir(exist_ok=True) # 설정한 경로로 디렉토리 폴더를 만들어 준다.
    (output_dir / "미리보기.txt").write_text(preview, encoding="utf-8")

text = read_document() # 리턴 값이 여기로 들어옴. 디렉토리로 들어가고 다시 감.
preview = text[:100]
print(preview)
save_preview(preview)

# UTF-8 = 한글인 경우 이 형식으로 
# ANSI = 영문일 경우 이 형식으로

# 