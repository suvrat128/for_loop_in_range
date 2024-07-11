# wpt print even number in given range

sl= int(input())
el= int(input())

for i in range(sl,el+1):
    if i%2 ==0:
        print(i)
        
'''
#process
1. take input from usee for starting limit #25
2. take input from user for ending limit #30
3. using for loop
    iteration 1:
        it will fetch 25 so i is 25:
        check 25%2== 0 false
    iteration 2:
        it will fetch 26 so i is 26:
        check 2652==0 true:
            print(i) == 26
    iteration 3:
        it will fetch 27 so i is 27:
        check 27%2== 0 false
    iteration 4:
        it will fetch 28 so i is 28:
        check 28%2==0 true:
            print(i) == 28
    iteration 5:
        it will fetch 29 so i is 29:
        check 29%2== 0 false
    iteration 6:
        it will fetch 30 so i is 30:
        check 30%2==0 true:
            print(i) == 30

'''
