import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.DepSearchSvc
// Description: This object returns deposit inoices and payments for the particulat sales order.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DepSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DepSearchSvc/$metadata", {
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
   Summary: Invoke method GetDeposits
   Description: This method returns deposit inoices and payments for the particulat sales order.
   OperationID: GetDeposits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDeposits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeposits_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDeposits(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DepSearchSvc/GetDeposits", {
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
export interface Erp_Tablesets_AllocDepositTrkRow{
      /**  Company  */  
   Company:string,
   CurrencyCode:string,
      /**  "0 - Prepaid Invoiced Deposit   1 - Cash Deposit 2 - Reverse Cash Deposit"  */  
   PrePayType:number,
      /**  Deposit Invoice Number  */  
   DepInvoiceNum:number,
      /**  Group ID of deposit payment  */  
   DepGroupID:string,
      /**  Identification of Deposit Payment  */  
   DepHeadNum:number,
      /**  Apply Date of Deposit Invoice  */  
   DepApplyDate:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  "0 - Unrecognized               1 - Partial Recognized 2 - Full Recognized"  */  
   PrePayStatus:number,
      /**  Allocated Amount  */  
   DocAllocAmt:number,
   AllocAmt:number,
   Rpt1AllocAmt:number,
   Rpt2AllocAmt:number,
   Rpt3AllocAmt:number,
      /**  Allocated Balance  */  
   DocAllocBal:number,
   AllocBal:number,
   Rpt1AllocBal:number,
   Rpt2AllocBal:number,
   Rpt3AllocBal:number,
      /**  Total Tax Amount of Deposit  */  
   DocTaxAmt:number,
   TaxAmt:number,
   Rpt1TaxAmt:number,
   Rpt2TaxAmt:number,
   Rpt3TaxAmt:number,
      /**  Remaining Tax Amount of Deposit  */  
   DocAllocTaxBal:number,
   AllocTaxBal:number,
   Rpt1AllocTaxBal:number,
   Rpt2AllocTaxBal:number,
   Rpt3AllocTaxBal:number,
      /**  Shipment Invoice Number for which this Deposit is allocated  */  
   InvoiceNum:number,
   DepCheckRef:string,
      /**  Currency switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
      /**  Original Amt  */  
   DocOriginalAmt:number,
   OriginalAmt:number,
   Rpt1OriginalAmt:number,
   Rpt2OriginalAmt:number,
   Rpt3OriginalAmt:number,
      /**  Original Tax Amt  */  
   DocOriginalTaxAmt:number,
   OriginalTaxAmt:number,
   Rpt1OriginalTaxAmt:number,
   Rpt2OriginalTaxAmt:number,
   Rpt3OriginalTaxAmt:number,
   CustNum:number,
   LegalNumber:string,
   Reference:string,
      /**  IsDepCM to distinguish between Deposit Billing Invoices and Deposit Billing Credit Memos  */  
   IsDepCM:boolean,
   DepInvoiceDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DepSearchTableset{
   DepSearchTot:Erp_Tablesets_DepSearchTotRow[],
   AllocDepositTrk:Erp_Tablesets_AllocDepositTrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DepSearchTotRow{
   Company:string,
   OrderNum:number,
   CurrencyCode:string,
   AllocAmt:number,
   DocAllocAmt:number,
   Rpt1AllocAmt:number,
   Rpt2AllocAmt:number,
   Rpt3AllocAmt:number,
   AllocBal:number,
   DocAllocBal:number,
   Rpt1AllocBal:number,
   Rpt2AllocBal:number,
   Rpt3AllocBal:number,
   TaxAmt:number,
   DocTaxAmt:number,
   Rpt1TaxAmt:number,
   Rpt2TaxAmt:number,
   Rpt3TaxAmt:number,
   AllocTaxBal:number,
   DocAllocTaxBal:number,
   Rpt1AllocTaxBal:number,
   Rpt2AllocTaxBal:number,
   Rpt3AllocTaxBal:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipOrderNum
      @param ds
   */  
export interface GetDeposits_input{
      /**  Sales Order Number  */  
   ipOrderNum:number,
   ds:Erp_Tablesets_DepSearchTableset[],
}

export interface GetDeposits_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DepSearchTableset[],
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

