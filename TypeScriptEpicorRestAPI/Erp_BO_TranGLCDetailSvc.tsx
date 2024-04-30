import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.TranGLCDetailSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranGLCDetailSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranGLCDetailSvc/$metadata", {
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
   Summary: Invoke method ParseValueInParametersToTranGLCKeys
   Description: Parse input ValueIn Parameters to TranGLC keys.
like1-like6, likeValue1-likeValue6 - data from CompoundKeys (or else) input arrays when from was opened from context menu.
   OperationID: ParseValueInParametersToTranGLCKeys
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ParseValueInParametersToTranGLCKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseValueInParametersToTranGLCKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ParseValueInParametersToTranGLCKeys(requestBody:ParseValueInParametersToTranGLCKeys_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ParseValueInParametersToTranGLCKeys_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranGLCDetailSvc/ParseValueInParametersToTranGLCKeys", {
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
         resolve(data as ParseValueInParametersToTranGLCKeys_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTransactionDetail
   Description: Purpose:  retrieve tracker data.
Parameters:
<param name="ipBookID">ipBookID</param><param name="ipDocumentType">ARInvoice, APInvoice, etc</param><param name="ipKey1">Key1</param><param name="ipKey2">Key2</param><param name="ipKey3">Key3</param><param name="ipKey4">Key4</param><param name="ipKey5">Key5</param><param name="ipKey6">Key6</param><param name="opMessage">returns informational messages to the user when no records are found.</param><param name="opNoData">if yes then no TranGLC records and no GLJrnDtl records were found.</param><param name="opNoGLPosting">Yes indicates there are not GL Postings for this document.</param><returns>TranGLC and GLJrnDtl data set</returns>
Notes:
   OperationID: GetTransactionDetail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTransactionDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransactionDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransactionDetail(requestBody:GetTransactionDetail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTransactionDetail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TranGLCDetailSvc/GetTransactionDetail", {
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
         resolve(data as GetTransactionDetail_output)
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
export interface Erp_Tablesets_TranGLCDetailTableset{
   TranGLC:Erp_Tablesets_TranGLCRow[],
   TranGLJrnDtl:Erp_Tablesets_TranGLJrnDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TranGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   TGLCTranNum:number,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Indicates if the user can update or delete this record.  */  
   UserCanModify:boolean,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Unique Identifier of the system GL Control Type.  */  
   SysGLControlType:string,
      /**  System generated GL Control Identifier.  */  
   SysGLControlCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   FiscalYear:number,
      /**  JournalCode of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Journal number of the related GLJrnDtl.  */  
   JournalNum:number,
      /**  JournalLine of the related GLJrnDtl.  */  
   JournalLine:number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   TranDate:string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   TranSource:string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborDtlSeq:number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysDate:string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysTime:number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   TranNum:number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   ARInvoiceNum:number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   TransAmt:number,
      /**  Invoice Line Number associated with this GL Journal  */  
   InvoiceLine:number,
      /**  The sequence number associated with this GL journal  */  
   SeqNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  BookCreditAmount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   RecordType:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  this field equals ABTUID which was created during posting  */  
   ABTUID:string,
      /**  Technical identifier.  */  
   RuleUID:number,
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
      /**  IsModifiedByUser  */  
   IsModifiedByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  MovementType  */  
   MovementType:string,
      /**  Plant  */  
   Plant:string,
      /**  AP Tran Number  */  
   APTranNo:number,
      /**  Indicates if the AP Transaction is voided  */  
   APTranVoided:boolean,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Bank Group ID  */  
   BankGroupID:string,
      /**  Bank Tran Number  */  
   BankTranNum:number,
      /**  Indicates if the Bank Transaction has been voided  */  
   BankTranVoided:boolean,
   BookCurrencyCode:string,
      /**  Cash Head Number  */  
   CashHeadNum:number,
      /**  Cash Head Group ID  */  
   CashHedGroup:string,
      /**  Cash Detail Invoice Reference  */  
   CashInvRef:number,
      /**  Chead Head Number  */  
   CheckHeadNum:number,
      /**  Indicates if the Check Header has been voided.  */  
   CheckHedVoided:boolean,
      /**  Container ID  */  
   ContainerID:number,
   DocumentText:string,
   DocumentType:string,
      /**  Used to display a context sensitive label for Key1.  This data is set on the server side and is translateable.  */  
   Key1Label:string,
      /**  Used to display a context sensitive label for Key2.  This data is set on the server side and is translateable.  */  
   Key2Label:string,
      /**  Used to display a context sensitive label for Key3.  This data is set on the server side and is translateable.  */  
   Key3Label:string,
      /**  Used to display a context sensitive label for Key4.  This data is set on the server side and is translateable.  */  
   Key4Label:string,
      /**  Used to display a context sensitive label for Key6.  This data is set on the server side and is translateable.  */  
   Key5Label:string,
      /**  Used to display a context sensitive label for Key6.  This data is set on the server side and is translateable.  */  
   Key6Label:string,
      /**  Purchase order receipt pack slip number  */  
   Packslip:string,
      /**  Purchase Order Line Number  */  
   POLine:number,
      /**  Purchase Order Number  */  
   PONum:number,
      /**  Purchase Order Release Number  */  
   PORelNum:number,
      /**  Purchase Point  */  
   PurPoint:string,
   RateCodeDesc:string,
   StatAmount:number,
   SupplierName:string,
      /**  The Taxable Amount if the current TranGLc record is related to the InvcTax or APInvTax tables.  */  
   TaxableAmt:number,
   TaxAmt:number,
   TaxCode:string,
   TaxCodeDesc:string,
      /**  The percent of the rate if current TranGLC record is related to the InvcTax or APInvTax tables  */  
   TaxRatePercent:number,
      /**  AP Tran head Number  */  
   APHeadNum:number,
   HideKey2:boolean,
   HideKey3:boolean,
   HideKey4:boolean,
   HideKey5:boolean,
   HideKey6:boolean,
   BitFlag:number,
   CurrencyCurrSymbol:string,
   CurrencyCurrName:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrDesc:string,
   CurrencyCurrencyID:string,
   FiscalCalendarDescription:string,
   GLAccountAccountDesc:string,
   GLAccountGLAcctDisp:string,
   GLAccountGLShortAcct:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
   InvoiceLineLineDesc:string,
   InvoiceNumTermsCode:string,
   InvoiceNumCardMemberName:string,
   JournalCodeJrnlDescription:string,
   StatUOMStatUOMDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TranGLJrnDtlRow{
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
      /**  The TranGLC transaction number this GLJrnDtl is associated with.  When transactions are summarized, it is possible for a GLJrnDtl to have multiple TranGLC records.  */  
   TGLCTranNum:number,
   StatAmount:number,
   BitFlag:number,
   DocCurrencyCurrName:string,
   DocCurrencyCurrencyID:string,
   DocCurrencyCurrDesc:string,
   DocCurrencyDocumentDesc:string,
   DocCurrencyCurrSymbol:string,
   FiscalCalendarDescription:string,
   StatUOMStatUOMDesc:string,
   TranGLToDetailAcctGLAcctDisp:string,
   TranGLToDetailAcctGLShortAcct:string,
   TranGLToDetailAcctAccountDesc:string,
   TranGLToGLAccountGLAcctDisp:string,
   TranGLToGLAccountAccountDesc:string,
   TranGLToGLAccountGLShortAcct:string,
   TranGLToJrnlCodeJrnlDescription:string,
   TranGLToSummaryAcctGLShortAcct:string,
   TranGLToSummaryAcctGLAcctDisp:string,
   TranGLToSummaryAcctAccountDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipBookID
      @param ipDocumentType
      @param ipKey1
      @param ipKey2
      @param ipKey3
      @param ipKey4
      @param ipKey5
      @param ipKey6
   */  
export interface GetTransactionDetail_input{
   ipBookID:string,
   ipDocumentType:string,
   ipKey1:string,
   ipKey2:string,
   ipKey3:string,
   ipKey4:string,
   ipKey5:string,
   ipKey6:string,
}

export interface GetTransactionDetail_output{
   returnObj:Erp_Tablesets_TranGLCDetailTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
   opNoData:boolean,
   opNoGLPosting:boolean,
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
      @param like1
      @param like2
      @param like3
      @param like4
      @param like5
      @param like6
      @param likeValue1
      @param likeValue2
      @param likeValue3
      @param likeValue4
      @param likeValue5
      @param likeValue6
   */  
export interface ParseValueInParametersToTranGLCKeys_input{
   like1:string,
   like2:string,
   like3:string,
   like4:string,
   like5:string,
   like6:string,
   likeValue1:string,
   likeValue2:string,
   likeValue3:string,
   likeValue4:string,
   likeValue5:string,
   likeValue6:string,
}

export interface ParseValueInParametersToTranGLCKeys_output{
parameters : {
      /**  output parameters  */  
   bookID:string,
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}
}

