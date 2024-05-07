##mystery_dict = {}
##my_keys = []
##my_values = []
##def key_fetcher(*keys):
##    for key in keys:
##        my_keys.append(key)
##def value_fetcher(*vals):
##    for val in vals:
##        my_values.append(val)
##def dict_creator(key_list, val_list, dict = mystery_dict):
##    for i in range(len(key_list)):
##        dict[key_list[i]] = val_list[i]
##    return dict
##key_fetcher(1,2)
##value_fetcher('three', 'four')
##new_dict = dict_creator(my_keys, my_values)
##print(new_dict)

##s=open('my_file.txt')
##print(s)
##s.close()
##read_file=open('my_file.txt','r')
##rf=read_file.read()
##print(rf)
##read_file.close()

##with open('story.txt', 'r') as read_file:
##    title=read_file.readline()
##    print(title)
##    print(title.upper())
##    for line in read_file:
####        print(line.strip('.'))
####
####
##
##with open('bestmovies.txt','a') as b:
##    b.write('encanto ')
##    b.write('bluey')
##    
##with open('your_name.txt','w') as f:
##    name = input("What is your name, user?")
##    f.write("last person to run this code is: " + name + "\n")
##    f.close()
##
##with open('candy_text.txt','r') as candy:
##    content=candy.readlines()
##    ##print(content)
##    candy_names=[]
##    candies={}
##    for line in content:
####        print(line)
##        temp=line.split(',')
####        print(temp)
##        candy_names.append(temp[0])
####        candies[temp[0]]=temp[1]
##print(candies)
##print(candy_names)

##
##poem=open('long_poem.txt','r')
##writing=poem.readline()
##print(writing)
##poem2=open('second_poem.txt','r')
##writer=poem2.read()
##print(writer.strip())
##writer.close()

##with open ('all_coders.txt','a') as coder:
##    while True:
##        a=input('What is your name: ')
##        if a=='exit':
##            break
##        coder.write(a)
##        coder.write('\n')

##open with open('file_knownledge.txt','a') as f:
##        f.write('opening a file in write mode erases prior codes and you cannot retrieve them')
##        f.close()

##with open ('pattern.txt', 'a') as pattern:
##        for i in range(11,0,-1):
##            pattern.write('*'*i)
##            pattern.write('\n')
##a=open('pattern.txt','r')
##info=a.read()
##print(info)

##A-8
B-3
##C-5
##D-4
E-1
##F-7

