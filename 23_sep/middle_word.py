#print the middle word of a sentence
st=str(input("Enter the string-"))
middle_idx=len(st)//2
wd=st.split(" ")
if(wd%2==0):
    print(st[middle_idx-1:middle_idx+1])
else:
    print(st[middle_idx])


            