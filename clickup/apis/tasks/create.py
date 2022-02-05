import requests

def newTask(access_token, list_id, data=''):
  response=requests.post(f'https://api.clickup.com/api/v2/list/{list_id}/task',
                         data=getTaskObj(),
                        headers={'Authorization': access_token,'Content-Type': 'application/json'})
  print(response.text)
  task_id=response.json()['id']
  print('task_id', task_id)
  return task_id



def getTaskObj():
  obj = """
  {
    "name": "do this",
    "description": "New Task Description",
    "assignees": [
      183
    ],
    "tags": [
      "tag name 1"
    ],
    "status": "Open",
    "priority": 3,
    "due_date": 1508369194377,
    "due_date_time": false,
    "time_estimate": 8640000,
    "start_date": 1567780450202,
    "start_date_time": false,
    "notify_all": true,
    "parent": null,
    "links_to": null,
    "check_required_custom_fields": true,
    "custom_fields": [
      {
        "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
        "value": 23
      },
      {
        "id": "03efda77-c7a0-42d3-8afd-fd546353c2f5",
        "value": "Text field input"
      }
    ]
  }
  """
  return obj