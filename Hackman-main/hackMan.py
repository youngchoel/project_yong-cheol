import random as r

wordList = [
    'apple', 'iguana', 'hospital', 'argorithm', 'nullpointerexeption'
]

word = wordList[r.randint(0, len(wordList) - 1)]
wordLength = len(word)
hintText = '-'*wordLength

prize = 100000 * wordLength

def returnIndexes(word, char): #알파벳 위치들을 리턴하는 함수
    indexs = []
    index = 0
    for i in word:
        if i == char:
            indexs.append(index)
        index+=1
    return indexs

def fill(word, lword, char): #알파벳 채워서 리턴하는 함수
    indexs = returnIndexes(word, char)
    
    wList = list(lword)
    for j in indexs:
        wList[j] = char

    lword = ''.join(wList)
    return lword
    

while True:
    print('제시어: {}'.format(hintText))
    print('상금: {}원'.format(prize))
    alphabet = input('알파벳 입력: ').lower()
    if len(alphabet) == 1:
        if alphabet in word:
            hintText = fill(word, hintText, alphabet)
            print('제시어: {}'.format(hintText))
            prize -= 100000
            print('상금: {}원'.format(prize))
            answer = input('정답은?: ')
            if answer == word:
                print('정답')
                break
            else:
                print('오답')
        else:
            print('{}은(는) 없습니다'.format(alphabet))
            prize -= 100000
    else:
        print('알파벳 한글자만 입력해 주세요')
            
            
            
