import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.IMRMAHeadSvc
// Description: Business Object to handle: Add, Update, Delete of RMAHead
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMRMAHeadSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMRMAHeadSvc/$metadata", {
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
   Summary: Invoke method AddRMAHead
   Description: Add RMAHead related tables
   OperationID: AddRMAHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddRMAHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRMAHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddRMAHead(requestBody:AddRMAHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddRMAHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMRMAHeadSvc/AddRMAHead", {
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
         resolve(data as AddRMAHead_output)
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
      @param IMRMAHeadTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param saveAddOnError
      @param imIntegrationKey
   */  
export interface AddRMAHead_input{
   IMRMAHeadTableset:Erp_Tablesets_IMRMAHeadTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
   saveAddOnError:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset[],
}

export interface AddRMAHead_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset,
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

export interface Erp_Tablesets_IMNaturalKeysRow{
   KeyValue:string,
   KeyColumn:string,
   Sequence:number,
   PrimaryKey:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMRMADtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Return Authorization Number. Used to relate RMADtl to RMAHead.  */  
   RMANum:number,
      /**  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  */  
   RMALine:number,
      /**  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  */  
   ReturnReasonCode:string,
      /**   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  */  
   Note:string,
      /**  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  */  
   PartNum:string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   LineDesc:string,
      /**  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  */  
   RevisionNum:string,
      /**  Quantity that is to be returned  */  
   ReturnQty:number,
      /**  Unit Of Measure of the  ReturnQty.  */  
   ReturnQtyUOM:string,
      /**  The Ship to number of the related header contact.  */  
   ShipToNum:string,
      /**  The Contact Number of the related header contact  */  
   ConNum:number,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   CustNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Unique identifier for transaction  */  
   IntQueID:number,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Unique identifier of related integration record. The value is  GUID.  */  
   ExternalKey:string,
      /**  Call Code  */  
   CallCode:string,
      /**  Employee ID  */  
   EmpID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMRMAHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  */  
   RMANum:number,
      /**  Date of the Return Material Authorization.  Default as System date.  */  
   RMADate:string,
      /**  Contains the system internal customer number used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The Ship to number of the related header contact.  */  
   ShipToNum:string,
      /**  The Contact Number of the related header contact  */  
   ConNum:number,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Comments about the RMA overall  */  
   RMAComment:string,
      /**  EpicorFSA  */  
   EpicorFSA:boolean,
      /**  Unique identifier for transaction  */  
   IntQueID:number,
      /**  Unique identifier of related integration record. The value is  GUID.  */  
   ExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMRMAHeadTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMRMADtl:Erp_Tablesets_IMRMADtlRow[],
   IMRMAHead:Erp_Tablesets_IMRMAHeadRow[],
   IMRMARcpt:Erp_Tablesets_IMRMARcptRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMRMARcptRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Return Authorization Number of related RMAHead.  */  
   RMANum:number,
      /**  Line # of the related RMADtl record.  */  
   RMALine:number,
      /**  RMA Receipt  */  
   RMAReceipt:number,
      /**  Warehouse ID the item was received into.  Normally this would be a "Inspection" type of warehouse.  */  
   WareHouseCode:string,
      /**  Warehouse Bin location in which the received item was placed.  */  
   BinNum:string,
      /**  Receipt Date  */  
   RcvDate:string,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  The Site that this RMA receipt was received to.  This is set as from the "Current Site" at the time of receipt.  It will be used in the filtering of receipts in the Disposition process.  */  
   Plant:string,
      /**  Quantity that has been received.  */  
   ReceivedQty:number,
      /**  Received Quantity unit of measure.  */  
   ReceivedQtyUOM:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Unique identifier for transaction.  */  
   IntQueID:number,
   SerialNumber:string,
      /**  Unique identifier of related integration record. The value is  GUID.  */  
   ExternalKey:string,
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

