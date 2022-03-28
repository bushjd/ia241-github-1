'''
lab 8 
'''
#3.1
def count_words(input_string):
    return ( (len(input_string.split() ))) 

#3.2
demo_string = "hi, Hello World!"

print(count_words(demo_string))

#3.3
def minimal_num(num_list):
 
    min_item = num_list[-1]
    
    for num in num_list:
        if num is not str:
          if min_item>= num:
            min_item = num
        


    return (min_item)
  
#3.4
demo_list = [2,3,4,5,6,7,8]
print(minimal_num(demo_list))

#3.5 Mixed list

mix_list = [1,2,3,4,'a', 4,5,6]

print (minimal_num(mix_list))










