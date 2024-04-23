import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.EcfToolsSvc
# Description: ATTENTION: This service is for internal use only.
It can be changed or even removed without any public announces.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetAssemblyBytes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAssemblyBytes
   OperationID: GetAssemblyBytes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAssemblyBytes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAssemblyBytes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableServiceKinds(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableServiceKinds
   Description: Method returns Service Kinds (BO, Lib, etc.) available per System Code
   OperationID: GetAvailableServiceKinds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableServiceKinds_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableServices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableServices
   Description: Method returns an array of ServiceInfo items of specified kind available for the specified system code.
   OperationID: GetAvailableServices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableServices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableServices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetServiceApi(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetServiceApi
   Description: Method returns service API description (e.g. methods with their signatures)
   OperationID: GetServiceApi
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetServiceApi_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetServiceApi_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTablesetInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTablesetInfo
   Description: Method returns tableset description for the provided type reference.
If type reference describes not a tableset, then method throws an exception.
If tableset is unknown, then method returns null
If ignoreExtensions == false, then method loads information about extension tables
available for the current company (if any).
   OperationID: GetTablesetInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTablesetInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTablesetInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTablesetInfoInCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTablesetInfoInCompany
   Description: Method returns tableset description for the provided type reference.
If type reference describes not a tableset, then method throws an exception.
If tableset is unknown, then method returns null
If inCompany parameter is specified, then method tries to provide information
about extension tables available in the company.
   OperationID: GetTablesetInfoInCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTablesetInfoInCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTablesetInfoInCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDBModel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDBModel
   Description: Method returns definition of the product DB model.
   OperationID: GetDBModel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDBModel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDBModel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDBEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDBEntity
   Description: Method returns entity definition of the product DB model.
   OperationID: GetDBEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDBEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDBEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CanCallWorkato(epicorHeaders = None):
   """  
   Summary: Invoke method CanCallWorkato
   OperationID: CanCallWorkato
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanCallWorkato_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetWorkatoApiCollections(epicorHeaders = None):
   """  
   Summary: Invoke method GetWorkatoApiCollections
   OperationID: GetWorkatoApiCollections
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWorkatoApiCollections_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetWorkatoEndpoints(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWorkatoEndpoints
   OperationID: GetWorkatoEndpoints
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWorkatoEndpoints_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWorkatoEndpoints_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWorkatoEndpointSignature(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWorkatoEndpointSignature
   OperationID: GetWorkatoEndpointSignature
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWorkatoEndpointSignature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWorkatoEndpointSignature_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CanCallWorkato_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class Epicor_Customization_Metadata_DBEntityId:
   def __init__(self, obj):
      self.product:str = obj["product"]
      self.entityName:str = obj["entityName"]
      pass

class Epicor_Customization_Metadata_DBEntityInfo:
   def __init__(self, obj):
      self.id:list[Epicor_Customization_Metadata_DBEntityId] = obj["id"]
      self.typeName:str = obj["typeName"]
      self.rowTypeName:str = obj["rowTypeName"]
      self.columns:list[Epicor_Customization_Metadata_IceColumnInfo] = obj["columns"]
      self.keyColumns:int = obj["keyColumns"]
      pass

class Epicor_Customization_Metadata_DBModelInfo:
   def __init__(self, obj):
      self.product:str = obj["product"]
      self.assembly:str = obj["assembly"]
      self.entities:list[Epicor_Customization_Metadata_DBEntityId] = obj["entities"]
      pass

class Epicor_Customization_Metadata_EpicorServiceApi:
   def __init__(self, obj):
      self.serviceId:list[Epicor_Typed_ServiceId] = obj["serviceId"]
      self.methods:list[Epicor_Customization_Metadata_ServiceMethodSignature] = obj["methods"]
      self.options:int = obj["options"]
      pass

class Epicor_Customization_Metadata_IceColumnInfo:
   def __init__(self, obj):
      self.name:str = obj["name"]
      self.typeName:str = obj["typeName"]
      self.kind:int = obj["kind"]
      pass

class Epicor_Customization_Metadata_IceTableInfo:
   def __init__(self, obj):
      self.name:str = obj["name"]
      self.extension:bool = obj["extension"]
      self.tableTypeName:str = obj["tableTypeName"]
      self.rowTypeName:str = obj["rowTypeName"]
      self.columns:list[Epicor_Customization_Metadata_IceColumnInfo] = obj["columns"]
      self.keyColumns:int = obj["keyColumns"]
      pass

class Epicor_Customization_Metadata_IceTablesetInfo:
   def __init__(self, obj):
      self.id:str = obj["id"]
      self.type:list[Epicor_Customization_Metadata_TypeRef] = obj["type"]
      self.tables:list[Epicor_Customization_Metadata_IceTableInfo] = obj["tables"]
      self.extensionTables:list[Epicor_Customization_Metadata_IceTableInfo] = obj["extensionTables"]
      self.relations:list[Epicor_Customization_Metadata_TableRelation] = obj["relations"]
      self.primaryTableIdx:int = obj["primaryTableIdx"]
      pass

class Epicor_Customization_Metadata_MethodArg:
   def __init__(self, obj):
      self.name:str = obj["name"]
      self.type:list[Epicor_Customization_Metadata_TypeRef] = obj["type"]
      self.modifier:int = obj["modifier"]
      pass

class Epicor_Customization_Metadata_RelationColumns:
   def __init__(self, obj):
      self.parentColumn:str = obj["parentColumn"]
      self.childColumn:str = obj["childColumn"]
      pass

class Epicor_Customization_Metadata_RestParameter:
   def __init__(self, obj):
      self.name:str = obj["name"]
      self.type:list[Epicor_Customization_Metadata_TypeRef] = obj["type"]
      self.location:str = obj["location"]
      pass

class Epicor_Customization_Metadata_RestSignature:
   def __init__(self, obj):
      self.input:list[Epicor_Customization_Metadata_RestParameter] = obj["input"]
      self.output:list[Epicor_Customization_Metadata_RestParameter] = obj["output"]
      pass

class Epicor_Customization_Metadata_ServiceMethodSignature:
   def __init__(self, obj):
      self.name:str = obj["name"]
      self.arguments:list[Epicor_Customization_Metadata_MethodArg] = obj["arguments"]
      self.resultType:list[Epicor_Customization_Metadata_TypeRef] = obj["resultType"]
      self.options:int = obj["options"]
      pass

class Epicor_Customization_Metadata_TableRelation:
   def __init__(self, obj):
      self.parentTable:str = obj["parentTable"]
      self.childTable:str = obj["childTable"]
      self.columns:list[Epicor_Customization_Metadata_RelationColumns] = obj["columns"]
      pass

class Epicor_Customization_Metadata_TypeRef:
   def __init__(self, obj):
      self.wellknownType:int = obj["wellknownType"]
      self.namespace:str = obj["namespace"]
      self.name:str = obj["name"]
      self.assembly:str = obj["assembly"]
      self.options:int = obj["options"]
      self.elementType:list[Epicor_Customization_Metadata_TypeRef] = obj["elementType"]
      self.genericArguments:list[Epicor_Customization_Metadata_TypeRef] = obj["genericArguments"]
      pass

class Epicor_Typed_ProductCode:
   def __init__(self, obj):
      self.value:str = obj["value"]
      pass

class Epicor_Typed_ServiceId:
   def __init__(self, obj):
      self.product:list[Epicor_Typed_ProductCode] = obj["product"]
      self.kind:list[Epicor_Typed_ServiceKind] = obj["kind"]
      self.name:str = obj["name"]
      pass

class Epicor_Typed_ServiceKind:
   def __init__(self, obj):
      self.value:str = obj["value"]
      pass

class GetAssemblyBytes_input:
   """ Required : 
   assemblyId
   """  
   def __init__(self, obj):
      self.assemblyId:str = obj["assemblyId"]
      pass

class GetAssemblyBytes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetAvailableServiceKinds_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_EcfTools_ProductServiceKinds] = obj["returnObj"]
      pass

class GetAvailableServices_input:
   """ Required : 
   systemCode
   serviceKind
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.serviceKind:str = obj["serviceKind"]
      pass

class GetAvailableServices_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_EcfTools_ServiceInfo] = obj["returnObj"]
      pass

class GetDBEntity_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:list[Epicor_Customization_Metadata_DBEntityId] = obj["id"]
      pass

class GetDBEntity_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_Customization_Metadata_DBEntityInfo] = obj["returnObj"]
      pass

class GetDBModel_input:
   """ Required : 
   systemCode
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      pass

class GetDBModel_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_Customization_Metadata_DBModelInfo] = obj["returnObj"]
      pass

class GetServiceApi_input:
   """ Required : 
   serviceId
   """  
   def __init__(self, obj):
      self.serviceId:list[Epicor_Typed_ServiceId] = obj["serviceId"]
      pass

class GetServiceApi_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_Customization_Metadata_EpicorServiceApi] = obj["returnObj"]
      pass

class GetTablesetInfoInCompany_input:
   """ Required : 
   typeRef
   inCompany
   """  
   def __init__(self, obj):
      self.typeRef:list[Epicor_Customization_Metadata_TypeRef] = obj["typeRef"]
      self.inCompany:str = obj["inCompany"]
      pass

class GetTablesetInfoInCompany_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_Customization_Metadata_IceTablesetInfo] = obj["returnObj"]
      pass

