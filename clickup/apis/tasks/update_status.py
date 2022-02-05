import requests

def closeTask(access_token, task_id):
  response=requests.put(f'https://api.clickup.com/api/v2/task/{task_id}',
                         data='{"status": "Complete"}',
                        headers={'Authorization': access_token,'Content-Type': 'application/json'})
  print(response.text)