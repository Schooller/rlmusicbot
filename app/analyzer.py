Keywords = ['алкоголичка', 'пидорас', 'ебаться', 'блять', 'еби', 'сиськи', 'ебень', 'поебень', 'пиздеж', 'пох', 'майнкрафт', 'гимн', 'ссср', 'бухать', 'похую', 'путин', 'зона', 'похуй', 'мусора', 'хуй', 'хер', 'блять', 'бля', 'блядь', 'нахуй', 'пизда', 'долбоёб', 'хую', 'пенису', 'фалосу', 'бля']


def analyze(S: str):
    text = ''
    Array = ['-', ',', '.', '"', '"']
    for i in S:
        if i.isupper():
            text += " "
        if i in Array:
            text += " "
            continue
        text += i
    Words = list(map(str, text.lower().split(" ")))
    for keyword in Keywords:
        if keyword in Words:
            return False
    return True


if __name__ == "__main__":
    pass
