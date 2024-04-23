import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.BpTableDependSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpTableDependSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpTableDependSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetConnectionInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetConnectionInfo
   OperationID: GetConnectionInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConnectionInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConnectionInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpTableDependSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetConnectedTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetConnectedTables
   OperationID: GetConnectedTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConnectedTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConnectedTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpTableDependSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetConnectedTables_input:
   """ Required : 
   tableSchema
   tableID
   """  
   def __init__(self, obj):
      self.tableSchema:str = obj["tableSchema"]
      self.tableID:str = obj["tableID"]
      pass

class GetConnectedTables_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpTableDependSearchTableset] = obj["returnObj"]
      pass

class GetConnectionInfo_input:
   """ Required : 
   tableSchema
   tableID
   connectedTableSchema
   connectedTableID
   currentID
   """  
   def __init__(self, obj):
      self.tableSchema:str = obj["tableSchema"]
      self.tableID:str = obj["tableID"]
      self.connectedTableSchema:str = obj["connectedTableSchema"]
      self.connectedTableID:str = obj["connectedTableID"]
      self.currentID:int = obj["currentID"]
      pass

class GetConnectionInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpTableDependSearchTableset] = obj["returnObj"]
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

class Ice_Tablesets_BpTableConnectKeysRow:
   def __init__(self, obj):
      self.Seq:int = obj["Seq"]
      """  Sequence number of the connection  """  
      self.FieldName:str = obj["FieldName"]
      self.ForeignFieldName:str = obj["ForeignFieldName"]
      self.ID:int = obj["ID"]
      """  Simple autoincrement ID  """  
      self.FieldIsExpr:bool = obj["FieldIsExpr"]
      self.ForeignFieldIsExpr:bool = obj["ForeignFieldIsExpr"]
      self.CompOp:str = obj["CompOp"]
      self.AndOr:str = obj["AndOr"]
      self.Not:bool = obj["Not"]
      self.LeftP:str = obj["LeftP"]
      self.RightP:str = obj["RightP"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpTableConnectionRow:
   def __init__(self, obj):
      self.ConnectedTableID:str = obj["ConnectedTableID"]
      """  DataTableID of the connected table  """  
      self.ConnectionType:int = obj["ConnectionType"]
      """  Type of the table connection: 0 - child table from zRelation, 1 - parent table from zRelation, 2 - child table from zLookupLink, 3 -parent table from zLookupLink  """  
      self.ConnectionID:str = obj["ConnectionID"]
      """  RelationID or LookupID for connected table  """  
      self.KeyID:str = obj["KeyID"]
      """  KeyID of the connection  """  
      self.DataTableID:str = obj["DataTableID"]
      """  Data table  """  
      self.ID:int = obj["ID"]
      """  autoincrement sequence number  """  
      self.SameFieldNames:bool = obj["SameFieldNames"]
      self.TableSchema:str = obj["TableSchema"]
      self.ConnectedTableSchema:str = obj["ConnectedTableSchema"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpTableDependSearchRow:
   def __init__(self, obj):
      self.ConnectedTableID:str = obj["ConnectedTableID"]
      self.DataTableID:str = obj["DataTableID"]
      self.isChildRel:bool = obj["isChildRel"]
      """  indicates if connected table is child table  """  
      self.TableSchema:str = obj["TableSchema"]
      self.ConnectedTableSchema:str = obj["ConnectedTableSchema"]
      self.ConnectedTableFullName:str = obj["ConnectedTableFullName"]
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpTableDependSearchTableset:
   def __init__(self, obj):
      self.BpTableDependSearch:list[Ice_Tablesets_BpTableDependSearchRow] = obj["BpTableDependSearch"]
      self.BpTableConnection:list[Ice_Tablesets_BpTableConnectionRow] = obj["BpTableConnection"]
      self.BpTableConnectKeys:list[Ice_Tablesets_BpTableConnectKeysRow] = obj["BpTableConnectKeys"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

