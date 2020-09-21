from random import randint # randint를 임포트한다.

# ch1과 ch2 사이의 랜덤 문자를 생성한다.
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

# 랜덤 소문자를 생성한다.
def getRandomLowerCaseLetter():
    return getRandomCharacter('a', 'z')

# 랜덤 대문자를 생성한다.
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')

# 랜덤 숫자를 생성한다.
def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')

# 랜덤 문자를 생성한다.
def getRandomASCIICharacter():
    return getRandomCharacter(chr(0), chr(127))
