import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.LIB.DataFabricSvc
// Description: Data Fabric Service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/$metadata", {
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
   Summary: Invoke method ListLibraryFunctions
   Description: Get a list of Epicor Functions including whether they are disabled,
invalid or not compatible with the Data Fabric.
   OperationID: ListLibraryFunctions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ListLibraryFunctions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListLibraryFunctions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListLibraryFunctions(requestBody:ListLibraryFunctions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListLibraryFunctions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/ListLibraryFunctions", {
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
         resolve(data as ListLibraryFunctions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ListEventTypes
   Description: List all the event types that are supported by this system.
   OperationID: Get_ListEventTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListEventTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_ListEventTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListEventTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/ListEventTypes", {
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
         resolve(data as ListEventTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEventType
   Description: Get a specific Event Type and related functions.
   OperationID: Get_GetEventType
      @param eventType Desc: Event Type, required   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEventType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetEventType(eventType:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof eventType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "eventType=" + eventType
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEventType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/GetEventType" + params, {
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
         resolve(data as GetEventType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFunctions
   Description: Checks whether a list of functions are valid to use with Data Fabric.
   OperationID: ValidateFunctions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFunctions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFunctions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFunctions(requestBody:ValidateFunctions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFunctions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/ValidateFunctions", {
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
         resolve(data as ValidateFunctions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateFunctions
   Description: Add or remove functions from an Event Type Consumer or Producer.
   OperationID: UpdateFunctions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateFunctions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateFunctions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateFunctions(requestBody:UpdateFunctions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateFunctions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/UpdateFunctions", {
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
         resolve(data as UpdateFunctions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Produce
   Description: Produce an Integration Outbox Event.
<remarks>Access to this method is restricted and cannot be called directly, for example via the REST API.</remarks>
   OperationID: Produce
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Produce_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Produce_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Produce(requestBody:Produce_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Produce_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.DataFabricSvc/Produce", {
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
         resolve(data as Produce_output)
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
      @param eventType
   */  
export interface GetEventType_input{
      /**  Event Type, required  */  
   eventType:string,
}

export interface GetEventType_output{
   returnObj:Ice_Tablesets_DataFabricEventTypeTableset[],
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

export interface Ice_Tablesets_DataFabricEfxFunctionRow{
   LibraryID:string,
   FunctionID:string,
   Disabled:boolean,
   Invalid:boolean,
   Compatible:boolean,
   Description:string,
   Message:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DataFabricEfxFunctionTableset{
   DataFabricEfxFunction:Ice_Tablesets_DataFabricEfxFunctionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_DataFabricEventTypeFunctionRow{
   EventType:string,
   HandlerType:string,
   LibraryID:string,
   FunctionID:string,
   Mode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DataFabricEventTypeRow{
   EventType:string,
   Producer:boolean,
   Consumer:boolean,
   ConsumerFunctionsEnabled:boolean,
   ProducerFunctionsEnabled:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DataFabricEventTypeTableset{
   DataFabricEventType:Ice_Tablesets_DataFabricEventTypeRow[],
   DataFabricEventTypeFunction:Ice_Tablesets_DataFabricEventTypeFunctionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface ListEventTypes_output{
   returnObj:Ice_Tablesets_DataFabricEventTypeTableset[],
}

   /** Required : 
      @param libraryID
      @param startsWith
      @param sortBy
   */  
export interface ListLibraryFunctions_input{
      /**  Library ID  */  
   libraryID:string,
      /**  Description starts with  */  
   startsWith:string,
      /**  Sort by either description or function ID  */  
   sortBy:string,
}

export interface ListLibraryFunctions_output{
   returnObj:Ice_Tablesets_DataFabricEfxFunctionTableset[],
}

   /** Required : 
      @param eventType
      @param key
      @param data
      @param correlationId
   */  
export interface Produce_input{
      /**  Event Type  */  
   eventType:string,
      /**  Key  */  
   key:string,
      /**  Data  */  
   data:string,
      /**  Correlation ID  */  
   correlationId:string,
}

export interface Produce_output{
}

   /** Required : 
      @param ds
   */  
export interface UpdateFunctions_input{
   ds:Ice_Tablesets_DataFabricEventTypeTableset[],
}

export interface UpdateFunctions_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DataFabricEventTypeTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateFunctions_input{
   ds:Ice_Tablesets_DataFabricEfxFunctionTableset[],
}

export interface ValidateFunctions_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DataFabricEfxFunctionTableset,
   valid:boolean,
}
}

