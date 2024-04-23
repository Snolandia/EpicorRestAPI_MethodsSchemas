import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ChgLogSvc
# Description: bo/ChgLog/ChgLog.p
           Generic Change Log - BL
           Rajesh Tapde
           06-19-2003
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ChgLogSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ChgLogSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetChgLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetChgLog
   Description: Gets the related ChgLog records based on TableName,RowID
   OperationID: GetChgLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetChgLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChgLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ChgLogSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetChgLogByClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetChgLogByClause
   Description: Gets the related ChgLog records based on where clause passed in
   OperationID: GetChgLogByClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetChgLogByClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChgLogByClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ChgLogSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GetChgLogByClause_input:
   """ Required : 
   ip_WhereClause
   """  
   def __init__(self, obj):
      self.ip_WhereClause:str = obj["ip_WhereClause"]
      """  Where clause used for retrieval  """  
      pass

class GetChgLogByClause_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ChgLogTableset] = obj["returnObj"]
      pass

class GetChgLog_input:
   """ Required : 
   ip_systemCode
   ip_tableName
   ip_sysRowID
   """  
   def __init__(self, obj):
      self.ip_systemCode:str = obj["ip_systemCode"]
      """  SystemCode to retrieve ChgLog records for  """  
      self.ip_tableName:str = obj["ip_tableName"]
      """  Table name to retrieve ChgLog records for  """  
      self.ip_sysRowID:str = obj["ip_sysRowID"]
      """  RowID of the record to retrieve ChgLog records for  """  
      pass

class GetChgLog_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ChgLogTableset] = obj["returnObj"]
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

class Ice_Tablesets_ChgLogRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Identifier:str = obj["Identifier"]
      """  The identifier is used to group the changes made to related tables together. This value is assigned by the system using the value found in ZDataField.ChgLogID.  For example: Customer, ShipTo, CustBillTo, CustCnt, are all related and will have a ChgLogID = "Customer".  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  Name of the table which was changed  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record.  For example: For a "PO" change record this field would contain the related PO Number,  for a "SO" change record it would contain the related SO Number.  """  
      self.Key2:str = obj["Key2"]
      """   tilde separated list of key values of the changed record
For Example a ChgLog for POREL might be something like 301~2~1. 301 is the PONum, 2 is the LineNum and 1 is the ReleaseNum  """  
      self.Key3:str = obj["Key3"]
      """  Third component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  """  
      self.DateStampedOn:str = obj["DateStampedOn"]
      """  DateStampedOn  """  
      self.LogText:str = obj["LogText"]
      """   Log message text.  This text may be in the following formats:
1) "New Record"
2) UserID  Time  FieldLabel/Name  OldValue "->" NewValue  """  
      self.LogNum:int = obj["LogNum"]
      """  This field allows one record to have more than one change log for a day.  This is to fix the issue of storing more than 32K in logtext field  """  
      self.UserID:str = obj["UserID"]
      """  The User ID that created this log.  """  
      self.ChgLogMethod:str = obj["ChgLogMethod"]
      """   Possible values D & U (Described in XbSyst.ChgLogMethod).
For value D (Daily), the DCDUserID value is blank. For value U (User), the DCDUserID is populated.  """  
      self.ChgLogSeq:int = obj["ChgLogSeq"]
      """   For future use.

An integer assigned by the system to uniquely identify the ChgLog record.  This integer is created by using the database sequence "ChgLogSeq".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ChgLogTableset:
   def __init__(self, obj):
      self.ChgLog:list[Ice_Tablesets_ChgLogRow] = obj["ChgLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

