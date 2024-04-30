import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.LIB.CdcSubscriberSvc
// Description: Cdc Subscriber API
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", {
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
   Summary: Invoke method Register
   Description: Register a new subscriber for the API
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/Register", {
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
   Summary: Invoke method Unregister
   Description: Unregister a subscriber
   OperationID: Unregister
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Unregister_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Unregister_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Unregister(requestBody:Unregister_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Unregister_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/Unregister", {
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
         resolve(data as Unregister_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SubscriberUpdate
   Description: Update a subscriber's configuration
   OperationID: SubscriberUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SubscriberUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubscriberUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubscriberUpdate(requestBody:SubscriberUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SubscriberUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/SubscriberUpdate", {
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
         resolve(data as SubscriberUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RegenerateSecret
   Description: Generate a new secret for a subscriber
   OperationID: RegenerateSecret
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RegenerateSecret_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenerateSecret_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RegenerateSecret(requestBody:RegenerateSecret_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RegenerateSecret_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/RegenerateSecret", {
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
         resolve(data as RegenerateSecret_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RuleGet
   OperationID: RuleGet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RuleGet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleGet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RuleGet(requestBody:RuleGet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RuleGet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/RuleGet", {
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
         resolve(data as RuleGet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RuleAdd
   Description: Add a rule for a specific subscriber
   OperationID: RuleAdd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RuleAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RuleAdd(requestBody:RuleAdd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RuleAdd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/RuleAdd", {
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
         resolve(data as RuleAdd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RuleRemove
   Description: Remove a rule from a specific subscriber
   OperationID: RuleRemove
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RuleRemove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleRemove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RuleRemove(requestBody:RuleRemove_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RuleRemove_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/RuleRemove", {
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
         resolve(data as RuleRemove_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RuleUpdate
   Description: Update a rule
   OperationID: RuleUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RuleUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RuleUpdate(requestBody:RuleUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RuleUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/RuleUpdate", {
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
         resolve(data as RuleUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RulesList
   Description: List out all the rules for a specific subscriber
   OperationID: RulesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RulesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RulesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RulesList(requestBody:RulesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RulesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/RulesList", {
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
         resolve(data as RulesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RuleTableList
   Description: List tables that have been enabled for CDC and can be used for rules
   OperationID: RuleTableList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RuleTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RuleTableList(requestBody:RuleTableList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RuleTableList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/RuleTableList", {
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
         resolve(data as RuleTableList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateSampleData
   Description: Generate sample data for a given table
   OperationID: GenerateSampleData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateSampleData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSampleData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateSampleData(requestBody:GenerateSampleData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateSampleData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/GenerateSampleData", {
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
         resolve(data as GenerateSampleData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateLookupSampleData
   Description: Generate sample data for the lookups on a given table
   OperationID: GenerateLookupSampleData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateLookupSampleData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateLookupSampleData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateLookupSampleData(requestBody:GenerateLookupSampleData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateLookupSampleData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/GenerateLookupSampleData", {
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
         resolve(data as GenerateLookupSampleData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateKeyTags
   Description: Generate Tags based on the primary key columns
   OperationID: GenerateKeyTags
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateKeyTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateKeyTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateKeyTags(requestBody:GenerateKeyTags_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateKeyTags_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/GenerateKeyTags", {
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
         resolve(data as GenerateKeyTags_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLookupLinks
   Description: Get look up links available for a specific table
   OperationID: GetLookupLinks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLookupLinks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupLinks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLookupLinks(requestBody:GetLookupLinks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLookupLinks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/GetLookupLinks", {
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
         resolve(data as GetLookupLinks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLookupDataFields
   Description: Get data fields for a specific look up on a table
   OperationID: GetLookupDataFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLookupDataFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupDataFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLookupDataFields(requestBody:GetLookupDataFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLookupDataFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/GetLookupDataFields", {
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
         resolve(data as GetLookupDataFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Pull
   Description: Pull messages from the subscriber queue.
   OperationID: Pull
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Pull_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Pull_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Pull(requestBody:Pull_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Pull_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/Pull", {
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
         resolve(data as Pull_output)
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
      @param subscriberID
      @param secret
      @param schemaName
      @param tableName
   */  
export interface GenerateKeyTags_input{
      /**  Subscriber's ID  */  
   subscriberID:string,
      /**  Subscriber's secret  */  
   secret:string,
      /**  Schema  */  
   schemaName:string,
      /**  Table  */  
   tableName:string,
}

export interface GenerateKeyTags_output{
      /**  Tags  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param subscriberID
      @param secret
      @param schemaName
      @param tableName
      @param lookupIDs
   */  
export interface GenerateLookupSampleData_input{
   subscriberID:string,
      /**  Secret  */  
   secret:string,
      /**  Schema name  */  
   schemaName:string,
      /**  Table name  */  
   tableName:string,
      /**  Lookup IDs to include  */  
   lookupIDs:string,
}

export interface GenerateLookupSampleData_output{
      /**  Sample data for table  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param subscriberID
      @param secret
      @param schemaName
      @param tableName
   */  
export interface GenerateSampleData_input{
   subscriberID:string,
      /**  Secret  */  
   secret:string,
      /**  Schema name  */  
   schemaName:string,
      /**  Table name  */  
   tableName:string,
}

export interface GenerateSampleData_output{
      /**  Sample data for table  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param subscriberID
      @param secret
      @param schemaName
      @param tableName
      @param lookupID
   */  
export interface GetLookupDataFields_input{
      /**  Subscriber's ID  */  
   subscriberID:string,
      /**  Subscriber's secret  */  
   secret:string,
      /**  Schema  */  
   schemaName:string,
      /**  Table  */  
   tableName:string,
      /**  Lookup ID  */  
   lookupID:string,
}

export interface GetLookupDataFields_output{
      /**  List of lookup links  */  
   returnObj:string,
}

   /** Required : 
      @param subscriberID
      @param secret
      @param schemaName
      @param tableName
   */  
export interface GetLookupLinks_input{
      /**  Subscriber's ID  */  
   subscriberID:string,
      /**  Subscriber's secret  */  
   secret:string,
      /**  Schema  */  
   schemaName:string,
      /**  Table  */  
   tableName:string,
}

export interface GetLookupLinks_output{
      /**  List of lookup links  */  
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

export interface Ice_Lib_CdcSubscriber_PullResponse{
   results:Ice_Lib_CdcSubscriber_SubscriberQueue[],
   morePages:boolean,
   lastOffset:number,
}

export interface Ice_Lib_CdcSubscriber_SubscriberQueue{
   company:string,
   schemaName:string,
   tableName:string,
   keys:string,
   ruleID:string,
   data:string,
   metadata:string,
   occurredWhenUtc:string,
}

export interface Ice_Tablesets_CdcSubscriberRuleRow{
   SubscriberID:string,
   RuleID:string,
   SchemaName:string,
   TableName:string,
   ChangeType:string,
   SystemFlag:boolean,
   Inactive:boolean,
   LastUpdated:string,
   LastUpdatedBy:string,
   Description:string,
   Company:string,
      /**  Security Code  */  
   SecCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_CdcSubscriberRuleTableset{
   CdcSubscriberRule:Ice_Tablesets_CdcSubscriberRuleRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param subscriberID
      @param secret
      @param offset
      @param pageSize
   */  
export interface Pull_input{
      /**  Subscriber ID  */  
   subscriberID:string,
      /**  Subscriber's secret  */  
   secret:string,
      /**  Offset to start from, when 0 is supplied will read from end of last offset read up to  */  
   offset:number,
      /**  Max amount of messages to return  */  
   pageSize:number,
}

export interface Pull_output{
   returnObj:Ice_Lib_CdcSubscriber_PullResponse[],
}

   /** Required : 
      @param subscriberID
      @param oldSecret
   */  
export interface RegenerateSecret_input{
      /**  Subscriber ID  */  
   subscriberID:string,
      /**  Old secret  */  
   oldSecret:string,
}

export interface RegenerateSecret_output{
parameters : {
      /**  output parameters  */  
   newSecret:string,
}
}

   /** Required : 
      @param description
      @param mode
      @param webHookURI
      @param webHookHeaders
   */  
export interface Register_input{
      /**  Description of Subscriber  */  
   description:string,
      /**  Subscriber Mode - "PUSH", "PUSHPULL" or "PULL"  */  
   mode:string,
      /**  Web Hook URI for Push or Push-Pull  */  
   webHookURI:string,
      /**  Web Hook Headers, only valid for Push or Push-Pull  */  
   webHookHeaders:string,
}

export interface Register_output{
parameters : {
      /**  output parameters  */  
   subscriberID:string,
   secret:string,
}
}

   /** Required : 
      @param subscriberID
      @param secret
      @param companyID
      @param ruleID
      @param description
      @param schemaName
      @param tableName
      @param changeType
      @param rule
      @param metadataRule
      @param lookupLinks
      @param inactive
      @param secCode
   */  
export interface RuleAdd_input{
      /**  Subscriber ID  */  
   subscriberID:string,
      /**  Subscriber's secret  */  
   secret:string,
      /**  Company the rule is assigned to  */  
   companyID:string,
      /**  Rule ID  */  
   ruleID:string,
      /**  Description of rule  */  
   description:string,
      /**  Schema rule applies to  */  
   schemaName:string,
      /**  Table rule applies to  */  
   tableName:string,
      /**  Change type rule applies to, valid options are insert, update and delete  */  
   changeType:string,
      /**  Rule JSON logic  */  
   rule:string,
      /**  Metadata JSON logic output  */  
   metadataRule:string,
      /**  Look up links  */  
   lookupLinks:string,
      /**  Whether rule is currently active  */  
   inactive:boolean,
      /**  Security code assigned to rule  */  
   secCode:string,
}

export interface RuleAdd_output{
}

   /** Required : 
      @param subscriberID
      @param secret
      @param companyID
      @param ruleID
   */  
export interface RuleGet_input{
   subscriberID:string,
   secret:string,
   companyID:string,
   ruleID:string,
}

export interface RuleGet_output{
parameters : {
      /**  output parameters  */  
   description:string,
   schemaName:string,
   tableName:string,
   changeType:string,
   rule:string,
   metadataRule:string,
   lookupLinks:string,
   systemFlag:boolean,
   inactive:boolean,
   lastUpdated:string,
   lastUpdatedBy:string,
   secCode:string,
}
}

   /** Required : 
      @param subscriberID
      @param secret
      @param companyID
      @param ruleID
   */  
export interface RuleRemove_input{
      /**  Subscriber ID  */  
   subscriberID:string,
      /**  Subscriber's secret  */  
   secret:string,
      /**  Company the rule is assigned to  */  
   companyID:string,
      /**  Rule ID  */  
   ruleID:string,
}

export interface RuleRemove_output{
}

   /** Required : 
      @param subscriberID
      @param secret
   */  
export interface RuleTableList_input{
      /**  Subscriber ID  */  
   subscriberID:string,
      /**  Secret  */  
   secret:string,
}

export interface RuleTableList_output{
      /**  List of available tables  */  
   returnObj:array
}

   /** Required : 
      @param subscriberID
      @param secret
      @param companyID
      @param ruleID
      @param description
      @param changeType
      @param rule
      @param metadataRule
      @param lookupLinks
      @param inactive
      @param secCode
   */  
export interface RuleUpdate_input{
      /**  Subscriber ID  */  
   subscriberID:string,
      /**  Subscriber's secret  */  
   secret:string,
      /**  Company the rule is assigned to  */  
   companyID:string,
      /**  ID of rule being updated  */  
   ruleID:string,
      /**  Description of rule  */  
   description:string,
      /**  Change types rule applies to, valid options are insert, update and delete  */  
   changeType:string,
      /**  Rule JSON logic, passing null will ignore column from updating  */  
   rule:string,
      /**  Metadata JSON logic output  */  
   metadataRule:string,
      /**  Look up links  */  
   lookupLinks:string,
      /**  Set the rule to active/inactive  */  
   inactive:boolean,
      /**  Security code assigned to rule  */  
   secCode:string,
}

export interface RuleUpdate_output{
}

   /** Required : 
      @param subscriberID
      @param secret
      @param companyID
      @param description
      @param schemaName
      @param tableName
      @param excludeSystem
      @param skip
      @param pageSize
   */  
export interface RulesList_input{
      /**  Subscriber ID  */  
   subscriberID:string,
      /**  Subscriber's secret  */  
   secret:string,
      /**  Company, blank to list all available companies  */  
   companyID:string,
      /**  Contains description  */  
   description:string,
      /**  Filter to specific schema  */  
   schemaName:string,
      /**  Filter to specific table  */  
   tableName:string,
      /**  Exclude System rules  */  
   excludeSystem:boolean,
      /**  Skip n results  */  
   skip:number,
      /**  Page size, maximum 200  */  
   pageSize:number,
}

export interface RulesList_output{
   returnObj:Ice_Tablesets_CdcSubscriberRuleTableset[],
parameters : {
      /**  output parameters  */  
   pageSize:number,
   morePages:boolean,
   total:number,
}
}

   /** Required : 
      @param subscriberID
      @param secret
      @param description
      @param inactive
      @param webHookURI
      @param webHookHeaders
      @param pageSize
      @param TTLRead
      @param TTLUnread
   */  
export interface SubscriberUpdate_input{
      /**  Subscriber ID  */  
   subscriberID:string,
      /**  Subscriber's secret  */  
   secret:string,
      /**  New description  */  
   description:string,
      /**  Set subscriber to inactive  */  
   inactive:boolean,
      /**  Web Hook URI, only valid for Push or Push-Pull  */  
   webHookURI:string,
      /**  Web Hook Headers, only valid for Push or Push-Pull  */  
   webHookHeaders:string,
      /**  Page size for messages are pushed/pulled  */  
   pageSize:number,
      /**  How long to keep read messages, in seconds  */  
   TTLRead:number,
      /**  How long to keep unread messages, in seconds  */  
   TTLUnread:number,
}

export interface SubscriberUpdate_output{
}

   /** Required : 
      @param subscriberID
      @param secret
   */  
export interface Unregister_input{
      /**  Subscriber ID  */  
   subscriberID:string,
      /**  Subscriber's secret  */  
   secret:string,
}

export interface Unregister_output{
}

