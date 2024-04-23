import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.BAQExtDBSearchSvc
# Description: The BAQ external database search service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDSNRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDSNList(epicorHeaders = None):
   """  
   Summary: Invoke method GetDSNList
   Description: Get full list of ODBC DSN
   OperationID: GetDSNList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDSNList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List",headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Get full list of ODBC DSN - equal to GetDSNList. Used for ComboBox listing
   OperationID: Get_GetList
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetSqlDatabasesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSqlDatabasesList
   Description: Get MS SQL server databases
   OperationID: GetSqlDatabasesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSqlDatabasesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSqlDatabasesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetProperties(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetProperties
   OperationID: GetProperties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetProperties_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProperties_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDbProviderList(epicorHeaders = None):
   """  
   Summary: Invoke method GetDbProviderList
   Description: Gets the database provider list.
   OperationID: GetDbProviderList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDbProviderList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_TestConnection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestConnection
   OperationID: TestConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestServiceConnectivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestServiceConnectivity
   OperationID: TestServiceConnectivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestServiceConnectivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestServiceConnectivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestDatasourceConnection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestDatasourceConnection
   Description: Test connection to the external data source by name
   OperationID: TestDatasourceConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestDatasourceConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestDatasourceConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTableListFromSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTableListFromSearch
   Description: Get full list of tables from Recordset.Open for palette and code editor
   OperationID: GetTableListFromSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableListFromSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableListFromSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTableList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTableList
   Description: Get full list of tables from Recordset.Open for palette and code editor
   OperationID: GetTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TableExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TableExists
   Description: Checks is the table exists in the database
   OperationID: TableExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TableExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TableExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TableSchemaList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TableSchemaList
   OperationID: TableSchemaList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TableSchemaList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TableSchemaList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFieldList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldList
   Description: Get full list of columns for the specified table
datatableID can contain tables divided by commas
   OperationID: GetFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetConnectionKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetConnectionKeys
   OperationID: GetConnectionKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConnectionKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConnectionKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFunctionList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFunctionList
   Description: MS SQL Functions
   OperationID: GetFunctionList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFunctionList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTableFunctionFieldList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTableFunctionFieldList
   Description: Get full list of columns for the specified table-value function
functionName can contain functions divided by commas
   OperationID: GetTableFunctionFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableFunctionFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableFunctionFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFunctionParameterList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFunctionParameterList
   Description: Get full list of paramters for the specified  function call
functionName can contain functions divided by commas
   OperationID: GetFunctionParameterList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFunctionParameterList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionParameterList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExecutionSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExecutionSettings
   Description: Execution settings required or supported by the external query system
   OperationID: GetExecutionSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExecutionSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExecutionSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDSNRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQExtDSNRow] = obj["value"]
      pass

class Ice_Tablesets_BAQExtDSNRow:
   def __init__(self, obj):
      self.DSN:str = obj["DSN"]
      self.Description:str = obj["Description"]
      self.DSNType:str = obj["DSNType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class GetConnectedTables_input:
   """ Required : 
   datasourceName
   tableSchema
   dataTableID
   """  
   def __init__(self, obj):
      self.datasourceName:str = obj["datasourceName"]
      self.tableSchema:str = obj["tableSchema"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class GetConnectedTables_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtConnectedTablesTableset] = obj["returnObj"]
      pass

class GetConnectionKeys_input:
   """ Required : 
   datasourceName
   connectionSchema
   connectionID
   connectionType
   """  
   def __init__(self, obj):
      self.datasourceName:str = obj["datasourceName"]
      self.connectionSchema:str = obj["connectionSchema"]
      self.connectionID:str = obj["connectionID"]
      self.connectionType:str = obj["connectionType"]
      pass

class GetConnectionKeys_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtConnectionKeysTableset] = obj["returnObj"]
      pass

class GetDSNList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDSNTableset] = obj["returnObj"]
      pass

class GetDbProviderList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDSNTableset] = obj["returnObj"]
      pass

class GetExecutionSettings_input:
   """ Required : 
   datasourceName
   """  
   def __init__(self, obj):
      self.datasourceName:str = obj["datasourceName"]
      pass

class GetExecutionSettings_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtExecSettingListTableset] = obj["returnObj"]
      pass

class GetFieldList_input:
   """ Required : 
   DatasourceName
   catalog
   tableSchema
   dataTableID
   """  
   def __init__(self, obj):
      self.DatasourceName:str = obj["DatasourceName"]
      self.catalog:str = obj["catalog"]
      self.tableSchema:str = obj["tableSchema"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class GetFieldList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDataFieldTableset] = obj["returnObj"]
      pass

