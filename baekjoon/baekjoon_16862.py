# An I for an Eye
"""
Ken has been having trouble lately staying under the word limit in Twitter,
so he’s decided to write a little front-end program which will take in text and
shorten it using a fixed set of abbreviations for commonly used letter sequences.
Those abbreviations are shown in the table below:

The character ...	... substitutes for the letter sequence
@	at
&	and
1	one, won
2	to, too, two
4	for, four
b	bea, be, bee
c	sea, see
i	eye
o	oh, owe
r	are
u	you
y	why
Ken is about to start writing this program when he realizes that the extent of his computer knowledge is ... well ... using Twitter.
He’s looking for someone to help him – r u th@ some1?
"""
"""
--- 적당한 문제 내용 요약 ---
1. 숫자를 받아서 해당 숫자만큼 문자열을 받는다.
2. 문자열 내에서 축약어 테이블에 해당하는 문자들은 모두 축약어로 바꾼다.
3. 바꾸기 전 문자열이 대문자로 시작하면 축약어도 대문자로 바꾼다.(Be = B, be = b)
4. 문자열을 여러 축약어로 바꿀 수 있다면 제일 먼저 바꿀 수 있는 문자열을 축약어로 바꾼다. (ato는 @o로 바꿔야 하며, a2로 바꾸는 것이 아님)
5. 바꿀 수 있는 문자열이 더 긴 걸로 문자열을 바꾼다.(bee는 be와 bee를 모두 b로 바꿔서 각각 be와 b를 만들 수 있는데, 더 긴 문자인 bee를 b로 바꾼다.)
6. 문자열이 축약어로 바꾸고 또 바뀐 축약어를 또 축약어로 바꾸지는 않는다. (oweh는 바꾸면 oh가 되는데, oh도 o로 바꿀 수 있으나 그렇게 하지 않는다)
7. 문자열은 알파벳 대소문자와 공백으로만 이루어진 200자의 텍스트이고, 제한시간은 2초이다.

--- 문제점 ---
#1 bee와 be는 어떻게 해결할 것인가?
#2 for는 어떻게 해결할 것인가?
#3 seeye와 seyee는 어떻게 해결할 것인가? (제일 문제였음)

# 해결방안 1
1. 한 글자를 읽는다.
2. 축약어 테이블의 시작 문자(a, o, e 등)라면 임시 변수에 넣는다.
3. 시작 문자가 아니라면 그냥 result에 추가한다.
4. 다음 글자를 읽는다.
5. 다음 글자와 임시 변수에 있는 글자를 붙여서 축약어 테이블에 존재한다면 축약어로 바꾼다.
6. 축약어 테이블에 존재하지 않는다면 임시 변수에 있는 문자를 result에 추가한다.
-> 실패 : be와 bee는 해결할 수 있지만, for와 같은 3글자가 넘는 축약어는 해결할 수 없음

# 해결방안 2
1. 한 글자를 읽는다.
2. 시작 문자라면 임시 변수에 넣는다. 
3. 다음 문자들을 받아서 축약어 테이블에 맞춰 하드코딩한다.
-> 실패 : seyee같은 경우 문제 발생. sey까지 왔을 때 축약어가 되지 못함을 깨닫고 다음으로 넘어가야 하는데, 다시 e로 돌아가야 함.

# 해결방안 3
1. 한 글자를 읽는다.
2. 시작 문자라면 다음과 같은 함수를 거친다.
3. 축약어 테이블의 문자열 길이는 최대 4자(four)이므로, 해당 시작문자와 앞으로 최대 3개의 문자를 탐색한다.
4. 탐색하면서 축약어가 나온다면 해당 문자를 임시로 축약어로 삼고, 몇 글자가 축약됐는지 기록한다.
5. 문자를 더 붙이면서 또 축약어가 나온다면 해당 문자를 다시 축약어로 삼고, 몇 글자가 축약됐는지 기록한다.
6. 축약어와 몇 글자가 축약됐는지를 리턴한다.
7. 축약어를 result에 붙이고, 축약된 만큼 뒤에 있는 문자를 확인한다.
8. 시작 문자가 아니라면 그냥 result에 붙인다.
-> 성공
"""
import sys

# 시작 문자들
start_digits = set(['a', 'o', 'w', 't', 'f', 'b', 's', 'e', 'o', 'a', 'y', 'w'])

# 축약어 테이블
letters_to_be_substituted = {
    'at':'@',
    'and':'&',
    'one':'1',
    'won':'1',
    'to':'2',
    'too':'2',
    'two':'2',
    'for':'4',
    'four':'4',
    'bea':'b',
    'be':'b',
    'bee':'b',
    'sea':'c',
    'see':'c',
    'eye':'i',
    'oh':'o',
    'owe':'o',
    'are':'r',
    'you':'u',
    'why':'y'
}

# 시작 문자와 앞으로 탐색할 문자열을 받아서 축약어와 축약된 개수를 리턴하는 함수
def get_abbreviation(temp_letters, candidates):
    result = temp_letters
    abbreviated_number = 0

    for i in range(min(3, len(candidates))):
        # 탐색한 문자를 붙인다.
        temp_letters += candidates[i]
        # 붙인 문자가 축약어 테이블에 존재할 경우 임시로 축약어를 기록하고, 축약된 개수를 기록해준다.
        # 더 긴 축약어가 있다면 더 긴 축약어로 덮어쓴다.
        if letters_to_be_substituted.get(temp_letters.lower(), False):
            result = letters_to_be_substituted[temp_letters.lower()]
            # 대문자로 시작할 경우
            if temp_letters[0].isupper():
                result = result.upper()
            abbreviated_number = len(temp_letters)-1

    return result, abbreviated_number


for _ in range(int(sys.stdin.readline().rstrip())):
    input_text = sys.stdin.readline().rstrip()
    result = ""
    # 축약된 만큼 다음 문자를 탐색해야 하는데, python의 for문에서 인덱스를 늘리는 방법을 몰라서 for문의 반복횟수를 true_index라는 변수로 제어한다.
    true_index = 0

    for false_index in range(len(input_text)):
        # 다음 문자 탐색
        if false_index == true_index:
            # 시작문자일 경우
            if input_text[true_index].lower() in start_digits:
                abbreviation, abbreviated_count = get_abbreviation(input_text[true_index], input_text[true_index + 1:])
                result += abbreviation
                true_index += abbreviated_count
            # 시작문자가 아닐 경우
            else:
                result += input_text[true_index]
            true_index += 1
        else:
            continue

    print(result)