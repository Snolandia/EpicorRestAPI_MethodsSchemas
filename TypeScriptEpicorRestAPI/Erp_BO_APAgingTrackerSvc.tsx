import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.APAgingTrackerSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APAgingTrackerSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APAgingTrackerSvc/$metadata", {
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
   Summary: Invoke method GenerateTrackerAgingSite
   Description: This method should be called to populate the dataset for the AP Aging Tracker.
   OperationID: GenerateTrackerAgingSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateTrackerAgingSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTrackerAgingSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateTrackerAgingSite(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APAgingTrackerSvc/GenerateTrackerAgingSite", {
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
   Summary: Invoke method GenerateTracker
   Description: This method should be called to populate the dataset for the AP Aging Tracker.
   OperationID: GenerateTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APAgingTrackerSvc/GenerateTracker", {
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
export interface Erp_Tablesets_APAgingTotalsRow{
      /**  Company  */  
   Company:string,
   CurNumInv:number,
   InvTotal:number,
   PaidYtd:number,
   YTDNumInv:number,
   PYTDNumInv:number,
   PYTDPurchased:number,
   PYTDAvgInvAmt:number,
   YTDPurchased:number,
   YTDAvgInvAmt:number,
   LastPayment:number,
   LastPaymentDate:string,
   CurDueAmt:number,
   CurDuePct:number,
   Due30Amt:number,
   Due30Pct:number,
   Due60Amt:number,
   Due60Pct:number,
   Due90Amt:number,
   Due90Pct:number,
   Due120Amt:number,
   Due120Pct:number,
   FutureDueAmt:number,
   FutureDuePct:number,
   CurInvAmt:number,
   CurInvPct:number,
   Inv30Amt:number,
   Inv30Pct:number,
   Inv60Amt:number,
   Inv60Pct:number,
   Inv90Amt:number,
   Inv90Pct:number,
   Inv120Amt:number,
   FutureInvAmt:number,
   FutureInvPct:number,
   VendorNum:number,
   VendorName:string,
   Inv120Pct:number,
      /**  Column 1 heading (Current)  */  
   ColHead1:string,
      /**  Column 2 heading (Over 30)  */  
   ColHead2:string,
      /**  Column 3 heading (Over 60)  */  
   ColHead3:string,
      /**  Column 4 heading (Over 90)  */  
   ColHead4:string,
      /**  Column 5 heading (Over 120)  */  
   ColHead5:string,
      /**  Column 6 heading (Future)  */  
   ColHead6:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APAgingTrackerTableset{
   APAgingTotals:Erp_Tablesets_APAgingTotalsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param supplierID
      @param plant
   */  
export interface GenerateTrackerAgingSite_input{
      /**  Supplier ID.  */  
   supplierID:string,
      /**  Supplier ID.  */  
   plant:string,
}

export interface GenerateTrackerAgingSite_output{
   returnObj:Erp_Tablesets_APAgingTrackerTableset[],
}

   /** Required : 
      @param supplierID
   */  
export interface GenerateTracker_input{
      /**  Supplier ID.  */  
   supplierID:string,
}

export interface GenerateTracker_output{
   returnObj:Erp_Tablesets_APAgingTrackerTableset[],
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

