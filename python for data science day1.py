#create datatype
a=3
print(a)
type(a)
b=7.21
print(b)
c="hello"
print(c)
#to know datatype of variables
print(type(a))
print(type(b))
print(type(c))

#add sentence with output(combine text and variable)
d="data"
s="science"
print("python with "+d+" "+s)   #it will print "python with data science"

#LIST
e=["orange","mango","banana","papaya"]
print(e)
print(e[0])   #for "orange"
print(e[-2])  #for "orange"
print(e[-1])

#LIST SLICING
f=[1,2,3,4,5,6,7,8,9]
print(f[0:4])    #f(starting position:ending position)
print(f[2:4])

#APPEND
f.append("number")
print(f)

f.append(45)
print(f)

#EXTEND
f.extend(e)
print(f)

#TUPLE
tupl=("c++","java","python","R")
print(tupl)
print(tupl[0])  #c++ position

#DICTIONARY
DICSIONRY={"ML":"MACHINE LEARNING","AI":"ARTIFICIAL INTELLIGENCE","BIG ":"DATA","HAD":"DOP","R":"PYTHON"}
print(DICSIONRY)
print(DICSIONRY["ML"])
DICSIONRY["BI"]="BUISNESS INTELLEGENCE "   #TO ADD NEW ONE
print(DICSIONRY)

print(DICSIONRY.items())

print(DICSIONRY.values())

print(DICSIONRY.keys())

#CONDITIONS IF-ELSE STATEMENT

num1=10
num2=20      
if num1>num2:
    print("num1 is greater than num2")
else:
     print("num2 is greater than num1") 
     

num3=35
num4=25    
if num3>num4:
    print("num3 is greater than num4")
else:
     print("num4 is greater than num3") 
print("DONE")
         
# WHILE LOOPING

num5=1
while num5<6:
     print(num5)
     num5+=1               #"num5" is variable
     
num6=1
while num6<6:
     print(num6)
     num6+=1               #"num6" is variable
else:
      print("while loop is finished")
      
# FOR LOOPING
      
listFORloop=["mango","apple","banana","orange"] 
for x in listFORloop:
                    print(x) 
                    
listFORloop1="ANY NAME "
for y in listFORloop1:
                    print(y)  
                    
numbers=[1,2,3,4,5]  
values=["first","second","third","fourth","fifth"]          
for x in numbers:
   for y in values:
      print(x,y)

values=["first","second","third","fourth","fifth"]         
for x in values:
      print(x) 
      if x=="second":
         break
print("DONE")        

values=["first","second","third","fourth","fifth"]         
for x in values:
      if x=="second":      
         continue
      print(x)           
                    
      
     
        
          
