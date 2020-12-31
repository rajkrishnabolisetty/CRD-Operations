#here are the commands to demonstrate how to access and perform operations on a main file
from threading import*


#run the MODULE of MAIN FILE and import mainfile as a library 

import main as x 
#importing the main file("code" is the name of the file I have used) as a library 


x.create("bookone",25)
#to create a key with key_name,value given and with no time-to-live property


x.create("booktwo",50,2500) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("bookone")
#it returns the value of the respective key in Jsonobject format 'key_name:value'


x.read("booktwo")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("bookthree",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


x.modify("booktwo",55)
#it replaces the initial value of the respective key with new value 

 
x.delete("booktwo")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(x.create or x.read or x.delete),args=("bookone",5)) #as per the operation
t1.start()
t2=Thread(target=(x.create or x.read or x.delete),args=("mohankrishna",2,10)) #as per the operation
t2.start()
#and so on upto tn
#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

