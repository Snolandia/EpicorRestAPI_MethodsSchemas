import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.FileStoreSvc
# Description: File storage on the server
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.FileStoreSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.FileStoreSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_Create(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Create
   Description: Create a new file
   OperationID: Create
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Create_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Create_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileStoreSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WriteAllBytes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WriteAllBytes
   Description: Overwrite an existing file
   OperationID: WriteAllBytes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WriteAllBytes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WriteAllBytes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileStoreSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReadAllBytes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReadAllBytes
   Description: Read a file.
   OperationID: ReadAllBytes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReadAllBytes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReadAllBytes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileStoreSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Delete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Delete
   Description: Deletes the specified file.
   OperationID: Delete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Delete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Delete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileStoreSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReadAllFiles(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReadAllFiles
   OperationID: ReadAllFiles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReadAllFiles_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReadAllFiles_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileStoreSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Create_input:
   """ Required : 
   bytes
   foreignSysRowID
   relatedToSchemaName
   relatedToTable
   fileName
   companyID
   tenantID
   secCode
   """  
   def __init__(self, obj):
      self.bytes:str = obj["bytes"]
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTable:str = obj["relatedToTable"]
      self.fileName:str = obj["fileName"]
      self.companyID:str = obj["companyID"]
      self.tenantID:str = obj["tenantID"]
      self.secCode:str = obj["secCode"]
      pass

class Create_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class Delete_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class Delete_output:
   def __init__(self, obj):
      pass

class Ice_Lib_StoredFile:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      self.FileName:str = obj["FileName"]
      self.Contents:str = obj["Contents"]
      pass

class ReadAllBytes_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class ReadAllBytes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.fileName:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReadAllFiles_input:
   """ Required : 
   foreignSysRowID
   """  
   def __init__(self, obj):
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      pass

class ReadAllFiles_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_StoredFile] = obj["returnObj"]
      pass

class WriteAllBytes_input:
   """ Required : 
   id
   bytes
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      self.bytes:str = obj["bytes"]
      pass

class WriteAllBytes_output:
   def __init__(self, obj):
      pass

