import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PCIDJobOperSearchSvc
# Description: Search object for Job Operations
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PCIDJobOperSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PCIDJobOperSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCIDJobOperSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobOperRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/PCIDJobOperSearches",headers=creds) as resp:
           return await resp.json()

async def post_PCIDJobOperSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCIDJobOperSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobOperRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobOperRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/PCIDJobOperSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PCIDJobOperSearches_Company_JobNum_AssemblySeq_OprSeq(Company, JobNum, AssemblySeq, OprSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCIDJobOperSearch item
   Description: Calls GetByID to retrieve the PCIDJobOperSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCIDJobOperSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobOperRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/PCIDJobOperSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PCIDJobOperSearches_Company_JobNum_AssemblySeq_OprSeq(Company, JobNum, AssemblySeq, OprSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PCIDJobOperSearch for the service
   Description: Calls UpdateExt to update PCIDJobOperSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCIDJobOperSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobOperRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/PCIDJobOperSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PCIDJobOperSearches_Company_JobNum_AssemblySeq_OprSeq(Company, JobNum, AssemblySeq, OprSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PCIDJobOperSearch item
   Description: Call UpdateExt to delete PCIDJobOperSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCIDJobOperSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/PCIDJobOperSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCIDJobOperListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJobOper, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseJobOper=" + whereClauseJobOper
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(jobNum, assemblySeq, oprSeq, epicorHeaders = None):
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
   params += "oprSeq=" + oprSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_PCIDJobOperSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PCIDJobOperSearch
   Description: Purpose:
Parameters:
<param name="WhereClause">JobOper Search clause</param><returns>JobOper List Data Set</returns><param name="WhoCalled">Who Called</param><param name="pageSize">Page size</param><param name="absolutePage">Absolute page</param><param name="morePages">More Pages</param>
Notes:
   OperationID: PCIDJobOperSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PCIDJobOperSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PCIDJobOperSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PCIDJobOperListSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PCIDJobOperListSearch
   Description: Purpose:
Parameters:
<param name="WhereClause">JobOper Search clause</param><returns>JobOper List Data Set</returns><param name="WhoCalled">Who Called</param><param name="pageSize">Page size</param><param name="absolutePage">Absolute page</param><param name="morePages">More Pages</param>
Notes:
   OperationID: PCIDJobOperListSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PCIDJobOperListSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PCIDJobOperListSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobOper(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobOper
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobOper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobOper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobOper_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCIDJobOperSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobOperRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobOperRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCIDJobOperListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCIDJobOperListRow] = obj["value"]
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

class Erp_Tablesets_PCIDJobOperListRow:
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
      self.JobReleased:bool = obj["JobReleased"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.Resource:str = obj["Resource"]
      self.JobClosed:bool = obj["JobClosed"]
      self.BitFlag:int = obj["BitFlag"]
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
   oprSeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
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

class Erp_Tablesets_PCIDJobOperListRow:
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
      self.JobReleased:bool = obj["JobReleased"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.Resource:str = obj["Resource"]
      self.JobClosed:bool = obj["JobClosed"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCIDJobOperListTableset:
   def __init__(self, obj):
      self.PCIDJobOperList:list[Erp_Tablesets_PCIDJobOperListRow] = obj["PCIDJobOperList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PCIDJobOperSearchTableset:
   def __init__(self, obj):
      self.JobOper:list[Erp_Tablesets_JobOperRow] = obj["JobOper"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPCIDJobOperSearchTableset:
   def __init__(self, obj):
      self.JobOper:list[Erp_Tablesets_JobOperRow] = obj["JobOper"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   jobNum
   assemblySeq
   oprSeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCIDJobOperSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PCIDJobOperSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PCIDJobOperSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PCIDJobOperListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewJobOper_input:
   """ Required : 
   ds
   jobNum
   assemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCIDJobOperSearchTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class GetNewJobOper_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCIDJobOperSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseJobOper
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobOper:str = obj["whereClauseJobOper"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCIDJobOperSearchTableset] = obj["returnObj"]
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

class PCIDJobOperListSearch_input:
   """ Required : 
   WhereClause
   WhoCalled
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      self.WhoCalled:str = obj["WhoCalled"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class PCIDJobOperListSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCIDJobOperListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class PCIDJobOperSearch_input:
   """ Required : 
   WhereClause
   WhoCalled
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      self.WhoCalled:str = obj["WhoCalled"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class PCIDJobOperSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCIDJobOperListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPCIDJobOperSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPCIDJobOperSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCIDJobOperSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCIDJobOperSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

