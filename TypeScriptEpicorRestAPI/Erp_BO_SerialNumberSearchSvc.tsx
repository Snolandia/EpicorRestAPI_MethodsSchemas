import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.SerialNumberSearchSvc
// Description: This process uses 3 tokens to generate a whereclause which is
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumberSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumberSearchSvc/$metadata", {
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
   Summary: Invoke method GetNewSerialNumberSearch
   OperationID: GetNewSerialNumberSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSerialNumberSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialNumberSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSerialNumberSearch(requestBody:GetNewSerialNumberSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSerialNumberSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumberSearchSvc/GetNewSerialNumberSearch", {
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
         resolve(data as GetNewSerialNumberSearch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method _SerialNumberSearch
   Description: To be whenever a search on the serial table is required. Depending on the
contents of the tokens, a specific where clause is determined and returned.
            
ProcessToken contains the Sonoma process name.
GenericToken1 List of field names and corresponding values ~ delimited.
The format of each value pair is (field name)=(value).
GenericToken2 not used.
            
The following is a list of processes supported by this object.
xae65-jb            SerialNoAssign
ProcessToken    = SerialNoAssign
GenericToken1   = SortBy
xae65-ct            Customer transfer                       lib/brwsn
ProcessToken    = SerialNoAssign
GenericToken1   = SortBy
ime20-dg            Issues and returns                      xae65-mi
ProcessToken    = IssuesandReturns
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
ime10-dg            Receipts from manufacturing             xae65-mi
ProcessToken    = ReceiptsfromManufacturing
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
ime30-dg            Inventory transfers                     xae65-mi
ProcessToken    = InventoryTransfer
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
ime30-dg-vs         Inventory transfers                     xae65-mi
ProcessToken    = InventoryTransfer
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
ime40-qa            Inventory quantity adjust               xae65-mi
ProcessToken    = InventoryQtyAdj
GenericToken1   = TranType ~ TranQty ~ WareHseCode
jce10-gj            Processing of jobs                      xae65-mi
ProcessToken    = JobProcessing
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
jce10-js            Job split                               xae65-mi
ProcessToken    = JobSplit
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
mse30-dg            Receive from plant                      xae65-mi
ProcessToken    = PlantReceipt
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae10-in            NonConformance Entry from Inventory     xae65-qr
ProcessToken    = NonConf
GenericToken1   = TranType ~ TranQty ~ WareHseCode
qae10-ma            NonConformance Entry from Job Material  xae65-qr
ProcessToken    = NonConf
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae10-op            NonConformance Entry from Operation     xae65-qr
ProcessToken    = NonConf
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae40-iv            DMR to stock/inventory                  xae65-mi
ProcessToken    = DMRtoInventory
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae40-jm            DMR to job material                     xae65-mi
ProcessToken    = DMRtoJobMtl
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae40-op            DMR to job operation                    xae65-mi
ProcessToken    = DMRtoJobOper
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
qae40-rm            Rejecte material from DMR               xae65-mi
ProcessToken    = RejectfromDMR
GenericToken1   = JobNum ~ TranType ~ TranQty ~ WareHseCode
xa/snleavetrig.i    SN select from receipts                 xae65-pm
ProcessToken    = Receipts
GenericToken1   = null
xa/snleavetrig.i    SN select from shipments                xae65-sh
ProcessToken    = Shipment
GenericToken1   = ShipFrom
xa/snleavetrig.i    SN select from transfer orders          xae65-to
ProcessToken    = TransferOrder
GenericToken1   = ShipFrom
xa/xam65-dg         Serial Number Maintenance
Process Token   = SNMaint
GenericToken1   = SortBy
om/ome80-dt         RMA detail maintentance                 xae65-rm
ProcessToken    = RMADTL
GenericToken1   = RMANum ~ RMALine
om/ome80-re         RMA Receipt maintenance                 xae65-rm
ProcessToken    = RMARCPT
GenericToken1   = RMANum ~ RMALine ~ RMAReceipt
om/ome81-rd         RMA Disposition                         xae65-rm
ProcessToken    = RMADISP
GenericToken1   = RMANum ~ RMALine ~ RMAReceipt ~ RMADisp
xa/xae65-sc         Service Contract Maintenance
Process Token   = ServiceContract
GenericToken1   = Null
SubConShipEntry     Subcontract Shipment Entry (NEW for 8.0)
Process Token = SubConShipment
GenericToken1 = null
Receipt Entry       Receipt Entry - (for Job Subcontract) (NEW for 8.0)
Process Token = SubConReceipts
GenericToken1 = null
   OperationID: _SerialNumberSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/_SerialNumberSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/_SerialNumberSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SerialNumberSearch(requestBody:_SerialNumberSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<_SerialNumberSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumberSearchSvc/_SerialNumberSearch", {
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
         resolve(data as _SerialNumberSearch_output)
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
export interface Erp_Tablesets_SerialNumberSearchRow{
      /**  Token reserved for the process ID  */  
   ProcessToken:string,
      /**  1st generic token.  */  
   GenericToken1:string,
      /**  2nd generic token  */  
   GenericToken2:string,
      /**  Returns where clause based on input tokens.  */  
   WhereClause:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SerialNumberSearchTableset{
   SerialNumberSearch:Erp_Tablesets_SerialNumberSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GetNewSerialNumberSearch_input{
   ds:Erp_Tablesets_SerialNumberSearchTableset[],
}

export interface GetNewSerialNumberSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNumberSearchTableset,
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

   /** Required : 
      @param ds
   */  
export interface _SerialNumberSearch_input{
   ds:Erp_Tablesets_SerialNumberSearchTableset[],
}

export interface _SerialNumberSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNumberSearchTableset,
}
}

