import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.IMShipDtlSvc
// Description: Outbound integration point for ShipDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMShipDtlSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMShipDtlSvc/$metadata", {
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
   Summary: Invoke method AckShipDtl
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AckShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMShipDtlSvc/AckShipDtl", {
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
   Summary: Invoke method CountShipDtl
   Description: Returns the count of existing IntQueOut records along with the count of updated shipments in the database that IntQueOut records have not yet been created for
   OperationID: CountShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMShipDtlSvc/CountShipDtl", {
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
   Summary: Invoke method GetShipDtl
   Description: Generates IntQueOut and IMShipDtl rows since the last time this was called and then returns these along with any existing
   OperationID: GetShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMShipDtlSvc/GetShipDtl", {
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
   Summary: Invoke method GetAllShipDtl
   Description: Generates IntQueOut and IMShipDtl rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMShipDtlSvc/GetAllShipDtl", {
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
      @param ts
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface AckShipDtl_input{
   ts:Erp_Tablesets_IMShipDtlTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface AckShipDtl_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface CountShipDtl_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface CountShipDtl_output{
parameters : {
      /**  output parameters  */  
   totalCount:number,
}
}

export interface Erp_Tablesets_IMSerialNoRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Serial number.  This is part is the unique index for this table.  It can contain prefixes and sufixxes determined during setup of the part.  */  
   SerialNumber:string,
      /**   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  */  
   SNStatus:string,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  LotNumber assigned to the serial number in cycle count/Physical Inventory.  */  
   LotNum:string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Misc Shipment Pack Num if related to a misc shipment  */  
   MscPackNum:number,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
      /**  Misc Shipment Pack Line if related to a Misc Shipment  */  
   MscPackLine:number,
      /**  Identifier of the asset this Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   AssetNum:string,
      /**  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  */  
   AdditionNum:number,
      /**  DisposalNum  */  
   DisposalNum:number,
      /**  Determines if the serial number has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Contains the calculated value of CustID  */  
   CustID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   ShipToName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMShipDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  */  
   OurInventoryShipQty:number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  */  
   OurJobShipQty:number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  */  
   PartNum:string,
      /**  Line Description  */  
   LineDesc:string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   RevisionNum:string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   ShipComment:string,
      /**  Lot Number is for Inventory Shipments.  */  
   LotNum:string,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  */  
   CustNum:number,
      /**  The shipto number. Used for warranty validation.  */  
   ShipToNum:string,
      /**  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  */  
   EffectiveDate:string,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MaterialExpiration:string,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   LaborExpiration:string,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MiscExpiration:string,
      /**  The latest of the 3 warranty expiration dates  */  
   LastExpiration:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  */  
   Plant:string,
      /**  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  */  
   TrackSerialNum:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates that the warranty will be sent to FSA  */  
   WarrantySendToFSA:boolean,
      /**  When the shipment line is marked as "send as equipment", it will create an Installation in Epicor FSA.  */  
   FSAEquipment:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Key of related IntueInOut record  */  
   IntQueID:number,
   IntSysRowID:string,
   FSAInstallationCost:number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   FSAInstallationRequired:boolean,
   FSAInstallationType:string,
   FSATemplateServiceOrderID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMShipDtlTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMSerialNo:Erp_Tablesets_IMSerialNoRow[],
   IMShipDtl:Erp_Tablesets_IMShipDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

   /** Required : 
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param pageSize
      @param absolutePage
   */  
export interface GetAllShipDtl_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetAllShipDtl_output{
   returnObj:Erp_Tablesets_IMShipDtlTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param pageSize
      @param absolutePage
   */  
export interface GetShipDtl_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetShipDtl_output{
   returnObj:Erp_Tablesets_IMShipDtlTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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

