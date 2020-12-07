import boto3

#class Command:
#    def __init__(self, description, 

class Config:
    dynamodb = boto3.resource('dynamodb')
    
    def __init__(self, table_name):
        self.table = self.dynamodb.Table(table_name)
    
    def get(self, key):
        response = self.table.get_item(Key = {'Key' : key}, ConsistentRead = True)
        return response['Item']['Value']
    def put(self, key, value): 
        self.table.put_item(Item = {'Key' : key, 'Value' : value})
        
config = Config('BonkBotConfig')
    

# using the singleton pattern
def get_instance():
    return config
