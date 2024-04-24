import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.CdcManageSvc
// Description: Cdc Management Service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/$metadata", {
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
   Summary: Invoke method ListCaptureStatus
   Description: List the Capture Status
   OperationID: ListCaptureStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ListCaptureStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListCaptureStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListCaptureStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/ListCaptureStatus", {
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
   Summary: Invoke method EnableCapture
   Description: Enable capture on a list of tables
   OperationID: EnableCapture
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableCapture_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableCapture_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnableCapture(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/EnableCapture", {
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
   Summary: Invoke method DisableCapture
   Description: Disable capture on a list of tables
   OperationID: DisableCapture
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisableCapture_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisableCapture_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DisableCapture(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/DisableCapture", {
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
   Summary: Invoke method GenerateAvailableTables
   Description: Generate list of available tables that can have Change Capture enabled on them
This should only be used if a new table was created and the change capture trigger was added, or alternatively a trigger was disabled
   OperationID: GenerateAvailableTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateAvailableTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateAvailableTables(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GenerateAvailableTables", {
          method: 'post',
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
   Summary: Invoke method Register
   Description: Register a new subscriber for the API
   OperationID: Register
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Register_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Register_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Register(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/Register", {
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
   Summary: Invoke method Unregister
   Description: Unregister a subscriber
   OperationID: Unregister
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Unregister_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Unregister_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Unregister(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/Unregister", {
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
   Summary: Invoke method SubscriberUpdate
   Description: Update a subscriber's configuration
   OperationID: SubscriberUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubscriberUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubscriberUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubscriberUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/SubscriberUpdate", {
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
   Summary: Invoke method RegenerateSecret
   Description: Generate a new secret for a subscriber
   OperationID: RegenerateSecret
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegenerateSecret_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenerateSecret_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RegenerateSecret(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/RegenerateSecret", {
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
   Summary: Invoke method SubscribersList
   Description: List all CDC subscribers
   OperationID: SubscribersList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubscribersList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubscribersList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/SubscribersList", {
          method: 'post',
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
   Summary: Invoke method SubscriberGet
   Description: Get a specific CDC subscriber
   OperationID: SubscriberGet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubscriberGet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubscriberGet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubscriberGet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/SubscriberGet", {
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
   Summary: Invoke method RuleGet
   OperationID: RuleGet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleGet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleGet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RuleGet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/RuleGet", {
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
   Summary: Invoke method RuleAdd
   Description: Add a rule for a specific subscriber
   OperationID: RuleAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RuleAdd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/RuleAdd", {
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
   Summary: Invoke method RuleRemove
   Description: Remove a rule from a specific subscriber
   OperationID: RuleRemove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleRemove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleRemove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RuleRemove(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/RuleRemove", {
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
   Summary: Invoke method RuleUpdate
   Description: Update a rule
   OperationID: RuleUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RuleUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/RuleUpdate", {
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
   Summary: Invoke method RulesList
   Description: List out all the rules for a specific subscriber
   OperationID: RulesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RulesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RulesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RulesList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/RulesList", {
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
   Summary: Invoke method RuleTableList
   Description: List tables that have been enabled for CDC and can be used for rules
   OperationID: RuleTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RuleTableList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/RuleTableList", {
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
   Summary: Invoke method GenerateSampleData
   Description: Generate sample data for a given table
   OperationID: GenerateSampleData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSampleData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSampleData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateSampleData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GenerateSampleData", {
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
   Summary: Invoke method GenerateLookupSampleData
   Description: Generate sample data for the lookups on a given table
   OperationID: GenerateLookupSampleData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateLookupSampleData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateLookupSampleData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateLookupSampleData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GenerateLookupSampleData", {
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
   Summary: Invoke method GenerateKeyTags
   Description: Generate Tags based on the primary key columns
   OperationID: GenerateKeyTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateKeyTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateKeyTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateKeyTags(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GenerateKeyTags", {
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
   Summary: Invoke method GetLookupLinks
   Description: Get look up links available for a specific table
   OperationID: GetLookupLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLookupLinks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupLinks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLookupLinks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GetLookupLinks", {
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
   Summary: Invoke method GetLookupDataFields
   Description: Get data fields for a specific look up on a table
   OperationID: GetLookupDataFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLookupDataFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupDataFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLookupDataFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GetLookupDataFields", {
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
   Summary: Invoke method GetCollaborateUserDefinedRuleSecurityCodes
   Description: Get User Defined Security Code for Collaborate Notification rules
   OperationID: GetCollaborateUserDefinedRuleSecurityCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GetCollaborateUserDefinedRuleSecurityCodes", {
          method: 'post',
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
   Summary: Invoke method GetCollaborateSecurityCodes
   Description: Get All Security Code for Collaborate Notification rules
   OperationID: GetCollaborateSecurityCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GetCollaborateSecurityCodes", {
          method: 'post',
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
   Summary: Invoke method GetSecurityAccessForUsers
   Description: Return the list of users and their accessible security codes
   OperationID: GetSecurityAccessForUsers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSecurityAccessForUsers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSecurityAccessForUsers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSecurityAccessForUsers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GetSecurityAccessForUsers", {
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
   Summary: Invoke method GetCollaborateSecurityCodeAccessRights
   Description: Get Access status for current user for the collaborate security codes
   OperationID: GetCollaborateSecurityCodeAccessRights
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GetCollaborateSecurityCodeAccessRights", {
          method: 'post',
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
   Summary: Invoke method GetCollaborateSecurityCodeAccessStatus
   Description: Check the access status for the current user for the given security code
   OperationID: GetCollaborateSecurityCodeAccessStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCollaborateSecurityCodeAccessStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateSecurityCodeAccessStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCollaborateSecurityCodeAccessStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GetCollaborateSecurityCodeAccessStatus", {
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
   Summary: Invoke method GetCollaborateSecurityCodeUserAccessStatus
   Description: Check the access status for a user for the given security code
   OperationID: GetCollaborateSecurityCodeUserAccessStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCollaborateSecurityCodeUserAccessStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCollaborateSecurityCodeUserAccessStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCollaborateSecurityCodeUserAccessStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/GetCollaborateSecurityCodeUserAccessStatus", {
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
   Summary: Invoke method CreateCollaborateUserDefinedRuleSecurityCode
   Description: Create User Defined Security Code for Collaborate Notification rules
   OperationID: CreateCollaborateUserDefinedRuleSecurityCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateCollaborateUserDefinedRuleSecurityCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateCollaborateUserDefinedRuleSecurityCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateCollaborateUserDefinedRuleSecurityCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.CdcManageSvc/CreateCollaborateUserDefinedRuleSecurityCode", {
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
      @param catgory
   */  
export interface CreateCollaborateUserDefinedRuleSecurityCode_input{
   catgory:string,
}

export interface CreateCollaborateUserDefinedRuleSecurityCode_output{
   returnObj:string,
}

   /** Required : 
      @param tables
   */  
export interface DisableCapture_input{
      /**  Schema and table name  */  
   tables:string,
}

export interface DisableCapture_output{
}

   /** Required : 
      @param tables
   */  
export interface EnableCapture_input{
      /**  Schema and table name  */  
   tables:string,
}

export interface EnableCapture_output{
}

export interface GenerateAvailableTables_output{
}

   /** Required : 
      @param schemaName
      @param tableName
   */  
export interface GenerateKeyTags_input{
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
      @param schemaName
      @param tableName
      @param lookupIDs
   */  
export interface GenerateLookupSampleData_input{
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
      @param schemaName
      @param tableName
   */  
export interface GenerateSampleData_input{
      /**  Schema name  */  
   schemaName:string,
      /**  Table name  */  
   tableName:string,
}

export interface GenerateSampleData_output{
      /**  Sample data for table  */  
   returnObj:any,      //schema had no properties on an object.
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

   /** Required : 
      @param schemaName
      @param tableName
      @param lookupID
   */  
export interface GetLookupDataFields_input{
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
      @param schemaName
      @param tableName
   */  
export interface GetLookupLinks_input{
      /**  Schema  */  
   schemaName:string,
      /**  Table  */  
   tableName:string,
}

export interface GetLookupLinks_output{
      /**  List of lookup links  */  
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

export interface Ice_Tablesets_CdcCaptureStatusRow{
   SchemaName:string,
   TableName:string,
   CaptureEnabled:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_CdcCaptureStatusTableset{
   CdcCaptureStatus:Ice_Tablesets_CdcCaptureStatusRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_CdcSubscriberRow{
   SubscriberID:string,
   Description:string,
      /**  Subscribers read mode, options are push, push-pull or pull  */  
   SubscriberMode:string,
   Inactive:boolean,
   MarkDeletion:boolean,
   Offset:number,
   PageSize:number,
   LastPush:string,
   LastPushAttempt:string,
   LastPull:string,
      /**  Number of push attempts made without success  */  
   PushAttempts:number,
      /**  Duration (in seconds) that read messages are kept for the subscriber  */  
   TTLRead:number,
      /**  Duration (in seconds) that unread messages are kept for the subscriber  */  
   TTLUnread:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
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

export interface Ice_Tablesets_CdcSubscriberTableset{
   CdcSubscriber:Ice_Tablesets_CdcSubscriberRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param schemaName
      @param tableName
      @param status
      @param skip
      @param pageSize
   */  
export interface ListCaptureStatus_input{
      /**  Schema Name  */  
   schemaName:string,
      /**  Table to search for  */  
   tableName:string,
      /**  Status 0 = All, 1 = Enabled, 2 = Disabled  */  
   status:number,
      /**  Skip n results  */  
   skip:number,
      /**  Page size, maximum 200  */  
   pageSize:number,
}

export interface ListCaptureStatus_output{
   returnObj:Ice_Tablesets_CdcCaptureStatusTableset[],
parameters : {
      /**  output parameters  */  
   pageSize:number,
   morePages:boolean,
   total:number,
}
}

   /** Required : 
      @param subscriberID
   */  
export interface RegenerateSecret_input{
      /**  Subscriber ID  */  
   subscriberID:string,
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
      @param webHookSecret
   */  
export interface Register_input{
      /**  Description of Subscriber  */  
   description:string,
      /**  Subscriber Mode - "PUSH", "PUSHPULL" or "PULL"  */  
   mode:string,
      /**  Web Hook URI for Push or Push-Pull  */  
   webHookURI:string,
      /**  Web Hook Secret for Push or Push-Pull  */  
   webHookSecret:string,
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
      /**  Security Code  */  
   secCode:string,
}

export interface RuleAdd_output{
}

   /** Required : 
      @param subscriberID
      @param companyID
      @param ruleID
   */  
export interface RuleGet_input{
   subscriberID:string,
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
      @param companyID
      @param ruleID
   */  
export interface RuleRemove_input{
      /**  Subscriber ID  */  
   subscriberID:string,
      /**  Company the rule belongs to  */  
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
   returnObj:array
}

   /** Required : 
      @param subscriberID
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
      /**  Company the rule is assigned to  */  
   companyID:string,
      /**  ID of rule being updated  */  
   ruleID:string,
      /**  Description of rule  */  
   description:string,
      /**  Change type rule applies to, valid options are insert, update and delete  */  
   changeType:string,
      /**  Rule JSON logic, passing null will ignore column from updating  */  
   rule:string,
      /**  Metadata JSON logic output  */  
   metadataRule:string,
      /**  Look up links  */  
   lookupLinks:string,
      /**  Set the rule to active/inactive  */  
   inactive:boolean,
      /**  Security Code  */  
   secCode:string,
}

export interface RuleUpdate_output{
}

   /** Required : 
      @param subscriberID
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
   */  
export interface SubscriberGet_input{
      /**  Subscriber ID  */  
   subscriberID:string,
}

export interface SubscriberGet_output{
   returnObj:Ice_Tablesets_CdcSubscriberTableset[],
}

   /** Required : 
      @param subscriberID
      @param description
      @param inactive
      @param webHookURI
      @param webHookSecret
      @param pageSize
      @param TTLRead
      @param TTLUnread
   */  
export interface SubscriberUpdate_input{
      /**  Subscriber ID  */  
   subscriberID:string,
      /**  New description  */  
   description:string,
      /**  Set subscriber to inactive  */  
   inactive:boolean,
      /**  Web Hook URI, only valid for Push or Push-Pull  */  
   webHookURI:string,
      /**  Web Hook Secret, only valid for Push or Push-Pull  */  
   webHookSecret:string,
      /**  Page size for messages are pushed/pulled  */  
   pageSize:number,
      /**  How long to keep read messages, in seconds  */  
   TTLRead:number,
      /**  How long to keep unread messages, in seconds  */  
   TTLUnread:number,
}

export interface SubscriberUpdate_output{
}

export interface SubscribersList_output{
   returnObj:Ice_Tablesets_CdcSubscriberTableset[],
}

   /** Required : 
      @param subscriberID
   */  
export interface Unregister_input{
      /**  Subscriber ID  */  
   subscriberID:string,
}

export interface Unregister_output{
}

