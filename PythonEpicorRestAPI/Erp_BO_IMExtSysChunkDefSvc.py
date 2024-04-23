import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMExtSysChunkDefSvc
# Description: Business Object to handle: Count, Get, Ack, and GetAll of ExtSysChunkDef
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMExtSysChunkDefSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMExtSysChunkDefSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AckExtSysChunkDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AckExtSysChunkDef
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckExtSysChunkDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckExtSysChunkDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckExtSysChunkDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMExtSysChunkDefSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CountExtSysChunkDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CountExtSysChunkDef
   Description: Returns the count of existing IntQueOut records along with the count of updated ExtSysChunkDef in the database that IntQueOut records have not yet been created for
   OperationID: CountExtSysChunkDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountExtSysChunkDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountExtSysChunkDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMExtSysChunkDefSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllExtSysChunkDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllExtSysChunkDef
   Description: Generates IntQueOut and IMExtSysChunkDef rows since the last time this was called and then returns these along with any existing
No difference between GetAllExtSysChunkDef and GetExtSysChunkDef for this object
   OperationID: GetAllExtSysChunkDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllExtSysChunkDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllExtSysChunkDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMExtSysChunkDefSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExtSysChunkDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExtSysChunkDef
   Description: Generates IntQueOut and IMExtSysChunkDef rows since the last time this was called and then returns these along with any existing
No difference between GetAllExtSysChunkDef and GetExtSysChunkDef for this object
   OperationID: GetExtSysChunkDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExtSysChunkDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtSysChunkDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMExtSysChunkDefSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AckExtSysChunkDef_input:
   """ Required : 
   ts
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.ts:list[Erp_Tablesets_IMExtSysChunkDefTableset] = obj["ts"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class AckExtSysChunkDef_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class CountExtSysChunkDef_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class CountExtSysChunkDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMExtSysChunkDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ChunkID:int = obj["ChunkID"]
      """  ChunkID  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique idenfitier for record group  """  
      self.UpdateSource:str = obj["UpdateSource"]
      """  The source of the chunk. Used when consumer of message needs to perform logic in response  """  
      self.UpdateAction:str = obj["UpdateAction"]
      """  The action chunk relates to. Used when consumer of message needs to perform logic in response.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Related Service Order Number from FSA  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Related Service Order Resource Number from FSA  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMExtSysChunkDefTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMExtSysChunk:list[Erp_Tablesets_IMExtSysChunkRow] = obj["IMExtSysChunk"]
      self.IMExtSysChunkDef:list[Erp_Tablesets_IMExtSysChunkDefRow] = obj["IMExtSysChunkDef"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMExtSysChunkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ChunkID:int = obj["ChunkID"]
      """  ChunkID  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.Chunk:str = obj["Chunk"]
      """  Chunk  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique idenfitier for record group  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntQueInOutRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique key from IntQueIn or IntQueOut  """  
      self.Action:str = obj["Action"]
      """  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  """  
      self.IncomingOutgoing:str = obj["IncomingOutgoing"]
      """  "I" for incoming or "O" for outgoing  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAllExtSysChunkDef_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetAllExtSysChunkDef_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMExtSysChunkDefTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetExtSysChunkDef_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetExtSysChunkDef_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMExtSysChunkDefTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

