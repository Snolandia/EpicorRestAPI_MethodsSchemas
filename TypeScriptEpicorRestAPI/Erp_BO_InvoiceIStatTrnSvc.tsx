import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.InvoiceIStatTrnSvc
// Description: Intrastat entry for AP Invoices and AR Invoices
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/$metadata", {
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
   Summary: Invoke method APGetInvoiceIStatTrn
   Description: Gets the InvoiceIStatTrn record for an APInvDtl record.
   OperationID: APGetInvoiceIStatTrn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/APGetInvoiceIStatTrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/APGetInvoiceIStatTrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APGetInvoiceIStatTrn(requestBody:APGetInvoiceIStatTrn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<APGetInvoiceIStatTrn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/APGetInvoiceIStatTrn", {
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
         resolve(data as APGetInvoiceIStatTrn_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ARGetInvoiceIStatTrn
   Description: Gets the InvoiceIStatTrn record for an AR InvcDtl record.
   OperationID: ARGetInvoiceIStatTrn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ARGetInvoiceIStatTrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ARGetInvoiceIStatTrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARGetInvoiceIStatTrn(requestBody:ARGetInvoiceIStatTrn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ARGetInvoiceIStatTrn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/ARGetInvoiceIStatTrn", {
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
         resolve(data as ARGetInvoiceIStatTrn_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCommodityCode
   Description: Method to call when changing the commodity code.  Validates the code and
updates CommodityCodeDescription field for the code.
   OperationID: ChangeCommodityCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCommodityCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCommodityCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCommodityCode(requestBody:ChangeCommodityCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCommodityCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/ChangeCommodityCode", {
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
         resolve(data as ChangeCommodityCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFOB
   Description: Method to call when changing the FOB code.  Validates the code and
updates FOBDescription field for the code.
   OperationID: ChangeFOB
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFOB_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFOB_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFOB(requestBody:ChangeFOB_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFOB_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/ChangeFOB", {
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
         resolve(data as ChangeFOB_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipVia
   Description: Method to call when changing the ship via code.  Validates the code and
updates ShipViaDescription field for the code.
   OperationID: ChangeShipVia
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeShipVia_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipVia_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipVia(requestBody:ChangeShipVia_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeShipVia_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/ChangeShipVia", {
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
         resolve(data as ChangeShipVia_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateIStatTrn
   Description: Updates/creates the IStatTrn record.
   OperationID: UpdateIStatTrn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateIStatTrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateIStatTrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateIStatTrn(requestBody:UpdateIStatTrn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateIStatTrn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/UpdateIStatTrn", {
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
         resolve(data as UpdateIStatTrn_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFlowList
   Description: Returns the Flow List.
   OperationID: GetFlowList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFlowList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFlowList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFlowList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvoiceIStatTrnSvc/GetFlowList", {
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
         resolve(data as GetFlowList_output)
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
      @param InVendorNum
      @param InInvoiceNum
      @param InInvoiceLine
      @param forTracker
   */  
export interface APGetInvoiceIStatTrn_input{
      /**  The vendor number of the invoice detail line  */  
   InVendorNum:number,
      /**  The invoice number of the invoice detail line  */  
   InInvoiceNum:string,
      /**  The line number of the invoice detail line  */  
   InInvoiceLine:number,
      /**  This flag indicates that this function is called for Tracker  */  
   forTracker:boolean,
}

export interface APGetInvoiceIStatTrn_output{
   returnObj:Erp_Tablesets_InvoiceIStatTrnTableset[],
}

   /** Required : 
      @param InInvoiceNum
      @param InInvoiceLine
      @param forTracker
   */  
export interface ARGetInvoiceIStatTrn_input{
      /**  The invoice number of the invoice detail line  */  
   InInvoiceNum:number,
      /**  The line number of the invoice detail line  */  
   InInvoiceLine:number,
      /**  This flag indicates that this function is called for Tracker  */  
   forTracker:boolean,
}

export interface ARGetInvoiceIStatTrn_output{
   returnObj:Erp_Tablesets_InvoiceIStatTrnTableset[],
}

   /** Required : 
      @param ProposedCommodityCode
      @param ds
   */  
export interface ChangeCommodityCode_input{
      /**  The proposed commodity code  */  
   ProposedCommodityCode:string,
   ds:Erp_Tablesets_InvoiceIStatTrnTableset[],
}

export interface ChangeCommodityCode_output{
parameters : {
      /**  output parameters  */  
   cErrMessage:string,
   ds:Erp_Tablesets_InvoiceIStatTrnTableset,
}
}

   /** Required : 
      @param ProposedFOB
      @param ds
   */  
export interface ChangeFOB_input{
      /**  The proposed FOB code  */  
   ProposedFOB:string,
   ds:Erp_Tablesets_InvoiceIStatTrnTableset[],
}

export interface ChangeFOB_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvoiceIStatTrnTableset,
}
}

   /** Required : 
      @param ProposedShipViaCode
      @param ds
   */  
export interface ChangeShipVia_input{
      /**  The proposed ship via code  */  
   ProposedShipViaCode:string,
   ds:Erp_Tablesets_InvoiceIStatTrnTableset[],
}

export interface ChangeShipVia_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvoiceIStatTrnTableset,
}
}

export interface Erp_Tablesets_IStatTrnRow{
      /**  Indicates whether the transaction is an "Arrival" (receipt) or "Dispatch" (shipment) of goods.  */  
   Flow:string,
      /**  Depending on the ISSyst.PeriodFormat settings, this field contains the period in which this transaction was executed.  */  
   Period:string,
      /**  Harmonized System goods classification code. The Commodity Code field must be valid in the ICommCode (formerly called IStatGrp) master file.  */  
   CommodityCode:string,
      /**  Value of transported goods excluding taxes but including miscellaneous charges.  */  
   Amount:number,
      /**  Delivery terms.  */  
   Terms:string,
      /**  Indicates the purpose of the transaction: Change of ownership, goods for subcontract job...  */  
   TransactionType:string,
      /**  Weight  */  
   Weight:number,
      /**  Country of Consignment/Destination. This field contains the Intrastat Code from the Country table.  */  
   ISCountryCode:string,
      /**  Intrastat code for method of transportation. The value comes from the IStatCode field from the ShipVia record.  */  
   ISShipViaCode:string,
      /**  Area/city code from where goods cross the border.  */  
   BorderCrossing:string,
      /**  Indicates if there is a non-standard type of transaction. (for example, goods imported and immediately exported again)  */  
   FlowSpec:string,
      /**  Currency indicator. Primarily used to cover the transitional period for the Euro.  */  
   ISCurrency:string,
      /**  Description of the Commodity Code or the Detail line depending on the value of the ISSyst.DescType field.  */  
   Description:string,
      /**  When the RequiresUM field in the IStatGrp is set, this field contains the quantity part for the UM for this Commodity Code.  */  
   SuppUnits:number,
      /**  Company Identifier.  */  
   Company:string,
      /**   Indicates the module that created Intrastat transaction.  This is assigned by the system.
Values can be; AR, AP or M (Manual Entry)  */  
   SourceModule:string,
      /**  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  */  
   InvoiceNum:string,
      /**  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  */  
   InvoiceLine:number,
      /**  Posted Flag  */  
   Posted:boolean,
      /**  VendorNum duplicated from the corresponding APInvDtl record.  */  
   VendorNum:number,
      /**   Indicates the type of document.  Yes = Credit/Debit Memo No = Regular AR/AP Invoice. This value can't be changed after the record has been created.
Credit/Debit memos affect the way amounts are displayed in theIntrastat reports. They will always be stored with a positive sign but will be displayed as a negative.  */  
   MemoFlag:boolean,
      /**  Contains the key value of the record in the "ShipVia" table.  */  
   ShipViaCode:string,
      /**  The code for the FOB policy.  */  
   FOB:string,
      /**  Optional field used to record the customer/vendor State Tax Identification number.  */  
   TaxID:string,
      /**  Value of transported goods excluding taxes and miscellaneous charges.  */  
   InvAmount:number,
      /**  Transaction Date  */  
   TransDate:string,
      /**  Not Reported Flag  */  
   NotReported:boolean,
      /**  Intrastat Region  */  
   ISRegion:string,
      /**  This field contains the Intrastat Country of Origin Code from the Country table.  */  
   ISOrigCountry:string,
      /**  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  */  
   IntCommCode:string,
      /**  Free form stamp to indicate the record has been reported to the authorities.  */  
   StampID:string,
      /**  SeqNum  */  
   SeqNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CommentText  */  
   CommentText:string,
      /**  European Union integrated tariff.  */  
   TaricCode:string,
      /**  European Union preference.  */  
   EUPreference:string,
      /**  Extra trade transaction indicator.  */  
   ExtraTrade:boolean,
      /**  Commodity flow refers to the nature of a (cross-border) movement of goods.  */  
   CommodityFlow:string,
      /**  Indicates which requested procedure and preceding procedure applies to the customs declaration.  */  
   CustomsProcedure:string,
      /**  The country where the customs declaration was filed, where the license for this procedure was issued by customs.  */  
   ISCustomsDeclCountry:string,
      /**  The EU Country from which the goods were dispatched for export, or to which the goods are ultimately destined for import.  */  
   ISEUBorderCrossingCountry:string,
      /**  The mode of transport refers to the mode of transport within the EU.  */  
   IntraEUTransportMode:string,
      /**  Indicates whether or not there is transport by container.  */  
   ContainerShip:boolean,
      /**  Value of transported goods in invoice currency excluding taxes but including miscellaneous charges.  */  
   DocAmount:number,
      /**  Value of transported goods  in invoice currency excluding taxes and miscellaneous charges.  */  
   DocInvAmount:number,
      /**  A unique code that identifies the invoice currency.  */  
   InvCurrencyCode:string,
      /**  EUThirdParty  */  
   EUThirdParty:boolean,
      /**  Country description  */  
   CountryDescr:string,
      /**  Description of country of origin  */  
   CountryOfOriginDescr:string,
      /**  When it is an AR Invoice this will represent the Customer ID, and when it is from AP Invoice this will represent the Supplier ID.  */  
   CustIDSuppID:string,
   CustSuppName:string,
      /**  Delivery Terms description  */  
   DelivTermsDescr:string,
      /**  Entry Point description  */  
   EntrPointDescr:string,
   Generate2Line:boolean,
   LegalNumber:string,
   ManualEntry:boolean,
      /**  Mode of Transport description  */  
   ModeOfTransportDescr:string,
   PartDescription:string,
   PartNum:string,
      /**  Region description  */  
   RegionDescr:string,
   ReportID:string,
      /**  Spec description  */  
   SpecDescr:string,
      /**  Transaction Type description  */  
   TranTypeDescr:string,
   BitFlag:number,
   CommodityCodeSuppUnitsUOM:string,
   CommodityCodeDescription:string,
   FOBDescription:string,
   InvCurrencyCurrDesc:string,
   InvCurrencyCurrSymbol:string,
   InvoiceNumDescription:string,
   ShipViaDescription:string,
   ShipViaWebDesc:string,
   VendorNumTermsCode:string,
   VendorNumAddress1:string,
   VendorNumAddress3:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumState:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumName:string,
   VendorNumAddress2:string,
   VendorNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvoiceIStatTrnTableset{
   IStatTrn:Erp_Tablesets_IStatTrnRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetFlowList_output{
      /**  Flow List  */  
   returnObj:string,
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
export interface UpdateIStatTrn_input{
   ds:Erp_Tablesets_InvoiceIStatTrnTableset[],
}

export interface UpdateIStatTrn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvoiceIStatTrnTableset,
}
}

