import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ConfigCheckSvc
# Description: The Annotations service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ConfigCheckSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ConfigCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_runConfigCheck(epicorHeaders = None):
   """  
   Summary: Invoke method runConfigCheck
   Description: Runs a series of rules to check the configuration of the E10 AppServer
   OperationID: runConfigCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/runConfigCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ConfigCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_CompactLOH(epicorHeaders = None):
   """  
   Summary: Invoke method CompactLOH
   Description: CompactLOH
   OperationID: CompactLOH
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompactLOH_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ConfigCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetInstanceDefinition(epicorHeaders = None):
   """  
   Summary: Invoke method GetInstanceDefinition
   Description: Gets the sysconfig rows that will define an instance, rows are purged every 60 days for stale records
   OperationID: GetInstanceDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstanceDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ConfigCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_zippedLogFiles(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method zippedLogFiles
   Description: Method used to retrieve the server log files from the server if there is any, returned files will be zipped
for convenience of travel over the wire using GZipStream
   OperationID: zippedLogFiles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/zippedLogFiles_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/zippedLogFiles_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ConfigCheckSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CompactLOH_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A string with a completion or failure message  """  
      pass

class GetInstanceDefinition_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class runConfigCheck_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A string that can then be transformed to a dataset using DataSet.ReadXML  """  
      pass

class zippedLogFiles_input:
   """ Required : 
   getOnlyLastItem
   """  
   def __init__(self, obj):
      self.getOnlyLastItem:bool = obj["getOnlyLastItem"]
      """  Get only the last server log file by name  """  
      pass

class zippedLogFiles_output:
   def __init__(self, obj):
      self.returnObj:object
      """  A list with a dictionary of the name and byte array of the server log file zipped  """  
      pass

