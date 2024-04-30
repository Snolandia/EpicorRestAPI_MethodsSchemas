import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.LIB.SynergySvc
// Description: Interacts with Synergy.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/$metadata", {
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
   Summary: Invoke method GetSynergyUrl
   Description: Retrieves the Synergy URL.
   OperationID: GetSynergyUrl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSynergyUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSynergyUrl(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSynergyUrl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetSynergyUrl", {
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
         resolve(data as GetSynergyUrl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSynergyApiUrl
   Description: Retrieves the Synergy API URL.
   OperationID: GetSynergyApiUrl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSynergyApiUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSynergyApiUrl(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSynergyApiUrl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetSynergyApiUrl", {
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
         resolve(data as GetSynergyApiUrl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Register
   Description: Register for Synergy.
   OperationID: Register
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Register_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Register_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Register(requestBody:Register_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Register_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/Register", {
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
         resolve(data as Register_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Login
   Description: Login to Synergy.
   OperationID: Login
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Login_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Login_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Login(requestBody:Login_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Login_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/Login", {
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
         resolve(data as Login_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DownloadFile
   Description: Download Non ERP file from any DMS
   OperationID: DownloadFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DownloadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DownloadFile(requestBody:DownloadFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DownloadFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/DownloadFile", {
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
         resolve(data as DownloadFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteFile
   Description: Delete Non ERP file from any DMS
   OperationID: DeleteFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteFile(requestBody:DeleteFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/DeleteFile", {
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
         resolve(data as DeleteFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultCompanyStorage
   OperationID: GetDefaultCompanyStorage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultCompanyStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultCompanyStorage(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultCompanyStorage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetDefaultCompanyStorage", {
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
         resolve(data as GetDefaultCompanyStorage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UploadFile
   Description: Upload Non ERP file to any DMS
   OperationID: UploadFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UploadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadFile(requestBody:UploadFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UploadFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/UploadFile", {
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
         resolve(data as UploadFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEnabledStorageTypes
   Description: Gets the enabled storage types.
   OperationID: GetEnabledStorageTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEnabledStorageTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEnabledStorageTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEnabledStorageTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetEnabledStorageTypes", {
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
         resolve(data as GetEnabledStorageTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetHealthInfo
   Description: Gets information for the health check.
   OperationID: GetHealthInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHealthInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHealthInfo(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetHealthInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetHealthInfo", {
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
         resolve(data as GetHealthInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeployRules
   Description: Deploy rules.
   OperationID: DeployRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeployRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeployRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeployRules(requestBody:DeployRules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeployRules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/DeployRules", {
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
         resolve(data as DeployRules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Reconnect
   Description: Reconnect to a previous Collaborate environment.
   OperationID: Reconnect
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Reconnect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Reconnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Reconnect(requestBody:Reconnect_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Reconnect_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/Reconnect", {
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
         resolve(data as Reconnect_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Disconnect
   Description: Disconnect from the current Collaborate environment.
   OperationID: Disconnect
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Disconnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Disconnect(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Disconnect_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/Disconnect", {
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
         resolve(data as Disconnect_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Configure
   Description: Configure Synergy.
   OperationID: Configure
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Configure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Configure_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Configure(requestBody:Configure_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Configure_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/Configure", {
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
         resolve(data as Configure_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDetails
   Description: Gets details about a record.
   OperationID: GetDetails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDetails(requestBody:GetDetails_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDetails_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetDetails", {
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
         resolve(data as GetDetails_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEntityInfoFromTags
   Description: Get the status of an entity based on the related tags
   OperationID: GetEntityInfoFromTags
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetEntityInfoFromTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEntityInfoFromTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEntityInfoFromTags(requestBody:GetEntityInfoFromTags_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEntityInfoFromTags_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetEntityInfoFromTags", {
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
         resolve(data as GetEntityInfoFromTags_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRuleCategories
   Description: Get Rule Categories currently in use by a specific company
   OperationID: GetRuleCategories
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRuleCategories_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRuleCategories_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRuleCategories(requestBody:GetRuleCategories_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRuleCategories_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetRuleCategories", {
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
         resolve(data as GetRuleCategories_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetActivityFeed
   Description: Get the activity feed for the company
   OperationID: GetActivityFeed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetActivityFeed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActivityFeed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetActivityFeed(requestBody:GetActivityFeed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetActivityFeed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetActivityFeed", {
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
         resolve(data as GetActivityFeed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MarkActivityRead
   Description: Mark an activity read in Collobrate
   OperationID: MarkActivityRead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MarkActivityRead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkActivityRead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MarkActivityRead(requestBody:MarkActivityRead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MarkActivityRead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/MarkActivityRead", {
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
         resolve(data as MarkActivityRead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MarkActivityUnread
   Description: Mark an activity unread in Collaborate
   OperationID: MarkActivityUnread
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MarkActivityUnread_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkActivityUnread_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MarkActivityUnread(requestBody:MarkActivityUnread_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MarkActivityUnread_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/MarkActivityUnread", {
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
         resolve(data as MarkActivityUnread_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRules
   Description: Get rules for a specific category
   OperationID: GetRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRules(requestBody:GetRules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetRules", {
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
         resolve(data as GetRules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRulesListWithSecurityCode
   Description: Get rules for a specific category
   OperationID: GetRulesListWithSecurityCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRulesListWithSecurityCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRulesListWithSecurityCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRulesListWithSecurityCode(requestBody:GetRulesListWithSecurityCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRulesListWithSecurityCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetRulesListWithSecurityCode", {
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
         resolve(data as GetRulesListWithSecurityCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailableGroups
   Description: Get list of available Collaborate groups (public and private) for current user
   OperationID: GetAvailableGroups
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAvailableGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableGroups(requestBody:GetAvailableGroups_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailableGroups_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetAvailableGroups", {
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
         resolve(data as GetAvailableGroups_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PostContentToCollaborate
   Description: Share message content on Collaborate channel or group
   OperationID: PostContentToCollaborate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PostContentToCollaborate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostContentToCollaborate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostContentToCollaborate(requestBody:PostContentToCollaborate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PostContentToCollaborate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/PostContentToCollaborate", {
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
         resolve(data as PostContentToCollaborate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUsersForCompany
   Description: Gets all users for a company
   OperationID: GetUsersForCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetUsersForCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUsersForCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUsersForCompany(requestBody:GetUsersForCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetUsersForCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetUsersForCompany", {
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
         resolve(data as GetUsersForCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUsersForGroup
   Description: Gets all members for a group
   OperationID: GetUsersForGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetUsersForGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUsersForGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUsersForGroup(requestBody:GetUsersForGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetUsersForGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetUsersForGroup", {
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
         resolve(data as GetUsersForGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCollaborateUserDefinedRuleSecurityCodes
   Description: Get User Defined Security Code for Collaborate Notification rules
   OperationID: GetCollaborateUserDefinedRuleSecurityCodes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateUserDefinedRuleSecurityCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCollaborateUserDefinedRuleSecurityCodes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCollaborateUserDefinedRuleSecurityCodes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetCollaborateUserDefinedRuleSecurityCodes", {
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
         resolve(data as GetCollaborateUserDefinedRuleSecurityCodes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCollaborateSecurityCodes
   Description: Get All Security Code for Collaborate Notification rules
   OperationID: GetCollaborateSecurityCodes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateSecurityCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCollaborateSecurityCodes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCollaborateSecurityCodes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetCollaborateSecurityCodes", {
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
         resolve(data as GetCollaborateSecurityCodes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSecurityAccessForUsers
   Description: Return the list of users and their accessible security codes
   OperationID: GetSecurityAccessForUsers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSecurityAccessForUsers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSecurityAccessForUsers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSecurityAccessForUsers(requestBody:GetSecurityAccessForUsers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSecurityAccessForUsers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetSecurityAccessForUsers", {
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
         resolve(data as GetSecurityAccessForUsers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCollaborateSecurityCodeAccessRights
   Description: Get Access status for current user for the collaborate security codes
   OperationID: GetCollaborateSecurityCodeAccessRights
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateSecurityCodeAccessRights_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCollaborateSecurityCodeAccessRights(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCollaborateSecurityCodeAccessRights_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetCollaborateSecurityCodeAccessRights", {
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
         resolve(data as GetCollaborateSecurityCodeAccessRights_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCollaborateSecurityCodeAccessStatus
   Description: Check the access status for the current user for the given security code
   OperationID: GetCollaborateSecurityCodeAccessStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCollaborateSecurityCodeAccessStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateSecurityCodeAccessStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCollaborateSecurityCodeAccessStatus(requestBody:GetCollaborateSecurityCodeAccessStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCollaborateSecurityCodeAccessStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetCollaborateSecurityCodeAccessStatus", {
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
         resolve(data as GetCollaborateSecurityCodeAccessStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCollaborateSecurityCodeUserAccessStatus
   Description: Check the access status for a user for the given security code
   OperationID: GetCollaborateSecurityCodeUserAccessStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCollaborateSecurityCodeUserAccessStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateSecurityCodeUserAccessStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCollaborateSecurityCodeUserAccessStatus(requestBody:GetCollaborateSecurityCodeUserAccessStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCollaborateSecurityCodeUserAccessStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/GetCollaborateSecurityCodeUserAccessStatus", {
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
         resolve(data as GetCollaborateSecurityCodeUserAccessStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateCollaborateUserDefinedRuleSecurityCode
   Description: Create User Defined Security Code for Collaborate Notification rules
   OperationID: CreateCollaborateUserDefinedRuleSecurityCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateCollaborateUserDefinedRuleSecurityCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateCollaborateUserDefinedRuleSecurityCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateCollaborateUserDefinedRuleSecurityCode(requestBody:CreateCollaborateUserDefinedRuleSecurityCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateCollaborateUserDefinedRuleSecurityCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SynergySvc/CreateCollaborateUserDefinedRuleSecurityCode", {
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
         resolve(data as CreateCollaborateUserDefinedRuleSecurityCode_output)
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
      @param url
      @param apiUrl
      @param id
      @param secret
      @param subscriber
   */  
export interface Configure_input{
      /**  A new URL, or null/empty to leave it unchanged.  */  
   url:string,
      /**  A new API URL, or null/empty to leave it unchanged.  */  
   apiUrl:string,
      /**  A new ID, or null/empty to leave it unchanged.  */  
   id:string,
      /**  A new secret, or null/empty to leave it unchanged.  */  
   secret:string,
      /**  A new subscriber, or null/empty to leave it unchanged.  */  
   subscriber:string,
}

export interface Configure_output{
}

   /** Required : 
      @param category
   */  
export interface CreateCollaborateUserDefinedRuleSecurityCode_input{
   category:string,
}

export interface CreateCollaborateUserDefinedRuleSecurityCode_output{
   returnObj:string,
}

   /** Required : 
      @param fileDetails
      @param token
      @param companyId
      @param storageType
   */  
export interface DeleteFile_input{
   fileDetails:any,      //schema had no properties on an object.
   token:string,
   companyId:string,
   storageType:number,
}

export interface DeleteFile_output{
}

   /** Required : 
      @param company
      @param rules
   */  
export interface DeployRules_input{
      /**  The company to deploy to, or null/empty to deploy to all companies that the current user has access to.  */  
   company:string,
      /**  The rules to deploy.  */  
   rules:string,
}

export interface DeployRules_output{
}

export interface Disconnect_output{
}

   /** Required : 
      @param xFileRefNum
      @param companyId
      @param storageType
   */  
export interface DownloadFile_input{
   xFileRefNum:number,
   companyId:string,
   storageType:number,
}

export interface DownloadFile_output{
   returnObj:string,
}

   /** Required : 
      @param companyID
      @param token
      @param queryParams
   */  
export interface GetActivityFeed_input{
      /**  Company  */  
   companyID:string,
   token:string,
   queryParams:string,
}

export interface GetActivityFeed_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param companyID
      @param queryParams
   */  
export interface GetAvailableGroups_input{
   companyID:string,
   queryParams:string,
}

export interface GetAvailableGroups_output{
   returnObj:object
}

export interface GetCollaborateSecurityCodeAccessRights_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param secCode
   */  
export interface GetCollaborateSecurityCodeAccessStatus_input{
   secCode:string,
}

export interface GetCollaborateSecurityCodeAccessStatus_output{
   returnObj:boolean,
}

   /** Required : 
      @param secCode
      @param userId
   */  
export interface GetCollaborateSecurityCodeUserAccessStatus_input{
   secCode:string,
   userId:string,
}

export interface GetCollaborateSecurityCodeUserAccessStatus_output{
   returnObj:boolean,
}

export interface GetCollaborateSecurityCodes_output{
   returnObj:string,
}

export interface GetCollaborateUserDefinedRuleSecurityCodes_output{
   returnObj:string,
}

export interface GetDefaultCompanyStorage_output{
      /**  Default Company DMS Value  */  
   returnObj:number,
}

   /** Required : 
      @param record
   */  
export interface GetDetails_input{
      /**  Information used to identify the record.  */  
   record:string,
}

export interface GetDetails_output{
      /**  Record details.  */  
   returnObj:string,
}

export interface GetEnabledStorageTypes_output{
      /**  A list of enabled storage types.  */  
   returnObj:string,
}

   /** Required : 
      @param tags
   */  
export interface GetEntityInfoFromTags_input{
      /**  Tags to search on, at least one tag must be specified  */  
   tags:any,      //schema had no properties on an object.
}

export interface GetEntityInfoFromTags_output{
parameters : {
      /**  output parameters  */  
   notSupported:boolean,
   notFound:boolean,
   type:string,
   result:string,
}
}

export interface GetHealthInfo_output{
      /**  Health info.  */  
   returnObj:string,
}

   /** Required : 
      @param companyID
   */  
export interface GetRuleCategories_input{
      /**  Company to lookup  */  
   companyID:string,
}

export interface GetRuleCategories_output{
      /**  Categories (table names)  */  
   returnObj:string,
}

   /** Required : 
      @param companyID
      @param category
   */  
export interface GetRulesListWithSecurityCode_input{
      /**  Company to lookup  */  
   companyID:string,
      /**  Company to lookup  */  
   category:string,
}

export interface GetRulesListWithSecurityCode_output{
      /**  Rule description  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param companyID
      @param category
   */  
export interface GetRules_input{
      /**  Company to lookup  */  
   companyID:string,
      /**  Category (table name), blank for all categories  */  
   category:string,
}

export interface GetRules_output{
      /**  Rule description  */  
   returnObj:string,
}

   /** Required : 
      @param userIds
   */  
export interface GetSecurityAccessForUsers_input{
   userIds:string,
}

export interface GetSecurityAccessForUsers_output{
   returnObj:any,      //schema had no properties on an object.
}

export interface GetSynergyApiUrl_output{
      /**  The Synergy API URL.  */  
   returnObj:string,
}

export interface GetSynergyUrl_output{
      /**  The Synergy URL.  */  
   returnObj:string,
}

   /** Required : 
      @param companyID
   */  
export interface GetUsersForCompany_input{
   companyID:string,
}

export interface GetUsersForCompany_output{
   returnObj:object
}

   /** Required : 
      @param companyID
      @param groupID
   */  
export interface GetUsersForGroup_input{
   companyID:string,
   groupID:string,
}

export interface GetUsersForGroup_output{
   returnObj:object
}

   /** Required : 
      @param erpUrl
      @param erpToken
   */  
export interface Login_input{
      /**  The ERP URL.  */  
   erpUrl:string,
      /**  The ERP token.  */  
   erpToken:string,
}

export interface Login_output{
      /**  A Synergy token.  */  
   returnObj:string,
}

   /** Required : 
      @param token
      @param activityID
   */  
export interface MarkActivityRead_input{
      /**  Collaborate token  */  
   token:string,
      /**  Activity ID  */  
   activityID:string,
}

export interface MarkActivityRead_output{
}

   /** Required : 
      @param token
      @param activityID
   */  
export interface MarkActivityUnread_input{
      /**  Collaborate token  */  
   token:string,
      /**  Activity ID  */  
   activityID:string,
}

export interface MarkActivityUnread_output{
}

   /** Required : 
      @param content
      @param groupId
   */  
export interface PostContentToCollaborate_input{
   content:string,
   groupId:string,
}

export interface PostContentToCollaborate_output{
}

   /** Required : 
      @param recoveryKey
   */  
export interface Reconnect_input{
      /**  The environment's recovery key.  */  
   recoveryKey:string,
}

export interface Reconnect_output{
}

   /** Required : 
      @param synergyUrl
      @param synergyApiUrl
      @param erpUrl
      @param erpToken
   */  
export interface Register_input{
      /**  The Synergy front-end URL.  */  
   synergyUrl:string,
      /**  The Synergy API URL.  */  
   synergyApiUrl:string,
      /**  The ERP URL.  */  
   erpUrl:string,
      /**  The ERP token.  */  
   erpToken:string,
}

export interface Register_output{
      /**  The environment's recovery key.  */  
   returnObj:string,
}

   /** Required : 
      @param sourceFile
      @param fileData
      @param token
      @param storageType
   */  
export interface UploadFile_input{
   sourceFile:string,
   fileData:string,
   token:string,
   storageType:number,
}

export interface UploadFile_output{
   returnObj:any,      //schema had no properties on an object.
}

