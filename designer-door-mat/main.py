# Program for##### # if __name__ == '__main__':
values = input().split()
n = int(values[0])
m = int(values[1])

   
if ((n%2 != 0) and (m%2 != 0)):
  
    #Beginning  part
    for i in range(1,n,2):       
        # print(i)
        print((".|." * i).center(m, "-"))    
    #Middle Part 
    print("WELCOME".center(m, "-"))
    
    #End Part
    for i in range(n-2, 0, -2):
        # print(i)
        print((".|." * i).center(m, "-"))
else:
    print('Even values not available')
