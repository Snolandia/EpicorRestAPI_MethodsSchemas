import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.ClassAttributeSvc
# Description: Provides attributes for a service
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetAttributes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAttributes
   Description: Get Attributes for set of class names and namespace
   OperationID: GetAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAttributesForAllTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAttributesForAllTables
   Description: Get attributes for a set of class names and namespace (including Extension tables if in the list).
   OperationID: GetAttributesForAllTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributesForAllTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributesForAllTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAttributesForTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAttributesForTable
   Description: Get Attributes for one table
   OperationID: GetAttributesForTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributesForTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributesForTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllAttributesForTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllAttributesForTables
   Description: Gets the base and user defined attributes for several tables
   OperationID: GetAllAttributesForTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllAttributesForTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllAttributesForTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAttributesForTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAttributesForTables
   Description: Get Attributes for several tables - must be qualified as SchemaName.DataTableID
   OperationID: GetAttributesForTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributesForTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributesForTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUDColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUDColumns
   Description: Get Attributes for set of ud class names and namespace
   OperationID: GetUDColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUDColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUDColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAttributesForExtensionTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAttributesForExtensionTable
   Description: Get attributes for the extension tables, defined for the main dataset in the class
   OperationID: GetAttributesForExtensionTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributesForExtensionTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributesForExtensionTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetAllAttributesForTables_input:
   """ Required : 
   dataTables
   propertiesFilter
   """  
   def __init__(self, obj):
      self.dataTables:str = obj["dataTables"]
      """  The list of data tables. Must be qualified as SystemCode.DataTableID~DataSetID.
            The DataSetID is used to retrieve Peer Extension tables and columns. If not present, only ERP ZData based tables will be returned.  """  
      self.propertiesFilter:str = obj["propertiesFilter"]
      """  The properties to filter the results.  """  
      pass

class GetAllAttributesForTables_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetAttributesForAllTables_input:
   """ Required : 
   companyID
   classNames
   nameSpace
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  company ID.  """  
      self.classNames:str = obj["classNames"]
      """  list of class names.  """  
      self.nameSpace:str = obj["nameSpace"]
      """  Namespace (Ex: Ice, Erp).  """  
      pass

class GetAttributesForAllTables_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ClassAttributeTableset] = obj["returnObj"]
      pass

class GetAttributesForExtensionTable_input:
   """ Required : 
   companyID
   classNames
   nameSpace
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company ID where extension table is defined. If empty, current company will be used.  """  
      self.classNames:str = obj["classNames"]
      """  Class name or class names, separated by comma  """  
      self.nameSpace:str = obj["nameSpace"]
      """  Namespace for the class(es)  """  
      pass

class GetAttributesForExtensionTable_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ClassAttributeTableset] = obj["returnObj"]
      pass

class GetAttributesForTable_input:
   """ Required : 
   schemaName
   dataTableID
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class GetAttributesForTable_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ClassAttributeTableset] = obj["returnObj"]
      pass

class GetAttributesForTables_input:
   """ Required : 
   dataTables
   """  
   def __init__(self, obj):
      self.dataTables:str = obj["dataTables"]
      pass

class GetAttributesForTables_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ClassAttributeTableset] = obj["returnObj"]
      pass

class GetAttributes_input:
   """ Required : 
   classNames
   nameSpace
   """  
   def __init__(self, obj):
      self.classNames:str = obj["classNames"]
      self.nameSpace:str = obj["nameSpace"]
      pass

class GetAttributes_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ClassAttributeTableset] = obj["returnObj"]
      pass

class GetUDColumns_input:
   """ Required : 
   classNames
   nameSpace
   """  
   def __init__(self, obj):
      self.classNames:str = obj["classNames"]
      self.nameSpace:str = obj["nameSpace"]
      pass

class GetUDColumns_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ClassAttributeTableset] = obj["returnObj"]
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

class Ice_Tablesets_ClassAttributeRow:
   def __init__(self, obj):
      self.DataSetID:str = obj["DataSetID"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.AttributeName:str = obj["AttributeName"]
      self.AttributeValue:str = obj["AttributeValue"]
      self.ClassName:str = obj["ClassName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ClassAttributeTableset:
   def __init__(self, obj):
      self.ClassAttribute:list[Ice_Tablesets_ClassAttributeRow] = obj["ClassAttribute"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

