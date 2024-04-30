import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.KineticErpSvc
// Description: Represents the Kinetic Erp Service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/$metadata", {
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
   Summary: Invoke method GetTokenList
   Description: Returns a comma separated list of valid tokens for the given data type.
   OperationID: GetTokenList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTokenList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTokenList(requestBody:GetTokenList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTokenList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetTokenList", {
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
         resolve(data as GetTokenList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTokenValue
   Description: Returns a token list of vaules based on a type that is passed in.
   OperationID: GetTokenValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTokenValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTokenValue(requestBody:GetTokenValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTokenValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetTokenValue", {
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
         resolve(data as GetTokenValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SerializePrinterAndPageSettings
   Description: Serialized the printer and page settings using the ERP library.
   OperationID: SerializePrinterAndPageSettings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SerializePrinterAndPageSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SerializePrinterAndPageSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SerializePrinterAndPageSettings(requestBody:SerializePrinterAndPageSettings_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SerializePrinterAndPageSettings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/SerializePrinterAndPageSettings", {
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
         resolve(data as SerializePrinterAndPageSettings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeserializePrinterAndPageSettings
   Description: Deserialize the printer and page settings using the ERP library.
   OperationID: DeserializePrinterAndPageSettings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeserializePrinterAndPageSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeserializePrinterAndPageSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeserializePrinterAndPageSettings(requestBody:DeserializePrinterAndPageSettings_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeserializePrinterAndPageSettings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/DeserializePrinterAndPageSettings", {
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
         resolve(data as DeserializePrinterAndPageSettings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUserSessionAndVersion
   Description: Get the current user, session and version info.
   OperationID: GetUserSessionAndVersion
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserSessionAndVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUserSessionAndVersion(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetUserSessionAndVersion_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetUserSessionAndVersion", {
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
         resolve(data as GetUserSessionAndVersion_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetHomepageCompany
   Description: Get the company info for KHP.
   OperationID: GetHomepageCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetHomepageCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHomepageCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHomepageCompany(requestBody:GetHomepageCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetHomepageCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetHomepageCompany", {
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
         resolve(data as GetHomepageCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFeaturesAndLicenses
   Description: Gets the object that provides the collection of Licensed Modules and Feature Flags.
   OperationID: GetFeaturesAndLicenses
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFeaturesAndLicenses_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFeaturesAndLicenses(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFeaturesAndLicenses_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetFeaturesAndLicenses", {
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
         resolve(data as GetFeaturesAndLicenses_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDatasetTables
   Description: Gets the collection of <cref>ErpDataset</cref> when given a collection of system codes and dataset ids.
   OperationID: GetDatasetTables
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDatasetTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDatasetTables(requestBody:GetDatasetTables_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDatasetTables_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetDatasetTables", {
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
         resolve(data as GetDatasetTables_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetConfirmDialogUserOptions
   Description: Retrieves the personalization layer for the current user from Ice.XXXDef and extracts the ConfirmOptions
form options.
   OperationID: GetConfirmDialogUserOptions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetConfirmDialogUserOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConfirmDialogUserOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetConfirmDialogUserOptions(requestBody:GetConfirmDialogUserOptions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetConfirmDialogUserOptions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetConfirmDialogUserOptions", {
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
         resolve(data as GetConfirmDialogUserOptions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateConfirmDialogOptions
   Description: Updates the confirm dialog options into the XXXDef Personalization row.
   OperationID: UpdateConfirmDialogOptions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateConfirmDialogOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateConfirmDialogOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateConfirmDialogOptions(requestBody:UpdateConfirmDialogOptions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateConfirmDialogOptions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/UpdateConfirmDialogOptions", {
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
         resolve(data as UpdateConfirmDialogOptions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSearchOptions
   Description: Gets the <cref>ErpSearchOptions</cref> object that describes the various search options.
   OperationID: GetSearchOptions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSearchOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSearchOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSearchOptions(requestBody:GetSearchOptions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSearchOptions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetSearchOptions", {
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
         resolve(data as GetSearchOptions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExecuteBaq
   Description: This method run an existing query with differing params and returns a collection of untyped datasets.
   OperationID: ExecuteBaq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExecuteBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExecuteBaq(requestBody:ExecuteBaq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExecuteBaq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/ExecuteBaq", {
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
         resolve(data as ExecuteBaq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateBaq
   Description: Friendly wrapper over the Ice.BO.DynamicQuerySvc to provide queryResultDataset schema validation logic.
Call Update method of an updatable query and return result dataset
   OperationID: UpdateBaq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateBaq(requestBody:UpdateBaq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateBaq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/UpdateBaq", {
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
         resolve(data as UpdateBaq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateBaqCustomAction
   Description: Friendly wrapper over the Ice.BO.DynamicQuerySvc to provide queryResultDataset schema validation logic.
This method does nothing per se, but is useful if there are BPM directives
attached to the query. Directives can examine actionId value and perform some actions.
   OperationID: UpdateBaqCustomAction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateBaqCustomAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBaqCustomAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateBaqCustomAction(requestBody:UpdateBaqCustomAction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateBaqCustomAction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/UpdateBaqCustomAction", {
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
         resolve(data as UpdateBaqCustomAction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateBaqFieldValidate
   Description: Friendly wrapper over the Ice.BO.DynamicQuerySvc to provide queryResultDataset schema validation logic.
Calls FieldUpdate method of an updatable query and return result set.
   OperationID: UpdateBaqFieldValidate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateBaqFieldValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBaqFieldValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateBaqFieldValidate(requestBody:UpdateBaqFieldValidate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateBaqFieldValidate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/UpdateBaqFieldValidate", {
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
         resolve(data as UpdateBaqFieldValidate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateBaqFieldUpdate
   Description: Friendly wrapper over the Ice.BO.DynamicQuerySvc to provide queryResultDataset schema validation logic.
Calls FieldUpdate method of an updatable query and return result set.
   OperationID: UpdateBaqFieldUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateBaqFieldUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBaqFieldUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateBaqFieldUpdate(requestBody:UpdateBaqFieldUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateBaqFieldUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/UpdateBaqFieldUpdate", {
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
         resolve(data as UpdateBaqFieldUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUserSettingsForView
   Description: Gets the <cref>ErpUserSettingsForView</cref> object that has user settings for a view.
   OperationID: GetUserSettingsForView
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetUserSettingsForView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserSettingsForView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUserSettingsForView(requestBody:GetUserSettingsForView_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetUserSettingsForView_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetUserSettingsForView", {
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
         resolve(data as GetUserSettingsForView_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveGridLayout
   Description: Save a grid layout.
   OperationID: SaveGridLayout
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveGridLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveGridLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveGridLayout(requestBody:SaveGridLayout_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveGridLayout_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/SaveGridLayout", {
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
         resolve(data as SaveGridLayout_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteGridLayout
   Description: Deletes a grid layout for a user.
   OperationID: DeleteGridLayout
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteGridLayout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteGridLayout_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteGridLayout(requestBody:DeleteGridLayout_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteGridLayout_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/DeleteGridLayout", {
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
         resolve(data as DeleteGridLayout_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInstallationSettings
   Description: Gets the installation level Kinetic settings.
   OperationID: GetInstallationSettings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstallationSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInstallationSettings(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInstallationSettings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetInstallationSettings", {
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
         resolve(data as GetInstallationSettings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateInstallationSettings
   Description: Updates the installation level Kinetic settings.
   OperationID: UpdateInstallationSettings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateInstallationSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateInstallationSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateInstallationSettings(requestBody:UpdateInstallationSettings_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateInstallationSettings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/UpdateInstallationSettings", {
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
         resolve(data as UpdateInstallationSettings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLaunchModes
   Description: Returns launch modes json
   OperationID: GetLaunchModes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLaunchModes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLaunchModes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLaunchModes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetLaunchModes", {
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
         resolve(data as GetLaunchModes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SendEmail
   Description: Use the from email address and mail services from the current company company mail settings to send email.
   OperationID: SendEmail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SendEmail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendEmail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SendEmail(requestBody:SendEmail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SendEmail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/SendEmail", {
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
         resolve(data as SendEmail_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SendEmailWithClientAttachments
   Description: Use the from email address and mail services from the current company mail settings to send email from smart client.
   OperationID: SendEmailWithClientAttachments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SendEmailWithClientAttachments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendEmailWithClientAttachments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SendEmailWithClientAttachments(requestBody:SendEmailWithClientAttachments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SendEmailWithClientAttachments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/SendEmailWithClientAttachments", {
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
         resolve(data as SendEmailWithClientAttachments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLikeFieldForAdapter
   Description: Gets the related likeField given an adapter name.
   OperationID: GetLikeFieldForAdapter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLikeFieldForAdapter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLikeFieldForAdapter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLikeFieldForAdapter(requestBody:GetLikeFieldForAdapter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLikeFieldForAdapter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetLikeFieldForAdapter", {
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
         resolve(data as GetLikeFieldForAdapter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAdapterList
   Description: Gets the adapter name list.
   OperationID: GetAdapterList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAdapterList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAdapterList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAdapterList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetAdapterList", {
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
         resolve(data as GetAdapterList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGrowMetrics
   Description: Gets grow's metrics.
   OperationID: GetGrowMetrics
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGrowMetrics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGrowMetrics(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGrowMetrics_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetGrowMetrics", {
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
         resolve(data as GetGrowMetrics_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEmbedGrowMetricUrl
   Description: Gets grow's metric url.
   OperationID: GetEmbedGrowMetricUrl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetEmbedGrowMetricUrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmbedGrowMetricUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEmbedGrowMetricUrl(requestBody:GetEmbedGrowMetricUrl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEmbedGrowMetricUrl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/GetEmbedGrowMetricUrl", {
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
         resolve(data as GetEmbedGrowMetricUrl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DocStarTestConnection
   Description: Test connection to DocStar system.
   OperationID: DocStarTestConnection
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DocStarTestConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarTestConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarTestConnection(requestBody:DocStarTestConnection_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DocStarTestConnection_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/DocStarTestConnection", {
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
         resolve(data as DocStarTestConnection_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DocStarCreateBrowserUrl
   Description: Builds a URL in DocStar which will be used to open the attachment within DocStar.
   OperationID: DocStarCreateBrowserUrl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DocStarCreateBrowserUrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateBrowserUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarCreateBrowserUrl(requestBody:DocStarCreateBrowserUrl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DocStarCreateBrowserUrl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.KineticErpSvc/DocStarCreateBrowserUrl", {
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
         resolve(data as DocStarCreateBrowserUrl_output)
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
      @param formKey
      @param gridId
   */  
export interface DeleteGridLayout_input{
      /**  The unique view key. Example: App.AbcCodeEntry.AbcCodeForm  */  
   formKey:string,
      /**  The unique grid id from the view.  */  
   gridId:string,
}

export interface DeleteGridLayout_output{
}

   /** Required : 
      @param serializedPrinterSettings
      @param serializedPageSettings
   */  
export interface DeserializePrinterAndPageSettings_input{
      /**  Serialized printer settings  */  
   serializedPrinterSettings:string,
      /**  Serialized page settings  */  
   serializedPageSettings:string,
}

export interface DeserializePrinterAndPageSettings_output{
   returnObj:Ice_BO_KineticErp_ErpPrinterProperties[],
}

   /** Required : 
      @param docTypeID
      @param documentId
      @param userName
      @param userPwd
      @param domain
      @param authType
      @param saveLogin
   */  
export interface DocStarCreateBrowserUrl_input{
      /**  Document type for the attachment  */  
   docTypeID:string,
      /**  Document identifier  */  
   documentId:string,
      /**  User Identifier  */  
   userName:string,
      /**  Encrypted user password  */  
   userPwd:string,
      /**  Domain for Windows authentication  */  
   domain:string,
      /**  Authentication type  */  
   authType:string,
      /**  If true saves the user account information  */  
   saveLogin:boolean,
}

export interface DocStarCreateBrowserUrl_output{
      /**  URL for the attachment document within DocStar  */  
   returnObj:string,
}

   /** Required : 
      @param docTypeID
      @param userName
      @param userPwd
      @param domain
      @param authType
   */  
export interface DocStarTestConnection_input{
      /**  Document type ID, or empty string to test company access  */  
   docTypeID:string,
      /**  suggested user name  */  
   userName:string,
      /**  suggested password  */  
   userPwd:string,
      /**  domain for Windows authentication  */  
   domain:string,
      /**  Authentication type - NTLM or USERNAME  */  
   authType:string,
}

export interface DocStarTestConnection_output{
      /**  Message that connection succeeded. In case of failure exception will be thrown  */  
   returnObj:string,
}

   /** Required : 
      @param queryID
      @param executionParams
   */  
export interface ExecuteBaq_input{
      /**  The current Query ID  */  
   queryID:string,
      /**  The collection of Query execution parameters (named parameter values, filtering and etc.)  */  
   executionParams:Ice_Tablesets_QueryExecutionTableset[],
}

export interface ExecuteBaq_output{
      /**  Returns the collection of results from each of the query executions.  */  
   returnObj:object
}

export interface GetAdapterList_output{
   returnObj:string,
}

   /** Required : 
      @param formKey
   */  
export interface GetConfirmDialogUserOptions_input{
      /**  Key for the UI form.  */  
   formKey:string,
}

export interface GetConfirmDialogUserOptions_output{
   returnObj:Ice_BO_KineticErp_ErpDialogConfirmOption[],
}

   /** Required : 
      @param ids
   */  
export interface GetDatasetTables_input{
      /**  The collection of system code and dataset ids.  */  
   ids:Ice_BO_KineticErp_ErpDatasetId[],
}

export interface GetDatasetTables_output{
      /**  The collection of <cref>ErpDataset</cref>.  */  
   returnObj:Ice_BO_KineticErp_ErpDataset[],
}

   /** Required : 
      @param id
   */  
export interface GetEmbedGrowMetricUrl_input{
      /**  Metric id  */  
   id:string,
}

export interface GetEmbedGrowMetricUrl_output{
   returnObj:any,      //schema had no properties on an object.
}

export interface GetFeaturesAndLicenses_output{
   returnObj:Ice_BO_KineticErp_ErpFeaturesAndLicenses[],
}

export interface GetGrowMetrics_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param companyId
   */  
export interface GetHomepageCompany_input{
   companyId:string,
}

export interface GetHomepageCompany_output{
   returnObj:any,      //schema had no properties on an object.
}

export interface GetInstallationSettings_output{
   returnObj:Ice_BO_KineticErp_InstallationSettings[],
}

export interface GetLaunchModes_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param adapterName
   */  
export interface GetLikeFieldForAdapter_input{
      /**  The adapter name  */  
   adapterName:string,
}

export interface GetLikeFieldForAdapter_output{
   returnObj:string,
}

   /** Required : 
      @param context
   */  
export interface GetSearchOptions_input{
   context:Ice_BO_KineticErp_ErpSearchContext[],
}

export interface GetSearchOptions_output{
   returnObj:Ice_BO_KineticErp_ErpSearchOptions[],
}

   /** Required : 
      @param tokenDataType
   */  
export interface GetTokenList_input{
      /**  Type of token for which you want the list of valid values. Valid Types are; Date, FiscalPeriod, FiscalYear  */  
   tokenDataType:string,
}

export interface GetTokenList_output{
   returnObj:string,
}

   /** Required : 
      @param token
   */  
export interface GetTokenValue_input{
      /**  Type of token  */  
   token:string,
}

export interface GetTokenValue_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   tokenValue:string,
}
}

export interface GetUserSessionAndVersion_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param formKey
   */  
export interface GetUserSettingsForView_input{
      /**  The unique view key. Example: App.AbcCodeEntry.AbcCodeForm  */  
   formKey:string,
}

export interface GetUserSettingsForView_output{
   returnObj:Ice_BO_KineticErp_ErpUserSettingsForView[],
}

export interface Ice_BO_KineticErp_ErpDataset{
   systemCode:string,
   datasetId:string,
   tables:Ice_BO_KineticErp_ErpDatasetTable[],
}

export interface Ice_BO_KineticErp_ErpDatasetId{
   systemCode:string,
   datasetId:string,
}

export interface Ice_BO_KineticErp_ErpDatasetTable{
   systemCode:string,
   tableId:string,
   keys:string,
   isPrimaryTable:boolean,
   childAttachmentTableName:string,
   parentAttachmentTableName:string,
   changeLogTableName:string,
   memoTableName:string,
}

export interface Ice_BO_KineticErp_ErpDialogConfirmOption{
   optionName:string,
   optionEnabled:boolean,
   key:string,
}

export interface Ice_BO_KineticErp_ErpFeatureFlag{
   Identifier:string,
   Name:string,
   isEnabled:boolean,
}

export interface Ice_BO_KineticErp_ErpFeaturesAndLicenses{
   FeatureFlags:Ice_BO_KineticErp_ErpFeatureFlag[],
   LicensedModules:Ice_BO_KineticErp_ErpLicensedModule[],
   LicensedCsfModules:Ice_BO_KineticErp_ErpLicensedModule[],
}

export interface Ice_BO_KineticErp_ErpLicensedModule{
   Identifier:string,
   Name:string,
   isLicensed:boolean,
   isEnabled:boolean,
}

export interface Ice_BO_KineticErp_ErpPrinterProperties{
   Company:string,
   PrinterID:string,
   Description:string,
   NetworkPath:string,
   PageColor:boolean,
   PageLandscape:boolean,
   PageLeftMargin:number,
   PageRightMargin:number,
   PageTopMargin:number,
   PageBottomMargin:number,
   PagePaperSizeKind:string,
   PagePaperHeight:number,
   PagePaperWidth:number,
   PagePaperSourceKind:string,
   PagePrinterResolutionX:number,
   PagePrinterResolutionY:number,
   PageDuplex:string,
   FromPage:number,
   ToPage:number,
   Copies:number,
   CanDuplex:boolean,
   Collate:boolean,
   IsDefaultPrinter:boolean,
   PagePaperSourceRawKind:number,
   PagePaperSourceName:string,
   PagePaperSizeName:string,
}

export interface Ice_BO_KineticErp_ErpSearchContext{
   product:string,
   searchName:string,
   calledFrom:string,
   likeTableName:string,
   likeFieldName:string,
   includeQuickSearchWithNoCriteria:boolean,
}

export interface Ice_BO_KineticErp_ErpSearchOptions{
   namedSearches:Ice_IceTableset[],
   quickSearches:Ice_IceTableset[],
   baqSearches:Ice_IceTableset[],
   advancedSearches:Ice_IceTableset[],
   baseDefaultQuickSearch:string,
   contextDefaultQuickSearch:string,
}

export interface Ice_BO_KineticErp_ErpUserSettingsForView{
   gridLayouts:any,      //schema had no properties on an object.
}

export interface Ice_BO_KineticErp_IceEmailMessageRequest{
   from:string,
   attachments:string,
   removeAttachmentFromSpecialFolder:boolean,
   attachmentSpecialFolder:number,
   body:string,
   subject:string,
   to:string,
   cc:string,
   bcc:string,
   priority:number,
   isBodyHtml:boolean,
}

export interface Ice_BO_KineticErp_IceEmailMessageRequestWithIncludedAttachments{
   from:string,
   includedAttachments:System_Collections_Generic_KeyValuePair_System_String_System_ByteArray[],
   body:string,
   subject:string,
   to:string,
   cc:string,
   bcc:string,
   priority:number,
   isBodyHtml:boolean,
}

export interface Ice_BO_KineticErp_InstallationSettings{
   Name:string,
   Color:string,
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

export interface Ice_IceTableset{
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ExecutionFilterRow{
   DataTableID:string,
   FieldName:string,
   Neg:boolean,
   CompOp:string,
   RValue:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_Tablesets_ExecutionParameterRow{
   ParameterID:string,
   ParameterValue:string,
   ValueType:string,
   IsEmpty:boolean,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_Tablesets_ExecutionSettingRow{
   Name:string,
   Value:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_Tablesets_ExecutionValueSetItemsRow{
   ValueSetID:string,
   ItemValue:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_Tablesets_QueryExecutionTableset{
   ExecutionFilter:Ice_Tablesets_ExecutionFilterRow[],
   ExecutionParameter:Ice_Tablesets_ExecutionParameterRow[],
   ExecutionSetting:Ice_Tablesets_ExecutionSettingRow[],
   ExecutionValueSetItems:Ice_Tablesets_ExecutionValueSetItemsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param formKey
      @param gridId
      @param layout
   */  
export interface SaveGridLayout_input{
      /**  The unique view key. Example: App.AbcCodeEntry.AbcCodeForm  */  
   formKey:string,
      /**  The unique grid id from the view.  */  
   gridId:string,
      /**  The serialized layout for the grid  */  
   layout:string,
}

export interface SaveGridLayout_output{
}

   /** Required : 
      @param message
   */  
export interface SendEmailWithClientAttachments_input{
   message:Ice_BO_KineticErp_IceEmailMessageRequestWithIncludedAttachments[],
}

export interface SendEmailWithClientAttachments_output{
}

   /** Required : 
      @param message
   */  
export interface SendEmail_input{
   message:Ice_BO_KineticErp_IceEmailMessageRequest[],
}

export interface SendEmail_output{
}

   /** Required : 
      @param printerPageProperties
   */  
export interface SerializePrinterAndPageSettings_input{
   printerPageProperties:Ice_BO_KineticErp_ErpPrinterProperties[],
}

export interface SerializePrinterAndPageSettings_output{
parameters : {
      /**  output parameters  */  
   serializedPrinterSettings:string,
   serializedPageSettings:string,
}
}

export interface System_Collections_Generic_KeyValuePair_System_String_System_ByteArray{
   Key:string,
   Value:string,
}

   /** Required : 
      @param queryID
      @param actionID
      @param queryResultDataset
   */  
export interface UpdateBaqCustomAction_input{
      /**  Updatable query id  */  
   queryID:string,
      /**  An action id  */  
   actionID:string,
      /**  Query result dataset with a changed row  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface UpdateBaqCustomAction_output{
      /**  Query result dataset with a changed row  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryID
      @param fieldName
      @param queryResultDataset
   */  
export interface UpdateBaqFieldUpdate_input{
      /**  Updatable query id  */  
   queryID:string,
      /**  Name of an updatable field  */  
   fieldName:string,
      /**  Query result dataset with a row where the field is going to be updated  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface UpdateBaqFieldUpdate_output{
      /**  Query result dataset with a row where the field is going to be updated  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryID
      @param fieldName
      @param fieldValue
      @param queryResultDataset
   */  
export interface UpdateBaqFieldValidate_input{
      /**  Updatable query id  */  
   queryID:string,
      /**  Name of an updatable field  */  
   fieldName:string,
      /**  The proposed value for the field  */  
   fieldValue:any,      //schema had no properties on an object.
      /**  Query result dataset with a changed row  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface UpdateBaqFieldValidate_output{
      /**  Query result dataset with a row where the field is going to be updated  */  
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   isValid:boolean,
}
}

   /** Required : 
      @param queryID
      @param queryResultDataset
   */  
export interface UpdateBaq_input{
      /**  Updatable query id  */  
   queryID:string,
      /**  Query result dataset  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface UpdateBaq_output{
      /**  Result of Update method call. Usually this is incoming query result dataset with some changes  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param formKey
      @param confirmOptions
   */  
export interface UpdateConfirmDialogOptions_input{
      /**  The form key.  */  
   formKey:string,
      /**  The confirmOptions (all items are expected).  */  
   confirmOptions:Ice_BO_KineticErp_ErpDialogConfirmOption[],
}

export interface UpdateConfirmDialogOptions_output{
}

   /** Required : 
      @param installationSettings
   */  
export interface UpdateInstallationSettings_input{
   installationSettings:Ice_BO_KineticErp_InstallationSettings[],
}

export interface UpdateInstallationSettings_output{
}