class GetTablesetInfo_input:
   """ Required : 
   typeRef
   ignoreExtensions
   """  
   def __init__(self, obj):
      self.typeRef:list[Epicor_Customization_Metadata_TypeRef] = obj["typeRef"]
      self.ignoreExtensions:bool = obj["ignoreExtensions"]
      pass

class GetTablesetInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_Customization_Metadata_IceTablesetInfo] = obj["returnObj"]
      pass

class GetWorkatoApiCollections_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_EcfTools_WorkatoApiCollectionInfo] = obj["returnObj"]
      pass

class GetWorkatoEndpointSignature_input:
   """ Required : 
   endpointId
   """  
   def __init__(self, obj):
      self.endpointId:list[Ice_Lib_EcfTools_WorkatoEndpointId] = obj["endpointId"]
      pass

class GetWorkatoEndpointSignature_output:
   def __init__(self, obj):
      self.returnObj:list[Epicor_Customization_Metadata_RestSignature] = obj["returnObj"]
      pass

class GetWorkatoEndpoints_input:
   """ Required : 
   collectionPath
   """  
   def __init__(self, obj):
      self.collectionPath:str = obj["collectionPath"]
      pass

class GetWorkatoEndpoints_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_EcfTools_WorkatoEndpointInfo] = obj["returnObj"]
      pass

class Ice_Lib_EcfTools_ProductServiceKinds:
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.serviceKinds:str = obj["serviceKinds"]
      pass

class Ice_Lib_EcfTools_ServiceInfo:
   def __init__(self, obj):
      self.className:str = obj["className"]
      self.serviceUsage:int = obj["serviceUsage"]
      pass

class Ice_Lib_EcfTools_WorkatoApiCollectionInfo:
   def __init__(self, obj):
      self.path:str = obj["path"]
      self.name:str = obj["name"]
      self.version:str = obj["version"]
      pass

class Ice_Lib_EcfTools_WorkatoEndpointId:
   def __init__(self, obj):
      self.collectionPath:str = obj["collectionPath"]
      self.endpointPath:str = obj["endpointPath"]
      self.httpMethod:str = obj["httpMethod"]
      pass

class Ice_Lib_EcfTools_WorkatoEndpointInfo:
   def __init__(self, obj):
      self.path:str = obj["path"]
      self.httpMethod:str = obj["httpMethod"]
      self.name:str = obj["name"]
      self.active:bool = obj["active"]
      pass

