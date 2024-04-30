import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CreateIDNumbersSvc
// Description: Service for generating ID Numbers
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/$metadata", {
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
   Summary: Invoke method GetCreateIDNumbersParams
   OperationID: GetCreateIDNumbersParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCreateIDNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCreateIDNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCreateIDNumbersParams(requestBody:GetCreateIDNumbersParams_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCreateIDNumbersParams_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/GetCreateIDNumbersParams", {
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
         resolve(data as GetCreateIDNumbersParams_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingFormatID
   Description: Call this method when the value of Epicor.Mfg.BO.CreateIDNumbersParams.FormatID is changing.
   OperationID: OnChangingFormatID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingFormatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingFormatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingFormatID(requestBody:OnChangingFormatID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingFormatID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/OnChangingFormatID", {
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
         resolve(data as OnChangingFormatID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSerialNumber
   Description: Validates the entered Serial
   OperationID: ValidateSerialNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSerialNumber(requestBody:ValidateSerialNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSerialNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/ValidateSerialNumber", {
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
         resolve(data as ValidateSerialNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetIDNumberShipmentStatusNoClear
   Description: Public method to set ID Numbers as shipped or not and do not clear ds at the end.
   OperationID: SetIDNumberShipmentStatusNoClear
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetIDNumberShipmentStatusNoClear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetIDNumberShipmentStatusNoClear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetIDNumberShipmentStatusNoClear(requestBody:SetIDNumberShipmentStatusNoClear_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetIDNumberShipmentStatusNoClear_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/SetIDNumberShipmentStatusNoClear", {
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
         resolve(data as SetIDNumberShipmentStatusNoClear_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetIDNumberShipmentStatus
   Description: Public method to set ID Numbers as shipped or not.
   OperationID: SetIDNumberShipmentStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetIDNumberShipmentStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetIDNumberShipmentStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetIDNumberShipmentStatus(requestBody:SetIDNumberShipmentStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetIDNumberShipmentStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/SetIDNumberShipmentStatus", {
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
         resolve(data as SetIDNumberShipmentStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignSerialsToIDNumbers
   Description: Public method to assign serials to ID Numbers.
   OperationID: AssignSerialsToIDNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AssignSerialsToIDNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignSerialsToIDNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignSerialsToIDNumbers(requestBody:AssignSerialsToIDNumbers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AssignSerialsToIDNumbers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/AssignSerialsToIDNumbers", {
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
         resolve(data as AssignSerialsToIDNumbers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignSerialandSetID
   Description: Method covering existing functionality in to a single method - AssignSerialsToIDNumbers, and SetIDNumberShipmentStatusNoClear
   OperationID: AssignSerialandSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AssignSerialandSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignSerialandSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignSerialandSetID(requestBody:AssignSerialandSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AssignSerialandSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/AssignSerialandSetID", {
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
         resolve(data as AssignSerialandSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateIDNumbers
   Description: Public method to create ID Numbers.
   OperationID: CreateIDNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateIDNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateIDNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateIDNumbers(requestBody:CreateIDNumbers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateIDNumbers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/CreateIDNumbers", {
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
         resolve(data as CreateIDNumbers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistIDFormat
   Description: Public method to check id ID Format Exists.
   OperationID: ExistIDFormat
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistIDFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistIDFormat(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistIDFormat_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreateIDNumbersSvc/ExistIDFormat", {
          method: 'post',
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
         resolve(data as ExistIDFormat_output)
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
      @param ds
   */  
export interface AssignSerialandSetID_input{
   ds:Erp_Tablesets_CreateIDNumbersTableset[],
}

export interface AssignSerialandSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreateIDNumbersTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface AssignSerialsToIDNumbers_input{
   ds:Erp_Tablesets_CreateIDNumbersTableset[],
}

export interface AssignSerialsToIDNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreateIDNumbersTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CreateIDNumbers_input{
   ds:Erp_Tablesets_CreateIDNumbersParamsTableset[],
}

export interface CreateIDNumbers_output{
   returnObj:Erp_Tablesets_CreateIDNumbersTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreateIDNumbersParamsTableset,
}
}

export interface Erp_Tablesets_CreateIDNumbersParamsRow{
   FormatID:string,
   PartNum:string,
   Quantity:number,
   SourceRowID:string,
   AssignedQty:number,
   BinNum:string,
   Company:string,
   EnableIDAddButton:boolean,
   IDNumberSample:string,
   IDStatus:string,
   IsSystemGenerated:boolean,
   JobNum:string,
   LotNum:string,
   NumberSeq:number,
   OrderLine:number,
   OrderNum:number,
   OrderRelNum:number,
   PackLine:number,
   PackNum:number,
   QtyToAdd:number,
   WarehouseCode:string,
      /**  Bool indicating if this manailly entered full ID number  */  
   IsFullNum:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CreateIDNumbersParamsTableset{
   CreateIDNumbersParams:Erp_Tablesets_CreateIDNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CreateIDNumbersRow{
   Company:string,
   IDNumber:string,
   JobNum:string,
   NotSavedToDB:boolean,
   PackLine:number,
   PackNum:number,
   PartNum:string,
   SeqNum:number,
   SerialNumber:string,
   SourceRowID:string,
   TranType:string,
   BinNum:string,
   LotNum:string,
   OrderLine:number,
   OrderNum:number,
   OrderRelNum:number,
   Selected:boolean,
   Status:string,
   WarehouseCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CreateIDNumbersTableset{
   CreateIDNumbers:Erp_Tablesets_CreateIDNumbersRow[],
   CreateIDNumbersParams:Erp_Tablesets_CreateIDNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface ExistIDFormat_output{
   returnObj:boolean,
}

   /** Required : 
      @param ipPartNum
      @param ipQuantity
      @param ipJobNum
      @param ipFormatID
      @param ipIDStatus
      @param ipPackNum
      @param ipPackLine
   */  
export interface GetCreateIDNumbersParams_input{
      /**  ipPartNum  */  
   ipPartNum:string,
      /**  ipQuantity  */  
   ipQuantity:number,
      /**  ipJobNum  */  
   ipJobNum:string,
      /**  ipJobNum  */  
   ipFormatID:string,
      /**  ipIDStatus - either WIP or SHIPPED  */  
   ipIDStatus:string,
      /**  ipPackNum  */  
   ipPackNum:number,
      /**  ipPackLine  */  
   ipPackLine:number,
}

export interface GetCreateIDNumbersParams_output{
   returnObj:Erp_Tablesets_CreateIDNumbersTableset[],
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
      @param formatID
   */  
export interface OnChangingFormatID_input{
      /**  Propose FormatID value.  */  
   formatID:string,
}

export interface OnChangingFormatID_output{
}

   /** Required : 
      @param ds
   */  
export interface SetIDNumberShipmentStatusNoClear_input{
   ds:Erp_Tablesets_CreateIDNumbersTableset[],
}

export interface SetIDNumberShipmentStatusNoClear_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreateIDNumbersTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface SetIDNumberShipmentStatus_input{
   ds:Erp_Tablesets_CreateIDNumbersTableset[],
}

export interface SetIDNumberShipmentStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreateIDNumbersTableset,
}
}

   /** Required : 
      @param ds
      @param SerialNumber
   */  
export interface ValidateSerialNumber_input{
   ds:Erp_Tablesets_CreateIDNumbersTableset[],
      /**  Proposed Serial number to validate  */  
   SerialNumber:string,
}

export interface ValidateSerialNumber_output{
}

