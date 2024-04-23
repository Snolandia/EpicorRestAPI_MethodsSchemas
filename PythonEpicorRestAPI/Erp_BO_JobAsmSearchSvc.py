import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JobAsmSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_JobAsmSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JobAsmSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobAsmSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobAsmblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/JobAsmSearches",headers=creds) as resp:
           return await resp.json()

async def post_JobAsmSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobAsmSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/JobAsmSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JobAsmSearches_Company_JobNum_AssemblySeq(Company, JobNum, AssemblySeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JobAsmSearch item
   Description: Calls GetByID to retrieve the JobAsmSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobAsmSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/JobAsmSearches(" + Company + "," + JobNum + "," + AssemblySeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JobAsmSearches_Company_JobNum_AssemblySeq(Company, JobNum, AssemblySeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JobAsmSearch for the service
   Description: Calls UpdateExt to update JobAsmSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobAsmSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/JobAsmSearches(" + Company + "," + JobNum + "," + AssemblySeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JobAsmSearches_Company_JobNum_AssemblySeq(Company, JobNum, AssemblySeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JobAsmSearch item
   Description: Call UpdateExt to delete JobAsmSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobAsmSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/JobAsmSearches(" + Company + "," + JobNum + "," + AssemblySeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobAsmblListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJobAsmbl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseJobAsmbl=" + whereClauseJobAsmbl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(jobNum, assemblySeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobAsmbl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobAsmbl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobAsmbl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobAsmbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobAsmbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobAsmblListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobAsmblRow] = obj["value"]
      pass

class Erp_Tablesets_JobAsmblListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production quantity required for this assembly per one of it's parent part.  """  
      self.IUM:str = obj["IUM"]
      """  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  """  
      self.PullQty:int = obj["PullQty"]
      """  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  This is the warehouse that the material is allocated against.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Assembly.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  """  
      self.OverRunQty:int = obj["OverRunQty"]
      """  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.DueDate:str = obj["DueDate"]
      """  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  """  
      self.Child:int = obj["Child"]
      """  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date, of this component that was issued from stock.  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total material burden cost to date, of this component that was issued from stock.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.TLALaborCost:int = obj["TLALaborCost"]
      """  This Level Actual Labor Cost.  """  
      self.TLABurdenCost:int = obj["TLABurdenCost"]
      """  This Level Actual Burden Cost.  """  
      self.TLAMaterialCost:int = obj["TLAMaterialCost"]
      """  This Level Actual Material Cost.  """  
      self.TLASubcontractCost:int = obj["TLASubcontractCost"]
      """  This Level Actual Subcontract Cost.  """  
      self.TLAMtlBurCost:int = obj["TLAMtlBurCost"]
      """  This Level Actual Material Burden Cost.  """  
      self.TLASetupHours:int = obj["TLASetupHours"]
      """  This Level Actual Setup Hours.  """  
      self.TLAProdHours:int = obj["TLAProdHours"]
      """  This Level Actual Production Hours.  """  
      self.TLELaborCost:int = obj["TLELaborCost"]
      """  This Level Estimated Labor Cost.  """  
      self.TLEBurdenCost:int = obj["TLEBurdenCost"]
      """  This Level Estimated Burden Cost.  """  
      self.TLEMaterialCost:int = obj["TLEMaterialCost"]
      """  This Level Estimated Material Cost.  """  
      self.TLESubcontractCost:int = obj["TLESubcontractCost"]
      """  This Level Estimated Subcontract Cost.  """  
      self.TLEMtlBurCost:int = obj["TLEMtlBurCost"]
      """  This Level Estimated Material Burden Cost.  """  
      self.TLESetupHours:int = obj["TLESetupHours"]
      """  This Level Estimated Setup Hours.  """  
      self.TLEProdHours:int = obj["TLEProdHours"]
      """  This Level Estimated Production Hours.  """  
      self.LLALaborCost:int = obj["LLALaborCost"]
      """  Lower Level Actual Labor Cost.  """  
      self.LLABurdenCost:int = obj["LLABurdenCost"]
      """  Lower Level Burden Labor Cost.  """  
      self.LLAMaterialCost:int = obj["LLAMaterialCost"]
      """  Lower Level Actual Material Cost.  """  
      self.LLASubcontractCost:int = obj["LLASubcontractCost"]
      """  Lower Level Actual Subcontractor Cost.  """  
      self.LLAMtlBurCost:int = obj["LLAMtlBurCost"]
      """  Lower Level Actual Material Burden Cost.  """  
      self.LLASetupHours:int = obj["LLASetupHours"]
      """  Lower Level Actual Setup Hours.  """  
      self.LLAProdHours:int = obj["LLAProdHours"]
      """  Lower Level Actual Production Hours.  """  
      self.LLELaborCost:int = obj["LLELaborCost"]
      """  Lower Level Estimated Labor Cost.  """  
      self.LLEBurdenCost:int = obj["LLEBurdenCost"]
      """  Lower Level Estimated Burden Cost.  """  
      self.LLEMaterialCost:int = obj["LLEMaterialCost"]
      """  Lower Level Estimated Material Cost.  """  
      self.LLESubcontractCost:int = obj["LLESubcontractCost"]
      """  Lower Level Estimated Subcontract Cost.  """  
      self.LLEMtlBurCost:int = obj["LLEMtlBurCost"]
      """  Lower Level Estimated Material Burden Cost.  """  
      self.LLESetupHours:int = obj["LLESetupHours"]
      """  Lower Level Estimated Setup Hours.  """  
      self.LLEProdHours:int = obj["LLEProdHours"]
      """  Lower Level Estimated Production Hours.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.ReceivedToStock:int = obj["ReceivedToStock"]
      """  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.TLAMaterialLabCost:int = obj["TLAMaterialLabCost"]
      """  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialMtlCost:int = obj["TLAMaterialMtlCost"]
      """  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialSubCost:int = obj["TLAMaterialSubCost"]
      """  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialBurCost:int = obj["TLAMaterialBurCost"]
      """  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.LLAMaterialLabCost:int = obj["LLAMaterialLabCost"]
      """  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialMtlCost:int = obj["LLAMaterialMtlCost"]
      """  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialSubCost:int = obj["LLAMaterialSubCost"]
      """  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialBurCost:int = obj["LLAMaterialBurCost"]
      """  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.TotalMtlMtlCost:int = obj["TotalMtlMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.TotalMtlLabCost:int = obj["TotalMtlLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlSubCost:int = obj["TotalMtlSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlBurCost:int = obj["TotalMtlBurCost"]
      """  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this assembly belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this assembly relates to.  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.OrigRequiredQty:int = obj["OrigRequiredQty"]
      """  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.TLAMaterialMtlBurCost:int = obj["TLAMaterialMtlBurCost"]
      """  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  """  
      self.LLAMaterialMtlBurCost:int = obj["LLAMaterialMtlBurCost"]
      """  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  """  
      self.TLAMfgCompLabCost:int = obj["TLAMfgCompLabCost"]
      """  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlCost:int = obj["TLAMfgCompMtlCost"]
      """  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompSubCost:int = obj["TLAMfgCompSubCost"]
      """  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompBurCost:int = obj["TLAMfgCompBurCost"]
      """  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlBurCost:int = obj["TLAMfgCompMtlBurCost"]
      """  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.LLAMfgCompLabCost:int = obj["LLAMfgCompLabCost"]
      """  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlCost:int = obj["LLAMfgCompMtlCost"]
      """  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompSubCost:int = obj["LLAMfgCompSubCost"]
      """  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompBurCost:int = obj["LLAMfgCompBurCost"]
      """  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlBurCost:int = obj["LLAMfgCompMtlBurCost"]
      """  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.Weight:int = obj["Weight"]
      """  Assembly Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Assembly Weight UOM defaulted from Part Master.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  Original Material Sequence. Used in the configurator.  """  
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      """  Original Rule Tag. Used in the Configurator.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.PlanAsAsm:bool = obj["PlanAsAsm"]
      """  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  """  
      self.PAARef:str = obj["PAARef"]
      """  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  """  
      self.PAAFirm:bool = obj["PAAFirm"]
      """  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      """  Related Operation Description  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Parent PartNum  """  
      self.ParentRev:str = obj["ParentRev"]
      """  Parent RevisionNum  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  Parent Description  """  
      self.AvailableQty:int = obj["AvailableQty"]
      """  Calculated Available Quantity  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  """  
      self.ChildAssemblySeq:int = obj["ChildAssemblySeq"]
      """  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  """  
      self.AddAsmAs:str = obj["AddAsmAs"]
      """  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  The order JobAsmbl records should be displayed.  """  
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.DispIUM:str = obj["DispIUM"]
      """  The internal unit of measure for this assembly.  Same as IUM but readOnly  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      self.bAvailQty:int = obj["bAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.bUseAvailQty:bool = obj["bUseAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.EnableAsmSplitCosts:bool = obj["EnableAsmSplitCosts"]
      """  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  """  
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      """  Description  """  
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production quantity required for this assembly per one of it's parent part.  """  
      self.IUM:str = obj["IUM"]
      """  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  """  
      self.PullQty:int = obj["PullQty"]
      """  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  This is the warehouse that the material is allocated against.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Assembly.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  """  
      self.OverRunQty:int = obj["OverRunQty"]
      """  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.DueDate:str = obj["DueDate"]
      """  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  """  
      self.Child:int = obj["Child"]
      """  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date, of this component that was issued from stock.  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total material burden cost to date, of this component that was issued from stock.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.TLALaborCost:int = obj["TLALaborCost"]
      """  This Level Actual Labor Cost.  """  
      self.TLABurdenCost:int = obj["TLABurdenCost"]
      """  This Level Actual Burden Cost.  """  
      self.TLAMaterialCost:int = obj["TLAMaterialCost"]
      """  This Level Actual Material Cost.  """  
      self.TLASubcontractCost:int = obj["TLASubcontractCost"]
      """  This Level Actual Subcontract Cost.  """  
      self.TLAMtlBurCost:int = obj["TLAMtlBurCost"]
      """  This Level Actual Material Burden Cost.  """  
      self.TLASetupHours:int = obj["TLASetupHours"]
      """  This Level Actual Setup Hours.  """  
      self.TLAProdHours:int = obj["TLAProdHours"]
      """  This Level Actual Production Hours.  """  
      self.TLELaborCost:int = obj["TLELaborCost"]
      """  This Level Estimated Labor Cost.  """  
      self.TLEBurdenCost:int = obj["TLEBurdenCost"]
      """  This Level Estimated Burden Cost.  """  
      self.TLEMaterialCost:int = obj["TLEMaterialCost"]
      """  This Level Estimated Material Cost.  """  
      self.TLESubcontractCost:int = obj["TLESubcontractCost"]
      """  This Level Estimated Subcontract Cost.  """  
      self.TLEMtlBurCost:int = obj["TLEMtlBurCost"]
      """  This Level Estimated Material Burden Cost.  """  
      self.TLESetupHours:int = obj["TLESetupHours"]
      """  This Level Estimated Setup Hours.  """  
      self.TLEProdHours:int = obj["TLEProdHours"]
      """  This Level Estimated Production Hours.  """  
      self.LLALaborCost:int = obj["LLALaborCost"]
      """  Lower Level Actual Labor Cost.  """  
      self.LLABurdenCost:int = obj["LLABurdenCost"]
      """  Lower Level Burden Labor Cost.  """  
      self.LLAMaterialCost:int = obj["LLAMaterialCost"]
      """  Lower Level Actual Material Cost.  """  
      self.LLASubcontractCost:int = obj["LLASubcontractCost"]
      """  Lower Level Actual Subcontractor Cost.  """  
      self.LLAMtlBurCost:int = obj["LLAMtlBurCost"]
      """  Lower Level Actual Material Burden Cost.  """  
      self.LLASetupHours:int = obj["LLASetupHours"]
      """  Lower Level Actual Setup Hours.  """  
      self.LLAProdHours:int = obj["LLAProdHours"]
      """  Lower Level Actual Production Hours.  """  
      self.LLELaborCost:int = obj["LLELaborCost"]
      """  Lower Level Estimated Labor Cost.  """  
      self.LLEBurdenCost:int = obj["LLEBurdenCost"]
      """  Lower Level Estimated Burden Cost.  """  
      self.LLEMaterialCost:int = obj["LLEMaterialCost"]
      """  Lower Level Estimated Material Cost.  """  
      self.LLESubcontractCost:int = obj["LLESubcontractCost"]
      """  Lower Level Estimated Subcontract Cost.  """  
      self.LLEMtlBurCost:int = obj["LLEMtlBurCost"]
      """  Lower Level Estimated Material Burden Cost.  """  
      self.LLESetupHours:int = obj["LLESetupHours"]
      """  Lower Level Estimated Setup Hours.  """  
      self.LLEProdHours:int = obj["LLEProdHours"]
      """  Lower Level Estimated Production Hours.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.ReceivedToStock:int = obj["ReceivedToStock"]
      """  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.TLAMaterialLabCost:int = obj["TLAMaterialLabCost"]
      """  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialMtlCost:int = obj["TLAMaterialMtlCost"]
      """  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialSubCost:int = obj["TLAMaterialSubCost"]
      """  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialBurCost:int = obj["TLAMaterialBurCost"]
      """  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.LLAMaterialLabCost:int = obj["LLAMaterialLabCost"]
      """  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialMtlCost:int = obj["LLAMaterialMtlCost"]
      """  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialSubCost:int = obj["LLAMaterialSubCost"]
      """  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialBurCost:int = obj["LLAMaterialBurCost"]
      """  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.TotalMtlMtlCost:int = obj["TotalMtlMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.TotalMtlLabCost:int = obj["TotalMtlLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlSubCost:int = obj["TotalMtlSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlBurCost:int = obj["TotalMtlBurCost"]
      """  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this assembly belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this assembly relates to.  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.OrigRequiredQty:int = obj["OrigRequiredQty"]
      """  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.TLAMaterialMtlBurCost:int = obj["TLAMaterialMtlBurCost"]
      """  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  """  
      self.LLAMaterialMtlBurCost:int = obj["LLAMaterialMtlBurCost"]
      """  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  """  
      self.TLAMfgCompLabCost:int = obj["TLAMfgCompLabCost"]
      """  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlCost:int = obj["TLAMfgCompMtlCost"]
      """  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompSubCost:int = obj["TLAMfgCompSubCost"]
      """  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompBurCost:int = obj["TLAMfgCompBurCost"]
      """  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlBurCost:int = obj["TLAMfgCompMtlBurCost"]
      """  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.LLAMfgCompLabCost:int = obj["LLAMfgCompLabCost"]
      """  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlCost:int = obj["LLAMfgCompMtlCost"]
      """  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompSubCost:int = obj["LLAMfgCompSubCost"]
      """  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompBurCost:int = obj["LLAMfgCompBurCost"]
      """  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlBurCost:int = obj["LLAMfgCompMtlBurCost"]
      """  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.Weight:int = obj["Weight"]
      """  Assembly Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Assembly Weight UOM defaulted from Part Master.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  Original Material Sequence. Used in the configurator.  """  
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      """  Original Rule Tag. Used in the Configurator.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.PlanAsAsm:bool = obj["PlanAsAsm"]
      """  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  """  
      self.PAARef:str = obj["PAARef"]
      """  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  """  
      self.PAAFirm:bool = obj["PAAFirm"]
      """  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  Reassign Serial Numbers Assembly  """  
      self.TLAODCCost:int = obj["TLAODCCost"]
      """  This Level Actual Other Direct Cost.  """  
      self.AssemblyMatch:str = obj["AssemblyMatch"]
      """  AssemblyMatch  """  
      self.JdfStatus:str = obj["JdfStatus"]
      """  JdfStatus  """  
      self.PressDevice:str = obj["PressDevice"]
      """  PressDevice  """  
      self.DigitalFileName:str = obj["DigitalFileName"]
      """  DigitalFileName  """  
      self.PrepressJobName:str = obj["PrepressJobName"]
      """  PrepressJobName  """  
      self.JdfPrepressAction:str = obj["JdfPrepressAction"]
      """  JdfPrepressAction  """  
      self.SendToPress:bool = obj["SendToPress"]
      """  SendToPress  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.SendToPressInitiator:int = obj["SendToPressInitiator"]
      """  SendToPressInitiator  """  
      self.OperationType:int = obj["OperationType"]
      """  OperationType  """  
      self.SendToPrePress:bool = obj["SendToPrePress"]
      """  SendToPrePress  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartPlanInfo:str = obj["PartPlanInfo"]
      """  PartPlanInfo  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      """  Calculated Available Quantity  """  
      self.bUseAvailQty:bool = obj["bUseAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.ChildAssemblySeq:int = obj["ChildAssemblySeq"]
      """  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  """  
      self.DispIUM:str = obj["DispIUM"]
      """  The internal unit of measure for this assembly.  Same as IUM but readOnly  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  The order JobAsmbl records should be displayed.  """  
      self.EnableAsmSplitCosts:bool = obj["EnableAsmSplitCosts"]
      """  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  """  
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  """  
      self.GetCostsFromInventory:bool = obj["GetCostsFromInventory"]
      """  External field for EQSyst GetCostsFromInventory  """  
      self.GetCostsFromTemplate:bool = obj["GetCostsFromTemplate"]
      """  External field to hold JCSyst.GetCostsFromTemplate value  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  Parent Description  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Parent PartNum  """  
      self.ParentRev:str = obj["ParentRev"]
      """  Parent RevisionNum  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if current Part is an Inventory Part.  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      """  Related Operation Description  """  
      self.ShowWarningBOMResequence:bool = obj["ShowWarningBOMResequence"]
      """  For Internal use ONLY to set a flag calculated from BO to show a warning message to the user when there exists some inconsistences between records on JobAsml table that can cause infinite loop when BOM Resequence.  """  
      self.AddAsmAs:str = obj["AddAsmAs"]
      """  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  """  
      self.bAvailQty:int = obj["bAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.AttrClassID:str = obj["AttrClassID"]
      self.TLATotalCost:int = obj["TLATotalCost"]
      """  This Level Total Actual Cost (TLAMaterialCost + TLALaborCost + TLABurdenCost + TLASubcontractCost + TLAMtlBurCost)  """  
      self.TLETotalCost:int = obj["TLETotalCost"]
      """  The Level Estimated Total Cost (TLEMaterialCost + TLELaborCost + TLEBurdenCost + TLESubcontractCost + TLEMtlBurCost)  """  
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
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   jobNum
   assemblySeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_JobAsmSearchTableset:
   def __init__(self, obj):
      self.JobAsmbl:list[Erp_Tablesets_JobAsmblRow] = obj["JobAsmbl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobAsmblListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production quantity required for this assembly per one of it's parent part.  """  
      self.IUM:str = obj["IUM"]
      """  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  """  
      self.PullQty:int = obj["PullQty"]
      """  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  This is the warehouse that the material is allocated against.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Assembly.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  """  
      self.OverRunQty:int = obj["OverRunQty"]
      """  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.DueDate:str = obj["DueDate"]
      """  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  """  
      self.Child:int = obj["Child"]
      """  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date, of this component that was issued from stock.  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total material burden cost to date, of this component that was issued from stock.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.TLALaborCost:int = obj["TLALaborCost"]
      """  This Level Actual Labor Cost.  """  
      self.TLABurdenCost:int = obj["TLABurdenCost"]
      """  This Level Actual Burden Cost.  """  
      self.TLAMaterialCost:int = obj["TLAMaterialCost"]
      """  This Level Actual Material Cost.  """  
      self.TLASubcontractCost:int = obj["TLASubcontractCost"]
      """  This Level Actual Subcontract Cost.  """  
      self.TLAMtlBurCost:int = obj["TLAMtlBurCost"]
      """  This Level Actual Material Burden Cost.  """  
      self.TLASetupHours:int = obj["TLASetupHours"]
      """  This Level Actual Setup Hours.  """  
      self.TLAProdHours:int = obj["TLAProdHours"]
      """  This Level Actual Production Hours.  """  
      self.TLELaborCost:int = obj["TLELaborCost"]
      """  This Level Estimated Labor Cost.  """  
      self.TLEBurdenCost:int = obj["TLEBurdenCost"]
      """  This Level Estimated Burden Cost.  """  
      self.TLEMaterialCost:int = obj["TLEMaterialCost"]
      """  This Level Estimated Material Cost.  """  
      self.TLESubcontractCost:int = obj["TLESubcontractCost"]
      """  This Level Estimated Subcontract Cost.  """  
      self.TLEMtlBurCost:int = obj["TLEMtlBurCost"]
      """  This Level Estimated Material Burden Cost.  """  
      self.TLESetupHours:int = obj["TLESetupHours"]
      """  This Level Estimated Setup Hours.  """  
      self.TLEProdHours:int = obj["TLEProdHours"]
      """  This Level Estimated Production Hours.  """  
      self.LLALaborCost:int = obj["LLALaborCost"]
      """  Lower Level Actual Labor Cost.  """  
      self.LLABurdenCost:int = obj["LLABurdenCost"]
      """  Lower Level Burden Labor Cost.  """  
      self.LLAMaterialCost:int = obj["LLAMaterialCost"]
      """  Lower Level Actual Material Cost.  """  
      self.LLASubcontractCost:int = obj["LLASubcontractCost"]
      """  Lower Level Actual Subcontractor Cost.  """  
      self.LLAMtlBurCost:int = obj["LLAMtlBurCost"]
      """  Lower Level Actual Material Burden Cost.  """  
      self.LLASetupHours:int = obj["LLASetupHours"]
      """  Lower Level Actual Setup Hours.  """  
      self.LLAProdHours:int = obj["LLAProdHours"]
      """  Lower Level Actual Production Hours.  """  
      self.LLELaborCost:int = obj["LLELaborCost"]
      """  Lower Level Estimated Labor Cost.  """  
      self.LLEBurdenCost:int = obj["LLEBurdenCost"]
      """  Lower Level Estimated Burden Cost.  """  
      self.LLEMaterialCost:int = obj["LLEMaterialCost"]
      """  Lower Level Estimated Material Cost.  """  
      self.LLESubcontractCost:int = obj["LLESubcontractCost"]
      """  Lower Level Estimated Subcontract Cost.  """  
      self.LLEMtlBurCost:int = obj["LLEMtlBurCost"]
      """  Lower Level Estimated Material Burden Cost.  """  
      self.LLESetupHours:int = obj["LLESetupHours"]
      """  Lower Level Estimated Setup Hours.  """  
      self.LLEProdHours:int = obj["LLEProdHours"]
      """  Lower Level Estimated Production Hours.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.ReceivedToStock:int = obj["ReceivedToStock"]
      """  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.TLAMaterialLabCost:int = obj["TLAMaterialLabCost"]
      """  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialMtlCost:int = obj["TLAMaterialMtlCost"]
      """  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialSubCost:int = obj["TLAMaterialSubCost"]
      """  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialBurCost:int = obj["TLAMaterialBurCost"]
      """  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.LLAMaterialLabCost:int = obj["LLAMaterialLabCost"]
      """  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialMtlCost:int = obj["LLAMaterialMtlCost"]
      """  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialSubCost:int = obj["LLAMaterialSubCost"]
      """  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialBurCost:int = obj["LLAMaterialBurCost"]
      """  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.TotalMtlMtlCost:int = obj["TotalMtlMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.TotalMtlLabCost:int = obj["TotalMtlLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlSubCost:int = obj["TotalMtlSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlBurCost:int = obj["TotalMtlBurCost"]
      """  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this assembly belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this assembly relates to.  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.OrigRequiredQty:int = obj["OrigRequiredQty"]
      """  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.TLAMaterialMtlBurCost:int = obj["TLAMaterialMtlBurCost"]
      """  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  """  
      self.LLAMaterialMtlBurCost:int = obj["LLAMaterialMtlBurCost"]
      """  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  """  
      self.TLAMfgCompLabCost:int = obj["TLAMfgCompLabCost"]
      """  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlCost:int = obj["TLAMfgCompMtlCost"]
      """  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompSubCost:int = obj["TLAMfgCompSubCost"]
      """  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompBurCost:int = obj["TLAMfgCompBurCost"]
      """  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlBurCost:int = obj["TLAMfgCompMtlBurCost"]
      """  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.LLAMfgCompLabCost:int = obj["LLAMfgCompLabCost"]
      """  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlCost:int = obj["LLAMfgCompMtlCost"]
      """  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompSubCost:int = obj["LLAMfgCompSubCost"]
      """  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompBurCost:int = obj["LLAMfgCompBurCost"]
      """  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlBurCost:int = obj["LLAMfgCompMtlBurCost"]
      """  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.Weight:int = obj["Weight"]
      """  Assembly Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Assembly Weight UOM defaulted from Part Master.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  Original Material Sequence. Used in the configurator.  """  
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      """  Original Rule Tag. Used in the Configurator.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.PlanAsAsm:bool = obj["PlanAsAsm"]
      """  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  """  
      self.PAARef:str = obj["PAARef"]
      """  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  """  
      self.PAAFirm:bool = obj["PAAFirm"]
      """  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      """  Related Operation Description  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Parent PartNum  """  
      self.ParentRev:str = obj["ParentRev"]
      """  Parent RevisionNum  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  Parent Description  """  
      self.AvailableQty:int = obj["AvailableQty"]
      """  Calculated Available Quantity  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  """  
      self.ChildAssemblySeq:int = obj["ChildAssemblySeq"]
      """  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  """  
      self.AddAsmAs:str = obj["AddAsmAs"]
      """  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  The order JobAsmbl records should be displayed.  """  
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.DispIUM:str = obj["DispIUM"]
      """  The internal unit of measure for this assembly.  Same as IUM but readOnly  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      self.bAvailQty:int = obj["bAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.bUseAvailQty:bool = obj["bUseAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.EnableAsmSplitCosts:bool = obj["EnableAsmSplitCosts"]
      """  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  """  
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      """  Description  """  
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobAsmblListTableset:
   def __init__(self, obj):
      self.JobAsmblList:list[Erp_Tablesets_JobAsmblListRow] = obj["JobAsmblList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production quantity required for this assembly per one of it's parent part.  """  
      self.IUM:str = obj["IUM"]
      """  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  """  
      self.PullQty:int = obj["PullQty"]
      """  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  This is the warehouse that the material is allocated against.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Assembly.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  """  
      self.OverRunQty:int = obj["OverRunQty"]
      """  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.DueDate:str = obj["DueDate"]
      """  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  """  
      self.Child:int = obj["Child"]
      """  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date, of this component that was issued from stock.  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total material burden cost to date, of this component that was issued from stock.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.TLALaborCost:int = obj["TLALaborCost"]
      """  This Level Actual Labor Cost.  """  
      self.TLABurdenCost:int = obj["TLABurdenCost"]
      """  This Level Actual Burden Cost.  """  
      self.TLAMaterialCost:int = obj["TLAMaterialCost"]
      """  This Level Actual Material Cost.  """  
      self.TLASubcontractCost:int = obj["TLASubcontractCost"]
      """  This Level Actual Subcontract Cost.  """  
      self.TLAMtlBurCost:int = obj["TLAMtlBurCost"]
      """  This Level Actual Material Burden Cost.  """  
      self.TLASetupHours:int = obj["TLASetupHours"]
      """  This Level Actual Setup Hours.  """  
      self.TLAProdHours:int = obj["TLAProdHours"]
      """  This Level Actual Production Hours.  """  
      self.TLELaborCost:int = obj["TLELaborCost"]
      """  This Level Estimated Labor Cost.  """  
      self.TLEBurdenCost:int = obj["TLEBurdenCost"]
      """  This Level Estimated Burden Cost.  """  
      self.TLEMaterialCost:int = obj["TLEMaterialCost"]
      """  This Level Estimated Material Cost.  """  
      self.TLESubcontractCost:int = obj["TLESubcontractCost"]
      """  This Level Estimated Subcontract Cost.  """  
      self.TLEMtlBurCost:int = obj["TLEMtlBurCost"]
      """  This Level Estimated Material Burden Cost.  """  
      self.TLESetupHours:int = obj["TLESetupHours"]
      """  This Level Estimated Setup Hours.  """  
      self.TLEProdHours:int = obj["TLEProdHours"]
      """  This Level Estimated Production Hours.  """  
      self.LLALaborCost:int = obj["LLALaborCost"]
      """  Lower Level Actual Labor Cost.  """  
      self.LLABurdenCost:int = obj["LLABurdenCost"]
      """  Lower Level Burden Labor Cost.  """  
      self.LLAMaterialCost:int = obj["LLAMaterialCost"]
      """  Lower Level Actual Material Cost.  """  
      self.LLASubcontractCost:int = obj["LLASubcontractCost"]
      """  Lower Level Actual Subcontractor Cost.  """  
      self.LLAMtlBurCost:int = obj["LLAMtlBurCost"]
      """  Lower Level Actual Material Burden Cost.  """  
      self.LLASetupHours:int = obj["LLASetupHours"]
      """  Lower Level Actual Setup Hours.  """  
      self.LLAProdHours:int = obj["LLAProdHours"]
      """  Lower Level Actual Production Hours.  """  
      self.LLELaborCost:int = obj["LLELaborCost"]
      """  Lower Level Estimated Labor Cost.  """  
      self.LLEBurdenCost:int = obj["LLEBurdenCost"]
      """  Lower Level Estimated Burden Cost.  """  
      self.LLEMaterialCost:int = obj["LLEMaterialCost"]
      """  Lower Level Estimated Material Cost.  """  
      self.LLESubcontractCost:int = obj["LLESubcontractCost"]
      """  Lower Level Estimated Subcontract Cost.  """  
      self.LLEMtlBurCost:int = obj["LLEMtlBurCost"]
      """  Lower Level Estimated Material Burden Cost.  """  
      self.LLESetupHours:int = obj["LLESetupHours"]
      """  Lower Level Estimated Setup Hours.  """  
      self.LLEProdHours:int = obj["LLEProdHours"]
      """  Lower Level Estimated Production Hours.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.ReceivedToStock:int = obj["ReceivedToStock"]
      """  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.TLAMaterialLabCost:int = obj["TLAMaterialLabCost"]
      """  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialMtlCost:int = obj["TLAMaterialMtlCost"]
      """  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialSubCost:int = obj["TLAMaterialSubCost"]
      """  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialBurCost:int = obj["TLAMaterialBurCost"]
      """  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.LLAMaterialLabCost:int = obj["LLAMaterialLabCost"]
      """  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialMtlCost:int = obj["LLAMaterialMtlCost"]
      """  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialSubCost:int = obj["LLAMaterialSubCost"]
      """  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialBurCost:int = obj["LLAMaterialBurCost"]
      """  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.TotalMtlMtlCost:int = obj["TotalMtlMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.TotalMtlLabCost:int = obj["TotalMtlLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlSubCost:int = obj["TotalMtlSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlBurCost:int = obj["TotalMtlBurCost"]
      """  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this assembly belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this assembly relates to.  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.OrigRequiredQty:int = obj["OrigRequiredQty"]
      """  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.TLAMaterialMtlBurCost:int = obj["TLAMaterialMtlBurCost"]
      """  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  """  
      self.LLAMaterialMtlBurCost:int = obj["LLAMaterialMtlBurCost"]
      """  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  """  
      self.TLAMfgCompLabCost:int = obj["TLAMfgCompLabCost"]
      """  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlCost:int = obj["TLAMfgCompMtlCost"]
      """  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompSubCost:int = obj["TLAMfgCompSubCost"]
      """  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompBurCost:int = obj["TLAMfgCompBurCost"]
      """  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlBurCost:int = obj["TLAMfgCompMtlBurCost"]
      """  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.LLAMfgCompLabCost:int = obj["LLAMfgCompLabCost"]
      """  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlCost:int = obj["LLAMfgCompMtlCost"]
      """  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompSubCost:int = obj["LLAMfgCompSubCost"]
      """  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompBurCost:int = obj["LLAMfgCompBurCost"]
      """  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlBurCost:int = obj["LLAMfgCompMtlBurCost"]
      """  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.Weight:int = obj["Weight"]
      """  Assembly Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Assembly Weight UOM defaulted from Part Master.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  Original Material Sequence. Used in the configurator.  """  
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      """  Original Rule Tag. Used in the Configurator.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.PlanAsAsm:bool = obj["PlanAsAsm"]
      """  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  """  
      self.PAARef:str = obj["PAARef"]
      """  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  """  
      self.PAAFirm:bool = obj["PAAFirm"]
      """  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  Reassign Serial Numbers Assembly  """  
      self.TLAODCCost:int = obj["TLAODCCost"]
      """  This Level Actual Other Direct Cost.  """  
      self.AssemblyMatch:str = obj["AssemblyMatch"]
      """  AssemblyMatch  """  
      self.JdfStatus:str = obj["JdfStatus"]
      """  JdfStatus  """  
      self.PressDevice:str = obj["PressDevice"]
      """  PressDevice  """  
      self.DigitalFileName:str = obj["DigitalFileName"]
      """  DigitalFileName  """  
      self.PrepressJobName:str = obj["PrepressJobName"]
      """  PrepressJobName  """  
      self.JdfPrepressAction:str = obj["JdfPrepressAction"]
      """  JdfPrepressAction  """  
      self.SendToPress:bool = obj["SendToPress"]
      """  SendToPress  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.SendToPressInitiator:int = obj["SendToPressInitiator"]
      """  SendToPressInitiator  """  
      self.OperationType:int = obj["OperationType"]
      """  OperationType  """  
      self.SendToPrePress:bool = obj["SendToPrePress"]
      """  SendToPrePress  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartPlanInfo:str = obj["PartPlanInfo"]
      """  PartPlanInfo  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      """  Calculated Available Quantity  """  
      self.bUseAvailQty:bool = obj["bUseAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.ChildAssemblySeq:int = obj["ChildAssemblySeq"]
      """  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  """  
      self.DispIUM:str = obj["DispIUM"]
      """  The internal unit of measure for this assembly.  Same as IUM but readOnly  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  The order JobAsmbl records should be displayed.  """  
      self.EnableAsmSplitCosts:bool = obj["EnableAsmSplitCosts"]
      """  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  """  
      self.EnableMtlSalvage:bool = obj["EnableMtlSalvage"]
      self.EnablePurDir:bool = obj["EnablePurDir"]
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  """  
      self.GetCostsFromInventory:bool = obj["GetCostsFromInventory"]
      """  External field for EQSyst GetCostsFromInventory  """  
      self.GetCostsFromTemplate:bool = obj["GetCostsFromTemplate"]
      """  External field to hold JCSyst.GetCostsFromTemplate value  """  
      self.ParentAssemblySeq:int = obj["ParentAssemblySeq"]
      """  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  Parent Description  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Parent PartNum  """  
      self.ParentRev:str = obj["ParentRev"]
      """  Parent RevisionNum  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if current Part is an Inventory Part.  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  """  
      self.RelatedOperationDesc:str = obj["RelatedOperationDesc"]
      """  Related Operation Description  """  
      self.ShowWarningBOMResequence:bool = obj["ShowWarningBOMResequence"]
      """  For Internal use ONLY to set a flag calculated from BO to show a warning message to the user when there exists some inconsistences between records on JobAsml table that can cause infinite loop when BOM Resequence.  """  
      self.AddAsmAs:str = obj["AddAsmAs"]
      """  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  """  
      self.bAvailQty:int = obj["bAvailQty"]
      """  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.AttrClassID:str = obj["AttrClassID"]
      self.TLATotalCost:int = obj["TLATotalCost"]
      """  This Level Total Actual Cost (TLAMaterialCost + TLALaborCost + TLABurdenCost + TLASubcontractCost + TLAMtlBurCost)  """  
      self.TLETotalCost:int = obj["TLETotalCost"]
      """  The Level Estimated Total Cost (TLEMaterialCost + TLELaborCost + TLEBurdenCost + TLESubcontractCost + TLEMtlBurCost)  """  
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
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtJobAsmSearchTableset:
   def __init__(self, obj):
      self.JobAsmbl:list[Erp_Tablesets_JobAsmblRow] = obj["JobAsmbl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   jobNum
   assemblySeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobAsmSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobAsmSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobAsmSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JobAsmblListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewJobAsmbl_input:
   """ Required : 
   ds
   jobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAsmSearchTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      pass

class GetNewJobAsmbl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAsmSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseJobAsmbl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobAsmbl:str = obj["whereClauseJobAsmbl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobAsmSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtJobAsmSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJobAsmSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JobAsmSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JobAsmSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

