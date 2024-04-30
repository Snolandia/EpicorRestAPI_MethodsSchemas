import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.MobileSettingsSvc
// Description: Mobile Settings Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/$metadata", {
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
   Summary: Invoke method ChangeCompanyAndPlant
   Description: Change the company and plant for the current user
   OperationID: ChangeCompanyAndPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCompanyAndPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCompanyAndPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCompanyAndPlant(requestBody:ChangeCompanyAndPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCompanyAndPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/ChangeCompanyAndPlant", {
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
         resolve(data as ChangeCompanyAndPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCompanyAndPlantForUser
   Description: Get list of Companies and Plants for the current user
   OperationID: GetCompanyAndPlantForUser
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanyAndPlantForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompanyAndPlantForUser(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCompanyAndPlantForUser_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/GetCompanyAndPlantForUser", {
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
         resolve(data as GetCompanyAndPlantForUser_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UserSettings
   Description: Return User and Employee information
   OperationID: UserSettings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UserSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UserSettings(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UserSettings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/UserSettings", {
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
         resolve(data as UserSettings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method validateUserForApplication
   Description: Uses the current session user to validate if it is allowed to access the  application
If allowed, then message is empty, if not allowed then
the message returns the reason for which the user is not allowed to access
   OperationID: validateUserForApplication
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/validateUserForApplication_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateUserForApplication_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_validateUserForApplication(requestBody:validateUserForApplication_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<validateUserForApplication_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/validateUserForApplication", {
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
         resolve(data as validateUserForApplication_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEpicorHelpUrl
   Description: Wrapper around the framework ClientFunctions service to retrieve the help url.
   OperationID: GetEpicorHelpUrl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetEpicorHelpUrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEpicorHelpUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEpicorHelpUrl(requestBody:GetEpicorHelpUrl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEpicorHelpUrl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/GetEpicorHelpUrl", {
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
         resolve(data as GetEpicorHelpUrl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetVersion
   Description: Returns the BO Version
   OperationID: GetVersion
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVersion(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetVersion_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/GetVersion", {
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
         resolve(data as GetVersion_output)
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
      @param company
      @param plantID
      @param applicationName
   */  
export interface ChangeCompanyAndPlant_input{
      /**  Company ID to which we want to change the users default  */  
   company:string,
      /**  Site ID to which we want to change the users default  */  
   plantID:string,
      /**  Application Name, Options: ERPExpense or ERPTime  */  
   applicationName:string,
}

export interface ChangeCompanyAndPlant_output{
}

export interface Erp_Tablesets_MobileSettingsLicenseRow{
   Company:string,
      /**  Describes whether the license is enable or not for the company  */  
   Enable:boolean,
      /**  License Name  */  
   LicenseName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileSettingsSessionRow{
   CompanyID:string,
   CompanyName:string,
   EmployeeID:string,
   UserID:string,
      /**  Indicates if the current user is restricted to entering time against employees where their username is set in the Employee record.  */  
   TimeRestrictEntry:boolean,
      /**  Indicates whether the user is allowed to create a Time transaction in Time Mobile application  for another employee for which they are an Approver.  */  
   TimeDisableCreate:boolean,
      /**  This value will be true if the Employee is allowed to enter Time  */  
   TimeEntryAllowed:boolean,
      /**  Indicates if the current user is restricted to entering expense against employees where their username is set in the Employee record.  */  
   ExpenseRestrictEntry:boolean,
      /**  Indicates whether the user is allowed to create a Expense transaction in Expense Mobile application  for another employee for which they are an Approver.  */  
   ExpenseDisableCreate:boolean,
      /**  This value will be true if the Employee is allowed to enter Expense.  */  
   ExpenseEntryAllowed:boolean,
   Plant:string,
   SalesRepCode:string,
      /**  Employee Name  */  
   EmployeeName:string,
      /**  Plant Name  */  
   PlantName:string,
      /**  User email address  */  
   EmailAddress:string,
      /**  Users name  */  
   UserName:string,
   LangNameID:string,
      /**  Language Name Description  */  
   LangNameDescription:string,
      /**  Culture flag  */  
   LangNameCulture:string,
   FormatCulture:string,
      /**  Returns the installed Sever version to which we are connecting.  */  
   ServerVersion:string,
      /**  The time zone offset in seconds between UTC and the time based on the time zone defined against the company  */  
   TimeZoneOffset:number,
   IsMultiTenant:boolean,
      /**   To validate if the user can enter Production/Service time.
This validation works together with the ProjectBilling license.  */  
   TimeAllowJobsEntry:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileSettingsTableset{
   MobileSettingsSession:Erp_Tablesets_MobileSettingsSessionRow[],
   MobileSettingsLicense:Erp_Tablesets_MobileSettingsLicenseRow[],
   MobileUserCompany:Erp_Tablesets_MobileUserCompanyRow[],
   MobileUserPlant:Erp_Tablesets_MobileUserPlantRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MobileUserCompanyRow{
      /**  Company ID  */  
   CompanyID:string,
      /**  Company Name  */  
   CompanyName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MobileUserPlantRow{
      /**  Company ID  */  
   CompanyID:string,
   Plant:string,
      /**  Plant Name  */  
   PlantName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface GetCompanyAndPlantForUser_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileSettingsTableset,
}
}

   /** Required : 
      @param label
      @param helpTopic
      @param username
      @param useremail
      @param aryTags
      @param zdSubDomain
      @param locale
   */  
export interface GetEpicorHelpUrl_input{
      /**  Corresponds to Label used in Zendesk for an article, and used to locate the URL of an article. Should be lowercase without spaces. In the case of Kinetic forms, use page title as label (lowercasing and trimming spaces)  */  
   label:string,
      /**  The fully qualified URL of a Zendesk article. Example- 'https://epicorerp.zendesk.com/hc/en-us/articles/360022072552-View-Schedule' If using label (preferred technique) send null for helpTopic.  */  
   helpTopic:string,
      /**  Consult with Epicor University writer on the generic user or users that may be appropriate. Until Epicor Idp is used, most apps will use a single user for the whole app.
            Example- 'Epicor TimeExpenseUser'  */  
   username:string,
      /**  Email for user. Until actual users are passed (afer Idp), email is just meeting a Zendesk requirement and will not be used (but must consistent for user from call to call).
            Example-'erptimeexpense@epicor.com'  */  
   useremail:string,
      /**  Tags are used in Zendesk to show or hide (segment) content. Consult with Epicor University writer on appropriate tags for user.
            Tags sent with call replace previous tag set. Example- ['erptime', 'erpexpense']  */  
   aryTags:string,
      /**  Consult with EU writer on the Zendesk subdomain to use  */  
   zdSubDomain:string,
      /**  Set to locale of user session. For example - en-us  */  
   locale:string,
}

export interface GetEpicorHelpUrl_output{
      /**  A URL with Zendesk SSO token and redirect url as querystring.  */  
   returnObj:string,
}

export interface GetVersion_output{
   returnObj:string,
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

export interface UserSettings_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MobileSettingsTableset,
}
}

   /** Required : 
      @param applicationName
   */  
export interface validateUserForApplication_input{
      /**  Application Name, Options: ERPExpense or ERPTime  */  
   applicationName:string,
}

export interface validateUserForApplication_output{
parameters : {
      /**  output parameters  */  
   message:string,
}
}

