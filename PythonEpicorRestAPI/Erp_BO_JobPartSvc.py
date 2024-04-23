import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JobPartSvc
# Description: Job part business object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_JobParts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JobParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobParts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/JobParts",headers=creds) as resp:
           return await resp.json()

async def post_JobParts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/JobParts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JobParts_Company_JobNum_PartNum(Company, JobNum, PartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JobPart item
   Description: Calls GetByID to retrieve the JobPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/JobParts(" + Company + "," + JobNum + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JobParts_Company_JobNum_PartNum(Company, JobNum, PartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JobPart for the service
   Description: Calls UpdateExt to update JobPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/JobParts(" + Company + "," + JobNum + "," + PartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JobParts_Company_JobNum_PartNum(Company, JobNum, PartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JobPart item
   Description: Call UpdateExt to delete JobPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/JobParts(" + Company + "," + JobNum + "," + PartNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobPartListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJobPart, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "whereClauseJobPart=" + whereClauseJobPart
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(jobNum, partNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "jobNum=" + jobNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobPartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobPartListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobPartListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobPartRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobPartRow] = obj["value"]
      pass

class Erp_Tablesets_JobPartListRow:
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
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrderQty:int = obj["OrderQty"]
      self.ProcessMode:str = obj["ProcessMode"]
      """  The value of the JobHead.ProcessMode  """  
      self.EnableShipDocReq:bool = obj["EnableShipDocReq"]
      """  Indicates if ShipDocReq is enabled. Only if JobPart.PartNum does not exist in Part Table and if Document Management is installed.  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      """  Logical field signifying whether JobPart.PartNum is a valid part master part.  """  
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




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   jobNum
   partNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.partNum:str = obj["partNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JobPartListRow:
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
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrderQty:int = obj["OrderQty"]
      self.ProcessMode:str = obj["ProcessMode"]
      """  The value of the JobHead.ProcessMode  """  
      self.EnableShipDocReq:bool = obj["EnableShipDocReq"]
      """  Indicates if ShipDocReq is enabled. Only if JobPart.PartNum does not exist in Part Table and if Document Management is installed.  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      """  Logical field signifying whether JobPart.PartNum is a valid part master part.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobPartListTableset:
   def __init__(self, obj):
      self.JobPartList:list[Erp_Tablesets_JobPartListRow] = obj["JobPartList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Erp_Tablesets_JobPartTableset:
   def __init__(self, obj):
      self.JobPart:list[Erp_Tablesets_JobPartRow] = obj["JobPart"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtJobPartTableset:
   def __init__(self, obj):
      self.JobPart:list[Erp_Tablesets_JobPartRow] = obj["JobPart"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   jobNum
   partNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.partNum:str = obj["partNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobPartTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobPartTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobPartTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobPartListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewJobPart_input:
   """ Required : 
   ds
   jobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobPartTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      pass

class GetNewJobPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseJobPart
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobPart:str = obj["whereClauseJobPart"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobPartTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJobPartTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJobPartTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobPartTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

