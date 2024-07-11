
#wpt find the sum of first n nubers

n = int(input())

summ = 0

for i in range(1,n+1):
    summ+=i
print(summ)

'''
1. take input from user for ending limit #5
2. asume that there is no numbers between that range summ = 0
3. using for loop
    iteration1:
        it will fetch 1 so i is 1:
            summ+=1 = 1
    iteration2:
        it will fetch 2 so i is 2:
            summ+=2 = 3
    iteration3:
        it will fetch 3 so i is 3:
            summ+=3 = 6
    iteration4:
        it will fetch 4 so i is 4:
            summ+=4 = 10
    iteration5:
        it will fetch 5 so i is 5:
            summ+=5 = 15
4. at we will print summ = 15
'''