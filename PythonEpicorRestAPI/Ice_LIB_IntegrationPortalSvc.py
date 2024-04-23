import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.IntegrationPortalSvc
# Description: Integration Portal Service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetStatus(epicorHeaders = None):
   """  
   Summary: Invoke method GetStatus
   Description: Get Status of the Integration Portal Environment.
   OperationID: Get_GetStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GetContext(epicorHeaders = None):
   """  
   Summary: Invoke method GetContext
   Description: Get the Current User Context for the Portal.
   OperationID: Get_GetContext
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContext_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_Register(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Register
   Description: Register Kinetic with the Integration Portal.
   OperationID: Register
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Register_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Register_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Reconnect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Reconnect
   Description: Reconnnect Kinetic with the Integration Portal.
   OperationID: Reconnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Reconnect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Reconnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Unregister(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Unregister
   Description: Unregister Kinetic from Integration Portal.
   OperationID: Unregister
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Unregister_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Unregister_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Login(epicorHeaders = None):
   """  
   Summary: Invoke method Login
   Description: Login to the Portal, if registered.
   OperationID: Login
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Login_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ListAutomationStudioAPICollections(pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method ListAutomationStudioAPICollections
   Description: List Automation Studio API Collections.
   OperationID: Get_ListAutomationStudioAPICollections
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListAutomationStudioAPICollections_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_ListAutomationStudioAPIEndpoints(collectionPath, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method ListAutomationStudioAPIEndpoints
   Description: List Automation Studio API Endpoints.
   OperationID: Get_ListAutomationStudioAPIEndpoints
      :param collectionPath: Desc: API Collection Path   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListAutomationStudioAPIEndpoints_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "collectionPath=" + collectionPath
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_IsAutomationStudioAPIEndpointValid(collectionPath, endpointPath, method, epicorHeaders = None):
   """  
   Summary: Invoke method IsAutomationStudioAPIEndpointValid
   Description: Verifies that an Automation Studio API Endpoint is Valid.
   OperationID: Get_IsAutomationStudioAPIEndpointValid
      :param collectionPath: Desc: Collection Path   Required: True   Allow empty value : True
      :param endpointPath: Desc: Endpoint Path   Required: True   Allow empty value : True
      :param method: Desc: HTTP Method, i.e. GET   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAutomationStudioAPIEndpointValid_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "collectionPath=" + collectionPath
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "endpointPath=" + endpointPath
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "method=" + method

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetContext_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Context, serialized as JSON.  """  
      pass

class GetStatus_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Whether Kinetic is registered with the Integration Portal  """  
      pass

   def parameters(self, obj):
      self.registeredModules:list = obj[any]
      pass

      """  output parameters  """  

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class Ice_Tablesets_AutomationStudioAPICollectionRow:
   def __init__(self, obj):
      self.CollectionID:int = obj["CollectionID"]
      self.Name:str = obj["Name"]
      self.Version:str = obj["Version"]
      self.URL:str = obj["URL"]
      self.CollectionPath:str = obj["CollectionPath"]
      self.APISpecURL:str = obj["APISpecURL"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AutomationStudioAPICollectionTableset:
   def __init__(self, obj):
      self.AutomationStudioAPICollection:list[Ice_Tablesets_AutomationStudioAPICollectionRow] = obj["AutomationStudioAPICollection"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_AutomationStudioAPIEndpointRow:
   def __init__(self, obj):
      self.EndpointID:int = obj["EndpointID"]
      self.CollectionID:int = obj["CollectionID"]
      self.FlowID:int = obj["FlowID"]
      self.Name:str = obj["Name"]
      self.Method:str = obj["Method"]
      self.EndpointPath:str = obj["EndpointPath"]
      self.URL:str = obj["URL"]
      self.Active:bool = obj["Active"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AutomationStudioAPIEndpointTableset:
   def __init__(self, obj):
      self.AutomationStudioAPIEndpoint:list[Ice_Tablesets_AutomationStudioAPIEndpointRow] = obj["AutomationStudioAPIEndpoint"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class IsAutomationStudioAPIEndpointValid_input:
   """ Required : 
   collectionPath
   endpointPath
   method
   """  
   def __init__(self, obj):
      self.collectionPath:str = obj["collectionPath"]
      """  Collection Path  """  
      self.endpointPath:str = obj["endpointPath"]
      """  Endpoint Path  """  
      self.method:str = obj["method"]
      """  HTTP Method, i.e. GET  """  
      pass

class IsAutomationStudioAPIEndpointValid_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.collectionValid:bool = obj["collectionValid"]
      self.endpointValid:bool = obj["endpointValid"]
      pass

      """  output parameters  """  

class ListAutomationStudioAPICollections_input:
   """ Required : 
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class ListAutomationStudioAPICollections_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AutomationStudioAPICollectionTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class ListAutomationStudioAPIEndpoints_input:
   """ Required : 
   collectionPath
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.collectionPath:str = obj["collectionPath"]
      """  API Collection Path  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class ListAutomationStudioAPIEndpoints_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AutomationStudioAPIEndpointTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Login_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.token:str = obj["parameters"]
      self.siteId:str = obj["parameters"]
      self.environmentId:str = obj["parameters"]
      pass

      """  output parameters  """  

class Reconnect_input:
   """ Required : 
   functionUrl
   kineticUrl
   instanceId
   token
   """  
   def __init__(self, obj):
      self.functionUrl:str = obj["functionUrl"]
      """  Portal Function URL  """  
      self.kineticUrl:str = obj["kineticUrl"]
      """  Kinetic App Server URL  """  
      self.instanceId:str = obj["instanceId"]
      """  Existing Instance ID  """  
      self.token:str = obj["token"]
      """  IdP Token supplied from Portal App  """  
      pass

class Reconnect_output:
   def __init__(self, obj):
      pass

class Register_input:
   """ Required : 
   functionUrl
   kineticUrl
   siteId
   environmentId
   name
   token
   """  
   def __init__(self, obj):
      self.functionUrl:str = obj["functionUrl"]
      """  Portal Function URL  """  
      self.kineticUrl:str = obj["kineticUrl"]
      """  Kinetic App Server URL  """  
      self.siteId:str = obj["siteId"]
      """  Site ID  """  
      self.environmentId:str = obj["environmentId"]
      """  Environment ID  """  
      self.name:str = obj["name"]
      """  Name of Instance  """  
      self.token:str = obj["token"]
      """  IdP Token supplied from Portal App  """  
      pass

class Register_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class Unregister_input:
   """ Required : 
   token
   """  
   def __init__(self, obj):
      self.token:str = obj["token"]
      """  IdP or Portal Token supplied from Portal App  """  
      pass

class Unregister_output:
   def __init__(self, obj):
      pass

