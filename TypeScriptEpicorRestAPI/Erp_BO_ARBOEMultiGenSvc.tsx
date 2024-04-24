import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ARBOEMultiGenSvc
// Description: Add your summary for this object here
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeBOEInvcAmount
   Description: Update total boe amount when the boe invoice amount changes
   OperationID: ChangeBOEInvcAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBOEInvcAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBOEInvcAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBOEInvcAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/ChangeBOEInvcAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCustomer
   Description: Update default information based on the customer changing
   OperationID: ChangeCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/ChangeCustomer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateARBOEMultiGenInvcs
   Description: Create records in the ARBOEMultiGenInvcs datatable.
   OperationID: CreateARBOEMultiGenInvcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateARBOEMultiGenInvcs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateARBOEMultiGenInvcs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateARBOEMultiGenInvcs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/CreateARBOEMultiGenInvcs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteARBOEMultiGenInvcs
   Description: Delete a record in the ARBOEMultiGenInvcs datatable.
   OperationID: DeleteARBOEMultiGenInvcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteARBOEMultiGenInvcs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteARBOEMultiGenInvcs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteARBOEMultiGenInvcs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/DeleteARBOEMultiGenInvcs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateBOEInvoices
   Description: Generate BOE Invoices.
   OperationID: GenerateBOEInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateBOEInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateBOEInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateBOEInvoices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/GenerateBOEInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
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
   */  
export function post_GetARBOEMultiGen(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/GetARBOEMultiGen", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
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
   */  
export function post_GetConvertedAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/GetConvertedAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvcsForSelection
   Description: This procedure returns the invoices for BOE selection
   OperationID: GetInvcsForSelection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcsForSelection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcsForSelection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvcsForSelection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/GetInvcsForSelection", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RecalcTotalBOEAmount
   Description: Recalculates total amount of BOEs to be generated.
   OperationID: RecalcTotalBOEAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcTotalBOEAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcTotalBOEAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecalcTotalBOEAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARBOEMultiGenSvc/RecalcTotalBOEAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param inBOEInvoiceAmt
      @param inBOESeq
      @param ds
   */  
export interface ChangeBOEInvcAmount_input{
      /**  The boe invoice amount  */  
   inBOEInvoiceAmt:number,
      /**  The boe sequence  */  
   inBOESeq:number,
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}

export interface ChangeBOEInvcAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}
}

   /** Required : 
      @param inCustID
      @param ds
   */  
export interface ChangeCustomer_input{
      /**  The customer id  */  
   inCustID:string,
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}

export interface ChangeCustomer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}
}

   /** Required : 
      @param inCreateMethod
      @param ds
   */  
export interface CreateARBOEMultiGenInvcs_input{
      /**  The create method: S - single M - multiple  */  
   inCreateMethod:string,
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}

export interface CreateARBOEMultiGenInvcs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}
}

   /** Required : 
      @param inBOESeq
      @param ds
   */  
export interface DeleteARBOEMultiGenInvcs_input{
      /**  The sequence to delete  */  
   inBOESeq:number,
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}

export interface DeleteARBOEMultiGenInvcs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}
}

