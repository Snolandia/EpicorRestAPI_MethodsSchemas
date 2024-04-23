import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.SysMonitorSvc
# Description: The System Monitor service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetMonitorDataKeepIdleTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMonitorDataKeepIdleTime
   Description: Gets the task data for the user.
   OperationID: GetMonitorDataKeepIdleTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMonitorDataKeepIdleTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMonitorDataKeepIdleTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckForTaskUpdatesKeepIdleTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForTaskUpdatesKeepIdleTime
   Description: Checks for Ice.SysRptLst and/or Ice.SysTask updates. This may return false positives.
   OperationID: CheckForTaskUpdatesKeepIdleTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForTaskUpdatesKeepIdleTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForTaskUpdatesKeepIdleTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CancelTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelTask
   Description: Use to terminate a running task.
   OperationID: CancelTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetScheduledTasks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetScheduledTasks
   Description: To return the SysMonitorSchedDataSet which contains the scheduled tasks for a user.
   OperationID: GetScheduledTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetScheduledTasks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetScheduledTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaskHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaskHistory
   Description: To return Task history records for the current user for a specified number of days.
   OperationID: GetTaskHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTReports(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTReports
   Description: To return the SysMonitorDataSet which contains the SysTask and SysRptLst tables.
   OperationID: GetTReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReports(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReports
   Description: To return the SysMonitorDataSet which contains the SysRptLst tables.
   OperationID: GetReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCompanyList(epicorHeaders = None):
   """  
   Summary: Invoke method GetCompanyList
   Description: Return list of company current user has access to.
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_UpdateSysMonitorDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSysMonitorDS
   Description: Use to commit updates and deletions of the SysMonitor dataset to the database.
Does NOT support adding new records.
Does NOT support deletion of SysTask records.
   OperationID: UpdateSysMonitorDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSysMonitorDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSysMonitorDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateSysMonitorSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSysMonitorSched
   Description: Use to commit deletions of the SysMonitor dataset to the database.
Does NOT support adding or updating of records.
   OperationID: UpdateSysMonitorSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSysMonitorSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSysMonitorSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CancelTask_input:
   """ Required : 
   sysTaskNum
   """  
   def __init__(self, obj):
      self.sysTaskNum:int = obj["sysTaskNum"]
      """  System Task Number to be terminated.  """  
      pass

class CancelTask_output:
   def __init__(self, obj):
      pass

class CheckForTaskUpdatesKeepIdleTime_input:
   """ Required : 
   sysRptLstSysRevId
   workstationId
   sysTaskSysRevId
   historyOnly
   startedOn
   retrieveAllTasks
   """  
   def __init__(self, obj):
      self.sysRptLstSysRevId:int = obj["sysRptLstSysRevId"]
      """  The last Ice.SysRptLst.SysRevId value previously queried. Less than zero if checking not necessary.  """  
      self.workstationId:str = obj["workstationId"]
      """  The workstation identifier.  """  
      self.sysTaskSysRevId:int = obj["sysTaskSysRevId"]
      """  The last Ice.SysTask.SysRevId value previously queried. Less than zero if checking not necessary.  """  
      self.historyOnly:bool = obj["historyOnly"]
      """  `true` if only completed tasks should be queried. Otherwise, all tasks will be returned.  """  
      self.startedOn:str = obj["startedOn"]
      """  The date to start querying from. This should be UTC time.  """  
      self.retrieveAllTasks:bool = obj["retrieveAllTasks"]
      """  `true` if all Ice.SysTask rows should be returned. This can only be used by an administrator.  """  
      pass

class CheckForTaskUpdatesKeepIdleTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newerSysRptLstSysRevId:int = obj["parameters"]
      self.newerSysTaskSysRevId:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetCompanyList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetMonitorDataKeepIdleTime_input:
   """ Required : 
   querySysRptLst
   workstationId
   querySysTask
   querySysTaskLog
   historyOnly
   startedOn
   retrieveAllTasks
   """  
   def __init__(self, obj):
      self.querySysRptLst:bool = obj["querySysRptLst"]
      """  `true` if Ice.SysRptLst rows should be returned.  """  
      self.workstationId:str = obj["workstationId"]
      """  The workstation identifier.  """  
      self.querySysTask:bool = obj["querySysTask"]
      """  `true` if Ice.SysTask rows should be returned.  """  
      self.querySysTaskLog:bool = obj["querySysTaskLog"]
      """  `true` if Ice.SysTaskLog rows should be returned.  """  
      self.historyOnly:bool = obj["historyOnly"]
      """  `true` if only completed tasks should be queried. Otherwise, all tasks will be returned.  """  
      self.startedOn:str = obj["startedOn"]
      """  The UTC date/time to start querying from.  """  
      self.retrieveAllTasks:bool = obj["retrieveAllTasks"]
      """  `true` if all Ice.SysTask rows should be returned. This can only be used by an administrator.  """  
      pass

class GetMonitorDataKeepIdleTime_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysMonitorTableset] = obj["returnObj"]
      pass

class GetReports_input:
   """ Required : 
   rptUserID
   rptWorkStationID
   RetrivalType
   interval
   """  
   def __init__(self, obj):
      self.rptUserID:str = obj["rptUserID"]
      """  User ID for which you want SysRptLst records.
            Leave this blank to consider all users for available reports.  """  
      self.rptWorkStationID:str = obj["rptWorkStationID"]
      """  Computer/Workstation name for which you want SysRptLst records.  This an obsolete parameter and will be removed.
            Leave this blank to consider ALL workstations for available reports  """  
      self.RetrivalType:str = obj["RetrivalType"]
      """  Retrival type.  """  
      self.interval:int = obj["interval"]
      """  Retrival interval  """  
      pass

class GetReports_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysMonitorTableset] = obj["returnObj"]
      pass

class GetScheduledTasks_input:
   """ Required : 
   userIDent
   """  
   def __init__(self, obj):
      self.userIDent:str = obj["userIDent"]
      """  User ID for which you want the schedule tasks.
            Leave blank to consider all users.  """  
      pass

class GetScheduledTasks_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysMonitorSchedTableset] = obj["returnObj"]
      pass

class GetTReports_input:
   """ Required : 
   rptUserID
   rptWorkStationID
   """  
   def __init__(self, obj):
      self.rptUserID:str = obj["rptUserID"]
      """  User ID for which you want SysRptLst and SysTask records.
            Leave this blank to consider all users for available reports.  """  
      self.rptWorkStationID:str = obj["rptWorkStationID"]
      """  Computer/Workstation name for which you want SysRptLst records.
            Leave this blank to consider ALL workstations for available reports  """  
      pass

class GetTReports_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysMonitorTableset] = obj["returnObj"]
      pass

class GetTaskHistory_input:
   """ Required : 
   taskNumOfDays
   rptUserID
   """  
   def __init__(self, obj):
      self.taskNumOfDays:int = obj["taskNumOfDays"]
      """  The number of days from today you wish to retrieve task history for.  """  
      self.rptUserID:str = obj["rptUserID"]
      """  User ID for which you want SysRptLst and SysTask records.
            Leave this blank to consider all users for available reports.  """  
      pass

class GetTaskHistory_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysMonitorTaskHistTableset] = obj["returnObj"]
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

class Ice_Tablesets_SysAgentTaskRow:
   def __init__(self, obj):
      self.AgentID:str = obj["AgentID"]
      """  System Agent Number  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  System Agent Scheduling Number  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  System Agent Task Number  """  
      self.TaskDesc:str = obj["TaskDesc"]
      """  System Task Description  """  
      self.TaskType:str = obj["TaskType"]
      """  Valid Values:  Process, Report  """  
      self.RunProcedure:str = obj["RunProcedure"]
      """  Run Procedure  """  
      self.RunMethod:str = obj["RunMethod"]
      """  Method (internal procedure) of the "RunProcedure" that this task will perform.  """  
      self.SubmittedOn:str = obj["SubmittedOn"]
      """  SubmittedOn  """  
      self.SubmitUser:str = obj["SubmitUser"]
      """  Submitted by user  """  
      self.ParamMaintProgram:str = obj["ParamMaintProgram"]
      """   Name of .net program which is used to maintain the parameters.
Example: Epicor.Mfg.UI.xx/xxxxxxx.dll  """  
      self.Company:str = obj["Company"]
      """  Current Company when the task was created.  """  
      self.TaskNote:str = obj["TaskNote"]
      """  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  """  
      self.ProcessSetSystemCode:str = obj["ProcessSetSystemCode"]
      """  ProcessSetSystemCode  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.ProcessTaskNum:int = obj["ProcessTaskNum"]
      """  ProcessTask.SysTaskNum that originated the schedule  """  
      self.IsSystemTask:bool = obj["IsSystemTask"]
      """  IsSystemTask  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessSetCompany:str = obj["ProcessSetCompany"]
      """  ProcessSetCompany  """  
      self.NextRunOn:str = obj["NextRunOn"]
      """  Next Run on  """  
      self.SchedDesc:str = obj["SchedDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysMonitorSchedTableset:
   def __init__(self, obj):
      self.SysAgentTask:list[Ice_Tablesets_SysAgentTaskRow] = obj["SysAgentTask"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysMonitorTableset:
   def __init__(self, obj):
      self.SysRptLst:list[Ice_Tablesets_SysRptLstRow] = obj["SysRptLst"]
      self.SysTask:list[Ice_Tablesets_SysTaskRow] = obj["SysTask"]
      self.SysTaskLog:list[Ice_Tablesets_SysTaskLogRow] = obj["SysTaskLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysMonitorTaskHistTableset:
   def __init__(self, obj):
      self.SysTaskHist:list[Ice_Tablesets_SysTaskHistRow] = obj["SysTaskHist"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysRptLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.RecSeq:int = obj["RecSeq"]
      """  Record Sequence  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Description  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.HostComputer:str = obj["HostComputer"]
      """  Name of Computer on which the file is located.  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.RptStatus:str = obj["RptStatus"]
      """  Pending, Printing, Printed  """  
      self.LastActionOn:str = obj["LastActionOn"]
      """  LastActionOn  """  
      self.LastAction:str = obj["LastAction"]
      """  Last Action  """  
      self.OutPutToPrinter:str = obj["OutPutToPrinter"]
      """  Name of Printer to use for Auto Print reports  """  
      self.AutoAction:str = obj["AutoAction"]
      """  Print, Preview, None  """  
      self.PrintDriver:str = obj["PrintDriver"]
      """  Program which calls the print program  """  
      self.PrintProgram:str = obj["PrintProgram"]
      """  Program which performs the actual printing  """  
      self.PrinterName:str = obj["PrinterName"]
      """  Name of "client" printer, used for auto print  """  
      self.PrintProgramOptions:str = obj["PrintProgramOptions"]
      """  additonal options/settings required by specfic PrintProgram  """  
      self.RptPageSettings:str = obj["RptPageSettings"]
      """  Report Page Settings  """  
      self.RptPrinterSettings:str = obj["RptPrinterSettings"]
      """  Report Printer Settings  """  
      self.RptVersion:str = obj["RptVersion"]
      """  Report Version  """  
      self.RptOutPutType:str = obj["RptOutPutType"]
      """  Report Output Type  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  name of computer/workstation that made the request for this report.  """  
      self.RptNote:str = obj["RptNote"]
      """  An optional descriptive note about this Report.  This value comes from the report parameter TaskNote field.  """  
      self.Archived:bool = obj["Archived"]
      """  Indicates that this Report has been Archived.  """  
      self.PurgeDate:str = obj["PurgeDate"]
      """  Date that this Report will be purged.  """  
      self.TxtLPP:int = obj["TxtLPP"]
      """  Number of lines per page for the specific text report. This was obtained from the XBSyst.TxtLPP..  """  
      self.FaxSubject:str = obj["FaxSubject"]
      """  Fax Subject  """  
      self.FaxTo:str = obj["FaxTo"]
      """  Fax To  """  
      self.FaxNumber:str = obj["FaxNumber"]
      """  Fax Number  """  
      self.EMailTo:str = obj["EMailTo"]
      """  Email To Address  """  
      self.EMailCC:str = obj["EMailCC"]
      """  Email  to CC  """  
      self.EMailBCC:str = obj["EMailBCC"]
      """  Email To BCC  """  
      self.SSRSURL:str = obj["SSRSURL"]
      """  SSRS URL  """  
      self.OutputEDI:str = obj["OutputEDI"]
      """  Field to save if file is going to be exported in txt o xml format  """  
      self.EMailBody:str = obj["EMailBody"]
      """  Email Body text  """  
      self.AttachmentType:str = obj["AttachmentType"]
      """  Attachment Type  """  
      self.SSRSRenderFormat:str = obj["SSRSRenderFormat"]
      """  SSRSRenderFormat  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  StyleNum  """  
      self.UserDescription:str = obj["UserDescription"]
      """  UserDescription  """  
      self.DesignMode:str = obj["DesignMode"]
      """  DesignMode  """  
      self.DesignUser:str = obj["DesignUser"]
      """  DesignUser  """  
      self.DesignVersionLocalFolder:str = obj["DesignVersionLocalFolder"]
      """  DesignVersionLocalFolder  """  
      self.StyleDescription:str = obj["StyleDescription"]
      """  StyleDescription  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysTaskHistRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Task Description  """  
      self.TaskType:str = obj["TaskType"]
      """   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  """  
      self.StartedOn:str = obj["StartedOn"]
      """  Date-time field that the task Started On in UTC time zone  """  
      self.EndedOn:str = obj["EndedOn"]
      """  Date-time field that the task Ended On in UTC time zone  """  
      self.SubmitUser:str = obj["SubmitUser"]
      """  User who submitrted the task  """  
      self.TaskStatus:str = obj["TaskStatus"]
      """  Values are; Active, Complete, Cancelled, Error.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AgentID:str = obj["AgentID"]
      """  Task Agent ID  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  Task Agent Scheduling Number  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  Task Agent Task Number  """  
      self.RunProcedure:str = obj["RunProcedure"]
      """  Run Procedure  """  
      self.InitiatorSource:str = obj["InitiatorSource"]
      """  Values are "Agent" or "Client".  """  
      self.ActivityMsg:str = obj["ActivityMsg"]
      """  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  """  
      self.History:bool = obj["History"]
      """  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  """  
      self.TaskNote:str = obj["TaskNote"]
      """  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  """  
      self.LastActivityOn:str = obj["LastActivityOn"]
      """  LastActivityOn  """  
      self.UserPIDInfo:str = obj["UserPIDInfo"]
      """  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.IsSystemTask:bool = obj["IsSystemTask"]
      """  IsSystemTask  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProgressPercent:int = obj["ProgressPercent"]
      """  ProgressPercent  """  
      self.EdgeCorrelationID:str = obj["EdgeCorrelationID"]
      """  EdgeCorrelationID  """  
      self.ErrorMsg:str = obj["ErrorMsg"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysTaskLogRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.EntryNum:int = obj["EntryNum"]
      """  Entry Number  """  
      self.EnteredOn:str = obj["EnteredOn"]
      """  EnteredOn  """  
      self.IsError:bool = obj["IsError"]
      """  Error indicator  """  
      self.MsgText:str = obj["MsgText"]
      """  Message Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MsgType:str = obj["MsgType"]
      """  MsgType  """  
      self.MsgTypeDescription:str = obj["MsgTypeDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysTaskRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Task Description  """  
      self.TaskType:str = obj["TaskType"]
      """   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  """  
      self.StartedOn:str = obj["StartedOn"]
      """  Date-time field that the task Started On in UTC time zone  """  
      self.EndedOn:str = obj["EndedOn"]
      """  Date-time field that the task Ended On in UTC time zone  """  
      self.SubmitUser:str = obj["SubmitUser"]
      """  User who submitrted the task  """  
      self.TaskStatus:str = obj["TaskStatus"]
      """  Values are; Active, Complete, Cancelled, Error.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AgentID:str = obj["AgentID"]
      """  Task Agent ID  """  
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      """  Task Agent Scheduling Number  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  Task Agent Task Number  """  
      self.RunProcedure:str = obj["RunProcedure"]
      """  Run Procedure  """  
      self.InitiatorSource:str = obj["InitiatorSource"]
      """  Values are "Agent" or "Client".  """  
      self.ActivityMsg:str = obj["ActivityMsg"]
      """  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  """  
      self.History:bool = obj["History"]
      """  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  """  
      self.TaskNote:str = obj["TaskNote"]
      """  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  """  
      self.LastActivityOn:str = obj["LastActivityOn"]
      """  LastActivityOn  """  
      self.UserPIDInfo:str = obj["UserPIDInfo"]
      """  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Unique ID for Process  """  
      self.IsSystemTask:bool = obj["IsSystemTask"]
      """  IsSystemTask  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProgressPercent:int = obj["ProgressPercent"]
      """  ProgressPercent  """  
      self.EdgeCorrelationID:str = obj["EdgeCorrelationID"]
      """  EdgeCorrelationID  """  
      self.ErrorMsg:str = obj["ErrorMsg"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class UpdateSysMonitorDS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysMonitorTableset] = obj["ds"]
      pass

class UpdateSysMonitorDS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysMonitorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateSysMonitorSched_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysMonitorSchedTableset] = obj["ds"]
      pass

class UpdateSysMonitorSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysMonitorSchedTableset] = obj["ds"]
      pass

      """  output parameters  """  

