import RandomCharacter

NUMBER_OF_CHARS = 175 # 생성할 문자 수
CHARS_PER_LINE = 25 # 한 행당 출력한 문자 수

# 'a'와 'z' 사이의 랜덤 문자를 출력한다. 한 행당 25개 문자를 출력한다.
for i in range(NUMBER_OF_CHARS):
    print(RandomCharacter.getRandomLowerCaseLetter(), end = "")
    if (i + 1) % CHARS_PER_LINE == 0:
        print()  # 새로운 행으로 이동한다.
