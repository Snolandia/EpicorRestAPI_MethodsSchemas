import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.FeatureFlagSvc
// Description: Service for managing feature flags.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FeatureFlagSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FeatureFlagSvc/$metadata", {
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
   Summary: Invoke method EnableFeature
   Description: Enable a feature.
   OperationID: EnableFeature
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableFeature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableFeature_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnableFeature(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FeatureFlagSvc/EnableFeature", {
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
   Summary: Invoke method DisableFeature
   Description: Disable a feature.
   OperationID: DisableFeature
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisableFeature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableFeature_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DisableFeature(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FeatureFlagSvc/DisableFeature", {
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
   Summary: Invoke method GetEnabledFeatures
   Description: Get the list of enabled features.
   OperationID: GetEnabledFeatures
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEnabledFeatures_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEnabledFeatures_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEnabledFeatures(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FeatureFlagSvc/GetEnabledFeatures", {
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
      @param featureID
      @param level
      @param target
   */  
export interface DisableFeature_input{
      /**  Feature flag identifier.  */  
   featureID:string,
      /**  Level at which the feature flag is to be disabled.  */  
   level:number,
      /**  The identifier for the level at which the flag applies. One of TenantID, Company, SecGroupCode, UserID. Ignored for level System.  */  
   target:string,
}

export interface DisableFeature_output{
}

   /** Required : 
      @param featureID
      @param level
      @param target
   */  
export interface EnableFeature_input{
      /**  Feature flag identifier.  */  
   featureID:string,
      /**  Level at which the feature flag is to be enabled.  */  
   level:number,
      /**  The identifier for the level at which the flag applies. One of TenantID, Company, SecGroupCode, UserID. Ignored for level System.  */  
   target:string,
}

export interface EnableFeature_output{
}

   /** Required : 
      @param userID
   */  
export interface GetEnabledFeatures_input{
      /**  The user identifier for which to retrieve the enabled feature flags or null for all users.  */  
   userID:string,
}

export interface GetEnabledFeatures_output{
   returnObj:Ice_Tablesets_FeatureFlagTableset[],
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

export interface Ice_Tablesets_EnabledFeatureRow{
      /**  FeatureID  */  
   FeatureID:string,
      /**  Level  */  
   Level:number,
      /**  Target  */  
   Target:string,
      /**  TenantID  */  
   TenantID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_FeatureFlagTableset{
   EnabledFeature:Ice_Tablesets_EnabledFeatureRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