export interface Erp_Tablesets_ARBOEMultiGenInvcsRow{
   Company:string,
   GroupID:string,
   DueDate:string,
   CurrencyCode:string,
   DocBOEAmount:number,
   BOEAmount:number,
   BOESeq:number,
   RateGrpCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARBOEMultiGenRow{
   Company:string,
   CustNum:number,
   CustID:string,
   CustName:string,
   CurrDesc:string,
   FirstDate:string,
   Periodicity:string,
   NumToGenerate:number,
   CurrencyCode:string,
   DocTotalAmount:number,
   TotalAmount:number,
   DocAppliedAmt:number,
   AppliedAmt:number,
   GroupID:string,
   GuaranteeAddress1:string,
   GuaranteeAddress2:string,
   GuaranteeAddress3:string,
   GuaranteeCity:string,
   GuaranteeCountry:string,
   GuaranteeName:string,
   GuaranteePhoneNum:string,
   GuaranteeState:string,
   GuaranteeTaxID:string,
   GuaranteeZip:string,
   RateGrpCode:string,
   CurrRateGrpDescription:string,
   DocTotalDetrAmt:number,
   BTCustNum:number,
   BTCustName:string,
      /**  Delimited list of available bill to customers.  */  
   AvailBTCustList:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARBOEMultiGenSelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if invoice is "open".  */  
   OpenInvoice:boolean,
      /**  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  */  
   ClosedDate:string,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   CreditMemo:boolean,
      /**  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  */  
   UnappliedCash:boolean,
      /**   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  */  
   InvoiceSuffix:string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   InvoiceType:string,
      /**  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  */  
   DeferredRevenue:boolean,
      /**  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  */  
   OrderNum:number,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   CustNum:number,
      /**  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  */  
   PONum:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Defaults from sales order ORderHed.FOB  */  
   FOB:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  */  
   FiscalPeriod:number,
      /**  Once posted, maintenance is not allowed.  */  
   GLPosted:boolean,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnpostedBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   DocUnpostedBal:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DepositCredit:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DocDepositCredit:number,
      /**  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  */  
   SalesRepList:string,
      /**   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   InvoiceRef:number,
      /**  Value of this field is reference to invoice which has been cancelled by current invoice.  */  
   RefCancelled:number,
      /**  Value of this field is reference to invoice that cancelled this invoice.  */  
   RefCancelledBy:number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   StartUp:boolean,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDates:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   PayAmounts:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   DocPayAmounts:string,
      /**  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  */  
   PayDiscDate:string,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   PayDiscAmt:number,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   DocPayDiscAmt:number,
      /**  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  */  
   BillConNum:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  */  
   InvoiceHeld:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Journal that invoice was posted to.  */  
   JournalCode:string,
      /**  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  */  
   LineType:string,
      /**   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**  The Site that the invoice is relate to.  */  
   Plant:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  External Identifier  */  
   ExternalID:string,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefInvoiceNum:string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   DepGainLoss:number,
      /**  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  */  
   DNComments:string,
      /**  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  */  
   DNCustNbr:string,
      /**   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  */  
   DebitNote:boolean,
      /**  This is populated from ShipHead.CustNum representing the Sold To customer.  */  
   SoldToCustNum:number,
      /**  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  */  
   Consolidated:boolean,
      /**  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  */  
   BillToInvoiceAddress:boolean,
      /**  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  */  
   SoldToInvoiceAddress:boolean,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm1:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm2:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm3:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm4:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm5:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate1:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate2:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate3:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate4:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate5:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales1:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales2:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales3:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales4:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales5:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit1:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit2:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit3:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit4:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit5:number,
      /**  Indicates if the Credit Memo is for a Rebate  */  
   CMType:string,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding in Customer currency  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt1PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt2PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt3PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt1PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnpostedBal:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3DepGainLoss:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Tax point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  The last date finance/late charges have been calculated for this invoice.  */  
   LastChrgCalcDate:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Total Finance Charge amount.  */  
   TotFinChrg:number,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDiscDays:string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   PayDiscPer:string,
      /**  Blocks certain invoice from generating finance/later charge.  */  
   BlockedFinChrg:boolean,
      /**  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  */  
   BlockedFinChrgReason:string,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Blocks certain invoice from being printed on reminder letters.  */  
   BlockedRemLetters:boolean,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PayDiscPartPay:boolean,
      /**  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  */  
   BlockedRemLettersReason:string,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  Currency Rate Date  */  
   CurrRateDate:string,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   PIPayment:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  */  
   UseAltBillTo:boolean,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden Finland Localization field - Banking Reference  */  
   SEBankRef:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Reversal Doucment Amount  */  
   ReversalDocAmount:number,
      /**  Original Due Date at posting time  */  
   OrigDueDate:string,
      /**  The reference to CashHead.HeadNum.Used in deposit invoices  */  
   HeadNum:number,
      /**  Letter of Credit ID.  */  
   ARLOCID:string,
      /**  The free text field which can contain reference (such as Contract)  */  
   ContractRef:string,
      /**  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  */  
   OurBank:string,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  If the invoice was generated in Project Billing then it is reference to the project.  */  
   PBProjectID:string,
      /**  Deposit amount is transaction amount of deposit payment  */  
   DepositAmt:number,
      /**   Taiwan Localization
Export Bill Number  */  
   GUIExportBillNumber:string,
      /**  Deposit amount is transaction amount of deposit payment in document currency  */  
   DocDepositAmt:number,
      /**   Taiwan Localization
Date of Export  */  
   GUIDateOfExport:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt1 currency  */  
   Rpt1DepositAmt:number,
      /**   Taiwan Localization
Export Type  */  
   GUIExportType:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt2 currency  */  
   Rpt2DepositAmt:number,
      /**   Taiwan Localization
Export Mark  */  
   GUIExportMark:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt23currency  */  
   Rpt3DepositAmt:number,
      /**   Taiwan Localization
Export Bill Type  */  
   GUIExportBillType:string,
      /**  Deposit unallocated amount in base currency  */  
   DepUnallocatedAmt:number,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   SummarizationDate:string,
      /**  Deposit unallocated amount in document currency  */  
   DocDepUnallocatedAmt:number,
      /**  Date when a company bills the customer  */  
   BillingDate:string,
      /**  Deposit unallocated amount in Rpt1 currency  */  
   Rpt1DepUnallocatedAmt:number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   BillingNumber:string,
      /**  Deposit unallocated amount in Rpt2 currency  */  
   Rpt2DepUnallocatedAmt:number,
      /**  Only records ready to bill will be printed in the Billing Statement  */  
   ReadyToBill:boolean,
      /**  Deposit unallocated amount in Rpt3 currency  */  
   Rpt3DepUnallocatedAmt:number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   OvrDefTaxDate:boolean,
      /**  Cross Reference Contract Number.  */  
   XRefContractNum:string,
      /**  Cross Reference Contract Date.  */  
   XRefContractDate:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Customer Agent Name  */  
   CustAgentName:string,
      /**  Customer Agent Tax Region Number  */  
   CustAgentTaxRegNo:string,
      /**  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  */  
   ExportType:string,
      /**  Export Report Number  */  
   ExportReportNo:string,
      /**  Real Estate Number  */  
   RealEstateNo:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  CycleCode  */  
   CycleCode:string,
      /**  Duration  */  
   Duration:number,
      /**  EndDate  */  
   EndDate:string,
      /**  MaxValueAmt  */  
   MaxValueAmt:number,
      /**  DocMaxValueAmt  */  
   DocMaxValueAmt:number,
      /**  Rpt1MaxValueAmt  */  
   Rpt1MaxValueAmt:number,
      /**  Rpt2MaxValueAmt  */  
   Rpt2MaxValueAmt:number,
      /**  Rpt3MaxValueAmt  */  
   Rpt3MaxValueAmt:number,
      /**  HoldInvoice  */  
   HoldInvoice:boolean,
      /**  CopyLatestInvoice  */  
   CopyLatestInvoice:boolean,
      /**  OverrideEndDate  */  
   OverrideEndDate:boolean,
      /**  CycleInactive  */  
   CycleInactive:boolean,
      /**  RecurSource  */  
   RecurSource:boolean,
      /**  InstanceNum  */  
   InstanceNum:number,
      /**  RecurBalance  */  
   RecurBalance:number,
      /**  DocRecurBalance  */  
   DocRecurBalance:number,
      /**  Rpt1RecurBalance  */  
   Rpt1RecurBalance:number,
      /**  Rpt2RecurBalance  */  
   Rpt2RecurBalance:number,
      /**  Rpt3RecurBalance  */  
   Rpt3RecurBalance:number,
      /**  LastDate  */  
   LastDate:string,
      /**  RecurringState  */  
   RecurringState:string,
      /**  IsRecurring  */  
   IsRecurring:boolean,
      /**  InvoiceNumList  */  
   InvoiceNumList:string,
      /**  IsAddedToGTI  */  
   IsAddedToGTI:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHISRCodeLine  */  
   CHISRCodeLine:string,
      /**  CMReason  */  
   CMReason:string,
      /**  THIsImmatAdjustment  */  
   THIsImmatAdjustment:boolean,
      /**  AGAuthorizationCode  */  
   AGAuthorizationCode:string,
      /**  AGAuthorizationDate  */  
   AGAuthorizationDate:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGDocumentLetter  */  
   AGDocumentLetter:string,
      /**  AGInvoicingPoint  */  
   AGInvoicingPoint:string,
      /**  AGLegalNumber  */  
   AGLegalNumber:string,
      /**  AGPrintingControlType  */  
   AGPrintingControlType:string,
      /**  RevisionDate  */  
   RevisionDate:string,
      /**  RevisionNum  */  
   RevisionNum:number,
      /**  TWDeclareYear  */  
   TWDeclareYear:number,
      /**  TWDeclarePeriod  */  
   TWDeclarePeriod:number,
      /**  TWGenerationType  */  
   TWGenerationType:string,
      /**  TWGUIGroup  */  
   TWGUIGroup:string,
      /**  TWPeriodPrefix  */  
   TWPeriodPrefix:string,
      /**  Indicates if the Invoice is in Collections status  */  
   InvInCollections:boolean,
      /**   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  */  
   CollectionsCust:boolean,
      /**  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  */  
   CounterARForm:number,
      /**  flag indicates if Revenue of the invoice has been already posted  */  
   PostedRecog:boolean,
      /**  Confirmation Date  */  
   CNConfirmDate:string,
      /**  MXSATSeal  */  
   MXSATSeal:string,
      /**  MXSerie  */  
   MXSerie:string,
      /**  MXTaxRcptType  */  
   MXTaxRcptType:string,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  MXTotalPayments  */  
   MXTotalPayments:number,
      /**  MXFolio  */  
   MXFolio:string,
      /**  MXCertifiedTimestamp  */  
   MXCertifiedTimestamp:string,
      /**  MXSATCertificateSN  */  
   MXSATCertificateSN:string,
      /**  MXDigitalSeal  */  
   MXDigitalSeal:string,
      /**  MXPostedTimeStamp  */  
   MXPostedTimeStamp:string,
      /**  MXCertificate  */  
   MXCertificate:string,
      /**  MXApprovalYear  */  
   MXApprovalYear:number,
      /**  MXCBB  */  
   MXCBB:string,
      /**  MXApprovalNum  */  
   MXApprovalNum:number,
      /**  MXOriginalStringTFD  */  
   MXOriginalStringTFD:string,
      /**  MXPaymentNum  */  
   MXPaymentNum:number,
      /**  MXPaidAs  */  
   MXPaidAs:string,
      /**  MXCertificateSN  */  
   MXCertificateSN:string,
      /**  MXOriginalAmount  */  
   MXOriginalAmount:number,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  MXOriginalDate  */  
   MXOriginalDate:string,
      /**  MXOriginalSeries  */  
   MXOriginalSeries:string,
      /**  MXOriginalFolio  */  
   MXOriginalFolio:string,
      /**  MXTaxRegime  */  
   MXTaxRegime:string,
      /**  MXOriginalString  */  
   MXOriginalString:string,
      /**  MXPaymentName  */  
   MXPaymentName:string,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  EInvStatus  */  
   EInvStatus:number,
      /**  EInvTimestamp  */  
   EInvTimestamp:string,
      /**  EInvUpdatedBy  */  
   EInvUpdatedBy:string,
      /**  EInvException  */  
   EInvException:string,
      /**  Flagged that this invoice has taxes which were necessary or is necessary now.  */  
   WithTaxConfirm:boolean,
      /**  UseAltBillToID  */  
   UseAltBillToID:boolean,
      /**  MXCancelledDate  */  
   MXCancelledDate:string,
      /**  Overpaid  */  
   Overpaid:boolean,
      /**  OrdExchangeRate  */  
   OrdExchangeRate:number,
      /**  PEAPPayNum  */  
   PEAPPayNum:number,
      /**  PEBankNumber  */  
   PEBankNumber:string,
      /**  PECharges  */  
   PECharges:number,
      /**  PECommissions  */  
   PECommissions:number,
      /**  PEDetTaxAmt  */  
   PEDetTaxAmt:number,
      /**  PEDetTaxCurrencyCode  */  
   PEDetTaxCurrencyCode:string,
      /**  PEDischargeAmt  */  
   PEDischargeAmt:number,
      /**  PEDischargeDate  */  
   PEDischargeDate:string,
      /**  PEInterest  */  
   PEInterest:number,
      /**  PENoPayPenalty  */  
   PENoPayPenalty:number,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   PESUNATDepAmt:number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   PESUNATDepDate:string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   PESUNATDepNum:string,
      /**  PEBOEPosted  */  
   PEBOEPosted:boolean,
      /**  DocPEInterest  */  
   DocPEInterest:number,
      /**  DocPECommissions  */  
   DocPECommissions:number,
      /**  DocPECharges  */  
   DocPECharges:number,
      /**  DocPENoPayPenalty  */  
   DocPENoPayPenalty:number,
      /**  DocPEDischargeAmt  */  
   DocPEDischargeAmt:number,
      /**  DocPEDetTaxAmt  */  
   DocPEDetTaxAmt:number,
      /**  Rpt1PEInterest  */  
   Rpt1PEInterest:number,
      /**  Rpt1PECommissions  */  
   Rpt1PECommissions:number,
      /**  Rpt1PECharges  */  
   Rpt1PECharges:number,
      /**  Rpt1PENoPayPenalty  */  
   Rpt1PENoPayPenalty:number,
      /**  Rpt1PEDischargeAmt  */  
   Rpt1PEDischargeAmt:number,
      /**  Rpt2PEInterest  */  
   Rpt2PEInterest:number,
      /**  Rpt2PECommissions  */  
   Rpt2PECommissions:number,
      /**  Rpt2PECharges  */  
   Rpt2PECharges:number,
      /**  Rpt2PENoPayPenalty  */  
   Rpt2PENoPayPenalty:number,
      /**  Rpt2PEDischargeAmt  */  
   Rpt2PEDischargeAmt:number,
      /**  Rpt3PEInterest  */  
   Rpt3PEInterest:number,
      /**  Rpt3PECommissions  */  
   Rpt3PECommissions:number,
      /**  Rpt3PECharges  */  
   Rpt3PECharges:number,
      /**  Rpt3PENoPayPenalty  */  
   Rpt3PENoPayPenalty:number,
      /**  Rpt3PEDischargeAmt  */  
   Rpt3PEDischargeAmt:number,
      /**  Our Supplier Code  */  
   OurSupplierCode:string,
      /**  PEGuaranteeName  */  
   PEGuaranteeName:string,
      /**  PEGuaranteeAddress1  */  
   PEGuaranteeAddress1:string,
      /**  PEGuaranteeAddress2  */  
   PEGuaranteeAddress2:string,
      /**  PEGuaranteeAddress3  */  
   PEGuaranteeAddress3:string,
      /**  PEGuaranteeCity  */  
   PEGuaranteeCity:string,
      /**  PEGuaranteeState  */  
   PEGuaranteeState:string,
      /**  PEGuaranteeZip  */  
   PEGuaranteeZip:string,
      /**  PEGuaranteeCountry  */  
   PEGuaranteeCountry:string,
      /**  PEGuaranteeTaxID  */  
   PEGuaranteeTaxID:string,
      /**  PEGuaranteePhoneNum  */  
   PEGuaranteePhoneNum:string,
      /**  PEBOEStatus  */  
   PEBOEStatus:string,
      /**  PEBOEIsMultiGen  */  
   PEBOEIsMultiGen:boolean,
      /**  PE Reference Document ID  */  
   PERefDocID:string,
      /**  PE Reason Code  */  
   PEReasonCode:string,
      /**  PE Reason Description  */  
   PEReasonDesc:string,
      /**  TW GUI Code Seller  */  
   TWGUIRegNumSeller:string,
      /**  TW GUI Code Buyer  */  
   TWGUIRegNumBuyer:string,
      /**  Document Name  */  
   TWGUIExportDocumentName:string,
      /**  Remarks  */  
   TWGUIExportRemarks:string,
      /**  Verification  */  
   TWGUIExportVerification:string,
      /**  PEDebitNoteReasonCode  */  
   PEDebitNoteReasonCode:string,
      /**  PEDebitNote  */  
   PEDebitNote:boolean,
      /**  MXPartPmt  */  
   MXPartPmt:boolean,
      /**  Tax Invoice Type  */  
   CNTaxInvoiceType:number,
      /**  MXExportOperationType  */  
   MXExportOperationType:string,
      /**  MXExportCustDocCode  */  
   MXExportCustDocCode:string,
      /**  MXExportCertOriginNum  */  
   MXExportCertOriginNum:string,
      /**  MXExportConfNum  */  
   MXExportConfNum:string,
      /**  MXExportCertOrigin  */  
   MXExportCertOrigin:boolean,
      /**  MXIncoterm  */  
   MXIncoterm:string,
      /**  AGDocConcept  */  
   AGDocConcept:number,
      /**  Electronic Invoice reference number  */  
   EInvRefNum:string,
      /**  Export document reference number  */  
   ExportDocRefNum:string,
      /**  Export document date  */  
   ExportDocDate:string,
      /**  Tax Transaction ID  */  
   INTaxTransactionID:string,
      /**  MXMovingReasonFlag  */  
   MXMovingReasonFlag:boolean,
      /**  MXMovingReason  */  
   MXMovingReason:string,
      /**  MXNumRegIdTrib  */  
   MXNumRegIdTrib:string,
      /**  MXResidenCountryNum  */  
   MXResidenCountryNum:number,
      /**  MXPurchaseType  */  
   MXPurchaseType:string,
      /**  MXConfirmationCode  */  
   MXConfirmationCode:string,
      /**  MXExternalCode  */  
   MXExternalCode:string,
      /**  This invoice was created via an integration with a third-party field service.  */  
   ServiceInvoice:boolean,
      /**  MXDomesticTransfer  */  
   MXDomesticTransfer:boolean,
      /**  MXCancellationMode  */  
   MXCancellationMode:string,
      /**  Shipping Port Code  */  
   INShippingPortCode:string,
      /**  Export Procedure  */  
   INExportProcedure:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  DigitalSignature  */  
   DigitalSignature:string,
      /**  SignedOn  */  
   SignedOn:string,
      /**  SignedBy  */  
   SignedBy:string,
      /**  FirstPrintDate  */  
   FirstPrintDate:string,
      /**  DocCopyNum  */  
   DocCopyNum:number,
      /**  DepositBalance  */  
   DepositBalance:number,
      /**  DocDepositBalance  */  
   DocDepositBalance:number,
      /**  Rpt1DepositBalance  */  
   Rpt1DepositBalance:number,
      /**  Rpt2DepositBalance  */  
   Rpt2DepositBalance:number,
      /**  Rpt3DepositBalance  */  
   Rpt3DepositBalance:number,
      /**  Quote number to which this invoice record is associated with.  */  
   QuoteNum:number,
      /**  The help desk case related to this invoice.  */  
   HDCaseNum:number,
      /**  Indicates that the credit hold was overridden for this invoice.  */  
   CreditOverride:boolean,
      /**  Description	Indicates that the credit hold was overridden for this invoice.	The date and time the user override the invoice credit hold.  */  
   CreditOverrideDate:string,
      /**  The user id that override the invoice credit hold.  */  
   CreditOverrideUserID:string,
      /**  Indicates the invoice is on credit hold.  Applicable to miscellaneous invoices only.  */  
   CreditHold:boolean,
      /**  Peru Electronic Invoice XML Type  */  
   PEXMLType:number,
      /**  COCreditMemoReasonCode  */  
   COCreditMemoReasonCode:string,
      /**  CODebitMemoReasonCode  */  
   CODebitMemoReasonCode:string,
      /**  COReasonDesc  */  
   COReasonDesc:string,
      /**  CODebitNote  */  
   CODebitNote:boolean,
      /**  PEDetractionTranNum  */  
   PEDetractionTranNum:number,
      /**  PEProductCode  */  
   PEProductCode:string,
      /**  PECollectionGroupID  */  
   PECollectionGroupID:string,
      /**  PE Caption Code  */  
   PECaptionCode:string,
      /**  PE Caption Code Description  */  
   PECaption:string,
      /**  PE Reference DocumentType 1  */  
   PERefDocumentType:string,
      /**  PE Reference Document Number 1  */  
   PERefDocumentNumber:string,
      /**  PE Detraction good or service code  */  
   PEDetrGoodServiceCode:string,
      /**  PE Reference DocumentType 2  */  
   PERefDocumentType2:string,
      /**  PE Reference DocumentType 3  */  
   PERefDocumentType3:string,
      /**  PE Reference DocumentType 4  */  
   PERefDocumentType4:string,
      /**  PE Reference DocumentType 5  */  
   PERefDocumentType5:string,
      /**  PE Reference Document Number 2  */  
   PERefDocumentNumber2:string,
      /**  PE Reference Document Number 3  */  
   PERefDocumentNumber3:string,
      /**  PE Reference Document Number 4  */  
   PERefDocumentNumber4:string,
      /**  PE Reference Document Number 5  */  
   PERefDocumentNumber5:string,
      /**  E-invoice  */  
   ELIEInvoice:boolean,
      /**  Status of E-invoice (1 - Open, 2 - Generated, 3 - Sent, 4 - Error).  */  
   ELIEInvStatus:number,
      /**  User Id of the person generated E-invoice.  */  
   ELIEInvUpdatedBy:string,
      /**  E-invoice error description.  */  
   ELIEInvException:string,
      /**  Date and Time of E-invoice generation.  */  
   ELIEInvUpdatedOn:string,
      /**  COOperType  */  
   COOperType:string,
      /**  Flag that indicates if the Invoice is for Central Collection.  */  
   CentralCollection:boolean,
      /**  Company that created this invoice.  */  
   CColChildCompany:string,
      /**  Central Collection company.  */  
   CColParentCompany:string,
      /**  Order number on the invoicing company.  */  
   CColOrderNum:number,
      /**  Invoice number on the invoicing company.  */  
   CColChildInvoiceNum:number,
      /**  Invoice number on central collection company  */  
   CColInvoiceNum:number,
      /**  Legal number on the invoicing company invoice.  */  
   CColChildLegalNumber:string,
      /**  Legal number on central collection company.  */  
   CColLegalNumber:string,
      /**  Invoice reference on the Invoicing Company.  */  
   CColInvoiceRef:number,
      /**  Invoice Balance in the Central Collection company.  */  
   CColInvBal:number,
      /**  Central Collection Doc Invoice Balance.  */  
   DocCColInvBal:number,
      /**  Invoice Amount on the Invoicing Company.  */  
   CColInvAmt:number,
      /**  Invoice Amount on the Invoicing Company.  */  
   DocCColInvAmt:number,
      /**  Rpt 1 Parent Invoice Balance  */  
   Rpt1CColInvBal:number,
      /**  Rpt 2 Parent Invoice Balance  */  
   Rpt2CColInvBal:number,
      /**  Rpt 3 Parent Invoice Balance  */  
   Rpt3CColInvBal:number,
      /**  Rpt 1 Child Invoice Amount  */  
   Rpt1CColInvAmt:number,
      /**  Rpt 2 Child Invoice Amount  */  
   Rpt2CColInvAmt:number,
      /**  Rpt 3 Child Invoice Amount  */  
   Rpt3CColInvAmt:number,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  User terminal name  */  
   ELIEInvTerminalName:string,
      /**  User terminal IP  */  
   ELIEInvTerminalIP:string,
      /**  GL Description  */  
   Description:string,
      /**  WithholdAcctToInterim  */  
   WithholdAcctToInterim:boolean,
      /**  Indicates if the Central Collection parent invoice is open.  */  
   CColOpenInvoice:boolean,
      /**  AGQRCodeData  */  
   AGQRCodeData:string,
      /**  Exempt Reason Code  */  
   ExemptReasonCode:string,
      /**  EInvoice ID  */  
   ELIEInvID:string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   CallNum:number,
      /**  this is a link to the service call line that this invoice is for.  Linetype = "CALL"  */  
   CallLine:number,
      /**  Associates the Call Line record back its linked jobnum  */  
   JobNum:string,
      /**  MXCancelReasonCode  */  
   MXCancelReasonCode:string,
      /**  MXSubstInvoiceNum  */  
   MXSubstInvoiceNum:number,
      /**  MXExportType  */  
   MXExportType:string,
      /**  MXGlobalInvoicePeriod  */  
   MXGlobalInvoicePeriod:string,
      /**  MXGlobalInvoiceMonth  */  
   MXGlobalInvoiceMonth:string,
      /**  ELIEInvServiceProviderStatus  */  
   ELIEInvServiceProviderStatus:number,
      /**  Incoterm Code  */  
   IncotermCode:string,
      /**  Incoterm Location  */  
   IncotermLocation:string,
      /**  CovenantDiscPercent  */  
   CovenantDiscPercent:number,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
      /**  Amount that will be applied to the BOE invoice  */  
   DocApplyAmt:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
   DocNetToBOE:number,
   Selected:boolean,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Amount that will be applied to the BOE invoice  */  
   ApplyAmt:number,
   NetToBOE:number,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  CSF Peru - Detractions Doc Tax amount  */  
   PEDocDetTaxAmt:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARBOEMultiGenTableset{
   ARBOEMultiGen:Erp_Tablesets_ARBOEMultiGenRow[],
   ARBOEMultiGenInvcs:Erp_Tablesets_ARBOEMultiGenInvcsRow[],
   ARBOEMultiGenSel:Erp_Tablesets_ARBOEMultiGenSelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GenerateBOEInvoices_input{
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}

export interface GenerateBOEInvoices_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
   outMessage:string,
   outAssignLN:boolean,
}
}

