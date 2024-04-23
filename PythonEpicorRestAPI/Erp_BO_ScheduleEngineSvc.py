import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ScheduleEngineSvc
# Description: For scheduling jobs, assemblies and operations.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ReadExtSchedule(epicorHeaders = None):
   """  
   Summary: Invoke method ReadExtSchedule
   Description: Load ExtSchedule dataset from a XML file
   OperationID: ReadExtSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReadExtSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ProcessExtSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessExtSchedule
   Description: Process data from External Schedule system receiving Operation Dates in ExtSchedule dataset
   OperationID: ProcessExtSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessExtSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessExtSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AcceptChanges(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AcceptChanges
   Description: This method commits a job. Move Whatif to scheduled.
   OperationID: AcceptChanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AcceptChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AcceptChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeProductionComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeProductionComplete
   Description: This method does stuff.
   OperationID: ChangeProductionComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeProductionComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProductionComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeResource
   Description: This method will change
the resource on a resourcetimeused record.
   OperationID: ChangeResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSetupComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSetupComplete
   Description: This method does stuff.
   OperationID: ChangeSetupComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSetupComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSetupComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLoadLevelDflts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLoadLevelDflts
   Description: This method does stuff .
   OperationID: GetLoadLevelDflts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLoadLevelDflts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLoadLevelDflts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMultiSchedTypeCodes(epicorHeaders = None):
   """  
   Summary: Invoke method GetMultiSchedTypeCodes
   Description: Returns the list of Schedule Type Code and Descriptions needed to schedule in multi-job
MultiSchedTypeCodes is used when scheduling initially in Multi-Job
   OperationID: GetMultiSchedTypeCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMultiSchedTypeCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetSchedTypeCodes(epicorHeaders = None):
   """  
   Summary: Invoke method GetSchedTypeCodes
   Description: Returns the list of Schedule Type Code and Descriptions . Three lists are returned
SchedTypecodes is used when moving the entire job,
OperationOnlySchedTypecodes is used only for operations.
   OperationID: GetSchedTypeCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSchedTypeCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetScheduleRecord(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetScheduleRecord
   Description: This method allows the UI to retrieve a blank Schedule record.
   OperationID: GetScheduleRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetScheduleRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetScheduleRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadChildJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadChildJobs
   OperationID: LoadChildJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadChildJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadChildJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadParentJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadParentJobs
   OperationID: LoadParentJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadParentJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadParentJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadLeveling(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadLeveling
   Description: Load method.
   OperationID: LoadLeveling
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadLeveling_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadLeveling_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveJobItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveJobItem
   Description: Procedure to move an Operation Detail.
   OperationID: MoveJobItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveJobItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveJobItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewParamsForJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewParamsForJob
   Description: Get New Schedule Engine Parameters for a specific Job.
   OperationID: GetNewParamsForJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewParamsForJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewParamsForJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveSchedBoardItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveSchedBoardItem
   Description: Procedure to move an Operation Detail, used for moving a scheduling board
item, allows the movement of a locked job.
   OperationID: MoveSchedBoardItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveSchedBoardItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveSchedBoardItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveSchedule
   Description: This method does stuff .
   OperationID: SaveSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetMachines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetMachines
   Description: This method does stuff. Assign  JobOper.WIMachines from ScheduleEngine.Machines.
   OperationID: SetMachines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetMachines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetMachines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UndoChanges(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UndoChanges
   Description: This method commits a job. Move Whatif to scheduled .
   OperationID: UndoChanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UndoChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSchedulingMultiJobFlags(epicorHeaders = None):
   """  
   Summary: Invoke method GetSchedulingMultiJobFlags
   Description: Get the flags needed for multi job scheduling
   OperationID: GetSchedulingMultiJobFlags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSchedulingMultiJobFlags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetSchedulingFlags(epicorHeaders = None):
   """  
   Summary: Invoke method GetSchedulingFlags
   Description: Get the flags needed for scheduling
   OperationID: GetSchedulingFlags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSchedulingFlags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AcceptChanges_input:
   """ Required : 
   JobsMoved
   ds
   """  
   def __init__(self, obj):
      self.JobsMoved:str = obj["JobsMoved"]
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

class AcceptChanges_output:
   def __init__(self, obj):
      pass

class ChangeProductionComplete_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

class ChangeProductionComplete_output:
   def __init__(self, obj):
      pass

class ChangeResource_input:
   """ Required : 
   ds
   ipAllocNum
   ipResourceID
   ipBlocksChanged
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      self.ipAllocNum:int = obj["ipAllocNum"]
      self.ipResourceID:str = obj["ipResourceID"]
      """  The ResourceTimeUsed ResourceID  """  
      self.ipBlocksChanged:bool = obj["ipBlocksChanged"]
      """  Determines wether the number of scheduling blocks changed or not  """  
      pass

