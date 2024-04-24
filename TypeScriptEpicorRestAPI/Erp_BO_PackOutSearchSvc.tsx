import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PackOutSearchSvc
// Description: This object replaces the current Warehouse object in some cases
           when building the combo-boxes/searches.  This is a non-standard
           object that will include shared warehouses in the result list
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackOutSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackOutSearchSvc/$metadata", {
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
   Summary: Invoke method GetRows
   Description: Get PackOut rows and filter them through POGetRows.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClause:string, matchField:string, orderNum:string, packNum:string, pcid:string, packMode:string, epicorHeaders?:Headers){
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
   if(typeof matchField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "matchField=" + matchField
   }
   if(typeof orderNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderNum=" + orderNum
   }
   if(typeof packNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packNum=" + packNum
   }
   if(typeof pcid!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pcid=" + pcid
   }
   if(typeof packMode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packMode=" + packMode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackOutSearchSvc/GetRows" + params, {
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
   Summary: Invoke method POGetRows
   Description: This methods will return all of the ttPackOut search records.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table we need our own public method.
   OperationID: POGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POGetRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackOutSearchSvc/POGetRows", {
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
   Summary: Invoke method TFOrderGetRows
   Description: Get PackOut rows and filter them through POGetRows.
   OperationID: Get_TFOrderGetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/TFOrderGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_TFOrderGetRows(matchField:string, packNum:string, orderNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof matchField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "matchField=" + matchField
   }
   if(typeof packNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packNum=" + packNum
   }
   if(typeof orderNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderNum=" + orderNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PackOutSearchSvc/TFOrderGetRows" + params, {
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
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POSNFormatRow{
      /**  Company  */  
   Company:string,
   HasSerialNumbers:boolean,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  PartNum  */  
   PartNum:string,
      /**  Serial Number base data type  */  
   SNBaseDataType:string,
      /**  Serial Number format  */  
   SNFormat:string,
      /**  Current Prefix setting  */  
   SNPrefix:string,
   Plant:string,
   SNLastUsedSeq:string,
   SNMask:string,
   SNMaskPrefix:string,
   SNMaskSuffix:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POSelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  PartNum  */  
   PartNum:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reference field  */  
   Reference:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
   SNPrefix:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask that was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
      /**  Used only by SN Assignment, needed here to keep POSelectedSerialNumbers in sync with SelectedSerialNumbers  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: needed here to keep POSelctedSerialNumbers in sync with SelectedSerialNumbers  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PackOutRow{
   Company:string,
   PackNum:number,
   ShipViaCode:string,
   EntryPerson:string,
   LabelComment:string,
   ShipComment:string,
   ShipToNum:string,
   CustNum:number,
   PackLine:number,
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   LineType:string,
   OurInventoryShipQty:number,
   OurJobShipQty:number,
   JobNum:string,
   PartNum:string,
   LineDesc:string,
   RevisionNum:string,
   ShipCmpl:boolean,
   BinNum:string,
   ShpConNum:number,
   LotNum:string,
   DimCode:string,
   DUM:string,
   DimConvFactor:number,
   InvoiceComment:string,
   ShipStatus:string,
   Stage:string,
   BTCustomerName:string,
   BTConNum:number,
   BTCustID:string,
   InvQty:number,
   PackQty:number,
   ShipAddr:string,
   StockPart:boolean,
   CustName:string,
   KitPartNum:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   KitNumPartDescription:string,
   KitPartRev:string,
   PartNumTrackDimension:boolean,
   TotRelQty:number,
   PromptPartRev:boolean,
   PromptKitRevision:boolean,
   PromptJobNum:boolean,
   PromptOrderRel:boolean,
   PromptKit:boolean,
   AutoQuantity:boolean,
   PromptOrderLine:boolean,
   ToPlant:string,
   FromPlant:string,
   FromAddr:string,
   PackMode:string,
   WarehouseCode:string,
   PartNumTrackLots:boolean,
   TFOrdNum:string,
   BTCustNum:number,
   AssemblySeq:number,
   OprSeq:number,
   VendorNum:number,
   PurPoint:string,
   WarehouseCodeDescription:string,
   NumMatchs:number,
      /**  Unique identifer for the PackOut dataset  */  
   PackOutNum:number,
   Plant:string,
   IsInvoiced:boolean,
   MFTransNum:string,
   TrackingNumber:string,
   MFCallTag:string,
   MFPickUpNum:string,
   MFZone:string,
   MFFreightAmt:number,
   MFDiscFreight:number,
   MFOtherAmt:number,
   MFOversized:boolean,
   MFTemplate:string,
   MFDimWeight:number,
   ShipDate:string,
   VendorID:string,
   Quantity:number,
   TotPackedQty:number,
   RemainQty:number,
   ShipViaDescription:string,
      /**  Set from ShipHead.HasCartonLines  */  
   HasCartonLines:boolean,
   PONum:number,
   POLine:number,
   PORelNum:number,
      /**  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  */  
   EnableWeight:boolean,
   ShipStatusXlate:string,
   PkgCode:string,
   PkgClass:string,
   KitFlag:string,
      /**  Height of packaging  */  
   PkgHeight:number,
      /**  If zero the packaging height prompt is enabled.  */  
   PkgHeightEnable:number,
      /**  Length of packaging  */  
   PkgLength:number,
      /**  Zero indicates the length is to be enabled.  */  
   PkgLenEnable:number,
      /**  Width of packaging  */  
   PkgWidth:number,
      /**  Zero indicates the width prompt is enabled.  */  
   PkgWidthEnable:number,
   WayBillNbr:string,
   FreightedShipViaCode:string,
      /**  COD Amount  */  
   CODAmount:number,
      /**  Decared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Logical indicating this pack has phantom cases.  Used by UI to disable phantom controlled fields.  */  
   PhantomPack:boolean,
      /**  Pack weight.  */  
   Weight:number,
      /**  Masterpack PackID this pack is on.  */  
   MasterpackPackNum:number,
      /**  Enables the Warehouse and Bin fields on the UIApp  */  
   EnableWhseBin:boolean,
      /**  0 indicates Pkg Size UOM should be enabled  */  
   PkgSizeUOMEnable:number,
   PkgSizeUOM:string,
   WeightUOM:string,
   InventoryShipUOM:string,
   JobShipUOM:string,
   EnablePOSerialBtn:boolean,
   DocumentPrinted:boolean,
      /**  Ship To Customer  */  
   ShipToCustNum:number,
      /**  Boolean indicating if the package control functionality should be enabled.  */  
   EnablePackageControl:boolean,
   PCID:string,
   ShipToWarning:string,
      /**  temp message to display newly created legal number  */  
   LegalNumberMessage:string,
      /**  Legal Number associated with pack  */  
   LegalNumber:string,
      /**  TranDocTypeID associated with Pack.  */  
   TranDocTypeID:string,
      /**  TranDocType Description associated with this Pack  */  
   TranDocTypeDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   PartNumAttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   KitAttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   KitAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   KitAttributeSetShortDescription:string,
   PartNumTrackInventoryAttributes:boolean,
   EnableAttributeSetSearch:boolean,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates if a legal number configuration exists for pack out  */  
   HasLegNumCnfg:boolean,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
   TrackInventoryByRevision:boolean,
   ReadyToInvoice:boolean,
      /**  Indicates if Ready to Invoice is enabled or not  */  
   EnableReadyToInvoice:boolean,
      /**  Indicates if the record is inactive.  */  
   ShipToInactive:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PackOutTableset{
   PackOut:Erp_Tablesets_PackOutRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   POSelectedSerialNumbers:Erp_Tablesets_POSelectedSerialNumbersRow[],
   POSNFormat:Erp_Tablesets_POSNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param whereClause
      @param matchField
      @param orderNum
      @param packNum
      @param pcid
      @param packMode
   */  
export interface GetRows_input{
   whereClause:string,
   matchField:string,
   orderNum:number,
   packNum:number,
   pcid:string,
   packMode:string,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PackOutTableset[],
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
      @param whereClausettPackOutSearch
      @param matchfield
      @param ds
   */  
export interface POGetRows_input{
      /**  The where clause to restrict data for  */  
   whereClausettPackOutSearch:string,
      /**  comma delimited list of field to find unique hits  */  
   matchfield:string,
   ds:Erp_Tablesets_PackOutTableset[],
}

export interface POGetRows_output{
   returnObj:Erp_Tablesets_PackOutTableset[],
}

   /** Required : 
      @param matchField
      @param packNum
      @param orderNum
   */  
export interface TFOrderGetRows_input{
   matchField:string,
   packNum:number,
   orderNum:string,
}

export interface TFOrderGetRows_output{
   returnObj:Erp_Tablesets_PackOutTableset[],
}

