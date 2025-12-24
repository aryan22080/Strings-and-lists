#q1
l = [1,2,3,10]
count = 0
sum = 0
for i in range(len(l)):
    sum = sum + l[i]
    avg = sum/len(l)
print(avg)
if(l[i]>=avg):
  count+=1
print(count)
    
#q23
l = [1,2,3]
l11 = l.copy()
l11.reverse()
if(l11==l):
   print("Palindrome")
else:
   print("Not a palindrome")
#q26
l15 = [5,10,15,20]
sum = 0
for i in range(len(l15)):
   if(i%2==0):
      sum = sum + l15[i]
print(sum)
#q27 (new commit)
l16 = [1,2,1]
l17 = l16.copy()
l17.reverse()
if(l17==l16):
   print("True")
else:
   print("False")
#q47
s = "python"
for i in range(len(s)):
  if(i%2!=0):
    s1 = s.replace("python","pto")
print(s1)
#q44
s1 = "hello world"
s2 = s1.title()
print(s2)
#q30
s3 = "python"
print(s3[2:4])
#q5
s12 = "apple"
s13 = list(s12)
print(s13)
for i in range(len(s13)):
  s14 = s13.count(s13[i])
  print(s13[i],s14)
#q11
s17 = "python"
count = 0
for i in range(len(s17)):
  if(s17[i]!="a" and s17[i]!="e" and s17[i]!="i" and s17[i]!="o" and s17[i]!="u"):
    count = count + 1
print(count)
#q8
li = [3,5,1,4]
max = li[0]
for i in range(len(li)):
  if(li[i]>max):
    print("Second max value:",li[i])