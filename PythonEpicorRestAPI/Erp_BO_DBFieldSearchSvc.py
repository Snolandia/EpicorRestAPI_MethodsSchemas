import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DBFieldSearchSvc
# Description: Database Fields Search Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DBFieldSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DBFieldSearchSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DBFieldListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DBFieldSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns DB Fields from _Field
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DBFieldSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DBFieldListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DBFieldListRow] = obj["value"]
      pass

class Erp_Tablesets_DBFieldListRow:
   def __init__(self, obj):
      self.CaseSensitive:bool = obj["CaseSensitive"]
      """  Indicates if the field is case sensitive  """  
      self.ColumnLabel:str = obj["ColumnLabel"]
      """  Column Label  """  
      self.DataType:str = obj["DataType"]
      self.Extent:int = obj["Extent"]
      """  Number of extents if the field is an array  """  
      self.FieldDecimals:int = obj["FieldDecimals"]
      """  Number of decimal places to the right of the decimal  """  
      self.FieldDescription:str = obj["FieldDescription"]
      """  Description  """  
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldHelp:str = obj["FieldHelp"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.FieldName:str = obj["FieldName"]
      self.FieldOrder:int = obj["FieldOrder"]
      """  Schema Field Order  """  
      self.FieldViewAs:str = obj["FieldViewAs"]
      """  View As format  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.InitialValue:str = obj["InitialValue"]
      """  Initial value  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  Mandatory  """  
      self.ValMsg:str = obj["ValMsg"]
      """  Validation Message  """  
      self.ValPhrase:str = obj["ValPhrase"]
      """  Validation Phrase  """  
      self.VBField:bool = obj["VBField"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_DBFieldListRow:
   def __init__(self, obj):
      self.CaseSensitive:bool = obj["CaseSensitive"]
      """  Indicates if the field is case sensitive  """  
      self.ColumnLabel:str = obj["ColumnLabel"]
      """  Column Label  """  
      self.DataType:str = obj["DataType"]
      self.Extent:int = obj["Extent"]
      """  Number of extents if the field is an array  """  
      self.FieldDecimals:int = obj["FieldDecimals"]
      """  Number of decimal places to the right of the decimal  """  
      self.FieldDescription:str = obj["FieldDescription"]
      """  Description  """  
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldHelp:str = obj["FieldHelp"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.FieldName:str = obj["FieldName"]
      self.FieldOrder:int = obj["FieldOrder"]
      """  Schema Field Order  """  
      self.FieldViewAs:str = obj["FieldViewAs"]
      """  View As format  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.InitialValue:str = obj["InitialValue"]
      """  Initial value  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  Mandatory  """  
      self.ValMsg:str = obj["ValMsg"]
      """  Validation Message  """  
      self.ValPhrase:str = obj["ValPhrase"]
      """  Validation Phrase  """  
      self.VBField:bool = obj["VBField"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DBFieldListTableset:
   def __init__(self, obj):
      self.DBFieldList:list[Erp_Tablesets_DBFieldListRow] = obj["DBFieldList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DBFieldListTableset] = obj["returnObj"]
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

