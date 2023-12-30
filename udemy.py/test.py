#SOLUTION

#1 - 
st = "Print only the words that starts with s in this sentences"
for words in st.split():
    if words[0].lower() == "s":
        print(words)
        
# 3- 
[x for x in range(1,51) if x%3 ==0 ]

#4- 
for worlds in st.split():
    if len (words) % 2 == 0 :
        print (words+ "is even")

#5 -
for num in range (1,101): #IMPORTANT QUES
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)

#6 - 
[word[0] for word in st.split()]
print(words)