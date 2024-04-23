import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CapPromiseSvc
# Description: bo/CapPromise/CapPromise.p
           Capable To Promise business object
           smr
           07/15/04
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CalculateCTP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateCTP
   Description: Performs the calculation logic for CTP.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: CalculateCTP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateCTP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateCTP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CancelCTP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelCTP
   Description: Performs the cancellation of CTP.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: CancelCTP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelCTP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelCTP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CapPromiseDmdGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CapPromiseDmdGetNew
   Description: Creates a temporary record to store information needed for the
Capable To Promise process.
   OperationID: CapPromiseDmdGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CapPromiseDmdGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CapPromiseDmdGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CapPromiseGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CapPromiseGetNew
   Description: Creates a temporary record to store information needed for the
Capable To Promise process.
   OperationID: CapPromiseGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CapPromiseGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CapPromiseGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCapPromiseDtlFiniteSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCapPromiseDtlFiniteSchedule
   Description: Reassigns the OverrideMtlConstraints and EnableOverrideMtlConstraints
fields based on the value of FiniteSchedule.
   OperationID: ChangeCapPromiseDtlFiniteSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCapPromiseDtlFiniteSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCapPromiseDtlFiniteSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCapPromiseGlobalCTP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCapPromiseGlobalCTP
   Description: Updates CapPromiseDtl records based on the new value of CapPromise.GlobalCTP.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: ChangeCapPromiseGlobalCTP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCapPromiseGlobalCTP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCapPromiseGlobalCTP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCapPromiseProjectedStartDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCapPromiseProjectedStartDate
   Description: Updates CapPromiseDtl records based on the new value of
CapPromise.ProjectedStartDate.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: ChangeCapPromiseProjectedStartDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCapPromiseProjectedStartDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCapPromiseProjectedStartDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConfirmCTP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConfirmCTP
   Description: Performs the confirmation logic for CTP.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: ConfirmCTP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfirmCTP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfirmCTP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConfirmCTPPOSug(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConfirmCTPPOSug
   Description: Performs the confirmation logic for the PO Suggestion created for CTP.
   OperationID: ConfirmCTPPOSug
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfirmCTPPOSug_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfirmCTPPOSug_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_deleteJob(epicorHeaders = None):
   """  
   Summary: Invoke method deleteJob
   Description: Purpose:     Delete the CTP job and leave the results from the calculation when parameter
from Site Configuration is set as "N - No Job"
Parameters:  none
Notes:       First the temporal job "CTP Job" is deleted and then as we alraedy have save the results from
CTP calculation into the ttCapPromise ds, we just update the OrderDtl and OrderRel records.
DEVELOPER NOTE: this method is also called from OM\ProcessDemand.cs and will require changes there if the parameters are changed.
   OperationID: deleteJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/deleteJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_DoWhseAtp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DoWhseAtp
   OperationID: DoWhseAtp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DoWhseAtp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoWhseAtp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindMaxConv(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindMaxConv
   Description: Purpose:  Find the maximum convertable quantity for giving unit of measure and quantity
   OperationID: FindMaxConv
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindMaxConv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindMaxConv_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetOrderPromiseDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetOrderPromiseDate
   Description: Sets the completion date for all detail records based on the latest date
of the detail records.
Before calling this method all CapPromiseDtl records must have the RowMod
field set to 'U'.
   OperationID: SetOrderPromiseDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetOrderPromiseDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetOrderPromiseDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapPromiseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CalculateCTP_input:
   """ Required : 
   lDemandEntry
   ds
   """  
   def __init__(self, obj):
      self.lDemandEntry:bool = obj["lDemandEntry"]
      """  If comes from Demand Entry or not.  """  
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

class CalculateCTP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CancelCTP_input:
   """ Required : 
   lDemandEntry
   ds
   """  
   def __init__(self, obj):
      self.lDemandEntry:bool = obj["lDemandEntry"]
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

class CancelCTP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CapPromiseDmdGetNew_input:
   """ Required : 
   DemandContractNum
   DemandHeadSeq
   DemandDtlSeq
   DemandScheduleSeq
   """  
   def __init__(self, obj):
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The Demand Contract number for the process  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The Demand Head Sequence for the process  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  The Demand Detail Sequence for the process  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  The Demand Schedule Sequence number for the process  """  
      pass

class CapPromiseDmdGetNew_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CapPromiseTableset] = obj["returnObj"]
      pass

