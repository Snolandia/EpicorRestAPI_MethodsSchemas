import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.BankPayMethodSearchSvc
// Description: this BO was created to be used on cboBankPayMethod.
and retrieve all payments methods marked as Manual(type = 0) fo PayMethod table and all payments
that are electronick payments that had been added to BankAcctID from BankPayMethod table.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankPayMethodSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankPayMethodSearchSvc/$metadata", {
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

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankPayMethodSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow)
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
   Summary: Invoke method GetRows
   Description: Returns paymethods by where clause
   OperationID: GetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankPayMethodSearchSvc/GetRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: Purpose: Returns valid PayMethods.
Parameters:
<param name="whereClause">Data Table Where Clause </param><param name="pageSize">Page Size</param><param name="absolutePage">Absolute Page</param><param name="morePages">More Pages flag</param><returns>BankPayMethodListDataSet dataset</returns>
Notes:
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankPayMethodSearchSvc/GetList", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PayMethodListRow[],
}

export interface Erp_Tablesets_PayMethodListRow{
      /**  Company  */  
   "Company":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Name of the payment method  */  
   "Name":string,
      /**   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  */  
   "Type":number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   "EFTHeadUID":number,
      /**  Payment Instrument Type  */  
   "PIType":string,
      /**  Payment Instrument Approve flag  */  
   "PIApprove":boolean,
      /**  System Row ID - GUID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_BankPayMethodSearchTableset{
   PayMethod:Erp_Tablesets_PayMethodRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PayMethodListRow{
      /**  Company  */  
   Company:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Name of the payment method  */  
   Name:string,
      /**   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  */  
   Type:number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   EFTHeadUID:number,
      /**  Payment Instrument Type  */  
   PIType:string,
      /**  Payment Instrument Approve flag  */  
   PIApprove:boolean,
      /**  System Row ID - GUID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PayMethodListTableset{
   PayMethodList:Erp_Tablesets_PayMethodListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PayMethodRow{
      /**  Company  */  
   Company:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Name of the payment method  */  
   Name:string,
      /**   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  */  
   Type:number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   EFTHeadUID:number,
      /**  This will be the default filename for the output file created by the electronic interface  */  
   OutputFile:string,
      /**  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  */  
   OnlyBankCurr:boolean,
      /**   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  */  
   PMSource:number,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   SummarizePerCustomer:boolean,
      /**  Default Payment Code  */  
   DefPayCode:string,
      /**  Auto Bank Reconciliation  */  
   AutoBankRec:boolean,
      /**  Sender Reference  */  
   SenderRef:string,
      /**  Registration Number  */  
   RegNum:string,
      /**  Checkbox to indicate test transmissions  */  
   Test:boolean,
      /**  Reimbursable  */  
   Reimbursable:boolean,
      /**  Inactive flag  */  
   Inactive:boolean,
      /**  Contains the overpayment threshold allowed for ar invoices in bank file import.  */  
   OverPayPct:number,
      /**  Contains the underpayment threshold allowed for ar invoices in bank file import.  */  
   UnderPayPct:number,
      /**  Payment Instrument Type  */  
   PIType:string,
      /**  Payment Instrument Generation Method  */  
   PIGenMethod:number,
      /**  Payment Instrument Approve flag  */  
   PIApprove:boolean,
      /**  Marks this PayMethod as global, available to be sent out to other companies.  */  
   GlobalPayMethod:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  System Row ID - GUID  */  
   SysRowID:string,
      /**  DepositSlips  */  
   DepositSlips:number,
      /**  IsPositiveBalance  */  
   IsPositiveBalance:boolean,
      /**  Specifies how the payments are processed in a bank - individually or in a batch  */  
   APGrouping:number,
      /**  When this check box is selected, the application uses identifiers generated via an EI program during processing  */  
   APIDGeneration:boolean,
      /**  Allows the user to specify how the receipts are processed in a bank - individually or in a batch  */  
   ARGrouping:number,
      /**  When this check box is selected, the application uses identifiers generated via an EI program during processing  */  
   ARIDGeneration:boolean,
      /**  Specify at what moment the application groups AR receipts in batches  */  
   ARIDTiming:number,
      /**  EFTDebitMemoHandlingCode  */  
   EFTDebitMemoHandlingCode:string,
      /**  EFTDebitMemoDueDate  */  
   EFTDebitMemoDueDate:string,
      /**  EFTProductNumDate  */  
   EFTProductNumDate:string,
      /**  EFTProductNumber  */  
   EFTProductNumber:number,
      /**  SEPO3Payment  */  
   SEPO3Payment:boolean,
      /**  SECrossBrdPayMethod  */  
   SECrossBrdPayMethod:string,
      /**  SECurrPocket  */  
   SECurrPocket:string,
      /**  SEErrorHandling  */  
   SEErrorHandling:string,
      /**  SEUseIBAN  */  
   SEUseIBAN:string,
      /**  SEPath  */  
   SEPath:string,
      /**  SECreateErrorLog  */  
   SECreateErrorLog:boolean,
      /**  SEFileForEachPayCurr  */  
   SEFileForEachPayCurr:boolean,
      /**  NOPaymentList  */  
   NOPaymentList:boolean,
      /**  NOTelepayPayment  */  
   NOTelepayPayment:boolean,
      /**  NOTelepayReply  */  
   NOTelepayReply:boolean,
      /**  DEFeeRule  */  
   DEFeeRule:string,
      /**  DESerialNum  */  
   DESerialNum:number,
      /**  DEStateNum  */  
   DEStateNum:string,
      /**  DELastUseDate  */  
   DELastUseDate:string,
      /**  MXPaidAs  */  
   MXPaidAs:string,
      /**  MXPaymentNum  */  
   MXPaymentNum:number,
      /**  MXTotalPayments  */  
   MXTotalPayments:number,
      /**  The field specifies the mexican type of the payment: 2 – Check, 3 – Transfer, 0 – Other  */  
   MXPaymentType:number,
      /**  MXSATCode  */  
   MXSATCode:string,
      /**  MXSATDesc  */  
   MXSATDesc:string,
      /**  PymtProposal  */  
   PymtProposal:boolean,
      /**  AutoCheckNum  */  
   AutoCheckNum:boolean,
      /**  EnterPymtTotal  */  
   EnterPymtTotal:boolean,
      /**  CheckNumSeq  */  
   CheckNumSeq:number,
      /**  Form 1099-K Transaction Type  */  
   US1099KTranType:string,
      /**  Form 1099-K Third Party Network Amount Threshold  */  
   US1099KAmtThreshold:number,
      /**  Form 1099-K Third Party Network Transaction Threshold  */  
   US1099KTranThreshold:number,
      /**  COPayForm  */  
   COPayForm:string,
      /**  COPayMethod  */  
   COPayMethod:string,
      /**  UNCL4461  */  
   TypeCode:string,
      /**  Indicates if the threshold fields are enabled  */  
   EnableThresholds:boolean,
   IsCZLocalization:boolean,
      /**  Shows a char representation of a PMSource: 0 = AP, 1 = AR.  */  
   PMSourceModule:string,
      /**  EnableAPInfo  */  
   EnableAPInfo:boolean,
   COPayMethodDesc:string,
   TypeDescription:string,
   BitFlag:number,
   EFTHeadName:string,
   EFTHeadType:number,
   PITypeDescription:string,
   XbSystELIEinvoice:boolean,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_PayMethodListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_BankPayMethodSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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

