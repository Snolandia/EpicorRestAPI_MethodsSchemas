import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.LIB.EcfToolsSvc
// Description: ATTENTION: This service is for internal use only.
It can be changed or even removed without any public announces.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/$metadata", {
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
   Summary: Invoke method GetAssemblyBytes
   OperationID: GetAssemblyBytes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAssemblyBytes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAssemblyBytes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAssemblyBytes(requestBody:GetAssemblyBytes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAssemblyBytes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/GetAssemblyBytes", {
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
         resolve(data as GetAssemblyBytes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailableServiceKinds
   Description: Method returns Service Kinds (BO, Lib, etc.) available per System Code
   OperationID: GetAvailableServiceKinds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableServiceKinds_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableServiceKinds(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailableServiceKinds_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/GetAvailableServiceKinds", {
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
         resolve(data as GetAvailableServiceKinds_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailableServices
   Description: Method returns an array of ServiceInfo items of specified kind available for the specified system code.
   OperationID: GetAvailableServices
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAvailableServices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableServices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableServices(requestBody:GetAvailableServices_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailableServices_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/GetAvailableServices", {
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
         resolve(data as GetAvailableServices_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetServiceApi
   Description: Method returns service API description (e.g. methods with their signatures)
   OperationID: GetServiceApi
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetServiceApi_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetServiceApi_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetServiceApi(requestBody:GetServiceApi_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetServiceApi_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/GetServiceApi", {
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
         resolve(data as GetServiceApi_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTablesetInfo
   Description: Method returns tableset description for the provided type reference.
If type reference describes not a tableset, then method throws an exception.
If tableset is unknown, then method returns null
If ignoreExtensions == false, then method loads information about extension tables
available for the current company (if any).
   OperationID: GetTablesetInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTablesetInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTablesetInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTablesetInfo(requestBody:GetTablesetInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTablesetInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/GetTablesetInfo", {
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
         resolve(data as GetTablesetInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTablesetInfoInCompany
   Description: Method returns tableset description for the provided type reference.
If type reference describes not a tableset, then method throws an exception.
If tableset is unknown, then method returns null
If inCompany parameter is specified, then method tries to provide information
about extension tables available in the company.
   OperationID: GetTablesetInfoInCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTablesetInfoInCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTablesetInfoInCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTablesetInfoInCompany(requestBody:GetTablesetInfoInCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTablesetInfoInCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/GetTablesetInfoInCompany", {
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
         resolve(data as GetTablesetInfoInCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDBModel
   Description: Method returns definition of the product DB model.
   OperationID: GetDBModel
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDBModel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDBModel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDBModel(requestBody:GetDBModel_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDBModel_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/GetDBModel", {
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
         resolve(data as GetDBModel_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDBEntity
   Description: Method returns entity definition of the product DB model.
   OperationID: GetDBEntity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDBEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDBEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDBEntity(requestBody:GetDBEntity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDBEntity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/GetDBEntity", {
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
         resolve(data as GetDBEntity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CanCallWorkato
   OperationID: CanCallWorkato
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanCallWorkato_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CanCallWorkato(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CanCallWorkato_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/CanCallWorkato", {
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
         resolve(data as CanCallWorkato_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWorkatoApiCollections
   OperationID: GetWorkatoApiCollections
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWorkatoApiCollections_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWorkatoApiCollections(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetWorkatoApiCollections_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/GetWorkatoApiCollections", {
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
         resolve(data as GetWorkatoApiCollections_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWorkatoEndpoints
   OperationID: GetWorkatoEndpoints
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetWorkatoEndpoints_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWorkatoEndpoints_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWorkatoEndpoints(requestBody:GetWorkatoEndpoints_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetWorkatoEndpoints_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/GetWorkatoEndpoints", {
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
         resolve(data as GetWorkatoEndpoints_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWorkatoEndpointSignature
   OperationID: GetWorkatoEndpointSignature
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetWorkatoEndpointSignature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWorkatoEndpointSignature_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWorkatoEndpointSignature(requestBody:GetWorkatoEndpointSignature_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetWorkatoEndpointSignature_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EcfToolsSvc/GetWorkatoEndpointSignature", {
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
         resolve(data as GetWorkatoEndpointSignature_output)
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
export interface CanCallWorkato_output{
   returnObj:boolean,
}

export interface Epicor_Customization_Metadata_DBEntityId{
   product:string,
   entityName:string,
}

export interface Epicor_Customization_Metadata_DBEntityInfo{
   id:Epicor_Customization_Metadata_DBEntityId[],
   typeName:string,
   rowTypeName:string,
   columns:Epicor_Customization_Metadata_IceColumnInfo[],
   keyColumns:number,
}

export interface Epicor_Customization_Metadata_DBModelInfo{
   product:string,
   assembly:string,
   entities:Epicor_Customization_Metadata_DBEntityId[],
}

export interface Epicor_Customization_Metadata_EpicorServiceApi{
   serviceId:Epicor_Typed_ServiceId[],
   methods:Epicor_Customization_Metadata_ServiceMethodSignature[],
   options:number,
}

export interface Epicor_Customization_Metadata_IceColumnInfo{
   name:string,
   typeName:string,
   kind:number,
}

export interface Epicor_Customization_Metadata_IceTableInfo{
   name:string,
   extension:boolean,
   tableTypeName:string,
   rowTypeName:string,
   columns:Epicor_Customization_Metadata_IceColumnInfo[],
   keyColumns:number,
}

export interface Epicor_Customization_Metadata_IceTablesetInfo{
   id:string,
   type:Epicor_Customization_Metadata_TypeRef[],
   tables:Epicor_Customization_Metadata_IceTableInfo[],
   extensionTables:Epicor_Customization_Metadata_IceTableInfo[],
   relations:Epicor_Customization_Metadata_TableRelation[],
   primaryTableIdx:number,
}

export interface Epicor_Customization_Metadata_MethodArg{
   name:string,
   type:Epicor_Customization_Metadata_TypeRef[],
   modifier:number,
}

export interface Epicor_Customization_Metadata_RelationColumns{
   parentColumn:string,
   childColumn:string,
}

export interface Epicor_Customization_Metadata_RestParameter{
   name:string,
   type:Epicor_Customization_Metadata_TypeRef[],
   location:string,
}

export interface Epicor_Customization_Metadata_RestSignature{
   input:Epicor_Customization_Metadata_RestParameter[],
   output:Epicor_Customization_Metadata_RestParameter[],
}

export interface Epicor_Customization_Metadata_ServiceMethodSignature{
   name:string,
   arguments:Epicor_Customization_Metadata_MethodArg[],
   resultType:Epicor_Customization_Metadata_TypeRef[],
   options:number,
}

export interface Epicor_Customization_Metadata_TableRelation{
   parentTable:string,
   childTable:string,
   columns:Epicor_Customization_Metadata_RelationColumns[],
}

export interface Epicor_Customization_Metadata_TypeRef{
   wellknownType:number,
   namespace:string,
   name:string,
   assembly:string,
   options:number,
   elementType:Epicor_Customization_Metadata_TypeRef[],
   genericArguments:Epicor_Customization_Metadata_TypeRef[],
}

export interface Epicor_Typed_ProductCode{
   value:string,
}

export interface Epicor_Typed_ServiceId{
   product:Epicor_Typed_ProductCode[],
   kind:Epicor_Typed_ServiceKind[],
   name:string,
}

export interface Epicor_Typed_ServiceKind{
   value:string,
}

   /** Required : 
      @param assemblyId
   */  
export interface GetAssemblyBytes_input{
   assemblyId:string,
}

export interface GetAssemblyBytes_output{
   returnObj:string,
}

export interface GetAvailableServiceKinds_output{
   returnObj:Ice_Lib_EcfTools_ProductServiceKinds[],
}

   /** Required : 
      @param systemCode
      @param serviceKind
   */  
export interface GetAvailableServices_input{
   systemCode:string,
   serviceKind:string,
}

export interface GetAvailableServices_output{
   returnObj:Ice_Lib_EcfTools_ServiceInfo[],
}

   /** Required : 
      @param id
   */  
export interface GetDBEntity_input{
   id:Epicor_Customization_Metadata_DBEntityId[],
}

export interface GetDBEntity_output{
   returnObj:Epicor_Customization_Metadata_DBEntityInfo[],
}

   /** Required : 
      @param systemCode
   */  
export interface GetDBModel_input{
   systemCode:string,
}

export interface GetDBModel_output{
   returnObj:Epicor_Customization_Metadata_DBModelInfo[],
}

   /** Required : 
      @param serviceId
   */  
export interface GetServiceApi_input{
   serviceId:Epicor_Typed_ServiceId[],
}

export interface GetServiceApi_output{
   returnObj:Epicor_Customization_Metadata_EpicorServiceApi[],
}

   /** Required : 
      @param typeRef
      @param inCompany
   */  
export interface GetTablesetInfoInCompany_input{
   typeRef:Epicor_Customization_Metadata_TypeRef[],
   inCompany:string,
}

export interface GetTablesetInfoInCompany_output{
   returnObj:Epicor_Customization_Metadata_IceTablesetInfo[],
}

   /** Required : 
      @param typeRef
      @param ignoreExtensions
   */  
export interface GetTablesetInfo_input{
   typeRef:Epicor_Customization_Metadata_TypeRef[],
   ignoreExtensions:boolean,
}

export interface GetTablesetInfo_output{
   returnObj:Epicor_Customization_Metadata_IceTablesetInfo[],
}

export interface GetWorkatoApiCollections_output{
   returnObj:Ice_Lib_EcfTools_WorkatoApiCollectionInfo[],
}

   /** Required : 
      @param endpointId
   */  
export interface GetWorkatoEndpointSignature_input{
   endpointId:Ice_Lib_EcfTools_WorkatoEndpointId[],
}

export interface GetWorkatoEndpointSignature_output{
   returnObj:Epicor_Customization_Metadata_RestSignature[],
}

   /** Required : 
      @param collectionPath
   */  
export interface GetWorkatoEndpoints_input{
   collectionPath:string,
}

export interface GetWorkatoEndpoints_output{
   returnObj:Ice_Lib_EcfTools_WorkatoEndpointInfo[],
}

export interface Ice_Lib_EcfTools_ProductServiceKinds{
   systemCode:string,
   serviceKinds:string,
}

export interface Ice_Lib_EcfTools_ServiceInfo{
   className:string,
   serviceUsage:number,
}

export interface Ice_Lib_EcfTools_WorkatoApiCollectionInfo{
   path:string,
   name:string,
   version:string,
}

export interface Ice_Lib_EcfTools_WorkatoEndpointId{
   collectionPath:string,
   endpointPath:string,
   httpMethod:string,
}

export interface Ice_Lib_EcfTools_WorkatoEndpointInfo{
   path:string,
   httpMethod:string,
   name:string,
   active:boolean,
}

