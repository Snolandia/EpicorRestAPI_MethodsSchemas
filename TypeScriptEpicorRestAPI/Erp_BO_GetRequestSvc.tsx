import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.GetRequestSvc
// Description: Material Get Request
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", {
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
   Summary: Invoke method CheckEmployee
   Description: This method needs to be called from the main menu only.  if the object
is being called from the shop floor menu then the employee id has already been determined
and validated and is passed in
   OperationID: CheckEmployee
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckEmployee_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEmployee_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckEmployee(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/CheckEmployee", {
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
   Summary: Invoke method GetNewEmpInfo
   Description: Call this method to create a new Epicor.Mfg.BO.GetRequestDataSet with Job#
   OperationID: GetNewEmpInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/GetNewEmpInfo", {
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
   Summary: Invoke method OnChangeAssembly
   Description: Call this method to update the dataset when the GetRequest.AssemblySeq is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/OnChangeAssembly", {
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
   Summary: Invoke method OnChangeCalcHours
   Description: Call this method to update the dataset when the GetRequest.CalcHours is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeCalcHours
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCalcHours_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalcHours_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCalcHours(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/OnChangeCalcHours", {
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
   Summary: Invoke method OnChangeCalcOption
   Description: Call this method to update the dataset when the GetRequest.CalcOption is changed
Valid values are "O" - Outstanding, "P" - Pieces, "H" - hours
CalcHours only enabled for "H" and CalcPieces only enabled for "P"
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeCalcOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCalcOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalcOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCalcOption(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/OnChangeCalcOption", {
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
   Summary: Invoke method OnChangeCalcPieces
   Description: Call this method to update the dataset when the GetRequest.CalcPieces is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeCalcPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCalcPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalcPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCalcPieces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/OnChangeCalcPieces", {
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
   Summary: Invoke method OnChangeJobNum
   Description: Call this method to update the dataset when the GetRequest.JobNum is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/OnChangeJobNum", {
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
   Summary: Invoke method OnChangeOpr
   Description: Call this method to update the dataset when the GetRequest.OprSeq is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/OnChangeOpr", {
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
   Summary: Invoke method OnChangeRequestQtyUOM
   Description: Call this method when the value of Epicor.Mfg.BO.GetRequestDataSet.RequestQtyUOM changes.
   OperationID: OnChangeRequestQtyUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRequestQtyUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRequestQtyUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRequestQtyUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/OnChangeRequestQtyUOM", {
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
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new request qty
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/OnChangingNumberOfPieces", {
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
   Summary: Invoke method OnChangeRequestQty
   Description: Call this method when the value of Epicor.Mfg.BO.GetRequestDataSet.RequestQty changes.
   OperationID: OnChangeRequestQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRequestQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRequestQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRequestQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/OnChangeRequestQty", {
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
   Summary: Invoke method ProcessLines
   Description: Run this method when done updating all the detail lines (currently OK button in 6.1)
clear screen when done
Must set the GetRequest RowMod to "U" for this method to work
   OperationID: ProcessLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessLines(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/ProcessLines", {
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
      @param empID
   */  
export interface CheckEmployee_input{
      /**  Employee ID  */  
   empID:string,
}

export interface CheckEmployee_output{
parameters : {
      /**  output parameters  */  
   empName:string,
}
}

export interface Erp_Tablesets_GetRequestRow{
   JobNum:string,
   JobPartNum:string,
   JobPartDesc:string,
   AssemblySeq:number,
   AsmPartNum:string,
   AsmPartDesc:string,
   OprSeq:number,
   OpCode:string,
   CalcOption:string,
   CalcPieces:number,
   CalcHours:number,
   NeedByDate:string,
   NeedByTime:number,
   RunQty:number,
   EstProdHours:number,
   QtyCompleted:number,
   CompletedHours:number,
   QtyRemaining:number,
   RemaingHours:number,
   OPDesc:string,
   EmpID:string,
   EmpName:string,
      /**  Dumy unique key  */  
   DummyKeyField:string,
   CalcPiecesUOM:string,
   RunQtyUOM:string,
   QtyCompletedUOM:string,
   QtyRemainingUOM:string,
   Warning:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   AsmRevisionNum:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   JobRevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GetRequestTableset{
   GetRequest:Erp_Tablesets_GetRequestRow[],
   RequestLines:Erp_Tablesets_RequestLinesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RequestLinesRow{
   JobNum:string,
   AssemblySeq:number,
   JobSeq:number,
   JobSeqType:string,
   PartNum:string,
   Description:string,
   RequiredQty:number,
   QtyIssued:number,
   QtyStaged:number,
      /**  Unit of Measure used for the transaction  */  
   IUM:string,
   TranType:string,
   MtlQueueQty:number,
   RequestQty:number,
   NextJobSeq:number,
   FromBinNum:string,
   FromWhse:string,
   ToBinNum:string,
   ToWhse:string,
   DummyKeyField:string,
   DummyLineField:string,
   FromWhseDesc:string,
   FromBinDesc:string,
   ToWhseDesc:string,
   ToBinDesc:string,
      /**  UOM for the Quantity Issued  */  
   IssuedUM:string,
      /**  The quantity value converted from Request UOM to Issued UOM.  */  
   ThisTranQty:number,
   RequiredQtyUOM:string,
   RequestQtyUOM:string,
   QtyStagedUOM:string,
      /**  Requested UOM  */  
   MtlQueueQtyUOM:string,
   QtyIssuedUOM:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   EnableAttributeSetSearch:boolean,
      /**  Site Identifier  */  
   Plant:string,
   FromPCID:string,
   ToPCID:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   TrackInventoryByRevision:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param empID
      @param ds
   */  
export interface GetNewEmpInfo_input{
      /**  Employee ID  */  
   empID:string,
   ds:Erp_Tablesets_GetRequestTableset[],
}

export interface GetNewEmpInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetRequestTableset[],
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
      @param assemblySeq
      @param ds
   */  
export interface OnChangeAssembly_input{
      /**  AssemblySeq  */  
   assemblySeq:number,
   ds:Erp_Tablesets_GetRequestTableset[],
}

export interface OnChangeAssembly_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetRequestTableset[],
}
}

   /** Required : 
      @param hours
      @param ds
   */  
export interface OnChangeCalcHours_input{
      /**  Hours  */  
   hours:number,
   ds:Erp_Tablesets_GetRequestTableset[],
}

export interface OnChangeCalcHours_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetRequestTableset[],
}
}

   /** Required : 
      @param calcOption
      @param ds
   */  
export interface OnChangeCalcOption_input{
      /**  calcOption  */  
   calcOption:string,
   ds:Erp_Tablesets_GetRequestTableset[],
}

export interface OnChangeCalcOption_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetRequestTableset[],
}
}

   /** Required : 
      @param pieces
      @param ds
   */  
export interface OnChangeCalcPieces_input{
      /**  Pieces  */  
   pieces:number,
   ds:Erp_Tablesets_GetRequestTableset[],
}

export interface OnChangeCalcPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetRequestTableset[],
}
}

   /** Required : 
      @param jobNum
      @param ds
   */  
