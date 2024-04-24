import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.IMMtlQueueSvc
// Description: MtlQueue outbound integration object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMtlQueueSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMtlQueueSvc/$metadata", {
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
   Summary: Invoke method AckMtlQueue
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckMtlQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckMtlQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckMtlQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AckMtlQueue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMtlQueueSvc/AckMtlQueue", {
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
   Summary: Invoke method CountMtlQueue
   Description: Returns the count of existing IntQueOut records along with the count of updated MtlQueue in the database that IntQueOut records have not yet been created for
   OperationID: CountMtlQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountMtlQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountMtlQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountMtlQueue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMtlQueueSvc/CountMtlQueue", {
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
   Summary: Invoke method GetAllMtlQueue
   Description: Generates IntQueOut and IMMtlQueue rows since the last time this was called and then returns these along with any existing
No difference between GetAllMtlQueue and GetMtlQueue for this object
   OperationID: GetAllMtlQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllMtlQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllMtlQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllMtlQueue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMtlQueueSvc/GetAllMtlQueue", {
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
   Summary: Invoke method GetMtlQueue
   Description: Generates IntQueOut and IMMtlQueue rows since the last time this was called and then returns these along with any existing
No difference between GetAllMtlQueue and GetMtlQueue for this object
   OperationID: GetMtlQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMtlQueue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMMtlQueueSvc/GetMtlQueue", {
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
export interface AckMtlQueue_input{
   ts:Erp_Tablesets_IMMtlQueueTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface AckMtlQueue_output{
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
export interface CountMtlQueue_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface CountMtlQueue_output{
parameters : {
      /**  output parameters  */  
   totalCount:number,
}
}

export interface Erp_Tablesets_IMMtlQueueRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  */  
   MtlQueueSeq:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Part Number of item in the container.  */  
   PartNum:string,
      /**  Quantity  */  
   Quantity:number,
      /**   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  */  
   TranType:string,
      /**  Employee ID that has selected this record from the queue for processing.  */  
   SelectedByEmpID:string,
      /**  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  */  
   ToWhse:string,
      /**  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  */  
   ToBinNum:string,
      /**  Part Revision number  */  
   RevisionNum:string,
      /**  Internal unit of measure.  */  
   IUM:string,
      /**  Lot Number of the part.  */  
   LotNum:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The PCID from which the material movement will occur.  */  
   FromPCID:string,
      /**  The PCID to which the material movement will occur.  */  
   ToPCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Service Order Resource Num from FSA  */  
   FSAServiceOrderResourceNum:number,
      /**  Unique identifier for transaction  */  
   IntQueID:number,
      /**  Service Order Number from FSA  */  
   FSAServiceOrderNum:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMMtlQueueTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMMtlQueue:Erp_Tablesets_IMMtlQueueRow[],
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
export interface GetAllMtlQueue_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetAllMtlQueue_output{
   returnObj:Erp_Tablesets_IMMtlQueueTableset[],
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
export interface GetMtlQueue_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetMtlQueue_output{
   returnObj:Erp_Tablesets_IMMtlQueueTableset[],
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

