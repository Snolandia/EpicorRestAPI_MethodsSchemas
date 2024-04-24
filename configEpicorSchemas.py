import base64

epicorURL = "https://centralusdtapp34.epicorsaas.com/SaaS840/api/v1/"
b64 = base64.b64encode(('jgrissom:Nimsgotadoor!1').encode("ascii")).decode("ascii") 
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
    
