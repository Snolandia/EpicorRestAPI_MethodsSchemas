import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JobClosingSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AllowCloseJob(epicorHeaders = None):
   """  
   Summary: Invoke method AllowCloseJob
   Description: This method exists soley for the purpose of allowing security for
availability of the close job field to be defined.
   OperationID: AllowCloseJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowCloseJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_CloseJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseJob
   Description: Call this method to close or complete the job.  The Job database is not updated
till this method is successfully executed.
   OperationID: CloseJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EnableSerialMatching(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EnableSerialMatching
   Description: Call this method when it is necessary to know in UI if the Serial Matching option should be enabled.
   OperationID: EnableSerialMatching
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableSerialMatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableSerialMatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobClosing(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobClosing
   Description: Returns a new , empty Call JobClosingDataSet row.
   OperationID: GetNewJobClosing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobClosing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobClosing_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobClosingList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobClosingList
   Description: This method creates a new JobClosingListDataSet row entry.
   OperationID: GetNewJobClosingList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobClosingList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobClosingList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobClosed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobClosed
   Description: Call this method when the value of Epicor.Mfg.BO.JobClosingDataSet.JobClosed changes.
   OperationID: OnChangeJobClosed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobClosed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobClosed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobCompletion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobCompletion
   Description: Call this method when the value of Epicor.Mfg.BO.JobClosingDataSet.JobComplete changes.
   OperationID: OnChangeJobCompletion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobCompletion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobCompletion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobNum
   Description: Call this method when the user selects a job.  This method populates
the Epicor.Mfg.BO.JobClosingDataSet dataset with Job , JobOper and JobMtl information.
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreCloseJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreCloseJob
   Description: This method will return a record in the LegalNumberGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreCloseJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCloseJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCloseJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectMultipleJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectMultipleJob
   Description: Call this method when the user selects multiple jobs.  This method populates
the Epicor.Mfg.BO.JobClosingDataSet dataset with Job , JobOper and JobMtl information.
   OperationID: SelectMultipleJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectMultipleJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectMultipleJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectJobByJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectJobByJobNum
   Description: Call this method when the user selects multiple jobs.  This method populates
the Epicor.Mfg.BO.JobClosingDataSet dataset with Job , JobOper and JobMtl information.
   OperationID: SelectJobByJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectJobByJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectJobByJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AllowCloseJob_output:
   def __init__(self, obj):
      pass

class CloseJob_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      pass

class CloseJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class EnableSerialMatching_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      pass

class EnableSerialMatching_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      self.plEnable:bool = obj["plEnable"]
      pass

      """  output parameters  """  

class Erp_Tablesets_JobClosingListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.JobNum:str = obj["JobNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobClosingListTableset:
   def __init__(self, obj):
      self.JobClosingList:list[Erp_Tablesets_JobClosingListRow] = obj["JobClosingList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobClosingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date the Job was closed.  Defaults as the system but can be overridden.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      """  The date that production was completed for this Job.  Maintained via Job Completion Processing.  """  
      self.PrintProductionDetail:bool = obj["PrintProductionDetail"]
      self.BackFlush:bool = obj["BackFlush"]
      self.StockQty:int = obj["StockQty"]
      self.OrderQty:int = obj["OrderQty"]
      self.ReceivedToStockQty:int = obj["ReceivedToStockQty"]
      self.ShippedQty:int = obj["ShippedQty"]
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.CompleteQty:int = obj["CompleteQty"]
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.CanPrintProfitInfo:bool = obj["CanPrintProfitInfo"]
      self.BackFlushProcessing:bool = obj["BackFlushProcessing"]
      """  If this field value is yes and backflush check box is yes then perform backflush processing in the backend.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.UserAllowedToCloseJob:bool = obj["UserAllowedToCloseJob"]
      self.MultiplePlant:bool = obj["MultiplePlant"]
      """  Yes means the Job uses work centers from multiple plants.  """  
      self.MultiplePlantContinue:int = obj["MultiplePlantContinue"]
      """  User response to job uses Multiple plant  """  
      self.PendingInspection:bool = obj["PendingInspection"]
      self.PendingInspectionContinue:int = obj["PendingInspectionContinue"]
      self.QuantityContinue:int = obj["QuantityContinue"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.JobUOM:str = obj["JobUOM"]
      self.BitFlag:int = obj["BitFlag"]
      self.OpenDMR:bool = obj["OpenDMR"]
      self.OpenDMRContinue:bool = obj["OpenDMRContinue"]
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableWIPCleared:bool = obj["EnableWIPCleared"]
      """  Flag to indicate whether WIPCleared column should be enabled  """  
      self.ReceivedToJobQty:int = obj["ReceivedToJobQty"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobClosingTableset:
   def __init__(self, obj):
      self.JobClosing:list[Erp_Tablesets_JobClosingRow] = obj["JobClosing"]
      self.JobMtl:list[Erp_Tablesets_JobMtlRow] = obj["JobMtl"]
      self.JobOper:list[Erp_Tablesets_JobOperRow] = obj["JobOper"]
      self.JobPart:list[Erp_Tablesets_JobPartRow] = obj["JobPart"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  """  
      self.Description:str = obj["Description"]
      """  A description of the material.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity per parent.  Field Service was EstQty in FSCallMt.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  The unit used to measure the material.  """  
      self.LeadTime:int = obj["LeadTime"]
      """   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvageable material.  Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Job Material.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      """  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  """  
      self.SalvageCredit:int = obj["SalvageCredit"]
      """  Total salvage credit to date.  A summary of salvage receipt transactions.  """  
      self.SalvageMtlBurCredit:int = obj["SalvageMtlBurCredit"]
      """  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  """  
      self.MfgComment:str = obj["MfgComment"]
      """   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  """  
      self.BuyIt:bool = obj["BuyIt"]
      """  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  """  
      self.Ordered:bool = obj["Ordered"]
      """  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  """  
      self.PurComment:str = obj["PurComment"]
      """   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  """  
      self.BackFlush:bool = obj["BackFlush"]
      """   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.SndAlrtCmpl:bool = obj["SndAlrtCmpl"]
      """  Controls if an alert is to be sent when this JobMtl is completed.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.SalvageMtlCredit:int = obj["SalvageMtlCredit"]
      """  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageLbrCredit:int = obj["SalvageLbrCredit"]
      """  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageBurCredit:int = obj["SalvageBurCredit"]
      """  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageSubCredit:int = obj["SalvageSubCredit"]
      """  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this Material belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this material relates to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  FS - Unit Price for the Material in base currency.  """  
      self.BillableUnitPrice:int = obj["BillableUnitPrice"]
      """  FS - Billable Unit Price for the Material in base currency.  """  
      self.DocBillableUnitPrice:int = obj["DocBillableUnitPrice"]
      """  FS - Billable Price per unit for the material in customers currency.  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  """  
      self.Billable:bool = obj["Billable"]
      """  Is this a billable material item.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Holds the quantity of the item that has been shipped through misc.  shipments  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  FS - Unit Price for the Material in Customer currency.  """  
      self.QtyStagedToDate:int = obj["QtyStagedToDate"]
      """  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  """  
      self.AddedMtl:bool = obj["AddedMtl"]
      """  This material was added after initial setup of the job  """  
      self.MiscCharge:bool = obj["MiscCharge"]
      """  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  """  
      self.SCMiscCode:str = obj["SCMiscCode"]
      """  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.WIReqDate:str = obj["WIReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.Rpt1BillableUnitPrice:int = obj["Rpt1BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2BillableUnitPrice:int = obj["Rpt2BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3BillableUnitPrice:int = obj["Rpt3BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.BaseRequiredQty:int = obj["BaseRequiredQty"]
      """   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  """  
      self.Weight:int = obj["Weight"]
      """  Material Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Material Weight UOM defaulted from Part Master.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.SalvageEstMtlUnitCredit:int = obj["SalvageEstMtlUnitCredit"]
      """   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstLbrUnitCredit:int = obj["SalvageEstLbrUnitCredit"]
      """   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstBurUnitCredit:int = obj["SalvageEstBurUnitCredit"]
      """   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstSubUnitCredit:int = obj["SalvageEstSubUnitCredit"]
      """   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.LoanedQty:int = obj["LoanedQty"]
      """  The material quantity that has been loaned out to another job.  """  
      self.BorrowedQty:int = obj["BorrowedQty"]
      """  The material quantity that has been borrowed from another job.  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  """  
      self.GeneralPlanInfo:str = obj["GeneralPlanInfo"]
      """  GeneralPlanInfo  """  
      self.EstStdDescription:str = obj["EstStdDescription"]
      """  EstStdDescription  """  
      self.PricingUOM:str = obj["PricingUOM"]
      """  PricingUOM  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.IsPOCostingMaintained:bool = obj["IsPOCostingMaintained"]
      """  IsPOCostingMaintained  """  
      self.EstStdType:int = obj["EstStdType"]
      """  EstStdType  """  
      self.POCostingFactor:int = obj["POCostingFactor"]
      """  POCostingFactor  """  
      self.PlannedQtyPerUnit:int = obj["PlannedQtyPerUnit"]
      """  PlannedQtyPerUnit  """  
      self.POCostingDirection:int = obj["POCostingDirection"]
      """  POCostingDirection  """  
      self.POCostingUnitVal:int = obj["POCostingUnitVal"]
      """  POCostingUnitVal  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.OrigGroupSeq:int = obj["OrigGroupSeq"]
      """  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.ShowStatusIcon:str = obj["ShowStatusIcon"]
      """  ShowStatusIcon  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  """  
      self.StagingLotNum:str = obj["StagingLotNum"]
      """  Stores the lot number of the material in the Staging Warehouse/Bin.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.LocationView:bool = obj["LocationView"]
      """  Controls if this material record is viewable in Location Management or the web.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.SalvageAttributeSetID:int = obj["SalvageAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SalvagePlanningNumberOfPieces:int = obj["SalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvagePlanningAttributeSetID:int = obj["SalvagePlanningAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RelatedStage:str = obj["RelatedStage"]
      """  The identification of related StageNo.  """  
      self.SalvageRevisionNum:str = obj["SalvageRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PartAllocQueueAction:str = obj["PartAllocQueueAction"]
      """  Indicates if the job material should be added or removed from the fulfillment queue.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job material is ready to be fulfilled.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  The currency switch flag  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DisplayExtPrice:int = obj["DisplayExtPrice"]
      """  The display of extended price.  """  
      self.DisplayUnitPrice:int = obj["DisplayUnitPrice"]
      """  The display unit price.  """  
      self.DocDisplayExtPrice:int = obj["DocDisplayExtPrice"]
      """  The document display extended price  """  
      self.DocDisplayUnitPrice:int = obj["DocDisplayUnitPrice"]
      """  The document display extended price  """  
      self.dspBuyIt:bool = obj["dspBuyIt"]
      """  BuyIt field for display in the UI.  """  
      self.DspIUM:str = obj["DspIUM"]
      """  Display IUM (readonly)  """  
      self.EnableBackflush:bool = obj["EnableBackflush"]
      """  Should the backflush field be enabled?  """  
      self.EnableBuyIt:bool = obj["EnableBuyIt"]
      """  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  """  
      self.EnableConfigure:bool = obj["EnableConfigure"]
      """  flag to determine whether the Configure Option should be enabled.  """  
      self.EnableDirect:bool = obj["EnableDirect"]
      """  flag to determine whether the Make Direct field should be enabled.  """  
      self.EnableFixedQty:bool = obj["EnableFixedQty"]
      """  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  """  
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.EnableRcvInspReq:bool = obj["EnableRcvInspReq"]
      """  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  """  
      self.EnableSndAlrtCmpl:bool = obj["EnableSndAlrtCmpl"]
      """  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  """  
      self.EnableSplitCosts:bool = obj["EnableSplitCosts"]
      """  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  """  
      self.EstCost:int = obj["EstCost"]
      """  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  """  
      self.IPCaller:str = obj["IPCaller"]
      """  The name of the calling program  """  
      self.IsBaseCurrency:bool = obj["IsBaseCurrency"]
      """  IsBaseCurrency  """  
      self.IsMtlConfigurationOn:bool = obj["IsMtlConfigurationOn"]
      self.IsMtlConfigureOn:bool = obj["IsMtlConfigureOn"]
      self.IsMtlExtConfig:bool = obj["IsMtlExtConfig"]
      self.IsMtlRevisionApproved:bool = obj["IsMtlRevisionApproved"]
      """  IsMtlRevisionApproved  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if current Part is an Inventory Part.  """  
      self.PlantList:str = obj["PlantList"]
      """  Calculated field gets list of available Sites  """  
      self.PricePerCodeDescription:str = obj["PricePerCodeDescription"]
      """  Price Per Code Description  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      """  The description of the related operation  """  
      self.RetainValues:bool = obj["RetainValues"]
      """  Logical used to determine if record is created from PO Entry.  """  
      self.Rpt1DisplayExtPrice:int = obj["Rpt1DisplayExtPrice"]
      self.Rpt1DisplayUnitPrice:int = obj["Rpt1DisplayUnitPrice"]
      self.Rpt2DisplayExtPrice:int = obj["Rpt2DisplayExtPrice"]
      self.Rpt2DisplayUnitPrice:int = obj["Rpt2DisplayUnitPrice"]
      self.Rpt3DisplayExtPrice:int = obj["Rpt3DisplayExtPrice"]
      self.Rpt3DisplayUnitPrice:int = obj["Rpt3DisplayUnitPrice"]
      self.SalvageBaseUOM:str = obj["SalvageBaseUOM"]
      """  BaseUOM for SalvagePartNum  """  
      self.ShowInspRqdImg:bool = obj["ShowInspRqdImg"]
      """  Satatus of InspectionRequired image on JobMaterial form.  """  
      self.SubContract:bool = obj["SubContract"]
      """  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  """  
      self.AllowBackflushUncheck:bool = obj["AllowBackflushUncheck"]
      """  Can the backflush be unchecked?  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.EnableSalvageAttributeSetSearch:bool = obj["EnableSalvageAttributeSetSearch"]
      self.PlanningNumberOfPiecesDisp:int = obj["PlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts  """  
      self.SalvagePlanningNumberOfPiecesDisp:int = obj["SalvagePlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.SkipUnitPriceCalc:bool = obj["SkipUnitPriceCalc"]
      """  Indicates if unit price calculation should occur.  When false the unit price will be calculated.  When false the unit price will remain its current value.  """  
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      """  Error Status Display  """  
      self.InPartAllocQueue:bool = obj["InPartAllocQueue"]
      """  True if this job material is in the fulfillment queue.  """  
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.SelectedForAction:bool = obj["SelectedForAction"]
      """  Indicates this row is selected for action.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  The allocated quantity for this job material.  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  The reserved quantity for this job material.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      """  The available quantity for this job material.  """  
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
      """  RowMod  """  
      pass

class Erp_Tablesets_JobOperRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobOper records are also marked.  This is used to make database access to open operation records more efficient.  """  
      self.OpComplete:bool = obj["OpComplete"]
      """   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this Operation is associated with.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID.  This links the JobOper to the OpStd master file.  This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.QueStartDate:str = obj["QueStartDate"]
      """  Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  """  
      self.QueStartHour:int = obj["QueStartHour"]
      """  Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  """  
      self.MoveDueDate:str = obj["MoveDueDate"]
      """  Scheduled move due date. Not directly maintainable, updated via the scheduling process.  """  
      self.MoveDueHour:int = obj["MoveDueHour"]
      """  Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  Labor rate used for estimated production labor costs. Default from the OpMaster.ProdLabRate.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Labor rate for estimated setup labor costs. Default from the OpMaster.SetupLabRate.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.ProdBurRate.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.SetupBurRate.  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  This indicates if this is an "added operation". An added operation is one that was not planned on.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.ProdComplete:bool = obj["ProdComplete"]
      """  A flag indicating if the production is complete for this operation. It is updated via Labor Entry.  """  
      self.SetupComplete:bool = obj["SetupComplete"]
      """  Flag that indicates if Setup is complete on this operation. This flag is only used when the operation has EstSetupHours > 0.00.  """  
      self.ActProdHours:int = obj["ActProdHours"]
      """  Total Actual Production Hours. A summary of non-setup LaborDtl.BurdenHrs. This includes REWORK hours.  This is maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActReworkHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H").  """  
      self.ActProdRwkHours:int = obj["ActProdRwkHours"]
      """  Total Actual Production Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "P" and Rework = Yes. This number is also included as part of the JobOPer.ActProdHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActProdHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  """  
      self.ActSetupHours:int = obj["ActSetupHours"]
      """  Actual setup hours.  A summary of setup (LaborDtl.LaborType = S) labor transactions hours (LaborDtl.Burden). Actual Setup hours reduce the shop load if the system is configured to remove load based on hours (JCSyst.RemoveLoad = "H").  """  
      self.ActSetupRwkHours:int = obj["ActSetupRwkHours"]
      """  Total Actual Setup Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "S" and Rework = Yes. This number is also included as part of the JobOPer.ActSetupHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActSetHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Setup function percent complete.  Maintained via labor entry.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Inventory UOM  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  """  
      self.Description:str = obj["Description"]
      """  Description used only for subcontract operations  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.RunQty:int = obj["RunQty"]
      """   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID. When not blank it indicates that the operations schedule has been changed and is considered as being in a "What If" mode.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIMachines:int = obj["WIMachines"]
      """  This is the What-If number of machines that this operation will run on at the same time.  Setup by and for scheduling from the Machines field.  """  
      self.WIQueStartDate:str = obj["WIQueStartDate"]
      """  What-if Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  """  
      self.WIQueStartHour:int = obj["WIQueStartHour"]
      """  What-if Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  What if Scheduled production start date. Not directly maintainable, updated via the scheduling process.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling. It represents the What If "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  What If Scheduled production due date. Not directly maintainable, updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  """  
      self.WIMoveDueDate:str = obj["WIMoveDueDate"]
      """  What-If Scheduled move due date. Not directly maintainable, updated via the scheduling process.  """  
      self.WIMoveDueHour:int = obj["WIMoveDueHour"]
      """  What-if Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  """  
      self.WIHoursPerMachine:int = obj["WIHoursPerMachine"]
      """  The Number of Hours per machine per day that this operations "What If" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining ShopLoad records.  """  
      self.WILoadDate:str = obj["WILoadDate"]
      """  Date at which the operations current outstanding "What-If" load starts at.  Updated by the JobOper write trigger. (See LoadDate)  """  
      self.WILoadHour:int = obj["WILoadHour"]
      """  "Hour offset from the beginning of the work day" for the operations outstanding "What-If"  load. Related to WILoadDate.  """  
      self.ActBurCost:int = obj["ActBurCost"]
      """  Total Burden cost to date. This is update via the LaborDtl\Write.p trigger procedure. It includes ALL burden costs (Setup, Production and Rework)  """  
      self.ActLabCost:int = obj["ActLabCost"]
      """   FOR NON-SUBCONTRACT OPERATIONS: Total of "ALL" labor costs to date. This includes Setup, Production and Rework. Updated via the LaborDtl.Write.p trigger.
FOR SUBCONTRACT OPERATIONS: The Total Cost, updated via the receipt process.  """  
      self.ReworkBurCost:int = obj["ReworkBurCost"]
      """  Total Rework Burden cost todate. This value is also included in the ActBurCost total. It includes both setup & production rework. Updated via LaborDtl\Write.P trigger.  """  
      self.ReworkLabCost:int = obj["ReworkLabCost"]
      """  Total Rework Labor cost to date. This value is also included in the ActLabCost field. This includes both Setup & Production. Updated via the LaborDtl\Write.p trigger.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  """  
      self.HoursPerMachine:int = obj["HoursPerMachine"]
      """  The Number of Hours per machine per day that this operations "actual" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining the ShopLoad records.  """  
      self.LoadDate:str = obj["LoadDate"]
      """   Date at which the operations current outstanding load starts at.
Ex: Op schedule is 2/1/97 - 2/10/97, initially LoadDate = 2/1/97. As load is relieved through labor processing the LoadDate moves forward accordingly. When 1/2 completed the LoadDate would be 2/5/97. This field is primarily used by the Scheduling Board to calculate the graphical image of outstanding load.  Updated by the JobOper write trigger.  """  
      self.LoadHour:int = obj["LoadHour"]
      """  "Hour offset from the beginning of the work day" for the operations outstanding load. Related to LoadDate.  """  
      self.ReloadNum:int = obj["ReloadNum"]
      """  Internally used field to prevent redundant read of JobOper during execution of "Reloader" program. (See WrkCenter.ReloadNum)  """  
      self.SndAlrtCmpl:bool = obj["SndAlrtCmpl"]
      """  Controls if an alert is to be sent when this JobOper is completed.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required when items are received to this JobOper (subcontract only). Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Identical to JobHead.JobEngineered.  ShopLoad capacity is only allocated to Jobs where JobEngineered = YES.  """  
      self.EstSetHoursPerMch:int = obj["EstSetHoursPerMch"]
      """   The estimated set up hours per machine.
Default from OpStd.SetupHours.  Used to calculate JobOper.EstSetupHours.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """   Part Revision number.
Pertains to subcontracting operations only.   An optional field.   Related JobAsmbl.RevisionNum is used as the default.  """  
      self.AutoReceiptDate:str = obj["AutoReceiptDate"]
      """  Currently not used. Prep for future development.  """  
      self.LastLaborDate:str = obj["LastLaborDate"]
      """  The labor date of the last labor transaction that was posted to this operation.  Used by the JobOper write trigger Auto Receieve logic.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this operation belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this operation relates to.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate used for  time on an operation.  Time per hour per technician. in base currency.  """  
      self.BillableLaborRate:int = obj["BillableLaborRate"]
      """  Billable Labor rate used for  time on a service.  Time per hour per technician. in base currency. This field considers the percentage coverage of a warranty or contract.  """  
      self.DocLaborRate:int = obj["DocLaborRate"]
      """  Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. Does not consider warranty or contract  """  
      self.DocBillableLaborRate:int = obj["DocBillableLaborRate"]
      """  Billable Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. considers warranty or contract  """  
      self.Billable:bool = obj["Billable"]
      """  FS - Is this a billable operation.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  FS - Unit Price for the subcontract in base currency.  """  
      self.BillableUnitPrice:int = obj["BillableUnitPrice"]
      """  FS - Billable Unit Price for the subcontract in base currency.  """  
      self.DocBillableUnitPrice:int = obj["DocBillableUnitPrice"]
      """  FS - Billable Price per unit for the subcontract in customers currency.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  FS - Unit Price for the for the Subcontract in Customer currency.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.QtyStagedToDate:int = obj["QtyStagedToDate"]
      """  The "to date" quantity that has been moved to the input Warehouse/Bin of the subsequent operations ResourceGroup/Resource input Warehouse/Bin.  This is NOT A balance.  It is a "to date" value.  It is not reduced as it is consumed.  Used in calculation of "Outstanding" WIP in the Request Material/WIP program (ame30-dg.w).  Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the WIP material in/out of the staging area (Issues, Returns).  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this job operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this job subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary JobOpDtl to be used for setup.  The setup time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary JobOpDtl to be used for production.  The production run time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = P or B.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.KitDate:str = obj["KitDate"]
      """  Kit Date. Not directly maintanable. Updated via the scheduling process.  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.BookedUnitCost:int = obj["BookedUnitCost"]
      """  Booked Unit Cost  """  
      self.RecalcExpProdYld:bool = obj["RecalcExpProdYld"]
      """   Initially defaulted to false. This flag is set to true at the time JobOper.ProdComplete is set to true if JobHead.ProductionYield = true and OpMaster. PrdYldRecalcExpected = true and the actual completed qty for the operation vs. the expected completion qty is out of variance based on the under percentage set in OpMaster. This flag is used by the production yield recalculation logic to determine if recalculation is required for a job.
This field is maintained by the system only.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.RoughCutSched:bool = obj["RoughCutSched"]
      """  When true this would signify that this operation was rough cut scheduled - meaning the operation would have start and end dates but no supporting resourcetimeused or shopload records.  """  
      self.SchedComment:str = obj["SchedComment"]
      """  Scheduling Comments  """  
      self.Rpt1BillableLaborRate:int = obj["Rpt1BillableLaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt2BillableLaborRate:int = obj["Rpt2BillableLaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt3BillableLaborRate:int = obj["Rpt3BillableLaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt1BillableUnitPrice:int = obj["Rpt1BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2BillableUnitPrice:int = obj["Rpt2BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3BillableUnitPrice:int = obj["Rpt3BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1LaborRate:int = obj["Rpt1LaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt2LaborRate:int = obj["Rpt2LaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt3LaborRate:int = obj["Rpt3LaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      """  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  """  
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      """  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  """  
      self.Weight:int = obj["Weight"]
      """  Operation Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Operation Weight UOM defaulted from Part Master.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.TearDwnEndDate:str = obj["TearDwnEndDate"]
      """  Scheduled tear down start date. The start date would be the production end date.  """  
      self.TearDwnEndHour:int = obj["TearDwnEndHour"]
      """  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  """  
      self.WITearDwnEndDate:str = obj["WITearDwnEndDate"]
      """  Scheduled tear down start date. The start date would be the production end date.  """  
      self.WITearDwnEndHour:int = obj["WITearDwnEndHour"]
      """  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      self.AssetPartNum:str = obj["AssetPartNum"]
      """  The PartNum for the asset. This should be disabled for a service call job, in which case the asset information would be transferred from the service call line when an operation is created for the job.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the asset.  """  
      self.ActualStartDate:str = obj["ActualStartDate"]
      """  ActualStartDate  """  
      self.ActualStartHour:int = obj["ActualStartHour"]
      """  ActualStartHour  """  
      self.ActualEndDate:str = obj["ActualEndDate"]
      """  ActualEndDate  """  
      self.ActualEndHour:int = obj["ActualEndHour"]
      """  ActualEndHour  """  
      self.FSJobStatus:int = obj["FSJobStatus"]
      """  FSJobStatus  """  
      self.Instructions:str = obj["Instructions"]
      """  Instructions  """  
      self.ProdUOM:str = obj["ProdUOM"]
      """  ProdUOM  """  
      self.GeneralPlanInfo:str = obj["GeneralPlanInfo"]
      """  GeneralPlanInfo  """  
      self.EstStdDescription:str = obj["EstStdDescription"]
      """  EstStdDescription  """  
      self.JDFOpCompleted:bool = obj["JDFOpCompleted"]
      """  JDFOpCompleted  """  
      self.RemovedfromPlan:bool = obj["RemovedfromPlan"]
      """  RemovedfromPlan  """  
      self.EstStdType:int = obj["EstStdType"]
      """  EstStdType  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PctReg:int = obj["PctReg"]
      """  PctReg  """  
      self.SetupMaterial:int = obj["SetupMaterial"]
      """  SetupMaterial  """  
      self.MaterialColorRating:int = obj["MaterialColorRating"]
      """  MaterialColorRating  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.ExpPctUp:int = obj["ExpPctUp"]
      """  ExpPctUp  """  
      self.ExpCycTm:int = obj["ExpCycTm"]
      """  ExpCycTm  """  
      self.ExpGood:int = obj["ExpGood"]
      """  ExpGood  """  
      self.NonProdLimit:int = obj["NonProdLimit"]
      """  NonProdLimit  """  
      self.AutoSpcEnable:bool = obj["AutoSpcEnable"]
      """  AutoSpcEnable  """  
      self.AutoSpcPeriod:int = obj["AutoSpcPeriod"]
      """  AutoSpcPeriod  """  
      self.PartQualEnable:bool = obj["PartQualEnable"]
      """  PartQualEnable  """  
      self.AutoSpcSubgroup:int = obj["AutoSpcSubgroup"]
      """  AutoSpcSubgroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MobileOperation:bool = obj["MobileOperation"]
      """  MobileOperation  """  
      self.ReWork:bool = obj["ReWork"]
      """  ReWork  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  RequestMove  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.PrinterID:str = obj["PrinterID"]
      """  PrinterID  """  
      self.LastPrintedDate:str = obj["LastPrintedDate"]
      """  LastPrintedDate  """  
      self.LastPCIDPrinted:str = obj["LastPCIDPrinted"]
      """  LastPCIDPrinted  """  
      self.CurrentPkgCode:str = obj["CurrentPkgCode"]
      """  CurrentPkgCode  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The identification of related StageNo.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.ActScrapQty:int = obj["ActScrapQty"]
      """  The sum of LaborDtl ScrapQty for this operation.  """  
      self.AutoReceive:bool = obj["AutoReceive"]
      """  Auto receive flag  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  The currency switch flag.  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DisplayExtPrice:int = obj["DisplayExtPrice"]
      self.DisplayServAmt:int = obj["DisplayServAmt"]
      """  The display service amount.  """  
      self.DisplayServLaborRate:int = obj["DisplayServLaborRate"]
      """  The display service labor rate  """  
      self.DisplayUnitPrice:int = obj["DisplayUnitPrice"]
      """  Calculated display unit price  """  
      self.DocDisplayExtPrice:int = obj["DocDisplayExtPrice"]
      """  The document display extended price  """  
      self.DocDisplayServAmt:int = obj["DocDisplayServAmt"]
      """  The converted display service amount.  """  
      self.DocDisplayServLaborRate:int = obj["DocDisplayServLaborRate"]
      """  The converted display service labor rate.  """  
      self.DocDisplayUnitPrice:int = obj["DocDisplayUnitPrice"]
      """  The document display unit price  """  
      self.DspIUM:str = obj["DspIUM"]
      """  Display IUM field (readonly)  """  
      self.EnableAutoReceive:bool = obj["EnableAutoReceive"]
      """  Field to determine to enable or disable autoreceive.  """  
      self.EnableSndAlrtCmpl:bool = obj["EnableSndAlrtCmpl"]
      """  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  """  
      self.EnableSNReqSubConShip:bool = obj["EnableSNReqSubConShip"]
      """  This external field is used as a flag to determine when to enable/disable the SNRequiredSubConShip field on UI screen.  """  
      self.EnableSNRequiredOpr:bool = obj["EnableSNRequiredOpr"]
      self.EstBurdenCost:int = obj["EstBurdenCost"]
      """  For non subconctract operations JobOper.EstSetHours * JobOper.SetupBurRate + JobOper.EstProdHours * JobOper.ProdBurRate  """  
      self.EstLabHours:int = obj["EstLabHours"]
      """  The calculated estimated labor hours  """  
      self.EstLaborCost:int = obj["EstLaborCost"]
      """  For non subcontract operations : JobOper.EstSetHours * JobOper.SetupCrewSize * JobOper.SetupLabRate +JobOper.EstProdHours * JobOper.ProdCrewSize * JobOper.ProdLabRate  """  
      self.EstSubCost:int = obj["EstSubCost"]
      """  For SubContract operations: JobOper.EstUnitCost * JobOper.RunQty  """  
      self.FinalOpr:bool = obj["FinalOpr"]
      """  Final operation  """  
      self.IsBaseCurrency:bool = obj["IsBaseCurrency"]
      """  IsBaseCurrency  """  
      self.LaborEntryMethodDesc:str = obj["LaborEntryMethodDesc"]
      """  This is the description of the Method for Labor Entry.  Can be "Time and Quantity" for 'T', "Quantity Only" for 'Q', "Backflush" for 'B' or "Time and Backflush Qty" for 'X'  """  
      self.LoadHrs:int = obj["LoadHrs"]
      """  The total Load Hours calculated by summing the SetUpLoadHrs + ProdLoadHrs.  """  
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.PrimaryProdOpDtlDesc:str = obj["PrimaryProdOpDtlDesc"]
      """  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.PrimaryResourceGrpDesc:str = obj["PrimaryResourceGrpDesc"]
      """  Primary Resource Group Description  """  
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      """  The Resource Group ID of the primary production operation detail.  """  
      self.PrimarySetupOpDtlDesc:str = obj["PrimarySetupOpDtlDesc"]
      """  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.ProductionQty:int = obj["ProductionQty"]
      """  The calculated production quantity  """  
      self.RefreshResources:bool = obj["RefreshResources"]
      """  Indicates if the scheduling resources should be refreshed when the op code changes.  """  
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
      """  The calculated scrap quantity  """  
      self.ShowStatusIcon:str = obj["ShowStatusIcon"]
      """  Contains the value of which icon to display in tree for joboper  """  
      self.StdBasisDescription:str = obj["StdBasisDescription"]
      """  StdBasis Description  """  
      self.StdFormatDescription:str = obj["StdFormatDescription"]
      """  StdFormat Description  """  
      self.ActSubCost:int = obj["ActSubCost"]
      """  For SubContract Operations equals to the ActLaborCost  """  
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
      """  RowMod  """  
      pass

class Erp_Tablesets_JobPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number. Used in tying record back to its parent JobHead record.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.PartsPerOp:int = obj["PartsPerOp"]
      """   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  """  
      self.PartQty:int = obj["PartQty"]
      """   The number of individual parts that are being produced
part. Sum of all related JobProd.ProdQty.
Not Directly maintable.  """  
      self.StockQty:int = obj["StockQty"]
      """  Part Qty that is being produced for Stock.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """   Total Quantity of the end part shipped from this job.
Updated via the ShipDtl write triggers.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """   Total quantity received to stock for the end part of the Job.
Updated via the Manufacturing receipts process.  """  
      self.WIPQty:int = obj["WIPQty"]
      """   Represents the "outstanding" WIP of production quantity.
A summary of JobProd.WIPQty, updated via JobProd write trigger.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Part Production quantity completed.
Updated via JobOper write trigger or LaborPart trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  Quantity of the job completed quantity that is "Reserved" for the linked demands (sales orders/other jobs). Summary of PartAlloc.ReservedQty where PartAlloc.SupplyJobNum = JobHead.JobNum.  Reservations for Orders are made via the Order Allocations program. They are excluded from available quantity calculations for the job. Available Quantity = JobHead.QtyCompleted - (Shipped + Received to stk + ReservedAllocQty + PickingQty + PickedQty).  Maintained via PartAlloc write trigger.  """  
      self.AllocatedQty900:int = obj["AllocatedQty900"]
      """  Total Allocated Quantity for this job part  """  
      self.PickingQty:int = obj["PickingQty"]
      """  Quantity of the job completed quantity that is considered as in the "Picking" process for the linked sales orders. Summary of PartAlloc.PickingQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickingQty is set in the Order Allocation program. Maintained via PartAlloc write trigger.  """  
      self.PickedQty:int = obj["PickedQty"]
      """  Quantity of the job completed quantity that is considered as in the shipping "Staging" process for the linked sales orders. Summary of PartAlloc.PickedQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickedQty is updated when the material move moves the item to the staging area.  Maintained via PartAlloc write trigger.  """  
      self.LbrCostBase:int = obj["LbrCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.MtlCostBase:int = obj["MtlCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  Mirror image of JobHead.JobClosed. Duplicated for performance reasons  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.   Mirror image of JobHead.JobClosed. Duplicated for performance reasons  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  Mirror image of JobHead.Site. Duplicated for performance reasons  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  """  
      self.ShipDocReq:bool = obj["ShipDocReq"]
      """   Shipping Documents Required.
Indicates if shipping documents are required when shipping this part from the Job. Pertains to Job Shipments only and only if the PartNum does not exist in the PartTable. If it does exist then the Part.ShipDocReq. If checked, then at the time of shipping the system will require that the JobPart.ShipDocsAvail flag is true before allowing the shipment.Requires DocManagement license.  """  
      self.ShipDocAvail:bool = obj["ShipDocAvail"]
      """   Required Shipping Documents Available.
A flag manually set by the user to indicate that the required documents for the Job Part  are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Job Part.  If the Part.ShipDocReq = yes  then JobPart.ShipDocsA vail must = yes before the system will allow shipment of the Part from the job.Requires DocManagement license.  """  
      self.MtlList:str = obj["MtlList"]
      """  List of materials that us this part as cost base  """  
      self.PreventSugg:bool = obj["PreventSugg"]
      """  Indicates that MRP should not create job suggestions for the specified co-part  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.OrderQty:int = obj["OrderQty"]
      self.ProcessMode:str = obj["ProcessMode"]
      """  The value of the JobHead.ProcessMode  """  
      self.EnableShipDocReq:bool = obj["EnableShipDocReq"]
      """  Indicates if ShipDocReq is enabled. Only if JobPart.PartNum does not exist in Part Table and if Document Management is installed.  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      """  Logical field signifying whether JobPart.PartNum is a valid part master part.  """  
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
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetNewJobClosingList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingListTableset] = obj["ds"]
      pass

class GetNewJobClosingList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewJobClosing_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      pass

class GetNewJobClosing_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
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

class OnChangeJobClosed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      pass

class OnChangeJobClosed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobCompletion_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      pass

class OnChangeJobCompletion_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobNum_input:
   """ Required : 
   pcJobNum
   ds
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job # selected  """  
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      pass

class OnChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreCloseJob_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      pass

class PreCloseJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
      pass

      """  output parameters  """  

class SelectJobByJobNum_input:
   """ Required : 
   jobNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  Closing JobNum.  """  
      pass

class SelectJobByJobNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobClosingTableset] = obj["returnObj"]
      pass

class SelectMultipleJob_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingListTableset] = obj["ds"]
      pass

class SelectMultipleJob_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobClosingTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingListTableset] = obj["ds"]
      pass

      """  output parameters  """  

