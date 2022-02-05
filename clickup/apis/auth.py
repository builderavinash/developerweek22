import requests
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from threading import Thread, Lock
from os.path import exists

code=''
mutex = Lock()

def getAuthToken(client_id, client_secret):
    if isValidAuthTokenPresent():
        return getSavedAuthToken()

    global code
    getCode(client_id)

    url = f'https://api.clickup.com/api/v2/oauth/token?client_id={client_id}&client_secret={client_secret}&code={code}'
    access_token=requests.post(url).json()['access_token']
    print('access_token ', access_token)

    saveAuthToken(access_token)

    return access_token

def getAuthorizedUser(token):
    response=requests.get('https://api.clickup.com/api/v2/user', headers={'Authorization': token})
    print('response ', response.text)

# this part would be done in client
def getCode(client_id):
    address='0.0.0.0'
    port=4000
    redirect_uri = f'http://{address}:{port}'

    url = f'https://app.clickup.com/api?client_id={client_id}&redirect_uri={redirect_uri}'
    webbrowser.get(using='chrome').open(url)

    webServer = HTTPServer((address, port), clickupAuthServer)
    thread=Thread(name='daemon_server', target=webServer.serve_forever, daemon = True)
    thread.start()
    mutex.acquire()
    mutex.acquire()
    webServer.server_close()

    return ""

class clickupAuthServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global code
        query=parse_qs(urlparse(self.path).query)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("OK", "utf-8"))
        if 'code' in query:
            code = query['code'][0]
            print('code is ', code)
            mutex.release()

def getAuthTokenFileName():
    return 'token.out'

def isValidAuthTokenPresent():
    filename=getAuthTokenFileName()
    if not exists(filename):
        return False
    token=getSavedAuthToken()
    return True

def getSavedAuthToken():
    filename=getAuthTokenFileName()
    if not exists(filename):
        return ''
    token=open(filename).read()
    print(token, ' <-- saved token')
    return token

def saveAuthToken(access_token):
    file=open(getAuthTokenFileName(), 'w')
    file.write(access_token)
    file.close()