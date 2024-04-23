import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.SetupInfoSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.SetupInfoSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.SetupInfoSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetSetupInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSetupInfo
   Description: Gets the setup information.
   OperationID: GetSetupInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSetupInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSetupInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SetupInfoSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveSetupInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveSetupInfo
   Description: Saves the setup information.
   OperationID: SaveSetupInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveSetupInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveSetupInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SetupInfoSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearInUse(epicorHeaders = None):
   """  
   Summary: Invoke method ClearInUse
   Description: Clear in use table
   OperationID: ClearInUse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearInUse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.SetupInfoSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ClearInUse_output:
   def __init__(self, obj):
      pass

class GetSetupInfo_input:
   """ Required : 
   userFile
   """  
   def __init__(self, obj):
      self.userFile:bool = obj["userFile"]
      """  Type of file to get  """  
      pass

class GetSetupInfo_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class SaveSetupInfo_input:
   """ Required : 
   info
   userFile
   """  
   def __init__(self, obj):
      self.info      #schema had no properties on an object.
      """  The information.  """  
      self.userFile:bool = obj["userFile"]
      """  Type of file to get  """  
      pass

class SaveSetupInfo_output:
   def __init__(self, obj):
      pass

