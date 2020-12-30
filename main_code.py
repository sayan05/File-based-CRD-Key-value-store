import threading
#this is for python 3.0 and above. use import thread for python2.0 versions
from threading import*
import time

object={} #'object' is the dictionary in which we store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in object:
        print("error: this key already exists") #error message if entered key already exists
    else:
        if(key.isalpha()):
            if len(object)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    object[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message if memeory limit exceeded
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message for not having any special character in the key

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in object:
        print("error: given key does not exist in database. Please enter a valid key") #error message if key doesn't exist
    else:
        b=object[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message if time-to-live has expired
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in object:
        print("error: given key does not exist in database. Please enter a valid key") #error message if key doesn't exist
    else:
        b=object[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del object[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message if time-to-live of the key expires
        else:
            del object[key]
            print("key is successfully deleted") #notification for key deletion

#I have an additional operation of modify in order to change the value of key before its expiry time if provided

#for modify operation 
#use syntax "modify(key_name,new_value)"

def modify(key,value):
    b=object[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in object:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                object[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message if time to live is expired
    else:
        if key not in object:
            print("error: given key does not exist in database. Please enter a valid key") #error message if the key doesn't exist
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            object[key]=l
