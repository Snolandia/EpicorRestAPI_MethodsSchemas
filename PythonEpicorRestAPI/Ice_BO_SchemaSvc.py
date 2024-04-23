import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.SchemaSvc
# Description: This is the Schema main business object.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.FileSchemaRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This method returns the Data Schema records
   OperationID: Get_GetRows
      :param whereClause: Desc: Data Table Where Clause   Required: True   Allow empty value : True
      :param pageSize: Desc: Page Size   Required: True
      :param absolutePage: Desc: Absolute Page   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetFieldByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldByID
   Description: This method returns a field dataset for the given table/field
   OperationID: GetFieldByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFieldList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldList
   Description: This method returns a list of fields for the given table
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateTableName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateTableName
   Description: This method returns true if the table name is exist
   OperationID: ValidateTableName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTableName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTableName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFieldName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFieldName
   Description: This method returns true if the table name is exist
   OperationID: ValidateFieldName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFieldName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFieldName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFileByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFileByID
   Description: This method returns a fileSchema dataset for the given table
   OperationID: GetFileByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFileByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFileByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFileList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFileList
   Description: This method returns a fileSchema dataset for the given criteria
   OperationID: GetFileList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFileList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFileList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIndexByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIndexByID
   Description: This method returns an index dataset for the given table/index
   OperationID: GetIndexByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIndexByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIndexByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIndexFieldByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIndexFieldByID
   Description: This method returns an index field dataset for the given table/index/sequence
   OperationID: GetIndexFieldByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIndexFieldByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIndexFieldByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIndexFieldList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIndexFieldList
   Description: This method returns a list of index fields for the given table/index
   OperationID: GetIndexFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIndexFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIndexFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIndexList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIndexList
   Description: This method returns a list of indexes in a table
   OperationID: GetIndexList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIndexList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIndexList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: This method returns the Data Schema records
   OperationID: Get_GetList
      :param whereClause: Desc: Data Table Where Clause   Required: True   Allow empty value : True
      :param pageSize: Desc: Page Size   Required: True
      :param absolutePage: Desc: Absolute Page   Required: True
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_TableSchemaList(epicorHeaders = None):
   """  
   Summary: Invoke method TableSchemaList
   Description: This method returns the Data Schema records
   OperationID: TableSchemaList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/TableSchemaList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetTableInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTableInfo
   OperationID: GetTableInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDictionaryTableByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDictionaryTableByID
   Description: This method returns a fileSchema dataset for the given table
   OperationID: GetDictionaryTableByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDictionaryTableByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDictionaryTableByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDictionaryTableByIDWithSortingFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDictionaryTableByIDWithSortingFields
   Description: This method returns a fileSchema dataset for the given table
   OperationID: GetDictionaryTableByIDWithSortingFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDictionaryTableByIDWithSortingFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDictionaryTableByIDWithSortingFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_FileSchemaRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_FileSchemaRow] = obj["value"]
      pass

class Ice_Tablesets_FileSchemaRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.PrimeIndex:int = obj["PrimeIndex"]
      self.NumFields:int = obj["NumFields"]
      self.Description:str = obj["Description"]
      self.ValidationExp:str = obj["ValidationExp"]
      self.ValidationMsg:str = obj["ValidationMsg"]
      self.Version:int = obj["Version"]
      self.TableType:str = obj["TableType"]
      self.SysRowID:str = obj["SysRowID"]
      self.SchemaName:str = obj["SchemaName"]
      """  Schema Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class GetDictionaryTableByIDWithSortingFields_input:
   """ Required : 
   schemaName
   pcFile
   sortingFields
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name of the table  """  
      self.pcFile:str = obj["pcFile"]
      """  name of the table  """  
      self.sortingFields:int = obj["sortingFields"]
      """  sorting of Fields  """  
      pass

class GetDictionaryTableByIDWithSortingFields_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DictionaryTableSchemaTableset] = obj["returnObj"]
      pass

class GetDictionaryTableByID_input:
   """ Required : 
   schemaName
   pcFile
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name of the table  """  
      self.pcFile:str = obj["pcFile"]
      """  name of the table  """  
      pass

class GetDictionaryTableByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DictionaryTableSchemaTableset] = obj["returnObj"]
      pass

class GetFieldByID_input:
   """ Required : 
   schemaName
   pcFile
   pcField
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  schema name of the field  """  
      self.pcFile:str = obj["pcFile"]
      """  name of the table  """  
      self.pcField:str = obj["pcField"]
      """  name of the field  """  
      pass

class GetFieldByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_FieldSchemaTableset] = obj["returnObj"]
      pass

class GetFieldList_input:
   """ Required : 
   schemaName
   pcFile
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  schema name of the table  """  
      self.pcFile:str = obj["pcFile"]
      """  name of the table  """  
      pass

class GetFieldList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_FieldSchemaTableset] = obj["returnObj"]
      pass

class GetFileByID_input:
   """ Required : 
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name of the table  """  
      self.tableName:str = obj["tableName"]
      """  name of the table  """  
      pass

class GetFileByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_FileSchemaTableset] = obj["returnObj"]
      pass

class GetFileList_input:
   """ Required : 
   pcWhere
   """  
   def __init__(self, obj):
      self.pcWhere:str = obj["pcWhere"]
      """  where clause  """  
      pass

class GetFileList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_FileSchemaTableset] = obj["returnObj"]
      pass

class GetIndexByID_input:
   """ Required : 
   schemaName
   pcFile
   pcIndex
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  name of the table  """  
      self.pcFile:str = obj["pcFile"]
      """  name of the table  """  
      self.pcIndex:str = obj["pcIndex"]
      """  name of the index  """  
      pass

class GetIndexByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IndexSchemaTableset] = obj["returnObj"]
      pass

class GetIndexFieldByID_input:
   """ Required : 
   schemaName
   pcFile
   pcIndex
   piSeq
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name of the table  """  
      self.pcFile:str = obj["pcFile"]
      """  name of the table  """  
      self.pcIndex:str = obj["pcIndex"]
      """  name of the index  """  
      self.piSeq:int = obj["piSeq"]
      """  the sequence number in the index  """  
      pass

class GetIndexFieldByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IndexFieldSchemaTableset] = obj["returnObj"]
      pass

class GetIndexFieldList_input:
   """ Required : 
   schemaName
   pcFile
   pcIndex
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name of the table  """  
      self.pcFile:str = obj["pcFile"]
      """  name of the table  """  
      self.pcIndex:str = obj["pcIndex"]
      """  name of the index  """  
      pass

class GetIndexFieldList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IndexFieldSchemaTableset] = obj["returnObj"]
      pass

class GetIndexList_input:
   """ Required : 
   schemaName
   pcFile
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name of the table  """  
      self.pcFile:str = obj["pcFile"]
      """  name of the table  """  
      pass

class GetIndexList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IndexSchemaTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Data Table Where Clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_FileSchemaTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Data Table Where Clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_FileSchemaTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTableInfo_input:
   """ Required : 
   schemaName
   pcFile
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      self.pcFile:str = obj["pcFile"]
      pass

class GetTableInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DictionaryTableSchemaTableset] = obj["returnObj"]
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

class Ice_Tablesets_DictionaryTableSchemaTableset:
   def __init__(self, obj):
      self.FileSchema:list[Ice_Tablesets_FileSchemaRow] = obj["FileSchema"]
      self.FieldSchema:list[Ice_Tablesets_FieldSchemaRow] = obj["FieldSchema"]
      self.IndexSchema:list[Ice_Tablesets_IndexSchemaRow] = obj["IndexSchema"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_FieldSchemaRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.FileRecid:int = obj["FileRecid"]
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.InitialValue:str = obj["InitialValue"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.Mandatory:bool = obj["Mandatory"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldDecimals:int = obj["FieldDecimals"]
      self.FieldSeq:int = obj["FieldSeq"]
      self.FieldExtent:int = obj["FieldExtent"]
      self.ValidationExp:str = obj["ValidationExp"]
      self.ValidationMsg:str = obj["ValidationMsg"]
      self.FieldHelp:str = obj["FieldHelp"]
      self.Description:str = obj["Description"]
      self.ColumnLabel:str = obj["ColumnLabel"]
      self.ViewAs:str = obj["ViewAs"]
      self.FieldWidth:int = obj["FieldWidth"]
      self.SysRowID:str = obj["SysRowID"]
      self.PrimaryKey:bool = obj["PrimaryKey"]
      self.Mapping:str = obj["Mapping"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_FieldSchemaTableset:
   def __init__(self, obj):
      self.FieldSchema:list[Ice_Tablesets_FieldSchemaRow] = obj["FieldSchema"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_FileSchemaRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.PrimeIndex:int = obj["PrimeIndex"]
      self.NumFields:int = obj["NumFields"]
      self.Description:str = obj["Description"]
      self.ValidationExp:str = obj["ValidationExp"]
      self.ValidationMsg:str = obj["ValidationMsg"]
      self.Version:int = obj["Version"]
      self.TableType:str = obj["TableType"]
      self.SysRowID:str = obj["SysRowID"]
      self.SchemaName:str = obj["SchemaName"]
      """  Schema Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_FileSchemaTableset:
   def __init__(self, obj):
      self.FileSchema:list[Ice_Tablesets_FileSchemaRow] = obj["FileSchema"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_IndexFieldSchemaRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.IndexName:str = obj["IndexName"]
      self.IndexRecid:int = obj["IndexRecid"]
      self.IndexSeq:int = obj["IndexSeq"]
      self.FieldRecid:int = obj["FieldRecid"]
      self.FieldName:str = obj["FieldName"]
      self.IsAscending:bool = obj["IsAscending"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IndexFieldSchemaTableset:
   def __init__(self, obj):
      self.IndexFieldSchema:list[Ice_Tablesets_IndexFieldSchemaRow] = obj["IndexFieldSchema"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_IndexSchemaRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.FileRecid:int = obj["FileRecid"]
      self.IndexName:str = obj["IndexName"]
      self.IsPrimary:bool = obj["IsPrimary"]
      self.IsUnique:bool = obj["IsUnique"]
      self.NumComp:int = obj["NumComp"]
      self.IndexNum:int = obj["IndexNum"]
      self.Active:bool = obj["Active"]
      self.WordIndex:int = obj["WordIndex"]
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.Fields:str = obj["Fields"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IndexSchemaTableset:
   def __init__(self, obj):
      self.IndexSchema:list[Ice_Tablesets_IndexSchemaRow] = obj["IndexSchema"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class TableSchemaList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ValidateFieldName_input:
   """ Required : 
   schemaName
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name of the table  """  
      self.tableName:str = obj["tableName"]
      """  name of the table  """  
      self.fieldName:str = obj["fieldName"]
      """  name of the table  """  
      pass

class ValidateFieldName_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  The dataset represents the file object  """  
      pass

class ValidateTableName_input:
   """ Required : 
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema name of the table  """  
      self.tableName:str = obj["tableName"]
      """  name of the table  """  
      pass

class ValidateTableName_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  The dataset represents the file object  """  
      pass

