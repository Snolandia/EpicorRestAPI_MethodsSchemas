import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.FileTransferSvc
# Description: File transfer service. Enables the manipulation of server files from the client
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_DownloadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DownloadFile
   Description: Get a file's content from the server
   OperationID: DownloadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DownloadFileForCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DownloadFileForCompany
   Description: Get a file's content from the server
   OperationID: DownloadFileForCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadFileForCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFileForCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DownloadFileForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DownloadFileForUser
   Description: Get a file's content from the server
   OperationID: DownloadFileForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadFileForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFileForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UploadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadFile
   Description: Set a file's content on the server
   OperationID: UploadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FileExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FileExists
   Description: Check if file exists on the server.
   OperationID: FileExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FileDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FileDelete
   Description: Deletes the specified file. If not found, nothing happens
   OperationID: FileDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFileDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFileDetails
   Description: Get the file detail for specific files.
   OperationID: GetFileDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFileDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFileDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetEdgeAgentCdnDetails(operatingSystem, epicorHeaders = None):
   """  
   Summary: Invoke method GetEdgeAgentCdnDetails
   Description: Get URL and version for current Edge Agent installation for the specific operating system.
   OperationID: Get_GetEdgeAgentCdnDetails
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEdgeAgentCdnDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "operatingSystem=" + operatingSystem

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DownloadFileForCompany_input:
   """ Required : 
   folder
   serverPath
   companyID
   """  
   def __init__(self, obj):
      self.folder:int = obj["folder"]
      """  The root of the path  """  
      self.serverPath:str = obj["serverPath"]
      """  The path of the file to get the content for  """  
      self.companyID:str = obj["companyID"]
      pass

class DownloadFileForCompany_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  File data  """  
      pass

class DownloadFileForUser_input:
   """ Required : 
   folder
   serverPath
   userID
   """  
   def __init__(self, obj):
      self.folder:int = obj["folder"]
      """  The root of the path  """  
      self.serverPath:str = obj["serverPath"]
      """  The path of the file to get the content for  """  
      self.userID:str = obj["userID"]
      pass

class DownloadFileForUser_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  File data  """  
      pass

class DownloadFile_input:
   """ Required : 
   folder
   serverPath
   """  
   def __init__(self, obj):
      self.folder:int = obj["folder"]
      """  The root of the path  """  
      self.serverPath:str = obj["serverPath"]
      """  The path of the file to get the content for  """  
      pass

class DownloadFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  File data  """  
      pass

class FileDelete_input:
   """ Required : 
   folder
   serverPath
   """  
   def __init__(self, obj):
      self.folder:int = obj["folder"]
      """  The root of the path.  """  
      self.serverPath:str = obj["serverPath"]
      """  The path of the file to delete.  """  
      pass

class FileDelete_output:
   def __init__(self, obj):
      pass

class FileExists_input:
   """ Required : 
   folder
   serverPath
   """  
   def __init__(self, obj):
      self.folder:int = obj["folder"]
      """  The root of the path.  """  
      self.serverPath:str = obj["serverPath"]
      """  Path to the file on the server.  """  
      pass

class FileExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if exists  """  
      pass

class GetEdgeAgentCdnDetails_input:
   """ Required : 
   operatingSystem
   """  
   def __init__(self, obj):
      self.operatingSystem:str = obj["operatingSystem"]
      pass

class GetEdgeAgentCdnDetails_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetFileDetails_input:
   """ Required : 
   folder
   serverPath
   """  
   def __init__(self, obj):
      self.folder:int = obj["folder"]
      """  The root of the path.  """  
      self.serverPath:str = obj["serverPath"]
      """  Path to the file on the server.  """  
      pass

class GetFileDetails_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Dictionary with keys for FileInfo object: FileName, FileVersion, ProductVersion, ModifiedDate, SizeInByte.  """  
      pass

class UploadFile_input:
   """ Required : 
   folder
   serverPath
   data
   """  
   def __init__(self, obj):
      self.folder:int = obj["folder"]
      """  The root of the path  """  
      self.serverPath:str = obj["serverPath"]
      """  The path of the file to set the content to  """  
      self.data:str = obj["data"]
      """  File data  """  
      pass

class UploadFile_output:
   def __init__(self, obj):
      pass

