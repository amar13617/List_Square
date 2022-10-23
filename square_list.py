import json

def handler(event, context):
  print('received event:')
  print(event)
  list1 = event.get("data")
  operation = event.get("operation")
  if operation == "find_square":
    return find_square(list1)
  else:
    return {

    }
def find_square(data):
    res = []
    for i in data:
        res.append(i*i)
    
    return {
        "find_square" : res
    }