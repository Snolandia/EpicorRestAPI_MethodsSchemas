import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.DataFabricSvc
# Description: Data Fabric Service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ListLibraryFunctions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ListLibraryFunctions
   Description: Get a list of Epicor Functions including whether they are disabled,
invalid or not compatible with the Data Fabric.
   OperationID: ListLibraryFunctions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ListLibraryFunctions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListLibraryFunctions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ListEventTypes(epicorHeaders = None):
   """  
   Summary: Invoke method ListEventTypes
   Description: List all the event types that are supported by this system.
   OperationID: Get_ListEventTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListEventTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GetEventType(eventType, epicorHeaders = None):
   """  
   Summary: Invoke method GetEventType
   Description: Get a specific Event Type and related functions.
   OperationID: Get_GetEventType
      :param eventType: Desc: Event Type, required   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEventType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "eventType=" + eventType

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFunctions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFunctions
   Description: Checks whether a list of functions are valid to use with Data Fabric.
   OperationID: ValidateFunctions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFunctions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFunctions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateFunctions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateFunctions
   Description: Add or remove functions from an Event Type Consumer or Producer.
   OperationID: UpdateFunctions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateFunctions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateFunctions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Produce(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Produce
   Description: Produce an Integration Outbox Event.
<remarks>Access to this method is restricted and cannot be called directly, for example via the REST API.</remarks>
   OperationID: Produce
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Produce_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Produce_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetEventType_input:
   """ Required : 
   eventType
   """  
   def __init__(self, obj):
      self.eventType:str = obj["eventType"]
      """  Event Type, required  """  
      pass

class GetEventType_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DataFabricEventTypeTableset] = obj["returnObj"]
      pass

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

class Ice_Tablesets_DataFabricEfxFunctionRow:
   def __init__(self, obj):
      self.LibraryID:str = obj["LibraryID"]
      self.FunctionID:str = obj["FunctionID"]
      self.Disabled:bool = obj["Disabled"]
      self.Invalid:bool = obj["Invalid"]
      self.Compatible:bool = obj["Compatible"]
      self.Description:str = obj["Description"]
      self.Message:str = obj["Message"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DataFabricEfxFunctionTableset:
   def __init__(self, obj):
      self.DataFabricEfxFunction:list[Ice_Tablesets_DataFabricEfxFunctionRow] = obj["DataFabricEfxFunction"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_DataFabricEventTypeFunctionRow:
   def __init__(self, obj):
      self.EventType:str = obj["EventType"]
      self.HandlerType:str = obj["HandlerType"]
      self.LibraryID:str = obj["LibraryID"]
      self.FunctionID:str = obj["FunctionID"]
      self.Mode:str = obj["Mode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DataFabricEventTypeRow:
   def __init__(self, obj):
      self.EventType:str = obj["EventType"]
      self.Producer:bool = obj["Producer"]
      self.Consumer:bool = obj["Consumer"]
      self.ConsumerFunctionsEnabled:bool = obj["ConsumerFunctionsEnabled"]
      self.ProducerFunctionsEnabled:bool = obj["ProducerFunctionsEnabled"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DataFabricEventTypeTableset:
   def __init__(self, obj):
      self.DataFabricEventType:list[Ice_Tablesets_DataFabricEventTypeRow] = obj["DataFabricEventType"]
      self.DataFabricEventTypeFunction:list[Ice_Tablesets_DataFabricEventTypeFunctionRow] = obj["DataFabricEventTypeFunction"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ListEventTypes_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DataFabricEventTypeTableset] = obj["returnObj"]
      pass

class ListLibraryFunctions_input:
   """ Required : 
   libraryID
   startsWith
   sortBy
   """  
   def __init__(self, obj):
      self.libraryID:str = obj["libraryID"]
      """  Library ID  """  
      self.startsWith:str = obj["startsWith"]
      """  Description starts with  """  
      self.sortBy:str = obj["sortBy"]
      """  Sort by either description or function ID  """  
      pass

class ListLibraryFunctions_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DataFabricEfxFunctionTableset] = obj["returnObj"]
      pass

class Produce_input:
   """ Required : 
   eventType
   key
   data
   correlationId
   """  
   def __init__(self, obj):
      self.eventType:str = obj["eventType"]
      """  Event Type  """  
      self.key:str = obj["key"]
      """  Key  """  
      self.data:str = obj["data"]
      """  Data  """  
      self.correlationId:str = obj["correlationId"]
      """  Correlation ID  """  
      pass

class Produce_output:
   def __init__(self, obj):
      pass

class UpdateFunctions_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DataFabricEventTypeTableset] = obj["ds"]
      pass

class UpdateFunctions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DataFabricEventTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateFunctions_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DataFabricEfxFunctionTableset] = obj["ds"]
      pass

class ValidateFunctions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DataFabricEfxFunctionTableset] = obj["ds"]
      self.valid:bool = obj["valid"]
      pass

      """  output parameters  """  