class GetFunctionList_input:
   """ Required : 
   datasourceName
   functionType
   """  
   def __init__(self, obj):
      self.datasourceName:str = obj["datasourceName"]
      self.functionType:int = obj["functionType"]
      pass

class GetFunctionList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDataTableTableset] = obj["returnObj"]
      pass

class GetFunctionParameterList_input:
   """ Required : 
   DatasourceName
   catalog
   tableSchema
   functionName
   """  
   def __init__(self, obj):
      self.DatasourceName:str = obj["DatasourceName"]
      self.catalog:str = obj["catalog"]
      self.tableSchema:str = obj["tableSchema"]
      self.functionName:str = obj["functionName"]
      pass

class GetFunctionParameterList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDataFieldTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQExtDSNTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetProperties_input:
   """ Required : 
   dbProviderType
   propertyGroup
   """  
   def __init__(self, obj):
      self.dbProviderType:str = obj["dbProviderType"]
      self.propertyGroup:str = obj["propertyGroup"]
      pass

class GetProperties_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtPropertiesTableset] = obj["returnObj"]
      pass

class GetRows_input:
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

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDataTableTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSqlDatabasesList_input:
   """ Required : 
   dbProviderType
   connStr
   """  
   def __init__(self, obj):
      self.dbProviderType:str = obj["dbProviderType"]
      self.connStr:str = obj["connStr"]
      pass

class GetSqlDatabasesList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtPropertiesTableset] = obj["returnObj"]
      pass

class GetTableFunctionFieldList_input:
   """ Required : 
   DatasourceName
   catalog
   tableSchema
   functionName
   """  
   def __init__(self, obj):
      self.DatasourceName:str = obj["DatasourceName"]
      self.catalog:str = obj["catalog"]
      self.tableSchema:str = obj["tableSchema"]
      self.functionName:str = obj["functionName"]
      pass

class GetTableFunctionFieldList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDataFieldTableset] = obj["returnObj"]
      pass

class GetTableListFromSearch_input:
   """ Required : 
   datasourceName
   schemaName
   startTableName
   """  
   def __init__(self, obj):
      self.datasourceName:str = obj["datasourceName"]
      self.schemaName:str = obj["schemaName"]
      self.startTableName:str = obj["startTableName"]
      pass

class GetTableListFromSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDataTableTableset] = obj["returnObj"]
      pass

class GetTableList_input:
   """ Required : 
   DatasourceName
   """  
   def __init__(self, obj):
      self.DatasourceName:str = obj["DatasourceName"]
      pass

class GetTableList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDataTableTableset] = obj["returnObj"]
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

