import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PurchaseAdvisorSvc
// Description: Purchase Advisor
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/$metadata", {
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
   Summary: Invoke method ChangePartNum
   Description: Run this method when the partnumber on the detail screen changes .
   OperationID: ChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartNum(requestBody:ChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/ChangePartNum", {
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
         resolve(data as ChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePlantOnOrder
   Description: Rebuild the On Order list when the plant changes.  Prior to calling this
procedure, the RowMod field in all ttPAOnOrder records must be set to "U"
because these records need to be cleared from the table before rebuilding the list.
   OperationID: ChangePlantOnOrder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePlantOnOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantOnOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePlantOnOrder(requestBody:ChangePlantOnOrder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePlantOnOrder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/ChangePlantOnOrder", {
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
         resolve(data as ChangePlantOnOrder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePlantPurchasedBefore
   Description: Rebuild the Purchased Before list when the plant changes.  Prior to calling this
procedure, the RowMod field in all ttPAPurchasedBefore records must be set to "U"
because these records need to be cleared from the table before rebuilding the list.
   OperationID: ChangePlantPurchasedBefore
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePlantPurchasedBefore_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantPurchasedBefore_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePlantPurchasedBefore(requestBody:ChangePlantPurchasedBefore_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePlantPurchasedBefore_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/ChangePlantPurchasedBefore", {
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
         resolve(data as ChangePlantPurchasedBefore_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPurchaseAdvisor
   Description: Get the PurchaseAdvisor records from the parameters.
   OperationID: GetPurchaseAdvisor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPurchaseAdvisor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPurchaseAdvisor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPurchaseAdvisor(requestBody:GetPurchaseAdvisor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPurchaseAdvisor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/GetPurchaseAdvisor", {
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
         resolve(data as GetPurchaseAdvisor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSupplierPriceList
   Description: Method to call to get the dataset based on a specific part.
   OperationID: GetSupplierPriceList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSupplierPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSupplierPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSupplierPriceList(requestBody:GetSupplierPriceList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSupplierPriceList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PurchaseAdvisorSvc/GetSupplierPriceList", {
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
         resolve(data as GetSupplierPriceList_output)
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
      @param newPartNum
      @param sysRowID
      @param rowType
      @param isSubstitute
      @param ds
   */  
export interface ChangePartNum_input{
      /**  New Part Number  */  
   newPartNum:string,
      /**  Sys Row ID for match (conflict resolution only)  */  
   sysRowID:string,
      /**  Row Type for match (conflict resolution only)  */  
   rowType:string,
      /**  True whether it is a Substitute Part  */  
   isSubstitute:boolean,
   ds:Erp_Tablesets_PurchaseAdvisorTableset[],
}

export interface ChangePartNum_output{
parameters : {
      /**  output parameters  */  
   newPartNum:string,
   multipleMatch:boolean,
   ds:Erp_Tablesets_PurchaseAdvisorTableset,
}
}

   /** Required : 
      @param ds
      @param cPartNum
      @param iPONum
      @param cPlant
   */  
export interface ChangePlantOnOrder_input{
   ds:Erp_Tablesets_PurchaseAdvisorTableset[],
      /**  The part number  */  
   cPartNum:string,
      /**  The PO number  */  
   iPONum:number,
      /**  The plant  */  
   cPlant:string,
}

export interface ChangePlantOnOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurchaseAdvisorTableset,
}
}

   /** Required : 
      @param ds
      @param cPartNum
      @param cPlant
   */  
export interface ChangePlantPurchasedBefore_input{
   ds:Erp_Tablesets_PurchaseAdvisorTableset[],
      /**  The part number  */  
   cPartNum:string,
      /**  The plant  */  
   cPlant:string,
}

export interface ChangePlantPurchasedBefore_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PurchaseAdvisorTableset,
}
}

export interface Erp_Tablesets_PAApprovedVendorsRow{
   Company:string,
   PartNum:string,
   APVType:string,
   VendorNum:number,
   ClassID:string,
   CustNum:number,
   OpCode:string,
   CustID:string,
   CustomerName:string,
   VendID:string,
   VendorName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PACompliantVendPartRow{
   Company:string,
   PartNum:string,
   ClassID:string,
   OpCode:string,
   PUM:string,
   VendorNum:number,
   VendID:string,
   VendorName:string,
   RestrictionTypeID:string,
   RestrictionName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PACompliantVendorsRow{
   Company:string,
   PartNum:string,
   ClassID:string,
   VendorNum:number,
   VendID:string,
   VendorName:string,
   RestrictionTypeID:string,
   RestrictionName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PAOnOrderRow{
   Company:string,
   PartNum:string,
   PONum:number,
   POLine:number,
   PORelNum:number,
   VendorName:string,
   RelQty:number,
   UnitCost:number,
   DocUnitCost:number,
   CostPerCode:string,
   PUM:string,
   JobSeqType:string,
   CurrSymbol:string,
      /**  DueDate  */  
   DueDate:string,
   BaseCurrSymbol:string,
   RelPromiseDt:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   POType:string,
      /**  Lead Time is set based on the following hierarchy: 1 - PartXRefVend.LeadTime, 2 - VendPart.LeadTime, 3 - PartPlant.LeadTime  */  
   LeadTime:number,
      /**  The unreceived quantity  */  
   UnreceivedQty:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PAPurchasedBeforeRow{
   Company:string,
   PartNum:string,
   POLine:number,
   PORelNum:number,
   SeqNum:number,
   ReceiptDate:string,
   VendorName:string,
   VendorQty:number,
   VendorUnitCost:number,
   ActLead:number,
   OrderDate:string,
   DueDate:string,
   PUM:string,
   CostPerCode:string,
   SeqType:string,
   PONum:number,
   BaseCurrSymbol:string,
   CurrSymbol:string,
   UnitCost:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PurchaseAdvisorAttchRow{
   Company:string,
   PartNum:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PurchaseAdvisorRow{
   Company:string,
   PartNum:string,
   PONum:number,
   APVType:string,
   ClassID:string,
   OpCode:string,
   CustNum:number,
   PurchasedBefore:boolean,
   AnyOnOrder:boolean,
   AnyOnHand:boolean,
   ApprovedVendors:boolean,
   DispPurchasedBefore:string,
   DispAnyOnOrder:string,
   DispAnyOnHand:string,
   DispApprovedVendors:string,
      /**  Indicates if there are supplier price lists  */  
   SupplierPriceListExists:boolean,
   CompliantVendors:boolean,
   DispCompliantVendors:string,
   CompliantVendParts:boolean,
   DispCompliantVendParts:string,
      /**  Question  */  
   Question:string,
      /**  Question Type  */  
   QuestionType:string,
      /**  The Part Description if exists otherwise "Non Part"  */  
   PartDescription:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PurchaseAdvisorTableset{
   PurchaseAdvisor:Erp_Tablesets_PurchaseAdvisorRow[],
   PurchaseAdvisorAttch:Erp_Tablesets_PurchaseAdvisorAttchRow[],
   PAOnOrder:Erp_Tablesets_PAOnOrderRow[],
   PAPurchasedBefore:Erp_Tablesets_PAPurchasedBeforeRow[],
   PAApprovedVendors:Erp_Tablesets_PAApprovedVendorsRow[],
   PACompliantVendors:Erp_Tablesets_PACompliantVendorsRow[],
   PACompliantVendPart:Erp_Tablesets_PACompliantVendPartRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SupplierPriceListTableset{
   SupplierVendPart:Erp_Tablesets_SupplierVendPartRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SupplierVendPartRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies our Part.  */  
   PartNum:string,
      /**   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor. 
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  */  
   OpCode:string,
      /**   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  */  
   PUM:string,
      /**  The date which this vendor/part information is effective.  */  
   EffectiveDate:string,
      /**  Vendor's unique internal number.  */  
   VendorNum:number,
      /**  Used to record the normal  order lead time that this vendor gives for this part. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  */  
   LeadTime:number,
      /**   BaseUnitPrice + VendPBrk.UnitPrice = Unit Price for the Part.  This design allows users to enter "Qty Break Unit Prices" (VendPBrk.UnitPrice) either as a price that should be Added or Subtracted (negatives) to Base or as a true Unit Price(Base = 0).  This is an attempt to make it easier to enter prices from varying formats of vendor price lists.
Some vendors define their prices as a Base Unit Price with an additional amount to be added/deducted to it at specific quantities levels.  */  
   BaseUnitPrice:number,
      /**  Part number that the Vendor uses to identify the item.  */  
   VenPartNum:string,
      /**  Indicates the format of UnitPrices in VendPBrk table.  This can either be "$" = Flat Unit Price, or "%" = Percent of Base.  */  
   PriceFormat:string,
      /**   Indicates the vendor's pricing per value for the part.                     "E" = per each, "C" = per hundred,  "M" = per thousand.
Used as a default in purchasing, also used to convert a vendor unit price to our unit costs.
Basic formula for converting to "our unit cost" is as follows...
Our Unit$ = Vendor Unit$ / Cost Per factor) * PurchasingFactor.  */  
   PricePerCode:string,
      /**   Minimum Charge for this material.  This is used as a default to QuoteMtl.MinimumCost, QuoteOpr.MinimumCost.  In routines used to retrieve a default unit cost (PO, Jobs..) the Manufacturing System  will take the greater of (required quantity * unit cost) or (MinimumCost).
Note: The AddlCharge is not included in the above formula.  */  
   MinimumPrice:number,
      /**  Optional Expiration date of this cost information.  The Manufacturing System uses this date to inform the user when the cost information that is being used has expired.  This is an indicator that this information may not be accurate and should be reconfirmed with the vendor.  */  
   ExpirationDate:string,
      /**  An optional field that may be used for any reference to this vendors costing info. Ex: RFQ, Quote#, etc...  */  
   Reference:string,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...). This is only used with a Subcontract price. It's used as a default to QuoteOpr.MiscCharge, JobOper.MiscCharge and POMisc.MiscAmt
will be defaulted to the This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   MiscAmt:number,
      /**  The Miscellaneous Charge Code related to the MiscCharge field. If MiscCharge <> 0 then must be entered and valid in the PURMisc file.  This will be the MiscCode used to create the PoMisc record when defaults are created in purchase order entry.  */  
   MiscCode:string,
      /**  Additional comments that will be used as a default for purchasing.  View as an EDITOR widget.  */  
   CommentText:string,
      /**   Overall discount percent. Used to develop an effective unit price.
(BaseUnitPrice + QtyBrkValue) *( (100 - DiscountPercent) * .01)  */  
   DiscountPercent:number,
      /**  Description of Part. Used only for Non Part master parts.  */  
   PartDescription:string,
      /**   Related RFQ number.
Note: zero for price breaks entered via master maintenance.  */  
   RFQNum:number,
      /**   Related RFQ Line number. 
Note: Zero for price breaks created by master maintenance programs.  */  
   RFQLine:number,
      /**   A unique code that identifies the currency.
NOT ACTIVE  AS OF 3.20. RESERVED FOR FUTURE USE.  */  
   CurrencyCode:string,
      /**  Suppliers Quantity on Hand  */  
   OnhandQty:number,
      /**  Date Suppliers Quantity was updated  */  
   OnHandDate:string,
      /**  Time Suppliers Quantity was updated  */  
   OnHandTime:number,
      /**  Supplier contact linked to this Price  */  
   ConNum:number,
      /**  This is for use in SupplierConnect.  It indicates the Supplier has completed the changes to the RFQ and is ready for the data to be posted back to Vantage.  */  
   SupplierResponseReady:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Vendor's Name  */  
   VendorName:string,
      /**  Supplier Part  */  
   VendPartNum:string,
      /**  Manufacturer's Name.  */  
   MfgName:string,
   MfgPartNum:string,
   CurrencyCodeDescription:string,
      /**  Id Counter of the total of data.  */  
   Id:number,
      /**  Manufacturer Part Number (not deprecated)  */  
   MfgPartNumber:string,
   PrimaryVendor:boolean,
      /**  PartXRefVend's Purchase Default field  */  
   PurchaseDefault:boolean,
      /**  PartXRefMfg's LeadTime  */  
   MarketLeadTime:string,
      /**  LifecycleStatus  */  
   LifecycleStatus:string,
   MfgNum:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param cPartNum
      @param iPONum
      @param cAPVType
      @param cClassID
      @param cOpCode
      @param iCustNum
   */  
export interface GetPurchaseAdvisor_input{
      /**  The Part Number  */  
   cPartNum:string,
      /**  The Purchase Order Number  */  
   iPONum:number,
      /**  The APVType for Approved Vendors  */  
   cAPVType:string,
      /**  The Class ID  */  
   cClassID:string,
      /**  The Op Code  */  
   cOpCode:string,
      /**  The customer number  */  
   iCustNum:number,
}

export interface GetPurchaseAdvisor_output{
   returnObj:Erp_Tablesets_PurchaseAdvisorTableset[],
}

   /** Required : 
      @param cPartNum
   */  
export interface GetSupplierPriceList_input{
      /**  The Part Number to retrieve the dataset for  */  
   cPartNum:string,
}

export interface GetSupplierPriceList_output{
   returnObj:Erp_Tablesets_SupplierPriceListTableset[],
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

