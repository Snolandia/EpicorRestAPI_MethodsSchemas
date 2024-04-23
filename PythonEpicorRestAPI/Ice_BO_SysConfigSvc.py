import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.SysConfigSvc
# Description: The SysConfig service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysConfigSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysConfigSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetValue
   Description: Get a system configuration value.
   OperationID: GetValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysConfigSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PassSessionValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PassSessionValues
   Description: Pass Session Values to server side to retrieve the instance details and return it to client
   OperationID: PassSessionValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PassSessionValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PassSessionValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysConfigSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGrowUrl(epicorHeaders = None):
   """  
   Summary: Invoke method GetGrowUrl
   Description: Gets the GrowUrl for the current company
   OperationID: GetGrowUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGrowUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysConfigSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SetGrowUrl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetGrowUrl
   Description: Sets the GrowUrl and associated token.
   OperationID: SetGrowUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetGrowUrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetGrowUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysConfigSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteGrowSettings(epicorHeaders = None):
   """  
   Summary: Invoke method DeleteGrowSettings
   Description: Deletes the Grow settings for the current company.
   OperationID: DeleteGrowSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteGrowSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysConfigSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DeleteGrowSettings_output:
   def __init__(self, obj):
      pass

class GetGrowUrl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetValue_input:
   """ Required : 
   companyID
   key1
   key2
   key3
   defaultValue
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  The company identifier.  """  
      self.key1:str = obj["key1"]
      """  The key1.  """  
      self.key2:str = obj["key2"]
      """  The key2.  """  
      self.key3:str = obj["key3"]
      """  The key3.  """  
      self.defaultValue:str = obj["defaultValue"]
      """  The default value.  """  
      pass

class GetValue_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The configured value or the default value if not configured.  """  
      pass

class PassSessionValues_input:
   """ Required : 
   url
   company
   """  
   def __init__(self, obj):
      self.url:str = obj["url"]
      self.company:str = obj["company"]
      pass

class PassSessionValues_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class SetGrowUrl_input:
   """ Required : 
   key2
   sysCharacter01
   """  
   def __init__(self, obj):
      self.key2:str = obj["key2"]
      """  The Grow Url  """  
      self.sysCharacter01:str = obj["sysCharacter01"]
      """  The Grow token  """  
      pass

class SetGrowUrl_output:
   def __init__(self, obj):
      pass

