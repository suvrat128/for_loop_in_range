#wpt find given number is perfect number or not

# if the given number is equal to sum of its diviser than we called given nimber is a perfect number

n = int(input())

summ = 0

for i in range(1,n):#or for i in range(1,n//2+1)  it will do code optimazation:
    if n%i == 0:
        summ+=i
if summ == n:
    print('perfect number')
else:
    print('not perfect number')
'''
#process
1. take input from user for ending limit #6
2. asume that variable summ = 0
3. using for loop:
    iteration1:
        it will fetch 1 so i is 1
        check 6%1 == 0 true
            so summ += 1 = 1
    iteration2:
        it will fetch 2 so i is 2
        check 6%2 == 0 true
            so summ += 2 = 3
    iteration3:
        it will fetch 3 so i is 3
        check 6%3 == 0 true
            so summ += 3 = 6
4. after complition of for loop
5. we check for summ == n :
        true print it is a perfect number
'''
