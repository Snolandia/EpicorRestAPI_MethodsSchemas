import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PlanningWBSvc
# Description: Service for Planning Work Bench.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PlanningWBs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlanningWBs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlanningWBs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSugRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/PlanningWBs",headers=creds) as resp:
           return await resp.json()

async def post_PlanningWBs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlanningWBs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartSugRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartSugRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/PlanningWBs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlanningWBs_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlanningWB item
   Description: Calls GetByID to retrieve the PlanningWB item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlanningWB
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSugRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/PlanningWBs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlanningWBs_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlanningWB for the service
   Description: Calls UpdateExt to update PlanningWB. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlanningWB
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartSugRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/PlanningWBs(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlanningWBs_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlanningWB item
   Description: Call UpdateExt to delete PlanningWB item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlanningWB
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/PlanningWBs(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSugListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartSug, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartSug=" + whereClausePartSug
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(sysRowID, epicorHeaders = None):
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
   params += "sysRowID=" + sysRowID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CreateJobFromPWB(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateJobFromPWB
   Description: This method will create jobs from pwb
   OperationID: CreateJobFromPWB
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateJobFromPWB_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateJobFromPWB_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartSug(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartSug
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartSug
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartSug_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartSug_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlanningWBSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSugListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartSugListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSugRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartSugRow] = obj["value"]
      pass

class Erp_Tablesets_PartSugListRow:
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
      self.Planner:str = obj["Planner"]
      self.SugSource:str = obj["SugSource"]
      self.ErrorMsg:str = obj["ErrorMsg"]
      """  An error message description.  Used initially when creating a job.  """  
      self.CustFullName:str = obj["CustFullName"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.UOM:str = obj["UOM"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
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
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
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




#########################################################################
# Custom Schemas:
#########################################################################
class CreateJobFromPWB_input:
   """ Required : 
   ds
   ipNewJobNum
   ipMessageResponseFlag
   ipGetDetails
   ipScheduleAll
   ipReleaseAll
   ipTravelerReadyToPrint
   ipBackground
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanningWBTableset] = obj["ds"]
      self.ipNewJobNum:str = obj["ipNewJobNum"]
      """  New Job Number  """  
      self.ipMessageResponseFlag:bool = obj["ipMessageResponseFlag"]
      """  Did user respond to any messages regarding the parts to process?  """  
      self.ipGetDetails:bool = obj["ipGetDetails"]
      """  Get Details flag  """  
      self.ipScheduleAll:bool = obj["ipScheduleAll"]
      """  Schedule All flag  """  
      self.ipReleaseAll:bool = obj["ipReleaseAll"]
      """  Release All flag  """  
      self.ipTravelerReadyToPrint:bool = obj["ipTravelerReadyToPrint"]
      """  TravelerReadyToPrint/MassPrint flag  """  
      self.ipBackground:bool = obj["ipBackground"]
      """  Process jobs in the background/more than one job flag  """  
      pass

class CreateJobFromPWB_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanningWBTableset] = obj["ds"]
      self.opCreatedJobNum:str = obj["parameters"]
      self.opErrMsg:str = obj["parameters"]
      self.opPartQuantityMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartSugListRow:
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
      self.Planner:str = obj["Planner"]
      self.SugSource:str = obj["SugSource"]
      self.ErrorMsg:str = obj["ErrorMsg"]
      """  An error message description.  Used initially when creating a job.  """  
      self.CustFullName:str = obj["CustFullName"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.UOM:str = obj["UOM"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
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
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSugListTableset:
   def __init__(self, obj):
      self.PartSugList:list[Erp_Tablesets_PartSugListRow] = obj["PartSugList"]
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

class Erp_Tablesets_PlanningWBTableset:
   def __init__(self, obj):
      self.PartSug:list[Erp_Tablesets_PartSugRow] = obj["PartSug"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPlanningWBTableset:
   def __init__(self, obj):
      self.PartSug:list[Erp_Tablesets_PartSugRow] = obj["PartSug"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlanningWBTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlanningWBTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlanningWBTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartSugListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartSug_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanningWBTableset] = obj["ds"]
      pass

class GetNewPartSug_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanningWBTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartSug
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartSug:str = obj["whereClausePartSug"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlanningWBTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPlanningWBTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPlanningWBTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlanningWBTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlanningWBTableset] = obj["ds"]
      pass

      """  output parameters  """  

