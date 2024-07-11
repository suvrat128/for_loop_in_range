# wpt print first 10 even numbers

for i in range(20):
    if i%2==0:
        print(i)

#or
        
for i in range(19,2):
    print(i)
'''
#process
using for loop with range
    iteration 1: it will fetch 0 so i is 0: print i = 0
    iteration 2: it will fetch 2 so i is 0: print i = 2
    iteration 3: it will fetch 4 so i is 0: print i = 4
    iteration 4: it will fetch 6 so i is 0: print i = 6
    iteration 5: it will fetch 8 so i is 0: print i = 8
    iteration 6: it will fetch 10 so i is 0: print i = 10
    iteration 7: it will fetch 12 so i is 0: print i = 12
    iteration 8: it will fetch 14 so i is 0: print i = 14
    iteration 9: it will fetch 16 so i is 0: print i = 16
    iteration 10: it will fetch 18 so i is 0: print i = 18
    
'''