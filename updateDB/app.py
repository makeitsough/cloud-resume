import boto3
from decimal import Decimal

def handler(event, context, dynamodb_resource=None):
    if not dynamodb_resource:
        dynamodb_resource = boto3.resource('dynamodb')

    table = dynamodb_resource.Table('view-count')  # Replace 'your_table_name' with the actual table name
    response = table.get_item(Key={'id': '0'})

    item = response.get('Item', {})
    views = item.get('views', 0)
    new_views = views + 1

    # Convert the new_views to an integer before putting it in the table
    new_views = int(new_views)

    table.put_item(Item={'id': '0', 'views': new_views})

    return new_views

    ## test comment 8:49 8/12