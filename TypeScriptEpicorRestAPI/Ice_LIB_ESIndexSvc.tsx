import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.ESIndexSvc
// Description: ESIndex service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/$metadata", {
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
   Summary: Invoke method CreateIndex
   Description: Creates an index in Enterprise Search.
   OperationID: CreateIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateIndex(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/CreateIndex", {
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
   Summary: Invoke method ModifyIndex
   Description: Modifies an existing index in Enterprise Search.
   OperationID: ModifyIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifyIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifyIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ModifyIndex(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/ModifyIndex", {
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
   Summary: Invoke method BuildIndex
   Description: Builds an index in Enterprise Search.
   OperationID: BuildIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildIndex(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/BuildIndex", {
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
   Summary: Invoke method DeleteIndex
   Description: Deletes an index from Enterprise Search.
   OperationID: DeleteIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteIndex(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/DeleteIndex", {
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
   Summary: Invoke method GetIndex
   Description: Gets the index details with the indexed BAQ's from Enterprise Search.
<param name="indexName">index name.</param>
   OperationID: GetIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIndex(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/GetIndex", {
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
   Summary: Invoke method GetBuildLog
   Description: Gets a build log by its id.
   OperationID: GetBuildLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBuildLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBuildLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBuildLog(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/GetBuildLog", {
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
   Summary: Invoke method WriteBuildLogToFile
   Description: Gets the build log by its id from Enterprise Search service and saves it in User data shared folder.
The file name is the build log id with .log extension.
   OperationID: WriteBuildLogToFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WriteBuildLogToFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WriteBuildLogToFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WriteBuildLogToFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/WriteBuildLogToFile", {
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
   Summary: Invoke method GetBuildHistory
   Description: Gets a list of the builds per index.
   OperationID: GetBuildHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBuildHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBuildHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBuildHistory(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/GetBuildHistory", {
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
   Summary: Invoke method GetAllIndexes
   Description: Gets a list of available indexes in Enterprise Search.
   OperationID: GetAllIndexes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllIndexes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllIndexes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/GetAllIndexes", {
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
   Summary: Invoke method GetTemplates
   Description: Gets a list of available templates in Enterprise Search.
   OperationID: GetTemplates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTemplates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTemplates(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/GetTemplates", {
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
   Summary: Invoke method GetAvailableCompanies
   Description: Gets a list of available companies.
   OperationID: GetAvailableCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableCompanies_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableCompanies(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/GetAvailableCompanies", {
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
   Summary: Invoke method GetSearchableBaqs
   Description: Gets a list of shared BAQ's that are NOT cross-company.
   OperationID: GetSearchableBaqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSearchableBaqs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSearchableBaqs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSearchableBaqs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/GetSearchableBaqs", {
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
   Summary: Invoke method GetLikeLinks
   Description: Gets a list of like links.
   OperationID: GetLikeLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLikeLinks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLikeLinks(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/GetLikeLinks", {
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
   Summary: Invoke method RefreshBaqs
   Description: Refreshes the list of BAQ's.
   OperationID: RefreshBaqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshBaqs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshBaqs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshBaqs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/RefreshBaqs", {
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
   Summary: Invoke method RefreshBaqList
   Description: Refreshes the list of BAQ's.
   OperationID: RefreshBaqList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshBaqList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshBaqList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshBaqList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/RefreshBaqList", {
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
   Summary: Invoke method ValidateBaq
   Description: Validates the list of BAQ's.
   OperationID: ValidateBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBaq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/ValidateBaq", {
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
   Summary: Invoke method ValidateAllBaqs
   Description: Validates all the BAQ's in an index.
   OperationID: ValidateAllBaqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAllBaqs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAllBaqs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateAllBaqs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/ValidateAllBaqs", {
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
   Summary: Invoke method DeleteBaq
   Description: Deletes a BAQ from the list of indexed BAQ's in Enterprise Search.
   OperationID: DeleteBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteBaq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/DeleteBaq", {
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
   Summary: Invoke method AddBaq
   Description: Adds a BAQ to the list of indexed BAQ's in Enterprise Search.
   OperationID: AddBaq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddBaq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddBaq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/AddBaq", {
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
   Summary: Invoke method GetBaqTuning
   Description: Gets the BAQ tuning settings.
   OperationID: GetBaqTuning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBaqTuning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBaqTuning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBaqTuning(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/GetBaqTuning", {
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
   Summary: Invoke method UpdateBaqTuning
   Description: Updates the BAQ tuning settings.
   OperationID: UpdateBaqTuning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateBaqTuning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBaqTuning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateBaqTuning(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/UpdateBaqTuning", {
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
   Summary: Invoke method RunBAQValidation
   Description: Validates a BAQ.
   OperationID: RunBAQValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunBAQValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunBAQValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunBAQValidation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/RunBAQValidation", {
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
   Summary: Invoke method RunAllBAQValidations
   Description: Validates all the BAQ's in an index.
   OperationID: RunAllBAQValidations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunAllBAQValidations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunAllBAQValidations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunAllBAQValidations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/RunAllBAQValidations", {
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
   Summary: Invoke method Update
   Description: Adds and updates any modified rows (ESIndex and ESIndexBAQ tables).
ESIndexBAQField can't have fields added (it comes from the BAQ definition).
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/Update", {
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
   Summary: Invoke method AssertUserCanAccess
   Description: Checks if the user can access ESIndex methods.
   OperationID: AssertUserCanAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssertUserCanAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssertUserCanAccess(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ESIndexSvc/AssertUserCanAccess", {
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



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param indexName
      @param queryId
      @param company
   */  
export interface AddBaq_input{
      /**  index name.  */  
   indexName:string,
      /**  query Id.  */  
   queryId:string,
      /**  company.  */  
   company:string,
}

export interface AddBaq_output{
}

export interface AssertUserCanAccess_output{
}

   /** Required : 
      @param indexName
   */  
export interface BuildIndex_input{
      /**  index name.  */  
   indexName:string,
}

export interface BuildIndex_output{
   returnObj:string,
}

   /** Required : 
      @param indexTableset
   */  
export interface CreateIndex_input{
   indexTableset:Ice_Tablesets_ESIndexTableset[],
}

export interface CreateIndex_output{
}

   /** Required : 
      @param indexName
      @param queryId
   */  
export interface DeleteBaq_input{
      /**  index name.  */  
   indexName:string,
      /**  query Id.  */  
   queryId:string,
}

export interface DeleteBaq_output{
}

   /** Required : 
      @param indexName
   */  
export interface DeleteIndex_input{
      /**  index name.  */  
   indexName:string,
}

export interface DeleteIndex_output{
}

export interface GetAllIndexes_output{
   returnObj:Ice_Tablesets_ESIndexTableset[],
}

export interface GetAvailableCompanies_output{
   returnObj:string,
}

   /** Required : 
      @param indexTableset
      @param indexName
      @param queryId
   */  
export interface GetBaqTuning_input{
   indexTableset:Ice_Tablesets_ESIndexTableset[],
      /**  the index name.  */  
   indexName:string,
      /**  the query id.  */  
   queryId:string,
}

export interface GetBaqTuning_output{
   returnObj:Ice_Tablesets_ESIndexTableset[],
}

   /** Required : 
      @param indexName
   */  
export interface GetBuildHistory_input{
   indexName:string,
}

export interface GetBuildHistory_output{
   returnObj:Ice_Tablesets_ESIndexTableset[],
}

   /** Required : 
      @param buildLogId
   */  
export interface GetBuildLog_input{
      /**  the build log identifier.  */  
   buildLogId:string,
}

export interface GetBuildLog_output{
   returnObj:string,
}

   /** Required : 
      @param indexName
   */  
export interface GetIndex_input{
   indexName:string,
}

export interface GetIndex_output{
   returnObj:Ice_Tablesets_ESIndexTableset[],
}

export interface GetLikeLinks_output{
   returnObj:string,
}

   /** Required : 
      @param indexName
   */  
export interface GetSearchableBaqs_input{
   indexName:string,
}

export interface GetSearchableBaqs_output{
   returnObj:Ice_Tablesets_ESIndexTableset[],
}

export interface GetTemplates_output{
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

export interface Ice_Lib_ESIndex_Model_SearchIndexBAQ{
   QueryId:string,
}

export interface Ice_Tablesets_ESIndexBAQFieldRow{
      /**  BAQ Field name.  */  
   FieldName:string,
      /**  BAQ Field title position.  */  
   TitlePosition:number,
      /**  BAQ key tag position.  */  
   KeyPosition:number,
      /**  If BAQ Field is included in the index.  */  
   IsIndexed:boolean,
      /**  If BAQ field is shown in search results.  */  
   ShowInThumbnail:boolean,
      /**  If BAQ field should be hidden if it has its default value.  */  
   HideIfDefaultValue:boolean,
      /**  BAQ Field alias.  */  
   Alias:string,
      /**  Search index name.  */  
   SearchIndexName:string,
      /**  Business Activity Query ID.  */  
   QueryID:string,
      /**  If the field is part of the surrogate key.  */  
   IsSurrogateKeyField:boolean,
      /**  Field label.  */  
   FieldLabel:string,
      /**  Field type.  */  
   FieldType:string,
      /**  The field format.  */  
   FieldFormat:string,
      /**  The source database schema name.  */  
   DBSchemaName:string,
      /**  The source database table name.  */  
   DBTableName:string,
      /**  Row unique identifier.  */  
   SysRowID:string,
      /**  Like Field.  */  
   LikeField:string,
      /**  BAQ Like Field.  */  
   SourceLikeField:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ESIndexBAQRow{
      /**  Search index name.  */  
   SearchIndexName:string,
      /**  Business Activity Query ID.  */  
   QueryID:string,
      /**  BAQ Company.  */  
   Company:string,
      /**  BAQ table title template.  */  
   TitleTemplate:string,
      /**  BAQ Table plural description.  */  
   PluralDescription:string,
      /**  BAQ table ranking.  */  
   Ranking:number,
      /**  BAQ primary table.  */  
   PrimaryTable:string,
      /**  BAQ like field.  */  
   LikeField:string,
      /**  BAQ Tags (search keywords).  */  
   Tags:string,
      /**  BAQ display name.  */  
   DisplayName:string,
      /**  BAQ Description.  */  
   QueryDescription:string,
      /**  If it is an external query.  */  
   ExternalQuery:boolean,
      /**  If the query is updatable.  */  
   UpdatableQuery:boolean,
      /**  Query display phrase.  */  
   QueryPhrase:string,
      /**  The tuning file checksum used for concurrency.  */  
   FileChecksum:string,
      /**  Row unique identifier.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ESIndexBAQTableRow{
      /**  The source database table name.  */  
   DBTableName:string,
      /**  The source database schema name.  */  
   DBSchemaName:string,
      /**  If it is a temporary table.  */  
   IsTempTable:boolean,
      /**  If it is a summary table.  */  
   IsSummaryTable:boolean,
      /**  The table name.  */  
   TableName:string,
      /**  Business Activity Query ID.  */  
   QueryID:string,
      /**  Search index name.  */  
   SearchIndexName:string,
      /**  Row unique identifier.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ESIndexLogRow{
      /**  The build ID.  */  
   BuildID:string,
      /**  The build number of crawl records.  */  
   CrawlRecords:number,
      /**  The build number of distinct words.  */  
   DistinctWords:number,
      /**  The build duration.  */  
   TotalDuration:number,
      /**  The build number of errors.  */  
   Exceptions:number,
      /**  The build number of records.  */  
   RecordCount:number,
      /**  Search Index Name in Enterprise Search  */  
   SearchIndexName:string,
      /**  The build start time.  */  
   Start:string,
      /**  Row unique identifier  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ESIndexRow{
      /**  Search Index Name in Enterprise Search  */  
   SearchIndexName:string,
      /**  Template to use for indexing.  */  
   TemplateName:string,
      /**  List of companies to include in the index.  */  
   CompanyList:string,
      /**  Azure Directory ID.  */  
   AzureDirectoryID:string,
      /**  Azure Native App ID.  */  
   AzureNativeAppID:string,
      /**  Azure Web App ID.  */  
   AzureWebAppID:string,
      /**  App server DNS identity.  */  
   DNSIdentity:string,
      /**  Password to connect to app server.  */  
   EpicorPassword:string,
      /**  User to connect to app server.  */  
   EpicorUser:string,
      /**  The app server operation timeout  */  
   OperationTimeout:number,
      /**  If certiicate should be validated when connecting to the app server.  */  
   UseCertificate:boolean,
      /**  App server URL.  */  
   AppServerURL:string,
      /**  Search Index URL.  */  
   SearchURL:string,
      /**  Search index build status.  */  
   Status:string,
      /**  Row unique identifier  */  
   SysRowID:string,
      /**  App server authentication mode.  */  
   AuthenticationMode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ESIndexTableset{
   ESIndex:Ice_Tablesets_ESIndexRow[],
   ESIndexBAQ:Ice_Tablesets_ESIndexBAQRow[],
   ESIndexBAQField:Ice_Tablesets_ESIndexBAQFieldRow[],
   ESIndexBAQTable:Ice_Tablesets_ESIndexBAQTableRow[],
   ESIndexLog:Ice_Tablesets_ESIndexLogRow[],
   SearchableBAQ:Ice_Tablesets_SearchableBAQRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ESIndexValidationTableset{
   ValidationResult:Ice_Tablesets_ValidationResultRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SearchableBAQRow{
      /**  Query ID.  */  
   QueryID:string,
      /**  BAQ Company.  */  
   Company:string,
      /**  BAQ Description.  */  
   Description:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ValidationResultRow{
      /**  Business Activity Query ID.  */  
   QueryID:string,
      /**  Validation rule name.  */  
   ValidationRule:string,
      /**  The result of the validation rule (if it passed).  */  
   Result:boolean,
      /**  In case of failure, the reason or details.  */  
   Details:string,
      /**  SysRowID. Row unique identifier.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param indexTableset
   */  
export interface ModifyIndex_input{
   indexTableset:Ice_Tablesets_ESIndexTableset[],
}

export interface ModifyIndex_output{
}

   /** Required : 
      @param indexName
      @param queriesToRefresh
      @param company
   */  
export interface RefreshBaqList_input{
      /**  index name.  */  
   indexName:string,
      /**  array of BAQ's to refresh  */  
   queriesToRefresh:Ice_Lib_ESIndex_Model_SearchIndexBAQ[],
      /**  company  */  
   company:string,
}

export interface RefreshBaqList_output{
}

   /** Required : 
      @param indexName
      @param queriesToRefresh
      @param company
   */  
export interface RefreshBaqs_input{
      /**  index name.  */  
   indexName:string,
      /**  BAQ's to refresh, or null or empty  */  
   queriesToRefresh:string,
      /**  company  */  
   company:string,
}

export interface RefreshBaqs_output{
}

   /** Required : 
      @param indexName
   */  
export interface RunAllBAQValidations_input{
      /**  index name.  */  
   indexName:string,
}

export interface RunAllBAQValidations_output{
   returnObj:Ice_Tablesets_ESIndexValidationTableset[],
}

   /** Required : 
      @param indexName
      @param queryId
   */  
export interface RunBAQValidation_input{
      /**  index name.  */  
   indexName:string,
      /**  BAQ to validate.  */  
   queryId:string,
}

export interface RunBAQValidation_output{
   returnObj:Ice_Tablesets_ESIndexValidationTableset[],
}

   /** Required : 
      @param indexTableset
      @param queryId
   */  
export interface UpdateBaqTuning_input{
   indexTableset:Ice_Tablesets_ESIndexTableset[],
      /**  query id.  */  
   queryId:string,
}

export interface UpdateBaqTuning_output{
   returnObj:Ice_Tablesets_ESIndexTableset[],
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_ESIndexTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ESIndexTableset[],
}
}

   /** Required : 
      @param indexName
   */  
export interface ValidateAllBaqs_input{
      /**  index name.  */  
   indexName:string,
}

export interface ValidateAllBaqs_output{
      /**  the validation results as XML.  */  
   returnObj:string,
}

   /** Required : 
      @param indexName
      @param queryId
   */  
export interface ValidateBaq_input{
      /**  index name.  */  
   indexName:string,
      /**  BAQ to validate.  */  
   queryId:string,
}

export interface ValidateBaq_output{
      /**  the validation results as XML.  */  
   returnObj:string,
}

   /** Required : 
      @param buildLogId
   */  
export interface WriteBuildLogToFile_input{
      /**  the build log.  */  
   buildLogId:string,
}

export interface WriteBuildLogToFile_output{
}

