import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.APBOEMultiGenSvc
// Description: APBOEMultiGen object
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBOEMultiGenSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBOEMultiGenSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBOEMultiGenSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCodeDescList_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeBOEInvcAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBOEInvcAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBOEInvcAmount(requestBody:ChangeBOEInvcAmount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeBOEInvcAmount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBOEMultiGenSvc/ChangeBOEInvcAmount", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeBOEInvcAmount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeVendor
   Description: Update default information based on the vendor changing
   OperationID: ChangeVendor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendor(requestBody:ChangeVendor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeVendor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBOEMultiGenSvc/ChangeVendor", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeVendor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCurrency
   Description: Update default information based on the currency changing
   OperationID: ChangeCurrency
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrency(requestBody:ChangeCurrency_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCurrency_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBOEMultiGenSvc/ChangeCurrency", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeCurrency_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateAPBOEMultiGenInvcs
   Description: Create records in the APBOEMultiGenInvcs datatable.
   OperationID: CreateAPBOEMultiGenInvcs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateAPBOEMultiGenInvcs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateAPBOEMultiGenInvcs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateAPBOEMultiGenInvcs(requestBody:CreateAPBOEMultiGenInvcs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateAPBOEMultiGenInvcs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBOEMultiGenSvc/CreateAPBOEMultiGenInvcs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateAPBOEMultiGenInvcs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteAPBOEMultiGenInvcs
   Description: Delete a record in the APBOEMultiGenInvcs datatable.
   OperationID: DeleteAPBOEMultiGenInvcs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteAPBOEMultiGenInvcs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAPBOEMultiGenInvcs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteAPBOEMultiGenInvcs(requestBody:DeleteAPBOEMultiGenInvcs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteAPBOEMultiGenInvcs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBOEMultiGenSvc/DeleteAPBOEMultiGenInvcs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteAPBOEMultiGenInvcs_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateBOEInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateBOEInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateBOEInvoices(requestBody:GenerateBOEInvoices_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateBOEInvoices_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBOEMultiGenSvc/GenerateBOEInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GenerateBOEInvoices_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAPBOEMultiGen
   Description: Creates a temporary record to store information needed to create multiple
Bill of Exchange invoices.
   OperationID: GetAPBOEMultiGen
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAPBOEMultiGen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPBOEMultiGen_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPBOEMultiGen(requestBody:GetAPBOEMultiGen_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAPBOEMultiGen_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBOEMultiGenSvc/GetAPBOEMultiGen", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetAPBOEMultiGen_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInvcsForSelection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcsForSelection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvcsForSelection(requestBody:GetInvcsForSelection_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInvcsForSelection_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APBOEMultiGenSvc/GetInvcsForSelection", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetInvcsForSelection_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
   ds:Erp_Tablesets_APBOEMultiGenTableset[],
}

export interface ChangeBOEInvcAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBOEMultiGenTableset,
}
}

   /** Required : 
      @param currencyCode
      @param ds
   */  
export interface ChangeCurrency_input{
      /**  The currency code  */  
   currencyCode:string,
   ds:Erp_Tablesets_APBOEMultiGenTableset[],
}

export interface ChangeCurrency_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBOEMultiGenTableset,
}
}

   /** Required : 
      @param vendID
      @param ds
   */  
export interface ChangeVendor_input{
      /**  The vendor ID  */  
   vendID:string,
   ds:Erp_Tablesets_APBOEMultiGenTableset[],
}

export interface ChangeVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBOEMultiGenTableset,
}
}

   /** Required : 
      @param inCreateMethod
      @param ds
   */  
export interface CreateAPBOEMultiGenInvcs_input{
      /**  The create method: S - single M - multiple  */  
   inCreateMethod:string,
   ds:Erp_Tablesets_APBOEMultiGenTableset[],
}

export interface CreateAPBOEMultiGenInvcs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBOEMultiGenTableset,
}
}

   /** Required : 
      @param inBOESeq
      @param ds
   */  
export interface DeleteAPBOEMultiGenInvcs_input{
      /**  The sequence to delete  */  
   inBOESeq:number,
   ds:Erp_Tablesets_APBOEMultiGenTableset[],
}

export interface DeleteAPBOEMultiGenInvcs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBOEMultiGenTableset,
}
}

