import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.IMInvcHeadSvc
// Description: Business object to handle AR Invoice integration
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMInvcHeadSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMInvcHeadSvc/$metadata", {
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
   Summary: Invoke method AddMiscInvc
   Description: Add Invoice Payment processing
   OperationID: AddMiscInvc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddMiscInvc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMiscInvc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddMiscInvc(requestBody:AddMiscInvc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddMiscInvc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMInvcHeadSvc/AddMiscInvc", {
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
         resolve(data as AddMiscInvc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddMiscCreditMemoInvc
   Description: Add Invoice Credit Memo Payment processing
   OperationID: AddMiscCreditMemoInvc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddMiscCreditMemoInvc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMiscCreditMemoInvc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddMiscCreditMemoInvc(requestBody:AddMiscCreditMemoInvc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddMiscCreditMemoInvc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMInvcHeadSvc/AddMiscCreditMemoInvc", {
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
         resolve(data as AddMiscCreditMemoInvc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteMiscInvc
   Description: Delete cash receipt and related tables
   OperationID: DeleteMiscInvc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteMiscInvc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteMiscInvc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteMiscInvc(requestBody:DeleteMiscInvc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteMiscInvc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMInvcHeadSvc/DeleteMiscInvc", {
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
         resolve(data as DeleteMiscInvc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateMiscInvc
   Description: Update cash receipt and related tables
   OperationID: UpdateMiscInvc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateMiscInvc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMiscInvc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMiscInvc(requestBody:UpdateMiscInvc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateMiscInvc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMInvcHeadSvc/UpdateMiscInvc", {
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
         resolve(data as UpdateMiscInvc_output)
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
      @param imInvcHeadTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param saveAddOnError
      @param imIntegrationKey
   */  
export interface AddMiscCreditMemoInvc_input{
   imInvcHeadTableset:Erp_Tablesets_IMInvcHeadTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
   saveAddOnError:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset[],
}

export interface AddMiscCreditMemoInvc_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset,
}
}

   /** Required : 
      @param imInvcHeadTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param saveAddOnError
      @param imIntegrationKey
   */  
export interface AddMiscInvc_input{
   imInvcHeadTableset:Erp_Tablesets_IMInvcHeadTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
   saveAddOnError:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset[],
}

export interface AddMiscInvc_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset,
}
}

   /** Required : 
      @param imInvcHeadTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface DeleteMiscInvc_input{
   imInvcHeadTableset:Erp_Tablesets_IMInvcHeadTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface DeleteMiscInvc_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
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

export interface Erp_Tablesets_IMInvcDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  */  
   LineType:string,
      /**  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  */  
   XRevisionNum:string,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   PartNum:string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   LineDesc:string,
      /**  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  */  
   IUM:string,
      /**  Our Current Revision Number for this Part.  */  
   RevisionNum:string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   POLine:string,
      /**  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  */  
   TaxExempt:string,
      /**  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  */  
   TaxCatID:string,
      /**   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  */  
   Commissionable:boolean,
      /**   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  */  
   DiscountPercent:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   UnitPrice:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocUnitPrice:number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  */  
   OurOrderQty:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocExtPrice:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   Discount:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   TotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   DocTotalMiscChrg:number,
      /**  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  */  
   ProdCode:string,
      /**  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  */  
   OurShipQty:number,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  The packing slip line number that is being invoiced.  */  
   PackLine:number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   OrderNum:number,
      /**  The associated sales order line number.  */  
   OrderLine:number,
      /**  Contains the release number of the order line item that is being invoiced.  */  
   OrderRelNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   ShipToNum:string,
      /**  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  */  
   ShipDate:string,
      /**  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  */  
   ShipViaCode:string,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   AdvanceBillCredit:number,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   DocAdvanceBillCredit:number,
      /**  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  */  
   CustNum:number,
      /**  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  */  
   InvoiceComment:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   ShpConNum:number,
      /**  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlBurUnitCost:number,
      /**  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  */  
   COSPostingReqd:boolean,
      /**   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   COSPosted:boolean,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   CallNum:number,
      /**  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  */  
   CallCode:string,
      /**   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  */  
   RMALine:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  */  
   JournalCode:string,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  */  
   SellingOrderQty:number,
      /**  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  */  
   SellingShipQty:number,
      /**  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Project Id that links the invoice detail  to the Project table.  */  
   ProjectID:string,
      /**  Milestone id that links the invoice detail  to the ProjectMilestone.  */  
   MilestoneID:string,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  */  
   ListPrice:number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  */  
   OrdBasedPrice:number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  */  
   DocOrdBasedPrice:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   AdvGainLoss:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Sales representative commission rate.  */  
   RepRate1:number,
      /**  Sales representative commission rate.  */  
   RepRate2:number,
      /**  Sales representative commission rate.  */  
   RepRate3:number,
      /**  Sales representative commission rate.  */  
   RepRate4:number,
      /**  Sales representative commission rate.  */  
   RepRate5:number,
      /**  Sales representative commission percentage.  */  
   RepSplit1:number,
      /**  Sales representative commission percentage.  */  
   RepSplit2:number,
      /**  Sales representative commission percentage.  */  
   RepSplit3:number,
      /**  Sales representative commission percentage.  */  
   RepSplit4:number,
      /**  Sales representative commission percentage.  */  
   RepSplit5:number,
      /**  Bill To Customer Number used for consolidated invoices  */  
   BTCustNum:number,
      /**  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCMtlUnitCost:number,
      /**  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCLbrUnitCost:number,
      /**  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCBurUnitCost:number,
      /**  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCSubUnitCost:number,
      /**  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCMtlBurUnitCost:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  */  
   RevChargeMethod:string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   OverrideReverseCharge:boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   RevChargeApplied:boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3AdvGainLoss:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping adress country Number.  */  
   OTSCountryNum:number,
      /**  Value is copied from PartTran for PE  */  
   Plant:string,
      /**  value is copied from PartTran for PE  */  
   WarehouseCode:string,
      /**  value is copied from PartTran for PE  */  
   CallLine:number,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  FK to the Finance Charges table  */  
   FinChargeCode:string,
      /**  Reference to the ABT, it is GUID, used in PostingEngine  */  
   ABTUID:string,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   InUnitPrice:number,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocInUnitPrice:number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   InExtPrice:number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocInExtPrice:number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   InDiscount:number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocInDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   InTotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   DocInTotalMiscChrg:number,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  */  
   InListPrice:number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  */  
   DocInListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  */  
   InOrdBasedPrice:number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  */  
   DocInOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt2InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt3InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InUnitPrice:number,
      /**  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  */  
   CorrectionDtl:boolean,
      /**  Asset number of the linked Asset Disposal transaction.  */  
   AssetNum:string,
      /**  Unique number to identify the linked Asset Disposal transaction.  */  
   DisposalNum:number,
      /**   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  */  
   PBLineType:string,
      /**  Invoice line reference  */  
   InvoiceLineRef:number,
      /**  Invoice Number Reference  */  
   InvoiceRef:number,
      /**  Lot Number.  This field should be set according to the linked Shipment Line.  */  
   LotNum:string,
      /**  Reference to the draft invoice line created in Invoice Preparation  */  
   PBInvoiceLine:number,
      /**  Contains the value of the AC_RAHead.RAID client accommodation.  */  
   RAID:number,
      /**  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  */  
   RADtlID:number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  */  
   ChargeDefRev:boolean,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  DefRevPosted  */  
   DefRevPosted:boolean,
      /**  Unit price of Invoice linked to Bill of Exchange in original currency.  */  
   LinkedInvcUnitPrice:number,
      /**  Withholding Tax Amount in reporting currency  */  
   DspWithholdAmt:number,
      /**  Withholding Tax Amount in document currency  */  
   DocDspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt1DspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt2DspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt3DspWithholdAmt:number,
      /**  Currency code from linked Invoice Header  */  
   LinkedCurrencyCode:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  PEBOEHeadNum  */  
   PEBOEHeadNum:number,
      /**  MXSellingShipQty  */  
   MXSellingShipQty:number,
      /**  MXUnitPrice  */  
   MXUnitPrice:number,
      /**  DocMXUnitPrice  */  
   DocMXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1MXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2MXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3MXUnitPrice:number,
      /**  CustCostCenter  */  
   CustCostCenter:string,
      /**  DEIsServices  */  
   DEIsServices:boolean,
      /**  DEIsSecurityFinancialDerivative  */  
   DEIsSecurityFinancialDerivative:boolean,
      /**  DEInternationalSecuritiesID  */  
   DEInternationalSecuritiesID:string,
      /**  DEIsInvestment  */  
   DEIsInvestment:boolean,
      /**  DEPayStatCode  */  
   DEPayStatCode:string,
      /**  DefRevEndDate  */  
   DefRevEndDate:string,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  Indicates tha this invoice Line was reclassified.  */  
   Reclassified:boolean,
      /**  Enables the user the ability to override the Percent or Amount of revenue to be deferred  */  
   PartiallyDefer:boolean,
      /**  Percentage of revenue to be deferred for this line item  */  
   DeferredPercent:number,
      /**  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  */  
   Reclass:boolean,
      /**  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  */  
   DeferredOnly:boolean,
      /**  Reclassification Code. This field will be required if Reclass is checked.  */  
   ReclassCodeID:string,
      /**  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  */  
   ReclassReasonCode:string,
      /**  Internal comments for reclassification entered by the user.  */  
   ReclassComments:string,
      /**  Deferred Revenue Amount in base currency  */  
   DeferredRevAmt:number,
      /**  Deferred Revenue Amount in document currency  */  
   DocDeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt1DeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt2DeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt3DeferredRevAmt:number,
      /**  ChargeReclass  */  
   ChargeReclass:boolean,
      /**  DEDenomination  */  
   DEDenomination:string,
      /**  DropShipPONum  */  
   DropShipPONum:number,
      /**  DocInAdvanceBillCredit  */  
   DocInAdvanceBillCredit:number,
      /**  InAdvanceBillCredit  */  
   InAdvanceBillCredit:number,
      /**  Rpt1InAdvanceBillCredit  */  
   Rpt1InAdvanceBillCredit:number,
      /**  Rpt2InAdvanceBillCredit  */  
   Rpt2InAdvanceBillCredit:number,
      /**  Rpt3InAdvanceBillCredit  */  
   Rpt3InAdvanceBillCredit:number,
      /**  MYIndustryCode  */  
   MYIndustryCode:string,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  ConsolidateLines  */  
   ConsolidateLines:boolean,
      /**  MXCustomsDuty  */  
   MXCustomsDuty:string,
      /**  CommodityCode  */  
   CommodityCode:string,
      /**  MXProdServCode  */  
   MXProdServCode:string,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  Key from related IntQueInOut  */  
   IntQueID:number,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   FSACallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   FSAContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   FSAContractNum:number,
      /**  FSA Warranty Code  */  
   WarrantyCode:string,
      /**  FSA Technician  */  
   EmpID:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Used for integration purposes.  */  
   IMCreditMemo:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMInvcHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if invoice is "open".  */  
   OpenInvoice:boolean,
      /**  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  */  
   ClosedDate:string,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   CreditMemo:boolean,
      /**  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  */  
   UnappliedCash:boolean,
      /**   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  */  
   InvoiceSuffix:string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   InvoiceType:string,
      /**  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  */  
   DeferredRevenue:boolean,
      /**  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  */  
   OrderNum:number,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   CustNum:number,
      /**  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  */  
   PONum:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Defaults from sales order ORderHed.FOB  */  
   FOB:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  */  
   FiscalPeriod:number,
      /**  Once posted, maintenance is not allowed.  */  
   GLPosted:boolean,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnpostedBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   DocUnpostedBal:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DepositCredit:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DocDepositCredit:number,
      /**  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  */  
   SalesRepList:string,
      /**   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   InvoiceRef:number,
      /**  Value of this field is reference to invoice which has been cancelled by current invoice.  */  
   RefCancelled:number,
      /**  Value of this field is reference to invoice that cancelled this invoice.  */  
   RefCancelledBy:number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   StartUp:boolean,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDates:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   PayAmounts:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   DocPayAmounts:string,
      /**  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  */  
   PayDiscDate:string,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   PayDiscAmt:number,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   DocPayDiscAmt:number,
      /**  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  */  
   BillConNum:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  */  
   InvoiceHeld:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Journal that invoice was posted to.  */  
   JournalCode:string,
      /**  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  */  
   LineType:string,
      /**   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**  The Site that the invoice is relate to.  */  
   Plant:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  External Identifier  */  
   ExternalID:string,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefInvoiceNum:string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   DepGainLoss:number,
      /**  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  */  
   DNComments:string,
      /**  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  */  
   DNCustNbr:string,
      /**   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  */  
   DebitNote:boolean,
      /**  This is populated from ShipHead.CustNum representing the Sold To customer.  */  
   SoldToCustNum:number,
      /**  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  */  
   Consolidated:boolean,
      /**  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  */  
   BillToInvoiceAddress:boolean,
      /**  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  */  
   SoldToInvoiceAddress:boolean,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm1:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm2:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm3:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm4:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm5:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate1:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate2:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate3:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate4:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate5:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales1:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales2:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales3:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales4:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales5:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit1:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit2:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit3:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit4:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit5:number,
      /**  Indicates if the Credit Memo is for a Rebate  */  
   CMType:string,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding in Customer currency  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3DepositCredit:number,
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
   Rpt1PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt2PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt3PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt1PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnpostedBal:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3DepGainLoss:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Tax point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  The last date finance/late charges have been calculated for this invoice.  */  
   LastChrgCalcDate:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Total Finance Charge amount.  */  
   TotFinChrg:number,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDiscDays:string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   PayDiscPer:string,
      /**  Blocks certain invoice from generating finance/later charge.  */  
   BlockedFinChrg:boolean,
      /**  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  */  
   BlockedFinChrgReason:string,
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
      /**  Blocks certain invoice from being printed on reminder letters.  */  
   BlockedRemLetters:boolean,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PayDiscPartPay:boolean,
      /**  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  */  
   BlockedRemLettersReason:string,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  Currency Rate Date  */  
   CurrRateDate:string,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   PIPayment:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  */  
   UseAltBillTo:boolean,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden Finland Localization field - Banking Reference  */  
   SEBankRef:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Reversal Doucment Amount  */  
   ReversalDocAmount:number,
      /**  Original Due Date at posting time  */  
   OrigDueDate:string,
      /**  The reference to CashHead.HeadNum.Used in deposit invoices  */  
   HeadNum:number,
      /**  Letter of Credit ID.  */  
   ARLOCID:string,
      /**  The free text field which can contain reference (such as Contract)  */  
   ContractRef:string,
      /**  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  */  
   OurBank:string,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  If the invoice was generated in Project Billing then it is reference to the project.  */  
   PBProjectID:string,
      /**  Deposit amount is transaction amount of deposit payment  */  
   DepositAmt:number,
      /**   Taiwan Localization
Export Bill Number  */  
   GUIExportBillNumber:string,
      /**  Deposit amount is transaction amount of deposit payment in document currency  */  
   DocDepositAmt:number,
      /**   Taiwan Localization
Date of Export  */  
   GUIDateOfExport:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt1 currency  */  
   Rpt1DepositAmt:number,
      /**   Taiwan Localization
Export Type  */  
   GUIExportType:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt2 currency  */  
   Rpt2DepositAmt:number,
      /**   Taiwan Localization
Export Mark  */  
   GUIExportMark:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt23currency  */  
   Rpt3DepositAmt:number,
      /**   Taiwan Localization
Export Bill Type  */  
   GUIExportBillType:string,
      /**  Deposit unallocated amount in base currency  */  
   DepUnallocatedAmt:number,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   SummarizationDate:string,
      /**  Deposit unallocated amount in document currency  */  
   DocDepUnallocatedAmt:number,
      /**  Date when a company bills the customer  */  
   BillingDate:string,
      /**  Deposit unallocated amount in Rpt1 currency  */  
   Rpt1DepUnallocatedAmt:number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   BillingNumber:string,
      /**  Deposit unallocated amount in Rpt2 currency  */  
   Rpt2DepUnallocatedAmt:number,
      /**  Only records ready to bill will be printed in the Billing Statement  */  
   ReadyToBill:boolean,
      /**  Deposit unallocated amount in Rpt3 currency  */  
   Rpt3DepUnallocatedAmt:number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   OvrDefTaxDate:boolean,
      /**  Cross Reference Contract Number.  */  
   XRefContractNum:string,
      /**  Cross Reference Contract Date.  */  
   XRefContractDate:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Customer Agent Name  */  
   CustAgentName:string,
      /**  Customer Agent Tax Region Number  */  
   CustAgentTaxRegNo:string,
      /**  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  */  
   ExportType:string,
      /**  Export Report Number  */  
   ExportReportNo:string,
      /**  Real Estate Number  */  
   RealEstateNo:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
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
      /**  RecurringState  */  
   RecurringState:string,
      /**  IsRecurring  */  
   IsRecurring:boolean,
      /**  InvoiceNumList  */  
   InvoiceNumList:string,
      /**  IsAddedToGTI  */  
   IsAddedToGTI:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHISRCodeLine  */  
   CHISRCodeLine:string,
      /**  CMReason  */  
   CMReason:string,
      /**  THIsImmatAdjustment  */  
   THIsImmatAdjustment:boolean,
      /**  AGAuthorizationCode  */  
   AGAuthorizationCode:string,
      /**  AGAuthorizationDate  */  
   AGAuthorizationDate:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGDocumentLetter  */  
   AGDocumentLetter:string,
      /**  AGInvoicingPoint  */  
   AGInvoicingPoint:string,
      /**  AGLegalNumber  */  
   AGLegalNumber:string,
      /**  AGPrintingControlType  */  
   AGPrintingControlType:string,
      /**  RevisionDate  */  
   RevisionDate:string,
      /**  RevisionNum  */  
   RevisionNum:number,
      /**  TWDeclareYear  */  
   TWDeclareYear:number,
      /**  TWDeclarePeriod  */  
   TWDeclarePeriod:number,
      /**  TWGenerationType  */  
   TWGenerationType:string,
      /**  TWGUIGroup  */  
   TWGUIGroup:string,
      /**  TWPeriodPrefix  */  
   TWPeriodPrefix:string,
      /**  Indicates if the Invoice is in Collections status  */  
   InvInCollections:boolean,
      /**   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  */  
   CollectionsCust:boolean,
      /**  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  */  
   CounterARForm:number,
      /**  flag indicates if Revenue of the invoice has been already posted  */  
   PostedRecog:boolean,
      /**  Confirmation Date  */  
   CNConfirmDate:string,
      /**  MXSATSeal  */  
   MXSATSeal:string,
      /**  MXSerie  */  
   MXSerie:string,
      /**  MXTaxRcptType  */  
   MXTaxRcptType:string,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  MXTotalPayments  */  
   MXTotalPayments:number,
      /**  MXFolio  */  
   MXFolio:string,
      /**  MXCertifiedTimestamp  */  
   MXCertifiedTimestamp:string,
      /**  MXSATCertificateSN  */  
   MXSATCertificateSN:string,
      /**  MXDigitalSeal  */  
   MXDigitalSeal:string,
      /**  MXPostedTimeStamp  */  
   MXPostedTimeStamp:string,
      /**  MXCertificate  */  
   MXCertificate:string,
      /**  MXApprovalYear  */  
   MXApprovalYear:number,
      /**  MXCBB  */  
   MXCBB:string,
      /**  MXApprovalNum  */  
   MXApprovalNum:number,
      /**  MXOriginalStringTFD  */  
   MXOriginalStringTFD:string,
      /**  MXPaymentNum  */  
   MXPaymentNum:number,
      /**  MXPaidAs  */  
   MXPaidAs:string,
      /**  MXCertificateSN  */  
   MXCertificateSN:string,
      /**  MXOriginalAmount  */  
   MXOriginalAmount:number,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  MXOriginalDate  */  
   MXOriginalDate:string,
      /**  MXOriginalSeries  */  
   MXOriginalSeries:string,
      /**  MXOriginalFolio  */  
   MXOriginalFolio:string,
      /**  MXTaxRegime  */  
   MXTaxRegime:string,
      /**  MXOriginalString  */  
   MXOriginalString:string,
      /**  MXPaymentName  */  
   MXPaymentName:string,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  EInvStatus  */  
   EInvStatus:number,
      /**  EInvTimestamp  */  
   EInvTimestamp:string,
      /**  EInvUpdatedBy  */  
   EInvUpdatedBy:string,
      /**  EInvException  */  
   EInvException:string,
      /**  Flagged that this invoice has taxes which were necessary or is necessary now.  */  
   WithTaxConfirm:boolean,
      /**  UseAltBillToID  */  
   UseAltBillToID:boolean,
      /**  MXCancelledDate  */  
   MXCancelledDate:string,
      /**  Overpaid  */  
   Overpaid:boolean,
      /**  OrdExchangeRate  */  
   OrdExchangeRate:number,
      /**  PEAPPayNum  */  
   PEAPPayNum:number,
      /**  PEBankNumber  */  
   PEBankNumber:string,
      /**  PECharges  */  
   PECharges:number,
      /**  PECommissions  */  
   PECommissions:number,
      /**  PEDetTaxAmt  */  
   PEDetTaxAmt:number,
      /**  PEDetTaxCurrencyCode  */  
   PEDetTaxCurrencyCode:string,
      /**  PEDischargeAmt  */  
   PEDischargeAmt:number,
      /**  PEDischargeDate  */  
   PEDischargeDate:string,
      /**  PEInterest  */  
   PEInterest:number,
      /**  PENoPayPenalty  */  
   PENoPayPenalty:number,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   PESUNATDepAmt:number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   PESUNATDepDate:string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   PESUNATDepNum:string,
      /**  PEBOEPosted  */  
   PEBOEPosted:boolean,
      /**  DocPEInterest  */  
   DocPEInterest:number,
      /**  DocPECommissions  */  
   DocPECommissions:number,
      /**  DocPECharges  */  
   DocPECharges:number,
      /**  DocPENoPayPenalty  */  
   DocPENoPayPenalty:number,
      /**  DocPEDischargeAmt  */  
   DocPEDischargeAmt:number,
      /**  DocPEDetTaxAmt  */  
   DocPEDetTaxAmt:number,
      /**  Rpt1PEInterest  */  
   Rpt1PEInterest:number,
      /**  Rpt1PECommissions  */  
   Rpt1PECommissions:number,
      /**  Rpt1PECharges  */  
   Rpt1PECharges:number,
      /**  Rpt1PENoPayPenalty  */  
   Rpt1PENoPayPenalty:number,
      /**  Rpt1PEDischargeAmt  */  
   Rpt1PEDischargeAmt:number,
      /**  Rpt2PEInterest  */  
   Rpt2PEInterest:number,
      /**  Rpt2PECommissions  */  
   Rpt2PECommissions:number,
      /**  Rpt2PECharges  */  
   Rpt2PECharges:number,
      /**  Rpt2PENoPayPenalty  */  
   Rpt2PENoPayPenalty:number,
      /**  Rpt2PEDischargeAmt  */  
   Rpt2PEDischargeAmt:number,
      /**  Rpt3PEInterest  */  
   Rpt3PEInterest:number,
      /**  Rpt3PECommissions  */  
   Rpt3PECommissions:number,
      /**  Rpt3PECharges  */  
   Rpt3PECharges:number,
      /**  Rpt3PENoPayPenalty  */  
   Rpt3PENoPayPenalty:number,
      /**  Rpt3PEDischargeAmt  */  
   Rpt3PEDischargeAmt:number,
      /**  Our Supplier Code  */  
   OurSupplierCode:string,
      /**  PEGuaranteeName  */  
   PEGuaranteeName:string,
      /**  PEGuaranteeAddress1  */  
   PEGuaranteeAddress1:string,
      /**  PEGuaranteeAddress2  */  
   PEGuaranteeAddress2:string,
      /**  PEGuaranteeAddress3  */  
   PEGuaranteeAddress3:string,
      /**  PEGuaranteeCity  */  
   PEGuaranteeCity:string,
      /**  PEGuaranteeState  */  
   PEGuaranteeState:string,
      /**  PEGuaranteeZip  */  
   PEGuaranteeZip:string,
      /**  PEGuaranteeCountry  */  
   PEGuaranteeCountry:string,
      /**  PEGuaranteeTaxID  */  
   PEGuaranteeTaxID:string,
      /**  PEGuaranteePhoneNum  */  
   PEGuaranteePhoneNum:string,
      /**  PEBOEStatus  */  
   PEBOEStatus:string,
      /**  PEBOEIsMultiGen  */  
   PEBOEIsMultiGen:boolean,
      /**  PE Reference Document ID  */  
   PERefDocID:string,
      /**  PE Reason Code  */  
   PEReasonCode:string,
      /**  PE Reason Description  */  
   PEReasonDesc:string,
      /**  TW GUI Code Seller  */  
   TWGUIRegNumSeller:string,
      /**  TW GUI Code Buyer  */  
   TWGUIRegNumBuyer:string,
      /**  Document Name  */  
   TWGUIExportDocumentName:string,
      /**  Remarks  */  
   TWGUIExportRemarks:string,
      /**  Verification  */  
   TWGUIExportVerification:string,
      /**  PEDebitNoteReasonCode  */  
   PEDebitNoteReasonCode:string,
      /**  PEDebitNote  */  
   PEDebitNote:boolean,
      /**  MXPartPmt  */  
   MXPartPmt:boolean,
      /**  Tax Invoice Type  */  
   CNTaxInvoiceType:number,
      /**  MXExportOperationType  */  
   MXExportOperationType:string,
      /**  MXExportCustDocCode  */  
   MXExportCustDocCode:string,
      /**  MXExportCertOriginNum  */  
   MXExportCertOriginNum:string,
      /**  MXExportConfNum  */  
   MXExportConfNum:string,
      /**  MXExportCertOrigin  */  
   MXExportCertOrigin:boolean,
      /**  MXIncoterm  */  
   MXIncoterm:string,
      /**  AGDocConcept  */  
   AGDocConcept:number,
      /**  Electronic Invoice reference number  */  
   EInvRefNum:string,
      /**  Export document reference number  */  
   ExportDocRefNum:string,
      /**  Export document date  */  
   ExportDocDate:string,
      /**  Tax Transaction ID  */  
   INTaxTransactionID:string,
      /**  MXMovingReasonFlag  */  
   MXMovingReasonFlag:boolean,
      /**  MXMovingReason  */  
   MXMovingReason:string,
      /**  MXNumRegIdTrib  */  
   MXNumRegIdTrib:string,
      /**  MXResidenCountryNum  */  
   MXResidenCountryNum:number,
      /**  MXPurchaseType  */  
   MXPurchaseType:string,
      /**  MXConfirmationCode  */  
   MXConfirmationCode:string,
      /**  MXExternalCode  */  
   MXExternalCode:string,
      /**  This invoice was created via an integration with a third-party field service.  */  
   ServiceInvoice:boolean,
      /**  Header record should not be updated for integration update  */  
   SkipUpdate:boolean,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
      /**  Key from related IntQueInOut  */  
   IntQueID:number,
      /**  Integration invoice type.  Used for setting of InvoiceType.  */  
   IntInvoiceType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMInvcHeadTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMInvcDtl:Erp_Tablesets_IMInvcDtlRow[],
   IMInvcHead:Erp_Tablesets_IMInvcHeadRow[],
   IMInvcMisc:Erp_Tablesets_IMInvcMiscRow[],
   IMInvcTax:Erp_Tablesets_IMInvcTaxRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMInvcMiscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  Invoice Line Number associated with this misc. charge.  */  
   InvoiceLine:number,
      /**  Sequence Number  */  
   SeqNum:number,
      /**  Miscellaneous Charge code  */  
   MiscCode:string,
      /**  Description  */  
   Description:string,
      /**  Miscellaneous line amount. Base Currency.  */  
   MiscAmt:number,
      /**  Miscellaneous line amount. Document Currency.  */  
   DocMiscAmt:number,
      /**  Indicates the Tax Category for this Misc. record. Defaults from the MiscChg master.  */  
   TaxCatID:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  Includes taxes  */  
   InMiscAmt:number,
      /**  Includes taxes  */  
   DocInMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InMiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  OrgInvcLine  */  
   OrgInvcLine:number,
      /**  OrgInvcSeq  */  
   OrgInvcSeq:number,
      /**  MXProdServCode  */  
   MXProdServCode:string,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
      /**  Key from related IntQueInOut  */  
   IntQueID:number,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   FSACallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   FSAContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   FSAContractNum:number,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Warranty Code from FSA  */  
   WarrantyCode:string,
      /**  Used for integration purposes.  */  
   IMCreditMemo:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMInvcTaxRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  Part of the foreign key used to relate back to a InvcDtl or InvcMisc record.  */  
   InvoiceLine:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  InvcDtl.TaxCode and InvcDtl/InvcMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount ((Qty*unitprice)-discount) or if this is for a InvcMisc record InvcMisc.Amount.  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  InvcDtl.TaxCode and InvcDtl/InvcMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount ((Qty*unitprice)-discount) or if this is for a InvcMisc record InvcMisc.Amount.  */  
   DocReportableAmt:number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   TaxableAmt:number,
      /**  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Tax Rate Code  */  
   RateCode:string,
      /**  Collection Type  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution number  */  
   ResolutionNum:string,
      /**  Resolution Date  */  
   ResolutionDate:string,
      /**  Tax Rate Date  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DocDefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount  */  
   DedTaxAmt:number,
      /**  Deducatable Tax Amount  */  
   DocDedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DedTaxAmt:number,
      /**   Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  */  
   ECAcquisitionSeq:number,
      /**  Fixed Tax Amount  */  
   FixedAmount:number,
      /**  Document Fixed Tax Amount  */  
   DocFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3FixedAmount:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt1TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt2TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   Rpt3TaxAmtVar:number,
      /**  Legal Text code  */  
   RateTextCode:string,
      /**  Deferred tax date for Service Tax Point  */  
   DefTaxDate:string,
      /**  Flag to indicate for posting engine and tax updates whether being treated as current or future  */  
   TaxFuture:boolean,
      /**  Flag to indicate if the Service Tax Line is already processed  */  
   STPProcessed:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  OrgInvcLine  */  
   OrgInvcLine:number,
      /**  MovementNum  */  
   MovementNum:number,
      /**  ConfirmationDate  */  
   ConfirmationDate:string,
      /**  ApplyConfirmationDate  */  
   ApplyConfirmationDate:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  TaxConfirm  */  
   TaxConfirm:boolean,
      /**  AllocDepInvcNum  */  
   AllocDepInvcNum:number,
      /**  AllocDepInvcLine  */  
   AllocDepInvcLine:number,
      /**  AllocDepRateCode  */  
   AllocDepRateCode:string,
      /**  AllocDepECAcqSeq  */  
   AllocDepECAcqSeq:number,
      /**  AllocDepTaxBal  */  
   AllocDepTaxBal:number,
      /**  DocAllocTaxBal  */  
   DocAllocTaxBal:number,
      /**  Rpt1AllocDepTaxBal  */  
   Rpt1AllocDepTaxBal:number,
      /**  Rpt2AllocDepTaxBal  */  
   Rpt2AllocDepTaxBal:number,
      /**  Rpt3AllocDepTaxBal  */  
   Rpt3AllocDepTaxBal:number,
      /**  TaxReverseDate  */  
   TaxReverseDate:string,
      /**  ReverseByInvoiceNum  */  
   ReverseByInvoiceNum:number,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
      /**  Key from related IntQueInOut  */  
   IntQueID:number,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   FSACallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   FSAContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   FSAContractNum:number,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Warranty Code from FSA  */  
   WarrantyCode:string,
      /**  Used for integration purposes.  */  
   IMCreditMemo:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
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

   /** Required : 
      @param imInvcHeadTablese
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface UpdateMiscInvc_input{
   imInvcHeadTablese:Erp_Tablesets_IMInvcHeadTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface UpdateMiscInvc_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

