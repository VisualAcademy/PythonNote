# 파이썬 패턴 매칭: match case 문: Python 3.10 이상에서 테스트
shape = "정사각형"
result = ""

match shape:
    case "정사각형":
        result = "Square"
    case "원":
        result = "Circle"
    case "오각형" | "팔각형"
        result = "Polygon"
    case _:
        result = "Other"

print(result)
