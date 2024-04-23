import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APInvDtlSearchSvc
# Description: bo/APInvDtlSearch/APInvDtlSearch.p
           APInvDtl Search Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APInvDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APInvDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APInvDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/APInvDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_APInvDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APInvDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APInvDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APInvDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/APInvDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APInvDtlSearches_Company_VendorNum_InvoiceNum_InvoiceLine(Company, VendorNum, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APInvDtlSearch item
   Description: Calls GetByID to retrieve the APInvDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/APInvDtlSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APInvDtlSearches_Company_VendorNum_InvoiceNum_InvoiceLine(Company, VendorNum, InvoiceNum, InvoiceLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APInvDtlSearch for the service
   Description: Calls UpdateExt to update APInvDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APInvDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APInvDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/APInvDtlSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APInvDtlSearches_Company_VendorNum_InvoiceNum_InvoiceLine(Company, VendorNum, InvoiceNum, InvoiceLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APInvDtlSearch item
   Description: Call UpdateExt to delete APInvDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APInvDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/APInvDtlSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPInvDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAPInvDtl=" + whereClauseAPInvDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, invoiceNum, invoiceLine, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceNum=" + invoiceNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceLine=" + invoiceLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPInvDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPInvDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPInvDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPInvDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPInvDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvDtlRow] = obj["value"]
      pass

class Erp_Tablesets_APInvDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Indicates the type of invoice line. "R" = Invoiced for Receipt of goods, "A" - Advance Billing,  "M" - Misc. Billing, "U" - Unreceived goods, "J" - Job Miscellaneous charge A/P invoice, "S" - Asset Invoice Line.  Not directly entered,  set by invoice entry by the user selecting the appropriate menu option.  """  
      self.UnitCost:int = obj["UnitCost"]
      """  item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost if related.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  """  
      self.PONum:int = obj["PONum"]
      """   Purchase Order Number that this invoice line item is related to. If packing slip is referenced then it is set = to RcvDtl.PONum and can't be changed.  If entered it must be a valid POHeader record.
A reference is made to the purchase order using PONUM, POLine and PORelNum fields. If any one of these fields are entered then they all must be entered and be valid.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # that invoice is for. Defaulted from the RvcDtl if referenced to packing slip document.. Only applicable when PO is referenced.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being invoiced. Defaulted from RcvDtl if related to a packing slip. If entered it Must be valid.  """  
      self.Description:str = obj["Description"]
      """  Invoice line description.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job that this invoice is related to. Set to the RcvDtl.JobNum.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence that this invoice line is related to. Set to RcvDtl.AssemblySeq.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """  Indicates if this invoice line is related to a job material (jobmtl) or job subcontract (JobOper) record. Valid values are "M" = material or "S" = subcontract. This is set to RvcDtl.JobSeqType.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this line item is costed against. Defaults from the RcvDtl.JobSeq. Only applicable for a receipts to job.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendor's purchase point ID. This is used as part of the foreign key to reference the RcvHead/RcvDtl records.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendor's packing slip that this A\P invoice detail line is associated with. This Along with PackLine provides a relationship to the receipt document detail (RcvDtl)  """  
      self.PackLine:int = obj["PackLine"]
      """  The Pack Slip line of the RcvDtl record  to which this A\P detail record is related to.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Total Invoiced Quantity for the line item.  This is stored in the Vendors Unit of Measure.  Can be defaulted from the packing slip detail if referenced (RcvDtl.POReceiptQty)  """  
      self.PUM:str = obj["PUM"]
      """  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDel.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  """  
      self.OurQty:int = obj["OurQty"]
      """  Invoiced Quantity for the line item in our unit of measure. This can be defaulted from the packing slip detail if referenced (RcvDtl.ReceiptQty)  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure code for invoiced quantity in our unit of measure. Defaulted in the following hierarchy: from the RcvDel.IUM if packing slip is referenced, from PODetail.IUM if PO is referenced, from Part.IUM if valid part or finally from XaSyst.DefaultUM.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the APInvDtl.VendorQty by the appropriate "per" value and then multiply by unit cost.  Use the PODetail.CostPerCode if related to a PO else use Part.PricePerCode if valid part. Else default as "E".
Valid database values are "E" = Each, "C" = per 100 or "M" = per 1,000.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's part number. Optional, defaults from the RcvDtl, PODetail or blank.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended Cost for the invoice line item. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  """  
      self.DocExtCost:int = obj["DocExtCost"]
      """  Extended Cost for the invoice line item in Vendors currency. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line in vendors currency.  """  
      self.LineComment:str = obj["LineComment"]
      """  Used to establish invoice comments about the invoice line.  """  
      self.MatchDate:str = obj["MatchDate"]
      """  Mirror image of related RCVHead.ReceiptDate.  Only applies to LineType = U. Updated during the Invoice/Receipt match posting process if GLSyst.PostInvtyWipCos = No.  This date is used as the journal date and to determine the fiscal period when the Invoice/Receipt process is responsible for generating the GL entries. (See CaMatchingDiv description)  """  
      self.MatchFiscalYear:int = obj["MatchFiscalYear"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.MatchFiscalPeriod:int = obj["MatchFiscalPeriod"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this line item.  Defaults from the Part Master.  """  
      self.AdvancePayAmt:int = obj["AdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments.    It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  """  
      self.DocAdvancePayAmt:int = obj["DocAdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments.   It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  Purchase Code.  """  
      self.LineDiscAmt:int = obj["LineDiscAmt"]
      """  Discount amount for this line  """  
      self.DocLineDiscAmt:int = obj["DocLineDiscAmt"]
      """  Discount amount (Vendors Currency) for this line  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceLine:int = obj["GlbInvoiceLine"]
      """  Global Invoice Line identifier.  Used in Consolidated Purchasing.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that G/L entries appearing under this invoice line will have multi-company journals entered at the target external company.  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.Rpt1AdvancePayAmt:int = obj["Rpt1AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvancePayAmt:int = obj["Rpt2AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvancePayAmt:int = obj["Rpt3AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtCost:int = obj["Rpt1ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtCost:int = obj["Rpt2ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtCost:int = obj["Rpt3ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt1LineDiscAmt:int = obj["Rpt1LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2LineDiscAmt:int = obj["Rpt2LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3LineDiscAmt:int = obj["Rpt3LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.DocAdvPayAppld:int = obj["DocAdvPayAppld"]
      """  Amount of advance payment applied  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.MatchFiscalYearSuffix:str = obj["MatchFiscalYearSuffix"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.MatchFiscalCalendarID:str = obj["MatchFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  The Supplier Shipment ID (also known as the ContainerID).  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Addition transaction.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Addition Number or sequence of the linked Asset Addition transaction.  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Used in a correction invoice to store reference to the original invoice line.  """  
      self.DocAssetInvoiceBal:int = obj["DocAssetInvoiceBal"]
      """  This is the current invoice line balance (in vendor currency) left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance of this DocAssetInvoiceBal.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  """  
      self.AssetBalOurQty:int = obj["AssetBalOurQty"]
      """  This is the Invoiced Quantity balance left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  This qty is expressed in our unit of measure.  """  
      self.AssetQtyIUM:str = obj["AssetQtyIUM"]
      """  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  The DMR Number that requires supplier credit.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  The Action Number for the DMR that requires supplier credit.  """  
      self.CreatedFromExpense:bool = obj["CreatedFromExpense"]
      """  Indicates if this invoice line was created from an EmpExpense record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Gen1099Code:str = obj["Gen1099Code"]
      """  Generated 1099 Code where this invoice was calculated in the 1099 Form  """  
      self.EnableIntrastat:bool = obj["EnableIntrastat"]
      """  Indicates if intrastat is available for the line.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.ScrExtCost:int = obj["ScrExtCost"]
      self.ScrDocExtCost:int = obj["ScrDocExtCost"]
      self.ScrTotalMiscChrg:int = obj["ScrTotalMiscChrg"]
      self.ScrDocTotalMiscChrg:int = obj["ScrDocTotalMiscChrg"]
      self.ScrLineType:str = obj["ScrLineType"]
      self.DebitMemo:bool = obj["DebitMemo"]
      self.Variance:int = obj["Variance"]
      self.EnablePurchaseCode:bool = obj["EnablePurchaseCode"]
      self.EnableDiscountAmt:bool = obj["EnableDiscountAmt"]
      self.UsePurchaseCode:bool = obj["UsePurchaseCode"]
      self.LineSubtotal:int = obj["LineSubtotal"]
      self.DocLineSubtotal:int = obj["DocLineSubtotal"]
      self.LineTotal:int = obj["LineTotal"]
      self.DocLineTotal:int = obj["DocLineTotal"]
      self.ScrVendorQty:int = obj["ScrVendorQty"]
      self.ScrOurQty:int = obj["ScrOurQty"]
      self.AllowGLDistAdd:bool = obj["AllowGLDistAdd"]
      self.AllowGLDistAllocation:bool = obj["AllowGLDistAllocation"]
      self.AllowGLDistDelete:bool = obj["AllowGLDistDelete"]
      self.ScrLineDiscAmt:int = obj["ScrLineDiscAmt"]
      self.ScrDocLineDiscAmt:int = obj["ScrDocLineDiscAmt"]
      self.AllowJobMiscAdd:bool = obj["AllowJobMiscAdd"]
      self.AllowJobMiscDelete:bool = obj["AllowJobMiscDelete"]
      self.AllowJobMiscUpdate:bool = obj["AllowJobMiscUpdate"]
      self.AllocationID:str = obj["AllocationID"]
      self.AllocationAmount:int = obj["AllocationAmount"]
      self.RcptReceiptDate:str = obj["RcptReceiptDate"]
      self.RcptPartNum:str = obj["RcptPartNum"]
      self.RcptPartDescription:str = obj["RcptPartDescription"]
      self.RcptDestination:str = obj["RcptDestination"]
      self.RcptVenPartNum:str = obj["RcptVenPartNum"]
      self.RcptVendorQty:int = obj["RcptVendorQty"]
      self.POPartNum:str = obj["POPartNum"]
      self.POLineDesc:str = obj["POLineDesc"]
      self.PORelQty:int = obj["PORelQty"]
      self.POReceivedQty:int = obj["POReceivedQty"]
      self.POVenPartNum:str = obj["POVenPartNum"]
      self.POUnitCost:int = obj["POUnitCost"]
      self.PODocUnitCost:int = obj["PODocUnitCost"]
      self.POCostPerCode:str = obj["POCostPerCode"]
      self.GridVenPartNum:str = obj["GridVenPartNum"]
      """  The VenPartNum field for the datagrid.  For display purposes only.  """  
      self.RcptPUM:str = obj["RcptPUM"]
      self.POPUM:str = obj["POPUM"]
      self.Posted:bool = obj["Posted"]
      self.LineTypeDescription:str = obj["LineTypeDescription"]
      self.GroupID:str = obj["GroupID"]
      self.AllocationDesc:str = obj["AllocationDesc"]
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Indicates if Override Reverse Charge check box should be enabled.  """  
      self.RevChargeMethodDesc:str = obj["RevChargeMethodDesc"]
      """  Reverse Charge Method description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.Rpt1ScrExtCost:int = obj["Rpt1ScrExtCost"]
      self.Rpt2ScrExtCost:int = obj["Rpt2ScrExtCost"]
      self.Rpt3ScrExtCost:int = obj["Rpt3ScrExtCost"]
      self.Rpt1ScrTotalMiscChrg:int = obj["Rpt1ScrTotalMiscChrg"]
      self.Rpt2ScrTotalMiscChrg:int = obj["Rpt2ScrTotalMiscChrg"]
      self.Rpt3ScrTotalMiscChrg:int = obj["Rpt3ScrTotalMiscChrg"]
      self.Rpt1ScrLineDiscAmt:int = obj["Rpt1ScrLineDiscAmt"]
      self.Rpt2ScrLineDiscAmt:int = obj["Rpt2ScrLineDiscAmt"]
      self.Rpt3ScrLineDiscAmt:int = obj["Rpt3ScrLineDiscAmt"]
      self.Rpt1LineSubTotal:int = obj["Rpt1LineSubTotal"]
      self.Rpt2LineSubtotal:int = obj["Rpt2LineSubtotal"]
      self.Rpt3LineSubtotal:int = obj["Rpt3LineSubtotal"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.RcptIUM:str = obj["RcptIUM"]
      """  Receipt Our UOM  """  
      self.RcptOurQty:int = obj["RcptOurQty"]
      """  Receipt Our Quantity  """  
      self.PORelOurQty:int = obj["PORelOurQty"]
      """  PO Rel Our Quantity  """  
      self.PORelIUM:str = obj["PORelIUM"]
      """  PO Rel Our UOM  """  
      self.Rpt1POUnitCost:int = obj["Rpt1POUnitCost"]
      self.Rpt2POUnitCost:int = obj["Rpt2POUnitCost"]
      self.Rpt3POUnitCost:int = obj["Rpt3POUnitCost"]
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.EnableShipmentID:bool = obj["EnableShipmentID"]
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.TotDistribAmt:int = obj["TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Base Currency  """  
      self.DocTotDistribAmt:int = obj["DocTotDistribAmt"]
      """  This is the value of the lines that have been entered. In Document Currency  """  
      self.Rpt1TotDistribAmt:int = obj["Rpt1TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 1.  """  
      self.Rpt2TotDistribAmt:int = obj["Rpt2TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 2.  """  
      self.Rpt3TotDistribAmt:int = obj["Rpt3TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 3.  """  
      self.EnableSubCData:bool = obj["EnableSubCData"]
      self.POWarn:str = obj["POWarn"]
      self.CurrencyID:str = obj["CurrencyID"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.AdjustmentValue:int = obj["AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.DocAdjustmentValue:int = obj["DocAdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt1AdjustmentValue:int = obj["Rpt1AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt2AdjustmentValue:int = obj["Rpt2AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt3AdjustmentValue:int = obj["Rpt3AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.AssetNumAssetDescription:str = obj["AssetNumAssetDescription"]
      """  Mandatory description of the asset.  """  
      self.ContainerIDContainerDescription:str = obj["ContainerIDContainerDescription"]
      """  Free form text that describes this particular container.  """  
      self.GLPurchPurchDesc:str = obj["GLPurchPurchDesc"]
      """  Description of the purchase type. Appears in drop-down lists for selection.  """  
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
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
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
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
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      """  defaults from the company file.  """  
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Indicates the type of invoice line. "R" = Invoiced for Receipt of goods, "A" - Advance Billing,  "M" - Misc. Billing, "U" - Unreceived goods, "J" - Job Miscellaneous charge A/P invoice, "S" - Asset Invoice Line.  Not directly entered,  set by invoice entry by the user selecting the appropriate menu option.  """  
      self.UnitCost:int = obj["UnitCost"]
      """  item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost if related.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  """  
      self.PONum:int = obj["PONum"]
      """   Purchase Order Number that this invoice line item is related to. If packing slip is referenced then it is set = to RcvDtl.PONum and can't be changed.  If entered it must be a valid POHeader record.
A reference is made to the purchase order using PONUM, POLine and PORelNum fields. If any one of these fields are entered then they all must be entered and be valid.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # that invoice is for. Defaulted from the RvcDtl if referenced to packing slip document.. Only applicable when PO is referenced.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being invoiced. Defaulted from RcvDtl if related to a packing slip. If entered it Must be valid.  """  
      self.Description:str = obj["Description"]
      """  Invoice line description.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job that this invoice is related to. Set to the RcvDtl.JobNum.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence that this invoice line is related to. Set to RcvDtl.AssemblySeq.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """  Indicates if this invoice line is related to a job material (jobmtl) or job subcontract (JobOper) record. Valid values are "M" = material or "S" = subcontract. This is set to RvcDtl.JobSeqType.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this line item is costed against. Defaults from the RcvDtl.JobSeq. Only applicable for a receipts to job.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendor's purchase point ID. This is used as part of the foreign key to reference the RcvHead/RcvDtl records.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendor's packing slip that this A\P invoice detail line is associated with. This Along with PackLine provides a relationship to the receipt document detail (RcvDtl)  """  
      self.PackLine:int = obj["PackLine"]
      """  The Pack Slip line of the RcvDtl record  to which this A\P detail record is related to.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Total Invoiced Quantity for the line item.  This is stored in the Vendors Unit of Measure.  Can be defaulted from the packing slip detail if referenced (RcvDtl.POReceiptQty)  """  
      self.PUM:str = obj["PUM"]
      """  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDel.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  """  
      self.OurQty:int = obj["OurQty"]
      """  Invoiced Quantity for the line item in our unit of measure. This can be defaulted from the packing slip detail if referenced (RcvDtl.ReceiptQty)  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure code for invoiced quantity in our unit of measure. Defaulted in the following hierarchy: from the RcvDel.IUM if packing slip is referenced, from PODetail.IUM if PO is referenced, from Part.IUM if valid part or finally from XaSyst.DefaultUM.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the APInvDtl.VendorQty by the appropriate "per" value and then multiply by unit cost.  Use the PODetail.CostPerCode if related to a PO else use Part.PricePerCode if valid part. Else default as "E".
Valid database values are "E" = Each, "C" = per 100 or "M" = per 1,000.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's part number. Optional, defaults from the RcvDtl, PODetail or blank.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended Cost for the invoice line item. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  """  
      self.DocExtCost:int = obj["DocExtCost"]
      """  Extended Cost for the invoice line item in Vendors currency. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line in vendors currency.  """  
      self.LineComment:str = obj["LineComment"]
      """  Used to establish invoice comments about the invoice line.  """  
      self.MatchDate:str = obj["MatchDate"]
      """  Mirror image of related RCVHead.ReceiptDate.  Only applies to LineType = U. Updated during the Invoice/Receipt match posting process if GLSyst.PostInvtyWipCos = No.  This date is used as the journal date and to determine the fiscal period when the Invoice/Receipt process is responsible for generating the GL entries. (See CaMatchingDiv description)  """  
      self.MatchFiscalYear:int = obj["MatchFiscalYear"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.MatchFiscalPeriod:int = obj["MatchFiscalPeriod"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this line item.  Defaults from the Part Master.  """  
      self.AdvancePayAmt:int = obj["AdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments.    It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  """  
      self.DocAdvancePayAmt:int = obj["DocAdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments.   It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  Purchase Code.  """  
      self.LineDiscAmt:int = obj["LineDiscAmt"]
      """  Discount amount for this line  """  
      self.DocLineDiscAmt:int = obj["DocLineDiscAmt"]
      """  Discount amount (Vendors Currency) for this line  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceLine:int = obj["GlbInvoiceLine"]
      """  Global Invoice Line identifier.  Used in Consolidated Purchasing.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that G/L entries appearing under this invoice line will have multi-company journals entered at the target external company.  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.Rpt1AdvancePayAmt:int = obj["Rpt1AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvancePayAmt:int = obj["Rpt2AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvancePayAmt:int = obj["Rpt3AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtCost:int = obj["Rpt1ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtCost:int = obj["Rpt2ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtCost:int = obj["Rpt3ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt1LineDiscAmt:int = obj["Rpt1LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2LineDiscAmt:int = obj["Rpt2LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3LineDiscAmt:int = obj["Rpt3LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.DocAdvPayAppld:int = obj["DocAdvPayAppld"]
      """  Amount of advance payment applied  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.MatchFiscalYearSuffix:str = obj["MatchFiscalYearSuffix"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.MatchFiscalCalendarID:str = obj["MatchFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  The Supplier Shipment ID (also known as the ContainerID).  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Addition transaction.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Addition Number or sequence of the linked Asset Addition transaction.  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Used in a correction invoice to store reference to the original invoice line.  """  
      self.DocAssetInvoiceBal:int = obj["DocAssetInvoiceBal"]
      """  This is the current invoice line balance (in vendor currency) left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance of this DocAssetInvoiceBal.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  """  
      self.AssetBalOurQty:int = obj["AssetBalOurQty"]
      """  This is the Invoiced Quantity balance left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  This qty is expressed in our unit of measure.  """  
      self.AssetQtyIUM:str = obj["AssetQtyIUM"]
      """  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  The DMR Number that requires supplier credit.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  The Action Number for the DMR that requires supplier credit.  """  
      self.CreatedFromExpense:bool = obj["CreatedFromExpense"]
      """  Indicates if this invoice line was created from an EmpExpense record.  """  
      self.InUnitCost:int = obj["InUnitCost"]
      """  item's unit cost in the vendors unit of measure including taxes.  """  
      self.DocInUnitCost:int = obj["DocInUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency including taxes.  """  
      self.Rpt1InUnitCost:int = obj["Rpt1InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitCost:int = obj["Rpt2InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitCost:int = obj["Rpt3InUnitCost"]
      """  Reporting currency value of this field  """  
      self.InExtCost:int = obj["InExtCost"]
      """  Extended Cost for the invoice line item including taxes.  """  
      self.DocInExtCost:int = obj["DocInExtCost"]
      """   Extended Cost for the invoice line item in Vendors currency
including taxes  """  
      self.Rpt1InExtCost:int = obj["Rpt1InExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtCost:int = obj["Rpt2InExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtCost:int = obj["Rpt3InExtCost"]
      """  Reporting currency value of this field  """  
      self.InTotalMiscChrg:int = obj["InTotalMiscChrg"]
      """  Rolled up total of all misc. charge records for this invoice detail line including taxes.  """  
      self.DocInTotalMiscChrg:int = obj["DocInTotalMiscChrg"]
      """  Rolled up total of all misc. charge records for this invoice detail line in vendors currency including taxes.  """  
      self.Rpt1InTotalMiscChrg:int = obj["Rpt1InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2InTotalMiscChrg:int = obj["Rpt2InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3InTotalMiscChrg:int = obj["Rpt3InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.InAdvancePayAmt:int = obj["InAdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments (incl taxes).  """  
      self.DocInAdvancePayAmt:int = obj["DocInAdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments (incl taxes).  """  
      self.Rpt1InAdvancePayAmt:int = obj["Rpt1InAdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InAdvancePayAmt:int = obj["Rpt2InAdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InAdvancePayAmt:int = obj["Rpt3InAdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.InLineDiscAmt:int = obj["InLineDiscAmt"]
      """  Discount amount for this line including taxes  """  
      self.DocInLineDiscAmt:int = obj["DocInLineDiscAmt"]
      """  Discount amount (Vendors Currency) for this line including taxes  """  
      self.Rpt1InLineDiscAmt:int = obj["Rpt1InLineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InLineDiscAmt:int = obj["Rpt2InLineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InLineDiscAmt:int = obj["Rpt3InLineDiscAmt"]
      self.NoTaxRecal:bool = obj["NoTaxRecal"]
      """  Indicates if no tax recalculation by the system is  supposed to be done since with "In Price" tax calculation the tax lines were adjusted or new tax lines added manually  """  
      self.DevInt1:int = obj["DevInt1"]
      """  Reserved for Development - Integer  """  
      self.DevInt2:int = obj["DevInt2"]
      """  Reserved for Development - Integer  """  
      self.DevDec1:int = obj["DevDec1"]
      """  Reserved for development - decimal  """  
      self.DevDec2:int = obj["DevDec2"]
      """  Reserved for development - decimal  """  
      self.DevDec3:int = obj["DevDec3"]
      """  Reserved for development - decimal  """  
      self.DevDec4:int = obj["DevDec4"]
      """  Reserved for development - decimal  """  
      self.DevLog1:bool = obj["DevLog1"]
      """  Reserved for development  - logical  """  
      self.DevLog2:bool = obj["DevLog2"]
      """  Reserved for development - logical  """  
      self.DevChar1:str = obj["DevChar1"]
      """  Reserved for development  - character  """  
      self.DevChar2:str = obj["DevChar2"]
      """  Reserved for development - character  """  
      self.DevDate1:str = obj["DevDate1"]
      """  Reserved for development - date  """  
      self.DevDate2:str = obj["DevDate2"]
      """  Reserved for development - date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ScrWithholdAmt:int = obj["ScrWithholdAmt"]
      """  Withholding Tax Amount  """  
      self.DocScrWithholdAmt:int = obj["DocScrWithholdAmt"]
      """  Withholding Tax Amount in document currency  """  
      self.Rpt1ScrWithholdAmt:int = obj["Rpt1ScrWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.Rpt2ScrWithholdAmt:int = obj["Rpt2ScrWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.Rpt3ScrWithholdAmt:int = obj["Rpt3ScrWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  Invoice Reference Number  """  
      self.APTranNo:int = obj["APTranNo"]
      """  AP Transaction Number  """  
      self.DocAdvPayAppliedAmt:int = obj["DocAdvPayAppliedAmt"]
      """  DocAdvPayAppliedAmt  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code, defaults from Supplier  """  
      self.Gen1099Code:str = obj["Gen1099Code"]
      """  Generated 1099 Code where this invoice was calculated in the 1099 Form  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DeferredExp:bool = obj["DeferredExp"]
      """  DeferredExp  """  
      self.DEACode:str = obj["DEACode"]
      """  DEACode  """  
      self.DEAAmt:int = obj["DEAAmt"]
      """  DEAAmt  """  
      self.DEAStartDate:str = obj["DEAStartDate"]
      """  DEAStartDate  """  
      self.DEAEndDate:str = obj["DEAEndDate"]
      """  DEAEndDate  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.ExternalPONum:str = obj["ExternalPONum"]
      """  This field is used to store the AVP Purchase Order Number.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  Malaysia Import Declaration Number  """  
      self.FinalInvoice:bool = obj["FinalInvoice"]
      """  Flag that indicates if the invoice is the final one for the last partial receipt.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax Amount  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax Amount  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Reporting currency value of this field  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Self-Assess Tax Amount  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Self-Assess Tax Amount  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Reporting currency value of this field  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total Deductible Tax Amount  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total Deductible Tax Amount  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Reporting currency value of this field  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  Project Billing Invoice Number  """  
      self.CancellationDtl:bool = obj["CancellationDtl"]
      """  Will be set to Yes if the AP Invoice Dtl was created by the Cancellation logic.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.TaxExemptReasonCode:str = obj["TaxExemptReasonCode"]
      """  TaxExemptReasonCode  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.AdjustmentValue:int = obj["AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.AllocationAmount:int = obj["AllocationAmount"]
      self.AllocationDesc:str = obj["AllocationDesc"]
      self.AllocationID:str = obj["AllocationID"]
      self.AllowGLDistAdd:bool = obj["AllowGLDistAdd"]
      self.AllowGLDistAllocation:bool = obj["AllowGLDistAllocation"]
      self.AllowGLDistDelete:bool = obj["AllowGLDistDelete"]
      self.AllowJobMiscAdd:bool = obj["AllowJobMiscAdd"]
      self.AllowJobMiscDelete:bool = obj["AllowJobMiscDelete"]
      self.AllowJobMiscUpdate:bool = obj["AllowJobMiscUpdate"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyID:str = obj["CurrencyID"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DEACodeDesc:str = obj["DEACodeDesc"]
      self.DEAScheduled:bool = obj["DEAScheduled"]
      """  Is Deferred Expense Amortization Scheduled  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      self.Distributed:int = obj["Distributed"]
      """  DEA Distributed Amount  """  
      self.DocAdjustmentValue:int = obj["DocAdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.DocAllocationAmount:int = obj["DocAllocationAmount"]
      self.DocDistributed:int = obj["DocDistributed"]
      """  DEA Distributed Amount in Doc Currency  """  
      self.DocDspLineTotal:int = obj["DocDspLineTotal"]
      self.DocExpense:int = obj["DocExpense"]
      """  DEA Expense Amount in Doc Currency  """  
      self.DocGLLineTotal:int = obj["DocGLLineTotal"]
      self.DocInTaxAmt:int = obj["DocInTaxAmt"]
      self.DocLineExpenses:int = obj["DocLineExpenses"]
      self.DocLineSubtotal:int = obj["DocLineSubtotal"]
      self.DocLineTotal:int = obj["DocLineTotal"]
      self.DocNonDeducTaxExpense:int = obj["DocNonDeducTaxExpense"]
      self.DocOrgExtCost:int = obj["DocOrgExtCost"]
      """  Value of original Ext Cost in document currency. Used for adjustment lines.  """  
      self.DocPEDetAmt:int = obj["DocPEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.DocRecognized:int = obj["DocRecognized"]
      """  DEA Recognized Amount in Doc Currency  """  
      self.DocRemaining:int = obj["DocRemaining"]
      """  DEA Remaining Amount in Doc Currency  """  
      self.DocScrInvoiceBal:int = obj["DocScrInvoiceBal"]
      self.DocScrTotalDedTax:int = obj["DocScrTotalDedTax"]
      self.DocScrTotalSATax:int = obj["DocScrTotalSATax"]
      self.DocScrTotalTax:int = obj["DocScrTotalTax"]
      self.DocScrUnitCost:int = obj["DocScrUnitCost"]
      self.DocTotDistribAmt:int = obj["DocTotDistribAmt"]
      """  This is the value of the lines that have been entered. In Document Currency  """  
      self.DocUnrecognized:int = obj["DocUnrecognized"]
      """  DEA Unrecognized Amount in Doc Currency  """  
      self.DocVariance:int = obj["DocVariance"]
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.DspAllocationAmount:int = obj["DspAllocationAmount"]
      self.DspLineTotal:int = obj["DspLineTotal"]
      self.EnableDiscountAmt:bool = obj["EnableDiscountAmt"]
      self.EnableIntrastat:bool = obj["EnableIntrastat"]
      """  Indicates if intrastat is available for the line.  """  
      self.EnableIntrastatDsp:bool = obj["EnableIntrastatDsp"]
      """  Indicates if intrastat is available for to be diplayed for the line. Used by AP invoice tracker  """  
      self.EnablePurchaseCode:bool = obj["EnablePurchaseCode"]
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Indicates if Override Reverse Charge check box should be enabled.  """  
      self.EnableScrWithholdAmt:bool = obj["EnableScrWithholdAmt"]
      self.EnableShipmentID:bool = obj["EnableShipmentID"]
      self.EnableSubCData:bool = obj["EnableSubCData"]
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.Expense:int = obj["Expense"]
      """  DEA Expense Amount  """  
      self.GLAccount:str = obj["GLAccount"]
      self.GLLineTotal:int = obj["GLLineTotal"]
      self.GridVenPartNum:str = obj["GridVenPartNum"]
      """  The VenPartNum field for the datagrid.  For display purposes only.  """  
      self.GroupID:str = obj["GroupID"]
      self.InPrice:bool = obj["InPrice"]
      self.InTaxAmt:int = obj["InTaxAmt"]
      self.IsAdvance:bool = obj["IsAdvance"]
      """  To determine if line have Advance Billing Line  """  
      self.JPTaxAdjustment:bool = obj["JPTaxAdjustment"]
      """  Japan Tax Adjustment Line  """  
      self.LineExpenses:int = obj["LineExpenses"]
      self.LineSubtotal:int = obj["LineSubtotal"]
      self.LineTotal:int = obj["LineTotal"]
      self.LineTypeDescription:str = obj["LineTypeDescription"]
      self.NonDeducTaxExpense:int = obj["NonDeducTaxExpense"]
      self.OrgExtCost:int = obj["OrgExtCost"]
      """  Value of original Ext Cost in base currency. Used for adjustment lines.  """  
      self.PEDetAmt:int = obj["PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.POCostPerCode:str = obj["POCostPerCode"]
      self.PODocUnitCost:int = obj["PODocUnitCost"]
      self.POLineDesc:str = obj["POLineDesc"]
      self.POPartNum:str = obj["POPartNum"]
      self.POPUM:str = obj["POPUM"]
      self.POReceivedQty:int = obj["POReceivedQty"]
      self.PORelIUM:str = obj["PORelIUM"]
      """  PO Rel Our UOM  """  
      self.PORelOurQty:int = obj["PORelOurQty"]
      """  PO Rel Our Quantity  """  
      self.PORelQty:int = obj["PORelQty"]
      self.Posted:bool = obj["Posted"]
      self.POUnitCost:int = obj["POUnitCost"]
      self.POVenPartNum:str = obj["POVenPartNum"]
      self.POWarn:str = obj["POWarn"]
      self.Print1099:bool = obj["Print1099"]
      """  Print 1099  """  
      self.RcptDestination:str = obj["RcptDestination"]
      self.RcptIUM:str = obj["RcptIUM"]
      """  Receipt Our UOM  """  
      self.RcptOurQty:int = obj["RcptOurQty"]
      """  Receipt Our Quantity  """  
      self.RcptPartDescription:str = obj["RcptPartDescription"]
      self.RcptPartNum:str = obj["RcptPartNum"]
      self.RcptPUM:str = obj["RcptPUM"]
      self.RcptReceiptDate:str = obj["RcptReceiptDate"]
      self.RcptVendorQty:int = obj["RcptVendorQty"]
      self.RcptVenPartNum:str = obj["RcptVenPartNum"]
      self.RecalcGLAcct:bool = obj["RecalcGLAcct"]
      self.Recognized:int = obj["Recognized"]
      """  DEA Recognized Amount  """  
      self.Remaining:int = obj["Remaining"]
      """  DEA Remaining Amount  """  
      self.RevChargeMethodDesc:str = obj["RevChargeMethodDesc"]
      """  Reverse Charge Method description  """  
      self.Rpt1AdjustmentValue:int = obj["Rpt1AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt1AllocationAmount:int = obj["Rpt1AllocationAmount"]
      self.Rpt1Distributed:int = obj["Rpt1Distributed"]
      """  DEA Distributed Amount in Rpt1 Currency  """  
      self.Rpt1DspLineTotal:int = obj["Rpt1DspLineTotal"]
      self.Rpt1Expense:int = obj["Rpt1Expense"]
      """  DEA Expense Amount in Rpt1 Currency  """  
      self.Rpt1GLLineTotal:int = obj["Rpt1GLLineTotal"]
      self.Rpt1InTaxAmt:int = obj["Rpt1InTaxAmt"]
      self.Rpt1LineExpenses:int = obj["Rpt1LineExpenses"]
      self.Rpt1LineSubTotal:int = obj["Rpt1LineSubTotal"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1NonDeducTaxExpense:int = obj["Rpt1NonDeducTaxExpense"]
      self.Rpt1OrgExtCost:int = obj["Rpt1OrgExtCost"]
      """  Value of original Ext Cost in reporting currency. Used for adjustment lines.  """  
      self.Rpt1PEDetAmt:int = obj["Rpt1PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt1POUnitCost:int = obj["Rpt1POUnitCost"]
      self.Rpt1Recognized:int = obj["Rpt1Recognized"]
      """  DEA Recognized Amount in Rpt1 Currency  """  
      self.Rpt1Remaining:int = obj["Rpt1Remaining"]
      """  DEA Remaining Amount in Rpt1 Currency  """  
      self.Rpt1ScrExtCost:int = obj["Rpt1ScrExtCost"]
      self.Rpt1ScrInvoiceBal:int = obj["Rpt1ScrInvoiceBal"]
      self.Rpt1ScrLineDiscAmt:int = obj["Rpt1ScrLineDiscAmt"]
      self.Rpt1ScrTotalDedTax:int = obj["Rpt1ScrTotalDedTax"]
      self.Rpt1ScrTotalMiscChrg:int = obj["Rpt1ScrTotalMiscChrg"]
      self.Rpt1ScrTotalSATax:int = obj["Rpt1ScrTotalSATax"]
      self.Rpt1ScrTotalTax:int = obj["Rpt1ScrTotalTax"]
      self.Rpt1ScrUnitCost:int = obj["Rpt1ScrUnitCost"]
      self.Rpt1TotDistribAmt:int = obj["Rpt1TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 1.  """  
      self.Rpt1Unrecognized:int = obj["Rpt1Unrecognized"]
      """  DEA Unrecognized Amount in Rpt1 Currency  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      self.Rpt2AdjustmentValue:int = obj["Rpt2AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt2AllocationAmount:int = obj["Rpt2AllocationAmount"]
      self.Rpt2Distributed:int = obj["Rpt2Distributed"]
      """  DEA Distributed Amount in Rpt2 Currency  """  
      self.Rpt2DspLineTotal:int = obj["Rpt2DspLineTotal"]
      self.Rpt2Expense:int = obj["Rpt2Expense"]
      """  DEA Expense Amount in Rpt2 Currency  """  
      self.Rpt2GLLineTotal:int = obj["Rpt2GLLineTotal"]
      self.Rpt2InTaxAmt:int = obj["Rpt2InTaxAmt"]
      self.Rpt2LineExpenses:int = obj["Rpt2LineExpenses"]
      self.Rpt2LineSubtotal:int = obj["Rpt2LineSubtotal"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2NonDeducTaxExpense:int = obj["Rpt2NonDeducTaxExpense"]
      self.Rpt2OrgExtCost:int = obj["Rpt2OrgExtCost"]
      """  Value of original Ext Cost in reporting currency. Used for adjustment lines.  """  
      self.Rpt2PEDetAmt:int = obj["Rpt2PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt2POUnitCost:int = obj["Rpt2POUnitCost"]
      self.Rpt2Recognized:int = obj["Rpt2Recognized"]
      """  DEA Recognized Amount in Rpt2 Currency  """  
      self.Rpt2Remaining:int = obj["Rpt2Remaining"]
      """  DEA Remaining Amount in Rpt2 Currency  """  
      self.Rpt2ScrExtCost:int = obj["Rpt2ScrExtCost"]
      self.Rpt2ScrInvoiceBal:int = obj["Rpt2ScrInvoiceBal"]
      self.Rpt2ScrLineDiscAmt:int = obj["Rpt2ScrLineDiscAmt"]
      self.Rpt2ScrTotalDedTax:int = obj["Rpt2ScrTotalDedTax"]
      self.Rpt2ScrTotalMiscChrg:int = obj["Rpt2ScrTotalMiscChrg"]
      self.Rpt2ScrTotalSATax:int = obj["Rpt2ScrTotalSATax"]
      self.Rpt2ScrTotalTax:int = obj["Rpt2ScrTotalTax"]
      self.Rpt2ScrUnitCost:int = obj["Rpt2ScrUnitCost"]
      self.Rpt2TotDistribAmt:int = obj["Rpt2TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 2.  """  
      self.Rpt2Unrecognized:int = obj["Rpt2Unrecognized"]
      """  DEA Unrecognized Amount in Rpt2 Currency  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      self.Rpt3AdjustmentValue:int = obj["Rpt3AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt3AllocationAmount:int = obj["Rpt3AllocationAmount"]
      self.Rpt3Distributed:int = obj["Rpt3Distributed"]
      """  DEA Distributed Amount in Rpt3 Currency  """  
      self.Rpt3DspLineTotal:int = obj["Rpt3DspLineTotal"]
      self.Rpt3Expense:int = obj["Rpt3Expense"]
      """  DEA Expense Amount in Rpt3 Currency  """  
      self.Rpt3GLLineTotal:int = obj["Rpt3GLLineTotal"]
      self.Rpt3InTaxAmt:int = obj["Rpt3InTaxAmt"]
      self.Rpt3LineExpenses:int = obj["Rpt3LineExpenses"]
      self.Rpt3LineSubtotal:int = obj["Rpt3LineSubtotal"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3NonDeducTaxExpense:int = obj["Rpt3NonDeducTaxExpense"]
      self.Rpt3OrgExtCost:int = obj["Rpt3OrgExtCost"]
      """  Value of original Ext Cost in reporting currency. Used for adjustment lines.  """  
      self.Rpt3PEDetAmt:int = obj["Rpt3PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt3POUnitCost:int = obj["Rpt3POUnitCost"]
      self.Rpt3Recognized:int = obj["Rpt3Recognized"]
      """  DEA Recognized Amount in Rpt3 Currency  """  
      self.Rpt3Remaining:int = obj["Rpt3Remaining"]
      """  DEA Remaining Amount in Rpt3 Currency  """  
      self.Rpt3ScrExtCost:int = obj["Rpt3ScrExtCost"]
      self.Rpt3ScrInvoiceBal:int = obj["Rpt3ScrInvoiceBal"]
      self.Rpt3ScrLineDiscAmt:int = obj["Rpt3ScrLineDiscAmt"]
      self.Rpt3ScrTotalDedTax:int = obj["Rpt3ScrTotalDedTax"]
      self.Rpt3ScrTotalMiscChrg:int = obj["Rpt3ScrTotalMiscChrg"]
      self.Rpt3ScrTotalSATax:int = obj["Rpt3ScrTotalSATax"]
      self.Rpt3ScrTotalTax:int = obj["Rpt3ScrTotalTax"]
      self.Rpt3ScrUnitCost:int = obj["Rpt3ScrUnitCost"]
      self.Rpt3TotDistribAmt:int = obj["Rpt3TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 3.  """  
      self.Rpt3Unrecognized:int = obj["Rpt3Unrecognized"]
      """  DEA Unrecognized Amount in Rpt3 Currency  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      self.ScrDocExtCost:int = obj["ScrDocExtCost"]
      self.ScrDocLineDiscAmt:int = obj["ScrDocLineDiscAmt"]
      self.ScrDocTotalMiscChrg:int = obj["ScrDocTotalMiscChrg"]
      self.ScrExtCost:int = obj["ScrExtCost"]
      self.ScrInvoiceBal:int = obj["ScrInvoiceBal"]
      self.ScrInvoiceRef:str = obj["ScrInvoiceRef"]
      """  Invoice ref for BOE  """  
      self.ScrLineDiscAmt:int = obj["ScrLineDiscAmt"]
      self.ScrLineType:str = obj["ScrLineType"]
      self.ScrOurQty:int = obj["ScrOurQty"]
      self.ScrTotalDedTax:int = obj["ScrTotalDedTax"]
      self.ScrTotalMiscChrg:int = obj["ScrTotalMiscChrg"]
      self.ScrTotalSATax:int = obj["ScrTotalSATax"]
      self.ScrTotalTax:int = obj["ScrTotalTax"]
      self.ScrUnitCost:int = obj["ScrUnitCost"]
      self.ScrVendorQty:int = obj["ScrVendorQty"]
      self.TotDistribAmt:int = obj["TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Base Currency  """  
      self.Unrecognized:int = obj["Unrecognized"]
      """  DEA Unrecognized Amount  """  
      self.UpdateExtCreateLineGL:bool = obj["UpdateExtCreateLineGL"]
      """  Indicates if line GL should be automatically created when running UpdateExt.  """  
      self.UsePurchaseCode:bool = obj["UsePurchaseCode"]
      self.Variance:int = obj["Variance"]
      self.UpdateExtOverrideRcpts:bool = obj["UpdateExtOverrideRcpts"]
      """  Indicates that  if LineType=R, then override standard UpdateExt logic to create APInvDtl data directly, as is done in the UI.  Before/AfterGetNew, Before/AfterUpdate will not run.  """  
      self.RelatedToRcvDtlSysRowID:str = obj["RelatedToRcvDtlSysRowID"]
      """  SysRowID of the related RcvDtl row for receipt line,  LineType = R  """  
      self.EnableAttributeSetBtn:bool = obj["EnableAttributeSetBtn"]
      self.DEPayStatCodeDescr:str = obj["DEPayStatCodeDescr"]
      """  DEPayStatCode Description  """  
      self.DEDenominationDescr:str = obj["DEDenominationDescr"]
      """  DEDenomination Description  """  
      self.PORevisionNum:str = obj["PORevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.RcptRevisionNum:str = obj["RcptRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.AssetNumAssetDescription:str = obj["AssetNumAssetDescription"]
      self.Code1099Description:str = obj["Code1099Description"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.ContainerIDContainerDescription:str = obj["ContainerIDContainerDescription"]
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      self.GLPurchPurchDesc:str = obj["GLPurchPurchDesc"]
      self.InvoiceNumDebitMemo:bool = obj["InvoiceNumDebitMemo"]
      self.InvoiceNumPosted:bool = obj["InvoiceNumPosted"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.InvoiceNumCurrencyCode:str = obj["InvoiceNumCurrencyCode"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorPPName:str = obj["VendorPPName"]
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   vendorNum
   invoiceNum
   invoiceLine
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_APInvDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Indicates the type of invoice line. "R" = Invoiced for Receipt of goods, "A" - Advance Billing,  "M" - Misc. Billing, "U" - Unreceived goods, "J" - Job Miscellaneous charge A/P invoice, "S" - Asset Invoice Line.  Not directly entered,  set by invoice entry by the user selecting the appropriate menu option.  """  
      self.UnitCost:int = obj["UnitCost"]
      """  item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost if related.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  """  
      self.PONum:int = obj["PONum"]
      """   Purchase Order Number that this invoice line item is related to. If packing slip is referenced then it is set = to RcvDtl.PONum and can't be changed.  If entered it must be a valid POHeader record.
A reference is made to the purchase order using PONUM, POLine and PORelNum fields. If any one of these fields are entered then they all must be entered and be valid.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # that invoice is for. Defaulted from the RvcDtl if referenced to packing slip document.. Only applicable when PO is referenced.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being invoiced. Defaulted from RcvDtl if related to a packing slip. If entered it Must be valid.  """  
      self.Description:str = obj["Description"]
      """  Invoice line description.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job that this invoice is related to. Set to the RcvDtl.JobNum.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence that this invoice line is related to. Set to RcvDtl.AssemblySeq.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """  Indicates if this invoice line is related to a job material (jobmtl) or job subcontract (JobOper) record. Valid values are "M" = material or "S" = subcontract. This is set to RvcDtl.JobSeqType.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this line item is costed against. Defaults from the RcvDtl.JobSeq. Only applicable for a receipts to job.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendor's purchase point ID. This is used as part of the foreign key to reference the RcvHead/RcvDtl records.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendor's packing slip that this A\P invoice detail line is associated with. This Along with PackLine provides a relationship to the receipt document detail (RcvDtl)  """  
      self.PackLine:int = obj["PackLine"]
      """  The Pack Slip line of the RcvDtl record  to which this A\P detail record is related to.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Total Invoiced Quantity for the line item.  This is stored in the Vendors Unit of Measure.  Can be defaulted from the packing slip detail if referenced (RcvDtl.POReceiptQty)  """  
      self.PUM:str = obj["PUM"]
      """  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDel.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  """  
      self.OurQty:int = obj["OurQty"]
      """  Invoiced Quantity for the line item in our unit of measure. This can be defaulted from the packing slip detail if referenced (RcvDtl.ReceiptQty)  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure code for invoiced quantity in our unit of measure. Defaulted in the following hierarchy: from the RcvDel.IUM if packing slip is referenced, from PODetail.IUM if PO is referenced, from Part.IUM if valid part or finally from XaSyst.DefaultUM.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the APInvDtl.VendorQty by the appropriate "per" value and then multiply by unit cost.  Use the PODetail.CostPerCode if related to a PO else use Part.PricePerCode if valid part. Else default as "E".
Valid database values are "E" = Each, "C" = per 100 or "M" = per 1,000.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's part number. Optional, defaults from the RcvDtl, PODetail or blank.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended Cost for the invoice line item. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  """  
      self.DocExtCost:int = obj["DocExtCost"]
      """  Extended Cost for the invoice line item in Vendors currency. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line in vendors currency.  """  
      self.LineComment:str = obj["LineComment"]
      """  Used to establish invoice comments about the invoice line.  """  
      self.MatchDate:str = obj["MatchDate"]
      """  Mirror image of related RCVHead.ReceiptDate.  Only applies to LineType = U. Updated during the Invoice/Receipt match posting process if GLSyst.PostInvtyWipCos = No.  This date is used as the journal date and to determine the fiscal period when the Invoice/Receipt process is responsible for generating the GL entries. (See CaMatchingDiv description)  """  
      self.MatchFiscalYear:int = obj["MatchFiscalYear"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.MatchFiscalPeriod:int = obj["MatchFiscalPeriod"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this line item.  Defaults from the Part Master.  """  
      self.AdvancePayAmt:int = obj["AdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments.    It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  """  
      self.DocAdvancePayAmt:int = obj["DocAdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments.   It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  Purchase Code.  """  
      self.LineDiscAmt:int = obj["LineDiscAmt"]
      """  Discount amount for this line  """  
      self.DocLineDiscAmt:int = obj["DocLineDiscAmt"]
      """  Discount amount (Vendors Currency) for this line  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceLine:int = obj["GlbInvoiceLine"]
      """  Global Invoice Line identifier.  Used in Consolidated Purchasing.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that G/L entries appearing under this invoice line will have multi-company journals entered at the target external company.  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.Rpt1AdvancePayAmt:int = obj["Rpt1AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvancePayAmt:int = obj["Rpt2AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvancePayAmt:int = obj["Rpt3AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtCost:int = obj["Rpt1ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtCost:int = obj["Rpt2ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtCost:int = obj["Rpt3ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt1LineDiscAmt:int = obj["Rpt1LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2LineDiscAmt:int = obj["Rpt2LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3LineDiscAmt:int = obj["Rpt3LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.DocAdvPayAppld:int = obj["DocAdvPayAppld"]
      """  Amount of advance payment applied  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.MatchFiscalYearSuffix:str = obj["MatchFiscalYearSuffix"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.MatchFiscalCalendarID:str = obj["MatchFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  The Supplier Shipment ID (also known as the ContainerID).  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Addition transaction.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Addition Number or sequence of the linked Asset Addition transaction.  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Used in a correction invoice to store reference to the original invoice line.  """  
      self.DocAssetInvoiceBal:int = obj["DocAssetInvoiceBal"]
      """  This is the current invoice line balance (in vendor currency) left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance of this DocAssetInvoiceBal.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  """  
      self.AssetBalOurQty:int = obj["AssetBalOurQty"]
      """  This is the Invoiced Quantity balance left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  This qty is expressed in our unit of measure.  """  
      self.AssetQtyIUM:str = obj["AssetQtyIUM"]
      """  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  The DMR Number that requires supplier credit.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  The Action Number for the DMR that requires supplier credit.  """  
      self.CreatedFromExpense:bool = obj["CreatedFromExpense"]
      """  Indicates if this invoice line was created from an EmpExpense record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Gen1099Code:str = obj["Gen1099Code"]
      """  Generated 1099 Code where this invoice was calculated in the 1099 Form  """  
      self.EnableIntrastat:bool = obj["EnableIntrastat"]
      """  Indicates if intrastat is available for the line.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.ScrExtCost:int = obj["ScrExtCost"]
      self.ScrDocExtCost:int = obj["ScrDocExtCost"]
      self.ScrTotalMiscChrg:int = obj["ScrTotalMiscChrg"]
      self.ScrDocTotalMiscChrg:int = obj["ScrDocTotalMiscChrg"]
      self.ScrLineType:str = obj["ScrLineType"]
      self.DebitMemo:bool = obj["DebitMemo"]
      self.Variance:int = obj["Variance"]
      self.EnablePurchaseCode:bool = obj["EnablePurchaseCode"]
      self.EnableDiscountAmt:bool = obj["EnableDiscountAmt"]
      self.UsePurchaseCode:bool = obj["UsePurchaseCode"]
      self.LineSubtotal:int = obj["LineSubtotal"]
      self.DocLineSubtotal:int = obj["DocLineSubtotal"]
      self.LineTotal:int = obj["LineTotal"]
      self.DocLineTotal:int = obj["DocLineTotal"]
      self.ScrVendorQty:int = obj["ScrVendorQty"]
      self.ScrOurQty:int = obj["ScrOurQty"]
      self.AllowGLDistAdd:bool = obj["AllowGLDistAdd"]
      self.AllowGLDistAllocation:bool = obj["AllowGLDistAllocation"]
      self.AllowGLDistDelete:bool = obj["AllowGLDistDelete"]
      self.ScrLineDiscAmt:int = obj["ScrLineDiscAmt"]
      self.ScrDocLineDiscAmt:int = obj["ScrDocLineDiscAmt"]
      self.AllowJobMiscAdd:bool = obj["AllowJobMiscAdd"]
      self.AllowJobMiscDelete:bool = obj["AllowJobMiscDelete"]
      self.AllowJobMiscUpdate:bool = obj["AllowJobMiscUpdate"]
      self.AllocationID:str = obj["AllocationID"]
      self.AllocationAmount:int = obj["AllocationAmount"]
      self.RcptReceiptDate:str = obj["RcptReceiptDate"]
      self.RcptPartNum:str = obj["RcptPartNum"]
      self.RcptPartDescription:str = obj["RcptPartDescription"]
      self.RcptDestination:str = obj["RcptDestination"]
      self.RcptVenPartNum:str = obj["RcptVenPartNum"]
      self.RcptVendorQty:int = obj["RcptVendorQty"]
      self.POPartNum:str = obj["POPartNum"]
      self.POLineDesc:str = obj["POLineDesc"]
      self.PORelQty:int = obj["PORelQty"]
      self.POReceivedQty:int = obj["POReceivedQty"]
      self.POVenPartNum:str = obj["POVenPartNum"]
      self.POUnitCost:int = obj["POUnitCost"]
      self.PODocUnitCost:int = obj["PODocUnitCost"]
      self.POCostPerCode:str = obj["POCostPerCode"]
      self.GridVenPartNum:str = obj["GridVenPartNum"]
      """  The VenPartNum field for the datagrid.  For display purposes only.  """  
      self.RcptPUM:str = obj["RcptPUM"]
      self.POPUM:str = obj["POPUM"]
      self.Posted:bool = obj["Posted"]
      self.LineTypeDescription:str = obj["LineTypeDescription"]
      self.GroupID:str = obj["GroupID"]
      self.AllocationDesc:str = obj["AllocationDesc"]
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Indicates if Override Reverse Charge check box should be enabled.  """  
      self.RevChargeMethodDesc:str = obj["RevChargeMethodDesc"]
      """  Reverse Charge Method description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.Rpt1ScrExtCost:int = obj["Rpt1ScrExtCost"]
      self.Rpt2ScrExtCost:int = obj["Rpt2ScrExtCost"]
      self.Rpt3ScrExtCost:int = obj["Rpt3ScrExtCost"]
      self.Rpt1ScrTotalMiscChrg:int = obj["Rpt1ScrTotalMiscChrg"]
      self.Rpt2ScrTotalMiscChrg:int = obj["Rpt2ScrTotalMiscChrg"]
      self.Rpt3ScrTotalMiscChrg:int = obj["Rpt3ScrTotalMiscChrg"]
      self.Rpt1ScrLineDiscAmt:int = obj["Rpt1ScrLineDiscAmt"]
      self.Rpt2ScrLineDiscAmt:int = obj["Rpt2ScrLineDiscAmt"]
      self.Rpt3ScrLineDiscAmt:int = obj["Rpt3ScrLineDiscAmt"]
      self.Rpt1LineSubTotal:int = obj["Rpt1LineSubTotal"]
      self.Rpt2LineSubtotal:int = obj["Rpt2LineSubtotal"]
      self.Rpt3LineSubtotal:int = obj["Rpt3LineSubtotal"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.RcptIUM:str = obj["RcptIUM"]
      """  Receipt Our UOM  """  
      self.RcptOurQty:int = obj["RcptOurQty"]
      """  Receipt Our Quantity  """  
      self.PORelOurQty:int = obj["PORelOurQty"]
      """  PO Rel Our Quantity  """  
      self.PORelIUM:str = obj["PORelIUM"]
      """  PO Rel Our UOM  """  
      self.Rpt1POUnitCost:int = obj["Rpt1POUnitCost"]
      self.Rpt2POUnitCost:int = obj["Rpt2POUnitCost"]
      self.Rpt3POUnitCost:int = obj["Rpt3POUnitCost"]
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.EnableShipmentID:bool = obj["EnableShipmentID"]
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.TotDistribAmt:int = obj["TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Base Currency  """  
      self.DocTotDistribAmt:int = obj["DocTotDistribAmt"]
      """  This is the value of the lines that have been entered. In Document Currency  """  
      self.Rpt1TotDistribAmt:int = obj["Rpt1TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 1.  """  
      self.Rpt2TotDistribAmt:int = obj["Rpt2TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 2.  """  
      self.Rpt3TotDistribAmt:int = obj["Rpt3TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 3.  """  
      self.EnableSubCData:bool = obj["EnableSubCData"]
      self.POWarn:str = obj["POWarn"]
      self.CurrencyID:str = obj["CurrencyID"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.AdjustmentValue:int = obj["AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.DocAdjustmentValue:int = obj["DocAdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt1AdjustmentValue:int = obj["Rpt1AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt2AdjustmentValue:int = obj["Rpt2AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt3AdjustmentValue:int = obj["Rpt3AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.AssetNumAssetDescription:str = obj["AssetNumAssetDescription"]
      """  Mandatory description of the asset.  """  
      self.ContainerIDContainerDescription:str = obj["ContainerIDContainerDescription"]
      """  Free form text that describes this particular container.  """  
      self.GLPurchPurchDesc:str = obj["GLPurchPurchDesc"]
      """  Description of the purchase type. Appears in drop-down lists for selection.  """  
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
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
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
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
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      """  defaults from the company file.  """  
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvDtlListTableset:
   def __init__(self, obj):
      self.APInvDtlList:list[Erp_Tablesets_APInvDtlListRow] = obj["APInvDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APInvDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Indicates the type of invoice line. "R" = Invoiced for Receipt of goods, "A" - Advance Billing,  "M" - Misc. Billing, "U" - Unreceived goods, "J" - Job Miscellaneous charge A/P invoice, "S" - Asset Invoice Line.  Not directly entered,  set by invoice entry by the user selecting the appropriate menu option.  """  
      self.UnitCost:int = obj["UnitCost"]
      """  item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost if related.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  """  
      self.PONum:int = obj["PONum"]
      """   Purchase Order Number that this invoice line item is related to. If packing slip is referenced then it is set = to RcvDtl.PONum and can't be changed.  If entered it must be a valid POHeader record.
A reference is made to the purchase order using PONUM, POLine and PORelNum fields. If any one of these fields are entered then they all must be entered and be valid.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # that invoice is for. Defaulted from the RvcDtl if referenced to packing slip document.. Only applicable when PO is referenced.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being invoiced. Defaulted from RcvDtl if related to a packing slip. If entered it Must be valid.  """  
      self.Description:str = obj["Description"]
      """  Invoice line description.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job that this invoice is related to. Set to the RcvDtl.JobNum.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence that this invoice line is related to. Set to RcvDtl.AssemblySeq.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """  Indicates if this invoice line is related to a job material (jobmtl) or job subcontract (JobOper) record. Valid values are "M" = material or "S" = subcontract. This is set to RvcDtl.JobSeqType.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this line item is costed against. Defaults from the RcvDtl.JobSeq. Only applicable for a receipts to job.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendor's purchase point ID. This is used as part of the foreign key to reference the RcvHead/RcvDtl records.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendor's packing slip that this A\P invoice detail line is associated with. This Along with PackLine provides a relationship to the receipt document detail (RcvDtl)  """  
      self.PackLine:int = obj["PackLine"]
      """  The Pack Slip line of the RcvDtl record  to which this A\P detail record is related to.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Total Invoiced Quantity for the line item.  This is stored in the Vendors Unit of Measure.  Can be defaulted from the packing slip detail if referenced (RcvDtl.POReceiptQty)  """  
      self.PUM:str = obj["PUM"]
      """  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDel.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  """  
      self.OurQty:int = obj["OurQty"]
      """  Invoiced Quantity for the line item in our unit of measure. This can be defaulted from the packing slip detail if referenced (RcvDtl.ReceiptQty)  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure code for invoiced quantity in our unit of measure. Defaulted in the following hierarchy: from the RcvDel.IUM if packing slip is referenced, from PODetail.IUM if PO is referenced, from Part.IUM if valid part or finally from XaSyst.DefaultUM.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the APInvDtl.VendorQty by the appropriate "per" value and then multiply by unit cost.  Use the PODetail.CostPerCode if related to a PO else use Part.PricePerCode if valid part. Else default as "E".
Valid database values are "E" = Each, "C" = per 100 or "M" = per 1,000.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's part number. Optional, defaults from the RcvDtl, PODetail or blank.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended Cost for the invoice line item. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  """  
      self.DocExtCost:int = obj["DocExtCost"]
      """  Extended Cost for the invoice line item in Vendors currency. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line in vendors currency.  """  
      self.LineComment:str = obj["LineComment"]
      """  Used to establish invoice comments about the invoice line.  """  
      self.MatchDate:str = obj["MatchDate"]
      """  Mirror image of related RCVHead.ReceiptDate.  Only applies to LineType = U. Updated during the Invoice/Receipt match posting process if GLSyst.PostInvtyWipCos = No.  This date is used as the journal date and to determine the fiscal period when the Invoice/Receipt process is responsible for generating the GL entries. (See CaMatchingDiv description)  """  
      self.MatchFiscalYear:int = obj["MatchFiscalYear"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.MatchFiscalPeriod:int = obj["MatchFiscalPeriod"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this line item.  Defaults from the Part Master.  """  
      self.AdvancePayAmt:int = obj["AdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments.    It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  """  
      self.DocAdvancePayAmt:int = obj["DocAdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments.   It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  Purchase Code.  """  
      self.LineDiscAmt:int = obj["LineDiscAmt"]
      """  Discount amount for this line  """  
      self.DocLineDiscAmt:int = obj["DocLineDiscAmt"]
      """  Discount amount (Vendors Currency) for this line  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceLine:int = obj["GlbInvoiceLine"]
      """  Global Invoice Line identifier.  Used in Consolidated Purchasing.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that G/L entries appearing under this invoice line will have multi-company journals entered at the target external company.  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.Rpt1AdvancePayAmt:int = obj["Rpt1AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvancePayAmt:int = obj["Rpt2AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvancePayAmt:int = obj["Rpt3AdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtCost:int = obj["Rpt1ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtCost:int = obj["Rpt2ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtCost:int = obj["Rpt3ExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt1LineDiscAmt:int = obj["Rpt1LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2LineDiscAmt:int = obj["Rpt2LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3LineDiscAmt:int = obj["Rpt3LineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.DocAdvPayAppld:int = obj["DocAdvPayAppld"]
      """  Amount of advance payment applied  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.MatchFiscalYearSuffix:str = obj["MatchFiscalYearSuffix"]
      """  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  """  
      self.MatchFiscalCalendarID:str = obj["MatchFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  The Supplier Shipment ID (also known as the ContainerID).  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Addition transaction.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Addition Number or sequence of the linked Asset Addition transaction.  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Used in a correction invoice to store reference to the original invoice line.  """  
      self.DocAssetInvoiceBal:int = obj["DocAssetInvoiceBal"]
      """  This is the current invoice line balance (in vendor currency) left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance of this DocAssetInvoiceBal.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  """  
      self.AssetBalOurQty:int = obj["AssetBalOurQty"]
      """  This is the Invoiced Quantity balance left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  This qty is expressed in our unit of measure.  """  
      self.AssetQtyIUM:str = obj["AssetQtyIUM"]
      """  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  The DMR Number that requires supplier credit.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  The Action Number for the DMR that requires supplier credit.  """  
      self.CreatedFromExpense:bool = obj["CreatedFromExpense"]
      """  Indicates if this invoice line was created from an EmpExpense record.  """  
      self.InUnitCost:int = obj["InUnitCost"]
      """  item's unit cost in the vendors unit of measure including taxes.  """  
      self.DocInUnitCost:int = obj["DocInUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency including taxes.  """  
      self.Rpt1InUnitCost:int = obj["Rpt1InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitCost:int = obj["Rpt2InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitCost:int = obj["Rpt3InUnitCost"]
      """  Reporting currency value of this field  """  
      self.InExtCost:int = obj["InExtCost"]
      """  Extended Cost for the invoice line item including taxes.  """  
      self.DocInExtCost:int = obj["DocInExtCost"]
      """   Extended Cost for the invoice line item in Vendors currency
including taxes  """  
      self.Rpt1InExtCost:int = obj["Rpt1InExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtCost:int = obj["Rpt2InExtCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtCost:int = obj["Rpt3InExtCost"]
      """  Reporting currency value of this field  """  
      self.InTotalMiscChrg:int = obj["InTotalMiscChrg"]
      """  Rolled up total of all misc. charge records for this invoice detail line including taxes.  """  
      self.DocInTotalMiscChrg:int = obj["DocInTotalMiscChrg"]
      """  Rolled up total of all misc. charge records for this invoice detail line in vendors currency including taxes.  """  
      self.Rpt1InTotalMiscChrg:int = obj["Rpt1InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2InTotalMiscChrg:int = obj["Rpt2InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3InTotalMiscChrg:int = obj["Rpt3InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.InAdvancePayAmt:int = obj["InAdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments (incl taxes).  """  
      self.DocInAdvancePayAmt:int = obj["DocInAdvancePayAmt"]
      """  The amount this line item that is reduced by due to prior advanced payments (incl taxes).  """  
      self.Rpt1InAdvancePayAmt:int = obj["Rpt1InAdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InAdvancePayAmt:int = obj["Rpt2InAdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InAdvancePayAmt:int = obj["Rpt3InAdvancePayAmt"]
      """  Reporting currency value of this field  """  
      self.InLineDiscAmt:int = obj["InLineDiscAmt"]
      """  Discount amount for this line including taxes  """  
      self.DocInLineDiscAmt:int = obj["DocInLineDiscAmt"]
      """  Discount amount (Vendors Currency) for this line including taxes  """  
      self.Rpt1InLineDiscAmt:int = obj["Rpt1InLineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InLineDiscAmt:int = obj["Rpt2InLineDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InLineDiscAmt:int = obj["Rpt3InLineDiscAmt"]
      self.NoTaxRecal:bool = obj["NoTaxRecal"]
      """  Indicates if no tax recalculation by the system is  supposed to be done since with "In Price" tax calculation the tax lines were adjusted or new tax lines added manually  """  
      self.DevInt1:int = obj["DevInt1"]
      """  Reserved for Development - Integer  """  
      self.DevInt2:int = obj["DevInt2"]
      """  Reserved for Development - Integer  """  
      self.DevDec1:int = obj["DevDec1"]
      """  Reserved for development - decimal  """  
      self.DevDec2:int = obj["DevDec2"]
      """  Reserved for development - decimal  """  
      self.DevDec3:int = obj["DevDec3"]
      """  Reserved for development - decimal  """  
      self.DevDec4:int = obj["DevDec4"]
      """  Reserved for development - decimal  """  
      self.DevLog1:bool = obj["DevLog1"]
      """  Reserved for development  - logical  """  
      self.DevLog2:bool = obj["DevLog2"]
      """  Reserved for development - logical  """  
      self.DevChar1:str = obj["DevChar1"]
      """  Reserved for development  - character  """  
      self.DevChar2:str = obj["DevChar2"]
      """  Reserved for development - character  """  
      self.DevDate1:str = obj["DevDate1"]
      """  Reserved for development - date  """  
      self.DevDate2:str = obj["DevDate2"]
      """  Reserved for development - date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ScrWithholdAmt:int = obj["ScrWithholdAmt"]
      """  Withholding Tax Amount  """  
      self.DocScrWithholdAmt:int = obj["DocScrWithholdAmt"]
      """  Withholding Tax Amount in document currency  """  
      self.Rpt1ScrWithholdAmt:int = obj["Rpt1ScrWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.Rpt2ScrWithholdAmt:int = obj["Rpt2ScrWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.Rpt3ScrWithholdAmt:int = obj["Rpt3ScrWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  Invoice Reference Number  """  
      self.APTranNo:int = obj["APTranNo"]
      """  AP Transaction Number  """  
      self.DocAdvPayAppliedAmt:int = obj["DocAdvPayAppliedAmt"]
      """  DocAdvPayAppliedAmt  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code, defaults from Supplier  """  
      self.Gen1099Code:str = obj["Gen1099Code"]
      """  Generated 1099 Code where this invoice was calculated in the 1099 Form  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DeferredExp:bool = obj["DeferredExp"]
      """  DeferredExp  """  
      self.DEACode:str = obj["DEACode"]
      """  DEACode  """  
      self.DEAAmt:int = obj["DEAAmt"]
      """  DEAAmt  """  
      self.DEAStartDate:str = obj["DEAStartDate"]
      """  DEAStartDate  """  
      self.DEAEndDate:str = obj["DEAEndDate"]
      """  DEAEndDate  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.ExternalPONum:str = obj["ExternalPONum"]
      """  This field is used to store the AVP Purchase Order Number.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  Malaysia Import Declaration Number  """  
      self.FinalInvoice:bool = obj["FinalInvoice"]
      """  Flag that indicates if the invoice is the final one for the last partial receipt.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax Amount  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax Amount  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Reporting currency value of this field  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Self-Assess Tax Amount  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Self-Assess Tax Amount  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Reporting currency value of this field  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total Deductible Tax Amount  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total Deductible Tax Amount  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Reporting currency value of this field  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  Project Billing Invoice Number  """  
      self.CancellationDtl:bool = obj["CancellationDtl"]
      """  Will be set to Yes if the AP Invoice Dtl was created by the Cancellation logic.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.TaxExemptReasonCode:str = obj["TaxExemptReasonCode"]
      """  TaxExemptReasonCode  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.AdjustmentValue:int = obj["AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.AllocationAmount:int = obj["AllocationAmount"]
      self.AllocationDesc:str = obj["AllocationDesc"]
      self.AllocationID:str = obj["AllocationID"]
      self.AllowGLDistAdd:bool = obj["AllowGLDistAdd"]
      self.AllowGLDistAllocation:bool = obj["AllowGLDistAllocation"]
      self.AllowGLDistDelete:bool = obj["AllowGLDistDelete"]
      self.AllowJobMiscAdd:bool = obj["AllowJobMiscAdd"]
      self.AllowJobMiscDelete:bool = obj["AllowJobMiscDelete"]
      self.AllowJobMiscUpdate:bool = obj["AllowJobMiscUpdate"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyID:str = obj["CurrencyID"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DEACodeDesc:str = obj["DEACodeDesc"]
      self.DEAScheduled:bool = obj["DEAScheduled"]
      """  Is Deferred Expense Amortization Scheduled  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      self.Distributed:int = obj["Distributed"]
      """  DEA Distributed Amount  """  
      self.DocAdjustmentValue:int = obj["DocAdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.DocAllocationAmount:int = obj["DocAllocationAmount"]
      self.DocDistributed:int = obj["DocDistributed"]
      """  DEA Distributed Amount in Doc Currency  """  
      self.DocDspLineTotal:int = obj["DocDspLineTotal"]
      self.DocExpense:int = obj["DocExpense"]
      """  DEA Expense Amount in Doc Currency  """  
      self.DocGLLineTotal:int = obj["DocGLLineTotal"]
      self.DocInTaxAmt:int = obj["DocInTaxAmt"]
      self.DocLineExpenses:int = obj["DocLineExpenses"]
      self.DocLineSubtotal:int = obj["DocLineSubtotal"]
      self.DocLineTotal:int = obj["DocLineTotal"]
      self.DocNonDeducTaxExpense:int = obj["DocNonDeducTaxExpense"]
      self.DocOrgExtCost:int = obj["DocOrgExtCost"]
      """  Value of original Ext Cost in document currency. Used for adjustment lines.  """  
      self.DocPEDetAmt:int = obj["DocPEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.DocRecognized:int = obj["DocRecognized"]
      """  DEA Recognized Amount in Doc Currency  """  
      self.DocRemaining:int = obj["DocRemaining"]
      """  DEA Remaining Amount in Doc Currency  """  
      self.DocScrInvoiceBal:int = obj["DocScrInvoiceBal"]
      self.DocScrTotalDedTax:int = obj["DocScrTotalDedTax"]
      self.DocScrTotalSATax:int = obj["DocScrTotalSATax"]
      self.DocScrTotalTax:int = obj["DocScrTotalTax"]
      self.DocScrUnitCost:int = obj["DocScrUnitCost"]
      self.DocTotDistribAmt:int = obj["DocTotDistribAmt"]
      """  This is the value of the lines that have been entered. In Document Currency  """  
      self.DocUnrecognized:int = obj["DocUnrecognized"]
      """  DEA Unrecognized Amount in Doc Currency  """  
      self.DocVariance:int = obj["DocVariance"]
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.DspAllocationAmount:int = obj["DspAllocationAmount"]
      self.DspLineTotal:int = obj["DspLineTotal"]
      self.EnableDiscountAmt:bool = obj["EnableDiscountAmt"]
      self.EnableIntrastat:bool = obj["EnableIntrastat"]
      """  Indicates if intrastat is available for the line.  """  
      self.EnableIntrastatDsp:bool = obj["EnableIntrastatDsp"]
      """  Indicates if intrastat is available for to be diplayed for the line. Used by AP invoice tracker  """  
      self.EnablePurchaseCode:bool = obj["EnablePurchaseCode"]
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Indicates if Override Reverse Charge check box should be enabled.  """  
      self.EnableScrWithholdAmt:bool = obj["EnableScrWithholdAmt"]
      self.EnableShipmentID:bool = obj["EnableShipmentID"]
      self.EnableSubCData:bool = obj["EnableSubCData"]
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.Expense:int = obj["Expense"]
      """  DEA Expense Amount  """  
      self.GLAccount:str = obj["GLAccount"]
      self.GLLineTotal:int = obj["GLLineTotal"]
      self.GridVenPartNum:str = obj["GridVenPartNum"]
      """  The VenPartNum field for the datagrid.  For display purposes only.  """  
      self.GroupID:str = obj["GroupID"]
      self.InPrice:bool = obj["InPrice"]
      self.InTaxAmt:int = obj["InTaxAmt"]
      self.IsAdvance:bool = obj["IsAdvance"]
      """  To determine if line have Advance Billing Line  """  
      self.JPTaxAdjustment:bool = obj["JPTaxAdjustment"]
      """  Japan Tax Adjustment Line  """  
      self.LineExpenses:int = obj["LineExpenses"]
      self.LineSubtotal:int = obj["LineSubtotal"]
      self.LineTotal:int = obj["LineTotal"]
      self.LineTypeDescription:str = obj["LineTypeDescription"]
      self.NonDeducTaxExpense:int = obj["NonDeducTaxExpense"]
      self.OrgExtCost:int = obj["OrgExtCost"]
      """  Value of original Ext Cost in base currency. Used for adjustment lines.  """  
      self.PEDetAmt:int = obj["PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.POCostPerCode:str = obj["POCostPerCode"]
      self.PODocUnitCost:int = obj["PODocUnitCost"]
      self.POLineDesc:str = obj["POLineDesc"]
      self.POPartNum:str = obj["POPartNum"]
      self.POPUM:str = obj["POPUM"]
      self.POReceivedQty:int = obj["POReceivedQty"]
      self.PORelIUM:str = obj["PORelIUM"]
      """  PO Rel Our UOM  """  
      self.PORelOurQty:int = obj["PORelOurQty"]
      """  PO Rel Our Quantity  """  
      self.PORelQty:int = obj["PORelQty"]
      self.Posted:bool = obj["Posted"]
      self.POUnitCost:int = obj["POUnitCost"]
      self.POVenPartNum:str = obj["POVenPartNum"]
      self.POWarn:str = obj["POWarn"]
      self.Print1099:bool = obj["Print1099"]
      """  Print 1099  """  
      self.RcptDestination:str = obj["RcptDestination"]
      self.RcptIUM:str = obj["RcptIUM"]
      """  Receipt Our UOM  """  
      self.RcptOurQty:int = obj["RcptOurQty"]
      """  Receipt Our Quantity  """  
      self.RcptPartDescription:str = obj["RcptPartDescription"]
      self.RcptPartNum:str = obj["RcptPartNum"]
      self.RcptPUM:str = obj["RcptPUM"]
      self.RcptReceiptDate:str = obj["RcptReceiptDate"]
      self.RcptVendorQty:int = obj["RcptVendorQty"]
      self.RcptVenPartNum:str = obj["RcptVenPartNum"]
      self.RecalcGLAcct:bool = obj["RecalcGLAcct"]
      self.Recognized:int = obj["Recognized"]
      """  DEA Recognized Amount  """  
      self.Remaining:int = obj["Remaining"]
      """  DEA Remaining Amount  """  
      self.RevChargeMethodDesc:str = obj["RevChargeMethodDesc"]
      """  Reverse Charge Method description  """  
      self.Rpt1AdjustmentValue:int = obj["Rpt1AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt1AllocationAmount:int = obj["Rpt1AllocationAmount"]
      self.Rpt1Distributed:int = obj["Rpt1Distributed"]
      """  DEA Distributed Amount in Rpt1 Currency  """  
      self.Rpt1DspLineTotal:int = obj["Rpt1DspLineTotal"]
      self.Rpt1Expense:int = obj["Rpt1Expense"]
      """  DEA Expense Amount in Rpt1 Currency  """  
      self.Rpt1GLLineTotal:int = obj["Rpt1GLLineTotal"]
      self.Rpt1InTaxAmt:int = obj["Rpt1InTaxAmt"]
      self.Rpt1LineExpenses:int = obj["Rpt1LineExpenses"]
      self.Rpt1LineSubTotal:int = obj["Rpt1LineSubTotal"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1NonDeducTaxExpense:int = obj["Rpt1NonDeducTaxExpense"]
      self.Rpt1OrgExtCost:int = obj["Rpt1OrgExtCost"]
      """  Value of original Ext Cost in reporting currency. Used for adjustment lines.  """  
      self.Rpt1PEDetAmt:int = obj["Rpt1PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt1POUnitCost:int = obj["Rpt1POUnitCost"]
      self.Rpt1Recognized:int = obj["Rpt1Recognized"]
      """  DEA Recognized Amount in Rpt1 Currency  """  
      self.Rpt1Remaining:int = obj["Rpt1Remaining"]
      """  DEA Remaining Amount in Rpt1 Currency  """  
      self.Rpt1ScrExtCost:int = obj["Rpt1ScrExtCost"]
      self.Rpt1ScrInvoiceBal:int = obj["Rpt1ScrInvoiceBal"]
      self.Rpt1ScrLineDiscAmt:int = obj["Rpt1ScrLineDiscAmt"]
      self.Rpt1ScrTotalDedTax:int = obj["Rpt1ScrTotalDedTax"]
      self.Rpt1ScrTotalMiscChrg:int = obj["Rpt1ScrTotalMiscChrg"]
      self.Rpt1ScrTotalSATax:int = obj["Rpt1ScrTotalSATax"]
      self.Rpt1ScrTotalTax:int = obj["Rpt1ScrTotalTax"]
      self.Rpt1ScrUnitCost:int = obj["Rpt1ScrUnitCost"]
      self.Rpt1TotDistribAmt:int = obj["Rpt1TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 1.  """  
      self.Rpt1Unrecognized:int = obj["Rpt1Unrecognized"]
      """  DEA Unrecognized Amount in Rpt1 Currency  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      self.Rpt2AdjustmentValue:int = obj["Rpt2AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt2AllocationAmount:int = obj["Rpt2AllocationAmount"]
      self.Rpt2Distributed:int = obj["Rpt2Distributed"]
      """  DEA Distributed Amount in Rpt2 Currency  """  
      self.Rpt2DspLineTotal:int = obj["Rpt2DspLineTotal"]
      self.Rpt2Expense:int = obj["Rpt2Expense"]
      """  DEA Expense Amount in Rpt2 Currency  """  
      self.Rpt2GLLineTotal:int = obj["Rpt2GLLineTotal"]
      self.Rpt2InTaxAmt:int = obj["Rpt2InTaxAmt"]
      self.Rpt2LineExpenses:int = obj["Rpt2LineExpenses"]
      self.Rpt2LineSubtotal:int = obj["Rpt2LineSubtotal"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2NonDeducTaxExpense:int = obj["Rpt2NonDeducTaxExpense"]
      self.Rpt2OrgExtCost:int = obj["Rpt2OrgExtCost"]
      """  Value of original Ext Cost in reporting currency. Used for adjustment lines.  """  
      self.Rpt2PEDetAmt:int = obj["Rpt2PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt2POUnitCost:int = obj["Rpt2POUnitCost"]
      self.Rpt2Recognized:int = obj["Rpt2Recognized"]
      """  DEA Recognized Amount in Rpt2 Currency  """  
      self.Rpt2Remaining:int = obj["Rpt2Remaining"]
      """  DEA Remaining Amount in Rpt2 Currency  """  
      self.Rpt2ScrExtCost:int = obj["Rpt2ScrExtCost"]
      self.Rpt2ScrInvoiceBal:int = obj["Rpt2ScrInvoiceBal"]
      self.Rpt2ScrLineDiscAmt:int = obj["Rpt2ScrLineDiscAmt"]
      self.Rpt2ScrTotalDedTax:int = obj["Rpt2ScrTotalDedTax"]
      self.Rpt2ScrTotalMiscChrg:int = obj["Rpt2ScrTotalMiscChrg"]
      self.Rpt2ScrTotalSATax:int = obj["Rpt2ScrTotalSATax"]
      self.Rpt2ScrTotalTax:int = obj["Rpt2ScrTotalTax"]
      self.Rpt2ScrUnitCost:int = obj["Rpt2ScrUnitCost"]
      self.Rpt2TotDistribAmt:int = obj["Rpt2TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 2.  """  
      self.Rpt2Unrecognized:int = obj["Rpt2Unrecognized"]
      """  DEA Unrecognized Amount in Rpt2 Currency  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      self.Rpt3AdjustmentValue:int = obj["Rpt3AdjustmentValue"]
      """  Fields to show difference in ExtCost between adjustment line and original line.  """  
      self.Rpt3AllocationAmount:int = obj["Rpt3AllocationAmount"]
      self.Rpt3Distributed:int = obj["Rpt3Distributed"]
      """  DEA Distributed Amount in Rpt3 Currency  """  
      self.Rpt3DspLineTotal:int = obj["Rpt3DspLineTotal"]
      self.Rpt3Expense:int = obj["Rpt3Expense"]
      """  DEA Expense Amount in Rpt3 Currency  """  
      self.Rpt3GLLineTotal:int = obj["Rpt3GLLineTotal"]
      self.Rpt3InTaxAmt:int = obj["Rpt3InTaxAmt"]
      self.Rpt3LineExpenses:int = obj["Rpt3LineExpenses"]
      self.Rpt3LineSubtotal:int = obj["Rpt3LineSubtotal"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3NonDeducTaxExpense:int = obj["Rpt3NonDeducTaxExpense"]
      self.Rpt3OrgExtCost:int = obj["Rpt3OrgExtCost"]
      """  Value of original Ext Cost in reporting currency. Used for adjustment lines.  """  
      self.Rpt3PEDetAmt:int = obj["Rpt3PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt3POUnitCost:int = obj["Rpt3POUnitCost"]
      self.Rpt3Recognized:int = obj["Rpt3Recognized"]
      """  DEA Recognized Amount in Rpt3 Currency  """  
      self.Rpt3Remaining:int = obj["Rpt3Remaining"]
      """  DEA Remaining Amount in Rpt3 Currency  """  
      self.Rpt3ScrExtCost:int = obj["Rpt3ScrExtCost"]
      self.Rpt3ScrInvoiceBal:int = obj["Rpt3ScrInvoiceBal"]
      self.Rpt3ScrLineDiscAmt:int = obj["Rpt3ScrLineDiscAmt"]
      self.Rpt3ScrTotalDedTax:int = obj["Rpt3ScrTotalDedTax"]
      self.Rpt3ScrTotalMiscChrg:int = obj["Rpt3ScrTotalMiscChrg"]
      self.Rpt3ScrTotalSATax:int = obj["Rpt3ScrTotalSATax"]
      self.Rpt3ScrTotalTax:int = obj["Rpt3ScrTotalTax"]
      self.Rpt3ScrUnitCost:int = obj["Rpt3ScrUnitCost"]
      self.Rpt3TotDistribAmt:int = obj["Rpt3TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Reportable currency 3.  """  
      self.Rpt3Unrecognized:int = obj["Rpt3Unrecognized"]
      """  DEA Unrecognized Amount in Rpt3 Currency  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      self.ScrDocExtCost:int = obj["ScrDocExtCost"]
      self.ScrDocLineDiscAmt:int = obj["ScrDocLineDiscAmt"]
      self.ScrDocTotalMiscChrg:int = obj["ScrDocTotalMiscChrg"]
      self.ScrExtCost:int = obj["ScrExtCost"]
      self.ScrInvoiceBal:int = obj["ScrInvoiceBal"]
      self.ScrInvoiceRef:str = obj["ScrInvoiceRef"]
      """  Invoice ref for BOE  """  
      self.ScrLineDiscAmt:int = obj["ScrLineDiscAmt"]
      self.ScrLineType:str = obj["ScrLineType"]
      self.ScrOurQty:int = obj["ScrOurQty"]
      self.ScrTotalDedTax:int = obj["ScrTotalDedTax"]
      self.ScrTotalMiscChrg:int = obj["ScrTotalMiscChrg"]
      self.ScrTotalSATax:int = obj["ScrTotalSATax"]
      self.ScrTotalTax:int = obj["ScrTotalTax"]
      self.ScrUnitCost:int = obj["ScrUnitCost"]
      self.ScrVendorQty:int = obj["ScrVendorQty"]
      self.TotDistribAmt:int = obj["TotDistribAmt"]
      """  This is the value of the lines that have been entered. In Base Currency  """  
      self.Unrecognized:int = obj["Unrecognized"]
      """  DEA Unrecognized Amount  """  
      self.UpdateExtCreateLineGL:bool = obj["UpdateExtCreateLineGL"]
      """  Indicates if line GL should be automatically created when running UpdateExt.  """  
      self.UsePurchaseCode:bool = obj["UsePurchaseCode"]
      self.Variance:int = obj["Variance"]
      self.UpdateExtOverrideRcpts:bool = obj["UpdateExtOverrideRcpts"]
      """  Indicates that  if LineType=R, then override standard UpdateExt logic to create APInvDtl data directly, as is done in the UI.  Before/AfterGetNew, Before/AfterUpdate will not run.  """  
      self.RelatedToRcvDtlSysRowID:str = obj["RelatedToRcvDtlSysRowID"]
      """  SysRowID of the related RcvDtl row for receipt line,  LineType = R  """  
      self.EnableAttributeSetBtn:bool = obj["EnableAttributeSetBtn"]
      self.DEPayStatCodeDescr:str = obj["DEPayStatCodeDescr"]
      """  DEPayStatCode Description  """  
      self.DEDenominationDescr:str = obj["DEDenominationDescr"]
      """  DEDenomination Description  """  
      self.PORevisionNum:str = obj["PORevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.RcptRevisionNum:str = obj["RcptRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.AssetNumAssetDescription:str = obj["AssetNumAssetDescription"]
      self.Code1099Description:str = obj["Code1099Description"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.ContainerIDContainerDescription:str = obj["ContainerIDContainerDescription"]
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      self.GLPurchPurchDesc:str = obj["GLPurchPurchDesc"]
      self.InvoiceNumDebitMemo:bool = obj["InvoiceNumDebitMemo"]
      self.InvoiceNumPosted:bool = obj["InvoiceNumPosted"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.InvoiceNumCurrencyCode:str = obj["InvoiceNumCurrencyCode"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorPPName:str = obj["VendorPPName"]
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvDtlSearchTableset:
   def __init__(self, obj):
      self.APInvDtl:list[Erp_Tablesets_APInvDtlRow] = obj["APInvDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtAPInvDtlSearchTableset:
   def __init__(self, obj):
      self.APInvDtl:list[Erp_Tablesets_APInvDtlRow] = obj["APInvDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   invoiceNum
   invoiceLine
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPInvDtl_input:
   """ Required : 
   ds
   vendorNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvDtlSearchTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class GetNewAPInvDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPInvDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPInvDtl:str = obj["whereClauseAPInvDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtAPInvDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPInvDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

