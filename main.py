import threading
#this is for python 3.0 and above. use import thread for python2.0 versions
from threading import*
import time
database={} #'database' is the dictionary in which we store data
#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout
def create(key,value,timeout=0):
    if key in database:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(database)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    temp=[value,timeout]
                else:
                    temp=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    database[key]=temp
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in database:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        currvalue=database[key] # Storing the current key's value in the temporary map to check the timeout condition.
        if currvalue[1]!=0:
            if time.time()<currvalue[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(currvalue[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(currvalue[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in database:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        currvalue=database[key]
        if currvalue[1]!=0:
            if time.time()<currvalue[1]: #comparing the current time with expiry time
                del database[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del database[key]
            print("key is successfully deleted")

#I have an additional operation of modify in order to change the value of key before its expiry time if provided

#for modify operation 
#use syntax "modify(key_name,new_value)"

def modify(key,value):
    b=database[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in database:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                database[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in database:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            database[key]=l



