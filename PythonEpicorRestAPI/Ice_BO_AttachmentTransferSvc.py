import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.AttachmentTransferSvc
# Description: File Attachments
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetFileStoreList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFileStoreList
   Description: Get list of attachments stored as files
   OperationID: GetFileStoreList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFileStoreList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFileStoreList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDocTypeList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDocTypeList
   Description: Get List of existing attachment types
   OperationID: GetDocTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDocTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDocTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteOrpanedRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteOrpanedRecords
   Description: Delete records from child table that do not have records in the parent table
   OperationID: DeleteOrpanedRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteOrpanedRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteOrpanedRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRecordsWithoutFiles(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRecordsWithoutFiles
   Description: Delete records that do not have correspondent files
   OperationID: DeleteRecordsWithoutFiles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRecordsWithoutFiles_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRecordsWithoutFiles_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateBasePath(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateBasePath
   Description: Change path for files to new location
   OperationID: UpdateBasePath
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateBasePath_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBasePath_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DeleteOrpanedRecords_input:
   """ Required : 
   company
   docType
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.docType:str = obj["docType"]
      pass

class DeleteOrpanedRecords_output:
   def __init__(self, obj):
      pass

class DeleteRecordsWithoutFiles_input:
   """ Required : 
   company
   docType
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.docType:str = obj["docType"]
      pass

class DeleteRecordsWithoutFiles_output:
   def __init__(self, obj):
      pass

class GetDocTypeList_input:
   """ Required : 
   Company
   docTypeID
   """  
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.docTypeID:str = obj["docTypeID"]
      pass

class GetDocTypeList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AttachmentTransferTableset] = obj["returnObj"]
      pass

class GetFileStoreList_input:
   """ Required : 
   Company
   docTypeID
   problemsOnly
   checkFileExists
   """  
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company to select attachments  """  
      self.docTypeID:str = obj["docTypeID"]
      """  DocTypeID of attachment - or empty for default attachments  """  
      self.problemsOnly:bool = obj["problemsOnly"]
      self.checkFileExists:bool = obj["checkFileExists"]
      pass

class GetFileStoreList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AttachmentTransferTableset] = obj["returnObj"]
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

class Ice_Tablesets_AttachmentTransferDocTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.FileTransferMode:int = obj["FileTransferMode"]
      self.FileTransferModeResolved:str = obj["FileTransferModeResolved"]
      self.BaseURL:str = obj["BaseURL"]
      self.Status:str = obj["Status"]
      self.StatusText:str = obj["StatusText"]
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AttachmentTransferFileRefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.XFileName:str = obj["XFileName"]
      self.Status:str = obj["Status"]
      self.StatusText:str = obj["StatusText"]
      self.RelatedToFile:str = obj["RelatedToFile"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      self.StorageType:int = obj["StorageType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AttachmentTransferRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BaseFolder:str = obj["BaseFolder"]
      self.FileTransferMode:int = obj["FileTransferMode"]
      self.FileTransferModeResolved:str = obj["FileTransferModeResolved"]
      self.Status:str = obj["Status"]
      self.StatusText:str = obj["StatusText"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AttachmentTransferTableset:
   def __init__(self, obj):
      self.AttachmentTransfer:list[Ice_Tablesets_AttachmentTransferRow] = obj["AttachmentTransfer"]
      self.AttachmentTransferDocType:list[Ice_Tablesets_AttachmentTransferDocTypeRow] = obj["AttachmentTransferDocType"]
      self.AttachmentTransferFileRef:list[Ice_Tablesets_AttachmentTransferFileRefRow] = obj["AttachmentTransferFileRef"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateBasePath_input:
   """ Required : 
   company
   docType
   existingPath
   newBasePath
   batchSize
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.docType:str = obj["docType"]
      self.existingPath:str = obj["existingPath"]
      """  existing path  """  
      self.newBasePath:str = obj["newBasePath"]
      """  new path to use  """  
      self.batchSize:int = obj["batchSize"]
      """  number of items to move in one transaction  """  
      pass

class UpdateBasePath_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

