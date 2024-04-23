import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.InAppNotificationsSvc
# Description: Provides methods to retrieve Notifications for license/user
and to get Notification content
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetNotificationsForCurrentUserKeepIdleTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNotificationsForCurrentUserKeepIdleTime
   Description: Calls M:Ice.Services.Lib.InAppNotificationsSvc.GetNotificationsForCurrentUser(System.String,System.String,System.String,System.String,System.String) without affecting the session's last accessed time.
   OperationID: GetNotificationsForCurrentUserKeepIdleTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNotificationsForCurrentUserKeepIdleTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNotificationsForCurrentUserKeepIdleTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNotificationsForCurrentUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNotificationsForCurrentUser
   Description: Retrieve the unread notifications for the given user
(which should be the currently logged one).
   OperationID: GetNotificationsForCurrentUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNotificationsForCurrentUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNotificationsForCurrentUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNotificationContent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNotificationContent
   Description: Retrieve the contents for a given Notification Id.
   OperationID: GetNotificationContent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNotificationContent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNotificationContent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUserPreferences(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUserPreferences
   Description: Retrieves User Preferences.
   OperationID: GetUserPreferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUserPreferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserPreferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.InAppNotificationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetNotificationContent_input:
   """ Required : 
   endpoint
   apiKey
   product
   notificationId
   """  
   def __init__(self, obj):
      self.endpoint:str = obj["endpoint"]
      """  Notifications APIM endpoint  """  
      self.apiKey:str = obj["apiKey"]
      """  subscription-key  """  
      self.product:str = obj["product"]
      """  ERP  """  
      self.notificationId:str = obj["notificationId"]
      """  Notification ID  """  
      pass

class GetNotificationContent_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetNotificationsForCurrentUserKeepIdleTime_input:
   """ Required : 
   endpoint
   apiKey
   product
   licenseId
   userId
   """  
   def __init__(self, obj):
      self.endpoint:str = obj["endpoint"]
      self.apiKey:str = obj["apiKey"]
      self.product:str = obj["product"]
      self.licenseId:str = obj["licenseId"]
      self.userId:str = obj["userId"]
      pass

class GetNotificationsForCurrentUserKeepIdleTime_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetNotificationsForCurrentUser_input:
   """ Required : 
   endpoint
   apiKey
   product
   licenseId
   userId
   """  
   def __init__(self, obj):
      self.endpoint:str = obj["endpoint"]
      """  Notifications APIM endpoint  """  
      self.apiKey:str = obj["apiKey"]
      """  subscription-key  """  
      self.product:str = obj["product"]
      """  ERP  """  
      self.licenseId:str = obj["licenseId"]
      """  License ID  """  
      self.userId:str = obj["userId"]
      """  User ID  """  
      pass

class GetNotificationsForCurrentUser_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetUserPreferences_input:
   """ Required : 
   userId
   licenseId
   product
   """  
   def __init__(self, obj):
      self.userId:str = obj["userId"]
      """  User ID  """  
      self.licenseId:str = obj["licenseId"]
      """  License ID  """  
      self.product:str = obj["product"]
      """  Product  """  
      pass

class GetUserPreferences_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

