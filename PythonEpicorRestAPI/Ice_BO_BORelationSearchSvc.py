import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.BORelationSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetBODataset(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBODataset
   Description: Gets the BO dataset.
   OperationID: GetBODataset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBODataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBODataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBOTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBOTables
   Description: Gets the BO tables.
   OperationID: GetBOTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBOTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBOTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPrimaryTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPrimaryTable
   Description: Gets the primary table.
   OperationID: GetPrimaryTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrimaryTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimaryTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDatasetTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDatasetTables
   Description: Gets the tables from specified dataset.
   OperationID: GetDatasetTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBOPKFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBOPKFields
   Description: Returns list of the BO's primary table's PK fields delimited by semicolon
   OperationID: GetBOPKFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBOPKFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBOPKFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetBODataset_input:
   """ Required : 
   systemCode
   boName
   ds
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  The system code.  """  
      self.boName:str = obj["boName"]
      """  The BO name  """  
      self.ds:list[Ice_Tablesets_BORelationSearchTableset] = obj["ds"]
      pass

class GetBODataset_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BORelationSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetBOPKFields_input:
   """ Required : 
   SystemCode
   BOName
   """  
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.BOName:str = obj["BOName"]
      """  name of the BO  """  
      pass

class GetBOPKFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.DBTableName:str = obj["parameters"]
      self.PKFieldsStr:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetBOTables_input:
   """ Required : 
   systemCode
   boName
   ds
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  The system code.  """  
      self.boName:str = obj["boName"]
      """  The BO name  """  
      self.ds:list[Ice_Tablesets_BORelationSearchTableset] = obj["ds"]
      pass

class GetBOTables_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BORelationSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDatasetTables_input:
   """ Required : 
   systemCode
   boName
   datasetID
   ds
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.boName:str = obj["boName"]
      self.datasetID:str = obj["datasetID"]
      self.ds:list[Ice_Tablesets_BORelationSearchTableset] = obj["ds"]
      pass

class GetDatasetTables_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BORelationSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPrimaryTable_input:
   """ Required : 
   systemCode
   boName
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  The system code.  """  
      self.boName:str = obj["boName"]
      """  Name of the BO.  """  
      pass

class GetPrimaryTable_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Table's logical ID for BO's primary table  """  
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

class Ice_Tablesets_BOFieldLinksRow:
   def __init__(self, obj):
      self.LinkID:int = obj["LinkID"]
      self.Seq:int = obj["Seq"]
      self.TableField:str = obj["TableField"]
      self.ForeignTableField:str = obj["ForeignTableField"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BORelationSearchTableset:
   def __init__(self, obj):
      self.BOTableTree:list[Ice_Tablesets_BOTableTreeRow] = obj["BOTableTree"]
      self.BOTableParentLinks:list[Ice_Tablesets_BOTableParentLinksRow] = obj["BOTableParentLinks"]
      self.BOTableLinks:list[Ice_Tablesets_BOTableLinksRow] = obj["BOTableLinks"]
      self.BOFieldLinks:list[Ice_Tablesets_BOFieldLinksRow] = obj["BOFieldLinks"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BOTableLinksRow:
   def __init__(self, obj):
      self.LinkID:int = obj["LinkID"]
      self.SystemCode:str = obj["SystemCode"]
      self.BOName:str = obj["BOName"]
      self.DataTableID:str = obj["DataTableID"]
      self.ForeignTableID:str = obj["ForeignTableID"]
      self.ForeignSystemCode:str = obj["ForeignSystemCode"]
      self.ForeignBOName:str = obj["ForeignBOName"]
      self.LookupID:str = obj["LookupID"]
      self.IsChildObject:bool = obj["IsChildObject"]
      self.DBTableName:str = obj["DBTableName"]
      self.ForeignDBTableName:str = obj["ForeignDBTableName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BOTableParentLinksRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.BOName:str = obj["BOName"]
      self.Seq:int = obj["Seq"]
      self.ChildFieldName:str = obj["ChildFieldName"]
      self.ParentFieldName:str = obj["ParentFieldName"]
      self.DataTableID:str = obj["DataTableID"]
      self.IsLinkToConstant:bool = obj["IsLinkToConstant"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BOTableTreeRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.BOName:str = obj["BOName"]
      """  Business object name  """  
      self.DataTableID:str = obj["DataTableID"]
      self.DBTableName:str = obj["DBTableName"]
      self.ParentTableID:str = obj["ParentTableID"]
      self.ParentTableName:str = obj["ParentTableName"]
      self.IsPrimaryTable:bool = obj["IsPrimaryTable"]
      self.HasLinks:bool = obj["HasLinks"]
      self.Seq:int = obj["Seq"]
      self.ParentRelationID:str = obj["ParentRelationID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

