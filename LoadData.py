import pymongo 

url = 'mongodb+srv://shahin-yusifli-98:<password>@cluster0.io3ts.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

    




class LoadData:
    

    def __init__(self, db_name, password):
        
        self.db_name = db_name
        self.password = password
    
    def create_db_connection(self):

        client = pymongo.MongoClient("mongodb+srv://shahin-yusifli-98:<"+self.password+">@cluster0.io3ts.mongodb.net/"+self.db_name+"?retryWrites=true&w=majority")
        db = client.test
        mycol = db["cloud_network_secuirty"]
        print(db)


class UpdateData:
    

    # show_difference function shows difference between current data and
    # new data whcih we want to update with them. 
    def show_difference(self):
        pass

    # update function updates data if differences are logical or acceptable which
    # this statemnt is given by show_difference function. 
    def update(self):
        pass

    # archive_updates function archives changes which was done with
    # refresing.
    def archive_updates(self):
        pass






data = LoadData('Cluster0', 'Nadya437saral',)
data.create_db_connection()