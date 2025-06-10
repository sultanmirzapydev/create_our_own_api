import requests
from .models import DataModel 


def call_api():
    params = {
            "startDate": "2025-06-01T00:00:00Z",
            "startTime": "00:00",
            "endTime": "23:59",
            "timeslot": 1,
            "columns": ["customerAccountId", "dialedNumberCountryIsoId"]
        }
    url = "https://mcm.beta.routetrust.com/api/rtSip/beta/asrSummary"
    headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjE1NDksImVtYWlsIjoicmF0ZXNAbXljb3VudHJ5bW9iaWxlLmNvbSIsInRmYUVuYWJsZWQiOmZhbHNlLCJ0ZmFWYWxpZGF0ZWQiOmZhbHNlLCJpYXQiOjE3NDkwMTk1MjYsImV4cCI6MTc0OTA1NTUyNn0.YCoG7p-N9NQLlNZRaWCyDzuOOecw4wg3147rkzQe21E"}
    response = requests.post(url, data= params, headers = headers)
    data = response.json()
    if len(data) <=2:
        return False 
    print(f"length {len(data)}")
    for item in data:
        
        item.pop('timeslot')
        print(item)
        DataModel(**item).save()  

    
# def aggregate(dataset):
#     for item in dataset:
