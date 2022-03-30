'''
lab 6
'''
#3.1
for i in range(6):
    if i != 3:
        print(i)
    
#3.2
result = 1

for i in range(1,6):
    print(i)
    


    result = result * i
    print(result)

#3.3
sig = 0

for n in range(1,6):
    print(n)
    
    sig = sig + n
    print(sig)
    
#3.4
result = 1
for i in range (3,9):
    print(i)
    
    result = result * i
    print(result)
    
#3.5
result = 1
for i in range(1,9):
   print(i)
    
for j in range(1,4):
 print(j)
    
result = result * (i/j)
print(result)

#3.6
for word in 'this is my 6th string'.split():
    print(len(word))
    
#3.7
my_tweet = {
    "favorite_count":1138,
"lang": "en",
"coordinates": (-75, 40),
"entities": { 'hashtags': ["Preds", "Pens", "SingIntoSpring"]}
}

print(my_tweet['entities'])

result = 0
for hashtag in my_tweet['entities']['hashtag']:
    result = result + 1
print(result)

    



    
