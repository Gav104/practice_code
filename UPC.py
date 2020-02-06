import requests
import json
import csv

UPC = input("What is the UPC? - ")
UPCResult = ("https://api.upcitemdb.com/prod/trial/lookup?upc=" + UPC)
UPCResult # Website / URL we will contact
wjdata = requests.get(UPCResult).json()

print('\n')

dataset = (wjdata['items'][0])

print(dataset)
print(type(dataset))
print("-")


for k in dataset:
    print("{}: {}".format(k, dataset[k]))
print("-")
for key,val in dataset.items():
    print(key,":", val)

print("-")
variable = dataset.get('description', None)
print(variable)




