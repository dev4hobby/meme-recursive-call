import time

sentence = 'hello world'

def what_is_recursive_function(remained, tabcount): # 재귀 횟수, 들여쓰기 횟수
    # animation 효과를 주기위한 print trick.
    print('\t'*tabcount, end='', flush=True)
    for character in sentence: # sentence 에서 글자단위로 가져와서 뿌리기
        if(character == '\n'):
            print('\n', end='', flush=True)
            print('\t'*tabcount, end='', flush=True)
            time.sleep(0.03)
        else:
            print(character, end='', flush=True)
            time.sleep(0.03)

    # 재귀 종료 조건에 가까워진다!
    remained -= 1
    if remained > 0:
        print('')
        # 아직 재귀횟수가 남아있다면 다시 호출
        what_is_recursive_function(remained, tabcount+1)
    else:
        # 그게 아니라면 종료.
        print('...')

if __name__ == "__main__":
  what_is_recursive_function(8, 0)

