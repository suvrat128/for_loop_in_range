#wpt find the fectorial of given number

n = int(input())

fact = 1

for i in range(1,n+1):
    fact*=i
print(fact)

'''
#process
1. take input from user for ending limit #5
2. asume that there is no numbers between that range fact 1
3. using for loop
    iteration1:
        it will fetch 1 so i is 1:
            fact*=1 = 1
    iteration2:
        it will fetch 2 so i is 2:
            fact*=2 = 2
    iteration3:
        it will fetch 3 so i is 3:
            fact*=3 = 6
    iteration4:
        it will fetch 4 so i is 4:
            fact*=4 = 24
    iteration5:
        it will fetch 5 so i is 5:
            fact*=5 = 120
4. at print fact = 120


'''
