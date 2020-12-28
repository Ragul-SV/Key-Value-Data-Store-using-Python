# Key-Value-Data-Store-using-Python

Created a key-value data store that supports the basic CRD(create, read and delete) operations using python. 

Memory Constraints:
1) Key is always a string with maximum of 32 characters
2) Data Store size limit is 1 GB
3) Values size limit is 16 KB

Error Responses Addressed:
1) All the memory constraints must be satisfied
2) Key not Found Error - If key is not present in dictionary during read/delete operations
3) Key Already Exists Error - If key already exists during create operation
4) Key must only contain alphabets Error - If key contains any numeric or special characters
5) Time_to_live of Key has expired Error - If time to live vlaue of key has expired during read/delete operations

Keys can have time to live (in seconds) property when created.
A client process is allowed to access data store using multiple threads (Multithreading).

The data store is then exported into a json file - "output.json".

To start the application, run the command: python run.py
