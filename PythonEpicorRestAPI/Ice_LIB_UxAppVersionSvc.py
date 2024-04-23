import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.UxAppVersionSvc
# Description: This Lib is designed to manage versioning for metafx apps/layers.
It contains apis to create, list and restore version for apps/layers
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetVersions(request, epicorHeaders = None):
   """  
   Summary: Invoke method GetVersions
   Description: Provides all versions for a layer or App
   OperationID: Get_GetVersions
      :param request: Desc: EpMetaFxRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_CreateVersion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateVersion
   Description: Create new version for layer or App
   OperationID: CreateVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUxAppVersions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUxAppVersions
   OperationID: GetUxAppVersions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUxAppVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUxAppVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PublishVersion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PublishVersion
   OperationID: PublishVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PublishVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PublishVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PublishBaseFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PublishBaseFile
   OperationID: PublishBaseFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PublishBaseFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PublishBaseFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BulkPublishBase(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BulkPublishBase
   OperationID: BulkPublishBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BulkPublishBase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BulkPublishBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBaseAppRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBaseAppRow
   OperationID: GetBaseAppRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBaseAppRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBaseAppRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BulkPublishLayers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BulkPublishLayers
   OperationID: BulkPublishLayers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BulkPublishLayers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BulkPublishLayers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteVersions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteVersions
   OperationID: DeleteVersions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BulkPublishBase_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_UxAppVersion_UxAppVersionRequest] = obj["request"]
      pass

class BulkPublishBase_output:
   def __init__(self, obj):
      pass

class BulkPublishLayers_input:
   """ Required : 
   uxVersionRequests
   """  
   def __init__(self, obj):
      self.uxVersionRequests:list[Ice_Lib_UxAppVersion_UxAppVersionRequest] = obj["uxVersionRequests"]
      pass

class BulkPublishLayers_output:
   def __init__(self, obj):
      pass

class CreateVersion_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_UxAppVersion_EpMetaFxRequest] = obj["request"]
      pass

class CreateVersion_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  List of UxAppVersionResponse  """  
      pass

class DeleteVersions_input:
   """ Required : 
   isBase
   appName
   layerName
   typeCode
   """  
   def __init__(self, obj):
      self.isBase:bool = obj["isBase"]
      self.appName:str = obj["appName"]
      self.layerName:str = obj["layerName"]
      self.typeCode:str = obj["typeCode"]
      pass

class DeleteVersions_output:
   def __init__(self, obj):
      pass

class GetBaseAppRow_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_UxAppVersion_UxAppVersionRequest] = obj["request"]
      pass

class GetBaseAppRow_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_UxAppVersion_UxAppVersionResponse] = obj["returnObj"]
      pass

class GetUxAppVersions_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_UxAppVersion_UxAppVersionRequest] = obj["request"]
      pass

class GetUxAppVersions_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_UxAppVersion_UxAppVersionResponse] = obj["returnObj"]
      pass

class GetVersions_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_UxAppVersion_EpMetaFxRequest] = obj["request"]
      pass

class GetVersions_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_UxAppVersion_UxAppVersionResponse] = obj["returnObj"]
      """  List of UxAppVersionResponse  """  
      pass

class Ice_Lib_UxAppVersion_EpMetaFxRequest:
   def __init__(self, obj):
      self.id:str = obj["id"]
      self.properties:list[Ice_Lib_UxAppVersion_EpMetaFxRequestProperty] = obj["properties"]
      pass

class Ice_Lib_UxAppVersion_EpMetaFxRequestProperty:
   def __init__(self, obj):
      self.layers:str = obj["layers"]
      self.layerType:str = obj["layerType"]
      self.deviceType:str = obj["deviceType"]
      self.mode:str = obj["mode"]
      self.userName:str = obj["userName"]
      self.pageName:str = obj["pageName"]
      self.company:str = obj["company"]
      self.countryGroupCode:str = obj["countryGroupCode"]
      self.debug:bool = obj["debug"]
      self.countryCode:str = obj["countryCode"]
      self.includeWasm:bool = obj["includeWasm"]
      self.applicationType:str = obj["applicationType"]
      self.additionalContext      #schema had no properties on an object.
      self.checkDuplicateIds:bool = obj["checkDuplicateIds"]
      self.layerVersion:int = obj["layerVersion"]
      self.baseAppVersion:int = obj["baseAppVersion"]
      self.comment:str = obj["comment"]
      pass

class Ice_Lib_UxAppVersion_UxAppVersionRequest:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Version:int = obj["Version"]
      self.TypeCode:str = obj["TypeCode"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.CGCCode:str = obj["CGCCode"]
      self.ProductID:str = obj["ProductID"]
      self.Content:str = obj["Content"]
      self.Comment:str = obj["Comment"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.IsPublish:bool = obj["IsPublish"]
      pass

class Ice_Lib_UxAppVersion_UxAppVersionResponse:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ProductID:str = obj["ProductID"]
      self.TypeCode:str = obj["TypeCode"]
      self.CGCCode:str = obj["CGCCode"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Version:int = obj["Version"]
      self.Content:str = obj["Content"]
      self.Comment:str = obj["Comment"]
      self.PublishDate:str = obj["PublishDate"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.CreatedOn:str = obj["CreatedOn"]
      self.SystemFlag:str = obj["SystemFlag"]
      self.SysRevID:str = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class PublishBaseFile_input:
   """ Required : 
   request
   prevVersion
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_UxAppVersion_UxAppVersionRequest] = obj["request"]
      self.prevVersion:int = obj["prevVersion"]
      pass

class PublishBaseFile_output:
   def __init__(self, obj):
      pass

class PublishVersion_input:
   """ Required : 
   request
   """  
   def __init__(self, obj):
      self.request:list[Ice_Lib_UxAppVersion_UxAppVersionRequest] = obj["request"]
      pass

class PublishVersion_output:
   def __init__(self, obj):
      pass

