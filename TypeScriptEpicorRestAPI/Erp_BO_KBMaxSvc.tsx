import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.KBMaxSvc
// Description: CPQ Library
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/$metadata", {
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
   Summary: Invoke method Login
   Description: Login to the CPQ Instance
   OperationID: Login
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<Login_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/Login", {
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
         resolve(data as Login_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetKBMaxAttachmentDocTypeList
   Description: Get the list of valid Attachment Document Types specific for CPQ.
List will contain Doc Types that are not specific to table, and Doc Types that are specific QuoteDtl, QuoteAsm, OrderDtl, JobHead, JobAsmbl.
   OperationID: GetKBMaxAttachmentDocTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKBMaxAttachmentDocTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetKBMaxAttachmentDocTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetKBMaxAttachmentDocTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/GetKBMaxAttachmentDocTypeList", {
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
         resolve(data as GetKBMaxAttachmentDocTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetConfigurator
   Description: Get the CPQ Configurator Product ID from a Kinetic Configurator
and validate it can be used.
   OperationID: GetConfigurator
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetConfigurator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConfigurator_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetConfigurator(requestBody:GetConfigurator_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetConfigurator_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/GetConfigurator", {
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
         resolve(data as GetConfigurator_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetConfiguredProduct
   Description: Validate entity table and get CPQ Configured Product.
   OperationID: GetConfiguredProduct
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetConfiguredProduct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConfiguredProduct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetConfiguredProduct(requestBody:GetConfiguredProduct_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetConfiguredProduct_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/GetConfiguredProduct", {
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
         resolve(data as GetConfiguredProduct_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCanSave
   Description: Checks if CPQ configuration has any validation errors and if so validates if it can be saved.
   OperationID: ValidateCanSave
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCanSave_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCanSave_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCanSave(requestBody:ValidateCanSave_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCanSave_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/ValidateCanSave", {
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
         resolve(data as ValidateCanSave_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCanSave
   Description: Checks if CPQ configuration has any validation errors and if so validates if it can be saved.
   OperationID: CheckCanSave
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCanSave_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCanSave_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCanSave(requestBody:CheckCanSave_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCanSave_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/CheckCanSave", {
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
         resolve(data as CheckCanSave_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddAttachments
   Description: Method to upload file to the storage defined by CPQ Document Type
   OperationID: AddAttachments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddAttachments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddAttachments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddAttachments(requestBody:AddAttachments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddAttachments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/AddAttachments", {
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
         resolve(data as AddAttachments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DocumentRulesEntitySchema
   Description: Returns schema for doc rules specific for CPQ
   OperationID: DocumentRulesEntitySchema
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DocumentRulesEntitySchema_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocumentRulesEntitySchema_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocumentRulesEntitySchema(requestBody:DocumentRulesEntitySchema_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DocumentRulesEntitySchema_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/DocumentRulesEntitySchema", {
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
         resolve(data as DocumentRulesEntitySchema_output)
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
      @param configID
      @param fileName
      @param data
      @param metadata
   */  
export interface AddAttachments_input{
   configID:number,
   fileName:string,
   data:string,
   metadata:any,      //schema had no properties on an object.
}

export interface AddAttachments_output{
}

   /** Required : 
      @param configuredProductJson
   */  
export interface CheckCanSave_input{
   configuredProductJson:string,
}

export interface CheckCanSave_output{
parameters : {
      /**  output parameters  */  
   canSave:boolean,
   canSaveError:string,
}
}

   /** Required : 
      @param kbConfigID
   */  
export interface DocumentRulesEntitySchema_input{
   kbConfigID:number,
}

export interface DocumentRulesEntitySchema_output{
   returnObj:Erp_Tablesets_KBMaxTableset[],
}

export interface Erp_Tablesets_KBMaxDocRulesColumnsRow{
      /**  Company indicator  */  
   Company:string,
      /**  Table Name  */  
   TableName:string,
      /**  Column Name  */  
   ColumnName:string,
      /**  Full column name.  */  
   ColumnSyntax:string,
      /**  Data Type  */  
   DataType:string,
      /**  Indicate if this field is a UD Field.  */  
   UDColumn:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_KBMaxDocRulesTablesRow{
      /**  Company indicator  */  
   Company:string,
      /**  Table name.  */  
   TableName:string,
      /**  Table description  */  
   Description:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_KBMaxRow{
      /**  Company indicator  */  
   Company:string,
      /**  CPQ Configurator ID  */  
   KBConfigID:number,
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  Attributes are allowed to be used in configuration  */  
   AllowAttributes:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_KBMaxTableset{
   KBMax:Erp_Tablesets_KBMaxRow[],
   KBMaxDocRulesTables:Erp_Tablesets_KBMaxDocRulesTablesRow[],
   KBMaxDocRulesColumns:Erp_Tablesets_KBMaxDocRulesColumnsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param configID
      @param validate
   */  
export interface GetConfigurator_input{
      /**  Configurator ID  */  
   configID:string,
      /**  Whether to perform validation  */  
   validate:boolean,
}

export interface GetConfigurator_output{
      /**  CPQ Configurator ID  */  
   returnObj:number,
}

   /** Required : 
      @param kbConfigProdID
      @param entityTable
   */  
export interface GetConfiguredProduct_input{
   kbConfigProdID:number,
   entityTable:string,
}

export interface GetConfiguredProduct_output{
      /**  CPQ Configured Product  */  
   returnObj:string,
}

export interface GetKBMaxAttachmentDocTypeList_output{
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

export interface Login_output{
parameters : {
      /**  output parameters  */  
   url:string,
   authCookie:string,
}
}

   /** Required : 
      @param configuredProductJson
   */  
export interface ValidateCanSave_input{
   configuredProductJson:string,
}

export interface ValidateCanSave_output{
}

