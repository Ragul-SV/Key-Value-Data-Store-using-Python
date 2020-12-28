
import time
import json


d = {} #Creating a dictionary to store all key-value pairs
 
"""
Syntax: 
1) Create Operation : create(key,value,time_to_live)  #time_to_live argument is optional
2) Read Operation   : read(key) 
2) Delete Operation : delete(key) 
"""

FILE_SIZE = 1073741824  # 1GB  ----> pow(2,10)*pow(2,10)*pow(2,10) Bytes
JSON_SIZE = 16384		   # 16KB ----> 16 * pow(2,10) Bytes

#CREATE
def create(key,value,time_to_live=0):
    if key not in d:
        if(key.isalpha()):	#Key must contain only alphabets. No numbers or Special Symbols.
            if len(d)<FILE_SIZE and value<=JSON_SIZE and len(key)<=32:  # Memory Limit Constraints
                if time_to_live==0:
                    d[key]=[value,time_to_live]
                    print("Key",key,"Created")
                else:
                    d[key]=[value,time.time()+time_to_live]
                    print("Key",key,"Created")
            else:
                print("Memory Limit Exceeded!!!")
        else:
            print("Key must contain only Alphabets!!!")
    else:
    	print("Key",key,"Already Exists!!!") 

#READ   
def read(key):
    if key in d:
        if d[key][1]==0:	# If time_to_live value is not specified for the key
        	json_object = json.dumps({key:+d[key][0]}, indent = 4)   
        	print(json_object)  
        	# print(str(key)+":"+str(d[key][0]))
        else:
            if time.time()<d[key][1]: 	  #comparing present time with time to live value of the key
                print(str(key)+" : "+str(d[key][0]) )
            else:
                print("Time to Live of Key "+str(key)+" has expired!!!"); 
    else:
    	print("Key",key,"does not exist");

#DELETE
def delete(key):
    if key not in d:
        print("Key",key,"does not exist!!!")
    else:
        if d[key][1]==0:	# If time_to_live value is not specified for the key
        	del d[key]
        	print("Key",key,"Deleted")
        else:
            if time.time()<d[key][1]:	 #comparing present time with time to live value of the key
                del d[key]
                print("Key",key,"Deleted")
            else:
                print("Time to Live of Key "+str(key)+" has expired!!!") 