   /** Required : 
      @param inGroupID
   */  
export interface GetARBOEMultiGen_input{
      /**  The group id  */  
   inGroupID:string,
}

export interface GetARBOEMultiGen_output{
   returnObj:Erp_Tablesets_ARBOEMultiGenTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param ipInvoiceNum
      @param ipCurrCode
      @param ipRateGrpCode
      @param ipInputAmount
      @param ipInvoiceDate
      @param ipApplyDate
   */  
export interface GetConvertedAmount_input{
      /**  Invoice Number  */  
   ipInvoiceNum:number,
      /**  Currency Code  */  
   ipCurrCode:string,
      /**  Rate Group Code  */  
   ipRateGrpCode:string,
      /**  Amount to be converted  */  
   ipInputAmount:number,
      /**  Invoice date  */  
   ipInvoiceDate:string,
      /**  Apply date  */  
   ipApplyDate:string,
}

export interface GetConvertedAmount_output{
parameters : {
      /**  output parameters  */  
   ipAmount:number,
}
}

   /** Required : 
      @param whereClause
      @param ds
   */  
export interface GetInvcsForSelection_input{
      /**  Where clause for Cash Receipt.  */  
   whereClause:string,
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}

export interface GetInvcsForSelection_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

   /** Required : 
      @param ds
   */  
export interface RecalcTotalBOEAmount_input{
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}

export interface RecalcTotalBOEAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARBOEMultiGenTableset[],
}
}

