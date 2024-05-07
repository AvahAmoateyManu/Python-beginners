##def area_square(width):
##    return width * width
##def area_rectangle(width, length):
##    return width * length
##def area_triangle(base, height):
##    return base * height / 2
##def area_circle(radius):
##    return radius*radius*3.14
##while True:
##    qis=input('What shape do you need area of? square, rectangle, triangle or circle ')
##
##    if qis=='square':
##        width=float(input('what is width'))
##        print('area is', area_square(width))
##    elif qis=='rectangle':
##        wifth=float(input('what is width'))
##        length=float(input('what is length'))
##        print('area is',area_rectangle(wifth,length))
##    elif qis=='triangle':
##        base=float(input('what is base'))
##        height=float(input('what is height'))
##        print('area is',area_triangle(base,height))
##    elif qis=='circle':
##        radius=float(input('what is radius'))
##        print('area is',area_circle(radius))
##    else:
##        print('invalid shape')
##print(area_square(4)) # what is printed?
##print(area_rectangle(6,10)) # what is printed?
##print(area_circle(4)) # call your circle function
#'scope'. A scope refers to how far something reaches
##
##def max(*nums):
##    biggest_so_far = 0 # this only works for positive numbers
##    for num in nums: # nums is a collection!
##        if num > biggest_so_far:
##            biggest_so_far = num
##    return biggest_so_far
######print(max(1,2,34,7))
##print(max()) # what if we give it no argu
##
###global is only accesible inside your file. local only works inside a function
###you get nameerror
##def min1(*nums):
##    minimum_num= nums[0]
##    for num in nums:
##        if minimum_num>num:
##            minimum_num=num
##    return minimum_num
##print(min1(1,3,-4,-3,6,7,3,-21))
##    
##def name_phone(name='N/A',number='xxx-xxx-xxxx'):
##    print(name,number)
##name_phone('chloe')
##name_phone(number=9876543)
####
##def rec_area(width,height=0):
##    if height==0:
##        a=width*width
##        return a
##    else:
##        a= width*height
##        return a
##print(rec_area(5))

##def sum_of_product(*nums, SUM= True):
##    if SUM == True:
##        s=0
##        for i in nums:
##            s+=i
##        return s
##    else:
##        m=1
##        for i in nums:
##            m*=i
##        return m
##
##print(sum_of_product(2,3,8))
##print(sum_of_product(2,3,8,SUM=False))

##def sum_function(*nums,SUM=True):
##    if SUM == True:
##        s=0
##        for i in nums:
##            s+=i
##        return s
##print(sum_function(3,4,5,6,6))
####
##def len_function(word):
##    length=0
##    for i in word:
##        length+=1
##    return length
##        
##print(len_function('hello'))

##def range_function(end,start=0,step=1):
##    list=[]
##    temp = start
##    if temp < end:
##        while temp<=end:
##            list.append(temp)
##            temp+=step
##        return list
##    else:
##        while temp>=end:
##            list.append(temp)
##            temp+=step
##        return list
##print(range_function(10,0,2))
##print(range_function(0,10,-1))

##def string_function(word,start=0,end = -1,step=1,):
##    list=[]
##    if end==-1:
##        end=len(word)
##    for i in range(start,end,step):
##       list.append(word[i])
##    return list
##print(string_function('hello world',0,5))

a=20
def globalv():
    global a
    print(a)
globalv()
#start,end,step
