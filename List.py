#create
fruits = ["apple", "banana", "cherry"] 
print(fruits)
print(fruits[1]) 

#modify
fruits[0]="Mango" 
print(fruits) 

#append
fruits.append("Grape")
print(fruits)

#insert
fruits.insert(1, "Orange")
print(fruits)

#remove
fruits.remove("Mango")
print(fruits)

#pop
fruits.pop(1)
print(fruits)

#forloop 
for fruit in fruits:
    print(fruit)
  