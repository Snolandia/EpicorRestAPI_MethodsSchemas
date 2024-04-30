import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.LIB.TokenServiceSvc
// Description: Generates tokens for token authentication
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/$metadata", {
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
   Summary: Invoke method GetAccessToken
   Description: Receive Access Token for currently logged in user and default client
   OperationID: GetAccessToken
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAccessToken_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAccessToken_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAccessToken(requestBody:GetAccessToken_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAccessToken_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/GetAccessToken", {
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
         resolve(data as GetAccessToken_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsTokenAuthenticationEnabled
   Description: Checks if Token Authentication is enabled in web.config
   OperationID: IsTokenAuthenticationEnabled
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsTokenAuthenticationEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsTokenAuthenticationEnabled(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsTokenAuthenticationEnabled_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/IsTokenAuthenticationEnabled", {
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
         resolve(data as IsTokenAuthenticationEnabled_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsTokenValid
   Description: Checks if given token is valid
   OperationID: IsTokenValid
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsTokenValid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsTokenValid_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsTokenValid(requestBody:IsTokenValid_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsTokenValid_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/IsTokenValid", {
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
         resolve(data as IsTokenValid_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AdminGetTokenConfig
   Description: Returns current settings for token authentication, available for security manager
   OperationID: AdminGetTokenConfig
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AdminGetTokenConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AdminGetTokenConfig(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AdminGetTokenConfig_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/AdminGetTokenConfig", {
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
         resolve(data as AdminGetTokenConfig_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AdminSetTokenConfig
   Description: Configure token resource
   OperationID: AdminSetTokenConfig
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AdminSetTokenConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AdminSetTokenConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AdminSetTokenConfig(requestBody:AdminSetTokenConfig_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AdminSetTokenConfig_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/AdminSetTokenConfig", {
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
         resolve(data as AdminSetTokenConfig_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AdminSetIdentityProvider
   Description: Set Identity provider connection
   OperationID: AdminSetIdentityProvider
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AdminSetIdentityProvider_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AdminSetIdentityProvider_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AdminSetIdentityProvider(requestBody:AdminSetIdentityProvider_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AdminSetIdentityProvider_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/AdminSetIdentityProvider", {
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
         resolve(data as AdminSetIdentityProvider_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AdminSetScimProvider
   Description: Setup Scim endpoint for Identity provider
   OperationID: AdminSetScimProvider
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AdminSetScimProvider_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AdminSetScimProvider_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AdminSetScimProvider(requestBody:AdminSetScimProvider_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AdminSetScimProvider_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/AdminSetScimProvider", {
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
         resolve(data as AdminSetScimProvider_output)
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
export interface AdminGetTokenConfig_output{
parameters : {
      /**  output parameters  */  
   tokenEnabled:boolean,
   signKey:string,
   lifeTime:number,
   refreshTokenEnabled:boolean,
   refreshTokenLifeTime:number,
}
}

   /** Required : 
      @param enable
      @param endpoint
      @param scope
      @param webClientID
      @param nativeClientID
   */  
export interface AdminSetIdentityProvider_input{
      /**  Enable or disable usage of identity provider in current App Server installation  */  
   enable:boolean,
      /**  URL where Identity provider is installed  */  
   endpoint:string,
      /**  Scope used in tokens  */  
   scope:string,
      /**  Client ID for the Web applications  */  
   webClientID:string,
      /**  Client ID for the native applications  */  
   nativeClientID:string,
}

export interface AdminSetIdentityProvider_output{
}

   /** Required : 
      @param enable
      @param clientId
      @param clientSecret
      @param scope
   */  
export interface AdminSetScimProvider_input{
      /**  Enable or disable authomatic user export  */  
   enable:boolean,
      /**  Client ID used for SCIM export  */  
   clientId:string,
      /**  Client secret used for SCIM export  */  
   clientSecret:string,
      /**  Scope used for SCIM export  */  
   scope:string,
}

export interface AdminSetScimProvider_output{
}

   /** Required : 
      @param tokenEnabled
      @param signKey
      @param lifeTime
      @param refreshTokenEnabled
      @param refreshTokenLifeTime
   */  
export interface AdminSetTokenConfig_input{
      /**  Token authentication is enabled  */  
   tokenEnabled:boolean,
      /**  Token signature key  */  
   signKey:string,
      /**  token lifetime in seconds  */  
   lifeTime:number,
      /**  Refresh token. Not implemented  */  
   refreshTokenEnabled:boolean,
      /**  Refresh token life time. Not implemented  */  
   refreshTokenLifeTime:number,
}

export interface AdminSetTokenConfig_output{
}

   /** Required : 
      @param clientId
      @param clientSecret
      @param scope
   */  
export interface GetAccessToken_input{
   clientId:string,
   clientSecret:string,
   scope:string,
}

export interface GetAccessToken_output{
   returnObj:Ice_Tablesets_TokenServiceTableset[],
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

export interface Ice_Tablesets_TokenServiceRow{
      /**  Aceess Token to use in Authentication  */  
   AccessToken:string,
      /**  Seconds to token expiration  */  
   ExpiresIn:number,
      /**  Refresh token to get new access token when current is expired  */  
   RefreshToken:string,
      /**  Type of token - now is always Bearer  */  
   TokenType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_TokenServiceTableset{
   TokenService:Ice_Tablesets_TokenServiceRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface IsTokenAuthenticationEnabled_output{
      /**  true if token authentication is enabled  */  
   returnObj:boolean,
}

   /** Required : 
      @param token
      @param userId
   */  
export interface IsTokenValid_input{
      /**  serialized token  */  
   token:string,
      /**  if specified, checks that token is valid and was issued for this user. If empty - just checks that token is valid  */  
   userId:string,
}

export interface IsTokenValid_output{
      /**  true if token is valid for current user  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   validTillUtc:string,
}
}

