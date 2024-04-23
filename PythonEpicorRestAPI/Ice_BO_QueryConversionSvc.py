import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.QueryConversionSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QueryConversionSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QueryConversionSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_QueryConversions_Company_QueryID(Company, QueryID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryConversion item
   Description: Calls GetByID to retrieve the QueryConversion item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryConversion
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryConversionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QueryConversionSvc/QueryConversions(" + Company + "," + QueryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryConversions_Company_QueryID_QueryFieldConversions_Company_QueryID_TableID_FieldName_Location(Company, QueryID, TableID, FieldName, Location, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFieldConversion item
   Description: Calls GetByID to retrieve the QueryFieldConversion item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldConversion1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param Location: Desc: Location   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldConversionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QueryConversionSvc/QueryConversions(" + Company + "," + QueryID + ")/QueryFieldConversions(" + Company + "," + QueryID + "," + TableID + "," + FieldName + "," + Location + ")",headers=creds) as resp:
           return await resp.json()

async def get_QueryFieldConversions_Company_QueryID_TableID_FieldName_Location(Company, QueryID, TableID, FieldName, Location, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QueryFieldConversion item
   Description: Calls GetByID to retrieve the QueryFieldConversion item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldConversion
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QueryID: Desc: QueryID   Required: True   Allow empty value : True
      :param TableID: Desc: TableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param Location: Desc: Location   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QueryFieldConversionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QueryConversionSvc/QueryFieldConversions(" + Company + "," + QueryID + "," + TableID + "," + FieldName + "," + Location + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQExtDatasourceLists_Company_DatasourceName(Company, DatasourceName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQExtDatasourceList item
   Description: Calls GetByID to retrieve the BAQExtDatasourceList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQExtDatasourceList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceName: Desc: DatasourceName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQExtDatasourceListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QueryConversionSvc/BAQExtDatasourceLists(" + Company + "," + DatasourceName + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryConversionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QueryConversionSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   OperationID: GetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QueryConversionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QueryConversionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFieldLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldLog
   OperationID: GetFieldLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QueryConversionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertExternalBAQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertExternalBAQ
   Description: goes through all tables where datatypes should be supplied and updates them.
   OperationID: ConvertExternalBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertExternalBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertExternalBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QueryConversionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryConversionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QueryConversionRow] = obj["value"]
      pass

class Ice_Tablesets_BAQExtDatasourceListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceName:str = obj["DatasourceName"]
      """  DatasourceName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.ProviderType:str = obj["ProviderType"]
      """  ProviderType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryConversionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.StatusCode:str = obj["StatusCode"]
      """  StatusCode  """  
      self.StatusText:str = obj["StatusText"]
      """  StatusText  """  
      self.Origin:str = obj["Origin"]
      """  Origin  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ModifiedOn:str = obj["ModifiedOn"]
      """  ModifiedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AuthorID:str = obj["AuthorID"]
      self.Description:str = obj["Description"]
      self.ExtQuery:bool = obj["ExtQuery"]
      self.ExtDatasourceName:str = obj["ExtDatasourceName"]
      self.Updatable:bool = obj["Updatable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryFieldConversionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  FieldFormat  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.Location:str = obj["Location"]
      """  Location  """  
      self.StatusCode:str = obj["StatusCode"]
      """  StatusCode  """  
      self.StatusText:str = obj["StatusText"]
      """  StatusText  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ModifiedOn:str = obj["ModifiedOn"]
      """  ModifiedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ConvertExternalBAQ_input:
   """ Required : 
   Company
   QueryId
   """  
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryId:str = obj["QueryId"]
      pass

class ConvertExternalBAQ_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   company
   queryId
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.queryId:str = obj["queryId"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QueryConversionTableset] = obj["returnObj"]
      pass

class GetFieldLog_input:
   """ Required : 
   company
   queryId
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.queryId:str = obj["queryId"]
      pass

class GetFieldLog_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QueryConversionTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QueryConversionTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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

class Ice_Tablesets_BAQExtDatasourceListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DatasourceName:str = obj["DatasourceName"]
      """  DatasourceName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.ProviderType:str = obj["ProviderType"]
      """  ProviderType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryConversionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.StatusCode:str = obj["StatusCode"]
      """  StatusCode  """  
      self.StatusText:str = obj["StatusText"]
      """  StatusText  """  
      self.Origin:str = obj["Origin"]
      """  Origin  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ModifiedOn:str = obj["ModifiedOn"]
      """  ModifiedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AuthorID:str = obj["AuthorID"]
      self.Description:str = obj["Description"]
      self.ExtQuery:bool = obj["ExtQuery"]
      self.ExtDatasourceName:str = obj["ExtDatasourceName"]
      self.Updatable:bool = obj["Updatable"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QueryConversionTableset:
   def __init__(self, obj):
      self.QueryConversion:list[Ice_Tablesets_QueryConversionRow] = obj["QueryConversion"]
      self.QueryFieldConversion:list[Ice_Tablesets_QueryFieldConversionRow] = obj["QueryFieldConversion"]
      self.BAQExtDatasourceList:list[Ice_Tablesets_BAQExtDatasourceListRow] = obj["BAQExtDatasourceList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_QueryFieldConversionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  FieldFormat  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.Location:str = obj["Location"]
      """  Location  """  
      self.StatusCode:str = obj["StatusCode"]
      """  StatusCode  """  
      self.StatusText:str = obj["StatusText"]
      """  StatusText  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ModifiedOn:str = obj["ModifiedOn"]
      """  ModifiedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