class CapPromiseGetNew_input:
   """ Required : 
   OrderNum
   """  
   def __init__(self, obj):
      self.OrderNum:int = obj["OrderNum"]
      """  The order number for the process  """  
      pass

class CapPromiseGetNew_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CapPromiseTableset] = obj["returnObj"]
      pass

class ChangeCapPromiseDtlFiniteSchedule_input:
   """ Required : 
   ProposedFiniteSchedule
   OrderNum
   OrderLine
   OrderRelNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedFiniteSchedule:bool = obj["ProposedFiniteSchedule"]
      """  The proposed value for FiniteSchedule  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The Order Line  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The Order Release Number  """  
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

class ChangeCapPromiseDtlFiniteSchedule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCapPromiseGlobalCTP_input:
   """ Required : 
   ProposedGlobalCTP
   ds
   """  
   def __init__(self, obj):
      self.ProposedGlobalCTP:bool = obj["ProposedGlobalCTP"]
      """  The proposed value for GlobalCTP  """  
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

class ChangeCapPromiseGlobalCTP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCapPromiseProjectedStartDate_input:
   """ Required : 
   ProposedProjectedStartDate
   ds
   """  
   def __init__(self, obj):
      self.ProposedProjectedStartDate:str = obj["ProposedProjectedStartDate"]
      """  The proposed value for ProjectedStartDate  """  
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

class ChangeCapPromiseProjectedStartDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ConfirmCTPPOSug_input:
   """ Required : 
   iSugNum
   """  
   def __init__(self, obj):
      self.iSugNum:int = obj["iSugNum"]
      """  PO Suggestion Number to be confirmed.  """  
      pass

class ConfirmCTPPOSug_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opError:str = obj["parameters"]
      pass

      """  output parameters  """  

class ConfirmCTP_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

class ConfirmCTP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opError:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DoWhseAtp_input:
   """ Required : 
   atpdate
   atpWhseqty
   ipPast
   """  
   def __init__(self, obj):
      self.atpdate:str = obj["atpdate"]
      self.atpWhseqty:int = obj["atpWhseqty"]
      self.ipPast:bool = obj["ipPast"]
      pass

class DoWhseAtp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.atpdate:str = obj["parameters"]
      self.atpWhseqty:int = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CapPromiseDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.PartNum:str = obj["PartNum"]
      self.LineDesc:str = obj["LineDesc"]
      self.Quantity:int = obj["Quantity"]
      """  Quantity displayed in base UOM  """  
      self.NeedByDate:str = obj["NeedByDate"]
      self.ProposedStartDate:str = obj["ProposedStartDate"]
      self.CTP:bool = obj["CTP"]
      self.EnableCTP:bool = obj["EnableCTP"]
      self.CalculatedCompDate:str = obj["CalculatedCompDate"]
      """  The calculated completion date.  """  
      self.UserCompDate:str = obj["UserCompDate"]
      """  The user entered completion date.  Defaults from CalculatedCompDate.  """  
      self.Confirm:bool = obj["Confirm"]
      self.EnableConfirm:bool = obj["EnableConfirm"]
      self.JobNum:str = obj["JobNum"]
      self.ErrorText:str = obj["ErrorText"]
      self.FiniteSchedule:bool = obj["FiniteSchedule"]
      self.OverrideMtlConstraints:bool = obj["OverrideMtlConstraints"]
      self.EnableOverrideMtlConstraints:bool = obj["EnableOverrideMtlConstraints"]
      self.HasBeenConfirmed:bool = obj["HasBeenConfirmed"]
      self.NewOrderRelNum:int = obj["NewOrderRelNum"]
      self.KitFlag:str = obj["KitFlag"]
      """  Describes if this record comes from a kit component (C) or a kit parent (P), and is blank if it's a non-kit line  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  If this record comes from a kit part then this field will hold the parent line number for this component. If the record comes from the kit parent then this field will hold the same value as the OrderLine  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  The quantity per kit in case that this line comes from a kit component, if not it will be 0  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  On Hand Qty for the record's PartNum, this is the sum of all PartBin for this part and it calculated on the CapPromiseGetNew  """  
      self.HasChangedData:bool = obj["HasChangedData"]
      """  HasChangedData  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  Quantity displayed in selling UOM  """  
      self.SellingQuantityUOM:str = obj["SellingQuantityUOM"]
      """  Selling Quantity UOM  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  Buy To Order flag of the OrderRel  """  
      self.SugNum:int = obj["SugNum"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  Demand Contract Number  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  Demand Head sequence  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail Sequence  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  DemandScheduleSeq  """  
      self.NewDemandScheduleSeq:int = obj["NewDemandScheduleSeq"]
      self.MultiLevelCTP:bool = obj["MultiLevelCTP"]
      self.EnableMultiLevelCTP:bool = obj["EnableMultiLevelCTP"]
      self.CTPNeedByDate:str = obj["CTPNeedByDate"]
      """  This column will be calculated as the Ship by date plus the delivery days.  """  
      self.CTPShipDate:str = obj["CTPShipDate"]
      """  This column will be calculated as the Completion date plus customer periodicity logic.  """  
      self.ConfirmAll:bool = obj["ConfirmAll"]
      """  Use by CTP from Demand Entry, indicates for each schedule if the Job created for CTP will be firmed and the PO Sug will create a PO after the schedule is processed and a order release is now available.  """  
      self.ContractID:str = obj["ContractID"]
      self.LinkToContract:bool = obj["LinkToContract"]
      self.ReqDate:str = obj["ReqDate"]
      """  Will show the OrderRel.ReqDate or DemandSchedule.ReqDate (ship by Date).  """  
      self.ReqDteNotMet:bool = obj["ReqDteNotMet"]
      """  True = the calculated CTP date will not meet the Ship By date on the order line/release  """  
      self.ReqDteMissedByDays:int = obj["ReqDteMissedByDays"]
      """  A numerical value in days to signify by how many days the calculated date misses or is greater than the Ship By date  """  
      self.Plant:str = obj["Plant"]
      """  The plant from either OrderRel.Plant or DemandSchedule.Plant depending on the source of the CTP used to calculate the difference between the calculated completion date and the ship by date after all dates have been calculated for the CapPromiseDtl  """  
      self.AvailQty:int = obj["AvailQty"]
      """  The inventory quantity that is projected to be available on the requested ship date and is not already committed to a demand as of when the CTP calculation is being done (today).  """  
      self.JobNumDisp:str = obj["JobNumDisp"]
      """  Holds the CTP job number or translated text for the values of CapPromiseDtl.JobNum: stock, OK - Stock, Lead time, PO Suggestion, etc  """  
      self.DemandCapPromiseUpdate:str = obj["DemandCapPromiseUpdate"]
      """  The column is only populated if Customer/ShipTo Demand Update Date (DemandCapPromisDate) = true. it is used to determne how to set the dates for a new DemandSchedule split line during Confirm CTP  """  
      self.IsDropShip:bool = obj["IsDropShip"]
      """  Indicates whether the demand schedule is for a drop ship part.  """  
      self.KitCompCalcCompDate:str = obj["KitCompCalcCompDate"]
      """  Date that was calculated for the completion of this kit component. After all CTP calcs the kit components will all be changed to the latest date calculated for any component on the kit.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number associated with Part  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CapPromiseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.OrderNum:int = obj["OrderNum"]
      self.GlobalCTP:bool = obj["GlobalCTP"]
      self.EnableGlobalCTP:bool = obj["EnableGlobalCTP"]
      self.ProjectedStartDate:str = obj["ProjectedStartDate"]
      self.AllowSetOrderPromiseDate:bool = obj["AllowSetOrderPromiseDate"]
      self.ShipOption:str = obj["ShipOption"]
      """  Indicates the Shipment Option to be used during CTP processing.  Can be "SOC" - Ship Order Complete, "SLC" - Ship Line Complete or "SPQ" - Ship Partial Quantities.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  Demand Contract Number  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  DemandHeadSeq  """  
      self.DemandContract:str = obj["DemandContract"]
      """  Demand Contract Description  """  
      self.PONum:str = obj["PONum"]
      """  PO Number for Demand Entry Logic  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CapPromiseTableset:
   def __init__(self, obj):
      self.CapPromise:list[Erp_Tablesets_CapPromiseRow] = obj["CapPromise"]
      self.CapPromiseDtl:list[Erp_Tablesets_CapPromiseDtlRow] = obj["CapPromiseDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindMaxConv_input:
   """ Required : 
   PartNum
   QtyIn
   fromuom
   touom
   """  
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      self.QtyIn:int = obj["QtyIn"]
      self.fromuom:str = obj["fromuom"]
      self.touom:str = obj["touom"]
      pass

class FindMaxConv_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.maxQty:int = obj["parameters"]
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

class SetOrderPromiseDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

class SetOrderPromiseDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CapPromiseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class deleteJob_output:
   def __init__(self, obj):
      pass

