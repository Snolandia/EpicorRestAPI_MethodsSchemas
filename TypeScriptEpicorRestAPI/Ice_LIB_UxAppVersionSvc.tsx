import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.UxAppVersionSvc
// Description: This Lib is designed to manage versioning for metafx apps/layers.
It contains apis to create, list and restore version for apps/layers
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/$metadata", {
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
   Summary: Invoke method GetVersions
   Description: Provides all versions for a layer or App
   OperationID: Get_GetVersions
      @param request Desc: EpMetaFxRequest   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetVersions(request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/GetVersions" + params, {
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
   Summary: Invoke method CreateVersion
   Description: Create new version for layer or App
   OperationID: CreateVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateVersion(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/CreateVersion", {
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
   Summary: Invoke method GetUxAppVersions
   OperationID: GetUxAppVersions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUxAppVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUxAppVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUxAppVersions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/GetUxAppVersions", {
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
   Summary: Invoke method PublishVersion
   OperationID: PublishVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PublishVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PublishVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PublishVersion(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/PublishVersion", {
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
   Summary: Invoke method PublishBaseFile
   OperationID: PublishBaseFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PublishBaseFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PublishBaseFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PublishBaseFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/PublishBaseFile", {
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
   Summary: Invoke method BulkPublishBase
   OperationID: BulkPublishBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BulkPublishBase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BulkPublishBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BulkPublishBase(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/BulkPublishBase", {
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
   Summary: Invoke method GetBaseAppRow
   OperationID: GetBaseAppRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBaseAppRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBaseAppRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBaseAppRow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/GetBaseAppRow", {
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
   Summary: Invoke method BulkPublishLayers
   OperationID: BulkPublishLayers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BulkPublishLayers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BulkPublishLayers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BulkPublishLayers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/BulkPublishLayers", {
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
   Summary: Invoke method DeleteVersions
   OperationID: DeleteVersions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteVersions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteVersions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteVersions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.UxAppVersionSvc/DeleteVersions", {
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
      @param request
   */  
export interface BulkPublishBase_input{
   request:Ice_Lib_UxAppVersion_UxAppVersionRequest[],
}

export interface BulkPublishBase_output{
}

   /** Required : 
      @param uxVersionRequests
   */  
export interface BulkPublishLayers_input{
   uxVersionRequests:Ice_Lib_UxAppVersion_UxAppVersionRequest[],
}

export interface BulkPublishLayers_output{
}

   /** Required : 
      @param request
   */  
export interface CreateVersion_input{
   request:Ice_Lib_UxAppVersion_EpMetaFxRequest[],
}

export interface CreateVersion_output{
      /**  List of UxAppVersionResponse  */  
   returnObj:number,
}

   /** Required : 
      @param isBase
      @param appName
      @param layerName
      @param typeCode
   */  
export interface DeleteVersions_input{
   isBase:boolean,
   appName:string,
   layerName:string,
   typeCode:string,
}

export interface DeleteVersions_output{
}

   /** Required : 
      @param request
   */  
export interface GetBaseAppRow_input{
   request:Ice_Lib_UxAppVersion_UxAppVersionRequest[],
}

export interface GetBaseAppRow_output{
   returnObj:Ice_Lib_UxAppVersion_UxAppVersionResponse[],
}

   /** Required : 
      @param request
   */  
export interface GetUxAppVersions_input{
   request:Ice_Lib_UxAppVersion_UxAppVersionRequest[],
}

export interface GetUxAppVersions_output{
   returnObj:Ice_Lib_UxAppVersion_UxAppVersionResponse[],
}

   /** Required : 
      @param request
   */  
export interface GetVersions_input{
   request:Ice_Lib_UxAppVersion_EpMetaFxRequest[],
}

export interface GetVersions_output{
      /**  List of UxAppVersionResponse  */  
   returnObj:Ice_Lib_UxAppVersion_UxAppVersionResponse[],
}

export interface Ice_Lib_UxAppVersion_EpMetaFxRequest{
   id:string,
   properties:Ice_Lib_UxAppVersion_EpMetaFxRequestProperty[],
}

export interface Ice_Lib_UxAppVersion_EpMetaFxRequestProperty{
   layers:string,
   layerType:string,
   deviceType:string,
   mode:string,
   userName:string,
   pageName:string,
   company:string,
   countryGroupCode:string,
   debug:boolean,
   countryCode:string,
   includeWasm:boolean,
   applicationType:string,
   additionalContext:any,      //schema had no properties on an object.
   checkDuplicateIds:boolean,
   layerVersion:number,
   baseAppVersion:number,
   comment:string,
}

export interface Ice_Lib_UxAppVersion_UxAppVersionRequest{
   Company:string,
   Version:number,
   TypeCode:string,
   Key1:string,
   Key2:string,
   Key3:string,
   CGCCode:string,
   ProductID:string,
   Content:string,
   Comment:string,
   SystemFlag:boolean,
   IsPublish:boolean,
}

export interface Ice_Lib_UxAppVersion_UxAppVersionResponse{
   Company:string,
   ProductID:string,
   TypeCode:string,
   CGCCode:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Version:number,
   Content:string,
   Comment:string,
   PublishDate:string,
   CreatedBy:string,
   CreatedOn:string,
   SystemFlag:string,
   SysRevID:string,
   SysRowID:string,
}

   /** Required : 
      @param request
      @param prevVersion
   */  
export interface PublishBaseFile_input{
   request:Ice_Lib_UxAppVersion_UxAppVersionRequest[],
   prevVersion:number,
}

export interface PublishBaseFile_output{
}

   /** Required : 
      @param request
   */  
export interface PublishVersion_input{
   request:Ice_Lib_UxAppVersion_UxAppVersionRequest[],
}

export interface PublishVersion_output{
}

