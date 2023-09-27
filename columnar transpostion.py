# take the key into a list
# num=(input("Enter Number: "))
# l=list(num)
# T3 = list(map(int, l))
# T1 = max(T3)
# print(T1)

#take the text length
#create the array
keymax = 4
text = "good dayqweqe"
z = len(text)
row = z% keymax
if(row == 0):
    row = int(z/keymax)
else:
    row = (int(z/keymax))+1    
rows, cols = (row, keymax)
arr = [["" for i in range(cols)] for j in range(rows)]
print(arr) 

#list the text in the array
index = 0
for i in range(rows):
    for j in range (cols):
        if(index < len(text)):
            arr[i][j] = text[index]
            index+=1
print (arr)

#ciphering the text
cipher = ""
keynum = 1234
keylist = [int(x) for x in str(keynum)]
key_index = 0

# read matrix column-wise using key
while(key_index<len(keylist)):
    for i in keylist:
        if(key_index+1 == keylist[i]):
            print("found number"+keylist[i])
            key_index+=1
  
   
