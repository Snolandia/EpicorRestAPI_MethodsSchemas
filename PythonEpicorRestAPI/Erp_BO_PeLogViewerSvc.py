import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PeLogViewerSvc
# Description: PELogViewer Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePeLogViewer, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a tableset that satisfy the where clause
   OperationID: Get_GetRows
      :param whereClausePeLogViewer: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
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
   params += "whereClausePeLogViewer=" + whereClausePeLogViewer
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_InitPath(epicorHeaders = None):
   """  
   Summary: Invoke method InitPath
   Description: This procedure init path for pelog.txt file on first PELogViewer UI call
   OperationID: InitPath
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitPath_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ClearLog(epicorHeaders = None):
   """  
   Summary: Invoke method ClearLog
   Description: This procedure supposed to delete old logging file. (pelog.txt)
   OperationID: ClearLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetPostModeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetPostModeList
   OperationID: GetPostModeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostModeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetCompanyList(epicorHeaders = None):
   """  
   Summary: Invoke method GetCompanyList
   OperationID: GetCompanyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetTransactionTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetTransactionTypeList
   Description: The list of possible Transaction Types (ACTTypes) across available companies
   OperationID: GetTransactionTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransactionTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetValidList(epicorHeaders = None):
   """  
   Summary: Invoke method GetValidList
   OperationID: GetValidList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValidList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPELogInfoByPostingUIDExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPELogInfoByPostingUIDExt
   Description: This function should return dataset containing logging infromation
about requested posting process. The clone of GetPELogInfoByPostingUID which returns the requested data as the function result
   OperationID: GetPELogInfoByPostingUIDExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPELogInfoByPostingUIDExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPELogInfoByPostingUIDExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPELogInfoByPostingUID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPELogInfoByPostingUID
   Description: This function should return dataset containing logging infromation
about requested posting process
   OperationID: GetPELogInfoByPostingUID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPELogInfoByPostingUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPELogInfoByPostingUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetActTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetActTypeList
   Description: Returns DataSet containing all Transaction types
   OperationID: GetActTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SaveActTypeList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveActTypeList
   Description: Applies changes in logging settings
   OperationID: SaveActTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveActTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveActTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPELogInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPELogInfo
   Description: This function should return dataset containing logging infromation
