import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FSASyncWbSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSASyncWbSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSASyncWbSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   OperationID: GetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSASyncWbSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetColumnList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetColumnList
   OperationID: GetColumnList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetColumnList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetColumnList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSASyncWbSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshCurrentRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshCurrentRows
   OperationID: RefreshCurrentRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshCurrentRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshCurrentRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSASyncWbSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSASyncWbSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSyncToFSA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSyncToFSA
   OperationID: ChangeSyncToFSA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSyncToFSA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSyncToFSA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSASyncWbSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ToggleColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ToggleColumn
   OperationID: ToggleColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ToggleColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ToggleColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSASyncWbSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSendToFSAChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSendToFSAChange
   Description: Returns If SendToFSA has change from false to true.
   OperationID: GetSendToFSAChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSendToFSAChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSendToFSAChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSASyncWbSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetToggleColumnsByTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetToggleColumnsByTable
   OperationID: GetToggleColumnsByTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetToggleColumnsByTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetToggleColumnsByTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSASyncWbSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeSyncToFSA_input:
   """ Required : 
   syncAll
   ds
   """  
   def __init__(self, obj):
      self.syncAll:bool = obj["syncAll"]
      self.ds:list[Erp_Tablesets_FSASyncWbTableset] = obj["ds"]
      pass

class ChangeSyncToFSA_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSASyncWbTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_FSAColumnRow:
   def __init__(self, obj):
      self.ColumnID:str = obj["ColumnID"]
      """  ColumnID  """  
      self.ID:str = obj["ID"]
      """  ID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ColumnName:str = obj["ColumnName"]
      """  ColumnName  """  
      self.ColumnValue:str = obj["ColumnValue"]
      """  ColumnValue  """  
      self.ColumnType:str = obj["ColumnType"]
      """  ColumnType  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSASyncWbTableset:
   def __init__(self, obj):
      self.FSATable:list[Erp_Tablesets_FSATableRow] = obj["FSATable"]
      self.FSAColumn:list[Erp_Tablesets_FSAColumnRow] = obj["FSAColumn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FSATableRow:
   def __init__(self, obj):
      self.ID:str = obj["ID"]
      """  ID  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      """  Character02  """  
      self.Character03:str = obj["Character03"]
      """  Character03  """  
      self.Character04:str = obj["Character04"]
      """  Character04  """  
      self.Checkbox01:bool = obj["Checkbox01"]
      """  Checkbox01  """  
      self.Checkbox02:bool = obj["Checkbox02"]
      """  Checkbox02  """  
      self.Checkbox03:bool = obj["Checkbox03"]
      """  Checkbox03  """  
      self.Number01:int = obj["Number01"]
      """  Number01  """  
      self.Number02:int = obj["Number02"]
      """  Number02  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  ShortChar01  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  ShortChar02  """  
      self.Character05:str = obj["Character05"]
      """  Character05  """  
      self.Checkbox04:bool = obj["Checkbox04"]
      """  Checkbox04  """  
      self.Decimal01:int = obj["Decimal01"]
      """  Decimal01  """  
      self.Decimal02:str = obj["Decimal02"]
      """  Decimal02  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetColumnList_input:
   """ Required : 
   tableName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      pass

class GetColumnList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   tableName
   whereClauseFSATable
   startingAt
   searchBy
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.whereClauseFSATable:str = obj["whereClauseFSATable"]
      self.startingAt:str = obj["startingAt"]
      self.searchBy:str = obj["searchBy"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSASyncWbTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSendToFSAChange_input:
   """ Required : 
   sendToFSA
   partNum
   ds
   """  
   def __init__(self, obj):
      self.sendToFSA:bool = obj["sendToFSA"]
      self.partNum:str = obj["partNum"]
      self.ds:list[Erp_Tablesets_FSASyncWbTableset] = obj["ds"]
      pass

class GetSendToFSAChange_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetToggleColumnsByTable_input:
   """ Required : 
   tableName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      pass

class GetToggleColumnsByTable_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

class RefreshCurrentRows_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FSASyncWbTableset] = obj["ds"]
      pass

class RefreshCurrentRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSASyncWbTableset] = obj["returnObj"]
      pass

class ToggleColumn_input:
   """ Required : 
   tableName
   columnName
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.columnName:str = obj["columnName"]
      self.ds:list[Erp_Tablesets_FSASyncWbTableset] = obj["ds"]
      pass

class ToggleColumn_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSASyncWbTableset] = obj["returnObj"]
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FSASyncWbTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSASyncWbTableset] = obj["returnObj"]
      pass

