import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.NaturalAcctCurrSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NaturalAcctCurrSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NaturalAcctCurrSearchSvc/$metadata", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NaturalAcctCurrSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NaturalAcctCurrSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NaturalAcctCurrSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NaturalAcctCurrSearchListRow)
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
   Summary: Invoke method GetList
   Description: Get Rows
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

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NaturalAcctCurrSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.NaturalAcctCurrSearchSvc/GetList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NaturalAcctCurrSearchListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NaturalAcctCurrSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_NaturalAcctCurrSearchListRow[],
}

export interface Erp_Tablesets_NaturalAcctCurrSearchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Description of the currency  */  
   "CurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "DocumentDesc":string,
      /**  Notes the about the Currency.  */  
   "Note":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrName":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyID":string,
      /**  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  */  
   "DecimalsGeneral":number,
      /**  Indicates if the currency is active  */  
   "Inactive":boolean,
      /**  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  */  
   "DecimalsPrice":number,
      /**  Can only maintain exchange rates for currencies with this flag checked  */  
   "MaintRate":boolean,
      /**  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  */  
   "DecimalsCost":number,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   "BaseCurr":boolean,
      /**  Define multiple that Unit Prices for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpUnitPrice":number,
      /**  Indicates if this is a reporting currency  */  
   "ReportCurr":boolean,
      /**  Define multiple that Unit Tax for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpUnitTax":number,
      /**  Define multiple that Extended Prices (total line amount) for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpExtPrice":number,
      /**  Define multiple that Extended Tax (total line tax) for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpExtTax":number,
      /**  Define multiple that Total amount for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpTotalAmt":number,
      /**  Determines whether or not this currency is shared between more than one company.  */  
   "GlobalCurr":boolean,
      /**  Define multiple that Total Tax amount for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpTotalTax":number,
      /**  Determines whether or not this currency record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Define the rule how Unit Price for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleUnitPrice":number,
      /**  Display factor for exchange rates  */  
   "ScaleFactor":number,
      /**  Define the rule how Unit Tax for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleUnitTax":number,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   "CountryNum":number,
      /**  Define the rule how Extended Prices (total line amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleExtPrice":number,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   "ReportCurrPos":number,
      /**  Define the rule how Extended Tax (total tax amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleExtTax":number,
      /**  Define the rule how total amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleTotalAmt":number,
      /**  Define the rule how total tax amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleTotalTax":number,
      /**  It used in AP Invoice, if the rounding amount remaining is less or equal to the tolerance, the remaining amount is automatically booked.  */  
   "RoundTolerance":number,
      /**  ISO unique identifier  */  
   "ISONumber":number,
      /**  Store ID for Credit Card Processing  */  
   "StoreID":string,
      /**  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpAnnualCharge":number,
      /**  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpPeriodCharge":number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleAnnualCharge":number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRulePeriodCharge":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Allowed":boolean,
   "Revalue":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_NaturalAcctCurrSearchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Description of the currency  */  
   CurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   DocumentDesc:string,
      /**  Notes the about the Currency.  */  
   Note:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrName:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyID:string,
      /**  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  */  
   DecimalsGeneral:number,
      /**  Indicates if the currency is active  */  
   Inactive:boolean,
      /**  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  */  
   DecimalsPrice:number,
      /**  Can only maintain exchange rates for currencies with this flag checked  */  
   MaintRate:boolean,
      /**  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  */  
   DecimalsCost:number,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   BaseCurr:boolean,
      /**  Define multiple that Unit Prices for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpUnitPrice:number,
      /**  Indicates if this is a reporting currency  */  
   ReportCurr:boolean,
      /**  Define multiple that Unit Tax for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpUnitTax:number,
      /**  Define multiple that Extended Prices (total line amount) for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpExtPrice:number,
      /**  Define multiple that Extended Tax (total line tax) for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpExtTax:number,
      /**  Define multiple that Total amount for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpTotalAmt:number,
      /**  Determines whether or not this currency is shared between more than one company.  */  
   GlobalCurr:boolean,
      /**  Define multiple that Total Tax amount for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpTotalTax:number,
      /**  Determines whether or not this currency record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Define the rule how Unit Price for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleUnitPrice:number,
      /**  Display factor for exchange rates  */  
   ScaleFactor:number,
      /**  Define the rule how Unit Tax for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleUnitTax:number,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Define the rule how Extended Prices (total line amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleExtPrice:number,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   ReportCurrPos:number,
      /**  Define the rule how Extended Tax (total tax amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleExtTax:number,
      /**  Define the rule how total amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleTotalAmt:number,
      /**  Define the rule how total tax amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleTotalTax:number,
      /**  It used in AP Invoice, if the rounding amount remaining is less or equal to the tolerance, the remaining amount is automatically booked.  */  
   RoundTolerance:number,
      /**  ISO unique identifier  */  
   ISONumber:number,
      /**  Store ID for Credit Card Processing  */  
   StoreID:string,
      /**  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpAnnualCharge:number,
      /**  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpPeriodCharge:number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleAnnualCharge:number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRulePeriodCharge:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Allowed:boolean,
   Revalue:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_NaturalAcctCurrSearchListTableset{
   NaturalAcctCurrSearchList:Erp_Tablesets_NaturalAcctCurrSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  Where Clause ExpressShip  */  
   whereClause:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_NaturalAcctCurrSearchListTableset[],
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