export interface Erp_Tablesets_APBOEMultiGenInvcsRow{
   BOEAmount:number,
   BOESeq:number,
   Company:string,
   CurrencyCode:string,
   DocBOEAmount:number,
   DueDate:string,
   GroupID:string,
   InvoiceNum:string,
   RateGrpCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APBOEMultiGenRow{
   AppliedAmt:number,
   Company:string,
   CurrDesc:string,
   CurrencyCode:string,
   CurrRateGrpDescription:string,
   DocAppliedAmt:number,
   DocTotalAmount:number,
   DocTotalDetrAmt:number,
   FirstDate:string,
   GroupID:string,
   NumToGenerate:number,
   Periodicity:string,
   RateGrpCode:string,
   TotalAmount:number,
   VendorID:string,
   VendorName:string,
   VendorNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APBOEMultiGenSelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this is an "open" Payable.  */  
   OpenPayable:boolean,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   InvoiceNum:string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   DebitMemo:boolean,
      /**  Invoice date.  */  
   InvoiceDate:string,
      /**  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   TaxAmt:number,
      /**  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  */  
   DocTaxAmt:number,
      /**  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  */  
   DiscountDate:string,
      /**  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DiscountAmt:number,
      /**  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DocDiscountAmt:number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDates:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   PayAmounts:string,
      /**  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   DocPayAmounts:string,
      /**  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  */  
   GLPosted:boolean,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  */  
   FiscalPeriod:number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   StartUp:boolean,
      /**  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  */  
   InvoiceRef:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Used to establish invoice comments about the overall invoice.  */  
   InvoiceComment:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  */  
   DocInvoiceVendorAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnpostedBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   DocUnpostedBal:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  */  
   InvoiceHeld:boolean,
      /**  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  */  
   PayHold:boolean,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   Description:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  */  
   REFPONum:number,
      /**  The Tax Region for this invoice.  */  
   TaxRegionCode:string,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Journal that invoice was posted to.  */  
   JournalCode:string,
      /**  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  */  
   UpdateTax:boolean,
      /**  For use by external G/L interfacing.  This field is sign flipped for debit memos.  */  
   InvoiceVendorAmt:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  External Identification of the Invoice.  */  
   ExternalID:string,
      /**  Allows user to control discount amount manually or automatically  */  
   FixedAmt:boolean,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefInvoiceNum:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceNum:string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   DepGainLoss:number,
      /**  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  */  
   CPay:boolean,
      /**  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  */  
   CPayLinked:boolean,
      /**  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  */  
   CPayLegalNumber:string,
      /**  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   CPayCheckNum:number,
      /**  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   CPayCheckDate:string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  */  
   CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  */  
   CPayDocInvoiceBal:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  */  
   GLControlType:string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  */  
   GLControlCode:string,
      /**  Reporting currency value of this field  */  
   Rpt1DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscountAmt:number,
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
   Rpt1InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt2PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt3PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnpostedBal:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt1CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt2CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt3CPayInvoiceBal:number,
      /**  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  */  
   AllowOverrideLI:boolean,
      /**  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  */  
   MatchedFromLI:boolean,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDiscDays:string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   PayDiscPer:string,
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
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PayDiscPartPay:boolean,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   PIPayment:string,
      /**  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden and Finland Localization Field - Banking Reference  */  
   SEBankRef:string,
      /**  Sweden and Finland Localization Field - Payment Code  */  
   SEPayCode:string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Indicates that this is pre-payment invoice.  */  
   PrePayment:boolean,
      /**  Letter of Credit ID.  */  
   APLOCID:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**   Taiwan Localization
Tax Amount Basis  */  
   GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in document currrency  */  
   DocGUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt1 currency  */  
   Rpt1GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt2 currency  */  
   Rpt2GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt3 currency  */  
   Rpt3GUIImportTaxBasis:number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   OvrDefTaxDate:boolean,
      /**  Linked flag  */  
   Linked:boolean,
      /**  The claim reference from the expense group that generated the invoice.  */  
   ClaimRef:string,
      /**  The employee from the group of expenses that created the invoice.  */  
   EmpID:string,
      /**  Indicates that Invoice has been selected for payment in a bankfile  */  
   InBankFile:boolean,
      /**  Credit Note Confirmation Date  */  
   CNConfirmDate:string,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Legal Number for the self assessment.  */  
   SelfLegalNumber:string,
      /**  Transaction Document Type for the self assessment.  */  
   SelfTranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**  Site Code  */  
   SiteCode:string,
      /**   Denmark Localization
Account Number  */  
   BankGiroAcctNbr:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Supplier Agent Name  */  
   SupAgentName:string,
      /**  Supplier Agent Tax Region Number  */  
   SupAgentTaxRegNo:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Card ID  */  
   CardID:string,
      /**  Card Holder Tax ID  */  
   CardHolderTaxID:string,
      /**  Card Member Name  */  
   CardMemberName:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Non Deductable VAT Amount  */  
   NonDeductVATAmt:number,
      /**  Non Deductable VAT Doc Amount  */  
   NonDeductVATDocAmt:number,
      /**  Non Deductable VAT Rpt1 Amount  */  
   NonDeductVATRpt1Amt:number,
      /**  Non Deductable VAT Rpt2 Amount  */  
   NonDeductVATRpt2Amt:number,
      /**  Non Deductable VAT Rpt3 Amount  */  
   NonDeductVATRpt3Amt:number,
      /**  Stores the number of the import document.  */  
   ImportNum:string,
      /**  Country of Import  */  
   ImportedFrom:string,
      /**  Date of import.  */  
   ImportedDate:string,
      /**   Indicates that this is Advanced Tax invoice received from
supplier  */  
   AdvTaxInv:boolean,
      /**   Indicates that the tax is included in the unit price
for this AP Invoice  */  
   InPrice:boolean,
      /**  Transaction Document Type ID  */  
   TranDocTypeID:string,
      /**  Reserved for Development - Integer  */  
   DevInt1:number,
      /**  Reserved for Development - Integer  */  
   DevInt2:number,
      /**  Reserved for development - decimal  */  
   DevDec1:number,
      /**  Reserved for development - decimal  */  
   DevDec2:number,
      /**  Reserved for development - decimal  */  
   DevDec3:number,
      /**  Reserved for development - decimal  */  
   DevDec4:number,
      /**  In case of Tax Inclusive Pricing if system-calculated Header related taxes are changed/deleted/added  by the user - this field is set to true by the system.  */  
   DevLog1:boolean,
      /**  Reserved for development - logical  */  
   DevLog2:boolean,
      /**  Assigned as "I" when Recurring Invoice has Inactive status.  */  
   DevChar1:string,
      /**  Reserved for development - character  */  
   DevChar2:string,
      /**  Reserved for development - date  */  
   DevDate1:string,
      /**  Reserved for development - date  */  
   DevDate2:string,
      /**  PaymentNumber  */  
   PaymentNumber:string,
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
      /**  IsRecurring  */  
   IsRecurring:boolean,
      /**  InvoiceNumList  */  
   InvoiceNumList:string,
      /**  IsMaxValue  */  
   IsMaxValue:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHISRCodeLine  */  
   CHISRCodeLine:string,
      /**  DMReason  */  
   DMReason:string,
      /**  UrgentPayment  */  
   UrgentPayment:boolean,
      /**  AGDocPageNum  */  
   AGDocPageNum:string,
      /**  AGCAICAEMark  */  
   AGCAICAEMark:string,
      /**  AGCAICAENum  */  
   AGCAICAENum:string,
      /**  AGCAICAEExpirationDate  */  
   AGCAICAEExpirationDate:string,
      /**  AGAvTaxCreditFlag  */  
   AGAvTaxCreditFlag:boolean,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGCustomsClearanceNum  */  
   AGCustomsClearanceNum:string,
      /**  AGCustomsCode  */  
   AGCustomsCode:string,
      /**  AGDestinationCode  */  
   AGDestinationCode:string,
      /**  Header Number  */  
   HeadNum:number,
      /**  TranType  */  
   TranType:string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   TaxSvcID:string,
      /**  TWDeclareYear  */  
   TWDeclareYear:number,
      /**  TWDeclarePeriod  */  
   TWDeclarePeriod:number,
      /**  AP Checking Group ID  */  
   APChkGrpID:string,
      /**  Invoice Type  */  
   InvoiceType:string,
      /**  Indicates a computational cost for the invoice  */  
   PEComputationalCost:string,
      /**  Referenced By BOE  */  
   ReferencedByBOE:string,
      /**  DUA Reference Number used on Peru Localiation  */  
   PEDUARefNum:string,
      /**  CustomsNumber  */  
   CustomsNumber:string,
      /**  ReceivedDate  */  
   ReceivedDate:string,
      /**  CustOverride  */  
   CustOverride:number,
      /**  Invoice Number of Invoice Pre-Payment which should be automatically applied to this one during posting process.  */  
   PrePaymentNum:string,
      /**  Pre-Payment amount in Base Currency.  */  
   PrePaymentAmt:number,
      /**  Pre-Payment amount in Document Currency.  */  
   DocPrePaymentAmt:number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   Rpt1PrePaymentAmt:number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   Rpt2PrePaymentAmt:number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   Rpt3PrePaymentAmt:number,
      /**  CSF Peru - AP Payment Number  */  
   PEAPPayNum:number,
      /**  SCF Peru - Detractions Tax Amount  */  
   PEDetTaxAmt:number,
      /**  Peru Detraction Tax Currency Code  */  
   PEDetTaxCurrencyCode:string,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   PESUNATDepAmt:number,
      /**  Peru Document SUNAT Deposit Amount  */  
   DocPESUNATDepAmt:number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   PESUNATDepDate:string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   PESUNATDepNum:string,
      /**  SUNAT Reference Number. Once a payment is made, the SUNAT returns a reference number used as the receipt number for the payment.  */  
   PESUNATNum:string,
      /**  Document Tax Amount used in Peru detractions  */  
   DocPEDetTaxAmt:number,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  PEBOEIsMultiGen  */  
   PEBOEIsMultiGen:boolean,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  PrePayHeadNum  */  
   PrePayHeadNum:number,
      /**  MXRetentionCode  */  
   MXRetentionCode:string,
      /**  PE Reference Document ID  */  
   PERefDocID:string,
      /**  PE Reason Code  */  
   PEReasonCode:string,
      /**  PE Reason Description  */  
   PEReasonDesc:string,
      /**  Malaysia Import Declaration Number  */  
   MYImportNum:string,
      /**  TW GUI Code Seller  */  
   TWGUIRegNumSeller:string,
      /**  TW GUI Code Buyer  */  
   TWGUIRegNumBuyer:string,
      /**  MXTARCode  */  
   MXTARCode:string,
      /**  Flag that indicates if the invoice is a GRNI document.  */  
   GRNIClearing:boolean,
      /**  CSF Peru - Fiscal Credit Operation Status  */  
   PEFiscalCreditOperStatus:number,
      /**  CSF Peru - International Tax agreement  */  
   PEInternatTaxAgr:string,
      /**  CSF Peru - Rent type  */  
   PERentType:string,
      /**  CSF Peru - Purchase  type  */  
   PEPurchaseType:string,
      /**  TH Reference Invoice Num  */  
   THRefInvoiceNum:string,
      /**  TH Reference Vendor Num  */  
   THRefVendorNum:number,
      /**  Day when a company sums up accounts payable for supplier  */  
   JPSummarizationDate:string,
      /**  Date of a Payment Statement  */  
   JPBillingDate:string,
      /**  Legal Number of Payment Statement  */  
   JPBillingNumber:string,
      /**  SelfInvoice  */  
   SelfInvoice:boolean,
      /**  Printed  */  
   Printed:boolean,
      /**  PurPoint  */  
   PurPoint:string,
      /**  PLInvoiceReference  */  
   PLInvoiceReference:string,
      /**  INPortCode  */  
   INPortCode:string,
      /**  Indicates which invoice number has cancelled this invoice.  */  
   RefCancelledby:string,
      /**  Indicates if this invoice is a cancellation invoice.  */  
   CancellationInv:boolean,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  WithholdAcctToInterim  */  
   WithholdAcctToInterim:boolean,
      /**  APTaxRoundOption  */  
   APTaxRoundOption:number,
      /**  Source Plant used for multi site GL  */  
   SourcePlant:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
      /**  CHQRIBAN  */  
   CHQRIBAN:string,
      /**  CHQRReference  */  
   CHQRReference:string,
      /**  Set to True for any invoice that is created via EDI  */  
   EDIInvoice:boolean,
   Selected:boolean,
   DocNetToBOE:number,
   NetToBOE:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APBOEMultiGenTableset{
   APBOEMultiGen:Erp_Tablesets_APBOEMultiGenRow[],
   APBOEMultiGenInvcs:Erp_Tablesets_APBOEMultiGenInvcsRow[],
   APBOEMultiGenSel:Erp_Tablesets_APBOEMultiGenSelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GenerateBOEInvoices_input{
   ds:Erp_Tablesets_APBOEMultiGenTableset[],
}

export interface GenerateBOEInvoices_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBOEMultiGenTableset,
   outMessage:string,
   opAssignLn:boolean,
}
}

   /** Required : 
      @param inGroupID
   */  
export interface GetAPBOEMultiGen_input{
      /**  The group id  */  
   inGroupID:string,
}

export interface GetAPBOEMultiGen_output{
   returnObj:Erp_Tablesets_APBOEMultiGenTableset[],
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
      @param whereClause
      @param ds
   */  
export interface GetInvcsForSelection_input{
      /**  Where clause for Cash Receipt.  */  
   whereClause:string,
   ds:Erp_Tablesets_APBOEMultiGenTableset[],
}

export interface GetInvcsForSelection_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APBOEMultiGenTableset,
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

