import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.OverrideSchedOrdersSvc
# Description: OverrideSchedOrdersSvc Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_DeleteRec(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRec
   Description: Delete current record and reset values (Job Number - number or list
   OperationID: DeleteRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadOverrideSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadOverrideSched
   Description: /// Populates ttOverrideSchedOrders table from JobHead, PatchFld
///
   OperationID: LoadOverrideSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadOverrideSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadOverrideSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MultiJobUpdateSchedPri(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MultiJobUpdateSchedPri
   Description: Update default information based on the warehouse changing
   OperationID: MultiJobUpdateSchedPri
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MultiJobUpdateSchedPri_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MultiJobUpdateSchedPri_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateSchedPri(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSchedPri
   Description: Update default information based on the warehouse changing
   OperationID: UpdateSchedPri
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSchedPri_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSchedPri_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCalculateGlobalSchedulingLastRun(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCalculateGlobalSchedulingLastRun
   Description: Get multi job Flag used in the Last Run of the Scheduling
   OperationID: GetCalculateGlobalSchedulingLastRun
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCalculateGlobalSchedulingLastRun_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCalculateGlobalSchedulingLastRun_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBackwards(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBackwards
   Description: Column Changed for Backwards
   OperationID: OnChangeBackwards
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBackwards_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBackwards_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMultiJobSchedSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMultiJobSchedSeq
   Description: Column Changed for MultiJobSchedSeq
   OperationID: OnChangeMultiJobSchedSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMultiJobSchedSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMultiJobSchedSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSchedSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSchedSeq
   Description: On changing of MultiJobSchedSeq
   OperationID: OnChangingSchedSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSchedSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSchedSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadOverrideSchedOrderView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadOverrideSchedOrderView
   Description: Add rows from the JobHead dataset to the OverrideSchedOrders dataset.
   OperationID: LoadOverrideSchedOrderView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadOverrideSchedOrderView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadOverrideSchedOrderView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadOverrideSchedOrderViewList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadOverrideSchedOrderViewList
   OperationID: LoadOverrideSchedOrderViewList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadOverrideSchedOrderViewList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadOverrideSchedOrderViewList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshOverrideSchedOrderView(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshOverrideSchedOrderView
   Description: Custom Refresh of jobs
   OperationID: RefreshOverrideSchedOrderView
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshOverrideSchedOrderView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshOverrideSchedOrderView_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SeqIsDecimal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SeqIsDecimal
   Description: determine if multiJobSchedSeq is a decimal
   OperationID: SeqIsDecimal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SeqIsDecimal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SeqIsDecimal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class DeleteRec_input:
   """ Required : 
   ipJobNum
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job Number  """  
      pass

class DeleteRec_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JobAsmRefDesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.RefDes:str = obj["RefDes"]
      self.RefDesSeq:int = obj["RefDesSeq"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      self.Side:str = obj["Side"]
      self.XLocation:int = obj["XLocation"]
      self.YLocation:int = obj["YLocation"]
      self.ZLocation:int = obj["ZLocation"]
      self.Rotation:int = obj["Rotation"]
      self.Description:str = obj["Description"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobAsmblAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobAsmblInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.PlanSeq:int = obj["PlanSeq"]
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      self.SpecID:str = obj["SpecID"]
      self.SpecRevNum:str = obj["SpecRevNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobAsmblRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      self.SubstanceID:str = obj["SubstanceID"]
      self.Weight:int = obj["Weight"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.Manual:bool = obj["Manual"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.PartNum:str = obj["PartNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobAsmblRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      self.PartNum:str = obj["PartNum"]
      self.Manual:bool = obj["Manual"]
      self.RollupType:str = obj["RollupType"]
      self.Compliance:str = obj["Compliance"]
      self.ComplianceDate:str = obj["ComplianceDate"]
      self.LastRollUp:str = obj["LastRollUp"]
      self.BuiltCompliance:str = obj["BuiltCompliance"]
      self.BuiltComplianceDate:str = obj["BuiltComplianceDate"]
      self.BuiltLastRollUp:str = obj["BuiltLastRollUp"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.Weight:bool = obj["Weight"]
      self.EnableRollUpType:bool = obj["EnableRollUpType"]
      self.BitFlag:int = obj["BitFlag"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobComplete:bool = obj["JobComplete"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.PartNum:str = obj["PartNum"]
      self.Description:str = obj["Description"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.QtyPer:int = obj["QtyPer"]
      self.IUM:str = obj["IUM"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.PullQty:int = obj["PullQty"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.MtlBurRate:int = obj["MtlBurRate"]
      self.EstUnitCost:int = obj["EstUnitCost"]
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      self.OverRunQty:int = obj["OverRunQty"]
      self.StartDate:str = obj["StartDate"]
      self.StartHour:int = obj["StartHour"]
      self.DueDate:str = obj["DueDate"]
      self.DueHour:int = obj["DueHour"]
      self.Parent:int = obj["Parent"]
      self.PriorPeer:int = obj["PriorPeer"]
      self.NextPeer:int = obj["NextPeer"]
      self.Child:int = obj["Child"]
      self.TotalCost:int = obj["TotalCost"]
      self.MtlBurCost:int = obj["MtlBurCost"]
      self.IssuedQty:int = obj["IssuedQty"]
      self.DrawNum:str = obj["DrawNum"]
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.CommentText:str = obj["CommentText"]
      self.InCopyList:bool = obj["InCopyList"]
      self.BomSequence:int = obj["BomSequence"]
      self.BomLevel:int = obj["BomLevel"]
      self.WIStartDate:str = obj["WIStartDate"]
      self.WIStartHour:int = obj["WIStartHour"]
      self.WIDueDate:str = obj["WIDueDate"]
      self.WIDueHour:int = obj["WIDueHour"]
      self.TLALaborCost:int = obj["TLALaborCost"]
      self.TLABurdenCost:int = obj["TLABurdenCost"]
      self.TLAMaterialCost:int = obj["TLAMaterialCost"]
      self.TLASubcontractCost:int = obj["TLASubcontractCost"]
      self.TLAMtlBurCost:int = obj["TLAMtlBurCost"]
      self.TLASetupHours:int = obj["TLASetupHours"]
      self.TLAProdHours:int = obj["TLAProdHours"]
      self.TLELaborCost:int = obj["TLELaborCost"]
      self.TLEBurdenCost:int = obj["TLEBurdenCost"]
      self.TLEMaterialCost:int = obj["TLEMaterialCost"]
      self.TLESubcontractCost:int = obj["TLESubcontractCost"]
      self.TLEMtlBurCost:int = obj["TLEMtlBurCost"]
      self.TLESetupHours:int = obj["TLESetupHours"]
      self.TLEProdHours:int = obj["TLEProdHours"]
      self.LLALaborCost:int = obj["LLALaborCost"]
      self.LLABurdenCost:int = obj["LLABurdenCost"]
      self.LLAMaterialCost:int = obj["LLAMaterialCost"]
      self.LLASubcontractCost:int = obj["LLASubcontractCost"]
      self.LLAMtlBurCost:int = obj["LLAMtlBurCost"]
      self.LLASetupHours:int = obj["LLASetupHours"]
      self.LLAProdHours:int = obj["LLAProdHours"]
      self.LLELaborCost:int = obj["LLELaborCost"]
      self.LLEBurdenCost:int = obj["LLEBurdenCost"]
      self.LLEMaterialCost:int = obj["LLEMaterialCost"]
      self.LLESubcontractCost:int = obj["LLESubcontractCost"]
      self.LLEMtlBurCost:int = obj["LLEMtlBurCost"]
      self.LLESetupHours:int = obj["LLESetupHours"]
      self.LLEProdHours:int = obj["LLEProdHours"]
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      self.FinalOpr:int = obj["FinalOpr"]
      self.FindNum:str = obj["FindNum"]
      self.ReceivedToStock:int = obj["ReceivedToStock"]
      self.Plant:str = obj["Plant"]
      self.Direct:bool = obj["Direct"]
      self.RelatedOperation:int = obj["RelatedOperation"]
      self.TLAMaterialLabCost:int = obj["TLAMaterialLabCost"]
      self.TLAMaterialMtlCost:int = obj["TLAMaterialMtlCost"]
      self.TLAMaterialSubCost:int = obj["TLAMaterialSubCost"]
      self.TLAMaterialBurCost:int = obj["TLAMaterialBurCost"]
      self.LLAMaterialLabCost:int = obj["LLAMaterialLabCost"]
      self.LLAMaterialMtlCost:int = obj["LLAMaterialMtlCost"]
      self.LLAMaterialSubCost:int = obj["LLAMaterialSubCost"]
      self.LLAMaterialBurCost:int = obj["LLAMaterialBurCost"]
      self.TotalMtlMtlCost:int = obj["TotalMtlMtlCost"]
      self.TotalMtlLabCost:int = obj["TotalMtlLabCost"]
      self.TotalMtlSubCost:int = obj["TotalMtlSubCost"]
      self.TotalMtlBurCost:int = obj["TotalMtlBurCost"]
      self.CallNum:int = obj["CallNum"]
      self.CallLine:int = obj["CallLine"]
      self.RestoreFlag:str = obj["RestoreFlag"]
      self.AnalysisCode:str = obj["AnalysisCode"]
      self.LastConfigDate:str = obj["LastConfigDate"]
      self.LastConfigTime:int = obj["LastConfigTime"]
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      self.OrigRequiredQty:int = obj["OrigRequiredQty"]
      self.UserMapData:str = obj["UserMapData"]
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      self.TLAMaterialMtlBurCost:int = obj["TLAMaterialMtlBurCost"]
      self.LLAMaterialMtlBurCost:int = obj["LLAMaterialMtlBurCost"]
      self.TLAMfgCompLabCost:int = obj["TLAMfgCompLabCost"]
      self.TLAMfgCompMtlCost:int = obj["TLAMfgCompMtlCost"]
      self.TLAMfgCompSubCost:int = obj["TLAMfgCompSubCost"]
      self.TLAMfgCompBurCost:int = obj["TLAMfgCompBurCost"]
      self.TLAMfgCompMtlBurCost:int = obj["TLAMfgCompMtlBurCost"]
      self.LLAMfgCompLabCost:int = obj["LLAMfgCompLabCost"]
      self.LLAMfgCompMtlCost:int = obj["LLAMfgCompMtlCost"]
      self.LLAMfgCompSubCost:int = obj["LLAMfgCompSubCost"]
      self.LLAMfgCompBurCost:int = obj["LLAMfgCompBurCost"]
      self.LLAMfgCompMtlBurCost:int = obj["LLAMfgCompMtlBurCost"]
      self.Weight:int = obj["Weight"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      self.ValRefDes:bool = obj["ValRefDes"]
      self.BasePartNum:str = obj["BasePartNum"]
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      self.PlanAsAsm:bool = obj["PlanAsAsm"]
      self.PAARef:str = obj["PAARef"]
      self.PAAFirm:bool = obj["PAAFirm"]
      self.EstScrap:int = obj["EstScrap"]
      self.EstScrapType:str = obj["EstScrapType"]
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      self.SmartString:str = obj["SmartString"]
      self.ReqRefDes:int = obj["ReqRefDes"]
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      self.TLAODCCost:int = obj["TLAODCCost"]
      self.AssemblyMatch:str = obj["AssemblyMatch"]
      self.JdfStatus:str = obj["JdfStatus"]
      self.PressDevice:str = obj["PressDevice"]
      self.DigitalFileName:str = obj["DigitalFileName"]
      self.PrepressJobName:str = obj["PrepressJobName"]
      self.JdfPrepressAction:str = obj["JdfPrepressAction"]
      self.SendToPress:bool = obj["SendToPress"]
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      self.SendToPressInitiator:int = obj["SendToPressInitiator"]
      self.OperationType:int = obj["OperationType"]
      self.SendToPrePress:bool = obj["SendToPrePress"]
      self.GroupSeq:int = obj["GroupSeq"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.PartPlanInfo:str = obj["PartPlanInfo"]
      self.OrigStructTag:str = obj["OrigStructTag"]
      self.ContractID:str = obj["ContractID"]
      self.LinkToContract:bool = obj["LinkToContract"]
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      self.AvailableQty:int = obj["AvailableQty"]
      self.bUseAvailQty:bool = obj["bUseAvailQty"]
      self.ChildAssemblySeq:int = obj["ChildAssemblySeq"]
      self.DispIUM:str = obj["DispIUM"]
      self.DisplayOrder:int = obj["DisplayOrder"]
      self.EnableAsmSplitCosts:bool = obj["EnableAsmSplitCosts"]
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      self.FirmProcess:bool = obj["FirmProcess"]
      self.GetCostsFromInventory:bool = obj["GetCostsFromInventory"]
      self.GetCostsFromTemplate:bool = obj["GetCostsFromTemplate"]
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      self.ParentDescription:str = obj["ParentDescription"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      self.ParentRev:str = obj["ParentRev"]
      self.PartExists:bool = obj["PartExists"]
      self.PartmasterPart:bool = obj["PartmasterPart"]
      self.RDEndNum:int = obj["RDEndNum"]
      self.RDPrefix:str = obj["RDPrefix"]
      self.RDStartNum:int = obj["RDStartNum"]
      self.RDSuffix:str = obj["RDSuffix"]
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      self.ShowWarningBOMResequence:bool = obj["ShowWarningBOMResequence"]
      self.AddAsmAs:str = obj["AddAsmAs"]
      self.bAvailQty:int = obj["bAvailQty"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.AttrClassID:str = obj["AttrClassID"]
      self.TLATotalCost:int = obj["TLATotalCost"]
      self.TLETotalCost:int = obj["TLETotalCost"]
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PlantName:str = obj["PlantName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobAuditRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.ChangeDate:str = obj["ChangeDate"]
      self.ChangeTime:int = obj["ChangeTime"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.ChangeDescription:str = obj["ChangeDescription"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.BitFlag:int = obj["BitFlag"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobEntryTableset:
   def __init__(self, obj):
      self.JobHead:list[Erp_Tablesets_JobHeadRow] = obj["JobHead"]
      self.JobHeadAttch:list[Erp_Tablesets_JobHeadAttchRow] = obj["JobHeadAttch"]
      self.JobAsmbl:list[Erp_Tablesets_JobAsmblRow] = obj["JobAsmbl"]
      self.JobAsmblAttch:list[Erp_Tablesets_JobAsmblAttchRow] = obj["JobAsmblAttch"]
      self.JobAsmblInsp:list[Erp_Tablesets_JobAsmblInspRow] = obj["JobAsmblInsp"]
      self.JobMtl:list[Erp_Tablesets_JobMtlRow] = obj["JobMtl"]
      self.JobMtlAttch:list[Erp_Tablesets_JobMtlAttchRow] = obj["JobMtlAttch"]
      self.JobMtlInsp:list[Erp_Tablesets_JobMtlInspRow] = obj["JobMtlInsp"]
      self.JobMtlRefDes:list[Erp_Tablesets_JobMtlRefDesRow] = obj["JobMtlRefDes"]
      self.JobMtlRestriction:list[Erp_Tablesets_JobMtlRestrictionRow] = obj["JobMtlRestriction"]
      self.JobMtlRestrictSubst:list[Erp_Tablesets_JobMtlRestrictSubstRow] = obj["JobMtlRestrictSubst"]
      self.JobOper:list[Erp_Tablesets_JobOperRow] = obj["JobOper"]
      self.JobOperAttch:list[Erp_Tablesets_JobOperAttchRow] = obj["JobOperAttch"]
      self.JobOperAction:list[Erp_Tablesets_JobOperActionRow] = obj["JobOperAction"]
      self.JobOperActionParam:list[Erp_Tablesets_JobOperActionParamRow] = obj["JobOperActionParam"]
      self.JobOperInsp:list[Erp_Tablesets_JobOperInspRow] = obj["JobOperInsp"]
      self.JobOperMachParam:list[Erp_Tablesets_JobOperMachParamRow] = obj["JobOperMachParam"]
      self.JobOpDtl:list[Erp_Tablesets_JobOpDtlRow] = obj["JobOpDtl"]
      self.JobResources:list[Erp_Tablesets_JobResourcesRow] = obj["JobResources"]
      self.JobOperRestriction:list[Erp_Tablesets_JobOperRestrictionRow] = obj["JobOperRestriction"]
      self.JobOperRestrictSubst:list[Erp_Tablesets_JobOperRestrictSubstRow] = obj["JobOperRestrictSubst"]
      self.JobAsmblRestriction:list[Erp_Tablesets_JobAsmblRestrictionRow] = obj["JobAsmblRestriction"]
      self.JobAsmblRestrictSubst:list[Erp_Tablesets_JobAsmblRestrictSubstRow] = obj["JobAsmblRestrictSubst"]
      self.JobAsmRefDes:list[Erp_Tablesets_JobAsmRefDesRow] = obj["JobAsmRefDes"]
      self.JobAudit:list[Erp_Tablesets_JobAuditRow] = obj["JobAudit"]
      self.JobPart:list[Erp_Tablesets_JobPartRow] = obj["JobPart"]
      self.JobProd:list[Erp_Tablesets_JobProdRow] = obj["JobProd"]
      self.JobStage:list[Erp_Tablesets_JobStageRow] = obj["JobStage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobClosed:bool = obj["JobClosed"]
      self.ClosedDate:str = obj["ClosedDate"]
      self.JobComplete:bool = obj["JobComplete"]
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      self.JobEngineered:bool = obj["JobEngineered"]
      self.JobReleased:bool = obj["JobReleased"]
      self.JobHeld:bool = obj["JobHeld"]
      self.JobNum:str = obj["JobNum"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.DrawNum:str = obj["DrawNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.ProdQty:int = obj["ProdQty"]
      self.IUM:str = obj["IUM"]
      self.StartDate:str = obj["StartDate"]
      self.StartHour:int = obj["StartHour"]
      self.DueDate:str = obj["DueDate"]
      self.DueHour:int = obj["DueHour"]
      self.ReqDueDate:str = obj["ReqDueDate"]
      self.JobCode:str = obj["JobCode"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.ProdCode:str = obj["ProdCode"]
      self.CommentText:str = obj["CommentText"]
      self.ExpenseCode:str = obj["ExpenseCode"]
      self.InCopyList:bool = obj["InCopyList"]
      self.WIName:str = obj["WIName"]
      self.WIStartDate:str = obj["WIStartDate"]
      self.WIStartHour:int = obj["WIStartHour"]
      self.Candidate:bool = obj["Candidate"]
      self.SchedCode:str = obj["SchedCode"]
      self.SchedLocked:bool = obj["SchedLocked"]
      self.ProjectID:str = obj["ProjectID"]
      self.WIPCleared:bool = obj["WIPCleared"]
      self.JobFirm:bool = obj["JobFirm"]
      self.PersonList:str = obj["PersonList"]
      self.PersonID:str = obj["PersonID"]
      self.ProdTeamID:str = obj["ProdTeamID"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.Plant:str = obj["Plant"]
      self.DatePurged:str = obj["DatePurged"]
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      self.CallNum:int = obj["CallNum"]
      self.CallLine:int = obj["CallLine"]
      self.JobType:str = obj["JobType"]
      self.PhaseID:str = obj["PhaseID"]
      self.AnalysisCode:str = obj["AnalysisCode"]
      self.HDCaseNum:int = obj["HDCaseNum"]
      self.ProductionYield:bool = obj["ProductionYield"]
      self.EquipID:str = obj["EquipID"]
      self.PlanNum:int = obj["PlanNum"]
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      self.ExternalMES:bool = obj["ExternalMES"]
      self.SysRowID:str = obj["SysRowID"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.PersonIDName:str = obj["PersonIDName"]
      self.SOExists:bool = obj["SOExists"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.EquipOEM:str = obj["EquipOEM"]
      self.EquipModel:str = obj["EquipModel"]
      self.EquipTypeID:str = obj["EquipTypeID"]
      self.EquipLocID:str = obj["EquipLocID"]
      self.PMJob:bool = obj["PMJob"]
      self.EquipDescription:str = obj["EquipDescription"]
      self.JobTypeName:str = obj["JobTypeName"]
      self.SmartString:str = obj["SmartString"]
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttrDescription:str = obj["AttrDescription"]
      self.ShortDescription:str = obj["ShortDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobHeadListTableset:
   def __init__(self, obj):
      self.JobHeadList:list[Erp_Tablesets_JobHeadListRow] = obj["JobHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobClosed:bool = obj["JobClosed"]
      self.ClosedDate:str = obj["ClosedDate"]
      self.JobComplete:bool = obj["JobComplete"]
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      self.JobEngineered:bool = obj["JobEngineered"]
      self.CheckOff1:bool = obj["CheckOff1"]
      self.CheckOff2:bool = obj["CheckOff2"]
      self.CheckOff3:bool = obj["CheckOff3"]
      self.CheckOff4:bool = obj["CheckOff4"]
      self.CheckOff5:bool = obj["CheckOff5"]
      self.JobReleased:bool = obj["JobReleased"]
      self.JobHeld:bool = obj["JobHeld"]
      self.SchedStatus:str = obj["SchedStatus"]
      self.JobNum:str = obj["JobNum"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.DrawNum:str = obj["DrawNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.ProdQty:int = obj["ProdQty"]
      self.IUM:str = obj["IUM"]
      self.StartDate:str = obj["StartDate"]
      self.StartHour:int = obj["StartHour"]
      self.DueDate:str = obj["DueDate"]
      self.DueHour:int = obj["DueHour"]
      self.ReqDueDate:str = obj["ReqDueDate"]
      self.JobCode:str = obj["JobCode"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.ProdCode:str = obj["ProdCode"]
      self.UserChar1:str = obj["UserChar1"]
      self.UserChar2:str = obj["UserChar2"]
      self.UserChar3:str = obj["UserChar3"]
      self.UserChar4:str = obj["UserChar4"]
      self.UserDate1:str = obj["UserDate1"]
      self.UserDate2:str = obj["UserDate2"]
      self.UserDate3:str = obj["UserDate3"]
      self.UserDate4:str = obj["UserDate4"]
      self.UserDecimal1:int = obj["UserDecimal1"]
      self.UserDecimal2:int = obj["UserDecimal2"]
      self.UserInteger1:int = obj["UserInteger1"]
      self.UserInteger2:int = obj["UserInteger2"]
      self.CommentText:str = obj["CommentText"]
      self.ExpenseCode:str = obj["ExpenseCode"]
      self.InCopyList:bool = obj["InCopyList"]
      self.WIName:str = obj["WIName"]
      self.WIStartDate:str = obj["WIStartDate"]
      self.WIStartHour:int = obj["WIStartHour"]
      self.WIDueDate:str = obj["WIDueDate"]
      self.WIDueHour:int = obj["WIDueHour"]
      self.Candidate:bool = obj["Candidate"]
      self.SchedCode:str = obj["SchedCode"]
      self.SchedLocked:bool = obj["SchedLocked"]
      self.ProjectID:str = obj["ProjectID"]
      self.WIPCleared:bool = obj["WIPCleared"]
      self.JobFirm:bool = obj["JobFirm"]
      self.PersonList:str = obj["PersonList"]
      self.PersonID:str = obj["PersonID"]
      self.ProdTeamID:str = obj["ProdTeamID"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.Plant:str = obj["Plant"]
      self.DatePurged:str = obj["DatePurged"]
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      self.CallNum:int = obj["CallNum"]
      self.CallLine:int = obj["CallLine"]
      self.JobType:str = obj["JobType"]
      self.RestoreFlag:str = obj["RestoreFlag"]
      self.PhaseID:str = obj["PhaseID"]
      self.AnalysisCode:str = obj["AnalysisCode"]
      self.LockQty:bool = obj["LockQty"]
      self.HDCaseNum:int = obj["HDCaseNum"]
      self.ProcessMode:str = obj["ProcessMode"]
      self.PlannedActionDate:str = obj["PlannedActionDate"]
      self.PlannedKitDate:str = obj["PlannedKitDate"]
      self.MSPTaskID:str = obj["MSPTaskID"]
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      self.UserMapData:str = obj["UserMapData"]
      self.ProductionYield:bool = obj["ProductionYield"]
      self.OrigProdQty:int = obj["OrigProdQty"]
      self.PreserveOrigQtys:bool = obj["PreserveOrigQtys"]
      self.NoAutoCompletion:bool = obj["NoAutoCompletion"]
      self.NoAutoClosing:bool = obj["NoAutoClosing"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.CreateDate:str = obj["CreateDate"]
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      self.PDMObjID:str = obj["PDMObjID"]
      self.ExportRequested:str = obj["ExportRequested"]
      self.SplitMfgCostElements:bool = obj["SplitMfgCostElements"]
      self.XRefPartNum:str = obj["XRefPartNum"]
      self.XRefPartType:str = obj["XRefPartType"]
      self.XRefCustNum:int = obj["XRefCustNum"]
      self.BasePartNum:str = obj["BasePartNum"]
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      self.RoughCutScheduled:bool = obj["RoughCutScheduled"]
      self.EquipID:str = obj["EquipID"]
      self.PlanNum:int = obj["PlanNum"]
      self.MaintPriority:str = obj["MaintPriority"]
      self.SplitJob:bool = obj["SplitJob"]
      self.NumberSource:bool = obj["NumberSource"]
      self.CloseMeterReading:int = obj["CloseMeterReading"]
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      self.IssueTopics:str = obj["IssueTopics"]
      self.ResTopicID1:str = obj["ResTopicID1"]
      self.ResTopicID2:str = obj["ResTopicID2"]
      self.ResTopicID3:str = obj["ResTopicID3"]
      self.ResTopicID4:str = obj["ResTopicID4"]
      self.ResTopicID5:str = obj["ResTopicID5"]
      self.ResTopicID6:str = obj["ResTopicID6"]
      self.ResTopicID7:str = obj["ResTopicID7"]
      self.ResTopicID8:str = obj["ResTopicID8"]
      self.ResTopicID9:str = obj["ResTopicID9"]
      self.ResTopicID10:str = obj["ResTopicID10"]
      self.ResTopics:str = obj["ResTopics"]
      self.Forward:bool = obj["Forward"]
      self.SchedSeq:int = obj["SchedSeq"]
      self.PAAExists:bool = obj["PAAExists"]
      self.DtlsWithinLeadTime:bool = obj["DtlsWithinLeadTime"]
      self.GroupSeq:int = obj["GroupSeq"]
      self.RoughCut:bool = obj["RoughCut"]
      self.PlanGUID:str = obj["PlanGUID"]
      self.PlanUserID:str = obj["PlanUserID"]
      self.LastChangedBy:str = obj["LastChangedBy"]
      self.LastChangedOn:str = obj["LastChangedOn"]
      self.EPMExportLevel:int = obj["EPMExportLevel"]
      self.JobWorkflowState:str = obj["JobWorkflowState"]
      self.JobCSR:str = obj["JobCSR"]
      self.ExternalMES:bool = obj["ExternalMES"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.LastExternalMESDate:str = obj["LastExternalMESDate"]
      self.LastScheduleDate:str = obj["LastScheduleDate"]
      self.LastScheduleProc:str = obj["LastScheduleProc"]
      self.SchedPriority:int = obj["SchedPriority"]
      self.DaysLate:int = obj["DaysLate"]
      self.ContractID:str = obj["ContractID"]
      self.ProjProcessed:bool = obj["ProjProcessed"]
      self.SyncReqBy:bool = obj["SyncReqBy"]
      self.CustName:str = obj["CustName"]
      self.CustID:str = obj["CustID"]
      self.IsCSRSet:bool = obj["IsCSRSet"]
      self.UnReadyCostProcess:bool = obj["UnReadyCostProcess"]
      self.ProcSuspendedUpdates:str = obj["ProcSuspendedUpdates"]
      self.ProjProcessedDate:str = obj["ProjProcessedDate"]
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      self.EpicorFSA:bool = obj["EpicorFSA"]
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.PersonIDName:str = obj["PersonIDName"]
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      self.FSMSendTo:bool = obj["FSMSendTo"]
      self.FSMServiceReportID:str = obj["FSMServiceReportID"]
      self.AdvanceLaborRate:bool = obj["AdvanceLaborRate"]
      self.dspReadyCostProcess:bool = obj["dspReadyCostProcess"]
      self.EnableJobEngineered:bool = obj["EnableJobEngineered"]
      self.EnableJobFirm:bool = obj["EnableJobFirm"]
      self.EnableJobReleased:bool = obj["EnableJobReleased"]
      self.EnableMaterialStatus:bool = obj["EnableMaterialStatus"]
      self.EnableProject:bool = obj["EnableProject"]
      self.EngineerAllowed:bool = obj["EngineerAllowed"]
      self.EquipLocDesc:str = obj["EquipLocDesc"]
      self.ExtUpdated:bool = obj["ExtUpdated"]
      self.FinalOpDueDate:str = obj["FinalOpDueDate"]
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      self.FirmProcess:bool = obj["FirmProcess"]
      self.HasPlanAsAsm:bool = obj["HasPlanAsAsm"]
      self.HeaderSensitive:bool = obj["HeaderSensitive"]
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      self.JobTypeName:str = obj["JobTypeName"]
      self.KitTime:int = obj["KitTime"]
      self.LockedQty:bool = obj["LockedQty"]
      self.NewMeter:int = obj["NewMeter"]
      self.OldJobNum:str = obj["OldJobNum"]
      self.OrderQty:int = obj["OrderQty"]
      self.PartmasterPart:bool = obj["PartmasterPart"]
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.PMJob:bool = obj["PMJob"]
      self.ProcessModeDescription:str = obj["ProcessModeDescription"]
      self.ReceiveTime:int = obj["ReceiveTime"]
      self.SmartString:str = obj["SmartString"]
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      self.SOExists:bool = obj["SOExists"]
      self.StockQty:int = obj["StockQty"]
      self.ToFirm:bool = obj["ToFirm"]
      self.XRefPartTypeDesc:str = obj["XRefPartTypeDesc"]
      self.ChangeDescription:str = obj["ChangeDescription"]
      self.ClearDataset:bool = obj["ClearDataset"]
      self.IsCoPart:bool = obj["IsCoPart"]
      self.PartRevProcessMfgID:str = obj["PartRevProcessMfgID"]
      self.PartRevProcessMfgType:str = obj["PartRevProcessMfgType"]
      self.SendToFSA:bool = obj["SendToFSA"]
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.EquipMeterUOM:str = obj["EquipMeterUOM"]
      self.EquipSerialNum:str = obj["EquipSerialNum"]
      self.EquipLocID:str = obj["EquipLocID"]
      self.EquipPlant:str = obj["EquipPlant"]
      self.EquipDescription:str = obj["EquipDescription"]
      self.EquipBrand:str = obj["EquipBrand"]
      self.EquipModel:str = obj["EquipModel"]
      self.EquipCurrentMeter:int = obj["EquipCurrentMeter"]
      self.EquipTypeID:str = obj["EquipTypeID"]
      self.EquipOEM:str = obj["EquipOEM"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumLocationIDNumReq:bool = obj["PartNumLocationIDNumReq"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.PlantMaintPlant:str = obj["PlantMaintPlant"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProdTeamIDDescription:str = obj["ProdTeamIDDescription"]
      self.ProdTeamIDName:str = obj["ProdTeamIDName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.SchedCodeDescription:str = obj["SchedCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobMtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobMtlInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.PlanSeq:int = obj["PlanSeq"]
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      self.SpecID:str = obj["SpecID"]
      self.SpecRevNum:str = obj["SpecRevNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobMtlRefDesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.RefDes:str = obj["RefDes"]
      self.RefDesSeq:int = obj["RefDesSeq"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      self.Side:str = obj["Side"]
      self.XLocation:int = obj["XLocation"]
      self.YLocation:int = obj["YLocation"]
      self.ZLocation:int = obj["ZLocation"]
      self.Rotation:int = obj["Rotation"]
      self.Description:str = obj["Description"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobMtlRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      self.SubstanceID:str = obj["SubstanceID"]
      self.Weight:int = obj["Weight"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.Manual:bool = obj["Manual"]
      self.ExemptDate:str = obj["ExemptDate"]
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.Exempt:bool = obj["Exempt"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobMtlRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      self.Manual:bool = obj["Manual"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.Weight:bool = obj["Weight"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobComplete:bool = obj["JobComplete"]
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.PartNum:str = obj["PartNum"]
      self.Description:str = obj["Description"]
      self.QtyPer:int = obj["QtyPer"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.IUM:str = obj["IUM"]
      self.LeadTime:int = obj["LeadTime"]
      self.RelatedOperation:int = obj["RelatedOperation"]
      self.MtlBurRate:int = obj["MtlBurRate"]
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      self.EstUnitCost:int = obj["EstUnitCost"]
      self.IssuedQty:int = obj["IssuedQty"]
      self.TotalCost:int = obj["TotalCost"]
      self.MtlBurCost:int = obj["MtlBurCost"]
      self.ReqDate:str = obj["ReqDate"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      self.SalvageDescription:str = obj["SalvageDescription"]
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      self.SalvageUM:str = obj["SalvageUM"]
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      self.SalvageCredit:int = obj["SalvageCredit"]
      self.SalvageMtlBurCredit:int = obj["SalvageMtlBurCredit"]
      self.MfgComment:str = obj["MfgComment"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.BuyIt:bool = obj["BuyIt"]
      self.Ordered:bool = obj["Ordered"]
      self.PurComment:str = obj["PurComment"]
      self.BackFlush:bool = obj["BackFlush"]
      self.EstScrap:int = obj["EstScrap"]
      self.EstScrapType:str = obj["EstScrapType"]
      self.FixedQty:bool = obj["FixedQty"]
      self.FindNum:str = obj["FindNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SndAlrtCmpl:bool = obj["SndAlrtCmpl"]
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      self.Plant:str = obj["Plant"]
      self.Direct:bool = obj["Direct"]
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      self.SalvageMtlCredit:int = obj["SalvageMtlCredit"]
      self.SalvageLbrCredit:int = obj["SalvageLbrCredit"]
      self.SalvageBurCredit:int = obj["SalvageBurCredit"]
      self.SalvageSubCredit:int = obj["SalvageSubCredit"]
      self.APSAddResType:str = obj["APSAddResType"]
      self.CallNum:int = obj["CallNum"]
      self.CallLine:int = obj["CallLine"]
      self.ProdCode:str = obj["ProdCode"]
      self.UnitPrice:int = obj["UnitPrice"]
      self.BillableUnitPrice:int = obj["BillableUnitPrice"]
      self.DocBillableUnitPrice:int = obj["DocBillableUnitPrice"]
      self.ResReasonCode:str = obj["ResReasonCode"]
      self.PricePerCode:str = obj["PricePerCode"]
      self.Billable:bool = obj["Billable"]
      self.ShippedQty:int = obj["ShippedQty"]
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      self.QtyStagedToDate:int = obj["QtyStagedToDate"]
      self.AddedMtl:bool = obj["AddedMtl"]
      self.MiscCharge:bool = obj["MiscCharge"]
      self.MiscCode:str = obj["MiscCode"]
      self.SCMiscCode:str = obj["SCMiscCode"]
      self.RFQNeeded:bool = obj["RFQNeeded"]
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      self.RFQNum:int = obj["RFQNum"]
      self.RFQLine:int = obj["RFQLine"]
      self.RFQStat:str = obj["RFQStat"]
      self.AnalysisCode:str = obj["AnalysisCode"]
      self.GlbRFQ:bool = obj["GlbRFQ"]
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      self.WIReqDate:str = obj["WIReqDate"]
      self.Rpt1BillableUnitPrice:int = obj["Rpt1BillableUnitPrice"]
      self.Rpt2BillableUnitPrice:int = obj["Rpt2BillableUnitPrice"]
      self.Rpt3BillableUnitPrice:int = obj["Rpt3BillableUnitPrice"]
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      self.BaseRequiredQty:int = obj["BaseRequiredQty"]
      self.BaseUOM:str = obj["BaseUOM"]
      self.Weight:int = obj["Weight"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.ReqRefDes:int = obj["ReqRefDes"]
      self.BasePartNum:str = obj["BasePartNum"]
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      self.SelectForPicking:bool = obj["SelectForPicking"]
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      self.StagingBinNum:str = obj["StagingBinNum"]
      self.PickError:str = obj["PickError"]
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      self.SalvageEstMtlUnitCredit:int = obj["SalvageEstMtlUnitCredit"]
      self.SalvageEstLbrUnitCredit:int = obj["SalvageEstLbrUnitCredit"]
      self.SalvageEstBurUnitCredit:int = obj["SalvageEstBurUnitCredit"]
      self.SalvageEstSubUnitCredit:int = obj["SalvageEstSubUnitCredit"]
      self.LoanedQty:int = obj["LoanedQty"]
      self.BorrowedQty:int = obj["BorrowedQty"]
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      self.GeneralPlanInfo:str = obj["GeneralPlanInfo"]
      self.EstStdDescription:str = obj["EstStdDescription"]
      self.PricingUOM:str = obj["PricingUOM"]
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      self.IsPOCostingMaintained:bool = obj["IsPOCostingMaintained"]
      self.EstStdType:int = obj["EstStdType"]
      self.POCostingFactor:int = obj["POCostingFactor"]
      self.PlannedQtyPerUnit:int = obj["PlannedQtyPerUnit"]
      self.POCostingDirection:int = obj["POCostingDirection"]
      self.POCostingUnitVal:int = obj["POCostingUnitVal"]
      self.GroupSeq:int = obj["GroupSeq"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.OrigStructTag:str = obj["OrigStructTag"]
      self.OrigGroupSeq:int = obj["OrigGroupSeq"]
      self.ShowStatusIcon:str = obj["ShowStatusIcon"]
      self.ContractID:str = obj["ContractID"]
      self.LinkToContract:bool = obj["LinkToContract"]
      self.StagingLotNum:str = obj["StagingLotNum"]
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      self.LocationView:bool = obj["LocationView"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      self.SalvageAttributeSetID:int = obj["SalvageAttributeSetID"]
      self.SalvagePlanningNumberOfPieces:int = obj["SalvagePlanningNumberOfPieces"]
      self.SalvagePlanningAttributeSetID:int = obj["SalvagePlanningAttributeSetID"]
      self.RelatedStage:str = obj["RelatedStage"]
      self.SalvageRevisionNum:str = obj["SalvageRevisionNum"]
      self.PartAllocQueueAction:str = obj["PartAllocQueueAction"]
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DisplayExtPrice:int = obj["DisplayExtPrice"]
      self.DisplayUnitPrice:int = obj["DisplayUnitPrice"]
      self.DocDisplayExtPrice:int = obj["DocDisplayExtPrice"]
      self.DocDisplayUnitPrice:int = obj["DocDisplayUnitPrice"]
      self.dspBuyIt:bool = obj["dspBuyIt"]
      self.DspIUM:str = obj["DspIUM"]
      self.EnableBackflush:bool = obj["EnableBackflush"]
      self.EnableBuyIt:bool = obj["EnableBuyIt"]
      self.EnableConfigure:bool = obj["EnableConfigure"]
      self.EnableDirect:bool = obj["EnableDirect"]
      self.EnableFixedQty:bool = obj["EnableFixedQty"]
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.EnableRcvInspReq:bool = obj["EnableRcvInspReq"]
      self.EnableSndAlrtCmpl:bool = obj["EnableSndAlrtCmpl"]
      self.EnableSplitCosts:bool = obj["EnableSplitCosts"]
      self.EstCost:int = obj["EstCost"]
      self.IPCaller:str = obj["IPCaller"]
      self.IsBaseCurrency:bool = obj["IsBaseCurrency"]
      self.IsMtlConfigurationOn:bool = obj["IsMtlConfigurationOn"]
      self.IsMtlConfigureOn:bool = obj["IsMtlConfigureOn"]
      self.IsMtlExtConfig:bool = obj["IsMtlExtConfig"]
      self.IsMtlRevisionApproved:bool = obj["IsMtlRevisionApproved"]
      self.PartExists:bool = obj["PartExists"]
      self.PlantList:str = obj["PlantList"]
      self.PricePerCodeDescription:str = obj["PricePerCodeDescription"]
      self.RDEndNum:int = obj["RDEndNum"]
      self.RDPrefix:str = obj["RDPrefix"]
      self.RDStartNum:int = obj["RDStartNum"]
      self.RDSuffix:str = obj["RDSuffix"]
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      self.RetainValues:bool = obj["RetainValues"]
      self.Rpt1DisplayExtPrice:int = obj["Rpt1DisplayExtPrice"]
      self.Rpt1DisplayUnitPrice:int = obj["Rpt1DisplayUnitPrice"]
      self.Rpt2DisplayExtPrice:int = obj["Rpt2DisplayExtPrice"]
      self.Rpt2DisplayUnitPrice:int = obj["Rpt2DisplayUnitPrice"]
      self.Rpt3DisplayExtPrice:int = obj["Rpt3DisplayExtPrice"]
      self.Rpt3DisplayUnitPrice:int = obj["Rpt3DisplayUnitPrice"]
      self.SalvageBaseUOM:str = obj["SalvageBaseUOM"]
      self.ShowInspRqdImg:bool = obj["ShowInspRqdImg"]
      self.SubContract:bool = obj["SubContract"]
      self.AllowBackflushUncheck:bool = obj["AllowBackflushUncheck"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.EnableSalvageAttributeSetSearch:bool = obj["EnableSalvageAttributeSetSearch"]
      self.PlanningNumberOfPiecesDisp:int = obj["PlanningNumberOfPiecesDisp"]
      self.SalvagePlanningNumberOfPiecesDisp:int = obj["SalvagePlanningNumberOfPiecesDisp"]
      self.SkipUnitPriceCalc:bool = obj["SkipUnitPriceCalc"]
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      self.InPartAllocQueue:bool = obj["InPartAllocQueue"]
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.AllocatedQty:int = obj["AllocatedQty"]
      self.ReservedQty:int = obj["ReservedQty"]
      self.AvailableQty:int = obj["AvailableQty"]
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.AssemblySeqPartNum:str = obj["AssemblySeqPartNum"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.JobNumPartNum:str = obj["JobNumPartNum"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PlantName:str = obj["PlantName"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.PurMiscCodeDescription:str = obj["PurMiscCodeDescription"]
      self.PurMiscCodeLCAmount:int = obj["PurMiscCodeLCAmount"]
      self.PurMiscCodeLCDisburseMethod:str = obj["PurMiscCodeLCDisburseMethod"]
      self.PurMiscCodeLCCurrencyCode:str = obj["PurMiscCodeLCCurrencyCode"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.SalvageAttributeSetIDDescription:str = obj["SalvageAttributeSetIDDescription"]
      self.SalvageAttributeSetIDShortDescription:str = obj["SalvageAttributeSetIDShortDescription"]
      self.SalvagePartNumPartDescription:str = obj["SalvagePartNumPartDescription"]
      self.SalvagePartNumPricePerCode:str = obj["SalvagePartNumPricePerCode"]
      self.SalvagePartNumTrackInventoryByRevision:bool = obj["SalvagePartNumTrackInventoryByRevision"]
      self.SalvagePartNumTrackSerialNum:bool = obj["SalvagePartNumTrackSerialNum"]
      self.SalvagePartNumTrackDimension:bool = obj["SalvagePartNumTrackDimension"]
      self.SalvagePartNumTrackInventoryAttributes:bool = obj["SalvagePartNumTrackInventoryAttributes"]
      self.SalvagePartNumAttrClassID:str = obj["SalvagePartNumAttrClassID"]
      self.SalvagePartNumSellingFactor:int = obj["SalvagePartNumSellingFactor"]
      self.SalvagePartNumTrackLots:bool = obj["SalvagePartNumTrackLots"]
      self.SalvagePartNumSalesUM:str = obj["SalvagePartNumSalesUM"]
      self.SalvagePartNumIUM:str = obj["SalvagePartNumIUM"]
      self.SCMiscCodeDescription:str = obj["SCMiscCodeDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorPPState:str = obj["VendorPPState"]
      self.VendorPPAddress2:str = obj["VendorPPAddress2"]
      self.VendorPPCountry:str = obj["VendorPPCountry"]
      self.VendorPPPrimPCon:int = obj["VendorPPPrimPCon"]
      self.VendorPPZip:str = obj["VendorPPZip"]
      self.VendorPPCity:str = obj["VendorPPCity"]
      self.VendorPPAddress1:str = obj["VendorPPAddress1"]
      self.VendorPPAddress3:str = obj["VendorPPAddress3"]
      self.VendorPPName:str = obj["VendorPPName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobOpDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      self.SetupOrProd:str = obj["SetupOrProd"]
      self.CapabilityID:str = obj["CapabilityID"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceID:str = obj["ResourceID"]
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      self.DailyProdRate:int = obj["DailyProdRate"]
      self.NumResources:int = obj["NumResources"]
      self.EstSetHours:int = obj["EstSetHours"]
      self.EstProdHours:int = obj["EstProdHours"]
      self.ProdStandard:int = obj["ProdStandard"]
      self.StdFormat:str = obj["StdFormat"]
      self.StdBasis:str = obj["StdBasis"]
      self.OpsPerPart:int = obj["OpsPerPart"]
      self.ProdLabRate:int = obj["ProdLabRate"]
      self.SetupLabRate:int = obj["SetupLabRate"]
      self.ProdBurRate:int = obj["ProdBurRate"]
      self.SetupBurRate:int = obj["SetupBurRate"]
      self.ProdComplete:bool = obj["ProdComplete"]
      self.SetupComplete:bool = obj["SetupComplete"]
      self.ActProdHours:int = obj["ActProdHours"]
      self.ActProdRwkHours:int = obj["ActProdRwkHours"]
      self.ActSetupHours:int = obj["ActSetupHours"]
      self.ActSetupRwkHours:int = obj["ActSetupRwkHours"]
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      self.ActBurCost:int = obj["ActBurCost"]
      self.ActLabCost:int = obj["ActLabCost"]
      self.ReworkBurCost:int = obj["ReworkBurCost"]
      self.ReworkLabCost:int = obj["ReworkLabCost"]
      self.ResourceLock:bool = obj["ResourceLock"]
      self.SysCreateDate:str = obj["SysCreateDate"]
      self.SysCreateTime:int = obj["SysCreateTime"]
      self.OpDtlDesc:str = obj["OpDtlDesc"]
      self.EstSetHoursPerMch:int = obj["EstSetHoursPerMch"]
      self.OverrideRates:bool = obj["OverrideRates"]
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      self.IsPrimaryProd:bool = obj["IsPrimaryProd"]
      self.IsPrimarySetup:bool = obj["IsPrimarySetup"]
      self.AutoSystemAdded:bool = obj["AutoSystemAdded"]
      self.MobileAllocatedResource:bool = obj["MobileAllocatedResource"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      self.CapabilityDesc:str = obj["CapabilityDesc"]
      self.OperOpStdID:str = obj["OperOpStdID"]
      self.PrimaryProd:bool = obj["PrimaryProd"]
      self.PrimarySetup:bool = obj["PrimarySetup"]
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      self.SchedResourceDesc:str = obj["SchedResourceDesc"]
      self.SchedResourceGrpDesc:str = obj["SchedResourceGrpDesc"]
      self.SubContract:bool = obj["SubContract"]
      self.WISchedResourceDesc:str = obj["WISchedResourceDesc"]
      self.WISchedResourceGrpDesc:str = obj["WISchedResourceGrpDesc"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.CapabilityIDDescription:str = obj["CapabilityIDDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.ResourceGrpIDDescription:str = obj["ResourceGrpIDDescription"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobOperActionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.ActionSeq:int = obj["ActionSeq"]
      self.ActionParamSeq:int = obj["ActionParamSeq"]
      self.ActionParamFieldDataType:str = obj["ActionParamFieldDataType"]
      self.ActionParamValueCharacter:str = obj["ActionParamValueCharacter"]
      self.ActionParamValueDate:str = obj["ActionParamValueDate"]
      self.ActionParamValueDecimal:int = obj["ActionParamValueDecimal"]
      self.ActionParamValueInteger:int = obj["ActionParamValueInteger"]
      self.ActionParamValueLogical:bool = obj["ActionParamValueLogical"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobOperActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.ActionSeq:int = obj["ActionSeq"]
      self.ActionDesc:str = obj["ActionDesc"]
      self.Required:bool = obj["Required"]
      self.Completed:bool = obj["Completed"]
      self.CompletedBy:str = obj["CompletedBy"]
      self.CompletedOn:str = obj["CompletedOn"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobOperAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobOperInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.PlanSeq:int = obj["PlanSeq"]
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      self.SpecID:str = obj["SpecID"]
      self.SpecRevNum:str = obj["SpecRevNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobOperMachParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.MachParamSeq:int = obj["MachParamSeq"]
      self.RequestCode:str = obj["RequestCode"]
      self.MachineNum:str = obj["MachineNum"]
      self.ToolNum:str = obj["ToolNum"]
      self.PartNum:str = obj["PartNum"]
      self.ParamNum:int = obj["ParamNum"]
      self.ParamUpperLimit:int = obj["ParamUpperLimit"]
      self.ParamNominalValue:int = obj["ParamNominalValue"]
      self.ParamLowerLimit:int = obj["ParamLowerLimit"]
      self.ParamDelayValue:int = obj["ParamDelayValue"]
      self.SpecEnable:bool = obj["SpecEnable"]
      self.SpecControlAlarm:bool = obj["SpecControlAlarm"]
      self.SpecRunAlarm:bool = obj["SpecRunAlarm"]
      self.ProcSpecAlarm:bool = obj["ProcSpecAlarm"]
      self.ProcControlAlarm:bool = obj["ProcControlAlarm"]
      self.PartQualSpecEnable:bool = obj["PartQualSpecEnable"]
      self.PartQualControlEnable:bool = obj["PartQualControlEnable"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.CreatedOn:str = obj["CreatedOn"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.ChangedOn:str = obj["ChangedOn"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobOperRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      self.SubstanceID:str = obj["SubstanceID"]
      self.Weight:int = obj["Weight"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.Manual:bool = obj["Manual"]
      self.ExemptDate:str = obj["ExemptDate"]
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.Exempt:bool = obj["Exempt"]
      self.OpCode:str = obj["OpCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobOperRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      self.OpCode:str = obj["OpCode"]
      self.Manual:bool = obj["Manual"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.Weight:bool = obj["Weight"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobOperRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobComplete:bool = obj["JobComplete"]
      self.OpComplete:bool = obj["OpComplete"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.OpCode:str = obj["OpCode"]
      self.OpStdID:str = obj["OpStdID"]
      self.EstSetHours:int = obj["EstSetHours"]
      self.EstProdHours:int = obj["EstProdHours"]
      self.ProdStandard:int = obj["ProdStandard"]
      self.StdFormat:str = obj["StdFormat"]
      self.StdBasis:str = obj["StdBasis"]
      self.OpsPerPart:int = obj["OpsPerPart"]
      self.QtyPer:int = obj["QtyPer"]
      self.QueStartDate:str = obj["QueStartDate"]
      self.QueStartHour:int = obj["QueStartHour"]
      self.StartDate:str = obj["StartDate"]
      self.StartHour:int = obj["StartHour"]
      self.DueDate:str = obj["DueDate"]
      self.DueHour:int = obj["DueHour"]
      self.MoveDueDate:str = obj["MoveDueDate"]
      self.MoveDueHour:int = obj["MoveDueHour"]
      self.ProdLabRate:int = obj["ProdLabRate"]
      self.SetupLabRate:int = obj["SetupLabRate"]
      self.ProdBurRate:int = obj["ProdBurRate"]
      self.SetupBurRate:int = obj["SetupBurRate"]
      self.AddedOper:bool = obj["AddedOper"]
      self.Machines:int = obj["Machines"]
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      self.ProdComplete:bool = obj["ProdComplete"]
      self.SetupComplete:bool = obj["SetupComplete"]
      self.ActProdHours:int = obj["ActProdHours"]
      self.ActProdRwkHours:int = obj["ActProdRwkHours"]
      self.ActSetupHours:int = obj["ActSetupHours"]
      self.ActSetupRwkHours:int = obj["ActSetupRwkHours"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      self.EstScrap:int = obj["EstScrap"]
      self.EstScrapType:str = obj["EstScrapType"]
      self.SubContract:bool = obj["SubContract"]
      self.IUM:str = obj["IUM"]
      self.EstUnitCost:int = obj["EstUnitCost"]
      self.DaysOut:int = obj["DaysOut"]
      self.PartNum:str = obj["PartNum"]
      self.Description:str = obj["Description"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.CommentText:str = obj["CommentText"]
      self.SchedRelation:str = obj["SchedRelation"]
      self.RunQty:int = obj["RunQty"]
      self.WIName:str = obj["WIName"]
      self.WIMachines:int = obj["WIMachines"]
      self.WIQueStartDate:str = obj["WIQueStartDate"]
      self.WIQueStartHour:int = obj["WIQueStartHour"]
      self.WIStartDate:str = obj["WIStartDate"]
      self.WIStartHour:int = obj["WIStartHour"]
      self.WIDueDate:str = obj["WIDueDate"]
      self.WIDueHour:int = obj["WIDueHour"]
      self.WIMoveDueDate:str = obj["WIMoveDueDate"]
      self.WIMoveDueHour:int = obj["WIMoveDueHour"]
      self.WIHoursPerMachine:int = obj["WIHoursPerMachine"]
      self.WILoadDate:str = obj["WILoadDate"]
      self.WILoadHour:int = obj["WILoadHour"]
      self.ActBurCost:int = obj["ActBurCost"]
      self.ActLabCost:int = obj["ActLabCost"]
      self.ReworkBurCost:int = obj["ReworkBurCost"]
      self.ReworkLabCost:int = obj["ReworkLabCost"]
      self.MiscAmt:int = obj["MiscAmt"]
      self.HoursPerMachine:int = obj["HoursPerMachine"]
      self.LoadDate:str = obj["LoadDate"]
      self.LoadHour:int = obj["LoadHour"]
      self.ReloadNum:int = obj["ReloadNum"]
      self.SndAlrtCmpl:bool = obj["SndAlrtCmpl"]
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      self.JobEngineered:bool = obj["JobEngineered"]
      self.EstSetHoursPerMch:int = obj["EstSetHoursPerMch"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AutoReceiptDate:str = obj["AutoReceiptDate"]
      self.LastLaborDate:str = obj["LastLaborDate"]
      self.CallNum:int = obj["CallNum"]
      self.CallLine:int = obj["CallLine"]
      self.LaborRate:int = obj["LaborRate"]
      self.BillableLaborRate:int = obj["BillableLaborRate"]
      self.DocLaborRate:int = obj["DocLaborRate"]
      self.DocBillableLaborRate:int = obj["DocBillableLaborRate"]
      self.Billable:bool = obj["Billable"]
      self.UnitPrice:int = obj["UnitPrice"]
      self.BillableUnitPrice:int = obj["BillableUnitPrice"]
      self.DocBillableUnitPrice:int = obj["DocBillableUnitPrice"]
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      self.PricePerCode:str = obj["PricePerCode"]
      self.FAQty:int = obj["FAQty"]
      self.QtyStagedToDate:int = obj["QtyStagedToDate"]
      self.RFQNeeded:bool = obj["RFQNeeded"]
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      self.RFQNum:int = obj["RFQNum"]
      self.RFQLine:int = obj["RFQLine"]
      self.RFQStat:str = obj["RFQStat"]
      self.SetupGroup:str = obj["SetupGroup"]
      self.RestoreFlag:str = obj["RestoreFlag"]
      self.AnalysisCode:str = obj["AnalysisCode"]
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      self.OpDesc:str = obj["OpDesc"]
      self.KitDate:str = obj["KitDate"]
      self.GlbRFQ:bool = obj["GlbRFQ"]
      self.BookedUnitCost:int = obj["BookedUnitCost"]
      self.RecalcExpProdYld:bool = obj["RecalcExpProdYld"]
      self.UserMapData:str = obj["UserMapData"]
      self.RoughCutSched:bool = obj["RoughCutSched"]
      self.SchedComment:str = obj["SchedComment"]
      self.Rpt1BillableLaborRate:int = obj["Rpt1BillableLaborRate"]
      self.Rpt2BillableLaborRate:int = obj["Rpt2BillableLaborRate"]
      self.Rpt3BillableLaborRate:int = obj["Rpt3BillableLaborRate"]
      self.Rpt1BillableUnitPrice:int = obj["Rpt1BillableUnitPrice"]
      self.Rpt2BillableUnitPrice:int = obj["Rpt2BillableUnitPrice"]
      self.Rpt3BillableUnitPrice:int = obj["Rpt3BillableUnitPrice"]
      self.Rpt1LaborRate:int = obj["Rpt1LaborRate"]
      self.Rpt2LaborRate:int = obj["Rpt2LaborRate"]
      self.Rpt3LaborRate:int = obj["Rpt3LaborRate"]
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      self.Weight:int = obj["Weight"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.SendAheadType:str = obj["SendAheadType"]
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      self.PrjRoleList:str = obj["PrjRoleList"]
      self.TearDwnEndDate:str = obj["TearDwnEndDate"]
      self.TearDwnEndHour:int = obj["TearDwnEndHour"]
      self.WITearDwnEndDate:str = obj["WITearDwnEndDate"]
      self.WITearDwnEndHour:int = obj["WITearDwnEndHour"]
      self.UseAllRoles:bool = obj["UseAllRoles"]
      self.AssetPartNum:str = obj["AssetPartNum"]
      self.SerialNumber:str = obj["SerialNumber"]
      self.ActualStartDate:str = obj["ActualStartDate"]
      self.ActualStartHour:int = obj["ActualStartHour"]
      self.ActualEndDate:str = obj["ActualEndDate"]
      self.ActualEndHour:int = obj["ActualEndHour"]
      self.FSJobStatus:int = obj["FSJobStatus"]
      self.Instructions:str = obj["Instructions"]
      self.ProdUOM:str = obj["ProdUOM"]
      self.GeneralPlanInfo:str = obj["GeneralPlanInfo"]
      self.EstStdDescription:str = obj["EstStdDescription"]
      self.JDFOpCompleted:bool = obj["JDFOpCompleted"]
      self.RemovedfromPlan:bool = obj["RemovedfromPlan"]
      self.EstStdType:int = obj["EstStdType"]
      self.ExternalMES:bool = obj["ExternalMES"]
      self.PctReg:int = obj["PctReg"]
      self.SetupMaterial:int = obj["SetupMaterial"]
      self.MaterialColorRating:int = obj["MaterialColorRating"]
      self.MiscInfo1:str = obj["MiscInfo1"]
      self.MiscInfo2:str = obj["MiscInfo2"]
      self.SetupURL:str = obj["SetupURL"]
      self.ExpPctUp:int = obj["ExpPctUp"]
      self.ExpCycTm:int = obj["ExpCycTm"]
      self.ExpGood:int = obj["ExpGood"]
      self.NonProdLimit:int = obj["NonProdLimit"]
      self.AutoSpcEnable:bool = obj["AutoSpcEnable"]
      self.AutoSpcPeriod:int = obj["AutoSpcPeriod"]
      self.PartQualEnable:bool = obj["PartQualEnable"]
      self.AutoSpcSubgroup:int = obj["AutoSpcSubgroup"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.MobileOperation:bool = obj["MobileOperation"]
      self.ReWork:bool = obj["ReWork"]
      self.RequestMove:bool = obj["RequestMove"]
      self.ContractID:str = obj["ContractID"]
      self.PrinterID:str = obj["PrinterID"]
      self.LastPrintedDate:str = obj["LastPrintedDate"]
      self.LastPCIDPrinted:str = obj["LastPCIDPrinted"]
      self.CurrentPkgCode:str = obj["CurrentPkgCode"]
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      self.StageNumber:str = obj["StageNumber"]
      self.TemplateID:str = obj["TemplateID"]
      self.ActScrapQty:int = obj["ActScrapQty"]
      self.AutoReceive:bool = obj["AutoReceive"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DisplayExtPrice:int = obj["DisplayExtPrice"]
      self.DisplayServAmt:int = obj["DisplayServAmt"]
      self.DisplayServLaborRate:int = obj["DisplayServLaborRate"]
      self.DisplayUnitPrice:int = obj["DisplayUnitPrice"]
      self.DocDisplayExtPrice:int = obj["DocDisplayExtPrice"]
      self.DocDisplayServAmt:int = obj["DocDisplayServAmt"]
      self.DocDisplayServLaborRate:int = obj["DocDisplayServLaborRate"]
      self.DocDisplayUnitPrice:int = obj["DocDisplayUnitPrice"]
      self.DspIUM:str = obj["DspIUM"]
      self.EnableAutoReceive:bool = obj["EnableAutoReceive"]
      self.EnableSndAlrtCmpl:bool = obj["EnableSndAlrtCmpl"]
      self.EnableSNReqSubConShip:bool = obj["EnableSNReqSubConShip"]
      self.EnableSNRequiredOpr:bool = obj["EnableSNRequiredOpr"]
      self.EstBurdenCost:int = obj["EstBurdenCost"]
      self.EstLabHours:int = obj["EstLabHours"]
      self.EstLaborCost:int = obj["EstLaborCost"]
      self.EstSubCost:int = obj["EstSubCost"]
      self.FinalOpr:bool = obj["FinalOpr"]
      self.IsBaseCurrency:bool = obj["IsBaseCurrency"]
      self.LaborEntryMethodDesc:str = obj["LaborEntryMethodDesc"]
      self.LoadHrs:int = obj["LoadHrs"]
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.PrimaryProdOpDtlDesc:str = obj["PrimaryProdOpDtlDesc"]
      self.PrimaryResourceGrpDesc:str = obj["PrimaryResourceGrpDesc"]
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      self.PrimarySetupOpDtlDesc:str = obj["PrimarySetupOpDtlDesc"]
      self.ProductionQty:int = obj["ProductionQty"]
      self.RefreshResources:bool = obj["RefreshResources"]
      self.Rpt1DisplayExtPrice:int = obj["Rpt1DisplayExtPrice"]
      self.Rpt1DisplayServAmt:int = obj["Rpt1DisplayServAmt"]
      self.Rpt1DisplayServLaborRate:int = obj["Rpt1DisplayServLaborRate"]
      self.Rpt1DisplayUnitPrice:int = obj["Rpt1DisplayUnitPrice"]
      self.Rpt2DisplayExtPrice:int = obj["Rpt2DisplayExtPrice"]
      self.Rpt2DisplayServAmt:int = obj["Rpt2DisplayServAmt"]
      self.Rpt2DisplayServLaborRate:int = obj["Rpt2DisplayServLaborRate"]
      self.Rpt2DisplayUnitPrice:int = obj["Rpt2DisplayUnitPrice"]
      self.Rpt3DisplayExtPrice:int = obj["Rpt3DisplayExtPrice"]
      self.Rpt3DisplayServAmt:int = obj["Rpt3DisplayServAmt"]
      self.Rpt3DisplayServLaborRate:int = obj["Rpt3DisplayServLaborRate"]
      self.Rpt3DisplayUnitPrice:int = obj["Rpt3DisplayUnitPrice"]
      self.ScrapQty:int = obj["ScrapQty"]
      self.ShowStatusIcon:str = obj["ShowStatusIcon"]
      self.StdBasisDescription:str = obj["StdBasisDescription"]
      self.StdFormatDescription:str = obj["StdFormatDescription"]
      self.ActSubCost:int = obj["ActSubCost"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorPPZip:str = obj["VendorPPZip"]
      self.VendorPPCity:str = obj["VendorPPCity"]
      self.VendorPPAddress2:str = obj["VendorPPAddress2"]
      self.VendorPPPrimPCon:int = obj["VendorPPPrimPCon"]
      self.VendorPPAddress1:str = obj["VendorPPAddress1"]
      self.VendorPPCountry:str = obj["VendorPPCountry"]
      self.VendorPPState:str = obj["VendorPPState"]
      self.VendorPPName:str = obj["VendorPPName"]
      self.VendorPPAddress3:str = obj["VendorPPAddress3"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.PartsPerOp:int = obj["PartsPerOp"]
      self.PartQty:int = obj["PartQty"]
      self.StockQty:int = obj["StockQty"]
      self.ShippedQty:int = obj["ShippedQty"]
      self.ReceivedQty:int = obj["ReceivedQty"]
      self.WIPQty:int = obj["WIPQty"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.ReservedQty:int = obj["ReservedQty"]
      self.AllocatedQty900:int = obj["AllocatedQty900"]
      self.PickingQty:int = obj["PickingQty"]
      self.PickedQty:int = obj["PickedQty"]
      self.LbrCostBase:int = obj["LbrCostBase"]
      self.MtlCostBase:int = obj["MtlCostBase"]
      self.JobClosed:bool = obj["JobClosed"]
      self.JobComplete:bool = obj["JobComplete"]
      self.Plant:str = obj["Plant"]
      self.PartDescription:str = obj["PartDescription"]
      self.IUM:str = obj["IUM"]
      self.ShipDocReq:bool = obj["ShipDocReq"]
      self.ShipDocAvail:bool = obj["ShipDocAvail"]
      self.MtlList:str = obj["MtlList"]
      self.PreventSugg:bool = obj["PreventSugg"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.OrderQty:int = obj["OrderQty"]
      self.ProcessMode:str = obj["ProcessMode"]
      self.EnableShipDocReq:bool = obj["EnableShipDocReq"]
      self.PartmasterPart:bool = obj["PartmasterPart"]
      self.EnableSugg:bool = obj["EnableSugg"]
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobProdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.ProdQty:int = obj["ProdQty"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.TargetJobNum:str = obj["TargetJobNum"]
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      self.ShippedQty:int = obj["ShippedQty"]
      self.ReceivedQty:int = obj["ReceivedQty"]
      self.WIPQty:int = obj["WIPQty"]
      self.CallNum:int = obj["CallNum"]
      self.CallLine:int = obj["CallLine"]
      self.TFLineNum:str = obj["TFLineNum"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      self.PlanUserID:str = obj["PlanUserID"]
      self.PlanID:str = obj["PlanID"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.WIPToMiscShipment:bool = obj["WIPToMiscShipment"]
      self.RMANum:int = obj["RMANum"]
      self.RMALine:int = obj["RMALine"]
      self.RMAReceipt:int = obj["RMAReceipt"]
      self.RMADisp:int = obj["RMADisp"]
      self.DMRNum:int = obj["DMRNum"]
      self.DMRActionNum:int = obj["DMRActionNum"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.DemandLinkSource:str = obj["DemandLinkSource"]
      self.DemandLinkStatus:str = obj["DemandLinkStatus"]
      self.IUM:str = obj["IUM"]
      self.JHPartDesc:str = obj["JHPartDesc"]
      self.JHPartNum:str = obj["JHPartNum"]
      self.MakeToJobQty:int = obj["MakeToJobQty"]
      self.MakeToStockQty:int = obj["MakeToStockQty"]
      self.MakeToType:str = obj["MakeToType"]
      self.MaxAllowedQty:int = obj["MaxAllowedQty"]
      self.MtlPartDesc:str = obj["MtlPartDesc"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      self.OrdWIPQty:int = obj["OrdWIPQty"]
      self.OurStockQty:int = obj["OurStockQty"]
      self.PullFromStockWarehouseCode:str = obj["PullFromStockWarehouseCode"]
      self.PullFromStockWarehouseDesc:str = obj["PullFromStockWarehouseDesc"]
      self.ShipBy:str = obj["ShipBy"]
      self.SplitQty:int = obj["SplitQty"]
      self.StkWIPQty:int = obj["StkWIPQty"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TotalSplitQuantity:int = obj["TotalSplitQuantity"]
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.Valid:bool = obj["Valid"]
      self.AsmPartDesc:str = obj["AsmPartDesc"]
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      self.CustInactive:bool = obj["CustInactive"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.BitFlag:int = obj["BitFlag"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobResourcesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      self.WhatIf:bool = obj["WhatIf"]
      self.AllocNum:int = obj["AllocNum"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceID:str = obj["ResourceID"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.CalendarName:str = obj["CalendarName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_JobStageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.StageSeq:int = obj["StageSeq"]
      self.StageNumber:str = obj["StageNumber"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.StageNumberDescription:str = obj["StageNumberDescription"]
      self.RowMod:str = obj["RowMod"]
      pass

class Erp_Tablesets_OverrideSchedOrdersRow:
   def __init__(self, obj):
      self.Backwards:bool = obj["Backwards"]
      self.Company:str = obj["Company"]
      self.DaysLate:int = obj["DaysLate"]
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.SchedSeq:int = obj["SchedSeq"]
      self.IsChanged:bool = obj["IsChanged"]
      """  Shows changed records for both cases: where SchedSeq was generated automatically or record was changed by user  """  
      self.StartDate:str = obj["StartDate"]
      self.BatchJob:str = obj["BatchJob"]
      """  Indicate which main job belong a group of jobs.  """  
      self.ParentJob:str = obj["ParentJob"]
      """  Indicate which job is its parent.  """  
      self.MultiJobTopParent:bool = obj["MultiJobTopParent"]
      self.MultiJobSchedSeq:int = obj["MultiJobSchedSeq"]
      self.SchedAsMultiJob:bool = obj["SchedAsMultiJob"]
      self.CurrentRow:bool = obj["CurrentRow"]
      self.IsDecimal:bool = obj["IsDecimal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OverrideSchedOrdersTableset:
   def __init__(self, obj):
      self.OverrideSchedOrders:list[Erp_Tablesets_OverrideSchedOrdersRow] = obj["OverrideSchedOrders"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetCalculateGlobalSchedulingLastRun_input:
   """ Required : 
   companyID
   plantID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      self.plantID:str = obj["plantID"]
      pass

class GetCalculateGlobalSchedulingLastRun_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.multijobFlag:bool = obj["multijobFlag"]
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

class LoadOverrideSchedOrderViewList_input:
   """ Required : 
   jobDs
   ds
   """  
   def __init__(self, obj):
      self.jobDs:list[Erp_Tablesets_JobHeadListTableset] = obj["jobDs"]
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

class LoadOverrideSchedOrderViewList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.jobDs:list[Erp_Tablesets_JobHeadListTableset] = obj["jobDs"]
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadOverrideSchedOrderView_input:
   """ Required : 
   jobDs
   ds
   """  
   def __init__(self, obj):
      self.jobDs:list[Erp_Tablesets_JobEntryTableset] = obj["jobDs"]
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

class LoadOverrideSchedOrderView_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.jobDs:list[Erp_Tablesets_JobEntryTableset] = obj["jobDs"]
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LoadOverrideSched_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

class LoadOverrideSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.WasChanged:bool = obj["WasChanged"]
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MultiJobUpdateSchedPri_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

class MultiJobUpdateSchedPri_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBackwards_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

class OnChangeBackwards_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMultiJobSchedSeq_input:
   """ Required : 
   multiJobSchedSeqOld
   currentJobNum
   ds
   """  
   def __init__(self, obj):
      self.multiJobSchedSeqOld:int = obj["multiJobSchedSeqOld"]
      self.currentJobNum:str = obj["currentJobNum"]
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

class OnChangeMultiJobSchedSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingSchedSeq_input:
   """ Required : 
   proposedValue
   schedAsMultiJob
   multiJobTopParent
   jobNum
   """  
   def __init__(self, obj):
      self.proposedValue:int = obj["proposedValue"]
      self.schedAsMultiJob:bool = obj["schedAsMultiJob"]
      self.multiJobTopParent:bool = obj["multiJobTopParent"]
      self.jobNum:str = obj["jobNum"]
      pass

class OnChangingSchedSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.askChangeSequenceOfSelectedJobOutsideOfItsGroup:bool = obj["askChangeSequenceOfSelectedJobOutsideOfItsGroup"]
      self.isDecimal:bool = obj["isDecimal"]
      pass

      """  output parameters  """  

class RefreshOverrideSchedOrderView_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

class RefreshOverrideSchedOrderView_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SeqIsDecimal_input:
   """ Required : 
   multiJobSchedSeq
   """  
   def __init__(self, obj):
      self.multiJobSchedSeq:int = obj["multiJobSchedSeq"]
      pass

class SeqIsDecimal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isDecimal:bool = obj["isDecimal"]
      pass

      """  output parameters  """  

class UpdateSchedPri_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

class UpdateSchedPri_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OverrideSchedOrdersTableset] = obj["ds"]
      pass

      """  output parameters  """  

