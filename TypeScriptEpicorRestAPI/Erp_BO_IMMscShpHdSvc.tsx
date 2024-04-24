import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.IMMscShpHdSvc
// Description: Outbound integration point for MscShpHd and MscShpDt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMscShpHdSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMscShpHdSvc/$metadata", {
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
   Summary: Invoke method AckMscShpHd
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckMscShpHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckMscShpHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckMscShpHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AckMscShpHd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMscShpHdSvc/AckMscShpHd", {
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
   Summary: Invoke method CountMscShpHd
   Description: Returns the count of existing IntQueOut records along with the count of updated MscShpHd in the database that IntQueOut records have not yet been created
   OperationID: CountMscShpHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountMscShpHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountMscShpHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountMscShpHd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMscShpHdSvc/CountMscShpHd", {
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
   Summary: Invoke method GetAllMscShpHd
   Description: Generates IntQueOut and IMMscShpHd rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllMscShpHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllMscShpHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllMscShpHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllMscShpHd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMscShpHdSvc/GetAllMscShpHd", {
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
   Summary: Invoke method GetMscShpHd
   Description: Generates IntQueOut and IMMscShpHd rows since the last time this was called and then returns these along with any existing
   OperationID: GetMscShpHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMscShpHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMscShpHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMscShpHd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMscShpHdSvc/GetMscShpHd", {
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
export interface AckMscShpHd_input{
   ts:Erp_Tablesets_IMMscShpHdTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface AckMscShpHd_output{
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
export interface CountMscShpHd_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface CountMscShpHd_output{
parameters : {
      /**  output parameters  */  
   totalCount:number,
}
}

export interface Erp_Tablesets_IMMscShpDtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Number of Packages.  */  
   Packages:number,
      /**  Part number of item actually shipped.  */  
   PartNum:string,
      /**  Unit of measure  */  
   IUM:string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   RevisionNum:string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   ShipComment:string,
      /**  Lot Number is defaulted as Job Number.  */  
   LotNum:string,
      /**  Holds the Quantity onhand for this Part in the warehouse in the specific bin location.  Whenever this quantity becomes zero the record should be deleted. This quantity needs to added to or subtracted from Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse Transfers, Shipping and Adjustments.  */  
   Quantity:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Unique identifier for transaction.  */  
   IntQueID:number,
      /**  The installation price, if installation is required.  */  
   FSAInstallationCost:number,
      /**  True if a service order for installation is required.  */  
   FSAInstallationRequired:boolean,
      /**  The installation type, if installation is required.  */  
   FSAInstallationType:string,
      /**  True if delivery service order is required.  */  
   FSARequiresServiceOrder:boolean,
      /**  Template Service Order ID from FSAInstallationType  */  
   FSATemplateServiceOrderID:number,
   IntSysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMMscShpHdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available number is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master.  Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   ShipComment:string,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   Name:string,
      /**  The first line of the main address.  */  
   Address1:string,
      /**  The second line of the main address.  */  
   Address2:string,
      /**  The third line of the main address.  */  
   Address3:string,
      /**  The city portion of the shipping  address.  */  
   City:string,
      /**  State ID for the ShipTo.  Can be blank.  */  
   State:string,
      /**  The zip or postal code portion of the shipping  address.  */  
   ZIP:string,
      /**  The country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGCOTMark  */  
   AGCOTMark:boolean,
      /**  SignedOn  */  
   SignedOn:string,
      /**  SignedBy  */  
   SignedBy:string,
      /**  EpicorFSA  */  
   EpicorFSA:boolean,
      /**  Unique identifier for transaction  */  
   IntQueID:number,
      /**  The related Service Order Number from FSA  */  
   FSAServiceOrderNum:number,
      /**  The related Service Order Resource Number from Epicor FSA  */  
   FSAServiceOrderResourceNum:number,
   IntSysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMMscShpHdTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMMscShpDt:Erp_Tablesets_IMMscShpDtRow[],
   IMMscShpHd:Erp_Tablesets_IMMscShpHdRow[],
   IMSerialNo:Erp_Tablesets_IMSerialNoRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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
export interface GetAllMscShpHd_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetAllMscShpHd_output{
   returnObj:Erp_Tablesets_IMMscShpHdTableset[],
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
export interface GetMscShpHd_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetMscShpHd_output{
   returnObj:Erp_Tablesets_IMMscShpHdTableset[],
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

