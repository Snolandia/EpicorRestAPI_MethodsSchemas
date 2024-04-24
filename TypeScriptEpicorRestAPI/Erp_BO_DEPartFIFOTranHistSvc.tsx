import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.DEPartFIFOTranHistSvc
// Description: Germany Part FIFO Transaction History BO
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DEPartFIFOTranHistSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DEPartFIFOTranHistSvc/$metadata", {
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
   Summary: Invoke method GetPartFIFOTranHistory
   Description: Retrieve Part FIFO Transaction History for specific Part and Date interval.
The Running Balance is calculated.
   OperationID: GetPartFIFOTranHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFIFOTranHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFIFOTranHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFIFOTranHistory(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DEPartFIFOTranHistSvc/GetPartFIFOTranHistory", {
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
export interface Erp_Tablesets_DEPartFIFOTranHistRow{
      /**  Company  */  
   Company:string,
      /**  Part Num  */  
   PartNum:string,
      /**  Part Description  */  
   PartDescription:string,
      /**  PartIUM  */  
   PartIUM:string,
      /**  Transaction Date  */  
   TranDate:string,
      /**  Transaction Number  */  
   TranNum:number,
      /**  FIFO Date  */  
   FIFODate:string,
      /**  FIFO Seq  */  
   FIFOSeq:number,
      /**  FIFO Sub Seq  */  
   FIFOSubSeq:number,
      /**  Transaction Type  */  
   TranType:string,
      /**  FIFO Action  */  
   FIFOAction:string,
      /**  Tran Qty  */  
   TranQty:number,
      /**  Unit Cost  */  
   UnitCost:number,
      /**  Ext Cost  */  
   ExtCost:number,
      /**  Total Part Quantity before transaction.  */  
   OpenQty:number,
      /**  Total Part Ext Cost before transaction.  */  
   OpenExtCost:number,
      /**  Total Part Quantity after transaction.  */  
   CloseQty:number,
      /**  Total Part Ext Cost after transaction.  */  
   CloseExtCost:number,
      /**  PO Number  */  
   PONum:number,
      /**  Packing Slip  */  
   PackSlip:string,
      /**  Order Number  */  
   OrderNum:number,
      /**  Pack Number  */  
   PackNum:number,
      /**  Pack Type  */  
   PackType:string,
      /**  Trans Reference  */  
   TranReference:string,
      /**  Warehouse Code  */  
   WareHouseCode:string,
      /**  Bin Num  */  
   BinNum:string,
      /**  Job Number  */  
   JobNum:string,
      /**  DMR Number  */  
   DMRNum:number,
      /**  RMA Number  */  
   RMANum:number,
      /**  System Entry Date and Time  */  
   SysEntryDT:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DEPartFIFOTranHistTableset{
   DEPartFIFOTranHist:Erp_Tablesets_DEPartFIFOTranHistRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
      @param startDate
      @param endDate
   */  
export interface GetPartFIFOTranHistory_input{
      /**  Part  */  
   partNum:string,
      /**  Start Date of the interval  */  
   startDate:string,
      /**  End Date of the interval  */  
   endDate:string,
}

export interface GetPartFIFOTranHistory_output{
   returnObj:Erp_Tablesets_DEPartFIFOTranHistTableset[],
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

