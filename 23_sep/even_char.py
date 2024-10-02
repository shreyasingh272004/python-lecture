#print all the even position characters in a word
word =str(input("Enter a word-"))
s=""
for i in range(len(word)):
    if(i%2==0):
        s+=word[i]
print(s)
        


    


