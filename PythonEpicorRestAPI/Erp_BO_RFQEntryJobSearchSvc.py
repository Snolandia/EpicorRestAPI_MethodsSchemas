import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RFQEntryJobSearchSvc
# Description: This is a Job Search object used in RFQEntry.
The GetRows of this objects returns the jobs
that are relevant in Add from Job function in RFQEntry.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RFQEntryJobSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQEntryJobSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQEntryJobSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/RFQEntryJobSearches",headers=creds) as resp:
           return await resp.json()

async def post_RFQEntryJobSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQEntryJobSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/RFQEntryJobSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQEntryJobSearches_Company_JobNum(Company, JobNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQEntryJobSearch item
   Description: Calls GetByID to retrieve the RFQEntryJobSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQEntryJobSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/RFQEntryJobSearches(" + Company + "," + JobNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQEntryJobSearches_Company_JobNum(Company, JobNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQEntryJobSearch for the service
   Description: Calls UpdateExt to update RFQEntryJobSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQEntryJobSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/RFQEntryJobSearches(" + Company + "," + JobNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQEntryJobSearches_Company_JobNum(Company, JobNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQEntryJobSearch item
   Description: Call UpdateExt to delete RFQEntryJobSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQEntryJobSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/RFQEntryJobSearches(" + Company + "," + JobNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJobHead, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseJobHead=" + whereClauseJobHead
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(jobNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobHeadRow] = obj["value"]
      pass

class Erp_Tablesets_JobHeadListRow:
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
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.SOExists:bool = obj["SOExists"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Part Description  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """  Track Dimension  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Track Lots  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Track Serial Num  """  
      self.EquipOEM:str = obj["EquipOEM"]
      self.EquipModel:str = obj["EquipModel"]
      self.EquipTypeID:str = obj["EquipTypeID"]
      self.EquipLocID:str = obj["EquipLocID"]
      self.PMJob:bool = obj["PMJob"]
      """  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  """  
      self.EquipDescription:str = obj["EquipDescription"]
      self.JobTypeName:str = obj["JobTypeName"]
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttrDescription:str = obj["AttrDescription"]
      """  Description of values in set  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobHeadRow:
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
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LockQty:bool = obj["LockQty"]
      """  Indicates that the quantity on this job is locked  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  """  
      self.PlannedActionDate:str = obj["PlannedActionDate"]
      """  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  """  
      self.PlannedKitDate:str = obj["PlannedKitDate"]
      """  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.OrigProdQty:int = obj["OrigProdQty"]
      """  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  """  
      self.PreserveOrigQtys:bool = obj["PreserveOrigQtys"]
      """  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  """  
      self.NoAutoCompletion:bool = obj["NoAutoCompletion"]
      """  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  """  
      self.NoAutoClosing:bool = obj["NoAutoClosing"]
      """  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user that created this Job.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that this Job was created.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of PDM parts.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.SplitMfgCostElements:bool = obj["SplitMfgCostElements"]
      """  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Num. Used for alternate serial mask support.  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.RoughCutScheduled:bool = obj["RoughCutScheduled"]
      """  Indicates if the job was rough cut scheduled.  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.MaintPriority:str = obj["MaintPriority"]
      """  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  """  
      self.SplitJob:bool = obj["SplitJob"]
      """  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  """  
      self.NumberSource:bool = obj["NumberSource"]
      """  Indicates the type of prefix which is used for create jobs in MRP  """  
      self.CloseMeterReading:int = obj["CloseMeterReading"]
      """  The Meter Reading value entered at time of Job Closing.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.Forward:bool = obj["Forward"]
      """  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  """  
      self.SchedSeq:int = obj["SchedSeq"]
      """  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.PAAExists:bool = obj["PAAExists"]
      """  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  """  
      self.DtlsWithinLeadTime:bool = obj["DtlsWithinLeadTime"]
      """  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RoughCut:bool = obj["RoughCut"]
      """  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  """  
      self.PlanGUID:str = obj["PlanGUID"]
      """  PlanGUID  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.LastChangedBy:str = obj["LastChangedBy"]
      """  LastChangedBy  """  
      self.LastChangedOn:str = obj["LastChangedOn"]
      """  LastChangedOn  """  
      self.EPMExportLevel:int = obj["EPMExportLevel"]
      """  EPMExportLevel  """  
      self.JobWorkflowState:str = obj["JobWorkflowState"]
      """  JobWorkflowState  """  
      self.JobCSR:str = obj["JobCSR"]
      """  JobCSR  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LastExternalMESDate:str = obj["LastExternalMESDate"]
      """  LastExternalMESDate  """  
      self.LastScheduleDate:str = obj["LastScheduleDate"]
      """  LastScheduleDate  """  
      self.LastScheduleProc:str = obj["LastScheduleProc"]
      """  LastScheduleProc  """  
      self.SchedPriority:int = obj["SchedPriority"]
      """  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.DaysLate:int = obj["DaysLate"]
      """  It indicates the days a job is going to be late in relation to its required due date  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.SyncReqBy:bool = obj["SyncReqBy"]
      """  SyncReqBy  """  
      self.CustName:str = obj["CustName"]
      """  CustName  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.IsCSRSet:bool = obj["IsCSRSet"]
      """  IsCSRSet  """  
      self.UnReadyCostProcess:bool = obj["UnReadyCostProcess"]
      """  UnReadyCostProcess  """  
      self.ProcSuspendedUpdates:str = obj["ProcSuspendedUpdates"]
      """  ProcSuspendedUpdates  """  
      self.ProjProcessedDate:str = obj["ProjProcessedDate"]
      """  DateTime field to indicate when this record has been read by project analysis process  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job is ready to be fulfilled.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMServiceReportID:str = obj["FSMServiceReportID"]
      """  FSMServiceReportID  """  
      self.AdvanceLaborRate:bool = obj["AdvanceLaborRate"]
      self.dspReadyCostProcess:bool = obj["dspReadyCostProcess"]
      """  Calculated field is set Not UnReadyCostProcess  """  
      self.EnableJobEngineered:bool = obj["EnableJobEngineered"]
      """  Determine if jobengineered is enabled or disabled.  """  
      self.EnableJobFirm:bool = obj["EnableJobFirm"]
      """  Should JobFirm be enabled or disabled?  """  
      self.EnableJobReleased:bool = obj["EnableJobReleased"]
      """  Determine if jobreleased is enabled or disabled.  """  
      self.EnableMaterialStatus:bool = obj["EnableMaterialStatus"]
      self.EnableProject:bool = obj["EnableProject"]
      self.EngineerAllowed:bool = obj["EngineerAllowed"]
      """  Is the job allowed to be engineered?  """  
      self.EquipLocDesc:str = obj["EquipLocDesc"]
      self.ExtUpdated:bool = obj["ExtUpdated"]
      """  If some fields except ToFirm have been updated  """  
      self.FinalOpDueDate:str = obj["FinalOpDueDate"]
      """   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  """  
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  """  
      self.HasPlanAsAsm:bool = obj["HasPlanAsAsm"]
      """  Job has at least one assembly with flag Plan as Assembly.  """  
      self.HeaderSensitive:bool = obj["HeaderSensitive"]
      """  Depending on the engineered job flag, is the header information enabled?  """  
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      """  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  """  
      self.JobTypeName:str = obj["JobTypeName"]
      self.KitTime:int = obj["KitTime"]
      """  If part is backflush the kit time is ignored.  """  
      self.LockedQty:bool = obj["LockedQty"]
      """  Locked Qty Flag  """  
      self.NewMeter:int = obj["NewMeter"]
      self.OldJobNum:str = obj["OldJobNum"]
      """  The old Job Number when JobFirm is changed from no to yes.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The order qty  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      """  Logical field signifying whether JobHead.PartNum is a valid part master part.  """  
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.PMJob:bool = obj["PMJob"]
      """  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  """  
      self.ProcessModeDescription:str = obj["ProcessModeDescription"]
      """  Process Mode Description  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  Receive Time field for Job Part entered on Job  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SOExists:bool = obj["SOExists"]
      self.StockQty:int = obj["StockQty"]
      self.ToFirm:bool = obj["ToFirm"]
      """  To be Firmed  """  
      self.XRefPartTypeDesc:str = obj["XRefPartTypeDesc"]
      """  Description for XRefPartType  """  
      self.ChangeDescription:str = obj["ChangeDescription"]
      """  The audit change description for the jobaudit record.  """  
      self.ClearDataset:bool = obj["ClearDataset"]
      self.IsCoPart:bool = obj["IsCoPart"]
      """  True if more than one co-part exists  """  
      self.PartRevProcessMfgID:str = obj["PartRevProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.PartRevProcessMfgType:str = obj["PartRevProcessMfgType"]
      """  Type of Process Manufacturing.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Service Job has to be synchronized with Epicor FSI application.  """  
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
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   jobNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JobHeadListRow:
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
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.SOExists:bool = obj["SOExists"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Part Description  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """  Track Dimension  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Track Lots  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Track Serial Num  """  
      self.EquipOEM:str = obj["EquipOEM"]
      self.EquipModel:str = obj["EquipModel"]
      self.EquipTypeID:str = obj["EquipTypeID"]
      self.EquipLocID:str = obj["EquipLocID"]
      self.PMJob:bool = obj["PMJob"]
      """  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  """  
      self.EquipDescription:str = obj["EquipDescription"]
      self.JobTypeName:str = obj["JobTypeName"]
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttrDescription:str = obj["AttrDescription"]
      """  Description of values in set  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobHeadListTableset:
   def __init__(self, obj):
      self.JobHeadList:list[Erp_Tablesets_JobHeadListRow] = obj["JobHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobHeadRow:
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
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LockQty:bool = obj["LockQty"]
      """  Indicates that the quantity on this job is locked  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  """  
      self.PlannedActionDate:str = obj["PlannedActionDate"]
      """  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  """  
      self.PlannedKitDate:str = obj["PlannedKitDate"]
      """  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.OrigProdQty:int = obj["OrigProdQty"]
      """  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  """  
      self.PreserveOrigQtys:bool = obj["PreserveOrigQtys"]
      """  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  """  
      self.NoAutoCompletion:bool = obj["NoAutoCompletion"]
      """  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  """  
      self.NoAutoClosing:bool = obj["NoAutoClosing"]
      """  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user that created this Job.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that this Job was created.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of PDM parts.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.SplitMfgCostElements:bool = obj["SplitMfgCostElements"]
      """  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Num. Used for alternate serial mask support.  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.RoughCutScheduled:bool = obj["RoughCutScheduled"]
      """  Indicates if the job was rough cut scheduled.  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.MaintPriority:str = obj["MaintPriority"]
      """  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  """  
      self.SplitJob:bool = obj["SplitJob"]
      """  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  """  
      self.NumberSource:bool = obj["NumberSource"]
      """  Indicates the type of prefix which is used for create jobs in MRP  """  
      self.CloseMeterReading:int = obj["CloseMeterReading"]
      """  The Meter Reading value entered at time of Job Closing.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.Forward:bool = obj["Forward"]
      """  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  """  
      self.SchedSeq:int = obj["SchedSeq"]
      """  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.PAAExists:bool = obj["PAAExists"]
      """  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  """  
      self.DtlsWithinLeadTime:bool = obj["DtlsWithinLeadTime"]
      """  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RoughCut:bool = obj["RoughCut"]
      """  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  """  
      self.PlanGUID:str = obj["PlanGUID"]
      """  PlanGUID  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.LastChangedBy:str = obj["LastChangedBy"]
      """  LastChangedBy  """  
      self.LastChangedOn:str = obj["LastChangedOn"]
      """  LastChangedOn  """  
      self.EPMExportLevel:int = obj["EPMExportLevel"]
      """  EPMExportLevel  """  
      self.JobWorkflowState:str = obj["JobWorkflowState"]
      """  JobWorkflowState  """  
      self.JobCSR:str = obj["JobCSR"]
      """  JobCSR  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LastExternalMESDate:str = obj["LastExternalMESDate"]
      """  LastExternalMESDate  """  
      self.LastScheduleDate:str = obj["LastScheduleDate"]
      """  LastScheduleDate  """  
      self.LastScheduleProc:str = obj["LastScheduleProc"]
      """  LastScheduleProc  """  
      self.SchedPriority:int = obj["SchedPriority"]
      """  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.DaysLate:int = obj["DaysLate"]
      """  It indicates the days a job is going to be late in relation to its required due date  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.SyncReqBy:bool = obj["SyncReqBy"]
      """  SyncReqBy  """  
      self.CustName:str = obj["CustName"]
      """  CustName  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.IsCSRSet:bool = obj["IsCSRSet"]
      """  IsCSRSet  """  
      self.UnReadyCostProcess:bool = obj["UnReadyCostProcess"]
      """  UnReadyCostProcess  """  
      self.ProcSuspendedUpdates:str = obj["ProcSuspendedUpdates"]
      """  ProcSuspendedUpdates  """  
      self.ProjProcessedDate:str = obj["ProjProcessedDate"]
      """  DateTime field to indicate when this record has been read by project analysis process  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job is ready to be fulfilled.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMServiceReportID:str = obj["FSMServiceReportID"]
      """  FSMServiceReportID  """  
      self.AdvanceLaborRate:bool = obj["AdvanceLaborRate"]
      self.dspReadyCostProcess:bool = obj["dspReadyCostProcess"]
      """  Calculated field is set Not UnReadyCostProcess  """  
      self.EnableJobEngineered:bool = obj["EnableJobEngineered"]
      """  Determine if jobengineered is enabled or disabled.  """  
      self.EnableJobFirm:bool = obj["EnableJobFirm"]
      """  Should JobFirm be enabled or disabled?  """  
      self.EnableJobReleased:bool = obj["EnableJobReleased"]
      """  Determine if jobreleased is enabled or disabled.  """  
      self.EnableMaterialStatus:bool = obj["EnableMaterialStatus"]
      self.EnableProject:bool = obj["EnableProject"]
      self.EngineerAllowed:bool = obj["EngineerAllowed"]
      """  Is the job allowed to be engineered?  """  
      self.EquipLocDesc:str = obj["EquipLocDesc"]
      self.ExtUpdated:bool = obj["ExtUpdated"]
      """  If some fields except ToFirm have been updated  """  
      self.FinalOpDueDate:str = obj["FinalOpDueDate"]
      """   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  """  
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  """  
      self.HasPlanAsAsm:bool = obj["HasPlanAsAsm"]
      """  Job has at least one assembly with flag Plan as Assembly.  """  
      self.HeaderSensitive:bool = obj["HeaderSensitive"]
      """  Depending on the engineered job flag, is the header information enabled?  """  
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      """  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  """  
      self.JobTypeName:str = obj["JobTypeName"]
      self.KitTime:int = obj["KitTime"]
      """  If part is backflush the kit time is ignored.  """  
      self.LockedQty:bool = obj["LockedQty"]
      """  Locked Qty Flag  """  
      self.NewMeter:int = obj["NewMeter"]
      self.OldJobNum:str = obj["OldJobNum"]
      """  The old Job Number when JobFirm is changed from no to yes.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The order qty  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      """  Logical field signifying whether JobHead.PartNum is a valid part master part.  """  
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.PMJob:bool = obj["PMJob"]
      """  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  """  
      self.ProcessModeDescription:str = obj["ProcessModeDescription"]
      """  Process Mode Description  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  Receive Time field for Job Part entered on Job  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SOExists:bool = obj["SOExists"]
      self.StockQty:int = obj["StockQty"]
      self.ToFirm:bool = obj["ToFirm"]
      """  To be Firmed  """  
      self.XRefPartTypeDesc:str = obj["XRefPartTypeDesc"]
      """  Description for XRefPartType  """  
      self.ChangeDescription:str = obj["ChangeDescription"]
      """  The audit change description for the jobaudit record.  """  
      self.ClearDataset:bool = obj["ClearDataset"]
      self.IsCoPart:bool = obj["IsCoPart"]
      """  True if more than one co-part exists  """  
      self.PartRevProcessMfgID:str = obj["PartRevProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.PartRevProcessMfgType:str = obj["PartRevProcessMfgType"]
      """  Type of Process Manufacturing.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Service Job has to be synchronized with Epicor FSI application.  """  
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
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQEntryJobSearchTableset:
   def __init__(self, obj):
      self.JobHead:list[Erp_Tablesets_JobHeadRow] = obj["JobHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRFQEntryJobSearchTableset:
   def __init__(self, obj):
      self.JobHead:list[Erp_Tablesets_JobHeadRow] = obj["JobHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   jobNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQEntryJobSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQEntryJobSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQEntryJobSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewJobHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryJobSearchTableset] = obj["ds"]
      pass

class GetNewJobHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryJobSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseJobHead
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobHead:str = obj["whereClauseJobHead"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQEntryJobSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtRFQEntryJobSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRFQEntryJobSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryJobSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryJobSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

