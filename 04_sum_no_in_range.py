# wpt find the sum of numbers in a given range
sl = int(input())
el = int(input())

summ =0

for i in range(sl,el+1):
    summ+=i
print(summ)


'''
#process
1. take input from usee for starting limit #25
2. take input from user for ending limit #28
3. asume that there is no numbers between that range
3. using for loop
    iteration1:
        it will fetch 25 so i is 25:
            summ+=25 = 25
    iteration2:
        it will fetch 26 so i is 26:
            summ+=26 = 51
    iteration3:
        it will fetch 27 so i is 27:
            summ+=27 = 78
    iteration4:
        it will fetch 28 so i is 28:
            summ+=28 = 106
4. after complition of loop print summ = 106   
'''