class Ice_Tablesets_BAQExtConnectedTablesRow:
   def __init__(self, obj):
      self.ConnectedTableID:str = obj["ConnectedTableID"]
      self.ConnectedTableSchema:str = obj["ConnectedTableSchema"]
      self.ConnectionID:str = obj["ConnectionID"]
      self.ConnectionType:str = obj["ConnectionType"]
      self.DataTableID:str = obj["DataTableID"]
      self.TableSchema:str = obj["TableSchema"]
      self.SortPriority:int = obj["SortPriority"]
      self.ConnectionSchema:str = obj["ConnectionSchema"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtConnectedTablesTableset:
   def __init__(self, obj):
      self.BAQExtConnectedTables:list[Ice_Tablesets_BAQExtConnectedTablesRow] = obj["BAQExtConnectedTables"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtConnectionKeysRow:
   def __init__(self, obj):
      self.FromColumn:str = obj["FromColumn"]
      self.ToColumn:str = obj["ToColumn"]
      self.Ordinal:int = obj["Ordinal"]
      self.FromIsExpr:bool = obj["FromIsExpr"]
      self.ToIsExpr:bool = obj["ToIsExpr"]
      self.CompOp:str = obj["CompOp"]
      self.AndOr:str = obj["AndOr"]
      self.Not:bool = obj["Not"]
      self.LeftP:str = obj["LeftP"]
      self.RightP:str = obj["RightP"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtConnectionKeysTableset:
   def __init__(self, obj):
      self.BAQExtConnectionKeys:list[Ice_Tablesets_BAQExtConnectionKeysRow] = obj["BAQExtConnectionKeys"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtDSNRow:
   def __init__(self, obj):
      self.DSN:str = obj["DSN"]
      self.Description:str = obj["Description"]
      self.DSNType:str = obj["DSNType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDSNTableset:
   def __init__(self, obj):
      self.BAQExtDSN:list[Ice_Tablesets_BAQExtDSNRow] = obj["BAQExtDSN"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtDataFieldRow:
   def __init__(self, obj):
      self.TableID:str = obj["TableID"]
      self.FieldName:str = obj["FieldName"]
      self.Seq:int = obj["Seq"]
      self.Description:str = obj["Description"]
      self.DataType:str = obj["DataType"]
      self.SQLDataType:str = obj["SQLDataType"]
      self.CharMaxLen:int = obj["CharMaxLen"]
      self.NumericPrecision:int = obj["NumericPrecision"]
      self.NumericScale:int = obj["NumericScale"]
      self.Mandatory:bool = obj["Mandatory"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.IsPrimaryKey:bool = obj["IsPrimaryKey"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.SchemaName:str = obj["SchemaName"]
      self.TableName:str = obj["TableName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDataFieldTableset:
   def __init__(self, obj):
      self.BAQExtDataField:list[Ice_Tablesets_BAQExtDataFieldRow] = obj["BAQExtDataField"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtDataTableRow:
   def __init__(self, obj):
      self.TableID:str = obj["TableID"]
      self.Description:str = obj["Description"]
      self.TableType:str = obj["TableType"]
      self.DBSchemaName:str = obj["DBSchemaName"]
      self.FullTableName:str = obj["FullTableName"]
      self.Catalog:str = obj["Catalog"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtDataTableTableset:
   def __init__(self, obj):
      self.BAQExtDataTable:list[Ice_Tablesets_BAQExtDataTableRow] = obj["BAQExtDataTable"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtExecSettingListRow:
   def __init__(self, obj):
      self.SettingID:str = obj["SettingID"]
      self.SettingType:str = obj["SettingType"]
      self.DefaultValue:str = obj["DefaultValue"]
      self.Required:bool = obj["Required"]
      self.IsEnum:bool = obj["IsEnum"]
      self.Description:str = obj["Description"]
      self.Category:str = obj["Category"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtExecSettingListTableset:
   def __init__(self, obj):
      self.BAQExtExecSettingList:list[Ice_Tablesets_BAQExtExecSettingListRow] = obj["BAQExtExecSettingList"]
      self.BAQExtExecSettingValues:list[Ice_Tablesets_BAQExtExecSettingValuesRow] = obj["BAQExtExecSettingValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtExecSettingValuesRow:
   def __init__(self, obj):
      self.SettingID:str = obj["SettingID"]
      self.SettingValueOrder:int = obj["SettingValueOrder"]
      self.SettingEnumValue:str = obj["SettingEnumValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQExtPropertiesTableset:
   def __init__(self, obj):
      self.BAQExtProviderProperties:list[Ice_Tablesets_BAQExtProviderPropertiesRow] = obj["BAQExtProviderProperties"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQExtProviderPropertiesRow:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      self.Value:str = obj["Value"]
      self.Description:str = obj["Description"]
      self.Type:str = obj["Type"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class TableExists_input:
   """ Required : 
   DatasourceName
   tableSchema
   dataTableID
   """  
   def __init__(self, obj):
      self.DatasourceName:str = obj["DatasourceName"]
      self.tableSchema:str = obj["tableSchema"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class TableExists_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQExtDataTableTableset] = obj["returnObj"]
      pass

class TableSchemaList_input:
   """ Required : 
   DatasourceName
   """  
   def __init__(self, obj):
      self.DatasourceName:str = obj["DatasourceName"]
      pass

class TableSchemaList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class TestConnection_input:
   """ Required : 
   connStr
   odbcDBType
   """  
   def __init__(self, obj):
      self.connStr:str = obj["connStr"]
      self.odbcDBType:str = obj["odbcDBType"]
      pass

class TestConnection_output:
   def __init__(self, obj):
      pass

class TestDatasourceConnection_input:
   """ Required : 
   DatasourceName
   """  
   def __init__(self, obj):
      self.DatasourceName:str = obj["DatasourceName"]
      """  Name of the data source  """  
      pass

class TestDatasourceConnection_output:
   def __init__(self, obj):
      pass

class TestServiceConnectivity_input:
   """ Required : 
   url
   clientID
   pwd
   stringAppType
   """  
   def __init__(self, obj):
      self.url:str = obj["url"]
      self.clientID:str = obj["clientID"]
      self.pwd:str = obj["pwd"]
      self.stringAppType:str = obj["stringAppType"]
      pass

class TestServiceConnectivity_output:
   def __init__(self, obj):
      pass

