import requests

redirect_uri='https://app.clickup.com'

def getAuthToken(client_id, client_secret):
    urlForCode = 'https://app.clickup.com/api?client_id={client_id}&redirect_uri={redirect_uri}/20529126'
    # requests.post(urlForCode, headers={'host': redirect_uri})

    print(requests.post(urlForCode, headers={'host': redirect_uri}).text)

    # urlForToken = 'https://api.clickup.com/api/v2/oauth/token?client_id={client_id}&client_secret={client_secret}&code='
    # requests.post(request2)