about requested posting process
   OperationID: GetPELogInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPELogInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPELogInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FileType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FileType
   Description: File Type check
   OperationID: FileType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDelims(epicorHeaders = None):
   """  
   Summary: Invoke method GetDelims
   Description: Returns list delimiters
   OperationID: GetDelims
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDelims_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ExportLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportLog
   Description: Export PE Log into the file
   OperationID: ExportLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportLog
   Description: Import PE Log file into the PE Log cache
   OperationID: ImportLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetNodeById(GPostingUID, NodeID, epicorHeaders = None):
   """  
   Summary: Invoke method GetNodeById
   Description: Use the posting Guid 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 or 0ae29784-6050-40a0-8764-099439c5b09b for test purposes
   OperationID: Get_GetNodeById
      :param GPostingUID: Desc: 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149   Required: True   Allow empty value : True
      :param NodeID: Desc: 0 to load parent   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNodeById_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "GPostingUID=" + GPostingUID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "NodeID=" + NodeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_FindNode(GPostingUID, searchText, direction, currentNodeID, epicorHeaders = None):
   """  
   Summary: Invoke method FindNode
   Description: Search node in the tree by the text
   OperationID: Get_FindNode
      :param GPostingUID: Desc: The posting log id (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 or 0ae29784-6050-40a0-8764-099439c5b09b for test purposes)   Required: True   Allow empty value : True
      :param searchText: Desc: Search text   Required: True   Allow empty value : True
      :param direction: Desc: Direction of the search: 0 - search forward, 1- search backward   Required: True
      :param currentNodeID: Desc: The start point for the search (empty string - search will be performed at the beginning of the log)   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindNode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "GPostingUID=" + GPostingUID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "searchText=" + searchText
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "direction=" + direction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "currentNodeID=" + currentNodeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ClearLog_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PEActTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CompanyName:str = obj["CompanyName"]
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      self.ACTTypeName:str = obj["ACTTypeName"]
      self.Logging:bool = obj["Logging"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PEActTypeTableset:
   def __init__(self, obj):
      self.PEActType:list[Erp_Tablesets_PEActTypeRow] = obj["PEActType"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PeLogViewerListRow:
   def __init__(self, obj):
      self.ActType:str = obj["ActType"]
      self.PostDate:str = obj["PostDate"]
      """  PostDate  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.RJ:int = obj["RJ"]
      """  RvJrnUID  """  
      self.Valid:bool = obj["Valid"]
      """  IsValid  """  
      self.XmlText:str = obj["XmlText"]
      """  XmlText  """  
      self.GPostingUID:str = obj["GPostingUID"]
      """  GPostingUID  """  
      self.PostMode:str = obj["PostMode"]
      """  PostMode  """  
      self.LineNum:int = obj["LineNum"]
      """  LineNum  """  
      self.ParentLineNum:int = obj["ParentLineNum"]
      """  ParentLineNum  """  
      self.Offset:int = obj["Offset"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PeLogViewerListTableset:
   def __init__(self, obj):
      self.PeLogViewerList:list[Erp_Tablesets_PeLogViewerListRow] = obj["PeLogViewerList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PeLogViewerRow:
   def __init__(self, obj):
      self.ActType:str = obj["ActType"]
      self.PostDate:str = obj["PostDate"]
      """  PostDate  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.RJ:int = obj["RJ"]
      """  RvJrnUID  """  
      self.Valid:bool = obj["Valid"]
      """  IsValid  """  
      self.XmlText:str = obj["XmlText"]
      """  XmlText  """  
      self.GPostingUID:str = obj["GPostingUID"]
      """  GPostingUID  """  
      self.PostMode:str = obj["PostMode"]
      """  PostMode  """  
      self.LineNum:int = obj["LineNum"]
      """  LineNum  """  
      self.ParentLineNum:int = obj["ParentLineNum"]
      """  ParentLineNum  """  
      self.Offset:int = obj["Offset"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PeLogViewerTableset:
   def __init__(self, obj):
      self.PeLogViewer:list[Erp_Tablesets_PeLogViewerRow] = obj["PeLogViewer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportLog_input:
   """ Required : 
   GPostingUID
   ipSpecialFolder
   ipFileName
   """  
   def __init__(self, obj):
      self.GPostingUID:str = obj["GPostingUID"]
      """  the UID of the PE Log  """  
      self.ipSpecialFolder:int = obj["ipSpecialFolder"]
      """  Special Folder  """  
      self.ipFileName:str = obj["ipFileName"]
      """  File Name in the Special Folder  """  
      pass

class ExportLog_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFileName:str = obj["parameters"]
      pass

      """  output parameters  """  

class FileType_input:
   """ Required : 
   FileInfo
   """  
   def __init__(self, obj):
      self.FileInfo:str = obj["FileInfo"]
      pass

class FileType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class FindNode_input:
   """ Required : 
   GPostingUID
   searchText
   direction
   currentNodeID
   """  
   def __init__(self, obj):
      self.GPostingUID:str = obj["GPostingUID"]
      """  The posting log id (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 or 0ae29784-6050-40a0-8764-099439c5b09b for test purposes)  """  
      self.searchText:str = obj["searchText"]
      """  Search text  """  
      self.direction:int = obj["direction"]
      """  Direction of the search: 0 - search forward, 1- search backward  """  
      self.currentNodeID:str = obj["currentNodeID"]
      """  The start point for the search (empty string - search will be performed at the beginning of the log)  """  
      pass

class FindNode_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  LogNode structure with the found node and all parent ones  """  
      pass

   def parameters(self, obj):
      self.foundNodeId:str = obj["parameters"]
      self.nextFoundNodeId:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetActTypeList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PEActTypeTableset] = obj["returnObj"]
      pass

class GetCompanyList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  list of posting modes  """  
      pass

class GetDelims_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ListDelim:str = obj["parameters"]
      self.SublistDelim:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   ds
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      self.ds:list[Erp_Tablesets_PeLogViewerListTableset] = obj["ds"]
      pass

class GetList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      self.ds:list[Erp_Tablesets_PeLogViewerListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNodeById_input:
   """ Required : 
   GPostingUID
   NodeID
   """  
   def __init__(self, obj):
      self.GPostingUID:str = obj["GPostingUID"]
      """  0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149  """  
      self.NodeID:str = obj["NodeID"]
      """  0 to load parent  """  
      pass

class GetNodeById_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetPELogInfoByPostingUIDExt_input:
   """ Required : 
   GPostingUID
   """  
   def __init__(self, obj):
      self.GPostingUID:str = obj["GPostingUID"]
      """  The Positng ID  """  
      pass

class GetPELogInfoByPostingUIDExt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PeLogViewerTableset] = obj["returnObj"]
      pass

class GetPELogInfoByPostingUID_input:
   """ Required : 
   GPostingUID
   ds
   """  
   def __init__(self, obj):
      self.GPostingUID:str = obj["GPostingUID"]
      self.ds:list[Erp_Tablesets_PeLogViewerTableset] = obj["ds"]
      pass

class GetPELogInfoByPostingUID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PeLogViewerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPELogInfo_input:
   """ Required : 
   inActType
   inPostDate
   inGroupID
   inRJ
   inValid
   inPostMode
   ds
   """  
   def __init__(self, obj):
      self.inActType:str = obj["inActType"]
      """  Act type name  """  
      self.inPostDate:str = obj["inPostDate"]
      """  Posting Date  """  
      self.inGroupID:str = obj["inGroupID"]
      """  posting group id  """  
      self.inRJ:int = obj["inRJ"]
      """  review journal number  """  
      self.inValid:str = obj["inValid"]
      """  valid review journal  """  
      self.inPostMode:str = obj["inPostMode"]
      """  posting process mode  """  
      self.ds:list[Erp_Tablesets_PeLogViewerTableset] = obj["ds"]
      pass

class GetPELogInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PeLogViewerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPostModeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.PostModeList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePeLogViewer
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePeLogViewer:str = obj["whereClausePeLogViewer"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PeLogViewerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTransactionTypeList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetValidList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ValidList:str = obj["parameters"]
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

class ImportLog_input:
   """ Required : 
   ipSpecialFolder
   ipFileName
   """  
   def __init__(self, obj):
      self.ipSpecialFolder:int = obj["ipSpecialFolder"]
      """  Special Folder  """  
      self.ipFileName:str = obj["ipFileName"]
      """  File Name in the Special Folder  """  
      pass

class ImportLog_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PeLogViewerTableset] = obj["returnObj"]
      pass

class InitPath_output:
   def __init__(self, obj):
      pass

class SaveActTypeList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PEActTypeTableset] = obj["ds"]
      pass

class SaveActTypeList_output:
   def __init__(self, obj):
      pass

