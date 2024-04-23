import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JobManagerSvc
# Description: JobManager, is an object which works with the Demand and Supply of a specific part number.
Provides dataset of Demand/Supply relationships matrix.
Provides methods for maintaining these relationships
Provides access to the Suggestions for a given part
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   Description: Retrieves part number
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   Description: Use SysrowID to find the part
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPartStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPartStatus
   Description: This method checks to see if there are any questions or issues with the part entered
and returns a message, if any substitutes exist and Message type.
Intended to be called prior to calling the CreateJob method.
   OperationID: CheckPartStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPartStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateJob
   Description: To create a new Job for production demand.
You pass this method the Reckey of the demand record for which a job will be created.
The job will be created and this demand record will be linked to it.
You must also pass the Job Number you wish to use. This should have been determined
using the standard object to assign job numbers.
IMPORTANT: Your logic should have also called the CheckPartStatus method and provided the appropriate
user interaction before calling this mehtod.
   OperationID: CreateJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteJob
   Description: To delete the Job of a specific JMSupply record.
   OperationID: DeleteJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeletePartSug(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeletePartSug
   Description: Deletes Part Suggestion
   OperationID: DeletePartSug
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePartSug_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePartSug_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMatrix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMatrix
   Description: To retrieve the JobManager dataset for a given part number.
This dataset is a Demand/Supply matrix for the part.
Note: Part numbers may not exist in the Part table. Therefore, this method allows you to pass in
the part description. Depending on where you are calling from, you might use OrderDtl.LineDesc,
JobMtl.Description, etc.
   OperationID: GetMatrix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMatrix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatrix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNextJobNumOrderRelease(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNextJobNumOrderRelease
   Description: This methods generates the job number based off
of the OrderRel record related to the input PartDtl.
   OperationID: GetNextJobNumOrderRelease
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNextJobNumOrderRelease_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextJobNumOrderRelease_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LinkToJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LinkToJob
   Description: To link a production demand (JMDemand record) with an existing job.
This validates the following:
1. The demand record still exists in the database.
2. That it is not already linked to a source of supply (job, warehouse)
3. Target job exists.
4. Target job is not a Field Service Job.
5. System configuration allows changes to engineered Jobs.
6. Job is not Closed.
   OperationID: LinkToJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkToJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkToJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreGetDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreGetDetails
   Description: This method checks to see if the part is a valid part in the part master.
Configured parts have the option to create part numbers without create a part
record.  If this is the case, then use the OrderDtl.BasePartNum and
OrderDtl.BaseRevisionNum or QuoteDtl.BasePartNum and QuoteDtl.BaseRevisionNum
to get details.  If the basePartNum isn't equal to null then use it to Get Details
   OperationID: PreGetDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGetDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGetDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PullFromStock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PullFromStock
   Description: To link a demand with to a warehouse that will supply the demand.
   OperationID: PullFromStock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PullFromStock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PullFromStock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TransferDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TransferDemand
   Description: To transfer a demand on one job to another job.
   OperationID: TransferDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TransferDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TransferDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlinkDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlinkDemand
   Description: To unlink a demand from the related Job.
   OperationID: UnlinkDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlinkDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlinkSupply(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlinkSupply
   Description: To unlink a supply from it's related demand.
   OperationID: UnlinkSupply
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlinkSupply_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkSupply_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobManagerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CheckPartStatus_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to validate  """  
      pass

class CheckPartStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMsgText:str = obj["parameters"]
      self.vSubAvail:bool = obj["vSubAvail"]
      self.vMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreateJob_input:
   """ Required : 
   demandReckey
   newJobNum
   """  
   def __init__(self, obj):
      self.demandReckey:str = obj["demandReckey"]
      """  The JMDemand.RecKey field value of row for which a new job will be created.  """  
      self.newJobNum:str = obj["newJobNum"]
      """  Job number to be assigned to the newly created job  """  
      pass

class CreateJob_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobManagerTableset] = obj["returnObj"]
      pass

class DeleteJob_input:
   """ Required : 
   jmSupply_RecKey
   """  
   def __init__(self, obj):
      self.jmSupply_RecKey:str = obj["jmSupply_RecKey"]
      """  The JMSupply.Reckey field is the physical rowid of the JobPart record.
Therefore it can be used to indicate the job that you wish deleted.  """  
      pass

class DeleteJob_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobManagerTableset] = obj["returnObj"]
      pass

class DeletePartSug_input:
   """ Required : 
   partSug_RowID
   """  
   def __init__(self, obj):
      self.partSug_RowID:str = obj["partSug_RowID"]
      """  Part Suggestions Row id  """  
      pass

class DeletePartSug_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobManagerTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_JMDemandRow:
   def __init__(self, obj):
      self.ParentRecKey:str = obj["ParentRecKey"]
      """  RecKey of the Parent record (JMPartSum)  """  
      self.RecKey:str = obj["RecKey"]
      """  Unique Key - Uses RowID of the PartDtl which was the data source  """  
      self.DueDate:str = obj["DueDate"]
      self.Quantity:int = obj["Quantity"]
      self.JobNum:str = obj["JobNum"]
      self.SourceString:str = obj["SourceString"]
      """  Formatted String representing Source of Demand. Ex: SO 105-3-1 means Sales Order 105 Line 3 Release 1  """  
      self.FirmRelease:bool = obj["FirmRelease"]
      self.OrderNum:int = obj["OrderNum"]
      self.Plant:str = obj["Plant"]
      self.CustomerName:str = obj["CustomerName"]
      self.SuggestionFlag:str = obj["SuggestionFlag"]
      """  N = New, C = Change, " " = No Suggestions. Used for filtering.  """  
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.CanCreateJob:bool = obj["CanCreateJob"]
      """  Indicates if create Job function is available for this record  """  
      self.CanPull:bool = obj["CanPull"]
      """  Indicates if Pull from Stock function is available for this record  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this Demand has one or more related DemandSupply records  """  
      self.SuggestionFlagDesc:str = obj["SuggestionFlagDesc"]
      """  Text description of the SuggestionFlag field for transalation N=new, C=Change, ""=None  """  
      self.HasSuggestion:bool = obj["HasSuggestion"]
      """  If this JMDemand record is associated with a PartSug record, this field is true.  """  
      self.PartSugDesc:str = obj["PartSugDesc"]
      """  Description from PartSug.Description field  """  
      self.UniqueRecKey:str = obj["UniqueRecKey"]
      """  either the rowid from PartDtl or PartSug  """  
      self.UOM:str = obj["UOM"]
      self.ContractID:str = obj["ContractID"]
      self.LinkToContract:bool = obj["LinkToContract"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JMDemandSupplyRow:
   def __init__(self, obj):
      self.ParentRecKey:str = obj["ParentRecKey"]
      """  RecKey of the Parent record (JMDemand)  """  
      self.RecKey:str = obj["RecKey"]
      """  Unique Key - RowID of the datasoure record (JobProd, PartDtl, OrderRel, JobMtl,JobAsmbl). Datasource table is identified in SourcTable field.  """  
      self.SourceTable:str = obj["SourceTable"]
      """  The main DB Source table that data in this record was derived from. Note: Reckey contains the RowID of the record from this table.  """  
      self.SourceString:str = obj["SourceString"]
      """  Formatted String representing Source of supply. Ex: Whse MPL  means supplied from Stock Warehouse Mpl  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Required By date of the supply  """  
      self.Quantity:int = obj["Quantity"]
      self.JobComplete:bool = obj["JobComplete"]
      self.JobReleased:bool = obj["JobReleased"]
      self.ProdQty:int = obj["ProdQty"]
      self.RelievedQty:int = obj["RelievedQty"]
      self.JobNum:str = obj["JobNum"]
      self.WareHouseCode:str = obj["WareHouseCode"]
      self.Transferable:bool = obj["Transferable"]
      """  Indicates if Transfer function is appropriate for this record  """  
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.CanUnLink:bool = obj["CanUnLink"]
      self.QuantityUOM:str = obj["QuantityUOM"]
      """  Quantity IUM  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JMInventoryRow:
   def __init__(self, obj):
      self.ParentRecKey:str = obj["ParentRecKey"]
      """  RecKey of the Parent record (JMPartSum)  """  
      self.RecKey:str = obj["RecKey"]
      """  Unique Key - Uses RowID of the PartWhse which was the data source  """  
      self.Plant:str = obj["Plant"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.OnHandQty:int = obj["OnHandQty"]
      self.AvailQty:int = obj["AvailQty"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.DemandQty:int = obj["DemandQty"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JMPartSumRow:
   def __init__(self, obj):
      self.RecKey:str = obj["RecKey"]
      """  Unique Key - Uses the PartNum as the value.  """  
      self.PartNum:str = obj["PartNum"]
      self.OnHandQty:int = obj["OnHandQty"]
      """  Quantity on hand, entire company  """  
      self.AvailQty:int = obj["AvailQty"]
      """  Part Quantity Available  - Entire Company  """  
      self.PartDescription:str = obj["PartDescription"]
      self.UOM:str = obj["UOM"]
      """  Part UOM  """  
      self.DemandQty:int = obj["DemandQty"]
      """  Demand - Entire Company/All warehouses  """  
      self.ContractDescription:str = obj["ContractDescription"]
      self.ContractID:str = obj["ContractID"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JMSupplyDemandRow:
   def __init__(self, obj):
      self.ParentRecKey:str = obj["ParentRecKey"]
      """  RecKey of the Parent record (JMSupply)  """  
      self.RecKey:str = obj["RecKey"]
      """  Unique Key - RowID of the datasoure record (JobProd).  """  
      self.SourceString:str = obj["SourceString"]
      self.ShipByDate:str = obj["ShipByDate"]
      self.WipQty:int = obj["WipQty"]
      self.ProdQty:int = obj["ProdQty"]
      self.RelievedQty:int = obj["RelievedQty"]
      self.OrderNum:int = obj["OrderNum"]
      self.JobNum:str = obj["JobNum"]
      self.DemandStatus:str = obj["DemandStatus"]
      self.Transferable:bool = obj["Transferable"]
      """  Indicates if transfer function is available for this record.  """  
      self.CanUnLink:bool = obj["CanUnLink"]
      self.IsServiceJob:bool = obj["IsServiceJob"]
      """  Flag that indicates if it is a service job  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Engineered or not.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JMSupplyRow:
   def __init__(self, obj):
      self.ParentRecKey:str = obj["ParentRecKey"]
      """  RecKey of the Parent record (JMPartSum)  """  
      self.RecKey:str = obj["RecKey"]
      """  Unique Key - Uses RowID of the JobHead which was the data source  """  
      self.ReqDate:str = obj["ReqDate"]
      self.JobNum:str = obj["JobNum"]
      self.WipQty:int = obj["WipQty"]
      self.JobReleased:bool = obj["JobReleased"]
      self.JobComplete:bool = obj["JobComplete"]
      self.ProdQty:int = obj["ProdQty"]
      self.RelievedQty:int = obj["RelievedQty"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.Linkable:bool = obj["Linkable"]
      """  Indicates if demands can be linked to this supply.  """  
      self.EnableGetDetails:bool = obj["EnableGetDetails"]
      """  Flag to indicate to the UI if the Get Details button should be enabled.  """  
      self.EnableDeleteJob:bool = obj["EnableDeleteJob"]
      """  Flag to indicate to UI if the Delete Job button should be enabled.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Engineered or not.  """  
      self.EnableSchedule:bool = obj["EnableSchedule"]
      """  Flag to indicate to UI if the Schedule button should be enabled.  """  
      self.EnableSplitJob:bool = obj["EnableSplitJob"]
      """  Indicates if split job is accessible  """  
      self.HasSuggestion:bool = obj["HasSuggestion"]
      """  If this JMSupply record is associated with a PartSug record, this field is true.  """  
      self.PartSugDesc:str = obj["PartSugDesc"]
      """  Description from PartSug.Description  """  
      self.PartSugRecKey:str = obj["PartSugRecKey"]
      """  RecKey of the associated PartSug record  """  
      self.IsServiceJob:bool = obj["IsServiceJob"]
      """  Flag that indicates if it is a service job  """  
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      """  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  """  
      self.JobDueDate:str = obj["JobDueDate"]
      self.ContractID:str = obj["ContractID"]
      self.LinkToContract:bool = obj["LinkToContract"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobManagerTableset:
   def __init__(self, obj):
      self.JMPartSum:list[Erp_Tablesets_JMPartSumRow] = obj["JMPartSum"]
      self.JMDemand:list[Erp_Tablesets_JMDemandRow] = obj["JMDemand"]
      self.JMDemandSupply:list[Erp_Tablesets_JMDemandSupplyRow] = obj["JMDemandSupply"]
      self.JMInventory:list[Erp_Tablesets_JMInventoryRow] = obj["JMInventory"]
      self.PartSug:list[Erp_Tablesets_PartSugRow] = obj["PartSug"]
      self.JMSupply:list[Erp_Tablesets_JMSupplyRow] = obj["JMSupply"]
      self.JMSupplyDemand:list[Erp_Tablesets_JMSupplyDemandRow] = obj["JMSupplyDemand"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartSugRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Classifier:str = obj["Classifier"]
      """   Suggestions fall into two classes.
"MFG" = Suggestion pertains to manufacturing 
"PUR" = Suggestion pertains to purchasing.
Used to keep Mfg and Purchase suggestions separate.  """  
      self.NewFlag:bool = obj["NewFlag"]
      """  New Requirement.  Used to filter between New and Changes.  """  
      self.Type:str = obj["Type"]
      """  Suggestions can be;  "New" , "Can", "Dat", "Qty",  "Chg", "Cfg"  """  
      self.SubType:str = obj["SubType"]
      """   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, R = Reduce Qty.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """  Job Number. Think of this as the Job that the suggestion is for ("target job")  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Job Assembly Sequence.  The assembly that the suggestion is for ("target assembly").  This can occur when an assembly has a PullQuantity that is marked "Make Direct."  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Job Material Sequence.  The material that the suggestion is for ("target material").  This can occur when the material is marked as "Make Direct."  """  
      self.Source:str = obj["Source"]
      """  Indicates the source of the requirement that suggestion is related to; "Order", "Stock" or "Job".  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """  Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Inventory warehouse that job is producing for.
Only relevant for build to stock demands (ordernum = 0). In this case a valid Part must be referenced.  """  
      self.DueDate:str = obj["DueDate"]
      """   Due date of the related requirement record.
OrderRel.ReqDate.....  """  
      self.SugDate:str = obj["SugDate"]
      """  Suggested due date to change meet the requirement.  """  
      self.SugQty:int = obj["SugQty"]
      """  Suggested quantity.  """  
      self.SugQtyUOM:str = obj["SugQtyUOM"]
      """  Unit of Measure that qualifies SugQty.  """  
      self.SugRevisionNum:str = obj["SugRevisionNum"]
      """  Suggested change to Revision Number.  """  
      self.Description:str = obj["Description"]
      """   Description of the proposed suggestion.
Ex: Change Job Due date to xx/xx/xx.  """  
      self.CustShortName:str = obj["CustShortName"]
      """  1st 8 characters of customer name. Used for sorting suggestions  """  
      self.CustID:str = obj["CustID"]
      """  Duplicated from the customer.custid. Used for sorting purposes.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that suggestion is for.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PoDetail record suggestion is for.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number that suggestion if for.  """  
      self.PlannerID:str = obj["PlannerID"]
      """  The ID of the Planner. Used to filter suggestions.  """  
      self.FirmRelease:bool = obj["FirmRelease"]
      """  A duplicate of "OrderRel.FirmRelease".  This only pertains to suggestions related to OrderRel.  Used to filter suggestions.  """  
      self.StockTrans:bool = obj["StockTrans"]
      """   Indicates if this suggestion affects stock.
Only the MRP Process creates StockTrans = Yes.  Various DB triggers and MRP create StockTrans = No (direct buy/mfg)  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier for this manufacturing suggestion.  """  
      self.SugNum:int = obj["SugNum"]
      """  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for the TFOrdDtl table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CustFullName:str = obj["CustFullName"]
      self.ErrorMsg:str = obj["ErrorMsg"]
      """  An error message description.  Used initially when creating a job.  """  
      self.JobInProcess:bool = obj["JobInProcess"]
      self.Planner:str = obj["Planner"]
      self.SugSource:str = obj["SugSource"]
      self.UOM:str = obj["UOM"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.SelectedPartSug:bool = obj["SelectedPartSug"]
      """  Used for selecting record on landing page grid for Kinetic version.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.JobNumReqDueDate:str = obj["JobNumReqDueDate"]
      self.JobNumStartDate:str = obj["JobNumStartDate"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetMatrix_input:
   """ Required : 
   ipPartNum
   ipAttributeSetID
   ipPartDescription
   uomCode
   contractID
   contractDesc
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part number to be retrieved.  """  
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      """  Attribute Set to be retrieved.  """  
      self.ipPartDescription:str = obj["ipPartDescription"]
      """  Description of the Part. Optional, used only if the the given part does not exist in the Part table.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      self.contractID:str = obj["contractID"]
      self.contractDesc:str = obj["contractDesc"]
      pass

class GetMatrix_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobManagerTableset] = obj["returnObj"]
      pass

class GetNextJobNumOrderRelease_input:
   """ Required : 
   ipPartDtlRowid
   """  
   def __init__(self, obj):
      self.ipPartDtlRowid:str = obj["ipPartDtlRowid"]
      """  The rowid of the partdtl record to create job for.  """  
      pass

class GetNextJobNumOrderRelease_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opNextJobNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      """  Row Type  """  
      self.ipRowID:str = obj["ipRowID"]
      """  SysRowID  """  
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   uomCode
   sysRowID
   rowType
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      self.sysRowID:str = obj["sysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.uomCode:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
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

class LinkToJob_input:
   """ Required : 
   demandReckey
   targetJobNum
   """  
   def __init__(self, obj):
      self.demandReckey:str = obj["demandReckey"]
      """  The JMDemand.RecKey field value of row to be linked.  """  
      self.targetJobNum:str = obj["targetJobNum"]
      """  Job number that you want to link the demand to.  """  
      pass

class LinkToJob_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobManagerTableset] = obj["returnObj"]
      pass

class PreGetDetails_input:
   """ Required : 
   partNum
   revisionNum
   targetJobNum
   targetAsm
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to validate  """  
      self.revisionNum:str = obj["revisionNum"]
      """  The revision number to validate  """  
      self.targetJobNum:str = obj["targetJobNum"]
      """  Target Job Number  """  
      self.targetAsm:int = obj["targetAsm"]
      """  Sequence of the target Assembly  """  
      pass

class PreGetDetails_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.basePartNum:str = obj["parameters"]
      self.baseRevisionNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class PullFromStock_input:
   """ Required : 
   demandReckey
   linkToWareHouseCode
   """  
   def __init__(self, obj):
      self.demandReckey:str = obj["demandReckey"]
      """  JMDemand.RecKey of the record to be pulled from stock.  """  
      self.linkToWareHouseCode:str = obj["linkToWareHouseCode"]
      """  Warehouse to be pulled from (allocated against).  """  
      pass

class PullFromStock_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobManagerTableset] = obj["returnObj"]
      pass

class TransferDemand_input:
   """ Required : 
   transferRecKey
   targetJobNum
   """  
   def __init__(self, obj):
      self.transferRecKey:str = obj["transferRecKey"]
      """  TransferRecKey (either DemandSupply or SupplyDemand.RecKey)  of the record to be transferred.  """  
      self.targetJobNum:str = obj["targetJobNum"]
      """  Job Number that the demand will be transfered to.  """  
      pass

class TransferDemand_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobManagerTableset] = obj["returnObj"]
      pass

class UnlinkDemand_input:
   """ Required : 
   supplyDemandReckey
   """  
   def __init__(self, obj):
      self.supplyDemandReckey:str = obj["supplyDemandReckey"]
      """  JMttJMSupplyDemand.RecKey of the record to be unlinked.  """  
      pass

class UnlinkDemand_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobManagerTableset] = obj["returnObj"]
      pass

class UnlinkSupply_input:
   """ Required : 
   demandSupplyReckey
   demandSupplySourceTable
   """  
   def __init__(self, obj):
      self.demandSupplyReckey:str = obj["demandSupplyReckey"]
      """  JMttJMDemandSupply.RecKey of the record to be unlinked.  """  
      self.demandSupplySourceTable:str = obj["demandSupplySourceTable"]
      """  ttJMDemandSupply.SourceTable of the record to be unlinked.  """  
      pass

class UnlinkSupply_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobManagerTableset] = obj["returnObj"]
      pass

