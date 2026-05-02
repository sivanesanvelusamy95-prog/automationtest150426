#print natural numbers using while loop
#i =0
#while i<=10:
 #  print(i)
  # i+=1

#print -9 to -1 using for loop
#for i in range(-9,0):
 #  print(i)
  # i-=1 

#for i in range(5):
 #  print(i)
#else:
 #  print("Done!")      

 #sum of all the numbers from 1 to 10
#sum=0
#for i in range(11):
 #  sum=sum+i
  # i+=1
#else:
 #  print(sum) 


#Print multiplication table of a given number
#for i in range(0,20,2):
 #   print(i) 

#Calculate the cube of all numbers from 1 to a given number
#for i in range(6):
 #   i=i*i*i
  #  print(i)

# Display numbers from a list using a loop
#lst = ["12", "75", "150", "180", "145", "525", "50"]
#for number in lst:
 #  number= int(number) 
  # if number>500:
   #   break

   #elif number>150:
    #  continue   

   #elif number%5==0:
    #  print(number)   

 #Count occurrences of a specific element in a list  
#list1 = ["10", "20", "10", "30", "10", "40", "50"] 
#count=0
#for item in list1:
 #  if item == "10":
  #    count =count+1
   #   print(count)             
   
 #Print elements from a list present at odd index positions
#my_list = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
#for items in range(20,120,20):
 #  print(items)  

 #Print list in reverse order using a loop
#list1 = ["10", "20", "30", "40", "50"]
#for items in reversed(list1):
 #  print(items)

#Reverse a string using a for loop
#originalstr="Sivanesh"
#Reversedstr=" "
#for char in originalstr:
 #  Reversedstr= char + Reversedstr
   
#print("Original:" + originalstr)
#print("Reversed:" + Reversedstr)

#Count vowels and consonants in a sentence
#Originalstr="Loops are Fun!"
#vowels="aeiou"
#consonants=0
#count=0
#for char in Originalstr.lower():
 # if char.isalpha(): 
  #  if char in vowels:
   #   count = count +1
    #else:  
     # consonants=consonants+1

#print("Vowelscount:" ,count)
#print("Constantscount:" ,consonants)

#Count total number of digits in a number
#number =75869
#count=0
#while number!=0:
 #   number =number//10
  #  count=count+1

#print(count)  

#Reverse an integer number
num=78654
rvrdigit=0
while num>0:
  digit=num%10
  rvrdigit=(rvrdigit*10)+digit
  num=num//10 
 
print(rvrdigit)  