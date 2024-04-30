import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ICReceiptSearchSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/$metadata", {
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
   Summary: Invoke method GetRows
   Description: This overload of AfterGetRows filters the Dataset for the criteria
   OperationID: Get_GetRows
      @param whereClause Desc: The criteria   Required: True   Allow empty value : True
      @param PONum Desc: PONum - Purchase Order Number   Required: True
      @param POLine Desc: POLine - Line   Required: True
      @param PORel Desc: PORel - Release   Required: True
      @param pageSize Desc: Size of a page   Required: True
      @param absolutePage Desc: The absolute page   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClause:string, PONum:string, POLine:string, PORel:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof PONum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "PONum=" + PONum
   }
   if(typeof POLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "POLine=" + POLine
   }
   if(typeof PORel!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "PORel=" + PORel
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/GetRows" + params, {
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
         resolve(data as GetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RcvHeadBeforeDelete
   OperationID: RcvHeadBeforeDelete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RcvHeadBeforeDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvHeadBeforeDelete(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RcvHeadBeforeDelete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/RcvHeadBeforeDelete", {
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
         resolve(data as RcvHeadBeforeDelete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RcvHeadBeforeGetNew
   OperationID: RcvHeadBeforeGetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RcvHeadBeforeGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvHeadBeforeGetNew(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RcvHeadBeforeGetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/RcvHeadBeforeGetNew", {
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
         resolve(data as RcvHeadBeforeGetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RcvHeadBeforeUpdate
   OperationID: RcvHeadBeforeUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RcvHeadBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RcvHeadBeforeUpdate(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RcvHeadBeforeUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/RcvHeadBeforeUpdate", {
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
         resolve(data as RcvHeadBeforeUpdate_output)
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
export interface Erp_Tablesets_ICReceiptSearchTableset{
   RcvHead:Erp_Tablesets_RcvHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RcvHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Receipt Date. Defaults as current system date.  */  
   ReceiptDate:string,
      /**  Person that entered the transaction. It is set to the DCD-USERID that was logged on when the record was created . This is not maintainable by the user. This is could be used as a selection parameter for reporting and browsing.  */  
   EntryPerson:string,
      /**  An internal flag that indicates this receipt document is to be saved for retrieval by A\P invoice entry. This is set based on the value stored in APSyst.SaveForInvoicing.  */  
   SaveForInvoicing:boolean,
      /**  An internal flag that indicates "ALL" the details items on this receipt document have been invoiced. This is set to "Yes" when there are no related RcvDtl records where RcvDtl.Invoiced = No. This flag along with the SaveForInvoicing flag are used to present a list of uninvoiced packing slips.  */  
   Invoiced:boolean,
      /**  Contains comments about the overall Receipt.  */  
   ReceiptComment:string,
      /**  Short name or initials of person who actually did the receiving. A totally optional field which can be used for internal reference.  */  
   ReceivePerson:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia.  */  
   ShipViaCode:string,
      /**  The system date when this record was created.  */  
   EntryDate:string,
      /**  Site that received the goods.  */  
   Plant:string,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   PONum:number,
      /**  Reference field for Landed Costs  */  
   LCReference:string,
      /**  Comment field for Landed Costs  */  
   LCComment:string,
      /**  Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  */  
   LandedCost:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  This field holds the variance amount for the landed costs.  */  
   LCVariance:number,
      /**  Indicates if linked to a inter-company shipment  */  
   ICLinked:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Purchase Point identifier.  Used in Consolidated Purchasing.  */  
   GlbPurPoint:string,
      /**  Global Packing Slip identifier.  Used in Consolidated Purchasing.  */  
   GlbPackSlip:string,
      /**  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  */  
   ContainerID:number,
      /**  Weight  */  
   Weight:number,
      /**  Identifies how the landed cost was disbursed among the container details.  Valid options are Volume (only for po releases tied to a container), Weight, Value and Manual.  */  
   LCDisburseMethod:string,
      /**  This is a flag representing whether or not this is a receipt that was auto generated.  It could only be true if it is associated with an SMI type PO.  */  
   AutoReceipt:boolean,
      /**  Indicates the type of transaction that created this auto receipt.  This field will only be populated if AutoReceipt = true.  */  
   AutoTranType:string,
      /**  POType Identifier of the associated PO ('Std', 'CMI', or 'SMI')  */  
   POType:string,
      /**  The unique number of the PartTran record that was the source of this transaction.  This field will only be populated if AutoReceipt = true.  */  
   AutoTranID:number,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  */  
   WeightUOM:string,
      /**  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  */  
   UpliftPercent:number,
      /**  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  */  
   SpecDutyAmt:number,
      /**  The total Landed Cost Amount disbursed for this receipt.  */  
   AppliedLCAmt:number,
      /**  The total Duty Amount of the entire receipt.  */  
   LCDutyAmt:number,
      /**  The total Indirect Cost Amount of the entire receipt.  */  
   LCIndCost:number,
      /**  Flag to indicate if all of the receipt duties and indirect costs needs to be applied or disbursed.  */  
   ApplyToLC:boolean,
      /**  Flag to indicate if the entire receipt has been completely received.  */  
   Received:boolean,
      /**  The date the shipment arrived. Defaults as current system date.  */  
   ArrivedDate:string,
      /**  The total Landed Cost Amount applied for this receipt.  */  
   AppliedRcptLCAmt:number,
      /**  The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  */  
   LCUpliftIndCost:number,
      /**  This field holds the applied variance amount for the landed costs.  */  
   AppliedLCVariance:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Stores the number of the import document.  Default value for lines.  */  
   ImportNum:string,
      /**  Stores the Country from which the document is imported.  Default value for lines.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  Default value for lines.  */  
   ImportedFromDesc:string,
      /**  Gross Weight  */  
   GrossWeight:number,
      /**   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.GrossWeightUOM is not known.  */  
   GrossWeightUOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  The Tax Liability for this Receipt  */  
   TaxRegionCode:string,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  ** NOT USED TO BE DROPPED 10.2 ** This flag determines whether any manual taxes were created for a header miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   HdrTaxNoUpdt:boolean,
      /**  Tax Rate Group Code - FUTUREUSE  */  
   TaxRateGrpCode:string,
      /**  The flag indicates that taxes have been calculated.  Once the flag is true is should never be changed back to false.  This will be set to true when any receipt line is marked as received, or when taxes have been calculated via the Calculate All Taxes menu option.  */  
   TaxesCalculated:boolean,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount disbursed for this receipt.  */  
   InAppliedLCAmt:number,
      /**  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  */  
   InAppliedLCVariance:number,
      /**  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt.  */  
   InAppliedRcptLCAmt:number,
      /**  Internal usage for inclusive taxes - Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  */  
   InLandedCost:number,
      /**  Internal usage for inclusive taxes - The total Duty Amount of the entire receipt.  */  
   InLCDutyAmt:number,
      /**  Internal usage for inclusive taxes - The total Indirect Cost Amount of the entire receipt.  */  
   InLCIndCost:number,
      /**  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  */  
   InLCUpliftIndCost:number,
      /**  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  */  
   InLCVariance:number,
      /**  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  */  
   InSpecDutyAmt:number,
      /**  Declaration Bill  */  
   CNDeclarationBill:string,
      /**  Bonded  */  
   CNBonded:boolean,
      /**  APTaxRoundOption  */  
   APTaxRoundOption:number,
      /**  Address Information from Vendor or VendorPP  */  
   AddrList:string,
      /**  Logical indicating whether or not the receipt has been fully received.  If yes then the receipt has only been partially received.  */  
   PartialReceipt:boolean,
   POLine:number,
   PORel:number,
   POTypeDesc:string,
   ShipViaDesc:string,
      /**  Total amount.  This is the sum of all the other total fields.  */  
   TotalAmt:number,
      /**  Total dedicated Tax amount.  */  
   TotDedTaxAmt:number,
      /**  Total duties amount.  This is the sum of RcvHead.SpecDutyAmt + RcvHead.LCDutyAmt  */  
   TotDutiesAmt:number,
      /**  Total Gross Weight of all receipt lines  */  
   TotGrossWeight:number,
      /**  Qualifies the unit of measure of the Gross Weight field.  */  
   TotGrossWeightUOM:string,
      /**  Total Indirect Costs amount.  This is a sum of all RcvMisc.ActualAmt.  */  
   TotIndirectCostsAmt:number,
      /**  Total amount for all receipt lines.  This is the sum of RcvDtl.POTransValue.  */  
   TotLinesAmt:number,
      /**  Total Self Assessed Tax amount  */  
   TotSATaxAmt:number,
      /**  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  */  
   TotTaxAmt:number,
      /**  Total Weight of all receipt lines  */  
   TotWeight:number,
      /**  Qualifies the unit of measure of the Weight field.  */  
   TotWeightUOM:string,
      /**  Total WithHolding Tax amount  */  
   TotWHTaxAmt:number,
      /**  Flag to indicate if receipt details need to be refreshed after changing the Arrival Date from header.  */  
   UpdateDtlArvdDate:boolean,
      /**  Flag to indicate if receipt details need to be refreshed after changing the Receipt Date from header.  */  
   UpdateDtlRcptDate:boolean,
      /**  Flag to indicate if details need to be refreshed after changing the UpliftPercent from header.  */  
   UpdateDtlRecs:boolean,
      /**  Flag to indicate if record can be updated.  */  
   AllowLCUpdate:boolean,
      /**  Flag to indicate if UpliftPercent should be enabled.  */  
   AllowUplift:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Display field used for container landed costs.  */  
   DispLandedCost:number,
      /**  Logical used to indicate if all details have been received.  */  
   eshReceived:boolean,
   IntQueID:number,
      /**  Landed cost message used to inform the user on retrieval of data that the applied and landed costs do not equal.  */  
   LCMessage:string,
   LegalNumberMessage:string,
      /**  This field is used to hold the original total landed cost for containers for all plants.  */  
   OrigLandedCost:number,
      /**  The formatted address Information from Vendor or VendorPP  */  
   AddrListFormatted:string,
   BitFlag:number,
   PurPointName:string,
   PurPointCountry:string,
   PurPointState:string,
   PurPointAddress3:string,
   PurPointAddress1:string,
   PurPointPrimPCon:number,
   PurPointAddress2:string,
   PurPointCity:string,
   PurPointZip:string,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   TaxRegionCodeDescription:string,
   VendorNumState:string,
   VendorNumTermsCode:string,
   VendorNumVendorID:string,
   VendorNumAddress2:string,
   VendorNumCity:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumName:string,
   VendorNumZIP:string,
   VendorNumCountry:string,
   VendorNumAddress3:string,
   VendorNumAddress1:string,
   vrPONumCNBonded:boolean,
   vrPONumShipToConName:string,
   vrPONumShipName:string,
   XbSystReceiptTaxCalculate:boolean,
   XbSystAPTaxLnLevel:boolean,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param whereClause
      @param PONum
      @param POLine
      @param PORel
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
      /**  The criteria  */  
   whereClause:string,
      /**  PONum - Purchase Order Number  */  
   PONum:number,
      /**  POLine - Line  */  
   POLine:number,
      /**  PORel - Release  */  
   PORel:number,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ICReceiptSearchTableset[],
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

export interface RcvHeadBeforeDelete_output{
}

export interface RcvHeadBeforeGetNew_output{
}

export interface RcvHeadBeforeUpdate_output{
}

