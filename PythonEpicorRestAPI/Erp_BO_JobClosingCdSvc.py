import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JobClosingCdSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_JobClosingCds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JobClosingCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobClosingCds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobClosingCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/JobClosingCds",headers=creds) as resp:
           return await resp.json()

async def post_JobClosingCds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobClosingCds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobClosingCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobClosingCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/JobClosingCds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JobClosingCds_Company_JobClosingCode(Company, JobClosingCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JobClosingCd item
   Description: Calls GetByID to retrieve the JobClosingCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobClosingCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobClosingCode: Desc: JobClosingCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobClosingCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/JobClosingCds(" + Company + "," + JobClosingCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JobClosingCds_Company_JobClosingCode(Company, JobClosingCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JobClosingCd for the service
   Description: Calls UpdateExt to update JobClosingCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobClosingCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobClosingCode: Desc: JobClosingCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobClosingCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/JobClosingCds(" + Company + "," + JobClosingCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JobClosingCds_Company_JobClosingCode(Company, JobClosingCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JobClosingCd item
   Description: Call UpdateExt to delete JobClosingCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobClosingCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobClosingCode: Desc: JobClosingCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/JobClosingCds(" + Company + "," + JobClosingCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobClosingCdListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJobClosingCd, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseJobClosingCd=" + whereClauseJobClosingCd
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(jobClosingCode, epicorHeaders = None):
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
   params += "jobClosingCode=" + jobClosingCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobClosingCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobClosingCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobClosingCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobClosingCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobClosingCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobClosingCdListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobClosingCdListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobClosingCdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobClosingCdRow] = obj["value"]
      pass

class Erp_Tablesets_JobClosingCdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosingCode:str = obj["JobClosingCode"]
      """  A unique code to identify the job closing record  """  
      self.Description:str = obj["Description"]
      """  Description field  """  
      self.JobCompletion:bool = obj["JobCompletion"]
      """  Indicates that this job closing record can be used for job completion.  """  
      self.JobClosing:bool = obj["JobClosing"]
      """  Indicates that this job closing record can be used for job closing.  """  
      self.JobCompletionDefault:bool = obj["JobCompletionDefault"]
      """  If set to yes then this record has the default values for the job completion process.  """  
      self.JobClosingDefault:bool = obj["JobClosingDefault"]
      """  If set to yes then this  record has the default values for the job closing process.  """  
      self.MtlQtyPercent:int = obj["MtlQtyPercent"]
      """  Material Quantity Under Percent. Threshold for the Material Quantity under completed.  """  
      self.MtlCostPercent:int = obj["MtlCostPercent"]
      """  Material Cost Under Percent. Threshold for the Material Cost under completed.  """  
      self.OprQtyPercent:int = obj["OprQtyPercent"]
      """  Operation Quantity Under Percent. Threshold for the Operation Quantity under completed.  """  
      self.OprCostPercent:int = obj["OprCostPercent"]
      """  Operation Cost Under Percent. Threshold for the Operation Cost under completed.  """  
      self.SubQtyPercent:int = obj["SubQtyPercent"]
      """  SubContract Quantity Under Percent. Threshold for the SubContract Quantity under completed.  """  
      self.SubCostPercent:int = obj["SubCostPercent"]
      """  SubContract Cost Percent. Threshold for the SubContract Cost under completed.  """  
      self.MtlQtyOverPercent:int = obj["MtlQtyOverPercent"]
      """  Material Quantity Percent. Threshold for the Material Quantity  over completed.  """  
      self.MtlCostOverPercent:int = obj["MtlCostOverPercent"]
      """  Material Cost Over Percent. Threshold for the Material Cost over completed.  """  
      self.OprQtyOverPercent:int = obj["OprQtyOverPercent"]
      """  Operation Quantity Over Percent. Threshold for the Operation Quantity over completed.  """  
      self.OprCostOverPercent:int = obj["OprCostOverPercent"]
      """  Operation Cost Over Percent. Threshold for the Operation Cost over completed.  """  
      self.SubQtyOverPercent:int = obj["SubQtyOverPercent"]
      """  SubContract Quantity Over Percent. Threshold for the SubContract Quantity over completed.  """  
      self.SubCostOverPercent:int = obj["SubCostOverPercent"]
      """  SubContract Cost Over Percent. Threshold for the SubContract Cost over completed.  """  
      self.JobCostAmount:int = obj["JobCostAmount"]
      """  Job Cost Under Amount. Under threshold for the Total Job Cost.  """  
      self.JobCostOverAmount:int = obj["JobCostOverAmount"]
      """  Job Cost Over Amount. Over Threshold for the Total Job Cost.  """  
      self.Backflush:bool = obj["Backflush"]
      """  If Set to yes then the materials will be backflushed during the job completion process. (for future use).  """  
      self.PendingInspection:bool = obj["PendingInspection"]
      """  If set to yes then jobs pending for inspection are completed in the auto completion process.  The auto closing process will not process any pending inspection jobs.  """  
      self.MultiplePlants:bool = obj["MultiplePlants"]
      """  If set to yes then job operations using resources in other Sites than the job header Site are allowed to be completed in the auto completion process and the auto closing process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobClosingCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosingCode:str = obj["JobClosingCode"]
      """  A unique code to identify the job closing record  """  
      self.Description:str = obj["Description"]
      """  Description field  """  
      self.JobCompletion:bool = obj["JobCompletion"]
      """  Indicates that this job closing record can be used for job completion.  """  
      self.JobClosing:bool = obj["JobClosing"]
      """  Indicates that this job closing record can be used for job closing.  """  
      self.JobCompletionDefault:bool = obj["JobCompletionDefault"]
      """  If set to yes then this record has the default values for the job completion process.  """  
      self.JobClosingDefault:bool = obj["JobClosingDefault"]
      """  If set to yes then this  record has the default values for the job closing process.  """  
      self.MtlQtyPercent:int = obj["MtlQtyPercent"]
      """  Material Quantity Under Percent. Threshold for the Material Quantity under completed.  """  
      self.MtlCostPercent:int = obj["MtlCostPercent"]
      """  Material Cost Under Percent. Threshold for the Material Cost under completed.  """  
      self.OprQtyPercent:int = obj["OprQtyPercent"]
      """  Operation Quantity Under Percent. Threshold for the Operation Quantity under completed.  """  
      self.OprCostPercent:int = obj["OprCostPercent"]
      """  Operation Cost Under Percent. Threshold for the Operation Cost under completed.  """  
      self.SubQtyPercent:int = obj["SubQtyPercent"]
      """  SubContract Quantity Under Percent. Threshold for the SubContract Quantity under completed.  """  
      self.SubCostPercent:int = obj["SubCostPercent"]
      """  SubContract Cost Percent. Threshold for the SubContract Cost under completed.  """  
      self.MtlQtyOverPercent:int = obj["MtlQtyOverPercent"]
      """  Material Quantity Percent. Threshold for the Material Quantity  over completed.  """  
      self.MtlCostOverPercent:int = obj["MtlCostOverPercent"]
      """  Material Cost Over Percent. Threshold for the Material Cost over completed.  """  
      self.OprQtyOverPercent:int = obj["OprQtyOverPercent"]
      """  Operation Quantity Over Percent. Threshold for the Operation Quantity over completed.  """  
      self.OprCostOverPercent:int = obj["OprCostOverPercent"]
      """  Operation Cost Over Percent. Threshold for the Operation Cost over completed.  """  
      self.SubQtyOverPercent:int = obj["SubQtyOverPercent"]
      """  SubContract Quantity Over Percent. Threshold for the SubContract Quantity over completed.  """  
      self.SubCostOverPercent:int = obj["SubCostOverPercent"]
      """  SubContract Cost Over Percent. Threshold for the SubContract Cost over completed.  """  
      self.JobCostAmount:int = obj["JobCostAmount"]
      """  Job Cost Under Amount. Under threshold for the Total Job Cost.  """  
      self.JobCostOverAmount:int = obj["JobCostOverAmount"]
      """  Job Cost Over Amount. Over Threshold for the Total Job Cost.  """  
      self.Backflush:bool = obj["Backflush"]
      """  If Set to yes then the materials will be backflushed during the job completion process. (for future use).  """  
      self.PendingInspection:bool = obj["PendingInspection"]
      """  If set to yes then jobs pending for inspection are completed in the auto completion process.  The auto closing process will not process any pending inspection jobs.  """  
      self.MultiplePlants:bool = obj["MultiplePlants"]
      """  If set to yes then job operations using resources in other Sites than the job header Site are allowed to be completed in the auto completion process and the auto closing process.  """  
      self.IgnoreCompleted:bool = obj["IgnoreCompleted"]
      """  IgnoreCompleted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   jobClosingCode
   """  
   def __init__(self, obj):
      self.jobClosingCode:str = obj["jobClosingCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JobClosingCdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosingCode:str = obj["JobClosingCode"]
      """  A unique code to identify the job closing record  """  
      self.Description:str = obj["Description"]
      """  Description field  """  
      self.JobCompletion:bool = obj["JobCompletion"]
      """  Indicates that this job closing record can be used for job completion.  """  
      self.JobClosing:bool = obj["JobClosing"]
      """  Indicates that this job closing record can be used for job closing.  """  
      self.JobCompletionDefault:bool = obj["JobCompletionDefault"]
      """  If set to yes then this record has the default values for the job completion process.  """  
      self.JobClosingDefault:bool = obj["JobClosingDefault"]
      """  If set to yes then this  record has the default values for the job closing process.  """  
      self.MtlQtyPercent:int = obj["MtlQtyPercent"]
      """  Material Quantity Under Percent. Threshold for the Material Quantity under completed.  """  
      self.MtlCostPercent:int = obj["MtlCostPercent"]
      """  Material Cost Under Percent. Threshold for the Material Cost under completed.  """  
      self.OprQtyPercent:int = obj["OprQtyPercent"]
      """  Operation Quantity Under Percent. Threshold for the Operation Quantity under completed.  """  
      self.OprCostPercent:int = obj["OprCostPercent"]
      """  Operation Cost Under Percent. Threshold for the Operation Cost under completed.  """  
      self.SubQtyPercent:int = obj["SubQtyPercent"]
      """  SubContract Quantity Under Percent. Threshold for the SubContract Quantity under completed.  """  
      self.SubCostPercent:int = obj["SubCostPercent"]
      """  SubContract Cost Percent. Threshold for the SubContract Cost under completed.  """  
      self.MtlQtyOverPercent:int = obj["MtlQtyOverPercent"]
      """  Material Quantity Percent. Threshold for the Material Quantity  over completed.  """  
      self.MtlCostOverPercent:int = obj["MtlCostOverPercent"]
      """  Material Cost Over Percent. Threshold for the Material Cost over completed.  """  
      self.OprQtyOverPercent:int = obj["OprQtyOverPercent"]
      """  Operation Quantity Over Percent. Threshold for the Operation Quantity over completed.  """  
      self.OprCostOverPercent:int = obj["OprCostOverPercent"]
      """  Operation Cost Over Percent. Threshold for the Operation Cost over completed.  """  
      self.SubQtyOverPercent:int = obj["SubQtyOverPercent"]
      """  SubContract Quantity Over Percent. Threshold for the SubContract Quantity over completed.  """  
      self.SubCostOverPercent:int = obj["SubCostOverPercent"]
      """  SubContract Cost Over Percent. Threshold for the SubContract Cost over completed.  """  
      self.JobCostAmount:int = obj["JobCostAmount"]
      """  Job Cost Under Amount. Under threshold for the Total Job Cost.  """  
      self.JobCostOverAmount:int = obj["JobCostOverAmount"]
      """  Job Cost Over Amount. Over Threshold for the Total Job Cost.  """  
      self.Backflush:bool = obj["Backflush"]
      """  If Set to yes then the materials will be backflushed during the job completion process. (for future use).  """  
      self.PendingInspection:bool = obj["PendingInspection"]
      """  If set to yes then jobs pending for inspection are completed in the auto completion process.  The auto closing process will not process any pending inspection jobs.  """  
      self.MultiplePlants:bool = obj["MultiplePlants"]
      """  If set to yes then job operations using resources in other Sites than the job header Site are allowed to be completed in the auto completion process and the auto closing process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobClosingCdListTableset:
   def __init__(self, obj):
      self.JobClosingCdList:list[Erp_Tablesets_JobClosingCdListRow] = obj["JobClosingCdList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobClosingCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosingCode:str = obj["JobClosingCode"]
      """  A unique code to identify the job closing record  """  
      self.Description:str = obj["Description"]
      """  Description field  """  
      self.JobCompletion:bool = obj["JobCompletion"]
      """  Indicates that this job closing record can be used for job completion.  """  
      self.JobClosing:bool = obj["JobClosing"]
      """  Indicates that this job closing record can be used for job closing.  """  
      self.JobCompletionDefault:bool = obj["JobCompletionDefault"]
      """  If set to yes then this record has the default values for the job completion process.  """  
      self.JobClosingDefault:bool = obj["JobClosingDefault"]
      """  If set to yes then this  record has the default values for the job closing process.  """  
      self.MtlQtyPercent:int = obj["MtlQtyPercent"]
      """  Material Quantity Under Percent. Threshold for the Material Quantity under completed.  """  
      self.MtlCostPercent:int = obj["MtlCostPercent"]
      """  Material Cost Under Percent. Threshold for the Material Cost under completed.  """  
      self.OprQtyPercent:int = obj["OprQtyPercent"]
      """  Operation Quantity Under Percent. Threshold for the Operation Quantity under completed.  """  
      self.OprCostPercent:int = obj["OprCostPercent"]
      """  Operation Cost Under Percent. Threshold for the Operation Cost under completed.  """  
      self.SubQtyPercent:int = obj["SubQtyPercent"]
      """  SubContract Quantity Under Percent. Threshold for the SubContract Quantity under completed.  """  
      self.SubCostPercent:int = obj["SubCostPercent"]
      """  SubContract Cost Percent. Threshold for the SubContract Cost under completed.  """  
      self.MtlQtyOverPercent:int = obj["MtlQtyOverPercent"]
      """  Material Quantity Percent. Threshold for the Material Quantity  over completed.  """  
      self.MtlCostOverPercent:int = obj["MtlCostOverPercent"]
      """  Material Cost Over Percent. Threshold for the Material Cost over completed.  """  
      self.OprQtyOverPercent:int = obj["OprQtyOverPercent"]
      """  Operation Quantity Over Percent. Threshold for the Operation Quantity over completed.  """  
      self.OprCostOverPercent:int = obj["OprCostOverPercent"]
      """  Operation Cost Over Percent. Threshold for the Operation Cost over completed.  """  
      self.SubQtyOverPercent:int = obj["SubQtyOverPercent"]
      """  SubContract Quantity Over Percent. Threshold for the SubContract Quantity over completed.  """  
      self.SubCostOverPercent:int = obj["SubCostOverPercent"]
      """  SubContract Cost Over Percent. Threshold for the SubContract Cost over completed.  """  
      self.JobCostAmount:int = obj["JobCostAmount"]
      """  Job Cost Under Amount. Under threshold for the Total Job Cost.  """  
      self.JobCostOverAmount:int = obj["JobCostOverAmount"]
      """  Job Cost Over Amount. Over Threshold for the Total Job Cost.  """  
      self.Backflush:bool = obj["Backflush"]
      """  If Set to yes then the materials will be backflushed during the job completion process. (for future use).  """  
      self.PendingInspection:bool = obj["PendingInspection"]
      """  If set to yes then jobs pending for inspection are completed in the auto completion process.  The auto closing process will not process any pending inspection jobs.  """  
      self.MultiplePlants:bool = obj["MultiplePlants"]
      """  If set to yes then job operations using resources in other Sites than the job header Site are allowed to be completed in the auto completion process and the auto closing process.  """  
      self.IgnoreCompleted:bool = obj["IgnoreCompleted"]
      """  IgnoreCompleted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobClosingCdTableset:
   def __init__(self, obj):
      self.JobClosingCd:list[Erp_Tablesets_JobClosingCdRow] = obj["JobClosingCd"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtJobClosingCdTableset:
   def __init__(self, obj):
      self.JobClosingCd:list[Erp_Tablesets_JobClosingCdRow] = obj["JobClosingCd"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   jobClosingCode
   """  
   def __init__(self, obj):
      self.jobClosingCode:str = obj["jobClosingCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobClosingCdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobClosingCdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobClosingCdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobClosingCdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewJobClosingCd_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingCdTableset] = obj["ds"]
      pass

class GetNewJobClosingCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingCdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseJobClosingCd
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobClosingCd:str = obj["whereClauseJobClosingCd"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobClosingCdTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtJobClosingCdTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJobClosingCdTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingCdTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobClosingCdTableset] = obj["ds"]
      pass

      """  output parameters  """  

