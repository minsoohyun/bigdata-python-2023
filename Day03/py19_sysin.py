# 콘솔에서 파라미터 받기
import sys

args = sys.argv[1:] # py19_sysin.py(0) aaa(1) bbb(2) ccc(3)
ind = 1

if(len(args) == 1 ):
    print('도움말 표시 ~~~~~')

for i in args:
    if(ind == 1 ): 
        # --version, clone
        if( i == '--vesrion'):
            print('Curr Program Ver 1.0.4')
        elif(i == 'clone'):
            print('깃허브 리포지토리를 복사합니다')
    elif(ind == 2 ):
        # github 주소,
        print(i)

    ind += 1