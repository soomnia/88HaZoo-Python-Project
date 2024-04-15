# 기본 URL
BASE_URL = 'https://news.naver.com/breakingnews/section/105/'

# 카테고리별 id를 구해 리스트에 넣자
## 규칙이 있으면 좋을텐데... 당장 내 눈에 보이는 규칙은 없음...

# 모바일
# 'https://news.naver.com/breakingnews/section/105/731?date=20240410'
c_mobile = 731

# 인터넷/SNS
#'https://news.naver.com/breakingnews/section/105/226?date=20240410'
c_internet_sns = 226

# 통신/뉴미디어
#'https://news.naver.com/breakingnews/section/105/227?date=20240410'
c_communcation_media = 227

# IT 일반
#'https://news.naver.com/breakingnews/section/105/230?date=20240410'
c_it_general = 230

# 보안/해킹
#'https://news.naver.com/breakingnews/section/105/732?date=20240410'
c_security = 732

# 컴퓨터
#'https://news.naver.com/breakingnews/section/105/283?date=20240410'
c_computer = 283

# 게임/리뷰
#'https://news.naver.com/breakingnews/section/105/229?date=20240410'
c_game_review = 229

# 과학 일반 
#'https://news.naver.com/breakingnews/section/105/228?date=20240410'
c_science_general = 228

CATEGORY_LIST = [c_mobile, c_internet_sns, c_communcation_media, c_it_general, c_security, c_computer, c_game_review, c_science_general]

def get_category(id):
    switcher = {
        c_mobile: "모바일",
        c_internet_sns: "인터넷/SNS",
        c_communcation_media: "통신/뉴미디어",
        c_it_general: "IT 일반",
        c_security: "보안/해킹",
        c_computer: "컴퓨터",
        c_game_review: "게임/리뷰",
        c_science_general: "과학 일반"
    }
    return switcher.get(id, 0)
