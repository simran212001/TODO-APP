"""this is third party application through which we can operate CRUD operations.
Third party application can be in any language or anywhere , it can be a mobile app or website or anything
"""

import json
import requests
URL = "http://127.0.0.1:8000/"
URL2 = "http://127.0.0.1:8000/task-detail/16/"
URL3 = "http://127.0.0.1:8000/task-create/"
URL4 = "http://127.0.0.1:8000/task-update/19/"
URL5 = "http://127.0.0.1:8000/task-delete/16/"
'''
We want to extract data from database table
sent request to get the data
'''
# calling the function 
def get_data(id = None):

    data = {}
    if id is not None:
        data = {'id':id}
    # converting python data to json
    json_data = json.dumps(data)
    # requesting to get json data
    r = requests.get(url=URL , data = json_data)
    data = r.json()
    print(data)
# get_data(id ='2')      //got the data for id =2
# get_data()               

def detail_data():
    data = {
        # we have to mention the id for the details
        'id ':16
    }

    json_data = json.dumps(data)
    r = requests.get(url= URL2 , data=json_data)
    data = r.json()
    print(data)
# detail_data()



# Code for request to post/create the data
def post_data():
# python data
    data ={
        'task_title':'Internship',
        'task_desc':'Creating todo app ,and this is third party application'
    }
    # converting python to json data
    # json_data = json.dumps(data)
    # requesting url to post the data in the database table
    r = requests.post(url=URL3 , data= data)
    # data = r.json()
    print(data)
# post_data()



# Function for updating the data
def update_data():
    data = {
        # we have to mention the id for updating the details
        'id ':19,
        # lets we want to change the name and city for id 3
        'task_title':'Tutorial',
        'task_desc':'Django learning tutorial'
    }
    # python to json
    # json_data = json.dumps(data)
    # requesting url for updating the data in the database table
    r = requests.post(url= URL4 , data=data)
    # data = r.json()
    print(data)
update_data()


# Function for deleting the data
def delete_data():

    data={
        'id':16
    }
    # python to json
    json_data = json.dumps(data)
    # requesting url to delete the data for the mention id 
    r = requests.delete(url = URL5 ,data=json_data)
    data = r.json()
    print(data)
# delete_data()





# {
# "task_title" :
# "task_desc":
# }


# e:/Django/TODO/newenv/Scripts/Activate.ps1