class ChangeResource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.WarnLogTxt:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeSetupComplete_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

class ChangeSetupComplete_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ExtScheduleRow:
   def __init__(self, obj):
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.Company:str = obj["Company"]
      self.DueDate:str = obj["DueDate"]
      self.DueHour:int = obj["DueHour"]
      self.JobNum:str = obj["JobNum"]
      self.MoveDueDate:str = obj["MoveDueDate"]
      self.MoveDueHour:int = obj["MoveDueHour"]
      self.OprSeq:int = obj["OprSeq"]
      self.QueStartDate:str = obj["QueStartDate"]
      self.QueStartHour:int = obj["QueStartHour"]
      self.StartDate:str = obj["StartDate"]
      self.StartHour:int = obj["StartHour"]
      self.StatusDesc:str = obj["StatusDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtScheduleTableset:
   def __init__(self, obj):
      self.ExtSchedule:list[Erp_Tablesets_ExtScheduleRow] = obj["ExtSchedule"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ScheduleEngineRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      self.StartDate:str = obj["StartDate"]
      self.StartTime:int = obj["StartTime"]
      self.EndDate:str = obj["EndDate"]
      self.EndTime:int = obj["EndTime"]
      self.WhatIf:bool = obj["WhatIf"]
      self.Finite:bool = obj["Finite"]
      self.SchedTypeCode:str = obj["SchedTypeCode"]
      self.ScheduleDirection:str = obj["ScheduleDirection"]
      """  expected values are 'Start' / 'End'  """  
      self.SetupComplete:bool = obj["SetupComplete"]
      self.ProductionComplete:bool = obj["ProductionComplete"]
      self.ScheduleID:str = obj["ScheduleID"]
      self.CommentText:str = obj["CommentText"]
      self.loadLevelBy:str = obj["loadLevelBy"]
      self.ConsiderPriority:bool = obj["ConsiderPriority"]
      self.LLStartDate:str = obj["LLStartDate"]
      self.LLNewStartDate:str = obj["LLNewStartDate"]
      self.OverrideMtlCon:bool = obj["OverrideMtlCon"]
      self.LLCutOffDate:str = obj["LLCutOffDate"]
      self.OverRideHistDateSetting:int = obj["OverRideHistDateSetting"]
      """   Used to override the JCSyst.AllowSchedulingBeforeToday.
Values: 0 - false, 1 - true and 2 - ignored  """  
      self.ResourceID:str = obj["ResourceID"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.AllocNum:int = obj["AllocNum"]
      self.Machines:int = obj["Machines"]
      self.RecalcExpProdYld:bool = obj["RecalcExpProdYld"]
      """  Flag to indicate whether the job expected production yield quantities should be recalculated for this jobs if ProductionYield = true and there are operations that have been flagged for recalculation.  """  
      self.UpdateJobOpDtl:bool = obj["UpdateJobOpDtl"]
      """  Indicates whether the selected (What-If) Resource should be written back to the Job Operation Detail record.   In the case where the user wants to select a specific resource but have global or job schedule select a new resource by availability when re-scheduling the job they would uncheck this box.  If the "Update Job Operation Detail" check box is true AND the number of scheduling blocks is 1 then write the new resource back to the Job Operation just like selecting the resource manually in job  """  
      self.JobNumList:str = obj["JobNumList"]
      """  it contains the list of Job numbers to save  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      self.UseSchedulingMultiJob:bool = obj["UseSchedulingMultiJob"]
      """  Default value for the this flag at every place where the scheduling UI is called to instruct to the scheduling engine looks for any assembly or material that has a direct job link and those linked jobs get rescheduled as well to be just in time to supply the main job.  """  
      self.SchedulingMultiJobIgnoreLocks:bool = obj["SchedulingMultiJobIgnoreLocks"]
      """  When Schedule Multi Job option is selected this option is used to have the ability to ignore locks for Jobs.  """  
      self.SchedulingMultiJobMinimizeWIP:bool = obj["SchedulingMultiJobMinimizeWIP"]
      """  Used to Minimize WIP between jobs  """  
      self.JobType:str = obj["JobType"]
      self.SchedulingMultiJobMoveJobsAcrossPlants:bool = obj["SchedulingMultiJobMoveJobsAcrossPlants"]
      """  Allows moving Jobs across plants within the company and not only for the plant where user is logged on.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ScheduleEngineTableset:
   def __init__(self, obj):
      self.ScheduleEngine:list[Erp_Tablesets_ScheduleEngineRow] = obj["ScheduleEngine"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetLoadLevelDflts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

class GetLoadLevelDflts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetMultiSchedTypeCodes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.MultiSchedTypeCodes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewParamsForJob_input:
   """ Required : 
   jobNum
   kitTime
   ignoreMtlConstraints
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  Job Number  """  
      self.kitTime:int = obj["kitTime"]
      """  Kit Time defined on Job  """  
      self.ignoreMtlConstraints:bool = obj["ignoreMtlConstraints"]
      """  Ignore Material Constraints defined on Job  """  
      pass

class GetNewParamsForJob_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ScheduleEngineTableset] = obj["returnObj"]
      pass

class GetSchedTypeCodes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.SchedTypecodes:str = obj["parameters"]
      self.OperationOnlySchedTypecodes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetScheduleRecord_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

class GetScheduleRecord_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSchedulingFlags_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.schedulingMultiJobActive:bool = obj["schedulingMultiJobActive"]
      self.minimizeWIPFlag:bool = obj["minimizeWIPFlag"]
      self.allowMoveJobsAcrossPlants:bool = obj["allowMoveJobsAcrossPlants"]
      self.autoLoadParentJobs:bool = obj["autoLoadParentJobs"]
      self.autoLoadChildJobs:bool = obj["autoLoadChildJobs"]
      self.BWSchedStartTime:int = obj["parameters"]
      self.schedulingDirection:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSchedulingMultiJobFlags_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.schedulingMultiJobActive:bool = obj["schedulingMultiJobActive"]
      self.minimizeWIPFlag:bool = obj["minimizeWIPFlag"]
      self.allowMoveJobsAcrossPlants:bool = obj["allowMoveJobsAcrossPlants"]
      self.autoLoadParentJobs:bool = obj["autoLoadParentJobs"]
      self.autoLoadChildJobs:bool = obj["autoLoadChildJobs"]
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

class LoadChildJobs_input:
   """ Required : 
   jobNum
   company
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.company:str = obj["company"]
      pass

class LoadChildJobs_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class LoadLeveling_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

class LoadLeveling_output:
   def __init__(self, obj):
      pass

class LoadParentJobs_input:
   """ Required : 
   jobNum
   company
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.company:str = obj["company"]
      pass

class LoadParentJobs_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class MoveJobItem_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

class MoveJobItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.l_finished:bool = obj["l_finished"]
      self.c_WarnLogTxt:str = obj["parameters"]
      pass

      """  output parameters  """  

class MoveSchedBoardItem_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

class MoveSchedBoardItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.l_finished:bool = obj["l_finished"]
      self.c_WarnLogTxt:str = obj["parameters"]
      pass

      """  output parameters  """  

class ProcessExtSchedule_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtScheduleTableset] = obj["ds"]
      pass

class ProcessExtSchedule_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtScheduleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ReadExtSchedule_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtScheduleTableset] = obj["returnObj"]
      pass

class SaveSchedule_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

class SaveSchedule_output:
   def __init__(self, obj):
      pass

class SetMachines_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

class SetMachines_output:
   def __init__(self, obj):
      pass

class UndoChanges_input:
   """ Required : 
   JobsMoved
   ds
   """  
   def __init__(self, obj):
      self.JobsMoved:str = obj["JobsMoved"]
      self.ds:list[Erp_Tablesets_ScheduleEngineTableset] = obj["ds"]
      pass

class UndoChanges_output:
   def __init__(self, obj):
      pass

