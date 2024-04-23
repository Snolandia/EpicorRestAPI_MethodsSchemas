import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JobMtlSearchSvc
# Description: Search object for Job Material
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_JobMtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JobMtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobMtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/JobMtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_JobMtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobMtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobMtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobMtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/JobMtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JobMtlSearches_Company_JobNum_AssemblySeq_MtlSeq(Company, JobNum, AssemblySeq, MtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JobMtlSearch item
   Description: Calls GetByID to retrieve the JobMtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobMtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/JobMtlSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JobMtlSearches_Company_JobNum_AssemblySeq_MtlSeq(Company, JobNum, AssemblySeq, MtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JobMtlSearch for the service
   Description: Calls UpdateExt to update JobMtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobMtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobMtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/JobMtlSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JobMtlSearches_Company_JobNum_AssemblySeq_MtlSeq(Company, JobNum, AssemblySeq, MtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JobMtlSearch item
   Description: Call UpdateExt to delete JobMtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobMtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/JobMtlSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobMtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJobMtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseJobMtl=" + whereClauseJobMtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(jobNum, assemblySeq, mtlSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "assemblySeq=" + assemblySeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "mtlSeq=" + mtlSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobMtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobMtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobMtlRow] = obj["value"]
      pass

class Erp_Tablesets_JobMtlListRow:
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
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShowStatusIcon:str = obj["ShowStatusIcon"]
      """  ShowStatusIcon  """  
      self.DisplayUnitPrice:int = obj["DisplayUnitPrice"]
      """  The display unit price.  """  
      self.DisplayExtPrice:int = obj["DisplayExtPrice"]
      """  The display of extended price.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  The currency switch flag  """  
      self.DocDisplayUnitPrice:int = obj["DocDisplayUnitPrice"]
      """  The document display extended price  """  
      self.DocDisplayExtPrice:int = obj["DocDisplayExtPrice"]
      """  The document display extended price  """  
      self.IPCaller:str = obj["IPCaller"]
      """  The name of the calling program  """  
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      """  The description of the related operation  """  
      self.SubContract:bool = obj["SubContract"]
      """  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.EnableSndAlrtCmpl:bool = obj["EnableSndAlrtCmpl"]
      """  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  """  
      self.EnableBackflush:bool = obj["EnableBackflush"]
      """  Should the backflush field be enabled?  """  
      self.AllowBackflushUncheck:bool = obj["AllowBackflushUncheck"]
      """  Can the backflush be unchecked?  """  
      self.RetainValues:bool = obj["RetainValues"]
      """  Logical used to determine if record is created from PO Entry.  """  
      self.PricePerCodeDescription:str = obj["PricePerCodeDescription"]
      """  Price Per Code Description  """  
      self.AllowJobCosts:str = obj["AllowJobCosts"]
      """  Flag to allow/disallow the user to see the Job Costs. Since the Object designer is not letting me add a boolean, I added a string.  """  
      self.EstCost:int = obj["EstCost"]
      """  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  """  
      self.EnableRcvInspReq:bool = obj["EnableRcvInspReq"]
      """  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  """  
      self.ShowInspRqdImg:bool = obj["ShowInspRqdImg"]
      """  Satatus of InspectionRequired image on JobMaterial form.  """  
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.dspBuyIt:bool = obj["dspBuyIt"]
      """  BuyIt field for display in the UI.  """  
      self.EnableBuyIt:bool = obj["EnableBuyIt"]
      """  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  """  
      self.IsBaseCurrency:bool = obj["IsBaseCurrency"]
      """  IsBaseCurrency  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.SalvageBaseUOM:str = obj["SalvageBaseUOM"]
      """  BaseUOM for SalvagePartNum  """  
      self.Rpt1DisplayUnitPrice:int = obj["Rpt1DisplayUnitPrice"]
      self.Rpt2DisplayUnitPrice:int = obj["Rpt2DisplayUnitPrice"]
      self.Rpt3DisplayUnitPrice:int = obj["Rpt3DisplayUnitPrice"]
      self.Rpt1DisplayExtPrice:int = obj["Rpt1DisplayExtPrice"]
      self.Rpt2DisplayExtPrice:int = obj["Rpt2DisplayExtPrice"]
      self.Rpt3DisplayExtPrice:int = obj["Rpt3DisplayExtPrice"]
      self.EnableFixedQty:bool = obj["EnableFixedQty"]
      """  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  """  
      self.DspIUM:str = obj["DspIUM"]
      """  Display IUM (readonly)  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.EnableSplitCosts:bool = obj["EnableSplitCosts"]
      """  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  """  
      self.IsMtlExtConfig:bool = obj["IsMtlExtConfig"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      """  Description  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      """  Description of the Miscellaneous Charge. Appears on orders, invoices and in drop-down selection lists.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.PurMiscCodeLCCurrencyCode:str = obj["PurMiscCodeLCCurrencyCode"]
      """  The Landed Cost Currency Code for this miscellaneous charge.  """  
      self.PurMiscCodeDescription:str = obj["PurMiscCodeDescription"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.PurMiscCodeLCDisburseMethod:str = obj["PurMiscCodeLCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.PurMiscCodeLCAmount:int = obj["PurMiscCodeLCAmount"]
      """  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      """   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  """  
      self.SCMiscCodeDescription:str = obj["SCMiscCodeDescription"]
      """  Description of the Miscellaneous Charge. Appears on orders, invoices and in drop-down selection lists.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorPPCity:str = obj["VendorPPCity"]
      """  City portion of the address  """  
      self.VendorPPPrimPCon:int = obj["VendorPPPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.VendorPPAddress2:str = obj["VendorPPAddress2"]
      """  Second address line  """  
      self.VendorPPCountry:str = obj["VendorPPCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorPPState:str = obj["VendorPPState"]
      """  State portion of the address  """  
      self.VendorPPAddress3:str = obj["VendorPPAddress3"]
      """  Third address line  """  
      self.VendorPPName:str = obj["VendorPPName"]
      """  Purchase Point Name...can't be blank.  """  
      self.VendorPPZip:str = obj["VendorPPZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.VendorPPAddress1:str = obj["VendorPPAddress1"]
      """  First address line  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
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




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   jobNum
   assemblySeq
   mtlSeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JobMtlListRow:
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
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShowStatusIcon:str = obj["ShowStatusIcon"]
      """  ShowStatusIcon  """  
      self.DisplayUnitPrice:int = obj["DisplayUnitPrice"]
      """  The display unit price.  """  
      self.DisplayExtPrice:int = obj["DisplayExtPrice"]
      """  The display of extended price.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  The currency switch flag  """  
      self.DocDisplayUnitPrice:int = obj["DocDisplayUnitPrice"]
      """  The document display extended price  """  
      self.DocDisplayExtPrice:int = obj["DocDisplayExtPrice"]
      """  The document display extended price  """  
      self.IPCaller:str = obj["IPCaller"]
      """  The name of the calling program  """  
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      """  The description of the related operation  """  
      self.SubContract:bool = obj["SubContract"]
      """  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.EnableSndAlrtCmpl:bool = obj["EnableSndAlrtCmpl"]
      """  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  """  
      self.EnableBackflush:bool = obj["EnableBackflush"]
      """  Should the backflush field be enabled?  """  
      self.AllowBackflushUncheck:bool = obj["AllowBackflushUncheck"]
      """  Can the backflush be unchecked?  """  
      self.RetainValues:bool = obj["RetainValues"]
      """  Logical used to determine if record is created from PO Entry.  """  
      self.PricePerCodeDescription:str = obj["PricePerCodeDescription"]
      """  Price Per Code Description  """  
      self.AllowJobCosts:str = obj["AllowJobCosts"]
      """  Flag to allow/disallow the user to see the Job Costs. Since the Object designer is not letting me add a boolean, I added a string.  """  
      self.EstCost:int = obj["EstCost"]
      """  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  """  
      self.EnableRcvInspReq:bool = obj["EnableRcvInspReq"]
      """  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  """  
      self.ShowInspRqdImg:bool = obj["ShowInspRqdImg"]
      """  Satatus of InspectionRequired image on JobMaterial form.  """  
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.dspBuyIt:bool = obj["dspBuyIt"]
      """  BuyIt field for display in the UI.  """  
      self.EnableBuyIt:bool = obj["EnableBuyIt"]
      """  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  """  
      self.IsBaseCurrency:bool = obj["IsBaseCurrency"]
      """  IsBaseCurrency  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.SalvageBaseUOM:str = obj["SalvageBaseUOM"]
      """  BaseUOM for SalvagePartNum  """  
      self.Rpt1DisplayUnitPrice:int = obj["Rpt1DisplayUnitPrice"]
      self.Rpt2DisplayUnitPrice:int = obj["Rpt2DisplayUnitPrice"]
      self.Rpt3DisplayUnitPrice:int = obj["Rpt3DisplayUnitPrice"]
      self.Rpt1DisplayExtPrice:int = obj["Rpt1DisplayExtPrice"]
      self.Rpt2DisplayExtPrice:int = obj["Rpt2DisplayExtPrice"]
      self.Rpt3DisplayExtPrice:int = obj["Rpt3DisplayExtPrice"]
      self.EnableFixedQty:bool = obj["EnableFixedQty"]
      """  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  """  
      self.DspIUM:str = obj["DspIUM"]
      """  Display IUM (readonly)  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.EnableSplitCosts:bool = obj["EnableSplitCosts"]
      """  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  """  
      self.IsMtlExtConfig:bool = obj["IsMtlExtConfig"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      """  Description  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      """  Description of the Miscellaneous Charge. Appears on orders, invoices and in drop-down selection lists.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.PurMiscCodeLCCurrencyCode:str = obj["PurMiscCodeLCCurrencyCode"]
      """  The Landed Cost Currency Code for this miscellaneous charge.  """  
      self.PurMiscCodeDescription:str = obj["PurMiscCodeDescription"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.PurMiscCodeLCDisburseMethod:str = obj["PurMiscCodeLCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.PurMiscCodeLCAmount:int = obj["PurMiscCodeLCAmount"]
      """  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      """   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  """  
      self.SCMiscCodeDescription:str = obj["SCMiscCodeDescription"]
      """  Description of the Miscellaneous Charge. Appears on orders, invoices and in drop-down selection lists.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorPPCity:str = obj["VendorPPCity"]
      """  City portion of the address  """  
      self.VendorPPPrimPCon:int = obj["VendorPPPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.VendorPPAddress2:str = obj["VendorPPAddress2"]
      """  Second address line  """  
      self.VendorPPCountry:str = obj["VendorPPCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorPPState:str = obj["VendorPPState"]
      """  State portion of the address  """  
      self.VendorPPAddress3:str = obj["VendorPPAddress3"]
      """  Third address line  """  
      self.VendorPPName:str = obj["VendorPPName"]
      """  Purchase Point Name...can't be blank.  """  
      self.VendorPPZip:str = obj["VendorPPZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.VendorPPAddress1:str = obj["VendorPPAddress1"]
      """  First address line  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobMtlListTableset:
   def __init__(self, obj):
      self.JobMtlList:list[Erp_Tablesets_JobMtlListRow] = obj["JobMtlList"]
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

class Erp_Tablesets_JobMtlSearchTableset:
   def __init__(self, obj):
      self.JobMtl:list[Erp_Tablesets_JobMtlRow] = obj["JobMtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtJobMtlSearchTableset:
   def __init__(self, obj):
      self.JobMtl:list[Erp_Tablesets_JobMtlRow] = obj["JobMtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   jobNum
   assemblySeq
   mtlSeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobMtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobMtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobMtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobMtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewJobMtl_input:
   """ Required : 
   ds
   jobNum
   assemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobMtlSearchTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class GetNewJobMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobMtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseJobMtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobMtl:str = obj["whereClauseJobMtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobMtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtJobMtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJobMtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobMtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobMtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

