import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.AdminSessionSvc
# Description: Session maintenance business object for use by Admin Console
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AdminSessionListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Get list of sessions
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DeleteBySessionId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteBySessionId
   Description: This method deletes the session with the specified SessionId
   OperationID: DeleteBySessionId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteBySessionId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteBySessionId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteBySysRowId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteBySysRowId
   Description: This method deletes the session with the specified SysRowId
   OperationID: DeleteBySysRowId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteBySysRowId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteBySysRowId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentSession(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentSession
   Description: Returns the current session.
   OperationID: GetCurrentSession
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentSession_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetSessionList(epicorHeaders = None):
   """  
   Summary: Invoke method GetSessionList
   Description: Returns a list of all users sessions.
   OperationID: GetSessionList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSessionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetFilteredSessionList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFilteredSessionList
   Description: Returns a list of all users sessions.
   OperationID: GetFilteredSessionList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFilteredSessionList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFilteredSessionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockSessionCreation(epicorHeaders = None):
   """  
   Summary: Invoke method LockSessionCreation
   Description: Locks new sessions from being created. Usually for System Maintenance.
   OperationID: LockSessionCreation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockSessionCreation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_UnlockSessionCreation(epicorHeaders = None):
   """  
   Summary: Invoke method UnlockSessionCreation
   Description: Stops the new SessionCreation lock. Usually when a maintenance process is complete.
   OperationID: UnlockSessionCreation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockSessionCreation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_IsLockedForSessionCreation(epicorHeaders = None):
   """  
   Summary: Invoke method IsLockedForSessionCreation
   Description: Checks on the status of Session Creation lock
   OperationID: IsLockedForSessionCreation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsLockedForSessionCreation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List",headers=creds) as resp:
           return await resp.json()

async def get_GetSessionIdleTimeout(epicorHeaders = None):
   """  
   Summary: Invoke method GetSessionIdleTimeout
   Description: Gets the session idle timeout, i.e. the time period (in minutes) after which a session can be deleted if
there is no activity.
   OperationID: Get_GetSessionIdleTimeout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSessionIdleTimeout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SetSessionIdleTimeout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetSessionIdleTimeout
   Description: Updates the session idle timeout (in minutes).
   OperationID: SetSessionIdleTimeout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSessionIdleTimeout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSessionIdleTimeout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBaqHierarchicalQueryTimeout(epicorHeaders = None):
   """  
   Summary: Invoke method GetBaqHierarchicalQueryTimeout
   Description: Gets the BAQ hierarchical query execution timeout (in seconds).
   OperationID: Get_GetBaqHierarchicalQueryTimeout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBaqHierarchicalQueryTimeout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SetBaqHierarchicalQueryTimeout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetBaqHierarchicalQueryTimeout
   Description: Updates the BAQ hierarchical query execution timeout (in seconds).
   OperationID: SetBaqHierarchicalQueryTimeout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetBaqHierarchicalQueryTimeout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetBaqHierarchicalQueryTimeout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminSessionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AdminSessionListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_AdminSessionListRow] = obj["value"]
      pass

class Ice_Tablesets_AdminSessionListRow:
   def __init__(self, obj):
      self.LicNum:int = obj["LicNum"]
      """  License number.  """  
      self.SessionID:str = obj["SessionID"]
      self.CurUserID:str = obj["CurUserID"]
      self.LastDate:str = obj["LastDate"]
      """  Date the user last logged into the system.  """  
      self.CurComp:str = obj["CurComp"]
      """  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  """  
      self.SessionType:str = obj["SessionType"]
      self.Suspended:bool = obj["Suspended"]
      self.Suspend:bool = obj["Suspend"]
      self.Timeout:int = obj["Timeout"]
      self.ClientComputerName:str = obj["ClientComputerName"]
      self.SerialNum:int = obj["SerialNum"]
      """  Customer's License Serial Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LicenseType:str = obj["LicenseType"]
      self.Expired:bool = obj["Expired"]
      self.UserName:str = obj["UserName"]
      self.SessionTypeDescription:str = obj["SessionTypeDescription"]
      self.InUse:bool = obj["InUse"]
      """  Session in use  """  
      self.InstallationName:str = obj["InstallationName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteBySessionId_input:
   """ Required : 
   sessionId
   """  
   def __init__(self, obj):
      self.sessionId:str = obj["sessionId"]
      """  SessionId for session to be deleted  """  
      pass

class DeleteBySessionId_output:
   def __init__(self, obj):
      pass

class DeleteBySysRowId_input:
   """ Required : 
   sessionID
   """  
   def __init__(self, obj):
      self.sessionID:str = obj["sessionID"]
      """  SysRowId for session to be deleted  """  
      pass

class DeleteBySysRowId_output:
   def __init__(self, obj):
      pass

class GetBaqHierarchicalQueryTimeout_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  the BAQ hierarchical query execution timeout (in seconds).  """  
      pass

class GetCurrentSession_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminSessionListTableset] = obj["returnObj"]
      pass

class GetFilteredSessionList_input:
   """ Required : 
   filter
   """  
   def __init__(self, obj):
      self.filter:int = obj["filter"]
      """  Determines which kind of sessions to show  """  
      pass

class GetFilteredSessionList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminSessionListTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_AdminSessionListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSessionIdleTimeout_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  the session idle timeout (in minutes)  """  
      pass

class GetSessionList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminSessionListTableset] = obj["returnObj"]
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

class Ice_Tablesets_AdminSessionListRow:
   def __init__(self, obj):
      self.LicNum:int = obj["LicNum"]
      """  License number.  """  
      self.SessionID:str = obj["SessionID"]
      self.CurUserID:str = obj["CurUserID"]
      self.LastDate:str = obj["LastDate"]
      """  Date the user last logged into the system.  """  
      self.CurComp:str = obj["CurComp"]
      """  Represents the current or Last company logged on to by the user. This is used as default next time they log on.  """  
      self.SessionType:str = obj["SessionType"]
      self.Suspended:bool = obj["Suspended"]
      self.Suspend:bool = obj["Suspend"]
      self.Timeout:int = obj["Timeout"]
      self.ClientComputerName:str = obj["ClientComputerName"]
      self.SerialNum:int = obj["SerialNum"]
      """  Customer's License Serial Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LicenseType:str = obj["LicenseType"]
      self.Expired:bool = obj["Expired"]
      self.UserName:str = obj["UserName"]
      self.SessionTypeDescription:str = obj["SessionTypeDescription"]
      self.InUse:bool = obj["InUse"]
      """  Session in use  """  
      self.InstallationName:str = obj["InstallationName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AdminSessionListTableset:
   def __init__(self, obj):
      self.AdminSessionList:list[Ice_Tablesets_AdminSessionListRow] = obj["AdminSessionList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class IsLockedForSessionCreation_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  The SessionCreation lock state  """  
      pass

class LockSessionCreation_output:
   def __init__(self, obj):
      pass

class SetBaqHierarchicalQueryTimeout_input:
   """ Required : 
   value
   """  
   def __init__(self, obj):
      self.value:int = obj["value"]
      pass

class SetBaqHierarchicalQueryTimeout_output:
   def __init__(self, obj):
      pass

class SetSessionIdleTimeout_input:
   """ Required : 
   value
   """  
   def __init__(self, obj):
      self.value:int = obj["value"]
      pass

class SetSessionIdleTimeout_output:
   def __init__(self, obj):
      pass

class UnlockSessionCreation_output:
   def __init__(self, obj):
      pass

