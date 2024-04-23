import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ARBOEMultiGenSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBOEInvcAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBOEInvcAmount
   Description: Update total boe amount when the boe invoice amount changes
   OperationID: ChangeBOEInvcAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBOEInvcAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBOEInvcAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustomer
   Description: Update default information based on the customer changing
   OperationID: ChangeCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateARBOEMultiGenInvcs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateARBOEMultiGenInvcs
   Description: Create records in the ARBOEMultiGenInvcs datatable.
   OperationID: CreateARBOEMultiGenInvcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateARBOEMultiGenInvcs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateARBOEMultiGenInvcs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteARBOEMultiGenInvcs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteARBOEMultiGenInvcs
   Description: Delete a record in the ARBOEMultiGenInvcs datatable.
   OperationID: DeleteARBOEMultiGenInvcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteARBOEMultiGenInvcs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteARBOEMultiGenInvcs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateBOEInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateBOEInvoices
   Description: Generate BOE Invoices.
   OperationID: GenerateBOEInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateBOEInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateBOEInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetARBOEMultiGen(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetARBOEMultiGen
   Description: Creates a temporary record to store information needed to create multiple
Bill of Exchange invoices.
   OperationID: GetARBOEMultiGen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARBOEMultiGen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARBOEMultiGen_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetConvertedAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetConvertedAmount
   Description: Convert Amount to BOE currency
Bill of Exchange invoices.
   OperationID: GetConvertedAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConvertedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConvertedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvcsForSelection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvcsForSelection
   Description: This procedure returns the invoices for BOE selection
   OperationID: GetInvcsForSelection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcsForSelection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcsForSelection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecalcTotalBOEAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecalcTotalBOEAmount
   Description: Recalculates total amount of BOEs to be generated.
   OperationID: RecalcTotalBOEAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcTotalBOEAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcTotalBOEAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBOEInvcAmount_input:
   """ Required : 
   inBOEInvoiceAmt
   inBOESeq
   ds
   """  
   def __init__(self, obj):
      self.inBOEInvoiceAmt:int = obj["inBOEInvoiceAmt"]
      """  The boe invoice amount  """  
      self.inBOESeq:int = obj["inBOESeq"]
      """  The boe sequence  """  
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

class ChangeBOEInvcAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCustomer_input:
   """ Required : 
   inCustID
   ds
   """  
   def __init__(self, obj):
      self.inCustID:str = obj["inCustID"]
      """  The customer id  """  
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

class ChangeCustomer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateARBOEMultiGenInvcs_input:
   """ Required : 
   inCreateMethod
   ds
   """  
   def __init__(self, obj):
      self.inCreateMethod:str = obj["inCreateMethod"]
      """  The create method: S - single M - multiple  """  
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

class CreateARBOEMultiGenInvcs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteARBOEMultiGenInvcs_input:
   """ Required : 
   inBOESeq
   ds
   """  
   def __init__(self, obj):
      self.inBOESeq:int = obj["inBOESeq"]
      """  The sequence to delete  """  
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

class DeleteARBOEMultiGenInvcs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ARBOEMultiGenInvcsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.DueDate:str = obj["DueDate"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocBOEAmount:int = obj["DocBOEAmount"]
      self.BOEAmount:int = obj["BOEAmount"]
      self.BOESeq:int = obj["BOESeq"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARBOEMultiGenRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CustNum:int = obj["CustNum"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.CurrDesc:str = obj["CurrDesc"]
      self.FirstDate:str = obj["FirstDate"]
      self.Periodicity:str = obj["Periodicity"]
      self.NumToGenerate:int = obj["NumToGenerate"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocTotalAmount:int = obj["DocTotalAmount"]
      self.TotalAmount:int = obj["TotalAmount"]
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      self.AppliedAmt:int = obj["AppliedAmt"]
      self.GroupID:str = obj["GroupID"]
      self.GuaranteeAddress1:str = obj["GuaranteeAddress1"]
      self.GuaranteeAddress2:str = obj["GuaranteeAddress2"]
      self.GuaranteeAddress3:str = obj["GuaranteeAddress3"]
      self.GuaranteeCity:str = obj["GuaranteeCity"]
      self.GuaranteeCountry:str = obj["GuaranteeCountry"]
      self.GuaranteeName:str = obj["GuaranteeName"]
      self.GuaranteePhoneNum:str = obj["GuaranteePhoneNum"]
      self.GuaranteeState:str = obj["GuaranteeState"]
      self.GuaranteeTaxID:str = obj["GuaranteeTaxID"]
      self.GuaranteeZip:str = obj["GuaranteeZip"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      self.DocTotalDetrAmt:int = obj["DocTotalDetrAmt"]
      self.BTCustNum:int = obj["BTCustNum"]
      self.BTCustName:str = obj["BTCustName"]
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARBOEMultiGenSelRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Indicates if invoice is "open".  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  """  
      self.UnappliedCash:bool = obj["UnappliedCash"]
      """  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.InvoiceSuffix:str = obj["InvoiceSuffix"]
      """  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  """  
      self.DeferredRevenue:bool = obj["DeferredRevenue"]
      """  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  """  
      self.PONum:str = obj["PONum"]
      """  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.FOB:str = obj["FOB"]
      """  Defaults from sales order ORderHed.FOB  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date is duplicated from the InvcGrp record.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Once posted, maintenance is not allowed.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DepositCredit:int = obj["DepositCredit"]
      """  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  """  
      self.DocDepositCredit:int = obj["DocDepositCredit"]
      """  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  """  
      self.SalesRepList:str = obj["SalesRepList"]
      """  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  """  
      self.RefCancelled:int = obj["RefCancelled"]
      """  Value of this field is reference to invoice which has been cancelled by current invoice.  """  
      self.RefCancelledBy:int = obj["RefCancelledBy"]
      """  Value of this field is reference to invoice that cancelled this invoice.  """  
      self.StartUp:bool = obj["StartUp"]
      """  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  """  
      self.PayDates:str = obj["PayDates"]
      """  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayAmounts:str = obj["PayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.DocPayAmounts:str = obj["DocPayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.PayDiscDate:str = obj["PayDiscDate"]
      """  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  """  
      self.PayDiscAmt:int = obj["PayDiscAmt"]
      """  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  """  
      self.DocPayDiscAmt:int = obj["DocPayDiscAmt"]
      """  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  """  
      self.BillConNum:int = obj["BillConNum"]
      """  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal that invoice was posted to.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  """  
      self.RMANum:int = obj["RMANum"]
      """   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that the invoice is relate to.  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identifier  """  
      self.XRefInvoiceNum:str = obj["XRefInvoiceNum"]
      """  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.DepGainLoss:int = obj["DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.DNComments:str = obj["DNComments"]
      """  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  """  
      self.DebitNote:bool = obj["DebitNote"]
      """   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  This is populated from ShipHead.CustNum representing the Sold To customer.  """  
      self.Consolidated:bool = obj["Consolidated"]
      """  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  """  
      self.BillToInvoiceAddress:bool = obj["BillToInvoiceAddress"]
      """  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  """  
      self.SoldToInvoiceAddress:bool = obj["SoldToInvoiceAddress"]
      """  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.RepComm1:int = obj["RepComm1"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm2:int = obj["RepComm2"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm3:int = obj["RepComm3"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm4:int = obj["RepComm4"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm5:int = obj["RepComm5"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepSales1:int = obj["RepSales1"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales2:int = obj["RepSales2"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales3:int = obj["RepSales3"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales4:int = obj["RepSales4"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales5:int = obj["RepSales5"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.CMType:str = obj["CMType"]
      """  Indicates if the Credit Memo is for a Rebate  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding in Customer currency  """  
      self.Rpt1DepositCredit:int = obj["Rpt1DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2DepositCredit:int = obj["Rpt2DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3DepositCredit:int = obj["Rpt3DepositCredit"]
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
      self.Rpt1PayAmounts:str = obj["Rpt1PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayAmounts:str = obj["Rpt2PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayAmounts:str = obj["Rpt3PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayDiscAmt:int = obj["Rpt1PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayDiscAmt:int = obj["Rpt2PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayDiscAmt:int = obj["Rpt3PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnpostedBal:int = obj["Rpt1UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnpostedBal:int = obj["Rpt2UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnpostedBal:int = obj["Rpt3UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1DepGainLoss:int = obj["Rpt1DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2DepGainLoss:int = obj["Rpt2DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3DepGainLoss:int = obj["Rpt3DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.LastChrgCalcDate:str = obj["LastChrgCalcDate"]
      """  The last date finance/late charges have been calculated for this invoice.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.TotFinChrg:int = obj["TotFinChrg"]
      """  Total Finance Charge amount.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.PayDiscDays:str = obj["PayDiscDays"]
      """  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayDiscPer:str = obj["PayDiscPer"]
      """  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  """  
      self.BlockedFinChrg:bool = obj["BlockedFinChrg"]
      """  Blocks certain invoice from generating finance/later charge.  """  
      self.BlockedFinChrgReason:str = obj["BlockedFinChrgReason"]
      """  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  """  
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
      self.BlockedRemLetters:bool = obj["BlockedRemLetters"]
      """  Blocks certain invoice from being printed on reminder letters.  """  
      self.PayDiscPartPay:bool = obj["PayDiscPartPay"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.BlockedRemLettersReason:str = obj["BlockedRemLettersReason"]
      """  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.CurrRateDate:str = obj["CurrRateDate"]
      """  Currency Rate Date  """  
      self.PIPayment:str = obj["PIPayment"]
      """   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.UseAltBillTo:bool = obj["UseAltBillTo"]
      """  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden Finland Localization field - Banking Reference  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.ReversalDocAmount:int = obj["ReversalDocAmount"]
      """  Reversal Doucment Amount  """  
      self.OrigDueDate:str = obj["OrigDueDate"]
      """  Original Due Date at posting time  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The reference to CashHead.HeadNum.Used in deposit invoices  """  
      self.ARLOCID:str = obj["ARLOCID"]
      """  Letter of Credit ID.  """  
      self.ContractRef:str = obj["ContractRef"]
      """  The free text field which can contain reference (such as Contract)  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.PBProjectID:str = obj["PBProjectID"]
      """  If the invoice was generated in Project Billing then it is reference to the project.  """  
      self.DepositAmt:int = obj["DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment  """  
      self.GUIExportBillNumber:str = obj["GUIExportBillNumber"]
      """   Taiwan Localization
Export Bill Number  """  
      self.DocDepositAmt:int = obj["DocDepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in document currency  """  
      self.GUIDateOfExport:str = obj["GUIDateOfExport"]
      """   Taiwan Localization
Date of Export  """  
      self.Rpt1DepositAmt:int = obj["Rpt1DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt1 currency  """  
      self.GUIExportType:str = obj["GUIExportType"]
      """   Taiwan Localization
Export Type  """  
      self.Rpt2DepositAmt:int = obj["Rpt2DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt2 currency  """  
      self.GUIExportMark:str = obj["GUIExportMark"]
      """   Taiwan Localization
Export Mark  """  
      self.Rpt3DepositAmt:int = obj["Rpt3DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt23currency  """  
      self.GUIExportBillType:str = obj["GUIExportBillType"]
      """   Taiwan Localization
Export Bill Type  """  
      self.DepUnallocatedAmt:int = obj["DepUnallocatedAmt"]
      """  Deposit unallocated amount in base currency  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.DocDepUnallocatedAmt:int = obj["DocDepUnallocatedAmt"]
      """  Deposit unallocated amount in document currency  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.Rpt1DepUnallocatedAmt:int = obj["Rpt1DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt1 currency  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  Billing Number to be generated from Legal Numbering upon printing of billing statement.  """  
      self.Rpt2DepUnallocatedAmt:int = obj["Rpt2DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt2 currency  """  
      self.ReadyToBill:bool = obj["ReadyToBill"]
      """  Only records ready to bill will be printed in the Billing Statement  """  
      self.Rpt3DepUnallocatedAmt:int = obj["Rpt3DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt3 currency  """  
      self.OvrDefTaxDate:bool = obj["OvrDefTaxDate"]
      """  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  """  
      self.XRefContractNum:str = obj["XRefContractNum"]
      """  Cross Reference Contract Number.  """  
      self.XRefContractDate:str = obj["XRefContractDate"]
      """  Cross Reference Contract Date.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.CustAgentName:str = obj["CustAgentName"]
      """  Customer Agent Name  """  
      self.CustAgentTaxRegNo:str = obj["CustAgentTaxRegNo"]
      """  Customer Agent Tax Region Number  """  
      self.ExportType:str = obj["ExportType"]
      """  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  """  
      self.ExportReportNo:str = obj["ExportReportNo"]
      """  Export Report Number  """  
      self.RealEstateNo:str = obj["RealEstateNo"]
      """  Real Estate Number  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
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
      self.RecurringState:str = obj["RecurringState"]
      """  RecurringState  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.InvoiceNumList:str = obj["InvoiceNumList"]
      """  InvoiceNumList  """  
      self.IsAddedToGTI:bool = obj["IsAddedToGTI"]
      """  IsAddedToGTI  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.CMReason:str = obj["CMReason"]
      """  CMReason  """  
      self.THIsImmatAdjustment:bool = obj["THIsImmatAdjustment"]
      """  THIsImmatAdjustment  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.RevisionDate:str = obj["RevisionDate"]
      """  RevisionDate  """  
      self.RevisionNum:int = obj["RevisionNum"]
      """  RevisionNum  """  
      self.TWDeclareYear:int = obj["TWDeclareYear"]
      """  TWDeclareYear  """  
      self.TWDeclarePeriod:int = obj["TWDeclarePeriod"]
      """  TWDeclarePeriod  """  
      self.TWGenerationType:str = obj["TWGenerationType"]
      """  TWGenerationType  """  
      self.TWGUIGroup:str = obj["TWGUIGroup"]
      """  TWGUIGroup  """  
      self.TWPeriodPrefix:str = obj["TWPeriodPrefix"]
      """  TWPeriodPrefix  """  
      self.InvInCollections:bool = obj["InvInCollections"]
      """  Indicates if the Invoice is in Collections status  """  
      self.CollectionsCust:bool = obj["CollectionsCust"]
      """   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  """  
      self.CounterARForm:int = obj["CounterARForm"]
      """  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  """  
      self.PostedRecog:bool = obj["PostedRecog"]
      """  flag indicates if Revenue of the invoice has been already posted  """  
      self.CNConfirmDate:str = obj["CNConfirmDate"]
      """  Confirmation Date  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  MXSATSeal  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXTaxRcptType:str = obj["MXTaxRcptType"]
      """  MXTaxRcptType  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.MXTotalPayments:int = obj["MXTotalPayments"]
      """  MXTotalPayments  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  MXCertifiedTimestamp  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  MXSATCertificateSN  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  MXDigitalSeal  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  MXCertificate  """  
      self.MXApprovalYear:int = obj["MXApprovalYear"]
      """  MXApprovalYear  """  
      self.MXCBB:str = obj["MXCBB"]
      """  MXCBB  """  
      self.MXApprovalNum:int = obj["MXApprovalNum"]
      """  MXApprovalNum  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  MXOriginalStringTFD  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MXPaymentNum  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MXPaidAs  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  MXCertificateSN  """  
      self.MXOriginalAmount:int = obj["MXOriginalAmount"]
      """  MXOriginalAmount  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXOriginalDate:str = obj["MXOriginalDate"]
      """  MXOriginalDate  """  
      self.MXOriginalSeries:str = obj["MXOriginalSeries"]
      """  MXOriginalSeries  """  
      self.MXOriginalFolio:str = obj["MXOriginalFolio"]
      """  MXOriginalFolio  """  
      self.MXTaxRegime:str = obj["MXTaxRegime"]
      """  MXTaxRegime  """  
      self.MXOriginalString:str = obj["MXOriginalString"]
      """  MXOriginalString  """  
      self.MXPaymentName:str = obj["MXPaymentName"]
      """  MXPaymentName  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.EInvStatus:int = obj["EInvStatus"]
      """  EInvStatus  """  
      self.EInvTimestamp:str = obj["EInvTimestamp"]
      """  EInvTimestamp  """  
      self.EInvUpdatedBy:str = obj["EInvUpdatedBy"]
      """  EInvUpdatedBy  """  
      self.EInvException:str = obj["EInvException"]
      """  EInvException  """  
      self.WithTaxConfirm:bool = obj["WithTaxConfirm"]
      """  Flagged that this invoice has taxes which were necessary or is necessary now.  """  
      self.UseAltBillToID:bool = obj["UseAltBillToID"]
      """  UseAltBillToID  """  
      self.MXCancelledDate:str = obj["MXCancelledDate"]
      """  MXCancelledDate  """  
      self.Overpaid:bool = obj["Overpaid"]
      """  Overpaid  """  
      self.OrdExchangeRate:int = obj["OrdExchangeRate"]
      """  OrdExchangeRate  """  
      self.PEAPPayNum:int = obj["PEAPPayNum"]
      """  PEAPPayNum  """  
      self.PEBankNumber:str = obj["PEBankNumber"]
      """  PEBankNumber  """  
      self.PECharges:int = obj["PECharges"]
      """  PECharges  """  
      self.PECommissions:int = obj["PECommissions"]
      """  PECommissions  """  
      self.PEDetTaxAmt:int = obj["PEDetTaxAmt"]
      """  PEDetTaxAmt  """  
      self.PEDetTaxCurrencyCode:str = obj["PEDetTaxCurrencyCode"]
      """  PEDetTaxCurrencyCode  """  
      self.PEDischargeAmt:int = obj["PEDischargeAmt"]
      """  PEDischargeAmt  """  
      self.PEDischargeDate:str = obj["PEDischargeDate"]
      """  PEDischargeDate  """  
      self.PEInterest:int = obj["PEInterest"]
      """  PEInterest  """  
      self.PENoPayPenalty:int = obj["PENoPayPenalty"]
      """  PENoPayPenalty  """  
      self.PESUNATDepAmt:int = obj["PESUNATDepAmt"]
      """  CSF Peru - SUNAT Deposit Amount  """  
      self.PESUNATDepDate:str = obj["PESUNATDepDate"]
      """  CSF Peru - SUNAT Deposit Date  """  
      self.PESUNATDepNum:str = obj["PESUNATDepNum"]
      """  CSF Peru -  SUNAT Deposit Number  """  
      self.PEBOEPosted:bool = obj["PEBOEPosted"]
      """  PEBOEPosted  """  
      self.DocPEInterest:int = obj["DocPEInterest"]
      """  DocPEInterest  """  
      self.DocPECommissions:int = obj["DocPECommissions"]
      """  DocPECommissions  """  
      self.DocPECharges:int = obj["DocPECharges"]
      """  DocPECharges  """  
      self.DocPENoPayPenalty:int = obj["DocPENoPayPenalty"]
      """  DocPENoPayPenalty  """  
      self.DocPEDischargeAmt:int = obj["DocPEDischargeAmt"]
      """  DocPEDischargeAmt  """  
      self.DocPEDetTaxAmt:int = obj["DocPEDetTaxAmt"]
      """  DocPEDetTaxAmt  """  
      self.Rpt1PEInterest:int = obj["Rpt1PEInterest"]
      """  Rpt1PEInterest  """  
      self.Rpt1PECommissions:int = obj["Rpt1PECommissions"]
      """  Rpt1PECommissions  """  
      self.Rpt1PECharges:int = obj["Rpt1PECharges"]
      """  Rpt1PECharges  """  
      self.Rpt1PENoPayPenalty:int = obj["Rpt1PENoPayPenalty"]
      """  Rpt1PENoPayPenalty  """  
      self.Rpt1PEDischargeAmt:int = obj["Rpt1PEDischargeAmt"]
      """  Rpt1PEDischargeAmt  """  
      self.Rpt2PEInterest:int = obj["Rpt2PEInterest"]
      """  Rpt2PEInterest  """  
      self.Rpt2PECommissions:int = obj["Rpt2PECommissions"]
      """  Rpt2PECommissions  """  
      self.Rpt2PECharges:int = obj["Rpt2PECharges"]
      """  Rpt2PECharges  """  
      self.Rpt2PENoPayPenalty:int = obj["Rpt2PENoPayPenalty"]
      """  Rpt2PENoPayPenalty  """  
      self.Rpt2PEDischargeAmt:int = obj["Rpt2PEDischargeAmt"]
      """  Rpt2PEDischargeAmt  """  
      self.Rpt3PEInterest:int = obj["Rpt3PEInterest"]
      """  Rpt3PEInterest  """  
      self.Rpt3PECommissions:int = obj["Rpt3PECommissions"]
      """  Rpt3PECommissions  """  
      self.Rpt3PECharges:int = obj["Rpt3PECharges"]
      """  Rpt3PECharges  """  
      self.Rpt3PENoPayPenalty:int = obj["Rpt3PENoPayPenalty"]
      """  Rpt3PENoPayPenalty  """  
      self.Rpt3PEDischargeAmt:int = obj["Rpt3PEDischargeAmt"]
      """  Rpt3PEDischargeAmt  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Supplier Code  """  
      self.PEGuaranteeName:str = obj["PEGuaranteeName"]
      """  PEGuaranteeName  """  
      self.PEGuaranteeAddress1:str = obj["PEGuaranteeAddress1"]
      """  PEGuaranteeAddress1  """  
      self.PEGuaranteeAddress2:str = obj["PEGuaranteeAddress2"]
      """  PEGuaranteeAddress2  """  
      self.PEGuaranteeAddress3:str = obj["PEGuaranteeAddress3"]
      """  PEGuaranteeAddress3  """  
      self.PEGuaranteeCity:str = obj["PEGuaranteeCity"]
      """  PEGuaranteeCity  """  
      self.PEGuaranteeState:str = obj["PEGuaranteeState"]
      """  PEGuaranteeState  """  
      self.PEGuaranteeZip:str = obj["PEGuaranteeZip"]
      """  PEGuaranteeZip  """  
      self.PEGuaranteeCountry:str = obj["PEGuaranteeCountry"]
      """  PEGuaranteeCountry  """  
      self.PEGuaranteeTaxID:str = obj["PEGuaranteeTaxID"]
      """  PEGuaranteeTaxID  """  
      self.PEGuaranteePhoneNum:str = obj["PEGuaranteePhoneNum"]
      """  PEGuaranteePhoneNum  """  
      self.PEBOEStatus:str = obj["PEBOEStatus"]
      """  PEBOEStatus  """  
      self.PEBOEIsMultiGen:bool = obj["PEBOEIsMultiGen"]
      """  PEBOEIsMultiGen  """  
      self.PERefDocID:str = obj["PERefDocID"]
      """  PE Reference Document ID  """  
      self.PEReasonCode:str = obj["PEReasonCode"]
      """  PE Reason Code  """  
      self.PEReasonDesc:str = obj["PEReasonDesc"]
      """  PE Reason Description  """  
      self.TWGUIRegNumSeller:str = obj["TWGUIRegNumSeller"]
      """  TW GUI Code Seller  """  
      self.TWGUIRegNumBuyer:str = obj["TWGUIRegNumBuyer"]
      """  TW GUI Code Buyer  """  
      self.TWGUIExportDocumentName:str = obj["TWGUIExportDocumentName"]
      """  Document Name  """  
      self.TWGUIExportRemarks:str = obj["TWGUIExportRemarks"]
      """  Remarks  """  
      self.TWGUIExportVerification:str = obj["TWGUIExportVerification"]
      """  Verification  """  
      self.PEDebitNoteReasonCode:str = obj["PEDebitNoteReasonCode"]
      """  PEDebitNoteReasonCode  """  
      self.PEDebitNote:bool = obj["PEDebitNote"]
      """  PEDebitNote  """  
      self.MXPartPmt:bool = obj["MXPartPmt"]
      """  MXPartPmt  """  
      self.CNTaxInvoiceType:int = obj["CNTaxInvoiceType"]
      """  Tax Invoice Type  """  
      self.MXExportOperationType:str = obj["MXExportOperationType"]
      """  MXExportOperationType  """  
      self.MXExportCustDocCode:str = obj["MXExportCustDocCode"]
      """  MXExportCustDocCode  """  
      self.MXExportCertOriginNum:str = obj["MXExportCertOriginNum"]
      """  MXExportCertOriginNum  """  
      self.MXExportConfNum:str = obj["MXExportConfNum"]
      """  MXExportConfNum  """  
      self.MXExportCertOrigin:bool = obj["MXExportCertOrigin"]
      """  MXExportCertOrigin  """  
      self.MXIncoterm:str = obj["MXIncoterm"]
      """  MXIncoterm  """  
      self.AGDocConcept:int = obj["AGDocConcept"]
      """  AGDocConcept  """  
      self.EInvRefNum:str = obj["EInvRefNum"]
      """  Electronic Invoice reference number  """  
      self.ExportDocRefNum:str = obj["ExportDocRefNum"]
      """  Export document reference number  """  
      self.ExportDocDate:str = obj["ExportDocDate"]
      """  Export document date  """  
      self.INTaxTransactionID:str = obj["INTaxTransactionID"]
      """  Tax Transaction ID  """  
      self.MXMovingReasonFlag:bool = obj["MXMovingReasonFlag"]
      """  MXMovingReasonFlag  """  
      self.MXMovingReason:str = obj["MXMovingReason"]
      """  MXMovingReason  """  
      self.MXNumRegIdTrib:str = obj["MXNumRegIdTrib"]
      """  MXNumRegIdTrib  """  
      self.MXResidenCountryNum:int = obj["MXResidenCountryNum"]
      """  MXResidenCountryNum  """  
      self.MXPurchaseType:str = obj["MXPurchaseType"]
      """  MXPurchaseType  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MXConfirmationCode  """  
      self.MXExternalCode:str = obj["MXExternalCode"]
      """  MXExternalCode  """  
      self.ServiceInvoice:bool = obj["ServiceInvoice"]
      """  This invoice was created via an integration with a third-party field service.  """  
      self.MXDomesticTransfer:bool = obj["MXDomesticTransfer"]
      """  MXDomesticTransfer  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.INShippingPortCode:str = obj["INShippingPortCode"]
      """  Shipping Port Code  """  
      self.INExportProcedure:str = obj["INExportProcedure"]
      """  Export Procedure  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this invoice record is associated with.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case related to this invoice.  """  
      self.CreditOverride:bool = obj["CreditOverride"]
      """  Indicates that the credit hold was overridden for this invoice.  """  
      self.CreditOverrideDate:str = obj["CreditOverrideDate"]
      """  Description	Indicates that the credit hold was overridden for this invoice.	The date and time the user override the invoice credit hold.  """  
      self.CreditOverrideUserID:str = obj["CreditOverrideUserID"]
      """  The user id that override the invoice credit hold.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates the invoice is on credit hold.  Applicable to miscellaneous invoices only.  """  
      self.PEXMLType:int = obj["PEXMLType"]
      """  Peru Electronic Invoice XML Type  """  
      self.COCreditMemoReasonCode:str = obj["COCreditMemoReasonCode"]
      """  COCreditMemoReasonCode  """  
      self.CODebitMemoReasonCode:str = obj["CODebitMemoReasonCode"]
      """  CODebitMemoReasonCode  """  
      self.COReasonDesc:str = obj["COReasonDesc"]
      """  COReasonDesc  """  
      self.CODebitNote:bool = obj["CODebitNote"]
      """  CODebitNote  """  
      self.PEDetractionTranNum:int = obj["PEDetractionTranNum"]
      """  PEDetractionTranNum  """  
      self.PEProductCode:str = obj["PEProductCode"]
      """  PEProductCode  """  
      self.PECollectionGroupID:str = obj["PECollectionGroupID"]
      """  PECollectionGroupID  """  
      self.PECaptionCode:str = obj["PECaptionCode"]
      """  PE Caption Code  """  
      self.PECaption:str = obj["PECaption"]
      """  PE Caption Code Description  """  
      self.PERefDocumentType:str = obj["PERefDocumentType"]
      """  PE Reference DocumentType 1  """  
      self.PERefDocumentNumber:str = obj["PERefDocumentNumber"]
      """  PE Reference Document Number 1  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PE Detraction good or service code  """  
      self.PERefDocumentType2:str = obj["PERefDocumentType2"]
      """  PE Reference DocumentType 2  """  
      self.PERefDocumentType3:str = obj["PERefDocumentType3"]
      """  PE Reference DocumentType 3  """  
      self.PERefDocumentType4:str = obj["PERefDocumentType4"]
      """  PE Reference DocumentType 4  """  
      self.PERefDocumentType5:str = obj["PERefDocumentType5"]
      """  PE Reference DocumentType 5  """  
      self.PERefDocumentNumber2:str = obj["PERefDocumentNumber2"]
      """  PE Reference Document Number 2  """  
      self.PERefDocumentNumber3:str = obj["PERefDocumentNumber3"]
      """  PE Reference Document Number 3  """  
      self.PERefDocumentNumber4:str = obj["PERefDocumentNumber4"]
      """  PE Reference Document Number 4  """  
      self.PERefDocumentNumber5:str = obj["PERefDocumentNumber5"]
      """  PE Reference Document Number 5  """  
      self.ELIEInvoice:bool = obj["ELIEInvoice"]
      """  E-invoice  """  
      self.ELIEInvStatus:int = obj["ELIEInvStatus"]
      """  Status of E-invoice (1 - Open, 2 - Generated, 3 - Sent, 4 - Error).  """  
      self.ELIEInvUpdatedBy:str = obj["ELIEInvUpdatedBy"]
      """  User Id of the person generated E-invoice.  """  
      self.ELIEInvException:str = obj["ELIEInvException"]
      """  E-invoice error description.  """  
      self.ELIEInvUpdatedOn:str = obj["ELIEInvUpdatedOn"]
      """  Date and Time of E-invoice generation.  """  
      self.COOperType:str = obj["COOperType"]
      """  COOperType  """  
      self.CentralCollection:bool = obj["CentralCollection"]
      """  Flag that indicates if the Invoice is for Central Collection.  """  
      self.CColChildCompany:str = obj["CColChildCompany"]
      """  Company that created this invoice.  """  
      self.CColParentCompany:str = obj["CColParentCompany"]
      """  Central Collection company.  """  
      self.CColOrderNum:int = obj["CColOrderNum"]
      """  Order number on the invoicing company.  """  
      self.CColChildInvoiceNum:int = obj["CColChildInvoiceNum"]
      """  Invoice number on the invoicing company.  """  
      self.CColInvoiceNum:int = obj["CColInvoiceNum"]
      """  Invoice number on central collection company  """  
      self.CColChildLegalNumber:str = obj["CColChildLegalNumber"]
      """  Legal number on the invoicing company invoice.  """  
      self.CColLegalNumber:str = obj["CColLegalNumber"]
      """  Legal number on central collection company.  """  
      self.CColInvoiceRef:int = obj["CColInvoiceRef"]
      """  Invoice reference on the Invoicing Company.  """  
      self.CColInvBal:int = obj["CColInvBal"]
      """  Invoice Balance in the Central Collection company.  """  
      self.DocCColInvBal:int = obj["DocCColInvBal"]
      """  Central Collection Doc Invoice Balance.  """  
      self.CColInvAmt:int = obj["CColInvAmt"]
      """  Invoice Amount on the Invoicing Company.  """  
      self.DocCColInvAmt:int = obj["DocCColInvAmt"]
      """  Invoice Amount on the Invoicing Company.  """  
      self.Rpt1CColInvBal:int = obj["Rpt1CColInvBal"]
      """  Rpt 1 Parent Invoice Balance  """  
      self.Rpt2CColInvBal:int = obj["Rpt2CColInvBal"]
      """  Rpt 2 Parent Invoice Balance  """  
      self.Rpt3CColInvBal:int = obj["Rpt3CColInvBal"]
      """  Rpt 3 Parent Invoice Balance  """  
      self.Rpt1CColInvAmt:int = obj["Rpt1CColInvAmt"]
      """  Rpt 1 Child Invoice Amount  """  
      self.Rpt2CColInvAmt:int = obj["Rpt2CColInvAmt"]
      """  Rpt 2 Child Invoice Amount  """  
      self.Rpt3CColInvAmt:int = obj["Rpt3CColInvAmt"]
      """  Rpt 3 Child Invoice Amount  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.ELIEInvTerminalName:str = obj["ELIEInvTerminalName"]
      """  User terminal name  """  
      self.ELIEInvTerminalIP:str = obj["ELIEInvTerminalIP"]
      """  User terminal IP  """  
      self.Description:str = obj["Description"]
      """  GL Description  """  
      self.WithholdAcctToInterim:bool = obj["WithholdAcctToInterim"]
      """  WithholdAcctToInterim  """  
      self.CColOpenInvoice:bool = obj["CColOpenInvoice"]
      """  Indicates if the Central Collection parent invoice is open.  """  
      self.AGQRCodeData:str = obj["AGQRCodeData"]
      """  AGQRCodeData  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  Exempt Reason Code  """  
      self.ELIEInvID:str = obj["ELIEInvID"]
      """  EInvoice ID  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallLine:int = obj["CallLine"]
      """  this is a link to the service call line that this invoice is for.  Linetype = "CALL"  """  
      self.JobNum:str = obj["JobNum"]
      """  Associates the Call Line record back its linked jobnum  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstInvoiceNum:int = obj["MXSubstInvoiceNum"]
      """  MXSubstInvoiceNum  """  
      self.MXExportType:str = obj["MXExportType"]
      """  MXExportType  """  
      self.MXGlobalInvoicePeriod:str = obj["MXGlobalInvoicePeriod"]
      """  MXGlobalInvoicePeriod  """  
      self.MXGlobalInvoiceMonth:str = obj["MXGlobalInvoiceMonth"]
      """  MXGlobalInvoiceMonth  """  
      self.ELIEInvServiceProviderStatus:int = obj["ELIEInvServiceProviderStatus"]
      """  ELIEInvServiceProviderStatus  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.CovenantDiscPercent:int = obj["CovenantDiscPercent"]
      """  CovenantDiscPercent  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.DocApplyAmt:int = obj["DocApplyAmt"]
      """  Amount that will be applied to the BOE invoice  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.DocNetToBOE:int = obj["DocNetToBOE"]
      self.Selected:bool = obj["Selected"]
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.ApplyAmt:int = obj["ApplyAmt"]
      """  Amount that will be applied to the BOE invoice  """  
      self.NetToBOE:int = obj["NetToBOE"]
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.PEDocDetTaxAmt:int = obj["PEDocDetTaxAmt"]
      """  CSF Peru - Detractions Doc Tax amount  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARBOEMultiGenTableset:
   def __init__(self, obj):
      self.ARBOEMultiGen:list[Erp_Tablesets_ARBOEMultiGenRow] = obj["ARBOEMultiGen"]
      self.ARBOEMultiGenInvcs:list[Erp_Tablesets_ARBOEMultiGenInvcsRow] = obj["ARBOEMultiGenInvcs"]
      self.ARBOEMultiGenSel:list[Erp_Tablesets_ARBOEMultiGenSelRow] = obj["ARBOEMultiGenSel"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateBOEInvoices_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

class GenerateBOEInvoices_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      self.outAssignLN:bool = obj["outAssignLN"]
      pass

      """  output parameters  """  

class GetARBOEMultiGen_input:
   """ Required : 
   inGroupID
   """  
   def __init__(self, obj):
      self.inGroupID:str = obj["inGroupID"]
      """  The group id  """  
      pass

class GetARBOEMultiGen_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetConvertedAmount_input:
   """ Required : 
   ipInvoiceNum
   ipCurrCode
   ipRateGrpCode
   ipInputAmount
   ipInvoiceDate
   ipApplyDate
   """  
   def __init__(self, obj):
      self.ipInvoiceNum:int = obj["ipInvoiceNum"]
      """  Invoice Number  """  
      self.ipCurrCode:str = obj["ipCurrCode"]
      """  Currency Code  """  
      self.ipRateGrpCode:str = obj["ipRateGrpCode"]
      """  Rate Group Code  """  
      self.ipInputAmount:int = obj["ipInputAmount"]
      """  Amount to be converted  """  
      self.ipInvoiceDate:str = obj["ipInvoiceDate"]
      """  Invoice date  """  
      self.ipApplyDate:str = obj["ipApplyDate"]
      """  Apply date  """  
      pass

class GetConvertedAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ipAmount:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetInvcsForSelection_input:
   """ Required : 
   whereClause
   ds
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause for Cash Receipt.  """  
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

class GetInvcsForSelection_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

      """  output parameters  """  

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

class RecalcTotalBOEAmount_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

class RecalcTotalBOEAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARBOEMultiGenTableset] = obj["ds"]
      pass

      """  output parameters  """  

