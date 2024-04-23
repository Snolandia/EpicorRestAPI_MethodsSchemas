import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.ServerPathSvc
# Description: Performs operations on server-side paths.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.ServerPathSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.ServerPathSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetPaths(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPaths
   Description: Retrieve a list of paths from the server.
   OperationID: GetPaths
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPaths_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPaths_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ServerPathSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ServerDirectoryExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ServerDirectoryExists
   Description: Determines whether the given path refers to an existing directory on the server.
   OperationID: ServerDirectoryExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ServerDirectoryExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ServerDirectoryExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ServerPathSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetPaths_input:
   """ Required : 
   folder
   subfolder
   includeFiles
   """  
   def __init__(self, obj):
      self.folder:int = obj["folder"]
      self.subfolder:str = obj["subfolder"]
      self.includeFiles:bool = obj["includeFiles"]
      pass

class GetPaths_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_ServerPath_Types_PathInfo] = obj["returnObj"]
      pass

class Ice_Lib_ServerPath_Types_PathInfo:
   def __init__(self, obj):
      self.IsFile:bool = obj["IsFile"]
      self.FullName:str = obj["FullName"]
      self.LastWriteTimeUtc:str = obj["LastWriteTimeUtc"]
      self.Length:int = obj["Length"]
      pass

class ServerDirectoryExists_input:
   """ Required : 
   folder
   subfolder
   """  
   def __init__(self, obj):
      self.folder:int = obj["folder"]
      """  The root of the path  """  
      self.subfolder:str = obj["subfolder"]
      """  The folder to test  """  
      pass

class ServerDirectoryExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

