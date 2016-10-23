import pymongo
import requests
from array import array

client = pymongo.MongoClient()

my_array=[

for i in range(0,157):
    response = requests.get("http://sis.rutgers.edu/soc/courses.json?semester=12017&subject=%s&campus=NB&level=U%%2CG"%(my_array[i]))
    client.rutgers.classinfo.insert(response.json())
