import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SchedulingBoardSvc
# Description: Provide data for the scheduling boards.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_BuildJobLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildJobLine
   Description: This methods will return all of the JobLine Header type records.  This will
be a JobLine record that would represent the JobHead and JobAsmbl.AssemblySeq = 0
information.  To retrieve the details run the ExpandJobLine publice method.
If ipJobNum and ipProjectID are both blank or unknown you will get all jobs for the current plant,
or if ipJobNum is not blank then just that job, or if ipjobnum is blank and
ipProjectID is not, then all jobs associated with that projectid.
   OperationID: BuildJobLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildJobLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildJobLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildResourceLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildResourceLine
   Description: This methods will return all of the Resource Header type records.  This will
be a SchedulingBoard record that would represent the ResourceTimeUsed and it's assoc
information.
   OperationID: BuildResourceLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildResourceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildResourceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateComment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateComment
   OperationID: UpdateComment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSchedulingRec(epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSchedulingRec
   Description: This methods will create new record of the SchedulingBoard.
   OperationID: GetNewSchedulingRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSchedulingRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_Restore(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Restore
   Description: This method will restore the schedule based on the schedule id and return
and potential errors or warings with the restore in the SchedRestoreLog table.
   OperationID: Restore
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Restore_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Restore_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReturnCalendarID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReturnCalendarID
   Description: This methods will return the calendar id information along with whether or not
this calendar information can be used.
   OperationID: ReturnCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReturnCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReturnCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetLockSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetLockSched
   Description: This method locks/unlocks the schedule of a specific jobnum.
   OperationID: SetLockSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetLockSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetLockSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAccess(epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAccess
   Description: Validate if the Use3rdPartySched is checked send a message that access is not allowed.
   OperationID: ValidateAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BuildJobLine_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SchedulingBoardTableset] = obj["ds"]
      pass

class BuildJobLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SchedulingBoardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BuildResourceLine_input:
   """ Required : 
   ipResourceGrpID
   ipResourceID
   ipJobNum
   StartDate
   EndDate
   """  
   def __init__(self, obj):
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  The resource group id to schedule for.  """  
      self.ipResourceID:str = obj["ipResourceID"]
      """  The resource id or a list of resource id to schedule for  """  
      self.ipJobNum:str = obj["ipJobNum"]
      """  The job number to schedule for.  """  
      self.StartDate:str = obj["StartDate"]
      """  The StartDate to schedule for.  """  
      self.EndDate:str = obj["EndDate"]
      """  The EndDate to schedule for.  """  
      pass

class BuildResourceLine_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SchedulingBoardTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_SchedRestoreLogRow:
   def __init__(self, obj):
      self.JobNum:str = obj["JobNum"]
      """  The job number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The assembly sequence.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The operation sequence.  """  
      self.ErrorDesc:str = obj["ErrorDesc"]
      """  The description of the error or warning.  """  
      self.ErrorType:str = obj["ErrorType"]
      """  The type, either E for Error or W for Warning.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SchedulingBoardJobMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.PartNum:str = obj["PartNum"]
      self.Description:str = obj["Description"]
      self.QtyPer:int = obj["QtyPer"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.JobComplete:bool = obj["JobComplete"]
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.Plant:str = obj["Plant"]
      self.UnitPrice:int = obj["UnitPrice"]
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.BuyIt:bool = obj["BuyIt"]
      self.Direct:bool = obj["Direct"]
      self.RelatedOperation:int = obj["RelatedOperation"]
      self.IssuedQty:int = obj["IssuedQty"]
      self.LeadTime:int = obj["LeadTime"]
      """   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.  
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  """  
      self.Constrained:bool = obj["Constrained"]
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.DynAttrValueSetShortDesc:str = obj["DynAttrValueSetShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SchedulingBoardRow:
   def __init__(self, obj):
      self.BuildNum:int = obj["BuildNum"]
      self.RowNum:int = obj["RowNum"]
      self.JobNum:str = obj["JobNum"]
      self.AsmNum:int = obj["AsmNum"]
      self.OprNum:int = obj["OprNum"]
      self.OpDtlNum:int = obj["OpDtlNum"]
      self.JobPartNum:str = obj["JobPartNum"]
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.OprPartNum:str = obj["OprPartNum"]
      self.OpCode:str = obj["OpCode"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceID:str = obj["ResourceID"]
      self.CapabilityID:str = obj["CapabilityID"]
      self.BOMSequence:int = obj["BOMSequence"]
      self.BOMLevel:int = obj["BOMLevel"]
      self.JobPartDesc:str = obj["JobPartDesc"]
      self.AsmPartDesc:str = obj["AsmPartDesc"]
      self.OprPartDesc:str = obj["OprPartDesc"]
      self.AsmRevisionNum:str = obj["AsmRevisionNum"]
      self.WIMode:str = obj["WIMode"]
      self.WIStatus:str = obj["WIStatus"]
      self.WIName:str = obj["WIName"]
      self.NumMachines:int = obj["NumMachines"]
      self.TotalEstHours:int = obj["TotalEstHours"]
      self.TotalActHours:int = obj["TotalActHours"]
      self.RemainHours:int = obj["RemainHours"]
      self.PrctCmplt:int = obj["PrctCmplt"]
      self.RemainPerMachHours:int = obj["RemainPerMachHours"]
      self.OSDate:str = obj["OSDate"]
      """  The operation start date.  """  
      self.OSHour:int = obj["OSHour"]
      """  The operation start hour.  """  
      self.ODDate:str = obj["ODDate"]
      """  The operation due date.  """  
      self.ODHour:int = obj["ODHour"]
      """  The operation due hour.  """  
      self.QSDate:str = obj["QSDate"]
      """  The queue start date.  """  
      self.QSHour:int = obj["QSHour"]
      """  The queue start hour.  """  
      self.QDayDur:int = obj["QDayDur"]
      """  The queue days duration.  """  
      self.CSDate:str = obj["CSDate"]
      """  The completed start date.  """  
      self.CSHour:int = obj["CSHour"]
      """  The completed start hour.  """  
      self.CDayDur:int = obj["CDayDur"]
      """  The completed days duration  """  
      self.WISDate:str = obj["WISDate"]
      self.WISHour:int = obj["WISHour"]
      """  The what if start hours.  """  
      self.WIDDate:str = obj["WIDDate"]
      """  The what if due date.  """  
      self.WIDHour:int = obj["WIDHour"]
      """  The what if due hour.  """  
      self.MDDate:str = obj["MDDate"]
      """  The move due date.  """  
      self.MDHour:int = obj["MDHour"]
      """  The move due hour.  """  
      self.MDayDur:int = obj["MDayDur"]
      """  The move days duration.  """  
      self.OnCritPath:bool = obj["OnCritPath"]
      """  On the critical path?  """  
      self.OprSubcontract:bool = obj["OprSubcontract"]
      """  Is operation a subcontract?  """  
      self.Parent:int = obj["Parent"]
      self.PriorPeer:int = obj["PriorPeer"]
      self.NextPeer:int = obj["NextPeer"]
      self.LastOper:bool = obj["LastOper"]
      """  The last operation of the parent assembly.  """  
      self.Company:str = obj["Company"]
      self.HasOper:bool = obj["HasOper"]
      """  Indicates that the assembly has operations.  Always true for operations.  """  
      self.ShowChildrenFlag:bool = obj["ShowChildrenFlag"]
      """  Indicates that the asm should show children.  """  
      self.OnScreenFlag:bool = obj["OnScreenFlag"]
      """  Indicates that the record should be shown.  """  
      self.JobStatus:str = obj["JobStatus"]
      """  On Asm = 0 this set to 'E' for Engineered, 'R' for Released.  """  
      self.JobLateStatus:str = obj["JobLateStatus"]
      self.EstDurHours:int = obj["EstDurHours"]
      """  The estimated duration hours.  """  
      self.Lateness:int = obj["Lateness"]
      self.BuildAsms:bool = obj["BuildAsms"]
      self.OperationStarted:bool = obj["OperationStarted"]
      """  Has the operation started?  """  
      self.Plant:str = obj["Plant"]
      self.SetupGroup:str = obj["SetupGroup"]
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      self.SchedResourceGrpID:str = obj["SchedResourceGrpID"]
      self.SchedResourceID:str = obj["SchedResourceID"]
      self.WISchedResourceGrpID:str = obj["WISchedResourceGrpID"]
      self.WISchedResourceID:str = obj["WISchedResourceID"]
      self.ConstraintNoMtl:bool = obj["ConstraintNoMtl"]
      self.ConstraintNoPO:bool = obj["ConstraintNoPO"]
      self.ConstraintCapacity:bool = obj["ConstraintCapacity"]
      self.OpComplete:bool = obj["OpComplete"]
      self.SchedLocked:bool = obj["SchedLocked"]
      self.ResourceIDDesc:str = obj["ResourceIDDesc"]
      self.ResourceGrpIDDesc:str = obj["ResourceGrpIDDesc"]
      self.CapabilityIDDesc:str = obj["CapabilityIDDesc"]
      self.SortStartDate:str = obj["SortStartDate"]
      """  Sort by Start Date.  """  
      self.SortJob:str = obj["SortJob"]
      """  Sort by Job.  """  
      self.SortPart:str = obj["SortPart"]
      """  Sort by Part.  """  
      self.SortCustID:str = obj["SortCustID"]
      """  Sort by Cust ID.  """  
      self.SortDueDate:str = obj["SortDueDate"]
      """  Sort by Due Date.  """  
      self.SortDaysLate:str = obj["SortDaysLate"]
      """  Sort by Days Late.  """  
      self.SortSetupGroup:str = obj["SortSetupGroup"]
      """  Sort by Setup Group  """  
      self.SortOpCode:str = obj["SortOpCode"]
      """  Sort by OpCode.  """  
      self.CalcCustID:str = obj["CalcCustID"]
      """  The calculated custid.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  The job production quantity.  """  
      self.JobHeadQtyCompleted:int = obj["JobHeadQtyCompleted"]
      """  The jobhead quantity completed.  """  
      self.JobType:str = obj["JobType"]
      """  The job type.  """  
      self.JobOperQtyCompleted:int = obj["JobOperQtyCompleted"]
      """  The joboper quantity completed  """  
      self.RunQty:int = obj["RunQty"]
      """  The run quantity from the joboper table.  """  
      self.StartDate:str = obj["StartDate"]
      """  The jobhead start date.  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  The jobhead required due date.  """  
      self.JobRevisionNum:str = obj["JobRevisionNum"]
      """  The revision number for the part on the jobhead record.  """  
      self.JobLocked:bool = obj["JobLocked"]
      """  Is the job locked because winame is not equal the dcduserid?  """  
      self.AllocNum:int = obj["AllocNum"]
      """  The allocation number from the resourcetimeused table for resource boards.  Will be zero for job boards.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  The operation description  """  
      self.Batch:bool = obj["Batch"]
      """  Is this a batch operation?  """  
      self.OprStartTime:str = obj["OprStartTime"]
      """  Operation start time.  """  
      self.OprEndTime:str = obj["OprEndTime"]
      """  Operation end time.  """  
      self.OperRowIdent:str = obj["OperRowIdent"]
      """  The parent operation rowid  """  
      self.SetupGrpDescription:str = obj["SetupGrpDescription"]
      self.PartPlantNonStock:bool = obj["PartPlantNonStock"]
      self.PartPlantMaxMfgLotSize:int = obj["PartPlantMaxMfgLotSize"]
      self.DaysLate:int = obj["DaysLate"]
      """  The number of days late.  """  
      self.Machines:int = obj["Machines"]
      self.ProductionComplete:bool = obj["ProductionComplete"]
      self.SetupComplete:bool = obj["SetupComplete"]
      self.SchedComment:str = obj["SchedComment"]
      self.WISchedResourceIDDesc:str = obj["WISchedResourceIDDesc"]
      """  What-If Resource Description.  """  
      self.SchedResourceIDDesc:str = obj["SchedResourceIDDesc"]
      """  Current Resource Description.  """  
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      """  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  """  
      self.ResourceTotalEstHours:int = obj["ResourceTotalEstHours"]
      self.ProductionYield:bool = obj["ProductionYield"]
      self.AsmAttrClassID:str = obj["AsmAttrClassID"]
      """  ID of related Attribute Class  """  
      self.AsmAttrDesc:str = obj["AsmAttrDesc"]
      """  Description of values in set  """  
      self.AsmAttributeSetID:int = obj["AsmAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AsmShortDesc:str = obj["AsmShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.JobAttrClassID:str = obj["JobAttrClassID"]
      """  ID of related Attribute Class  """  
      self.JobAttrDesc:str = obj["JobAttrDesc"]
      """  Description of values in set  """  
      self.JobAttributeSetID:int = obj["JobAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.JobShortDesc:str = obj["JobShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.OprAttrClassID:str = obj["OprAttrClassID"]
      """  ID of related Attribute Class  """  
      self.OprAttrDesc:str = obj["OprAttrDesc"]
      """  Description of values in set  """  
      self.OprAttributeSetID:int = obj["OprAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.OprShortDesc:str = obj["OprShortDesc"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.OprRevisionNum:str = obj["OprRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SchedulingBoardTableset:
   def __init__(self, obj):
      self.SchedulingBoard:list[Erp_Tablesets_SchedulingBoardRow] = obj["SchedulingBoard"]
      self.SchedRestoreLog:list[Erp_Tablesets_SchedRestoreLogRow] = obj["SchedRestoreLog"]
      self.SchedulingBoardJobMtl:list[Erp_Tablesets_SchedulingBoardJobMtlRow] = obj["SchedulingBoardJobMtl"]
      self.SchedulingJob:list[Erp_Tablesets_SchedulingJobRow] = obj["SchedulingJob"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SchedulingJobRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.ProjectID:str = obj["ProjectID"]
      self.Plant:str = obj["Plant"]
      self.ExpandJob:bool = obj["ExpandJob"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetNewSchedulingRec_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SchedulingBoardTableset] = obj["returnObj"]
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

class Restore_input:
   """ Required : 
   ipScheduleID
   """  
   def __init__(self, obj):
      self.ipScheduleID:int = obj["ipScheduleID"]
      """  The Schedule ID  """  
      pass

class Restore_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SchedulingBoardTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opJobList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReturnCalendarID_input:
   """ Required : 
   ipResourceGrpID
   ipResourceID
   """  
   def __init__(self, obj):
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  The resource group id locate calendar for.  """  
      self.ipResourceID:str = obj["ipResourceID"]
      """  The resource id or a list of resource id locate calendar for.  """  
      pass

class ReturnCalendarID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCalendarID:str = obj["parameters"]
      self.opValidCalendar:bool = obj["opValidCalendar"]
      pass

      """  output parameters  """  

class SetLockSched_input:
   """ Required : 
   inLockedStatus
   ds
   """  
   def __init__(self, obj):
      self.inLockedStatus:bool = obj["inLockedStatus"]
      """  The locked status of the schedule.  """  
      self.ds:list[Erp_Tablesets_SchedulingBoardTableset] = obj["ds"]
      pass

class SetLockSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SchedulingBoardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateComment_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SchedulingBoardTableset] = obj["ds"]
      pass

class UpdateComment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SchedulingBoardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateAccess_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  bool: access is allowed or not  """  
      pass

