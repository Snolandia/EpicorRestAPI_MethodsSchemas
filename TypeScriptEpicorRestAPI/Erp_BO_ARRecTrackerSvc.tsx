import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ARRecTrackerSvc
// Description: AR Rec Tracker
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/$metadata", {
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
   Summary: Invoke method GetSelectionDefaults
   Description: Get selection criteria defaults
   OperationID: GetSelectionDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectionDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectionDefaults(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSelectionDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/GetSelectionDefaults", {
          method: 'post',
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
         resolve(data as GetSelectionDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSubLedgerMovements
   Description: This method gets all the movements records for the range of dates
   OperationID: GetSubLedgerMovements
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSubLedgerMovements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSubLedgerMovements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSubLedgerMovements(requestBody:GetSubLedgerMovements_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSubLedgerMovements_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/GetSubLedgerMovements", {
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
         resolve(data as GetSubLedgerMovements_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGLMovements
   Description: This method gets all jounal records for the range of dates
   OperationID: GetGLMovements
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGLMovements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLMovements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLMovements(requestBody:GetGLMovements_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGLMovements_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/GetGLMovements", {
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
         resolve(data as GetGLMovements_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRecTotals
   Description: This method gets the totals for a group of glaccounts
   OperationID: GetRecTotals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRecTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRecTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRecTotals(requestBody:GetRecTotals_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRecTotals_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/GetRecTotals", {
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
         resolve(data as GetRecTotals_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllRecs
   Description: This method gets all records
   OperationID: GetAllRecs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAllRecs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllRecs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllRecs(requestBody:GetAllRecs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllRecs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/GetAllRecs", {
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
         resolve(data as GetAllRecs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDiffs
   Description: This method gets just the differences
   OperationID: GetDiffs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDiffs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDiffs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDiffs(requestBody:GetDiffs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDiffs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/GetDiffs", {
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
         resolve(data as GetDiffs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBookID
   Description: This method is called when the BookID is changed.
   OperationID: OnChangeBookID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBookID(requestBody:OnChangeBookID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBookID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARRecTrackerSvc/OnChangeBookID", {
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
         resolve(data as OnChangeBookID_output)
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
export interface Erp_Tablesets_ARMovementRow{
      /**  Company identifier  */  
   Company:string,
      /**  Transaction type for the movement record created (Invoice, Cash, Adjustment, etc.)  */  
   TranType:string,
      /**  Internal cash receipt Number for the related cash receipt record that generated the movement  */  
   HeadNum:number,
      /**  Invoice number that is impacted by the movement record  */  
   InvoiceNum:number,
      /**  Reference invoice or credit memo number that generated the movement record against the corresponding invoice  */  
   InvoiceRef:number,
      /**  Transaction reference for the movement record (Invoice number, Check number, etc.)  */  
   TranRef:string,
      /**  Unique integer for the movement transaction  */  
   MovementNum:number,
      /**  Apply date of the movement's corresponding transaction  */  
   TranDate:string,
      /**  Contains the Customer number associated with the transaction.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  Legal number of the invoice/document that is impacted by the movement record  */  
   LegalNum:string,
      /**  Legal number of the document that generated the movement record  */  
   TranLegalNumber:string,
      /**  Currency code of the document that generated the movement record  */  
   CurrencyCode:string,
      /**  Amount of the movement in base currency  */  
   TranAmt:number,
      /**  Amount of the movement in document currency  */  
   DocTranAmt:number,
      /**  Amount of the movement in first reporting currency if defined  */  
   Rpt1TranAmt:number,
      /**  Amount of the movement in second reporting currency if defined  */  
   Rpt2TranAmt:number,
      /**  Amount of the movement in third reporting currency if defined  */  
   Rpt3TranAmt:number,
      /**  Sales order number against which the movement is generated  */  
   OrderNum:number,
      /**  Sales order line against which the movement is generated  */  
   OrderLine:number,
      /**  Sales order release against which the movement is generated  */  
   OrderRelNum:number,
      /**  Subledger of the movement record to differentiate between receivables, deposits, advance bill, etc.  */  
   Subledger:string,
      /**  "R" for realized or "U" for unrealized gain/loss  */  
   GainLossType:string,
      /**  Indicates the movement record is posted  */  
   Posted:boolean,
      /**  Indicates the movement record has updated the ARBalance table.  If real time balance updates are not enabled, this field will remain false until the balance update process is run.  */  
   BalUpdated:boolean,
      /**  System date and time of the generated movements  */  
   CreateDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CustName:string,
   CustID:string,
   GLAcctDisp:string,
   JournalCode:string,
   JournalNum:number,
   JournalLine:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARRecAllRecsRow{
   BookCreditAmount:number,
   CurrencyCode:string,
   BookDebitAmount:number,
   CreditAmount:number,
   CustID:string,
   CustName:string,
   CustNum:number,
   DebitAmount:number,
   DifferenceAmt:number,
   DocTranAmt:number,
   GLAcctDisp:string,
   InvoiceNum:number,
   JournalCode:string,
   JournalLine:number,
   JournalNum:number,
   LegalNum:string,
   TranAmt:number,
   TranDate:string,
   TranLegalNum:string,
   TranRef:string,
   TranType:string,
   Rpt1TranAmt:number,
   Rpt2TranAmt:number,
   Rpt3TranAmt:number,
   MovementNum:number,
   GLDate:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   FiscalPeriod:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BookTranAmt:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARRecDiffsRow{
   CurrencyCode:string,
   BookCreditAmount:number,
   BookDebitAmount:number,
   CustID:string,
   CustName:string,
   CustNum:number,
   DifferenceAmt:number,
   DifferenceReason:string,
   GLAcctDisp:string,
   GLAmount:number,
   GLDate:string,
   GLMovementNum:number,
   InvoiceNum:number,
   JournalCode:string,
   JournalLine:number,
   JournalNum:number,
   LegalNum:string,
   MovementNum:number,
   TranDate:string,
   TranAmt:number,
   TranLegalNum:string,
   TranRef:string,
   TranType:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   FiscalPeriod:number,
   DocTranAmt:number,
   Rpt1TranAmt:number,
   Rpt2TranAmt:number,
   Rpt3TranAmt:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BookTranAmt:number,
   DocWithholdAmt:number,
      /**  Rpt1WithholdAmt  */  
   Rpt1WithholdAmt:number,
      /**  Rpt2WithholdAmt  */  
   Rpt2WithholdAmt:number,
      /**  Rpt3WithholdAmt  */  
   Rpt3WithholdAmt:number,
      /**  WithholdAmt  */  
   WithholdAmt:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARRecTotalsRow{
   BookID:string,
   CurrencyCode:string,
   GLAccount:string,
   GLClosingBal:number,
   GLMovements:number,
   GLOpenBal:number,
   SubGLClosingBal:number,
   SubGLMovements:number,
   SubGLOpenBal:number,
   VarClosingBal:number,
   VarMovements:number,
   VarOpenBal:number,
   DocSubGLOpenBal:number,
   Rpt1SubGLOpenBal:number,
   Rpt2SubGLOpenBal:number,
   Rpt3SubGLOpenBal:number,
   DocSubGLMovements:number,
   Rpt1SubGLMovements:number,
   Rpt2SubGLMovements:number,
   Rpt3SubGLMovements:number,
   Rpt2SubGLClosingBal:number,
   DocSubGLClosingBal:number,
   Rpt1SubGLClosingBal:number,
   Rpt3SubGLClosingBal:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARRecTrackerRow{
   BookID:string,
   COACode:string,
   FiscalCalendarID:string,
   FiscalPeriodEnd:number,
   FiscalPeriodStart:number,
   FiscalYear:number,
   FiscalYearSuffix:string,
   GLAccount:string,
   GLAccountDesc:string,
   SegValue1:string,
   SegValue10:string,
   SegValue11:string,
   SegValue12:string,
   SegValue13:string,
   SegValue14:string,
   SegValue15:string,
   SegValue16:string,
   SegValue17:string,
   SegValue18:string,
   SegValue19:string,
   SegValue2:string,
   SegValue20:string,
   SegValue3:string,
   SegValue4:string,
   SegValue5:string,
   SegValue6:string,
   SegValue7:string,
   SegValue8:string,
   SegValue9:string,
   CurrencyCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARRecTrackerTableset{
   ARRecTracker:Erp_Tablesets_ARRecTrackerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARRecTrackerTotTableset{
   ARMovement:Erp_Tablesets_ARMovementRow[],
   ARRecAllRecs:Erp_Tablesets_ARRecAllRecsRow[],
   ARRecDiffs:Erp_Tablesets_ARRecDiffsRow[],
   ARRecTotals:Erp_Tablesets_ARRecTotalsRow[],
   GLJrnDtl:Erp_Tablesets_GLJrnDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLJrnDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  */  
   JournalNum:number,
      /**  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  */  
   JournalLine:number,
      /**  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  */  
   Description:string,
      /**  Date for this journal transaction entry.  */  
   JEDate:string,
      /**  Fiscal period that this journal entry applies to.  */  
   FiscalPeriod:number,
      /**  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  User ID that posted this translation.  */  
   PostedBy:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  */  
   Posted:boolean,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   SourceModule:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   ARInvoiceNum:number,
      /**  BankAcctId of the BankAcct master that this check was drawn  against.  */  
   BankAcctID:string,
      /**  Check number.  */  
   CheckNum:number,
      /**  Cash Receipts reference field.  */  
   CRHeadNum:number,
      /**  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  */  
   Reverse:boolean,
      /**  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  */  
   BankTranNum:number,
      /**   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  */  
   BankSlip:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefType:string,
      /**  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  */  
   ExtRefCode:string,
      /**  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalNum:number,
      /**  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  */  
   GlbJournalLine:number,
      /**  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  */  
   GlbJournalCode:string,
      /**  Global Vendor number.  Used by Multi-Company Journal.  */  
   GlbVendorNum:number,
      /**  Global AP Invoice identifier.  Used by Multi-Company Journal.  */  
   GlbAPInvoiceNum:string,
      /**  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  */  
   MultiCompany:boolean,
      /**  Linked to a Multi-Company Journal.  */  
   Linked:boolean,
      /**  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  */  
   CommentText:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   GlbCompanyID:string,
      /**  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  */  
   GlbFiscalYear:number,
      /**  Fiscal period from the external company that this journal entry applies to.  */  
   GlbFiscalPeriod:number,
      /**  The data entry Group from the external company that the journal entry is assigned to.  */  
   GlbGroupID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   GLAccount:string,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   ExtGLAccount:string,
      /**  External Segment Value 1  */  
   ExtSegValue1:string,
      /**  External Segment Value 2  */  
   ExtSegValue2:string,
      /**  External Segment Value 3  */  
   ExtSegValue3:string,
      /**  External Segment Value 4  */  
   ExtSegValue4:string,
      /**  External Segment Value 5  */  
   ExtSegValue5:string,
      /**  External Segment Value 6  */  
   ExtSegValue6:string,
      /**  External Segment Value 7  */  
   ExtSegValue7:string,
      /**  External Segment Value 8  */  
   ExtSegValue8:string,
      /**  External Segment Value 9  */  
   ExtSegValue9:string,
      /**  External Segment Value 10  */  
   ExtSegValue10:string,
      /**  External Segment Value 11  */  
   ExtSegValue11:string,
      /**  External Segment Value 12  */  
   ExtSegValue12:string,
      /**  External Segment Value 13  */  
   ExtSegValue13:string,
      /**  External Segment Value 14  */  
   ExtSegValue14:string,
      /**  External Segment Value 15  */  
   ExtSegValue15:string,
      /**  External Segment Value 16  */  
   ExtSegValue16:string,
      /**  External Segment Value 17  */  
   ExtSegValue17:string,
      /**  External Segment Value 18  */  
   ExtSegValue18:string,
      /**  External Segment Value 19  */  
   ExtSegValue19:string,
      /**  External Segment Value 20  */  
   ExtSegValue20:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**  Legal Number of source document  */  
   LegalNumber:string,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   PerBalFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   TBFlag:boolean,
      /**  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  */  
   DailyBalFlag:boolean,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Fiscal year suffix.  */  
   GlbFiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   GlbFiscalCalendarID:string,
      /**  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  */  
   IntermediateProc:boolean,
      /**  Internal system calculated sequence number not inteneded for external use.  */  
   GenID:number,
      /**  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  */  
   SrcCompany:string,
      /**  Unique Book Identifier  This is the book that is being consolidated into a target book.  */  
   SrcBook:string,
      /**  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  */  
   SrcGLAccount:string,
      /**  Source Journal Code  */  
   SrcJrnlCode:string,
      /**  Source Journal Number  */  
   SrcJournalNum:number,
      /**  Source Journal Line  */  
   SrcJournalLine:number,
      /**   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  */  
   SrcType:string,
      /**  this field equas ABTUID which was created during posting  */  
   ABTUID:string,
      /**  This field shows Debit value of transaction  */  
   DebitAmount:number,
      /**  This field shows Credit value of transaction  */  
   CreditAmount:number,
      /**  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  */  
   BookDebitAmount:number,
      /**  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  */  
   BookCreditAmount:number,
      /**  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  */  
   ParentRUID:string,
      /**  if has reverse line  */  
   HasReverseLine:boolean,
      /**  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  */  
   BalanceAcct:string,
      /**  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  */  
   TrialAcct:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  This is the last allocation stamp that affected this GLJrnDtl.  */  
   AllocationStamp:string,
      /**  Identifies the allocation batch this journal entry was processed under.  */  
   BatchID:string,
      /**  This is the allocation id that processed this journal entry.  */  
   AllocID:string,
      /**  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  */  
   RunNbr:number,
      /**  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  */  
   AllocRunNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtNbr:number,
      /**  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  */  
   AllocTgtSeq:number,
      /**  External COA Code  */  
   ExtCOACode:string,
      /**  MatchCode is used to match two or more journal detail records together.  */  
   MatchCode:string,
      /**  MatchDate is set when the journal detail record is matched to other journal detail records.  */  
   MatchDate:string,
      /**  Indicates whether or not the transaction has been flagged as reconciled.  */  
   Reconciled:boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Journal Sequence Number  */  
   Sequence:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   CustNum:number,
      /**  CloseFiscalPeriod  */  
   CloseFiscalPeriod:number,
      /**  SourcePlant  */  
   SourcePlant:string,
      /**  Plant  */  
   Plant:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
      /**   Colombia Loc field            
This field is used as external calculated only.  */  
   COOneTimeDesc:string,
      /**   Colombia Loc field.           
This field is used as external calculated only.  */  
   COOneTimeID:string,
      /**  DEA Code  */  
   DEACodeDesc:string,
      /**  DEA End Date  */  
   DEAEndDate:string,
      /**  DEA Start Date  */  
   DEAStartDate:string,
      /**  Deferred Expense  */  
   DeferredExp:boolean,
      /**  DEA Distributed Amount  */  
   Distributed:number,
      /**  DEA Distributed Amount in Doc Currency  */  
   DocDistributed:number,
      /**  DEA Expense Amount in Doc Currency  */  
   DocExpense:number,
      /**  DEA Recognized Amount in Doc Currency  */  
   DocRecognized:number,
      /**  DEA Remaining Amount in Doc Currency  */  
   DocRemaining:number,
      /**  DEA Unrecognized Amount in Doc Currency  */  
   DocUnrecognized:number,
      /**  Flag to indicate if the MultiCompany check box needs to be enabled.  */  
   EnableMultiCompany:boolean,
      /**  DEA Expense Amount  */  
   Expense:number,
   ExtRefAcctChart:string,
   ExtRefAcctDept:string,
   ExtRefAcctDiv:string,
   ExtRefCodeStatus:string,
   GLAcctDisp:string,
      /**  External field used in Journal Tracker and Chart tracker. Journal Comments tab.  */  
   HeaderCommentText:string,
      /**  Manual GL Journal Line Reference.  */  
   LineReference:string,
      /**  Manual GL Journal Line Reference Holder.  */  
   LineReferenceHolder:string,
      /**  Manual GL Journal Line Reference Holder Name.  */  
   LineReferenceHolderName:string,
      /**  Manual GL Journal Line Reference Type.  */  
   LineReferenceType:string,
   MovementNum:number,
      /**  Apply Date of the Original Transaction  */  
   OrigApplyDate:string,
      /**  Journal line of the original transaction that was reversed.  */  
   OrigJrnlLine:number,
      /**  Journal number of the original transaction that was reversed.  */  
   OrigJrnlNbr:number,
      /**  Fiscal year of the original transaction that was reversed.  */  
   OrigJrnlYear:number,
      /**  Fiscal year suffix of the original transaction that was reversed.  */  
   OrigJrnlYearSuffix:string,
      /**  DEA Recognized Amount  */  
   Recognized:number,
   RefAcctChart:string,
   RefAcctDept:string,
   RefAcctDiv:string,
   RefCodeStatus:string,
      /**  DEA Remaining Amount  */  
   Remaining:number,
      /**  Apply date of the reversing transaction  */  
   RevApplyDate:string,
      /**  Journal line of the latest journal entry made to reverse a transaction.  */  
   RevJrnlLine:number,
      /**  Journal number of the latest journal entry made to reverse a transaction.  */  
   RevJrnlNbr:number,
      /**  Fiscal year of the latest journal entry made to reverse a transaction.  */  
   RevJrnlYear:number,
      /**  Fiscal year suffix of the latest journal entry made to reverse a transaction.  */  
   RevJrnlYearSuffix:string,
   StatAmount:number,
   TotCredit:number,
   TotDebit:number,
      /**  DEA Unrecognized Amount  */  
   Unrecognized:number,
   BookCurrencyCode:string,
   BookCurrencySymbol:string,
      /**  Description of the entity the journal detail is for  */  
   EntityDescription:string,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrName:string,
   CurrencyCurrencyID:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrDesc:string,
   FiscalCalDescription:string,
   GLAccountGLAcctDisp:string,
   GLAccountAccountDesc:string,
   GLAccountGLAccount:string,
   JournalCodeJrnlDescription:string,
   SrcGLAccountGLShortAcct:string,
   SrcGLAccountAccountDesc:string,
   SrcGLAccountGLAcctDisp:string,
   StatUOMStatUOMDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipBookID
      @param ipFiscalCalendarID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipStartPeriod
      @param ipEndPeriod
      @param ipGLAccount
      @param ds
   */  
export interface GetAllRecs_input{
      /**  Book ID  */  
   ipBookID:string,
      /**  Calendar  */  
   ipFiscalCalendarID:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   ipFiscalYearSuffix:string,
      /**  Period Start  */  
   ipStartPeriod:number,
      /**  Period End  */  
   ipEndPeriod:number,
      /**  GL Account  */  
   ipGLAccount:string,
   ds:Erp_Tablesets_ARRecTrackerTotTableset[],
}

export interface GetAllRecs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARRecTrackerTotTableset,
}
}

   /** Required : 
      @param ipBookID
      @param ipFiscalCalendarID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipStartPeriod
      @param ipEndPeriod
      @param ipGLAccount
      @param ds
   */  
export interface GetDiffs_input{
      /**  Book ID  */  
   ipBookID:string,
      /**  Calendar  */  
   ipFiscalCalendarID:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   ipFiscalYearSuffix:string,
      /**  Period Start  */  
   ipStartPeriod:number,
      /**  Period End  */  
   ipEndPeriod:number,
      /**  GL Account  */  
   ipGLAccount:string,
   ds:Erp_Tablesets_ARRecTrackerTotTableset[],
}

export interface GetDiffs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARRecTrackerTotTableset,
}
}

   /** Required : 
      @param ipBookID
      @param ipFiscalCalendarID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipStartPeriod
      @param ipEndPeriod
      @param ipGLAccount
      @param ds
   */  
export interface GetGLMovements_input{
      /**  Book ID  */  
   ipBookID:string,
      /**  Fiscal Calendar  */  
   ipFiscalCalendarID:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   ipFiscalYearSuffix:string,
      /**  Period Start  */  
   ipStartPeriod:number,
      /**  Period End  */  
   ipEndPeriod:number,
      /**  GL Account  */  
   ipGLAccount:string,
   ds:Erp_Tablesets_ARRecTrackerTotTableset[],
}

export interface GetGLMovements_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARRecTrackerTotTableset,
}
}

   /** Required : 
      @param ipBookID
      @param ipFiscalCalendarID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipStartPeriod
      @param ipEndPeriod
      @param ipGLAccount
      @param ds
   */  
export interface GetRecTotals_input{
      /**  Book ID  */  
   ipBookID:string,
      /**  Fiscal Calendar  */  
   ipFiscalCalendarID:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   ipFiscalYearSuffix:string,
      /**  Period Start  */  
   ipStartPeriod:number,
      /**  Period End  */  
   ipEndPeriod:number,
      /**  GL Account  */  
   ipGLAccount:string,
   ds:Erp_Tablesets_ARRecTrackerTotTableset[],
}

export interface GetRecTotals_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARRecTrackerTotTableset,
}
}

export interface GetSelectionDefaults_output{
   returnObj:Erp_Tablesets_ARRecTrackerTableset[],
}

   /** Required : 
      @param ipBookID
      @param ipFiscalCalendarID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipStartPeriod
      @param ipEndPeriod
      @param ipGLAccount
      @param ds
   */  
export interface GetSubLedgerMovements_input{
      /**  Book ID  */  
   ipBookID:string,
      /**  Fiscal Calendar  */  
   ipFiscalCalendarID:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   ipFiscalYearSuffix:string,
      /**  Period Start  */  
   ipStartPeriod:number,
      /**  Period End  */  
   ipEndPeriod:number,
      /**  GL Account  */  
   ipGLAccount:string,
   ds:Erp_Tablesets_ARRecTrackerTotTableset[],
}

export interface GetSubLedgerMovements_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARRecTrackerTotTableset,
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
      @param cInBookID
      @param ds
   */  
export interface OnChangeBookID_input{
      /**  Proposed BookID  */  
   cInBookID:string,
   ds:Erp_Tablesets_ARRecTrackerTableset[],
}

export interface OnChangeBookID_output{
   returnObj:Erp_Tablesets_ARRecTrackerTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARRecTrackerTableset,
}
}

