import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.LotTraceSvc
// Description: Service to perform traces on part/lots
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotTraceSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotTraceSvc/$metadata", {
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
   Summary: Invoke method PerformTrace
   Description: Performs a trace on the specified part/lot
   OperationID: PerformTrace
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PerformTrace_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformTrace_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerformTrace(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotTraceSvc/PerformTrace", {
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
export interface Erp_Tablesets_LotTraceDtlRow{
      /**   Code that indicates if data was generated for Forward or Reverse mode:

F = Forward / R = Reverse  */  
   TraceMode:string,
      /**   Code that indicates what type of demand/supply record involves:

O = Sales Order               
T = Transfer Order
M = Job Mtl
P = Purchase Order  */  
   Type:string,
      /**  TranNum from related PartTran  */  
   TranNum:number,
      /**  Transaction Qty from related PartTran  */  
   TranQty:number,
      /**  Transaction Qty Unit of Measure from related PartTran  */  
   TranUOM:string,
      /**  Transaction date from related PartTran  */  
   TranDate:string,
      /**  PartNum from related PartTran  */  
   TranPartNum:string,
      /**  Order Number when type is Sales Order  */  
   OrderNum:number,
      /**  ID of related customer when type is Sales Order  */  
   CustID:string,
      /**  Name of related customer when type is Sales Order  */  
   CustName:string,
      /**  Job Number of related material when type is JobMtl  */  
   JobNum:string,
      /**  Assembly Seq of related material when type is JobMtl  */  
   AsmSeq:number,
      /**  Material Seq of related material when type is JobMtl  */  
   MtlSeq:number,
      /**  PartNum of the produced part from related job when type is JobMtl  */  
   PartNum:string,
      /**  LotNum of the produced part from related job when type is JobMtl  */  
   LotNum:string,
      /**  PartLotDescription of the produced part from related job when type is JobMtl  */  
   LotDesc:string,
      /**  Transfer Order Num when type is Transfer Order  */  
   TFOrdNum:string,
      /**   To Site when type is Transfer Order and mode is Forward
From Site when type is Transfer Order and mode is Reverse  */  
   TFSite:string,
      /**   Ship Date from Customer Shipment when type is Sales Order
Ship Date from Transfer Order when type is Transfer Order  */  
   ShipDate:string,
      /**   Date parent material was issued when mode is Forward
Date material was issued to the parent when mode is Reverse  */  
   IssueDate:string,
      /**   Order Date from Sales Order when type is Sales Order
Order Date from Transfer Order when type is Transfer Order
Order Date from Purchase Order when type is Purchase Order  */  
   OrderDate:string,
      /**  Purchase Order Number when type is Purchase Order  */  
   PONum:number,
      /**  Packing Slip Number from Receipt when type is Purchase Order  */  
   PackSlip:string,
      /**  Supplier ID from Supplier when type is Purchase Order  */  
   SupplierID:string,
      /**  Supplier Name from Supplier when type is Purchase Order  */  
   SupplierName:string,
      /**  SysRowID from PartTran  */  
   SysRowID:string,
   TypeDesc:string,
   TraceModeDesc:string,
      /**  The parent PartNum of this row in the hierarchy of manufactured part/lots  */  
   ParentPartNum:string,
      /**  The parent LogNum of this row in the hierarchy of manufactured part/lots  */  
   ParentLotNum:string,
      /**  Default is blank / "R" for hide on root node  */  
   HideOnNode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LotTraceTableset{
   LotTraceDtl:Erp_Tablesets_LotTraceDtlRow[],
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
      @param traceDirection
      @param partNum
      @param lotNum
   */  
export interface PerformTrace_input{
      /**  Direction to trace. F = Forward / R = Reverse (required)  */  
   traceDirection:string,
      /**  Part to trace (required)  */  
   partNum:string,
      /**  Lot to trace (required)  */  
   lotNum:string,
}

export interface PerformTrace_output{
   returnObj:Erp_Tablesets_LotTraceTableset[],
}

