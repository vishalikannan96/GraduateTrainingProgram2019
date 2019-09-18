1.a="Hakka and Bukka were brothers and warriors. The brothers wanted to build their own kingdom where people could live without fear. They collected a band of young men and trained "
a+="them in warfare. They lived in a forest hideout on the banks of the river Tungabhadra in South India. One day, the brothers were out on a hunt. Ferocious dogs accompanied them. "
a+="They crossed the river and rode on. A couple of frightened rabbits ran out of the bushes. The dogs gave them chase with the two brothers closely behind on their horses. "
a+="It was a long chase. The rabbits were running for their life. The dogs were catching up. Suddenly, in a swift move, the rabbits turned and faced the dogs. Taken aback by the "
a+="show of defiance, the barking dogs stepped back. Hakka called back the dogs. As the dogs turned back, the rabbits walked away. Hakka looked around. They were on the other side "
a+="of the Tungabhadra. It was a rocky land. The sun was blazing in the sky. “Strange! I’ve never seen rabbits challenging dogs before!” said Bukka. “That’s the quality of this land,” "
a+="said a quiet voice, “Even rabbits give fight.” Startled to hear a stranger speak, the two brothers turned. They saw a holy man walking towards them. He was a picture of peace. "
a+="At the same time, his eyes were blazing bright."

print(a)
length=len(a)
print(length)

b=a.split(" ")
noofwords=len(b)
print(noofwords)
print(b)

mydict={}
for i in b:
    if i not in mydict:
        mydict[i]=1
    else:
        mydict[i]+=1
print(mydict)
mylist=[]
for i in mydict:
    mylist.append(mydict[i])
max_occurance=max(mylist)
print(max_occurance)

for i,j in mydict.items():
    if j==max_occurance:
        max_occurance_word=i
print(max_occurance_word)

repeated_count=[]
for i in mylist:
    if i != 1:
        repeated_count.append(i)
print(repeated_count)

repeated_words=[]
for i,j in mydict.items():
    if j != 1:
        repeated_words.append(i)
print(repeated_words)

dictionary={"Length of string" : length,
            "Number of words" : noofwords,
            "Max Occurance" : max_occurance,
            "Max Occurance word" :max_occurance_word,
            "Repeated word's count" : repeated_count,
            "Repeated word's list" : repeated_words}

print(dictionary)

3.n=int(input("Enter a number: "))
temp=n
rev=0
while n != 0:
    dig= n % 10
    rev= rev * 10 + dig
    n= n // 10

if temp==rev:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")

n=int(input("Enter a number: "))
string=""
num=str(n)
mylist=list(num)
mylist.reverse()
for i in mylist:
    string=string+i
num=int(string)
if num == n:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")

5.str1=input("Enter the str1: ")
str2=input("Enter the str2: ")
list1=list(str1)
print(list1)
list2=list(str2)
print(list2)
list1.sort()
print(list1)
list2.sort()
print(list2)
stra=''.join(list1)
print(stra)
strb=''.join(list2)
print(strb)
if stra==strb:
    print("The given two strings are anagram")
else:
    print("The given two strings are not an anagram")


2.mydict={"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","plus":"+","minus":"-","divide":"/"}
inp=['five plus three','seven minus two','two plus eight minus five','eight divide four']

list1=[]
list2=[]
list3=[]
for j in inp:
    string = ""
    s=j.split(" ")
    for i in s:
        for k in mydict:
            if i==k:
                string+=mydict[k]
    list1.append(string)
for i in list1:
    res=eval(i)
    list2.append(str(int(res)))
for i in list2:
    for k,j in mydict.items():
        if i==j:
            list3.append(k)
print(list3)

