import random 

def get_days():
    days = []
    days = ["월", "화", "수", "목", "금", "토", "일"]
    return days

def get_random_wather_report():
    weather = ["맑음", "흐림", "비", "눈"]
    report = weather[random.randint(0, len(weather) - 1)]
    return report


def main():
    days = get_days()

    for d in days:
        r = get_random_wather_report()
        print("날씨: {0} -> {1}".format(d, r))

main()
