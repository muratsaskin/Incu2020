import pymongo

#By using MongoShell, a database has already been created with credentials:---------------------------------------------
    #database name: Device_Configuration
    #collection: Interfaces
    #username: svetlana
    #password: cisco123
    #running on: localhost:27017

#Now, let's connect to our database with these credentials by using PyMongo:--------------------------------------------
with pymongo.MongoClient("mongodb://svetlana:cisco123@localhost:27017/Device_Configuration") as client:
    db = client.Device_Configuration
    collection = db.Interfaces

#We are connected! It's time to populate our collection, "Interfaces", with information from "interfaces.txt" file:-----
#We are defining a function to handle that:-----------------------------------------------------------------------------
def PopulateMyCollection(SW,INF,DES,STA):
    collection.insert_one({
        "Switch_name" : SW,
        "Interface_Name" : INF,
        "Description" : DES,
        "State" : STA})

#Our function is ready! Let's populate the collection!-----------------------------------------------------------------
#It is better to adopt an automated approach in this step for importing data from "interfaces.txt"----------------------
#Let's leave this for a future upgrade!---------------------------------------------------------------------------------
PopulateMyCollection("bru-dna-1","int g1/0","Connected to the switch2 gi1/2","up")
PopulateMyCollection("bru-dna-1","int fc1/1/0","connected to the storage port 1","up")
PopulateMyCollection("mastodon","int GigabitEthernet1/0/3","Connected to printer CX2","up")
PopulateMyCollection("mastodon","int GigabitEthernet1/0/5","Connected to printer CX4","down")
PopulateMyCollection("mastodon","int GigabitEthernet1/4/3","Connected to server SERV1","up")

