import base64

epicorURL = "YOUR_EPICOR_API_URL_HERE"
b64 = base64.b64encode(('USERNAME:PASSWORD').encode("ascii")).decode("ascii") 
epicorCreds = {'Authorization':'Basic ' + b64}

def encodeToBase64(str):
    return base64.b64encode((str).encode("ascii")).decode("ascii")

def encodeToBase64(username, password):
    return base64.b64encode((username + ":" + password).encode("ascii")).decode("ascii")

def setEpicorURL(str):
    global epicorURL
    epicorURL = str

def getEpicorURL():
    return epicorURL

def setEpicorCreds(creds):
    global epicorCreds
    epicorCreds = creds

def setEpicorCreds(username, password):
    global epicorCreds
    epicorCreds = base64.b64encode((username + ":" + password).encode("ascii")).decode("ascii")


