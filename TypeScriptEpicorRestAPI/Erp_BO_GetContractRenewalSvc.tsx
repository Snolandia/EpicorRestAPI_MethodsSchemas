import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.GetContractRenewalSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/$metadata", {
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
   Summary: Invoke method ExpireDate
   Description: ExpireDate .
   OperationID: ExpireDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpireDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpireDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExpireDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/ExpireDate", {
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
   Summary: Invoke method BuildContractRenewalList
   Description: This method returns three possible lists of selected Contract (FSContHd) and/or
Renewal (FSRenewal) records.  This should be called to return a list containing the
key fields of selected records. Since each record has two key fields the list
could potentially exceed the maximum allowed length of characters.  To avoid
this runtime error, the list will be split into three lists if needed.
   OperationID: BuildContractRenewalList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildContractRenewalList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildContractRenewalList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildContractRenewalList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/BuildContractRenewalList", {
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
   Summary: Invoke method BuildContractRenewalListFromList
   Description: This method returns three possible lists of selected Contract (FSContHd) and/or
Renewal (FSRenewal) records.  This should be called to return a list containing the
key fields of selected records. Since each record has two key fields the list
could potentially exceed the maximum allowed length of characters.  To avoid
this runtime error, the list will be split into three lists if needed.
This method  created to call from Kinetic UI
   OperationID: BuildContractRenewalListFromList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildContractRenewalListFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildContractRenewalListFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildContractRenewalListFromList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/BuildContractRenewalListFromList", {
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
   Summary: Invoke method GetRowsCustom
   Description: This methods will return all Contract Renewal records (copy of GetRenewal method)
that meet the selection criteria.  This method will try
to mirror functionality of the base GetRows method and it called from Kinetic UI Proc
RenewContracts when user searches for the contract renewal
   OperationID: Get_GetRowsCustom
      @param ipCustList Desc: The where clause to restrict Customers   Required: True   Allow empty value : True
      @param ipTypeList Desc: The where clause to restrict Types   Required: True   Allow empty value : True
      @param ipExpireDate Desc: The where clause to restrict Date   Required: True   Allow empty value : True
      @param pageSize Desc: The page size, used only for UI adaptor   Required: True
      @param absolutePage Desc: The absolute page, used only for the UI adaptor   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsCustom(ipCustList:string, ipTypeList:string, ipExpireDate:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ipCustList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipCustList=" + ipCustList
   }
   if(typeof ipTypeList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipTypeList=" + ipTypeList
   }
   if(typeof ipExpireDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipExpireDate=" + ipExpireDate
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/GetRowsCustom" + params, {
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
   Summary: Invoke method GetRenewals
   Description: This method returns the ttContractRenewal dataset consisting of expired or soon to expire
contracts (FSContHd) and renewals (FSRenewal) mixed records with some calculated columns added.
   OperationID: GetRenewals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRenewals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRenewals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRenewals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetContractRenewalSvc/GetRenewals", {
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
      @param ipContRenewMainList
   */  
export interface BuildContractRenewalListFromList_input{
      /**  The main listof selected Contract/Renewal records  */  
   ipContRenewMainList:string,
}

export interface BuildContractRenewalListFromList_output{
parameters : {
      /**  output parameters  */  
   opContRenewList1:string,
   opContRenewList2:string,
   opContRenewList3:string,
}
}

   /** Required : 
      @param ds
   */  
export interface BuildContractRenewalList_input{
   ds:Erp_Tablesets_GetContractRenewalTableset[],
}

export interface BuildContractRenewalList_output{
parameters : {
      /**  output parameters  */  
   opContRenewList1:string,
   opContRenewList2:string,
   opContRenewList3:string,
   ds:Erp_Tablesets_GetContractRenewalTableset[],
}
}

export interface Erp_Tablesets_ContractRenewalRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   ContractNum:number,
      /**  Indicates if the renwal will automatically generate a quote.  */  
   QuotedRenewal:boolean,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates the Quote has been accepted.  */  
   QuoteAccepted:boolean,
      /**  This is the contract code assigned to the renewal.  */  
   RenewalCode:string,
      /**  Defaulted from the service contract code.  Determines whether or not the renewal can be invoiced directly or if it must be shipped.  When yes the contract must be added to a sales order and then shipped prior to invoicing.  */  
   ShipRenewal:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Coverage  for material  */  
   Material:boolean,
      /**  Coverage for Labor  */  
   Labor:boolean,
      /**  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  */  
   Misc:boolean,
      /**  This contract covers on site visits  */  
   OnSite:boolean,
      /**  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  */  
   Invoiced:boolean,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that Ties the Contract record to a packing slip detail line  */  
   PackLine:number,
      /**  Indicates that Service Contract with this Code will generate recurring invoices.  */  
   RecurringInv:boolean,
      /**  Indicates the Tax Category for this record.  */  
   TaxCatID:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Indicates if the contract is ready to be invoiced.   This is only available when ShipContract = no.  */  
   ReadyToInvoice:boolean,
      /**  The Sales order that this contract is linked to.  */  
   OrderNum:number,
      /**  The line number of the sales order that this contract is linked to  */  
   OrderLine:number,
      /**  Duration of Contract  */  
   Duration:number,
      /**  Date when the renewal begins.  */  
   RenewEffDate:string,
      /**  Date the renewal ends.  */  
   RenewedUntil:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Flag to indicate if the record has been selected for the Hold/Unhold Amortization Periods process.  */  
   Selected:boolean,
   RenewalNbr:number,
   Modifier:string,
   CustID:string,
   ContractCode:string,
   ContractCodeDesc:string,
   RACodeDesc:string,
      /**  Total Contract Amount  */  
   ContractTotal:number,
      /**  Total Contract Amount  */  
   DocContractTotal:number,
   Rpt1ContractTotal:number,
   Rpt2ContractTotal:number,
   Rpt3ContractTotal:number,
      /**  Total Renewal Amount  */  
   RenewalTotal:number,
   DocRenewalTotal:number,
   Rpt1RenewalTotal:number,
   Rpt2RenewalTotal:number,
   Rpt3RenewalTotal:number,
   ExpireDate:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GetContractRenewalTableset{
   ContractRenewal:Erp_Tablesets_ContractRenewalRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ExpirationDate
      @param EffectiveDAte
      @param Duration
      @param modifier
   */  
export interface ExpireDate_input{
   ExpirationDate:string,
   EffectiveDAte:string,
   Duration:number,
   modifier:string,
}

export interface ExpireDate_output{
   returnObj:string,
}

   /** Required : 
      @param ipCustList
      @param ipTypeList
      @param ipExpireDate
      @param ds
   */  
export interface GetRenewals_input{
      /**  The Customer Number list to filter the records with  */  
   ipCustList:string,
      /**  The Contract Type list to filter the records with  */  
   ipTypeList:string,
      /**  The Expire Date filter  */  
   ipExpireDate:string,
   ds:Erp_Tablesets_GetContractRenewalTableset[],
}

export interface GetRenewals_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetContractRenewalTableset[],
}
}

   /** Required : 
      @param ipCustList
      @param ipTypeList
      @param ipExpireDate
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustom_input{
      /**  The where clause to restrict Customers  */  
   ipCustList:string,
      /**  The where clause to restrict Types  */  
   ipTypeList:string,
      /**  The where clause to restrict Date  */  
   ipExpireDate:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetRowsCustom_output{
   returnObj:Erp_Tablesets_GetContractRenewalTableset[],
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