export interface OnChangeJobNum_input{
      /**  JobNum  */  
   jobNum:string,
   ds:Erp_Tablesets_GetRequestTableset[],
}

export interface OnChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetRequestTableset[],
}
}

   /** Required : 
      @param oprSeq
      @param ds
   */  
export interface OnChangeOpr_input{
      /**  OprSeq  */  
   oprSeq:number,
   ds:Erp_Tablesets_GetRequestTableset[],
}

export interface OnChangeOpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetRequestTableset[],
}
}

   /** Required : 
      @param pRequestQtyUOM
      @param seq
      @param ds
   */  
export interface OnChangeRequestQtyUOM_input{
      /**  RequestQtyUOM  */  
   pRequestQtyUOM:string,
      /**  seq  */  
   seq:number,
   ds:Erp_Tablesets_GetRequestTableset[],
}

export interface OnChangeRequestQtyUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetRequestTableset[],
}
}

   /** Required : 
      @param pdRequestQty
      @param seq
      @param ds
   */  
export interface OnChangeRequestQty_input{
      /**  Request Qty  */  
   pdRequestQty:number,
      /**  seq  */  
   seq:number,
   ds:Erp_Tablesets_GetRequestTableset[],
}

export interface OnChangeRequestQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetRequestTableset[],
}
}

   /** Required : 
      @param numberOfPieces
      @param seq
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
      /**  seq  */  
   seq:number,
   ds:Erp_Tablesets_GetRequestTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetRequestTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessLines_input{
   ds:Erp_Tablesets_GetRequestTableset[],
}

export interface ProcessLines_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetRequestTableset[],
}
}

