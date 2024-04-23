import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DMRActnSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DMRActnSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DMRActnSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DMRActnSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRActnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/DMRActnSearches",headers=creds) as resp:
           return await resp.json()

async def post_DMRActnSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DMRActnSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DMRActnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/DMRActnSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DMRActnSearches_Company_DMRNum_ActionNum(Company, DMRNum, ActionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DMRActnSearch item
   Description: Calls GetByID to retrieve the DMRActnSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRActnSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param ActionNum: Desc: ActionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/DMRActnSearches(" + Company + "," + DMRNum + "," + ActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DMRActnSearches_Company_DMRNum_ActionNum(Company, DMRNum, ActionNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DMRActnSearch for the service
   Description: Calls UpdateExt to update DMRActnSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DMRActnSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param ActionNum: Desc: ActionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/DMRActnSearches(" + Company + "," + DMRNum + "," + ActionNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DMRActnSearches_Company_DMRNum_ActionNum(Company, DMRNum, ActionNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DMRActnSearch item
   Description: Call UpdateExt to delete DMRActnSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DMRActnSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param ActionNum: Desc: ActionNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/DMRActnSearches(" + Company + "," + DMRNum + "," + ActionNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRActnListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDMRActn, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDMRActn=" + whereClauseDMRActn
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(dmRNum, actionNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "dmRNum=" + dmRNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "actionNum=" + actionNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorDMRSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorDMRSearch
   Description: Purpose: Get the list of a supplier's DMR with the filtered search.
Parameters:  none
Notes:
<param name="whereClause">Stores the filtered search of DMR</param><param name="vendorNum">The current supplier ID</param><param name="pageSize">The number of results to return</param><param name="absolutePage">Display whole page</param><param name="morePages">Display more results</param>
   OperationID: GetVendorDMRSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorDMRSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorDMRSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRActn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRActn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDMRActn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRActn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DMRActnListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DMRActnRow] = obj["value"]
      pass

class Erp_Tablesets_DMRActnListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  DMR Action Date.  """  
      self.ActionType:str = obj["ActionType"]
      """  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  """  
      self.Quantity:int = obj["Quantity"]
      """  DMR Action quantity in base unit of measure.  Must be > ZERO.  """  
      self.DestinationType:str = obj["DestinationType"]
      """  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.DMRSeqNum:int = obj["DMRSeqNum"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.UnitCredit:int = obj["UnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DocUnitCredit:int = obj["DocUnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.CreditUM:str = obj["CreditUM"]
      """  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DebitMemoNum:str = obj["DebitMemoNum"]
      """  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  """  
      self.DebitMemoLine:int = obj["DebitMemoLine"]
      """  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  """  
      self.VendRMANum:str = obj["VendRMANum"]
      """  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  """  
      self.ActionUserID:str = obj["ActionUserID"]
      """  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Required for all actions.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.FldWarehouseCode:str = obj["FldWarehouseCode"]
      """  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  """  
      self.FldBinNum:str = obj["FldBinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Rpt1UnitCredit:int = obj["Rpt1UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCredit:int = obj["Rpt2UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCredit:int = obj["Rpt3UnitCredit"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Resolution:str = obj["Resolution"]
      """   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  """  
      self.ReturnToSupplier:bool = obj["ReturnToSupplier"]
      """  Flag indicating that the part will be returned to the supplier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  This is the supplier's packing slip number for the original receipt of the part.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  IssuedComplete  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AcceptIUM:str = obj["AcceptIUM"]
      """  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  """  
      self.EnableWarehouse:bool = obj["EnableWarehouse"]
      """  Indicates if the Warehouse field should be enabled for input.  """  
      self.EnableBin:bool = obj["EnableBin"]
      """  Indicates if the Bin field should be enabled for input.  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Request to Move  """  
      self.EnableReqMove:bool = obj["EnableReqMove"]
      """  Indicates if the RequestMove field should be enabled for input.  """  
      self.EnableReason:bool = obj["EnableReason"]
      """  Indicates if the Reason field should be enabled for input.  """  
      self.OperationComplete:bool = obj["OperationComplete"]
      """  Job Operation Complete  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RejectType:str = obj["RejectType"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  """  
      self.OpenDMR:bool = obj["OpenDMR"]
      self.ActionTypeDesc:str = obj["ActionTypeDesc"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.DispQuantity:int = obj["DispQuantity"]
      """  External field for handling unit of measure conversions in the UI.  """  
      self.TotRemainQty:int = obj["TotRemainQty"]
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.SerialControlPlant:str = obj["SerialControlPlant"]
      """  The plant id of the plant that is controlling the serial processing for this transaction record  """  
      self.SerialControlPlant2:str = obj["SerialControlPlant2"]
      """  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  """  
      self.SerialControlPlantIsFromPlt:bool = obj["SerialControlPlantIsFromPlt"]
      """  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  """  
      self.TranQty:int = obj["TranQty"]
      """  TranQty  """  
      self.TranUOM:str = obj["TranUOM"]
      """  TranUOM  """  
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRActnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  DMR Action Date.  """  
      self.ActionType:str = obj["ActionType"]
      """  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  """  
      self.Quantity:int = obj["Quantity"]
      """  DMR Action quantity in base unit of measure.  Must be > ZERO.  """  
      self.DestinationType:str = obj["DestinationType"]
      """  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.DMRSeqNum:int = obj["DMRSeqNum"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.UnitCredit:int = obj["UnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DocUnitCredit:int = obj["DocUnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.CreditUM:str = obj["CreditUM"]
      """  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DebitMemoNum:str = obj["DebitMemoNum"]
      """  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  """  
      self.DebitMemoLine:int = obj["DebitMemoLine"]
      """  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  """  
      self.VendRMANum:str = obj["VendRMANum"]
      """  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  """  
      self.ActionUserID:str = obj["ActionUserID"]
      """  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Required for all actions.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.FldWarehouseCode:str = obj["FldWarehouseCode"]
      """  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  """  
      self.FldBinNum:str = obj["FldBinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Rpt1UnitCredit:int = obj["Rpt1UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCredit:int = obj["Rpt2UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCredit:int = obj["Rpt3UnitCredit"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Resolution:str = obj["Resolution"]
      """   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  """  
      self.ReturnToSupplier:bool = obj["ReturnToSupplier"]
      """  Flag indicating that the part will be returned to the supplier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  This is the supplier's packing slip number for the original receipt of the part.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.DisableRejection:bool = obj["DisableRejection"]
      """  Is a boolean and tell us about to disable or not the entire Rejection Screen. DisableRejection checks DisableRejectionChar to enable or disable.  """  
      self.DisableRejectionChar:str = obj["DisableRejectionChar"]
      """  Is a character and has the Company~Debit~ActionNum, has the linkedDebitMemo and helps to check if is needed the DisableRejection.  """  
      self.RefInvoiceNum:str = obj["RefInvoiceNum"]
      """  Displays the link AP Invoice linked to the Resolution Request Debit memo, Request Correction Invoice, Request supplier credit, the Reference invoice is created.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  IssuedComplete  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AcceptIUM:str = obj["AcceptIUM"]
      """  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  """  
      self.ActionTypeDesc:str = obj["ActionTypeDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DispQuantity:int = obj["DispQuantity"]
      """  External field for handling unit of measure conversions in the UI.  """  
      self.EnableBin:bool = obj["EnableBin"]
      """  Indicates if the Bin field should be enabled for input.  """  
      self.EnableReason:bool = obj["EnableReason"]
      """  Indicates if the Reason field should be enabled for input.  """  
      self.EnableReqMove:bool = obj["EnableReqMove"]
      """  Indicates if the RequestMove field should be enabled for input.  """  
      self.EnableWarehouse:bool = obj["EnableWarehouse"]
      """  Indicates if the Warehouse field should be enabled for input.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.OpenDMR:bool = obj["OpenDMR"]
      self.OperationComplete:bool = obj["OperationComplete"]
      """  Job Operation Complete  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.POCurrencyCode:str = obj["POCurrencyCode"]
      """  PO Currency Code.  """  
      self.POLine:int = obj["POLine"]
      self.PONum:int = obj["PONum"]
      self.POUnitCost:int = obj["POUnitCost"]
      """  DMR item's unit cost in the POs currency.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RejectType:str = obj["RejectType"]
      self.RequestMove:bool = obj["RequestMove"]
      """  Request to Move  """  
      self.Rpt1POUnitCost:int = obj["Rpt1POUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2POUnitCost:int = obj["Rpt2POUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3POUnitCost:int = obj["Rpt3POUnitCost"]
      """  Reporting currency value of this field  """  
      self.SerialControlPlant:str = obj["SerialControlPlant"]
      """  The plant id of the plant that is controlling the serial processing for this transaction record  """  
      self.SerialControlPlant2:str = obj["SerialControlPlant2"]
      """  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  """  
      self.SerialControlPlantIsFromPlt:bool = obj["SerialControlPlantIsFromPlt"]
      """  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  """  
      self.TotRemainQty:int = obj["TotRemainQty"]
      self.TranQty:int = obj["TranQty"]
      """  TranQty  """  
      self.TranUOM:str = obj["TranUOM"]
      """  TranUOM  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Displays the customer name for the Ship To contact related to the RMA.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  Displays the customer Ship To name related to the RMA.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  Customer that is returning parts on related RMA.  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA Number that the Return detail is related to.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA line that the Return detail is related to.  """  
      self.ShipToID:str = obj["ShipToID"]
      """  Specifies the ID of the Ship To contact related to the RMA.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   dmRNum
   actionNum
   """  
   def __init__(self, obj):
      self.dmRNum:int = obj["dmRNum"]
      self.actionNum:int = obj["actionNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DMRActnListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  DMR Action Date.  """  
      self.ActionType:str = obj["ActionType"]
      """  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  """  
      self.Quantity:int = obj["Quantity"]
      """  DMR Action quantity in base unit of measure.  Must be > ZERO.  """  
      self.DestinationType:str = obj["DestinationType"]
      """  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.DMRSeqNum:int = obj["DMRSeqNum"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.UnitCredit:int = obj["UnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DocUnitCredit:int = obj["DocUnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.CreditUM:str = obj["CreditUM"]
      """  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DebitMemoNum:str = obj["DebitMemoNum"]
      """  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  """  
      self.DebitMemoLine:int = obj["DebitMemoLine"]
      """  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  """  
      self.VendRMANum:str = obj["VendRMANum"]
      """  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  """  
      self.ActionUserID:str = obj["ActionUserID"]
      """  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Required for all actions.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.FldWarehouseCode:str = obj["FldWarehouseCode"]
      """  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  """  
      self.FldBinNum:str = obj["FldBinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Rpt1UnitCredit:int = obj["Rpt1UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCredit:int = obj["Rpt2UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCredit:int = obj["Rpt3UnitCredit"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Resolution:str = obj["Resolution"]
      """   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  """  
      self.ReturnToSupplier:bool = obj["ReturnToSupplier"]
      """  Flag indicating that the part will be returned to the supplier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  This is the supplier's packing slip number for the original receipt of the part.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  IssuedComplete  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AcceptIUM:str = obj["AcceptIUM"]
      """  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  """  
      self.EnableWarehouse:bool = obj["EnableWarehouse"]
      """  Indicates if the Warehouse field should be enabled for input.  """  
      self.EnableBin:bool = obj["EnableBin"]
      """  Indicates if the Bin field should be enabled for input.  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Request to Move  """  
      self.EnableReqMove:bool = obj["EnableReqMove"]
      """  Indicates if the RequestMove field should be enabled for input.  """  
      self.EnableReason:bool = obj["EnableReason"]
      """  Indicates if the Reason field should be enabled for input.  """  
      self.OperationComplete:bool = obj["OperationComplete"]
      """  Job Operation Complete  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RejectType:str = obj["RejectType"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  """  
      self.OpenDMR:bool = obj["OpenDMR"]
      self.ActionTypeDesc:str = obj["ActionTypeDesc"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.DispQuantity:int = obj["DispQuantity"]
      """  External field for handling unit of measure conversions in the UI.  """  
      self.TotRemainQty:int = obj["TotRemainQty"]
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.SerialControlPlant:str = obj["SerialControlPlant"]
      """  The plant id of the plant that is controlling the serial processing for this transaction record  """  
      self.SerialControlPlant2:str = obj["SerialControlPlant2"]
      """  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  """  
      self.SerialControlPlantIsFromPlt:bool = obj["SerialControlPlantIsFromPlt"]
      """  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  """  
      self.TranQty:int = obj["TranQty"]
      """  TranQty  """  
      self.TranUOM:str = obj["TranUOM"]
      """  TranUOM  """  
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRActnListTableset:
   def __init__(self, obj):
      self.DMRActnList:list[Erp_Tablesets_DMRActnListRow] = obj["DMRActnList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DMRActnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  DMR Action Date.  """  
      self.ActionType:str = obj["ActionType"]
      """  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  """  
      self.Quantity:int = obj["Quantity"]
      """  DMR Action quantity in base unit of measure.  Must be > ZERO.  """  
      self.DestinationType:str = obj["DestinationType"]
      """  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.DMRSeqNum:int = obj["DMRSeqNum"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.UnitCredit:int = obj["UnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DocUnitCredit:int = obj["DocUnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.CreditUM:str = obj["CreditUM"]
      """  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DebitMemoNum:str = obj["DebitMemoNum"]
      """  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  """  
      self.DebitMemoLine:int = obj["DebitMemoLine"]
      """  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  """  
      self.VendRMANum:str = obj["VendRMANum"]
      """  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  """  
      self.ActionUserID:str = obj["ActionUserID"]
      """  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Required for all actions.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.FldWarehouseCode:str = obj["FldWarehouseCode"]
      """  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  """  
      self.FldBinNum:str = obj["FldBinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Rpt1UnitCredit:int = obj["Rpt1UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCredit:int = obj["Rpt2UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCredit:int = obj["Rpt3UnitCredit"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Resolution:str = obj["Resolution"]
      """   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  """  
      self.ReturnToSupplier:bool = obj["ReturnToSupplier"]
      """  Flag indicating that the part will be returned to the supplier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  This is the supplier's packing slip number for the original receipt of the part.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.DisableRejection:bool = obj["DisableRejection"]
      """  Is a boolean and tell us about to disable or not the entire Rejection Screen. DisableRejection checks DisableRejectionChar to enable or disable.  """  
      self.DisableRejectionChar:str = obj["DisableRejectionChar"]
      """  Is a character and has the Company~Debit~ActionNum, has the linkedDebitMemo and helps to check if is needed the DisableRejection.  """  
      self.RefInvoiceNum:str = obj["RefInvoiceNum"]
      """  Displays the link AP Invoice linked to the Resolution Request Debit memo, Request Correction Invoice, Request supplier credit, the Reference invoice is created.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  IssuedComplete  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AcceptIUM:str = obj["AcceptIUM"]
      """  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  """  
      self.ActionTypeDesc:str = obj["ActionTypeDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DispQuantity:int = obj["DispQuantity"]
      """  External field for handling unit of measure conversions in the UI.  """  
      self.EnableBin:bool = obj["EnableBin"]
      """  Indicates if the Bin field should be enabled for input.  """  
      self.EnableReason:bool = obj["EnableReason"]
      """  Indicates if the Reason field should be enabled for input.  """  
      self.EnableReqMove:bool = obj["EnableReqMove"]
      """  Indicates if the RequestMove field should be enabled for input.  """  
      self.EnableWarehouse:bool = obj["EnableWarehouse"]
      """  Indicates if the Warehouse field should be enabled for input.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.OpenDMR:bool = obj["OpenDMR"]
      self.OperationComplete:bool = obj["OperationComplete"]
      """  Job Operation Complete  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.POCurrencyCode:str = obj["POCurrencyCode"]
      """  PO Currency Code.  """  
      self.POLine:int = obj["POLine"]
      self.PONum:int = obj["PONum"]
      self.POUnitCost:int = obj["POUnitCost"]
      """  DMR item's unit cost in the POs currency.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RejectType:str = obj["RejectType"]
      self.RequestMove:bool = obj["RequestMove"]
      """  Request to Move  """  
      self.Rpt1POUnitCost:int = obj["Rpt1POUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2POUnitCost:int = obj["Rpt2POUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3POUnitCost:int = obj["Rpt3POUnitCost"]
      """  Reporting currency value of this field  """  
      self.SerialControlPlant:str = obj["SerialControlPlant"]
      """  The plant id of the plant that is controlling the serial processing for this transaction record  """  
      self.SerialControlPlant2:str = obj["SerialControlPlant2"]
      """  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  """  
      self.SerialControlPlantIsFromPlt:bool = obj["SerialControlPlantIsFromPlt"]
      """  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  """  
      self.TotRemainQty:int = obj["TotRemainQty"]
      self.TranQty:int = obj["TranQty"]
      """  TranQty  """  
      self.TranUOM:str = obj["TranUOM"]
      """  TranUOM  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Displays the customer name for the Ship To contact related to the RMA.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  Displays the customer Ship To name related to the RMA.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  Customer that is returning parts on related RMA.  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA Number that the Return detail is related to.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA line that the Return detail is related to.  """  
      self.ShipToID:str = obj["ShipToID"]
      """  Specifies the ID of the Ship To contact related to the RMA.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRActnSearchTableset:
   def __init__(self, obj):
      self.DMRActn:list[Erp_Tablesets_DMRActnRow] = obj["DMRActn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtDMRActnSearchTableset:
   def __init__(self, obj):
      self.DMRActn:list[Erp_Tablesets_DMRActnRow] = obj["DMRActn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   dmRNum
   actionNum
   """  
   def __init__(self, obj):
      self.dmRNum:int = obj["dmRNum"]
      self.actionNum:int = obj["actionNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DMRActnSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DMRActnSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DMRActnSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DMRActnListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDMRActn_input:
   """ Required : 
   ds
   dmRNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRActnSearchTableset] = obj["ds"]
      self.dmRNum:int = obj["dmRNum"]
      pass

class GetNewDMRActn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRActnSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDMRActn
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDMRActn:str = obj["whereClauseDMRActn"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DMRActnSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetVendorDMRSearch_input:
   """ Required : 
   whereClause
   vendorNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.vendorNum:int = obj["vendorNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetVendorDMRSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DMRActnListTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtDMRActnSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDMRActnSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRActnSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRActnSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

