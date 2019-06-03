import boto3
   
dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('demo-sls-person')
   
def get_person(id):
    response = table.get_item(
            Key={
                 'person_id': id
            }
        )
    return response['Item']
           
def hello(event, context):
    person = get_person('001')
    return person

def get_persons():
    response = table.scan()
    return response['Items']
     
def hello(event, context):
    return get_persons() if event['person_id'] == '' else get_person(event['person_id'])