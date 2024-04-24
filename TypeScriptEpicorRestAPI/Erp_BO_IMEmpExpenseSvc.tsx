import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.IMEmpExpenseSvc
// Description: Business Object to handle: Add, Update, Delete of EmpExpense, EmpExpenseTax
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpExpenseSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpExpenseSvc/$metadata", {
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
   Summary: Invoke method AddIndirectEmpExpense
   Description: Add EmpExpense related tables
   OperationID: AddIndirectEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddIndirectEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddIndirectEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddIndirectEmpExpense(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpExpenseSvc/AddIndirectEmpExpense", {
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
      @param IMEmpExpenseTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param saveAddOnError
      @param imIntegrationKey
   */  
export interface AddIndirectEmpExpense_input{
   IMEmpExpenseTableset:Erp_Tablesets_IMEmpExpenseTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
   saveAddOnError:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset[],
}

export interface AddIndirectEmpExpense_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset[],
}
}

export interface Erp_Tablesets_IMEmpExpenseCommentRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The employee the expense comment record is for.  */  
   EmpID:string,
      /**  Internal identifier of the EmpExpense record.  This with EmpID links the comment to a specific EmpExpense record.  */  
   EmpExpenseNum:number,
      /**  Internal identifier of the comment record.  Used in conjunction with EmpExpenseNum to make the record unique.  */  
   CommentNum:number,
      /**   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  */  
   CommentType:string,
      /**  The comment text.  */  
   CommentText:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of  row in actual table  */  
   IntSysRowID:string,
      /**  Unique identifier of related integration record.  */  
   ExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMEmpExpenseRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The employee the expense record is for.  */  
   EmpID:string,
      /**  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  */  
   EmpExpenseNum:number,
      /**  The date of the expense.  */  
   ExpenseDate:string,
      /**  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   ClaimRef:string,
      /**  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  */  
   Indirect:boolean,
      /**  The payment method of the expense.  */  
   PMUID:number,
      /**  The number of units of this expense.  */  
   Units:number,
      /**  Rate per unit of the expense.  */  
   UnitRate:number,
      /**  The currency the expense occurred in.  */  
   ExpCurrencyCode:string,
      /**  The amount of the expense in the expense currency.  */  
   DocExpenseAmt:number,
      /**  Indicates if the expense amount includes tax.  */  
   TaxIncluded:boolean,
      /**  The total amount of the expense in the expense currency.  This value includes taxes.  */  
   DocTotalExpenseAmt:number,
      /**   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   ExpenseStatus:string,
      /**  The ap invoice number the expense was invoiced on.  */  
   InvoiceNum:string,
      /**  The miscellaneous charge code for this expense.  */  
   MiscCode:string,
      /**  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  */  
   TaxExempt:string,
      /**  Indicates if the expense is reimbursable.  */  
   Reimbursable:boolean,
      /**  Expense Comment  */  
   ExpCommentText:string,
      /**  The expense category.  */  
   ExpenseCategory:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ExpenseAutoSubmit  */  
   ExpenseAutoSubmit:boolean,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The IntQueID of the related IntQueIn  */  
   IntQueID:number,
      /**  Unique identifier of row in actual table.  */  
   IntSysRowID:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Unique identifier of related integration record. The value is  GUID.  */  
   ExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMEmpExpenseTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMEmpExpense:Erp_Tablesets_IMEmpExpenseRow[],
   IMEmpExpenseTax:Erp_Tablesets_IMEmpExpenseTaxRow[],
   IMEmpExpenseComment:Erp_Tablesets_IMEmpExpenseCommentRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMEmpExpenseTaxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The employee the expense record is for.  */  
   EmpID:string,
      /**  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  */  
   EmpExpenseNum:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Rate code  */  
   RateCode:string,
      /**   Used to allow a second tax record using the same tax code on an expense.  When the sales tax field EcAquisition is checked then 2 expense tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   ECAcquisitionSeq:number,
      /**  The reportable amount to the tax jurisdiction in the expense currency.  */  
   ExpReportableAmt:number,
      /**  Taxable Amount for this expense in the expense currency  */  
   ExpTaxableAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in the expense currency.  */  
   ExpTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Tax Rate Date  */  
   TaxRateDate:string,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
      /**  Unique identifier of related integration record. The value is a GUID  */  
   ExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMIntegrationKeyRow{
      /**  The master file which the integration is related to.  */  
   TableName:string,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMIntegrationKeyTableset{
   IMIntegrationKey:Erp_Tablesets_IMIntegrationKeyRow[],
   IMNaturalKeys:Erp_Tablesets_IMNaturalKeysRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMNaturalKeysRow{
   KeyValue:string,
   KeyColumn:string,
   Sequence:number,
   PrimaryKey:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IntQueInOutRow{
      /**  The unique key from IntQueIn or IntQueOut  */  
   IntQueID:number,
      /**  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  */  
   Action:string,
      /**  "I" for incoming or "O" for outgoing  */  
   IncomingOutgoing:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

