import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.IntegrationPortalSvc
// Description: Integration Portal Service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/$metadata", {
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
   Summary: Invoke method GetStatus
   Description: Get Status of the Integration Portal Environment.
   OperationID: Get_GetStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetStatus(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/GetStatus", {
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

   /**  
   Summary: Invoke method GetContext
   Description: Get the Current User Context for the Portal.
   OperationID: Get_GetContext
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContext_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetContext(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/GetContext", {
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

   /**  
   Summary: Invoke method Register
   Description: Register Kinetic with the Integration Portal.
   OperationID: Register
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Register_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Register_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Register(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/Register", {
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
   Summary: Invoke method Reconnect
   Description: Reconnnect Kinetic with the Integration Portal.
   OperationID: Reconnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Reconnect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Reconnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Reconnect(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/Reconnect", {
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
   Summary: Invoke method Unregister
   Description: Unregister Kinetic from Integration Portal.
   OperationID: Unregister
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Unregister_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Unregister_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Unregister(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/Unregister", {
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
   Summary: Invoke method Login
   Description: Login to the Portal, if registered.
   OperationID: Login
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Login_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Login(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/Login", {
          method: 'post',
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

   /**  
   Summary: Invoke method ListAutomationStudioAPICollections
   Description: List Automation Studio API Collections.
   OperationID: Get_ListAutomationStudioAPICollections
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListAutomationStudioAPICollections_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_ListAutomationStudioAPICollections(pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/ListAutomationStudioAPICollections" + params, {
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

   /**  
   Summary: Invoke method ListAutomationStudioAPIEndpoints
   Description: List Automation Studio API Endpoints.
   OperationID: Get_ListAutomationStudioAPIEndpoints
      @param collectionPath Desc: API Collection Path   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListAutomationStudioAPIEndpoints_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_ListAutomationStudioAPIEndpoints(collectionPath:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof collectionPath!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "collectionPath=" + collectionPath
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/ListAutomationStudioAPIEndpoints" + params, {
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

   /**  
   Summary: Invoke method IsAutomationStudioAPIEndpointValid
   Description: Verifies that an Automation Studio API Endpoint is Valid.
   OperationID: Get_IsAutomationStudioAPIEndpointValid
      @param collectionPath Desc: Collection Path   Required: True   Allow empty value : True
      @param endpointPath Desc: Endpoint Path   Required: True   Allow empty value : True
      @param method Desc: HTTP Method, i.e. GET   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAutomationStudioAPIEndpointValid_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_IsAutomationStudioAPIEndpointValid(collectionPath:string, endpointPath:string, method:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof collectionPath!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "collectionPath=" + collectionPath
   }
   if(typeof endpointPath!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "endpointPath=" + endpointPath
   }
   if(typeof method!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "method=" + method
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.IntegrationPortalSvc/IsAutomationStudioAPIEndpointValid" + params, {
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
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface GetContext_output{
      /**  Context, serialized as JSON.  */  
   returnObj:string,
}

export interface GetStatus_output{
      /**  Whether Kinetic is registered with the Integration Portal  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   registeredModules:any[],
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

export interface Ice_Tablesets_AutomationStudioAPICollectionRow{
   CollectionID:number,
   Name:string,
   Version:string,
   URL:string,
   CollectionPath:string,
   APISpecURL:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AutomationStudioAPICollectionTableset{
   AutomationStudioAPICollection:Ice_Tablesets_AutomationStudioAPICollectionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_AutomationStudioAPIEndpointRow{
   EndpointID:number,
   CollectionID:number,
   FlowID:number,
   Name:string,
   Method:string,
   EndpointPath:string,
   URL:string,
   Active:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AutomationStudioAPIEndpointTableset{
   AutomationStudioAPIEndpoint:Ice_Tablesets_AutomationStudioAPIEndpointRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param collectionPath
      @param endpointPath
      @param method
   */  
export interface IsAutomationStudioAPIEndpointValid_input{
      /**  Collection Path  */  
   collectionPath:string,
      /**  Endpoint Path  */  
   endpointPath:string,
      /**  HTTP Method, i.e. GET  */  
   method:string,
}

export interface IsAutomationStudioAPIEndpointValid_output{
parameters : {
      /**  output parameters  */  
   collectionValid:boolean,
   endpointValid:boolean,
}
}

   /** Required : 
      @param pageSize
      @param absolutePage
   */  
export interface ListAutomationStudioAPICollections_input{
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface ListAutomationStudioAPICollections_output{
   returnObj:Ice_Tablesets_AutomationStudioAPICollectionTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param collectionPath
      @param pageSize
      @param absolutePage
   */  
export interface ListAutomationStudioAPIEndpoints_input{
      /**  API Collection Path  */  
   collectionPath:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface ListAutomationStudioAPIEndpoints_output{
   returnObj:Ice_Tablesets_AutomationStudioAPIEndpointTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Login_output{
parameters : {
      /**  output parameters  */  
   token:string,
   siteId:string,
   environmentId:string,
}
}

   /** Required : 
      @param functionUrl
      @param kineticUrl
      @param instanceId
      @param token
   */  
export interface Reconnect_input{
      /**  Portal Function URL  */  
   functionUrl:string,
      /**  Kinetic App Server URL  */  
   kineticUrl:string,
      /**  Existing Instance ID  */  
   instanceId:string,
      /**  IdP Token supplied from Portal App  */  
   token:string,
}

export interface Reconnect_output{
}

   /** Required : 
      @param functionUrl
      @param kineticUrl
      @param siteId
      @param environmentId
      @param name
      @param token
   */  
export interface Register_input{
      /**  Portal Function URL  */  
   functionUrl:string,
      /**  Kinetic App Server URL  */  
   kineticUrl:string,
      /**  Site ID  */  
   siteId:string,
      /**  Environment ID  */  
   environmentId:string,
      /**  Name of Instance  */  
   name:string,
      /**  IdP Token supplied from Portal App  */  
   token:string,
}

export interface Register_output{
   returnObj:string,
}

   /** Required : 
      @param token
   */  
export interface Unregister_input{
      /**  IdP or Portal Token supplied from Portal App  */  
   token:string,
}

export interface Unregister_output{
}

