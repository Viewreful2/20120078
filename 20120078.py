def rule1(B) :
    for i in range(0,5) :
        if (B[i][0] +B[i][1] +B[i][2] +B[i][3] +B[i][4]) == 5:
            return True;
    return False;

def rule2(B):
    for i in range(0,5) :
        if (B[0][i] +B[1][i] +B[2][i] +B[3][i] +B[4][i]) == 5:
            return True;
    return False;

def rule3(B):
    count = 0
    for i in range(0,5) :
        if B[i][i] == 1:
            count = count +1
    if count == 5 :
        return True;

    count = 0
    for i in range(0,5):
        if B[i][4-i] == 1:
            count = count +1
    if count == 5 :
        return True;
    
    return False;


def rule4(B):
    if (B[0][0] +B[0][4] +B[4][0] +B[4][4]) == 4:
        return True;
    
    return False;    



row = 5#행의 길이
col = 5#열의 길이

BINGO = []#내가 만드는 빙고 게임의 게임판
B = []
T = int(input())#얼만큼 빙고 게임을 한 것인지 의미

for t in range(0,T):#T만큼 빙고 게임을 합시다.
    BINGO = []
    B = []
    for i in range(0, row):#행의 길이만큼 돌면서
        row_input = input().split()#인풋을 받고
        row_input = [int(j) for j in row_input]#그 인풋을 숫자로 만들어주고
        BINGO.append(row_input)#입력 받은 것을 내가 만드는 빙고판에 더해준다.
        
        if i == 2 :
            B.append([0,0,1,0,0])
        else :
            B.append([0]*5)
            
    input_numbers = input().split()#빙고 게임 시작시 불리는 숫자들
    input_numbers = [int(j) for j in input_numbers]#그 숫자들을 숫자로 만들어준다.

    count_of_input = 0#몇번째 불리는 숫자인지를 알기 위한 변수
    for number in input_numbers:#입력 받은 숫자들에 대해서 시작

        count_of_input = count_of_input + 1# 몇번째 불리는지 알기 위해 더해준다.

        for i in range(0,5):
            for j in range(0,5):
                if number == BINGO[i][j]:
                    B[i][j] = 1
                    #존재한다면 B에서 그 해당 위치의 값을 1로 바꿔줘
        if rule1(B) == True:
            print(count_of_input)
            break

        if rule2(B) == True:
            print(count_of_input)
            break


        if rule3(B) == True:
            print(count_of_input)
            break

        if rule4(B) == True:
            print(count_of_input)
            break