##i = 10
##while i > 2:
##    print(i)
##    i = i - 3
##
##    for i in range(10,2,-3):
##        print(i)

##
##print("Hello", end=" ")
##print("World!", end="")
##for i in range(10):
##    print(i, end="\t")
##for i in range(5):
##    print(i, end="0\n")
##
##user_name = "Gurleen"
##user_age = 13
##name = "Kyle"
##print("%s is your name, and %s is mine."%(user_name,name))
##print("Username:%s, age:%d years old."%(user_name, user_age))

#Here, %s is used as a placeholder for a string, and %d is used as a placeholder for a
##number. After the string, you see there are variable names written out. These variables
##will be put inside the string, replacing the placeholders, in order

##for i in range(10): # 10 rows
##    for j in range(5): # 5 columns
##        print("*", end="\t")
##    print() 
##
##for x in range(8): # 8 rows
##    for char in "abcd": # 4 columns
##        print(char, end=" ")
##    print('----')
##
##for x in range(6):
##    for a in range(4):
##        print('3',end=' ')
##    print()

##for i  in range(1,6):
##    for j in range (i):
##        print(i,end=' ')
##    print()
##
##for i  in range(6,0,-1):
##    for j in range (i,0,-1):
##        print(i,end=' ')
##    print()

##for i in range(4):
##    for j in range(4):
##        print('*',end=' ')
##    print()

##l='a'
##while l=='a':
##    for i in range(4):
##        for j in range(4):
##            print('*',end=' \t')
##        print()
##    l=input('write a if you want more stars ')
##
##
##n=input('what is your name ')
##for i in range(3):
##    for j in range(5):
##        print(n,end=" ")
##    print()


##
##for i in range(3):
##    for j in range(2):
##        print('\t|',end='')
##    if i<2:
 ##        print('\n------------------------')
##print('\n-------------------------')
##for i in range(3):
##    for j in range(4):
##        print('|',end='\t')
##    print('\n-------------------------')

##print('\n---------------------------------------------------------------------------\n|',end='')    
##for i in range (1,11):
##    for j in range (1,11):
##        print(i*j,end="|\t")
#if j<11:
##    print('\n---------------------------------------------------------------------------\n|',end='')    

##t=input('type y to start drawing a triangle? ')
##while t=='y':
##    size=1
##    for i in range(1,size+1):
##         for j in range(1):
##             print('*'*i)
##         print()
        
##
##num=2
##ch=input('type y to start drawing a triangle ')
##while ch=='y':
##    for j in range(1,num):
##        print('*'*j)
##    ch=input('type y to start drawing a triangle ')
##    num+=1
##        
##
##user_input = input("Do you want to print a triangle? (y/n): ")
##
##while user_input.lower() == 'y':
##    size = int(input("Enter the size of the triangle: "))
##
##    # Printing the triangle using a for loop
##    for i in range(1, size + 1):
##        print('*' * i)
##
##    user_input = input("Do you want to print another triangle? (y/n): ")
##
##print("Goodbye!")
