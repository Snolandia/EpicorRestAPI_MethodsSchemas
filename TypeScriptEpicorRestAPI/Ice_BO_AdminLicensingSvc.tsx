import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.AdminLicensingSvc
// Description: License maintenance business object for use by Admin Console
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata", {
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
   Summary: Invoke method GetLicense
   Description: Retrieving licensing information for the installation
   OperationID: GetLicense
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLicense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLicense(requestBody:GetLicense_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLicense_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/GetLicense", {
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
         resolve(data as GetLicense_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SysLicenseExists
   Description: Checks for existance of SysLicense record
   OperationID: SysLicenseExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SysLicenseExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SysLicenseExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SysLicenseExists(requestBody:SysLicenseExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SysLicenseExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/SysLicenseExists", {
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
         resolve(data as SysLicenseExists_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteLicense
   Description: This method deletes the License with the specified installation id.
   OperationID: DeleteLicense
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteLicense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteLicense(requestBody:DeleteLicense_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteLicense_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/DeleteLicense", {
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
         resolve(data as DeleteLicense_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateExistingLicense
   Description: Updates a license file if an update is available.
   OperationID: UpdateExistingLicense
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExistingLicense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExistingLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExistingLicense(requestBody:UpdateExistingLicense_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExistingLicense_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/UpdateExistingLicense", {
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
         resolve(data as UpdateExistingLicense_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EnableModule
   Description: This method enables a licensed feature/module.
   OperationID: EnableModule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/EnableModule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableModule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnableModule(requestBody:EnableModule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<EnableModule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/EnableModule", {
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
         resolve(data as EnableModule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EnableSingleModule
   Description: Enables a license module.
   OperationID: EnableSingleModule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/EnableSingleModule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableSingleModule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnableSingleModule(requestBody:EnableSingleModule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<EnableSingleModule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/EnableSingleModule", {
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
         resolve(data as EnableSingleModule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLicenseList
   Description: Returns a list of all licenses.
   OperationID: GetLicenseList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicenseList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLicenseList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLicenseList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/GetLicenseList", {
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
         resolve(data as GetLicenseList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUsableLicenseList
   Description: Returns a list of all usable licenses.
   OperationID: GetUsableLicenseList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUsableLicenseList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUsableLicenseList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetUsableLicenseList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/GetUsableLicenseList", {
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
         resolve(data as GetUsableLicenseList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportLicense
   Description: This method imports a new License.
   OperationID: ImportLicense
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportLicense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportLicense(requestBody:ImportLicense_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportLicense_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/ImportLicense", {
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
         resolve(data as ImportLicense_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckAndDownloadCloudLicenseUpdates
   Description: Checks the Global license server and download cloud license updates if exists.
   OperationID: CheckAndDownloadCloudLicenseUpdates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAndDownloadCloudLicenseUpdates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAndDownloadCloudLicenseUpdates(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckAndDownloadCloudLicenseUpdates_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/CheckAndDownloadCloudLicenseUpdates", {
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
         resolve(data as CheckAndDownloadCloudLicenseUpdates_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetTenantID
   Description: Sets the tenant ID by updated or creating the row in LicenseTenant
   OperationID: SetTenantID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetTenantID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTenantID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetTenantID(requestBody:SetTenantID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetTenantID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/SetTenantID", {
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
         resolve(data as SetTenantID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLicensesByTenantID
   Description: Gets the licenses by tenant ID.
   OperationID: GetLicensesByTenantID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLicensesByTenantID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicensesByTenantID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLicensesByTenantID(requestBody:GetLicensesByTenantID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLicensesByTenantID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/GetLicensesByTenantID", {
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
         resolve(data as GetLicensesByTenantID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSysLicenseList
   OperationID: GetSysLicenseList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSysLicenseList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSysLicenseList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSysLicenseList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/GetSysLicenseList", {
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
         resolve(data as GetSysLicenseList_output)
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
export interface CheckAndDownloadCloudLicenseUpdates_output{
}

   /** Required : 
      @param installationId
   */  
export interface DeleteLicense_input{
      /**  Installation id of license to be deleted  */  
   installationId:string,
}

export interface DeleteLicense_output{
}

   /** Required : 
      @param ds
   */  
export interface EnableModule_input{
   ds:Ice_Tablesets_AdminLicensingTableset[],
}

export interface EnableModule_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_AdminLicensingTableset,
}
}

   /** Required : 
      @param installationId
      @param moduleId
   */  
export interface EnableSingleModule_input{
      /**  The installation identifier.  */  
   installationId:string,
      /**  The module identifier.  */  
   moduleId:string,
}

export interface EnableSingleModule_output{
}

export interface GetLicenseList_output{
   returnObj:Ice_Tablesets_AdminLicensingTableset[],
}

   /** Required : 
      @param installationId
   */  
export interface GetLicense_input{
   installationId:string,
}

export interface GetLicense_output{
   returnObj:Ice_Tablesets_AdminLicensingTableset[],
}

   /** Required : 
      @param tenantID
   */  
export interface GetLicensesByTenantID_input{
      /**  The tenant ID.  */  
   tenantID:string,
}

export interface GetLicensesByTenantID_output{
   returnObj:Ice_Tablesets_AdminSerialNumberListTableset[],
}

export interface GetSysLicenseList_output{
   returnObj:Ice_Tablesets_SysLicenseTableset[],
}

export interface GetUsableLicenseList_output{
   returnObj:Ice_Tablesets_AdminSerialNumberListTableset[],
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

export interface Ice_Tablesets_AdminCSFLicenseRow{
   Enabled:boolean,
   Licensed:boolean,
   CGCCode:string,
   CGCName:string,
   CountryGroup:boolean,
   CGID:string,
      /**  Uniqueidentifier provided by the license file.  */  
   InstallationID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AdminLicensingTableset{
   AdminSerialNumber:Ice_Tablesets_AdminSerialNumberRow[],
   AdminCSFLicense:Ice_Tablesets_AdminCSFLicenseRow[],
   AdminModuleLicense:Ice_Tablesets_AdminModuleLicenseRow[],
   AdminUserLicense:Ice_Tablesets_AdminUserLicenseRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_AdminModuleLicenseRow{
   Enabled:boolean,
   Licensed:boolean,
   ModuleCode:string,
   ModuleName:string,
   Automatic:boolean,
      /**  Uniqueidentifier provided by the license file.  */  
   InstallationID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AdminSerialNumberListRow{
   MaxUsers:number,
   EvalExpires:string,
   MaxAdditionalDCUsers:number,
   DBLevel:number,
   DBPatchLevel:string,
      /**  Disconnected CRM Salesperson User Limit  */  
   MaxAdditionalDCRMUsers:number,
      /**  Disconnected CRM Sales Engineer User Limit  */  
   MaxAdditionalDCRMSEUsers:number,
   MaxWebServices:number,
      /**  An Isolated Company (=True) license indicates that this company is a Single Company in a shared (Hosted)database and should not be able to affect changes or share any data or administrative functions with other companies in the system.  */  
   Multitenant:boolean,
      /**  A uniqueidentifier provided by the license file.  */  
   Version:string,
   Edition:string,
   AssignedCompanies:string,
   Product:string,
   MaxAdditionalSCUsers:number,
   MaxAdditionalCCUsers:number,
   MaxAdditionalCRMUsers:number,
   MaxAdditionalMFWUsers:number,
   MaxAdditionalTEUsers:number,
      /**  Holds the tenant identity all companies using this license will operate under.  */  
   TenantID:string,
   InstallationID:string,
   UpdateAvailable:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AdminSerialNumberListTableset{
   AdminSerialNumberList:Ice_Tablesets_AdminSerialNumberListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_AdminSerialNumberRow{
   MaxUsers:number,
   EvalExpires:string,
   MaxAdditionalDCUsers:number,
   DBLevel:number,
   DBPatchLevel:string,
      /**  Disconnected CRM Salesperson User Limit  */  
   MaxAdditionalDCRMUsers:number,
      /**  Disconnected CRM Sales Engineer User Limit  */  
   MaxAdditionalDCRMSEUsers:number,
   MaxWebServices:number,
      /**  An Isolated Company (=True) license indicates that this company is a Single Company in a shared (Hosted)database and should not be able to affect changes or share any data or administrative functions with other companies in the system.  */  
   Multitenant:boolean,
   Version:string,
   Edition:string,
   AssignedCompanies:string,
   Product:string,
   MaxAdditionalSCUsers:number,
   MaxAdditionalCCUsers:number,
   MaxAdditionalCRMUsers:number,
   MaxAdditionalMFWUsers:number,
   MaxAdditionalTEUsers:number,
      /**  Uniqueidentifier provided by the license file.  */  
   InstallationID:string,
      /**  Holds the tenant identity all companies using this license will operate under.  */  
   TenantID:string,
   UpdateAvailable:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AdminUserLicenseRow{
   ActiveUsers:number,
   AvailableUsers:number,
   MaxUsers:number,
   UserLicenseCode:string,
   UserLicenseName:string,
      /**  Uniqueidentifier provided by the license file.  */  
   InstallationID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysLicenseRow{
   InstallationID:string,
   Name:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysLicenseTableset{
   SysLicense:Ice_Tablesets_SysLicenseRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param fileName
      @param licenseInfo
   */  
export interface ImportLicense_input{
      /**  The name of the license file to import  */  
   fileName:string,
      /**  Serial number and codes of license to be imported.  */  
   licenseInfo:string,
}

export interface ImportLicense_output{
}

   /** Required : 
      @param installationID
      @param tenantID
   */  
export interface SetTenantID_input{
      /**  The installation ID.  */  
   installationID:string,
      /**  The tenant ID.  */  
   tenantID:string,
}

export interface SetTenantID_output{
}

   /** Required : 
      @param name
   */  
export interface SysLicenseExists_input{
      /**  The Name of the SysLicense to check  */  
   name:string,
}

export interface SysLicenseExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param installationId
   */  
export interface UpdateExistingLicense_input{
      /**  Installation id of license to be updated.  */  
   installationId:string,
}

export interface UpdateExistingLicense_output{
}

