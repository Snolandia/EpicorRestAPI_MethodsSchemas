import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APInvSearchSvc
# Description: bo/APInvSearch/APInvSearch.p
           AP Invoice Search
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APInvSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APInvSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APInvSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/APInvSearches",headers=creds) as resp:
           return await resp.json()

async def post_APInvSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APInvSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APInvHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APInvHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/APInvSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APInvSearches_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APInvSearch item
   Description: Calls GetByID to retrieve the APInvSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/APInvSearches(" + Company + "," + VendorNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APInvSearches_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APInvSearch for the service
   Description: Calls UpdateExt to update APInvSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APInvSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APInvHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/APInvSearches(" + Company + "," + VendorNum + "," + InvoiceNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APInvSearches_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APInvSearch item
   Description: Call UpdateExt to delete APInvSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APInvSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/APInvSearches(" + Company + "," + VendorNum + "," + InvoiceNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPInvHed, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAPInvHed=" + whereClauseAPInvHed
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, invoiceNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceNum=" + invoiceNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPInvHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPInvHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPInvHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPInvHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPInvHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvHedRow] = obj["value"]
      pass

class Erp_Tablesets_APInvHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.CPay:bool = obj["CPay"]
      """  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  """  
      self.CPayInvoiceBal:int = obj["CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  """  
      self.CPayDocInvoiceBal:int = obj["CPayDocInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is pre-payment invoice.  """  
      self.APLOCID:str = obj["APLOCID"]
      """  Letter of Credit ID.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type ID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TWDeclareYear:int = obj["TWDeclareYear"]
      """  TWDeclareYear  """  
      self.TWDeclarePeriod:int = obj["TWDeclarePeriod"]
      """  TWDeclarePeriod  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type  """  
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      """  PLInvoiceReference  """  
      self.ScrInvoiceVendorAmt:int = obj["ScrInvoiceVendorAmt"]
      self.ScrDocInvoiceVendorAmt:int = obj["ScrDocInvoiceVendorAmt"]
      self.ScrInvoiceAmt:int = obj["ScrInvoiceAmt"]
      self.ScrDocInvoiceAmt:int = obj["ScrDocInvoiceAmt"]
      self.ScrInvoiceBal:int = obj["ScrInvoiceBal"]
      self.ScrDocInvoiceBal:int = obj["ScrDocInvoiceBal"]
      self.ScrUnpostedBal:int = obj["ScrUnpostedBal"]
      self.ScrDocUnpostedBal:int = obj["ScrDocUnpostedBal"]
      self.InvoiceVariance:int = obj["InvoiceVariance"]
      self.DocInvoiceVariance:int = obj["DocInvoiceVariance"]
      self.CPayOpenPayable:bool = obj["CPayOpenPayable"]
      """  Indicates if the CPay invoice is still an open payable at Corporate  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Supplier Name  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  Supplier ID  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.Rpt1ScrInvoiceAmt:int = obj["Rpt1ScrInvoiceAmt"]
      self.Rpt2ScrInvoiceAmt:int = obj["Rpt2ScrInvoiceAmt"]
      self.Rpt3ScrInvoiceAmt:int = obj["Rpt3ScrInvoiceAmt"]
      self.Rpt1InvoiceVariance:int = obj["Rpt1InvoiceVariance"]
      self.Rpt2InvoiceVariance:int = obj["Rpt2InvoiceVariance"]
      self.Rpt3InvoiceVariance:int = obj["Rpt3InvoiceVariance"]
      self.Rpt1ScrInvoiceVendorAmt:int = obj["Rpt1ScrInvoiceVendorAmt"]
      self.Rpt2ScrInvoiceVendorAmt:int = obj["Rpt2ScrInvoiceVendorAmt"]
      self.Rpt3ScrInvoiceVendorAmt:int = obj["Rpt3ScrInvoiceVendorAmt"]
      self.IsLcked:bool = obj["IsLcked"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      """  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.PayDates:str = obj["PayDates"]
      """  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayAmounts:str = obj["PayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.DocPayAmounts:str = obj["DocPayAmounts"]
      """  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  """  
      self.StartUp:bool = obj["StartUp"]
      """  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall invoice.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceVendorAmt:int = obj["DocInvoiceVendorAmt"]
      """  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.REFPONum:int = obj["REFPONum"]
      """  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal that invoice was posted to.  """  
      self.UpdateTax:bool = obj["UpdateTax"]
      """  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  """  
      self.InvoiceVendorAmt:int = obj["InvoiceVendorAmt"]
      """  For use by external G/L interfacing.  This field is sign flipped for debit memos.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identification of the Invoice.  """  
      self.FixedAmt:bool = obj["FixedAmt"]
      """  Allows user to control discount amount manually or automatically  """  
      self.XRefInvoiceNum:str = obj["XRefInvoiceNum"]
      """  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.DepGainLoss:int = obj["DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.CPay:bool = obj["CPay"]
      """  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  """  
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  """  
      self.CPayLegalNumber:str = obj["CPayLegalNumber"]
      """  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  """  
      self.CPayCheckNum:int = obj["CPayCheckNum"]
      """  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayCheckDate:str = obj["CPayCheckDate"]
      """  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayInvoiceBal:int = obj["CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  """  
      self.CPayDocInvoiceBal:int = obj["CPayDocInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlType:str = obj["GLControlType"]
      """  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceVendorAmt:int = obj["Rpt1InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceVendorAmt:int = obj["Rpt2InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceVendorAmt:int = obj["Rpt3InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayAmounts:str = obj["Rpt1PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayAmounts:str = obj["Rpt2PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayAmounts:str = obj["Rpt3PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnpostedBal:int = obj["Rpt1UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnpostedBal:int = obj["Rpt2UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnpostedBal:int = obj["Rpt3UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Rpt1CPayInvoiceBal:int = obj["Rpt1CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt2CPayInvoiceBal:int = obj["Rpt2CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt3CPayInvoiceBal:int = obj["Rpt3CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.AllowOverrideLI:bool = obj["AllowOverrideLI"]
      """  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  """  
      self.MatchedFromLI:bool = obj["MatchedFromLI"]
      """  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.PayDiscDays:str = obj["PayDiscDays"]
      """  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayDiscPer:str = obj["PayDiscPer"]
      """  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.PayDiscPartPay:bool = obj["PayDiscPartPay"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.PIPayment:str = obj["PIPayment"]
      """   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden and Finland Localization Field - Banking Reference  """  
      self.SEPayCode:str = obj["SEPayCode"]
      """  Sweden and Finland Localization Field - Payment Code  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is pre-payment invoice.  """  
      self.APLOCID:str = obj["APLOCID"]
      """  Letter of Credit ID.  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.GUIImportTaxBasis:int = obj["GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis  """  
      self.DocGUIImportTaxBasis:int = obj["DocGUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in document currrency  """  
      self.Rpt1GUIImportTaxBasis:int = obj["Rpt1GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt1 currency  """  
      self.Rpt2GUIImportTaxBasis:int = obj["Rpt2GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt2 currency  """  
      self.Rpt3GUIImportTaxBasis:int = obj["Rpt3GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt3 currency  """  
      self.OvrDefTaxDate:bool = obj["OvrDefTaxDate"]
      """  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked flag  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  The claim reference from the expense group that generated the invoice.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee from the group of expenses that created the invoice.  """  
      self.InBankFile:bool = obj["InBankFile"]
      """  Indicates that Invoice has been selected for payment in a bankfile  """  
      self.CNConfirmDate:str = obj["CNConfirmDate"]
      """  Credit Note Confirmation Date  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.SelfLegalNumber:str = obj["SelfLegalNumber"]
      """  Legal Number for the self assessment.  """  
      self.SelfTranDocTypeID:str = obj["SelfTranDocTypeID"]
      """  Transaction Document Type for the self assessment.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.SupAgentName:str = obj["SupAgentName"]
      """  Supplier Agent Name  """  
      self.SupAgentTaxRegNo:str = obj["SupAgentTaxRegNo"]
      """  Supplier Agent Tax Region Number  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.NonDeductVATAmt:int = obj["NonDeductVATAmt"]
      """  Non Deductable VAT Amount  """  
      self.NonDeductVATDocAmt:int = obj["NonDeductVATDocAmt"]
      """  Non Deductable VAT Doc Amount  """  
      self.NonDeductVATRpt1Amt:int = obj["NonDeductVATRpt1Amt"]
      """  Non Deductable VAT Rpt1 Amount  """  
      self.NonDeductVATRpt2Amt:int = obj["NonDeductVATRpt2Amt"]
      """  Non Deductable VAT Rpt2 Amount  """  
      self.NonDeductVATRpt3Amt:int = obj["NonDeductVATRpt3Amt"]
      """  Non Deductable VAT Rpt3 Amount  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.ImportedFrom:str = obj["ImportedFrom"]
      """  Country of Import  """  
      self.ImportedDate:str = obj["ImportedDate"]
      """  Date of import.  """  
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      """   Indicates that this is Advanced Tax invoice received from
supplier  """  
      self.InPrice:bool = obj["InPrice"]
      """   Indicates that the tax is included in the unit price
for this AP Invoice  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type ID  """  
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
      """  In case of Tax Inclusive Pricing if system-calculated Header related taxes are changed/deleted/added  by the user - this field is set to true by the system.  """  
      self.DevLog2:bool = obj["DevLog2"]
      """  Reserved for development - logical  """  
      self.DevChar1:str = obj["DevChar1"]
      """  Assigned as "I" when Recurring Invoice has Inactive status.  """  
      self.DevChar2:str = obj["DevChar2"]
      """  Reserved for development - character  """  
      self.DevDate1:str = obj["DevDate1"]
      """  Reserved for development - date  """  
      self.DevDate2:str = obj["DevDate2"]
      """  Reserved for development - date  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.CycleCode:str = obj["CycleCode"]
      """  CycleCode  """  
      self.Duration:int = obj["Duration"]
      """  Duration  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.MaxValueAmt:int = obj["MaxValueAmt"]
      """  MaxValueAmt  """  
      self.DocMaxValueAmt:int = obj["DocMaxValueAmt"]
      """  DocMaxValueAmt  """  
      self.Rpt1MaxValueAmt:int = obj["Rpt1MaxValueAmt"]
      """  Rpt1MaxValueAmt  """  
      self.Rpt2MaxValueAmt:int = obj["Rpt2MaxValueAmt"]
      """  Rpt2MaxValueAmt  """  
      self.Rpt3MaxValueAmt:int = obj["Rpt3MaxValueAmt"]
      """  Rpt3MaxValueAmt  """  
      self.HoldInvoice:bool = obj["HoldInvoice"]
      """  HoldInvoice  """  
      self.CopyLatestInvoice:bool = obj["CopyLatestInvoice"]
      """  CopyLatestInvoice  """  
      self.OverrideEndDate:bool = obj["OverrideEndDate"]
      """  OverrideEndDate  """  
      self.CycleInactive:bool = obj["CycleInactive"]
      """  CycleInactive  """  
      self.RecurSource:bool = obj["RecurSource"]
      """  RecurSource  """  
      self.InstanceNum:int = obj["InstanceNum"]
      """  InstanceNum  """  
      self.RecurBalance:int = obj["RecurBalance"]
      """  RecurBalance  """  
      self.DocRecurBalance:int = obj["DocRecurBalance"]
      """  DocRecurBalance  """  
      self.Rpt1RecurBalance:int = obj["Rpt1RecurBalance"]
      """  Rpt1RecurBalance  """  
      self.Rpt2RecurBalance:int = obj["Rpt2RecurBalance"]
      """  Rpt2RecurBalance  """  
      self.Rpt3RecurBalance:int = obj["Rpt3RecurBalance"]
      """  Rpt3RecurBalance  """  
      self.LastDate:str = obj["LastDate"]
      """  LastDate  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.InvoiceNumList:str = obj["InvoiceNumList"]
      """  InvoiceNumList  """  
      self.IsMaxValue:bool = obj["IsMaxValue"]
      """  IsMaxValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.DMReason:str = obj["DMReason"]
      """  DMReason  """  
      self.UrgentPayment:bool = obj["UrgentPayment"]
      """  UrgentPayment  """  
      self.AGDocPageNum:str = obj["AGDocPageNum"]
      """  AGDocPageNum  """  
      self.AGCAICAEMark:str = obj["AGCAICAEMark"]
      """  AGCAICAEMark  """  
      self.AGCAICAENum:str = obj["AGCAICAENum"]
      """  AGCAICAENum  """  
      self.AGCAICAEExpirationDate:str = obj["AGCAICAEExpirationDate"]
      """  AGCAICAEExpirationDate  """  
      self.AGAvTaxCreditFlag:bool = obj["AGAvTaxCreditFlag"]
      """  AGAvTaxCreditFlag  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGCustomsClearanceNum:str = obj["AGCustomsClearanceNum"]
      """  AGCustomsClearanceNum  """  
      self.AGCustomsCode:str = obj["AGCustomsCode"]
      """  AGCustomsCode  """  
      self.AGDestinationCode:str = obj["AGDestinationCode"]
      """  AGDestinationCode  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Header Number  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.TWDeclareYear:int = obj["TWDeclareYear"]
      """  TWDeclareYear  """  
      self.TWDeclarePeriod:int = obj["TWDeclarePeriod"]
      """  TWDeclarePeriod  """  
      self.APChkGrpID:str = obj["APChkGrpID"]
      """  AP Checking Group ID  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type  """  
      self.PEComputationalCost:str = obj["PEComputationalCost"]
      """  Indicates a computational cost for the invoice  """  
      self.ReferencedByBOE:str = obj["ReferencedByBOE"]
      """  Referenced By BOE  """  
      self.PEDUARefNum:str = obj["PEDUARefNum"]
      """  DUA Reference Number used on Peru Localiation  """  
      self.CustomsNumber:str = obj["CustomsNumber"]
      """  CustomsNumber  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  ReceivedDate  """  
      self.CustOverride:int = obj["CustOverride"]
      """  CustOverride  """  
      self.PrePaymentNum:str = obj["PrePaymentNum"]
      """  Invoice Number of Invoice Pre-Payment which should be automatically applied to this one during posting process.  """  
      self.PrePaymentAmt:int = obj["PrePaymentAmt"]
      """  Pre-Payment amount in Base Currency.  """  
      self.DocPrePaymentAmt:int = obj["DocPrePaymentAmt"]
      """  Pre-Payment amount in Document Currency.  """  
      self.Rpt1PrePaymentAmt:int = obj["Rpt1PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.Rpt2PrePaymentAmt:int = obj["Rpt2PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.Rpt3PrePaymentAmt:int = obj["Rpt3PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.PEAPPayNum:int = obj["PEAPPayNum"]
      """  CSF Peru - AP Payment Number  """  
      self.PEDetTaxAmt:int = obj["PEDetTaxAmt"]
      """  SCF Peru - Detractions Tax Amount  """  
      self.PEDetTaxCurrencyCode:str = obj["PEDetTaxCurrencyCode"]
      """  Peru Detraction Tax Currency Code  """  
      self.PESUNATDepAmt:int = obj["PESUNATDepAmt"]
      """  CSF Peru - SUNAT Deposit Amount  """  
      self.DocPESUNATDepAmt:int = obj["DocPESUNATDepAmt"]
      """  Peru Document SUNAT Deposit Amount  """  
      self.PESUNATDepDate:str = obj["PESUNATDepDate"]
      """  CSF Peru - SUNAT Deposit Date  """  
      self.PESUNATDepNum:str = obj["PESUNATDepNum"]
      """  CSF Peru -  SUNAT Deposit Number  """  
      self.PESUNATNum:str = obj["PESUNATNum"]
      """  SUNAT Reference Number. Once a payment is made, the SUNAT returns a reference number used as the receipt number for the payment.  """  
      self.DocPEDetTaxAmt:int = obj["DocPEDetTaxAmt"]
      """  Document Tax Amount used in Peru detractions  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.PEBOEIsMultiGen:bool = obj["PEBOEIsMultiGen"]
      """  PEBOEIsMultiGen  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.PrePayHeadNum:int = obj["PrePayHeadNum"]
      """  PrePayHeadNum  """  
      self.MXRetentionCode:str = obj["MXRetentionCode"]
      """  MXRetentionCode  """  
      self.PERefDocID:str = obj["PERefDocID"]
      """  PE Reference Document ID  """  
      self.PEReasonCode:str = obj["PEReasonCode"]
      """  PE Reason Code  """  
      self.PEReasonDesc:str = obj["PEReasonDesc"]
      """  PE Reason Description  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  Malaysia Import Declaration Number  """  
      self.TWGUIRegNumSeller:str = obj["TWGUIRegNumSeller"]
      """  TW GUI Code Seller  """  
      self.TWGUIRegNumBuyer:str = obj["TWGUIRegNumBuyer"]
      """  TW GUI Code Buyer  """  
      self.MXTARCode:str = obj["MXTARCode"]
      """  MXTARCode  """  
      self.GRNIClearing:bool = obj["GRNIClearing"]
      """  Flag that indicates if the invoice is a GRNI document.  """  
      self.PEFiscalCreditOperStatus:int = obj["PEFiscalCreditOperStatus"]
      """  CSF Peru - Fiscal Credit Operation Status  """  
      self.PEInternatTaxAgr:str = obj["PEInternatTaxAgr"]
      """  CSF Peru - International Tax agreement  """  
      self.PERentType:str = obj["PERentType"]
      """  CSF Peru - Rent type  """  
      self.PEPurchaseType:str = obj["PEPurchaseType"]
      """  CSF Peru - Purchase  type  """  
      self.THRefInvoiceNum:str = obj["THRefInvoiceNum"]
      """  TH Reference Invoice Num  """  
      self.THRefVendorNum:int = obj["THRefVendorNum"]
      """  TH Reference Vendor Num  """  
      self.JPSummarizationDate:str = obj["JPSummarizationDate"]
      """  Day when a company sums up accounts payable for supplier  """  
      self.JPBillingDate:str = obj["JPBillingDate"]
      """  Date of a Payment Statement  """  
      self.JPBillingNumber:str = obj["JPBillingNumber"]
      """  Legal Number of Payment Statement  """  
      self.SelfInvoice:bool = obj["SelfInvoice"]
      """  SelfInvoice  """  
      self.Printed:bool = obj["Printed"]
      """  Printed  """  
      self.PurPoint:str = obj["PurPoint"]
      """  PurPoint  """  
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      """  PLInvoiceReference  """  
      self.INPortCode:str = obj["INPortCode"]
      """  INPortCode  """  
      self.RefCancelledby:str = obj["RefCancelledby"]
      """  Indicates which invoice number has cancelled this invoice.  """  
      self.CancellationInv:bool = obj["CancellationInv"]
      """  Indicates if this invoice is a cancellation invoice.  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.WithholdAcctToInterim:bool = obj["WithholdAcctToInterim"]
      """  WithholdAcctToInterim  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  Source Plant used for multi site GL  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.CHQRIBAN:str = obj["CHQRIBAN"]
      """  CHQRIBAN  """  
      self.CHQRReference:str = obj["CHQRReference"]
      """  CHQRReference  """  
      self.EDIInvoice:bool = obj["EDIInvoice"]
      """  Set to True for any invoice that is created via EDI  """  
      self.AllowMultInvcReceipts:bool = obj["AllowMultInvcReceipts"]
      """  This external field will hold Company.AllowMultInvcReceipts flag.  """  
      self.ApplyAPPrePayAuto:bool = obj["ApplyAPPrePayAuto"]
      """  Apply AP Pre Payment Automatically.  """  
      self.BankName:str = obj["BankName"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  The base currency symbol  """  
      self.BillAddressList:str = obj["BillAddressList"]
      """  The bill address in list format  """  
      self.CanChangeTaxLiab:bool = obj["CanChangeTaxLiab"]
      self.COIFRSCalculation:bool = obj["COIFRSCalculation"]
      """  IFRS Calculation. If the checkbox is not checked then all the elements below are disabled. If the checkbox is checked, then some elements below become enabled showing default values so that the NPV can be calculated  """  
      self.COIFRSEnabled:bool = obj["COIFRSEnabled"]
      """  If true then Colombia IFRS Net Present Value calculation is enabled  """  
      self.COIFRSFinancialCharge:int = obj["COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.COIFRSInterestRate:int = obj["COIFRSInterestRate"]
      self.COIFRSNumberOfPeriods:int = obj["COIFRSNumberOfPeriods"]
      """  Number of Periods for payment  """  
      self.COIFRSPresentValue:int = obj["COIFRSPresentValue"]
      """  Present Value  """  
      self.CPayIMReceived:bool = obj["CPayIMReceived"]
      """  Flag to indicate if the CPay invoice has been received/trasferred to the corporate.  """  
      self.CPayOpenPayable:bool = obj["CPayOpenPayable"]
      """  Indicates if the CPay invoice is still an open payable at Corporate  """  
      self.CumulativeBalance:int = obj["CumulativeBalance"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrInstanceNum:int = obj["CurrInstanceNum"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  The document currency symbol  """  
      self.DisableAplDate:bool = obj["DisableAplDate"]
      """   The flag to indicate if Invoice Header Apply Date is supposed to be Read Only
(There are any detail/misc lines and not DMR Debit Memo invoice)  """  
      self.DocCOIFRSFinancialCharge:int = obj["DocCOIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.DocCOIFRSPresentValue:int = obj["DocCOIFRSPresentValue"]
      """  Present Value  """  
      self.DocCumulativeBalance:int = obj["DocCumulativeBalance"]
      self.DocInvoiceVariance:int = obj["DocInvoiceVariance"]
      """  The doc invoice variance amount  """  
      self.DocMiscChrgNonDeducTax:int = obj["DocMiscChrgNonDeducTax"]
      self.DocMiscChrgVariance:int = obj["DocMiscChrgVariance"]
      self.DocScrHdrExpTotal:int = obj["DocScrHdrExpTotal"]
      self.DocSourceRecurBalance:int = obj["DocSourceRecurBalance"]
      self.DspGuiImportTaxBasis:int = obj["DspGuiImportTaxBasis"]
      """   Taiwan Localization           
Display Field for Gui Import Tax Basis  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableCPay:bool = obj["EnableCPay"]
      """  Indicates when to enable the CPay field.  """  
      self.EnableDueDate:bool = obj["EnableDueDate"]
      self.EnableExchangeRate:bool = obj["EnableExchangeRate"]
      self.EnableLockRate:bool = obj["EnableLockRate"]
      self.EnableTaxExRate:bool = obj["EnableTaxExRate"]
      self.EnableTaxLock:bool = obj["EnableTaxLock"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Enable setting of Transaction Document Type  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.ExchangeRateDate:str = obj["ExchangeRateDate"]
      """  Indicates which date to be used to calculate the exchange rate, I for Invoice Date, A for Apply Date.  """  
      self.GuiTaxBasisFlag:bool = obj["GuiTaxBasisFlag"]
      """   Taiwan Localization           
The flag to indicate if GUITaxBasis prompt is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code  """  
      self.InvoiceTypeDesc:str = obj["InvoiceTypeDesc"]
      """  for Bill of Exchange  """  
      self.InvoiceVariance:int = obj["InvoiceVariance"]
      """  The invoice variance amount  """  
      self.IsLatestRecurrence:bool = obj["IsLatestRecurrence"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.IsOnlyMiscRecords:bool = obj["IsOnlyMiscRecords"]
      """  Is Only Misc lines exits  """  
      self.LACTaxCalcEnabled:bool = obj["LACTaxCalcEnabled"]
      """  LAC Tax Calculation Enabled  """  
      self.LatestInvoice:int = obj["LatestInvoice"]
      self.LatestInvString:str = obj["LatestInvString"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.LineOrMscChrgExists:bool = obj["LineOrMscChrgExists"]
      """  Indicates if lines or misc charges exist for the invoice  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.MiscChrgNonDeducTax:int = obj["MiscChrgNonDeducTax"]
      self.MiscChrgVariance:int = obj["MiscChrgVariance"]
      self.NextInvoiceDate:str = obj["NextInvoiceDate"]
      """  NextInvoiceDate = InvcRecurringCycle.LastDate + RecurringCycle.Interval in RecurringCycle.Modifier units  """  
      self.NoChangeRecur:bool = obj["NoChangeRecur"]
      self.PayMethod:str = obj["PayMethod"]
      """  Pay Method Type  """  
      self.PEFiscalCreditOperStatusDsp:str = obj["PEFiscalCreditOperStatusDsp"]
      """  CSF Peru - Fiscal Credit Operation Status  """  
      self.PEIsNRInvc:bool = obj["PEIsNRInvc"]
      """  Peru Localization Field, Field to disable Non-Resident Inovices Fields.  """  
      self.PLVendorAutoInvoiceNum:bool = obj["PLVendorAutoInvoiceNum"]
      """  CSF Poland. Vendor uses Invoice reference number  """  
      self.PostInvtyWipCos:bool = obj["PostInvtyWipCos"]
      self.RecalcAmts:str = obj["RecalcAmts"]
      """   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  """  
      self.Recurring:bool = obj["Recurring"]
      """  Recurring Source flag  """  
      self.RecurringState:str = obj["RecurringState"]
      self.Rpt1COIFRSFinancialCharge:int = obj["Rpt1COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt1COIFRSPresentValue:int = obj["Rpt1COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt1CumulativeBalance:int = obj["Rpt1CumulativeBalance"]
      self.Rpt1InvoiceVariance:int = obj["Rpt1InvoiceVariance"]
      self.Rpt1MiscChrgNonDeducTax:int = obj["Rpt1MiscChrgNonDeducTax"]
      self.Rpt1MiscChrgVariance:int = obj["Rpt1MiscChrgVariance"]
      self.Rpt1ScrDiscountAmt:int = obj["Rpt1ScrDiscountAmt"]
      self.Rpt1ScrHdrExpTotal:int = obj["Rpt1ScrHdrExpTotal"]
      self.Rpt1ScrHdrMiscChrgTotal:int = obj["Rpt1ScrHdrMiscChrgTotal"]
      self.Rpt1ScrInvLineTotal:int = obj["Rpt1ScrInvLineTotal"]
      self.Rpt1ScrInvoiceAmt:int = obj["Rpt1ScrInvoiceAmt"]
      self.Rpt1ScrInvoiceBal:int = obj["Rpt1ScrInvoiceBal"]
      self.Rpt1ScrInvoiceVendorAmt:int = obj["Rpt1ScrInvoiceVendorAmt"]
      self.Rpt1ScrLACTaxAmt:int = obj["Rpt1ScrLACTaxAmt"]
      """  Rpt1 Scr LAC Tax Amt  """  
      self.Rpt1ScrRounding:int = obj["Rpt1ScrRounding"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTotBOEWithholding:int = obj["Rpt1ScrTotBOEWithholding"]
      self.Rpt1ScrTotDedTaxAmt:int = obj["Rpt1ScrTotDedTaxAmt"]
      self.Rpt1ScrTotInvoiceAmt:int = obj["Rpt1ScrTotInvoiceAmt"]
      self.Rpt1ScrTotReportableAmt:int = obj["Rpt1ScrTotReportableAmt"]
      self.Rpt1ScrTotSelfAmt:int = obj["Rpt1ScrTotSelfAmt"]
      self.Rpt1ScrTotTaxableAmt:int = obj["Rpt1ScrTotTaxableAmt"]
      self.Rpt1ScrTotWithholdingAmt:int = obj["Rpt1ScrTotWithholdingAmt"]
      self.Rpt1ScrUnpostedBal:int = obj["Rpt1ScrUnpostedBal"]
      self.Rpt1SourceRecurBalance:int = obj["Rpt1SourceRecurBalance"]
      self.Rpt2COIFRSFinancialCharge:int = obj["Rpt2COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt2COIFRSPresentValue:int = obj["Rpt2COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt2CumulativeBalance:int = obj["Rpt2CumulativeBalance"]
      self.Rpt2InvoiceVariance:int = obj["Rpt2InvoiceVariance"]
      self.Rpt2MiscChrgNonDeducTax:int = obj["Rpt2MiscChrgNonDeducTax"]
      self.Rpt2MiscChrgVariance:int = obj["Rpt2MiscChrgVariance"]
      self.Rpt2ScrDiscountAmt:int = obj["Rpt2ScrDiscountAmt"]
      self.Rpt2ScrHdrExpTotal:int = obj["Rpt2ScrHdrExpTotal"]
      self.Rpt2ScrHdrMiscChrgTotal:int = obj["Rpt2ScrHdrMiscChrgTotal"]
      self.Rpt2ScrInvLineTotal:int = obj["Rpt2ScrInvLineTotal"]
      self.Rpt2ScrInvoiceAmt:int = obj["Rpt2ScrInvoiceAmt"]
      self.Rpt2ScrInvoiceBal:int = obj["Rpt2ScrInvoiceBal"]
      self.Rpt2ScrInvoiceVendorAmt:int = obj["Rpt2ScrInvoiceVendorAmt"]
      self.Rpt2ScrLACTaxAmt:int = obj["Rpt2ScrLACTaxAmt"]
      """  Rpt2 Scr LAC Tax Amt  """  
      self.Rpt2ScrRounding:int = obj["Rpt2ScrRounding"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTotBOEWithholding:int = obj["Rpt2ScrTotBOEWithholding"]
      self.Rpt2ScrTotDedTaxAmt:int = obj["Rpt2ScrTotDedTaxAmt"]
      self.Rpt2ScrTotInvoiceAmt:int = obj["Rpt2ScrTotInvoiceAmt"]
      self.Rpt2ScrTotReportableAmt:int = obj["Rpt2ScrTotReportableAmt"]
      self.Rpt2ScrTotSelfAmt:int = obj["Rpt2ScrTotSelfAmt"]
      self.Rpt2ScrTotTaxableAmt:int = obj["Rpt2ScrTotTaxableAmt"]
      self.Rpt2ScrTotWithholdingAmt:int = obj["Rpt2ScrTotWithholdingAmt"]
      self.Rpt2ScrUnpostedBal:int = obj["Rpt2ScrUnpostedBal"]
      self.Rpt2SourceRecurBalance:int = obj["Rpt2SourceRecurBalance"]
      self.Rpt3COIFRSFinancialCharge:int = obj["Rpt3COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt3COIFRSPresentValue:int = obj["Rpt3COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt3CumulativeBalance:int = obj["Rpt3CumulativeBalance"]
      self.Rpt3InvoiceVariance:int = obj["Rpt3InvoiceVariance"]
      self.Rpt3MiscChrgNonDeducTax:int = obj["Rpt3MiscChrgNonDeducTax"]
      self.Rpt3MiscChrgVariance:int = obj["Rpt3MiscChrgVariance"]
      self.Rpt3ScrDiscountAmt:int = obj["Rpt3ScrDiscountAmt"]
      self.Rpt3ScrHdrExpTotal:int = obj["Rpt3ScrHdrExpTotal"]
      self.Rpt3ScrHdrMiscChrgTotal:int = obj["Rpt3ScrHdrMiscChrgTotal"]
      self.Rpt3ScrInvLineTotal:int = obj["Rpt3ScrInvLineTotal"]
      self.Rpt3ScrInvoiceAmt:int = obj["Rpt3ScrInvoiceAmt"]
      self.Rpt3ScrInvoiceBal:int = obj["Rpt3ScrInvoiceBal"]
      self.Rpt3ScrInvoiceVendorAmt:int = obj["Rpt3ScrInvoiceVendorAmt"]
      self.Rpt3ScrLACTaxAmt:int = obj["Rpt3ScrLACTaxAmt"]
      """  Rpt3 Scr LAC Tax Amt  """  
      self.Rpt3ScrRounding:int = obj["Rpt3ScrRounding"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTotBOEWithholding:int = obj["Rpt3ScrTotBOEWithholding"]
      self.Rpt3ScrTotDedTaxAmt:int = obj["Rpt3ScrTotDedTaxAmt"]
      self.Rpt3ScrTotInvoiceAmt:int = obj["Rpt3ScrTotInvoiceAmt"]
      self.Rpt3ScrTotReportableAmt:int = obj["Rpt3ScrTotReportableAmt"]
      self.Rpt3ScrTotSelfAmt:int = obj["Rpt3ScrTotSelfAmt"]
      self.Rpt3ScrTotTaxableAmt:int = obj["Rpt3ScrTotTaxableAmt"]
      self.Rpt3ScrTotWithholdingAmt:int = obj["Rpt3ScrTotWithholdingAmt"]
      self.Rpt3ScrUnpostedBal:int = obj["Rpt3ScrUnpostedBal"]
      self.Rpt3SourceRecurBalance:int = obj["Rpt3SourceRecurBalance"]
      self.RptScrTotWithholdingAmt:int = obj["RptScrTotWithholdingAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.ScrDiscountAmt:int = obj["ScrDiscountAmt"]
      self.ScrDocDiscountAmt:int = obj["ScrDocDiscountAmt"]
      self.ScrDocHdrMiscChrgTotal:int = obj["ScrDocHdrMiscChrgTotal"]
      self.ScrDocInvLineTotal:int = obj["ScrDocInvLineTotal"]
      self.ScrDocInvoiceAmt:int = obj["ScrDocInvoiceAmt"]
      self.ScrDocInvoiceBal:int = obj["ScrDocInvoiceBal"]
      self.ScrDocInvoiceVendorAmt:int = obj["ScrDocInvoiceVendorAmt"]
      self.ScrDocRounding:int = obj["ScrDocRounding"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocTotBOEWithholding:int = obj["ScrDocTotBOEWithholding"]
      self.ScrDocTotDedTaxAmt:int = obj["ScrDocTotDedTaxAmt"]
      self.ScrDocTotInvoiceAmt:int = obj["ScrDocTotInvoiceAmt"]
      self.ScrDocTotReportableAmt:int = obj["ScrDocTotReportableAmt"]
      self.ScrDocTotSelfAmt:int = obj["ScrDocTotSelfAmt"]
      self.ScrDocTotTaxableAmt:int = obj["ScrDocTotTaxableAmt"]
      self.ScrDocTotWithholdingAmt:int = obj["ScrDocTotWithholdingAmt"]
      self.ScrDocUnpostedBal:int = obj["ScrDocUnpostedBal"]
      self.ScrHdrExpTotal:int = obj["ScrHdrExpTotal"]
      self.ScrHdrMiscChrgTotal:int = obj["ScrHdrMiscChrgTotal"]
      self.ScrInvLineTotal:int = obj["ScrInvLineTotal"]
      self.ScrInvoiceAmt:int = obj["ScrInvoiceAmt"]
      self.ScrInvoiceBal:int = obj["ScrInvoiceBal"]
      self.ScrInvoiceRef:str = obj["ScrInvoiceRef"]
      self.ScrInvoiceVendorAmt:int = obj["ScrInvoiceVendorAmt"]
      self.ScrLACDocTaxAmt:int = obj["ScrLACDocTaxAmt"]
      """  Scr LAC Doc Tax Amt  """  
      self.ScrLACTaxAmt:int = obj["ScrLACTaxAmt"]
      """  Scr LAC Tax Amt  """  
      self.ScrRounding:int = obj["ScrRounding"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      """  The screen tax amount  """  
      self.ScrTotBOEWithholding:int = obj["ScrTotBOEWithholding"]
      """  Total of withholdings of all BOE Lines.  """  
      self.ScrTotDedTaxAmt:int = obj["ScrTotDedTaxAmt"]
      self.ScrTotInvoiceAmt:int = obj["ScrTotInvoiceAmt"]
      """  Shall be the sum of column 'Tax Amount' for all lines with collection method 'Invoice'  """  
      self.ScrTotReportableAmt:int = obj["ScrTotReportableAmt"]
      self.ScrTotSelfAmt:int = obj["ScrTotSelfAmt"]
      """  shall be the sum of column 'Tax Amount' for all lines with collection method 'Self-Assessed' or mehtod 'Self-Assessed'  """  
      self.ScrTotTaxableAmt:int = obj["ScrTotTaxableAmt"]
      self.ScrTotWithholdingAmt:int = obj["ScrTotWithholdingAmt"]
      """  shall be the sum of column 'Tax Amount' for all lines with collection  method 'Withholding'  """  
      self.ScrUnpostedBal:int = obj["ScrUnpostedBal"]
      self.SkipRecurring:bool = obj["SkipRecurring"]
      self.SourceInvoiceNum:str = obj["SourceInvoiceNum"]
      """  Recurrent Invoices functionality  """  
      self.SourceLastDate:str = obj["SourceLastDate"]
      self.SourceRecurBalance:int = obj["SourceRecurBalance"]
      self.SwiftCode:str = obj["SwiftCode"]
      """  Swift Code  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  System Transaction Type: APInvoice/DebitMemo  is used in the filter of TranDocType combo-box.  """  
      self.TaxExchangeRate:int = obj["TaxExchangeRate"]
      self.TaxLinesExist:bool = obj["TaxLinesExist"]
      self.TaxRateLinesExist:bool = obj["TaxRateLinesExist"]
      self.TotalInstanceNum:int = obj["TotalInstanceNum"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Link to TranDocType table, can be removed when path filed TranDocTypeID is replaced with actual one.  """  
      self.TransApplyDate:str = obj["TransApplyDate"]
      """  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  """  
      self.UseTaxRate:bool = obj["UseTaxRate"]
      self.VendorInactive:bool = obj["VendorInactive"]
      """  Indicates if the vendor on the invoice is active or not.  """  
      self.VendorPayHold:bool = obj["VendorPayHold"]
      """  Indicates if the vendor on the invoice is in a pay hold state.  """  
      self.VNDateReceived:str = obj["VNDateReceived"]
      self.VNInvoiceType:str = obj["VNInvoiceType"]
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.FormattedVendorNameAddress:str = obj["FormattedVendorNameAddress"]
      """  Formatted Supplier Name and Address  """  
      self.SiteIsLegalEntity:bool = obj["SiteIsLegalEntity"]
      """  Site is a LegalEntity  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGCustomsDescription:str = obj["AGCustomsDescription"]
      self.AGDestinationDescription:str = obj["AGDestinationDescription"]
      self.APInvRecurringCycleInactive:bool = obj["APInvRecurringCycleInactive"]
      self.APInvRecurringCycleDescription:str = obj["APInvRecurringCycleDescription"]
      self.APLOCIDDescription:str = obj["APLOCIDDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.SourcePlantName:str = obj["SourcePlantName"]
      self.TaxRateGrpDescription:str = obj["TaxRateGrpDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.TermsCodeTermsType:str = obj["TermsCodeTermsType"]
      self.THRefVendorNumName:str = obj["THRefVendorNumName"]
      self.THRefVendorNumVendorID:str = obj["THRefVendorNumVendorID"]
      self.VendBankPMUID:int = obj["VendBankPMUID"]
      self.VendBankCardCode:str = obj["VendBankCardCode"]
      self.VendBankBankAcctNumber:str = obj["VendBankBankAcctNumber"]
      self.VendBankIBANCode:str = obj["VendBankIBANCode"]
      self.VendBankBankGiroAcctNbr:str = obj["VendBankBankGiroAcctNbr"]
      self.VendBankSwiftNum:str = obj["VendBankSwiftNum"]
      self.VendBankLocalBIC:str = obj["VendBankLocalBIC"]
      self.VendBankBankName:str = obj["VendBankBankName"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.XbSystAPTaxLnLevel:bool = obj["XbSystAPTaxLnLevel"]
      self.XbSystIsDiscountforDebitM:bool = obj["XbSystIsDiscountforDebitM"]
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
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_APInvHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.CPay:bool = obj["CPay"]
      """  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  """  
      self.CPayInvoiceBal:int = obj["CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  """  
      self.CPayDocInvoiceBal:int = obj["CPayDocInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is pre-payment invoice.  """  
      self.APLOCID:str = obj["APLOCID"]
      """  Letter of Credit ID.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type ID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TWDeclareYear:int = obj["TWDeclareYear"]
      """  TWDeclareYear  """  
      self.TWDeclarePeriod:int = obj["TWDeclarePeriod"]
      """  TWDeclarePeriod  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type  """  
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      """  PLInvoiceReference  """  
      self.ScrInvoiceVendorAmt:int = obj["ScrInvoiceVendorAmt"]
      self.ScrDocInvoiceVendorAmt:int = obj["ScrDocInvoiceVendorAmt"]
      self.ScrInvoiceAmt:int = obj["ScrInvoiceAmt"]
      self.ScrDocInvoiceAmt:int = obj["ScrDocInvoiceAmt"]
      self.ScrInvoiceBal:int = obj["ScrInvoiceBal"]
      self.ScrDocInvoiceBal:int = obj["ScrDocInvoiceBal"]
      self.ScrUnpostedBal:int = obj["ScrUnpostedBal"]
      self.ScrDocUnpostedBal:int = obj["ScrDocUnpostedBal"]
      self.InvoiceVariance:int = obj["InvoiceVariance"]
      self.DocInvoiceVariance:int = obj["DocInvoiceVariance"]
      self.CPayOpenPayable:bool = obj["CPayOpenPayable"]
      """  Indicates if the CPay invoice is still an open payable at Corporate  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Supplier Name  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  Supplier ID  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.Rpt1ScrInvoiceAmt:int = obj["Rpt1ScrInvoiceAmt"]
      self.Rpt2ScrInvoiceAmt:int = obj["Rpt2ScrInvoiceAmt"]
      self.Rpt3ScrInvoiceAmt:int = obj["Rpt3ScrInvoiceAmt"]
      self.Rpt1InvoiceVariance:int = obj["Rpt1InvoiceVariance"]
      self.Rpt2InvoiceVariance:int = obj["Rpt2InvoiceVariance"]
      self.Rpt3InvoiceVariance:int = obj["Rpt3InvoiceVariance"]
      self.Rpt1ScrInvoiceVendorAmt:int = obj["Rpt1ScrInvoiceVendorAmt"]
      self.Rpt2ScrInvoiceVendorAmt:int = obj["Rpt2ScrInvoiceVendorAmt"]
      self.Rpt3ScrInvoiceVendorAmt:int = obj["Rpt3ScrInvoiceVendorAmt"]
      self.IsLcked:bool = obj["IsLcked"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvHedListTableset:
   def __init__(self, obj):
      self.APInvHedList:list[Erp_Tablesets_APInvHedListRow] = obj["APInvHedList"]
      self.APInvHedTransferList:list[Erp_Tablesets_APInvHedTransferListRow] = obj["APInvHedTransferList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APInvHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      """  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.PayDates:str = obj["PayDates"]
      """  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayAmounts:str = obj["PayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.DocPayAmounts:str = obj["DocPayAmounts"]
      """  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  """  
      self.StartUp:bool = obj["StartUp"]
      """  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall invoice.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceVendorAmt:int = obj["DocInvoiceVendorAmt"]
      """  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.REFPONum:int = obj["REFPONum"]
      """  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal that invoice was posted to.  """  
      self.UpdateTax:bool = obj["UpdateTax"]
      """  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  """  
      self.InvoiceVendorAmt:int = obj["InvoiceVendorAmt"]
      """  For use by external G/L interfacing.  This field is sign flipped for debit memos.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identification of the Invoice.  """  
      self.FixedAmt:bool = obj["FixedAmt"]
      """  Allows user to control discount amount manually or automatically  """  
      self.XRefInvoiceNum:str = obj["XRefInvoiceNum"]
      """  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.DepGainLoss:int = obj["DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.CPay:bool = obj["CPay"]
      """  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  """  
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  """  
      self.CPayLegalNumber:str = obj["CPayLegalNumber"]
      """  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  """  
      self.CPayCheckNum:int = obj["CPayCheckNum"]
      """  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayCheckDate:str = obj["CPayCheckDate"]
      """  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayInvoiceBal:int = obj["CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  """  
      self.CPayDocInvoiceBal:int = obj["CPayDocInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlType:str = obj["GLControlType"]
      """  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceVendorAmt:int = obj["Rpt1InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceVendorAmt:int = obj["Rpt2InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceVendorAmt:int = obj["Rpt3InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayAmounts:str = obj["Rpt1PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayAmounts:str = obj["Rpt2PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayAmounts:str = obj["Rpt3PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnpostedBal:int = obj["Rpt1UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnpostedBal:int = obj["Rpt2UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnpostedBal:int = obj["Rpt3UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Rpt1CPayInvoiceBal:int = obj["Rpt1CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt2CPayInvoiceBal:int = obj["Rpt2CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt3CPayInvoiceBal:int = obj["Rpt3CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.AllowOverrideLI:bool = obj["AllowOverrideLI"]
      """  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  """  
      self.MatchedFromLI:bool = obj["MatchedFromLI"]
      """  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.PayDiscDays:str = obj["PayDiscDays"]
      """  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayDiscPer:str = obj["PayDiscPer"]
      """  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.PayDiscPartPay:bool = obj["PayDiscPartPay"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.PIPayment:str = obj["PIPayment"]
      """   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden and Finland Localization Field - Banking Reference  """  
      self.SEPayCode:str = obj["SEPayCode"]
      """  Sweden and Finland Localization Field - Payment Code  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is pre-payment invoice.  """  
      self.APLOCID:str = obj["APLOCID"]
      """  Letter of Credit ID.  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.GUIImportTaxBasis:int = obj["GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis  """  
      self.DocGUIImportTaxBasis:int = obj["DocGUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in document currrency  """  
      self.Rpt1GUIImportTaxBasis:int = obj["Rpt1GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt1 currency  """  
      self.Rpt2GUIImportTaxBasis:int = obj["Rpt2GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt2 currency  """  
      self.Rpt3GUIImportTaxBasis:int = obj["Rpt3GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt3 currency  """  
      self.OvrDefTaxDate:bool = obj["OvrDefTaxDate"]
      """  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked flag  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  The claim reference from the expense group that generated the invoice.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee from the group of expenses that created the invoice.  """  
      self.InBankFile:bool = obj["InBankFile"]
      """  Indicates that Invoice has been selected for payment in a bankfile  """  
      self.CNConfirmDate:str = obj["CNConfirmDate"]
      """  Credit Note Confirmation Date  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.SelfLegalNumber:str = obj["SelfLegalNumber"]
      """  Legal Number for the self assessment.  """  
      self.SelfTranDocTypeID:str = obj["SelfTranDocTypeID"]
      """  Transaction Document Type for the self assessment.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.SupAgentName:str = obj["SupAgentName"]
      """  Supplier Agent Name  """  
      self.SupAgentTaxRegNo:str = obj["SupAgentTaxRegNo"]
      """  Supplier Agent Tax Region Number  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.NonDeductVATAmt:int = obj["NonDeductVATAmt"]
      """  Non Deductable VAT Amount  """  
      self.NonDeductVATDocAmt:int = obj["NonDeductVATDocAmt"]
      """  Non Deductable VAT Doc Amount  """  
      self.NonDeductVATRpt1Amt:int = obj["NonDeductVATRpt1Amt"]
      """  Non Deductable VAT Rpt1 Amount  """  
      self.NonDeductVATRpt2Amt:int = obj["NonDeductVATRpt2Amt"]
      """  Non Deductable VAT Rpt2 Amount  """  
      self.NonDeductVATRpt3Amt:int = obj["NonDeductVATRpt3Amt"]
      """  Non Deductable VAT Rpt3 Amount  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.ImportedFrom:str = obj["ImportedFrom"]
      """  Country of Import  """  
      self.ImportedDate:str = obj["ImportedDate"]
      """  Date of import.  """  
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      """   Indicates that this is Advanced Tax invoice received from
supplier  """  
      self.InPrice:bool = obj["InPrice"]
      """   Indicates that the tax is included in the unit price
for this AP Invoice  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type ID  """  
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
      """  In case of Tax Inclusive Pricing if system-calculated Header related taxes are changed/deleted/added  by the user - this field is set to true by the system.  """  
      self.DevLog2:bool = obj["DevLog2"]
      """  Reserved for development - logical  """  
      self.DevChar1:str = obj["DevChar1"]
      """  Assigned as "I" when Recurring Invoice has Inactive status.  """  
      self.DevChar2:str = obj["DevChar2"]
      """  Reserved for development - character  """  
      self.DevDate1:str = obj["DevDate1"]
      """  Reserved for development - date  """  
      self.DevDate2:str = obj["DevDate2"]
      """  Reserved for development - date  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.CycleCode:str = obj["CycleCode"]
      """  CycleCode  """  
      self.Duration:int = obj["Duration"]
      """  Duration  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.MaxValueAmt:int = obj["MaxValueAmt"]
      """  MaxValueAmt  """  
      self.DocMaxValueAmt:int = obj["DocMaxValueAmt"]
      """  DocMaxValueAmt  """  
      self.Rpt1MaxValueAmt:int = obj["Rpt1MaxValueAmt"]
      """  Rpt1MaxValueAmt  """  
      self.Rpt2MaxValueAmt:int = obj["Rpt2MaxValueAmt"]
      """  Rpt2MaxValueAmt  """  
      self.Rpt3MaxValueAmt:int = obj["Rpt3MaxValueAmt"]
      """  Rpt3MaxValueAmt  """  
      self.HoldInvoice:bool = obj["HoldInvoice"]
      """  HoldInvoice  """  
      self.CopyLatestInvoice:bool = obj["CopyLatestInvoice"]
      """  CopyLatestInvoice  """  
      self.OverrideEndDate:bool = obj["OverrideEndDate"]
      """  OverrideEndDate  """  
      self.CycleInactive:bool = obj["CycleInactive"]
      """  CycleInactive  """  
      self.RecurSource:bool = obj["RecurSource"]
      """  RecurSource  """  
      self.InstanceNum:int = obj["InstanceNum"]
      """  InstanceNum  """  
      self.RecurBalance:int = obj["RecurBalance"]
      """  RecurBalance  """  
      self.DocRecurBalance:int = obj["DocRecurBalance"]
      """  DocRecurBalance  """  
      self.Rpt1RecurBalance:int = obj["Rpt1RecurBalance"]
      """  Rpt1RecurBalance  """  
      self.Rpt2RecurBalance:int = obj["Rpt2RecurBalance"]
      """  Rpt2RecurBalance  """  
      self.Rpt3RecurBalance:int = obj["Rpt3RecurBalance"]
      """  Rpt3RecurBalance  """  
      self.LastDate:str = obj["LastDate"]
      """  LastDate  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.InvoiceNumList:str = obj["InvoiceNumList"]
      """  InvoiceNumList  """  
      self.IsMaxValue:bool = obj["IsMaxValue"]
      """  IsMaxValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.DMReason:str = obj["DMReason"]
      """  DMReason  """  
      self.UrgentPayment:bool = obj["UrgentPayment"]
      """  UrgentPayment  """  
      self.AGDocPageNum:str = obj["AGDocPageNum"]
      """  AGDocPageNum  """  
      self.AGCAICAEMark:str = obj["AGCAICAEMark"]
      """  AGCAICAEMark  """  
      self.AGCAICAENum:str = obj["AGCAICAENum"]
      """  AGCAICAENum  """  
      self.AGCAICAEExpirationDate:str = obj["AGCAICAEExpirationDate"]
      """  AGCAICAEExpirationDate  """  
      self.AGAvTaxCreditFlag:bool = obj["AGAvTaxCreditFlag"]
      """  AGAvTaxCreditFlag  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGCustomsClearanceNum:str = obj["AGCustomsClearanceNum"]
      """  AGCustomsClearanceNum  """  
      self.AGCustomsCode:str = obj["AGCustomsCode"]
      """  AGCustomsCode  """  
      self.AGDestinationCode:str = obj["AGDestinationCode"]
      """  AGDestinationCode  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Header Number  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.TWDeclareYear:int = obj["TWDeclareYear"]
      """  TWDeclareYear  """  
      self.TWDeclarePeriod:int = obj["TWDeclarePeriod"]
      """  TWDeclarePeriod  """  
      self.APChkGrpID:str = obj["APChkGrpID"]
      """  AP Checking Group ID  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type  """  
      self.PEComputationalCost:str = obj["PEComputationalCost"]
      """  Indicates a computational cost for the invoice  """  
      self.ReferencedByBOE:str = obj["ReferencedByBOE"]
      """  Referenced By BOE  """  
      self.PEDUARefNum:str = obj["PEDUARefNum"]
      """  DUA Reference Number used on Peru Localiation  """  
      self.CustomsNumber:str = obj["CustomsNumber"]
      """  CustomsNumber  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  ReceivedDate  """  
      self.CustOverride:int = obj["CustOverride"]
      """  CustOverride  """  
      self.PrePaymentNum:str = obj["PrePaymentNum"]
      """  Invoice Number of Invoice Pre-Payment which should be automatically applied to this one during posting process.  """  
      self.PrePaymentAmt:int = obj["PrePaymentAmt"]
      """  Pre-Payment amount in Base Currency.  """  
      self.DocPrePaymentAmt:int = obj["DocPrePaymentAmt"]
      """  Pre-Payment amount in Document Currency.  """  
      self.Rpt1PrePaymentAmt:int = obj["Rpt1PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.Rpt2PrePaymentAmt:int = obj["Rpt2PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.Rpt3PrePaymentAmt:int = obj["Rpt3PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.PEAPPayNum:int = obj["PEAPPayNum"]
      """  CSF Peru - AP Payment Number  """  
      self.PEDetTaxAmt:int = obj["PEDetTaxAmt"]
      """  SCF Peru - Detractions Tax Amount  """  
      self.PEDetTaxCurrencyCode:str = obj["PEDetTaxCurrencyCode"]
      """  Peru Detraction Tax Currency Code  """  
      self.PESUNATDepAmt:int = obj["PESUNATDepAmt"]
      """  CSF Peru - SUNAT Deposit Amount  """  
      self.DocPESUNATDepAmt:int = obj["DocPESUNATDepAmt"]
      """  Peru Document SUNAT Deposit Amount  """  
      self.PESUNATDepDate:str = obj["PESUNATDepDate"]
      """  CSF Peru - SUNAT Deposit Date  """  
      self.PESUNATDepNum:str = obj["PESUNATDepNum"]
      """  CSF Peru -  SUNAT Deposit Number  """  
      self.PESUNATNum:str = obj["PESUNATNum"]
      """  SUNAT Reference Number. Once a payment is made, the SUNAT returns a reference number used as the receipt number for the payment.  """  
      self.DocPEDetTaxAmt:int = obj["DocPEDetTaxAmt"]
      """  Document Tax Amount used in Peru detractions  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.PEBOEIsMultiGen:bool = obj["PEBOEIsMultiGen"]
      """  PEBOEIsMultiGen  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.PrePayHeadNum:int = obj["PrePayHeadNum"]
      """  PrePayHeadNum  """  
      self.MXRetentionCode:str = obj["MXRetentionCode"]
      """  MXRetentionCode  """  
      self.PERefDocID:str = obj["PERefDocID"]
      """  PE Reference Document ID  """  
      self.PEReasonCode:str = obj["PEReasonCode"]
      """  PE Reason Code  """  
      self.PEReasonDesc:str = obj["PEReasonDesc"]
      """  PE Reason Description  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  Malaysia Import Declaration Number  """  
      self.TWGUIRegNumSeller:str = obj["TWGUIRegNumSeller"]
      """  TW GUI Code Seller  """  
      self.TWGUIRegNumBuyer:str = obj["TWGUIRegNumBuyer"]
      """  TW GUI Code Buyer  """  
      self.MXTARCode:str = obj["MXTARCode"]
      """  MXTARCode  """  
      self.GRNIClearing:bool = obj["GRNIClearing"]
      """  Flag that indicates if the invoice is a GRNI document.  """  
      self.PEFiscalCreditOperStatus:int = obj["PEFiscalCreditOperStatus"]
      """  CSF Peru - Fiscal Credit Operation Status  """  
      self.PEInternatTaxAgr:str = obj["PEInternatTaxAgr"]
      """  CSF Peru - International Tax agreement  """  
      self.PERentType:str = obj["PERentType"]
      """  CSF Peru - Rent type  """  
      self.PEPurchaseType:str = obj["PEPurchaseType"]
      """  CSF Peru - Purchase  type  """  
      self.THRefInvoiceNum:str = obj["THRefInvoiceNum"]
      """  TH Reference Invoice Num  """  
      self.THRefVendorNum:int = obj["THRefVendorNum"]
      """  TH Reference Vendor Num  """  
      self.JPSummarizationDate:str = obj["JPSummarizationDate"]
      """  Day when a company sums up accounts payable for supplier  """  
      self.JPBillingDate:str = obj["JPBillingDate"]
      """  Date of a Payment Statement  """  
      self.JPBillingNumber:str = obj["JPBillingNumber"]
      """  Legal Number of Payment Statement  """  
      self.SelfInvoice:bool = obj["SelfInvoice"]
      """  SelfInvoice  """  
      self.Printed:bool = obj["Printed"]
      """  Printed  """  
      self.PurPoint:str = obj["PurPoint"]
      """  PurPoint  """  
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      """  PLInvoiceReference  """  
      self.INPortCode:str = obj["INPortCode"]
      """  INPortCode  """  
      self.RefCancelledby:str = obj["RefCancelledby"]
      """  Indicates which invoice number has cancelled this invoice.  """  
      self.CancellationInv:bool = obj["CancellationInv"]
      """  Indicates if this invoice is a cancellation invoice.  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.WithholdAcctToInterim:bool = obj["WithholdAcctToInterim"]
      """  WithholdAcctToInterim  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  Source Plant used for multi site GL  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.CHQRIBAN:str = obj["CHQRIBAN"]
      """  CHQRIBAN  """  
      self.CHQRReference:str = obj["CHQRReference"]
      """  CHQRReference  """  
      self.EDIInvoice:bool = obj["EDIInvoice"]
      """  Set to True for any invoice that is created via EDI  """  
      self.AllowMultInvcReceipts:bool = obj["AllowMultInvcReceipts"]
      """  This external field will hold Company.AllowMultInvcReceipts flag.  """  
      self.ApplyAPPrePayAuto:bool = obj["ApplyAPPrePayAuto"]
      """  Apply AP Pre Payment Automatically.  """  
      self.BankName:str = obj["BankName"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  The base currency symbol  """  
      self.BillAddressList:str = obj["BillAddressList"]
      """  The bill address in list format  """  
      self.CanChangeTaxLiab:bool = obj["CanChangeTaxLiab"]
      self.COIFRSCalculation:bool = obj["COIFRSCalculation"]
      """  IFRS Calculation. If the checkbox is not checked then all the elements below are disabled. If the checkbox is checked, then some elements below become enabled showing default values so that the NPV can be calculated  """  
      self.COIFRSEnabled:bool = obj["COIFRSEnabled"]
      """  If true then Colombia IFRS Net Present Value calculation is enabled  """  
      self.COIFRSFinancialCharge:int = obj["COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.COIFRSInterestRate:int = obj["COIFRSInterestRate"]
      self.COIFRSNumberOfPeriods:int = obj["COIFRSNumberOfPeriods"]
      """  Number of Periods for payment  """  
      self.COIFRSPresentValue:int = obj["COIFRSPresentValue"]
      """  Present Value  """  
      self.CPayIMReceived:bool = obj["CPayIMReceived"]
      """  Flag to indicate if the CPay invoice has been received/trasferred to the corporate.  """  
      self.CPayOpenPayable:bool = obj["CPayOpenPayable"]
      """  Indicates if the CPay invoice is still an open payable at Corporate  """  
      self.CumulativeBalance:int = obj["CumulativeBalance"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrInstanceNum:int = obj["CurrInstanceNum"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  The document currency symbol  """  
      self.DisableAplDate:bool = obj["DisableAplDate"]
      """   The flag to indicate if Invoice Header Apply Date is supposed to be Read Only
(There are any detail/misc lines and not DMR Debit Memo invoice)  """  
      self.DocCOIFRSFinancialCharge:int = obj["DocCOIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.DocCOIFRSPresentValue:int = obj["DocCOIFRSPresentValue"]
      """  Present Value  """  
      self.DocCumulativeBalance:int = obj["DocCumulativeBalance"]
      self.DocInvoiceVariance:int = obj["DocInvoiceVariance"]
      """  The doc invoice variance amount  """  
      self.DocMiscChrgNonDeducTax:int = obj["DocMiscChrgNonDeducTax"]
      self.DocMiscChrgVariance:int = obj["DocMiscChrgVariance"]
      self.DocScrHdrExpTotal:int = obj["DocScrHdrExpTotal"]
      self.DocSourceRecurBalance:int = obj["DocSourceRecurBalance"]
      self.DspGuiImportTaxBasis:int = obj["DspGuiImportTaxBasis"]
      """   Taiwan Localization           
Display Field for Gui Import Tax Basis  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableCPay:bool = obj["EnableCPay"]
      """  Indicates when to enable the CPay field.  """  
      self.EnableDueDate:bool = obj["EnableDueDate"]
      self.EnableExchangeRate:bool = obj["EnableExchangeRate"]
      self.EnableLockRate:bool = obj["EnableLockRate"]
      self.EnableTaxExRate:bool = obj["EnableTaxExRate"]
      self.EnableTaxLock:bool = obj["EnableTaxLock"]
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Enable setting of Transaction Document Type  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.ExchangeRateDate:str = obj["ExchangeRateDate"]
      """  Indicates which date to be used to calculate the exchange rate, I for Invoice Date, A for Apply Date.  """  
      self.GuiTaxBasisFlag:bool = obj["GuiTaxBasisFlag"]
      """   Taiwan Localization           
The flag to indicate if GUITaxBasis prompt is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code  """  
      self.InvoiceTypeDesc:str = obj["InvoiceTypeDesc"]
      """  for Bill of Exchange  """  
      self.InvoiceVariance:int = obj["InvoiceVariance"]
      """  The invoice variance amount  """  
      self.IsLatestRecurrence:bool = obj["IsLatestRecurrence"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.IsOnlyMiscRecords:bool = obj["IsOnlyMiscRecords"]
      """  Is Only Misc lines exits  """  
      self.LACTaxCalcEnabled:bool = obj["LACTaxCalcEnabled"]
      """  LAC Tax Calculation Enabled  """  
      self.LatestInvoice:int = obj["LatestInvoice"]
      self.LatestInvString:str = obj["LatestInvString"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.LineOrMscChrgExists:bool = obj["LineOrMscChrgExists"]
      """  Indicates if lines or misc charges exist for the invoice  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.MiscChrgNonDeducTax:int = obj["MiscChrgNonDeducTax"]
      self.MiscChrgVariance:int = obj["MiscChrgVariance"]
      self.NextInvoiceDate:str = obj["NextInvoiceDate"]
      """  NextInvoiceDate = InvcRecurringCycle.LastDate + RecurringCycle.Interval in RecurringCycle.Modifier units  """  
      self.NoChangeRecur:bool = obj["NoChangeRecur"]
      self.PayMethod:str = obj["PayMethod"]
      """  Pay Method Type  """  
      self.PEFiscalCreditOperStatusDsp:str = obj["PEFiscalCreditOperStatusDsp"]
      """  CSF Peru - Fiscal Credit Operation Status  """  
      self.PEIsNRInvc:bool = obj["PEIsNRInvc"]
      """  Peru Localization Field, Field to disable Non-Resident Inovices Fields.  """  
      self.PLVendorAutoInvoiceNum:bool = obj["PLVendorAutoInvoiceNum"]
      """  CSF Poland. Vendor uses Invoice reference number  """  
      self.PostInvtyWipCos:bool = obj["PostInvtyWipCos"]
      self.RecalcAmts:str = obj["RecalcAmts"]
      """   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  """  
      self.Recurring:bool = obj["Recurring"]
      """  Recurring Source flag  """  
      self.RecurringState:str = obj["RecurringState"]
      self.Rpt1COIFRSFinancialCharge:int = obj["Rpt1COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt1COIFRSPresentValue:int = obj["Rpt1COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt1CumulativeBalance:int = obj["Rpt1CumulativeBalance"]
      self.Rpt1InvoiceVariance:int = obj["Rpt1InvoiceVariance"]
      self.Rpt1MiscChrgNonDeducTax:int = obj["Rpt1MiscChrgNonDeducTax"]
      self.Rpt1MiscChrgVariance:int = obj["Rpt1MiscChrgVariance"]
      self.Rpt1ScrDiscountAmt:int = obj["Rpt1ScrDiscountAmt"]
      self.Rpt1ScrHdrExpTotal:int = obj["Rpt1ScrHdrExpTotal"]
      self.Rpt1ScrHdrMiscChrgTotal:int = obj["Rpt1ScrHdrMiscChrgTotal"]
      self.Rpt1ScrInvLineTotal:int = obj["Rpt1ScrInvLineTotal"]
      self.Rpt1ScrInvoiceAmt:int = obj["Rpt1ScrInvoiceAmt"]
      self.Rpt1ScrInvoiceBal:int = obj["Rpt1ScrInvoiceBal"]
      self.Rpt1ScrInvoiceVendorAmt:int = obj["Rpt1ScrInvoiceVendorAmt"]
      self.Rpt1ScrLACTaxAmt:int = obj["Rpt1ScrLACTaxAmt"]
      """  Rpt1 Scr LAC Tax Amt  """  
      self.Rpt1ScrRounding:int = obj["Rpt1ScrRounding"]
      self.Rpt1ScrTaxAmt:int = obj["Rpt1ScrTaxAmt"]
      self.Rpt1ScrTotBOEWithholding:int = obj["Rpt1ScrTotBOEWithholding"]
      self.Rpt1ScrTotDedTaxAmt:int = obj["Rpt1ScrTotDedTaxAmt"]
      self.Rpt1ScrTotInvoiceAmt:int = obj["Rpt1ScrTotInvoiceAmt"]
      self.Rpt1ScrTotReportableAmt:int = obj["Rpt1ScrTotReportableAmt"]
      self.Rpt1ScrTotSelfAmt:int = obj["Rpt1ScrTotSelfAmt"]
      self.Rpt1ScrTotTaxableAmt:int = obj["Rpt1ScrTotTaxableAmt"]
      self.Rpt1ScrTotWithholdingAmt:int = obj["Rpt1ScrTotWithholdingAmt"]
      self.Rpt1ScrUnpostedBal:int = obj["Rpt1ScrUnpostedBal"]
      self.Rpt1SourceRecurBalance:int = obj["Rpt1SourceRecurBalance"]
      self.Rpt2COIFRSFinancialCharge:int = obj["Rpt2COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt2COIFRSPresentValue:int = obj["Rpt2COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt2CumulativeBalance:int = obj["Rpt2CumulativeBalance"]
      self.Rpt2InvoiceVariance:int = obj["Rpt2InvoiceVariance"]
      self.Rpt2MiscChrgNonDeducTax:int = obj["Rpt2MiscChrgNonDeducTax"]
      self.Rpt2MiscChrgVariance:int = obj["Rpt2MiscChrgVariance"]
      self.Rpt2ScrDiscountAmt:int = obj["Rpt2ScrDiscountAmt"]
      self.Rpt2ScrHdrExpTotal:int = obj["Rpt2ScrHdrExpTotal"]
      self.Rpt2ScrHdrMiscChrgTotal:int = obj["Rpt2ScrHdrMiscChrgTotal"]
      self.Rpt2ScrInvLineTotal:int = obj["Rpt2ScrInvLineTotal"]
      self.Rpt2ScrInvoiceAmt:int = obj["Rpt2ScrInvoiceAmt"]
      self.Rpt2ScrInvoiceBal:int = obj["Rpt2ScrInvoiceBal"]
      self.Rpt2ScrInvoiceVendorAmt:int = obj["Rpt2ScrInvoiceVendorAmt"]
      self.Rpt2ScrLACTaxAmt:int = obj["Rpt2ScrLACTaxAmt"]
      """  Rpt2 Scr LAC Tax Amt  """  
      self.Rpt2ScrRounding:int = obj["Rpt2ScrRounding"]
      self.Rpt2ScrTaxAmt:int = obj["Rpt2ScrTaxAmt"]
      self.Rpt2ScrTotBOEWithholding:int = obj["Rpt2ScrTotBOEWithholding"]
      self.Rpt2ScrTotDedTaxAmt:int = obj["Rpt2ScrTotDedTaxAmt"]
      self.Rpt2ScrTotInvoiceAmt:int = obj["Rpt2ScrTotInvoiceAmt"]
      self.Rpt2ScrTotReportableAmt:int = obj["Rpt2ScrTotReportableAmt"]
      self.Rpt2ScrTotSelfAmt:int = obj["Rpt2ScrTotSelfAmt"]
      self.Rpt2ScrTotTaxableAmt:int = obj["Rpt2ScrTotTaxableAmt"]
      self.Rpt2ScrTotWithholdingAmt:int = obj["Rpt2ScrTotWithholdingAmt"]
      self.Rpt2ScrUnpostedBal:int = obj["Rpt2ScrUnpostedBal"]
      self.Rpt2SourceRecurBalance:int = obj["Rpt2SourceRecurBalance"]
      self.Rpt3COIFRSFinancialCharge:int = obj["Rpt3COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt3COIFRSPresentValue:int = obj["Rpt3COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt3CumulativeBalance:int = obj["Rpt3CumulativeBalance"]
      self.Rpt3InvoiceVariance:int = obj["Rpt3InvoiceVariance"]
      self.Rpt3MiscChrgNonDeducTax:int = obj["Rpt3MiscChrgNonDeducTax"]
      self.Rpt3MiscChrgVariance:int = obj["Rpt3MiscChrgVariance"]
      self.Rpt3ScrDiscountAmt:int = obj["Rpt3ScrDiscountAmt"]
      self.Rpt3ScrHdrExpTotal:int = obj["Rpt3ScrHdrExpTotal"]
      self.Rpt3ScrHdrMiscChrgTotal:int = obj["Rpt3ScrHdrMiscChrgTotal"]
      self.Rpt3ScrInvLineTotal:int = obj["Rpt3ScrInvLineTotal"]
      self.Rpt3ScrInvoiceAmt:int = obj["Rpt3ScrInvoiceAmt"]
      self.Rpt3ScrInvoiceBal:int = obj["Rpt3ScrInvoiceBal"]
      self.Rpt3ScrInvoiceVendorAmt:int = obj["Rpt3ScrInvoiceVendorAmt"]
      self.Rpt3ScrLACTaxAmt:int = obj["Rpt3ScrLACTaxAmt"]
      """  Rpt3 Scr LAC Tax Amt  """  
      self.Rpt3ScrRounding:int = obj["Rpt3ScrRounding"]
      self.Rpt3ScrTaxAmt:int = obj["Rpt3ScrTaxAmt"]
      self.Rpt3ScrTotBOEWithholding:int = obj["Rpt3ScrTotBOEWithholding"]
      self.Rpt3ScrTotDedTaxAmt:int = obj["Rpt3ScrTotDedTaxAmt"]
      self.Rpt3ScrTotInvoiceAmt:int = obj["Rpt3ScrTotInvoiceAmt"]
      self.Rpt3ScrTotReportableAmt:int = obj["Rpt3ScrTotReportableAmt"]
      self.Rpt3ScrTotSelfAmt:int = obj["Rpt3ScrTotSelfAmt"]
      self.Rpt3ScrTotTaxableAmt:int = obj["Rpt3ScrTotTaxableAmt"]
      self.Rpt3ScrTotWithholdingAmt:int = obj["Rpt3ScrTotWithholdingAmt"]
      self.Rpt3ScrUnpostedBal:int = obj["Rpt3ScrUnpostedBal"]
      self.Rpt3SourceRecurBalance:int = obj["Rpt3SourceRecurBalance"]
      self.RptScrTotWithholdingAmt:int = obj["RptScrTotWithholdingAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.ScrDiscountAmt:int = obj["ScrDiscountAmt"]
      self.ScrDocDiscountAmt:int = obj["ScrDocDiscountAmt"]
      self.ScrDocHdrMiscChrgTotal:int = obj["ScrDocHdrMiscChrgTotal"]
      self.ScrDocInvLineTotal:int = obj["ScrDocInvLineTotal"]
      self.ScrDocInvoiceAmt:int = obj["ScrDocInvoiceAmt"]
      self.ScrDocInvoiceBal:int = obj["ScrDocInvoiceBal"]
      self.ScrDocInvoiceVendorAmt:int = obj["ScrDocInvoiceVendorAmt"]
      self.ScrDocRounding:int = obj["ScrDocRounding"]
      self.ScrDocTaxAmt:int = obj["ScrDocTaxAmt"]
      self.ScrDocTotBOEWithholding:int = obj["ScrDocTotBOEWithholding"]
      self.ScrDocTotDedTaxAmt:int = obj["ScrDocTotDedTaxAmt"]
      self.ScrDocTotInvoiceAmt:int = obj["ScrDocTotInvoiceAmt"]
      self.ScrDocTotReportableAmt:int = obj["ScrDocTotReportableAmt"]
      self.ScrDocTotSelfAmt:int = obj["ScrDocTotSelfAmt"]
      self.ScrDocTotTaxableAmt:int = obj["ScrDocTotTaxableAmt"]
      self.ScrDocTotWithholdingAmt:int = obj["ScrDocTotWithholdingAmt"]
      self.ScrDocUnpostedBal:int = obj["ScrDocUnpostedBal"]
      self.ScrHdrExpTotal:int = obj["ScrHdrExpTotal"]
      self.ScrHdrMiscChrgTotal:int = obj["ScrHdrMiscChrgTotal"]
      self.ScrInvLineTotal:int = obj["ScrInvLineTotal"]
      self.ScrInvoiceAmt:int = obj["ScrInvoiceAmt"]
      self.ScrInvoiceBal:int = obj["ScrInvoiceBal"]
      self.ScrInvoiceRef:str = obj["ScrInvoiceRef"]
      self.ScrInvoiceVendorAmt:int = obj["ScrInvoiceVendorAmt"]
      self.ScrLACDocTaxAmt:int = obj["ScrLACDocTaxAmt"]
      """  Scr LAC Doc Tax Amt  """  
      self.ScrLACTaxAmt:int = obj["ScrLACTaxAmt"]
      """  Scr LAC Tax Amt  """  
      self.ScrRounding:int = obj["ScrRounding"]
      self.ScrTaxAmt:int = obj["ScrTaxAmt"]
      """  The screen tax amount  """  
      self.ScrTotBOEWithholding:int = obj["ScrTotBOEWithholding"]
      """  Total of withholdings of all BOE Lines.  """  
      self.ScrTotDedTaxAmt:int = obj["ScrTotDedTaxAmt"]
      self.ScrTotInvoiceAmt:int = obj["ScrTotInvoiceAmt"]
      """  Shall be the sum of column 'Tax Amount' for all lines with collection method 'Invoice'  """  
      self.ScrTotReportableAmt:int = obj["ScrTotReportableAmt"]
      self.ScrTotSelfAmt:int = obj["ScrTotSelfAmt"]
      """  shall be the sum of column 'Tax Amount' for all lines with collection method 'Self-Assessed' or mehtod 'Self-Assessed'  """  
      self.ScrTotTaxableAmt:int = obj["ScrTotTaxableAmt"]
      self.ScrTotWithholdingAmt:int = obj["ScrTotWithholdingAmt"]
      """  shall be the sum of column 'Tax Amount' for all lines with collection  method 'Withholding'  """  
      self.ScrUnpostedBal:int = obj["ScrUnpostedBal"]
      self.SkipRecurring:bool = obj["SkipRecurring"]
      self.SourceInvoiceNum:str = obj["SourceInvoiceNum"]
      """  Recurrent Invoices functionality  """  
      self.SourceLastDate:str = obj["SourceLastDate"]
      self.SourceRecurBalance:int = obj["SourceRecurBalance"]
      self.SwiftCode:str = obj["SwiftCode"]
      """  Swift Code  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  System Transaction Type: APInvoice/DebitMemo  is used in the filter of TranDocType combo-box.  """  
      self.TaxExchangeRate:int = obj["TaxExchangeRate"]
      self.TaxLinesExist:bool = obj["TaxLinesExist"]
      self.TaxRateLinesExist:bool = obj["TaxRateLinesExist"]
      self.TotalInstanceNum:int = obj["TotalInstanceNum"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Link to TranDocType table, can be removed when path filed TranDocTypeID is replaced with actual one.  """  
      self.TransApplyDate:str = obj["TransApplyDate"]
      """  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  """  
      self.UseTaxRate:bool = obj["UseTaxRate"]
      self.VendorInactive:bool = obj["VendorInactive"]
      """  Indicates if the vendor on the invoice is active or not.  """  
      self.VendorPayHold:bool = obj["VendorPayHold"]
      """  Indicates if the vendor on the invoice is in a pay hold state.  """  
      self.VNDateReceived:str = obj["VNDateReceived"]
      self.VNInvoiceType:str = obj["VNInvoiceType"]
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.FormattedVendorNameAddress:str = obj["FormattedVendorNameAddress"]
      """  Formatted Supplier Name and Address  """  
      self.SiteIsLegalEntity:bool = obj["SiteIsLegalEntity"]
      """  Site is a LegalEntity  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGCustomsDescription:str = obj["AGCustomsDescription"]
      self.AGDestinationDescription:str = obj["AGDestinationDescription"]
      self.APInvRecurringCycleInactive:bool = obj["APInvRecurringCycleInactive"]
      self.APInvRecurringCycleDescription:str = obj["APInvRecurringCycleDescription"]
      self.APLOCIDDescription:str = obj["APLOCIDDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.SourcePlantName:str = obj["SourcePlantName"]
      self.TaxRateGrpDescription:str = obj["TaxRateGrpDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.TermsCodeTermsType:str = obj["TermsCodeTermsType"]
      self.THRefVendorNumName:str = obj["THRefVendorNumName"]
      self.THRefVendorNumVendorID:str = obj["THRefVendorNumVendorID"]
      self.VendBankPMUID:int = obj["VendBankPMUID"]
      self.VendBankCardCode:str = obj["VendBankCardCode"]
      self.VendBankBankAcctNumber:str = obj["VendBankBankAcctNumber"]
      self.VendBankIBANCode:str = obj["VendBankIBANCode"]
      self.VendBankBankGiroAcctNbr:str = obj["VendBankBankGiroAcctNbr"]
      self.VendBankSwiftNum:str = obj["VendBankSwiftNum"]
      self.VendBankLocalBIC:str = obj["VendBankLocalBIC"]
      self.VendBankBankName:str = obj["VendBankBankName"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.XbSystAPTaxLnLevel:bool = obj["XbSystAPTaxLnLevel"]
      self.XbSystIsDiscountforDebitM:bool = obj["XbSystIsDiscountforDebitM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvHedTransferListRow:
   def __init__(self, obj):
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount (Vendors Currency). This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and the miscellaneous charges/credits records (APInvMsc). This field has a positive sign (debit memos are negative).  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID taht entered the invoice. This is not maintainable by the user.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with during the data entry process. This field is not directly maintainable. it is assigned by the invoice entry program using teh GroupID of the "current" group that the user is working with. It is used as a selection criteria during the posting process.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and the miscellaneous charges/credits records (APInvMsc). This field has a positive sign (debit memos are negative).  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoceHeld= false. This flag can be used for whatever the reason a user may wish to keep an invoice in a data entry group from being posted. This is NOT the same as putting an invoice on PaymentHold.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record. This number is created based on setup parameters in table LegalNumber  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal VendorNum that ties back to the Vendor master file. This field is not directly maintainable, istead it is assigned from the Vendor. VendorNUmusing VendorID to find the Vendor record.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Supplier Name  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  Supplier ID  """  
      self.SelectedForAction:bool = obj["SelectedForAction"]
      """  This is used to preserve the selected status of the row.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvSearchTableset:
   def __init__(self, obj):
      self.APInvHed:list[Erp_Tablesets_APInvHedRow] = obj["APInvHed"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtAPInvSearchTableset:
   def __init__(self, obj):
      self.APInvHed:list[Erp_Tablesets_APInvHedRow] = obj["APInvHed"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPInvHed_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvSearchTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewAPInvHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPInvHed
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPInvHed:str = obj["whereClauseAPInvHed"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtAPInvSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPInvSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

