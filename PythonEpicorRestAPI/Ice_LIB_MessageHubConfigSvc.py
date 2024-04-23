import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.MessageHubConfigSvc
# Description: Manage settings for Epicor.MessageHub push notifications.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MessageHubConfigSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.MessageHubConfigSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetSettings(epicorHeaders = None):
   """  
   Summary: Invoke method GetSettings
   Description: Get settings from database.
   OperationID: GetSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MessageHubConfigSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_UpdateSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSettings
   Description: Add or update settings in the database.
   OperationID: UpdateSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MessageHubConfigSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveSettings(epicorHeaders = None):
   """  
   Summary: Invoke method RemoveSettings
   Description: Remove settings from database.
   OperationID: RemoveSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.MessageHubConfigSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetSettings_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MessageHubConfigTableset] = obj["returnObj"]
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

class Ice_Tablesets_MessageHubConfigRow:
   def __init__(self, obj):
      self.AzureSignalRConnectionString:str = obj["AzureSignalRConnectionString"]
      """  Connection string to the Azure SignalR service,  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enables or disables message hub usage.  By default it is enabled.  """  
      self.ServerConnectionCount:int = obj["ServerConnectionCount"]
      """  How many connections are used by server itself to connect to the Azure SignalR. Default value is 5.  """  
      self.SignalRAccessTokenLifetime:int = obj["SignalRAccessTokenLifetime"]
      """  SignalR token lifetime in seconds.  """  
      self.EdgeAgentEnabled:bool = obj["EdgeAgentEnabled"]
      self.MaximumReceiveMessageSize:int = obj["MaximumReceiveMessageSize"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MessageHubConfigTableset:
   def __init__(self, obj):
      self.MessageHubConfig:list[Ice_Tablesets_MessageHubConfigRow] = obj["MessageHubConfig"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class RemoveSettings_output:
   def __init__(self, obj):
      pass

class UpdateSettings_input:
   """ Required : 
   settings
   """  
   def __init__(self, obj):
      self.settings:list[Ice_Tablesets_MessageHubConfigTableset] = obj["settings"]
      pass

class UpdateSettings_output:
   def __init__(self, obj):
      pass

