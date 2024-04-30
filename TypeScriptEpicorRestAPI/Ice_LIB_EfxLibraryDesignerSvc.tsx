import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.LIB.EfxLibraryDesignerSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/$metadata", {
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
   Summary: Invoke method ApplyChanges
   OperationID: ApplyChanges
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ApplyChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApplyChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApplyChanges(requestBody:ApplyChanges_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ApplyChanges_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/ApplyChanges", {
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
         resolve(data as ApplyChanges_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ApplyChangesWithDiagnostics
   OperationID: ApplyChangesWithDiagnostics
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ApplyChangesWithDiagnostics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApplyChangesWithDiagnostics_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ApplyChangesWithDiagnostics(requestBody:ApplyChangesWithDiagnostics_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ApplyChangesWithDiagnostics_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/ApplyChangesWithDiagnostics", {
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
         resolve(data as ApplyChangesWithDiagnostics_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOwner
   Description: Changes ownership of specified library to specified user
   OperationID: ChangeOwner
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOwner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOwner_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOwner(requestBody:ChangeOwner_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOwner_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/ChangeOwner", {
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
         resolve(data as ChangeOwner_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaults
   OperationID: GetDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaults(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/GetDefaults", {
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
         resolve(data as GetDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFunctionInfo
   OperationID: GetFunctionInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFunctionInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFunctionInfo(requestBody:GetFunctionInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFunctionInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/GetFunctionInfo", {
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
         resolve(data as GetFunctionInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFunctionList
   OperationID: GetFunctionList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFunctionList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFunctionList(requestBody:GetFunctionList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFunctionList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/GetFunctionList", {
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
         resolve(data as GetFunctionList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFunctionList2
   Description: Kinetic REST params do not support FunctionSearchOptions.
   OperationID: GetFunctionList2
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFunctionList2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionList2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFunctionList2(requestBody:GetFunctionList2_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFunctionList2_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/GetFunctionList2", {
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
         resolve(data as GetFunctionList2_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLibraryInfo
   OperationID: GetLibraryInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLibraryInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLibraryInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLibraryInfo(requestBody:GetLibraryInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLibraryInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/GetLibraryInfo", {
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
         resolve(data as GetLibraryInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLibraryList
   Description: Gets a list of libraries.
   OperationID: GetLibraryList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLibraryList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLibraryList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLibraryList(requestBody:GetLibraryList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLibraryList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/GetLibraryList", {
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
         resolve(data as GetLibraryList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLibraryList2
   Description: Gets a list of libraries.
   OperationID: GetLibraryList2
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLibraryList2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLibraryList2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLibraryList2(requestBody:GetLibraryList2_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLibraryList2_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/GetLibraryList2", {
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
         resolve(data as GetLibraryList2_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLibrary
   Description: Finds a library by its ID.
   OperationID: GetLibrary
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLibrary(requestBody:GetLibrary_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLibrary_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/GetLibrary", {
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
         resolve(data as GetLibrary_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLibraries
   Description: Gets a list of libraries.
   OperationID: GetLibraries
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLibraries_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLibraries_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLibraries(requestBody:GetLibraries_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLibraries_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/GetLibraries", {
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
         resolve(data as GetLibraries_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DetectCircularReferences
   Description: Method returns true first found circular reference path for the specified library configuration if any.
Otherwise, it returns an empty array.
   OperationID: DetectCircularReferences
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DetectCircularReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DetectCircularReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DetectCircularReferences(requestBody:DetectCircularReferences_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DetectCircularReferences_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/DetectCircularReferences", {
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
         resolve(data as DetectCircularReferences_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockLibrary
   Description: Locks a library.
   OperationID: LockLibrary
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LockLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockLibrary(requestBody:LockLibrary_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LockLibrary_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/LockLibrary", {
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
         resolve(data as LockLibrary_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReleaseLibrary
   Description: Releases a library.
   OperationID: ReleaseLibrary
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReleaseLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReleaseLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReleaseLibrary(requestBody:ReleaseLibrary_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReleaseLibrary_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/ReleaseLibrary", {
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
         resolve(data as ReleaseLibrary_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PromoteToProduction
   Description: Promote specified library to production
   OperationID: PromoteToProduction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PromoteToProduction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PromoteToProduction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PromoteToProduction(requestBody:PromoteToProduction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PromoteToProduction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/PromoteToProduction", {
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
         resolve(data as PromoteToProduction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DemoteFromProduction
   Description: Demote the specified library from production to staging
   OperationID: DemoteFromProduction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DemoteFromProduction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DemoteFromProduction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DemoteFromProduction(requestBody:DemoteFromProduction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DemoteFromProduction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/DemoteFromProduction", {
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
         resolve(data as DemoteFromProduction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RegenerateLibrary
   OperationID: RegenerateLibrary
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RegenerateLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenerateLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RegenerateLibrary(requestBody:RegenerateLibrary_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RegenerateLibrary_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/RegenerateLibrary", {
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
         resolve(data as RegenerateLibrary_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RegenerateAllLibraries
   OperationID: RegenerateAllLibraries
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenerateAllLibraries_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RegenerateAllLibraries(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RegenerateAllLibraries_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/RegenerateAllLibraries", {
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
         resolve(data as RegenerateAllLibraries_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportLibrary
   Description: Exports the specified library.
   OperationID: ExportLibrary
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportLibrary(requestBody:ExportLibrary_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportLibrary_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/ExportLibrary", {
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
         resolve(data as ExportLibrary_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportLibrary
   Description: Imports the provided library.
   OperationID: ImportLibrary
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportLibrary(requestBody:ImportLibrary_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportLibrary_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/ImportLibrary", {
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
         resolve(data as ImportLibrary_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InstallLibrary
   OperationID: InstallLibrary
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InstallLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InstallLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InstallLibrary(requestBody:InstallLibrary_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InstallLibrary_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/InstallLibrary", {
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
         resolve(data as InstallLibrary_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UninstallLibrary
   Description: Removes previously installed library.
   OperationID: UninstallLibrary
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UninstallLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UninstallLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UninstallLibrary(requestBody:UninstallLibrary_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UninstallLibrary_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/UninstallLibrary", {
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
         resolve(data as UninstallLibrary_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DetermineInstallationOrder
   Description: Tries to order specified library Id from most independent to most dependent.
   OperationID: DetermineInstallationOrder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DetermineInstallationOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DetermineInstallationOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DetermineInstallationOrder(requestBody:DetermineInstallationOrder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DetermineInstallationOrder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.EfxLibraryDesignerSvc/DetermineInstallationOrder", {
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
         resolve(data as DetermineInstallationOrder_output)
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
      @param libraryTableset
   */  
export interface ApplyChangesWithDiagnostics_input{
   libraryTableset:Ice_Tablesets_EfxLibraryTableset[],
}

export interface ApplyChangesWithDiagnostics_output{
parameters : {
      /**  output parameters  */  
   libraryTableset:Ice_Tablesets_EfxLibraryTableset,
   diagnostics:any[],
}
}

   /** Required : 
      @param input
   */  
export interface ApplyChanges_input{
   input:Ice_Tablesets_EfxLibraryTableset[],
}

export interface ApplyChanges_output{
parameters : {
      /**  output parameters  */  
   input:Ice_Tablesets_EfxLibraryTableset,
}
}

   /** Required : 
      @param libraryId
      @param userId
   */  
export interface ChangeOwner_input{
   libraryId:string,
   userId:string,
}

export interface ChangeOwner_output{
}

   /** Required : 
      @param libraryID
   */  
export interface DemoteFromProduction_input{
   libraryID:string,
}

export interface DemoteFromProduction_output{
}

   /** Required : 
      @param libraryId
      @param referencedLibraries
   */  
export interface DetectCircularReferences_input{
   libraryId:string,
   referencedLibraries:string,
}

export interface DetectCircularReferences_output{
   returnObj:string,
}

   /** Required : 
      @param libraryIds
   */  
export interface DetermineInstallationOrder_input{
   libraryIds:string,
}

export interface DetermineInstallationOrder_output{
      /**  List of library Ids in the order of installation  */  
   returnObj:string,
}

   /** Required : 
      @param libraryID
      @param options
   */  
export interface ExportLibrary_input{
      /**  The identifier of the library to export.  */  
   libraryID:string,
   options:Ice_Lib_EfxLibraryDesigner_ExportOptions[],
}

export interface ExportLibrary_output{
      /**  The binary representation of the library.  */  
   returnObj:string,
}

export interface GetDefaults_output{
   returnObj:Ice_Tablesets_EfxLibraryTableset[],
}

   /** Required : 
      @param options
   */  
export interface GetFunctionInfo_input{
   options:Ice_Lib_EfxLibraryDesigner_FunctionInfoSearchOptions[],
}

export interface GetFunctionInfo_output{
   returnObj:Ice_Lib_EfxLibraryDesigner_FunctionInfoDto[],
}

   /** Required : 
      @param libraryID
      @param kind
      @param functionIDStartsWith
   */  
export interface GetFunctionList2_input{
   libraryID:string,
   kind:number,
   functionIDStartsWith:string,
}

export interface GetFunctionList2_output{
   returnObj:Ice_Tablesets_EfxFunctionSearchTableset[],
}

   /** Required : 
      @param options
   */  
export interface GetFunctionList_input{
   options:Ice_Lib_EfxLibraryDesigner_FunctionSearchOptions[],
}

export interface GetFunctionList_output{
   returnObj:Ice_Tablesets_EfxFunctionSearchTableset[],
}

   /** Required : 
      @param libraryIds
   */  
export interface GetLibraries_input{
      /**  the array of library ID's.  */  
   libraryIds:string,
}

export interface GetLibraries_output{
   returnObj:Ice_Tablesets_EfxLibraryTableset[],
}

   /** Required : 
      @param options
   */  
export interface GetLibraryInfo_input{
   options:Ice_Lib_EfxLibraryDesigner_LibraryInfoSearchOptions[],
}

export interface GetLibraryInfo_output{
   returnObj:Ice_Lib_EfxLibraryDesigner_LibraryInfoDto[],
}

   /** Required : 
      @param startsWith
      @param kind
      @param rollOutMode
      @param status
   */  
export interface GetLibraryList2_input{
      /**  library ID starts with  */  
   startsWith:string,
      /**  library kind.  */  
   kind:number,
      /**  the rollout mode.  */  
   rollOutMode:number,
      /**  library status.  */  
   status:number,
}

export interface GetLibraryList2_output{
   returnObj:Ice_Tablesets_EfxLibrarySearchTableset[],
}

   /** Required : 
      @param options
   */  
export interface GetLibraryList_input{
   options:Ice_Lib_EfxLibraryDesigner_LibrarySearchOptions[],
}

export interface GetLibraryList_output{
   returnObj:Ice_Tablesets_EfxLibrarySearchTableset[],
}

   /** Required : 
      @param libraryId
   */  
export interface GetLibrary_input{
      /**  the library ID.  */  
   libraryId:string,
}

export interface GetLibrary_output{
   returnObj:Ice_Tablesets_EfxLibraryTableset[],
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface Ice_Lib_EfxLibraryDesigner_ExportOptions{
   Mode:number,
   Format:number,
   Package:string,
   PackageVersion:string,
   Publisher:string,
   InstallAsHidden:boolean,
}

export interface Ice_Lib_EfxLibraryDesigner_FunctionInfoDto{
   LibraryId:string,
   FunctionId:string,
   Disabled:boolean,
   SignatureData:Ice_Lib_EfxLibraryDesigner_FunctionSignatureItem[],
   Description:string,
   Kind:number,
}

export interface Ice_Lib_EfxLibraryDesigner_FunctionInfoSearchOptions{
   kind:number,
   libraryId:string,
   functionId:string,
}

export interface Ice_Lib_EfxLibraryDesigner_FunctionSearchOptions{
   kind:number,
   libraryID:string,
   functionIDStartsWith:string,
}

export interface Ice_Lib_EfxLibraryDesigner_FunctionSignatureItem{
   Response:boolean,
   ParameterID:number,
   ArgumentName:string,
   Order:number,
   DataType:string,
   DataTypeInfo:string,
}

export interface Ice_Lib_EfxLibraryDesigner_ImportOptions{
   NewLibraryId:string,
   OverwriteMode:number,
}

export interface Ice_Lib_EfxLibraryDesigner_InstallOptions{
   AllowUpgrade:boolean,
   EnableIn:number,
}

export interface Ice_Lib_EfxLibraryDesigner_LibraryInfoDto{
   LibraryId:string,
   Disabled:boolean,
   Functions:Ice_Lib_EfxLibraryDesigner_FunctionInfoDto[],
}

export interface Ice_Lib_EfxLibraryDesigner_LibraryInfoSearchOptions{
   libraryId:string,
}

export interface Ice_Lib_EfxLibraryDesigner_LibrarySearchOptions{
   kind:number,
   startsWith:string,
   rollOutMode:number,
   status:number,
}

export interface Ice_Tablesets_EfxFunctionListRow{
   LibraryID:string,
   FunctionID:string,
      /**  Short function description  */  
   Description:string,
      /**  Type of function: widget-based, widget-based with custom code, code-based  */  
   Kind:number,
      /**  Flag determines the ability to expose the library as a REST endpoint. If column value is false, then library can be used via REST, otherwise not.  */  
   Private:boolean,
      /**  Function activity status  */  
   Disabled:boolean,
      /**  Flags determines whether stored function valid or not  */  
   Invalid:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EfxFunctionRow{
   LibraryID:string,
      /**  Function ID  */  
   FunctionID:string,
      /**  Short function description  */  
   Description:string,
      /**  Type of function: widget-based, widget-based with custom code, code-based  */  
   Kind:number,
      /**  Flag determines whether the function requires transaction or not  */  
   RequireTransaction:boolean,
      /**  Flag allows enabling the legacy single dirty row mode  */  
   SingleRowMode:boolean,
      /**  Flag determines the ability to expose the library as a REST endpoint. If column value is false, then library can be used via REST, otherwise not.  */  
   Private:boolean,
      /**  Function activity status  */  
   Disabled:boolean,
      /**  Flags determines whether stored function valid or not  */  
   Invalid:boolean,
      /**  Preview of widget-based function  */  
   Thumbnail:string,
      /**  Serialized function's body  */  
   Body:string,
      /**  Function-level notes  */  
   Notes:string,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EfxFunctionSearchTableset{
   EfxFunctionList:Ice_Tablesets_EfxFunctionListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_EfxFunctionSignatureRow{
   LibraryID:string,
   FunctionID:string,
      /**  Flag determines kind of parameter: request or response  */  
   Response:boolean,
      /**  Internal parameter id (part of PK)  */  
   ParameterID:number,
   ArgumentName:string,
   Order:number,
      /**  Full qualified .NET type name  */  
   DataType:string,
      /**  Additional data type information  */  
   DataTypeInfo:string,
      /**  Flag determines whether a parameter is mandatory or can be omitte  */  
   Optional:boolean,
   DefaultValue:string,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EfxLibraryListRow{
   LibraryID:string,
      /**  Short library description  */  
   Description:string,
      /**  Flag determines is library published for the production or is in staging mode  */  
   Published:boolean,
      /**  Flag determines the ability to expose the library as a REST endpoint. If column value is false, then library can be used via REST, otherwise not.  */  
   Private:boolean,
      /**  Company where the library was created or imported  */  
   OwnedByCompany:string,
      /**  Library activity status  */  
   Disabled:boolean,
      /**  Library cannot be edit by the current user  */  
   ReadOnly:boolean,
      /**  Library exlusively locked by the user  */  
   LockedBy:string,
   SysRowID:string,
      /**  Installation mode  */  
   Mode:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EfxLibraryMappingRow{
   LibraryID:string,
   Company:string,
   Allowed:boolean,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EfxLibraryRow{
      /**  Unique user-friendly Library Identifier  */  
   LibraryID:string,
      /**  Original library ID specified during development  */  
   OriginalID:string,
      /**  Short description of library  */  
   Description:string,
      /**  Internal unique library reference ID  */  
   GlobalID:string,
      /**  Version of a product used to build library  */  
   EpicorVersion:string,
      /**  Library version  */  
   Revision:number,
      /**  Flag determines is library published for the production or is in staging mode  */  
   Published:boolean,
      /**  Flag determines the ability to expose the library as a REST endpoint. If column value is false, then library can be used via REST, otherwise not.  */  
   Private:boolean,
      /**  Library activity status  */  
   Disabled:boolean,
      /**  Installation mode  */  
   Mode:number,
      /**  Flag determining the ability to change the library  */  
   Frozen:boolean,
      /**  Flag determining the ability to add widget-based functions with custom code elements  */  
   AllowCustomCodeWidgets:boolean,
      /**  Flag determining the ability to add custom code-base functions  */  
   AllowCustomCodeFunctions:boolean,
      /**  Allowed direct DB access mode in C# code: node, read-only, and read-write  */  
   DirectDBAccess:number,
      /**  Company where the library was created or imported  */  
   OwnedByCompany:string,
      /**  Library maintainer's ID  */  
   Owner:string,
      /**  Library maintainers group  */  
   SharedWithGroup:string,
      /**  Library-levele notes  */  
   Notes:string,
      /**  Library is part of this project  */  
   Package:string,
      /**  Version of packge containing the library  */  
   PackageVersion:string,
      /**  Library provided by the publisher  */  
   Publisher:string,
      /**  Row version column  */  
   SysRevID:number,
   SysRowID:string,
      /**  Enables (true) or disables (false) the debug mode of EFx library build  */  
   DebugMode:boolean,
      /**  Enables (true) or disables (false) the storing of the generated sources of an EFx library on the server  */  
   DumpSources:boolean,
      /**  Enables (true) or disables (false) advanced tracing for an EFx library  */  
   AdvTracing:boolean,
      /**  Library exlusively locked by the user  */  
   LockedBy:string,
   LockedOn:string,
      /**  Library locked for edit from the specific workstation  */  
   LockedFrom:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EfxLibrarySearchTableset{
   EfxLibraryList:Ice_Tablesets_EfxLibraryListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_EfxLibraryTableset{
   EfxLibrary:Ice_Tablesets_EfxLibraryRow[],
   EfxFunction:Ice_Tablesets_EfxFunctionRow[],
   EfxFunctionSignature:Ice_Tablesets_EfxFunctionSignatureRow[],
   EfxLibraryMapping:Ice_Tablesets_EfxLibraryMappingRow[],
   EfxRefAssembly:Ice_Tablesets_EfxRefAssemblyRow[],
   EfxRefLibrary:Ice_Tablesets_EfxRefLibraryRow[],
   EfxRefService:Ice_Tablesets_EfxRefServiceRow[],
   EfxRefTable:Ice_Tablesets_EfxRefTableRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_EfxRefAssemblyRow{
      /**  Library ID  */  
   LibraryID:string,
   Assembly:string,
   SysRevID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EfxRefLibraryRow{
      /**  Id of the current library  */  
   LibraryID:string,
      /**  Id of a referenced library  */  
   LibraryRef:string,
   SysRevID:number,
   SysRowID:string,
      /**  Refernced library mode (0  -Normal, 1 - ReadOnly (Installed), 2 - Hidden (Installed as Hidden))  */  
   Mode:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EfxRefServiceRow{
      /**  Library ID  */  
   LibraryID:string,
      /**  Epicor Service ID  */  
   ServiceID:string,
   SysRevID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_EfxRefTableRow{
      /**  Library ID  */  
   LibraryID:string,
      /**  DB Table ID  */  
   TableID:string,
   Updatable:boolean,
   SysRevID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param libraryPackage
      @param options
   */  
export interface ImportLibrary_input{
      /**  The binary representation of the library.  */  
   libraryPackage:string,
   options:Ice_Lib_EfxLibraryDesigner_ImportOptions[],
}

export interface ImportLibrary_output{
   returnObj:Ice_BOUpdErrorTableset[],
}

   /** Required : 
      @param libraryPackage
      @param options
   */  
export interface InstallLibrary_input{
   libraryPackage:string,
   options:Ice_Lib_EfxLibraryDesigner_InstallOptions[],
}

export interface InstallLibrary_output{
   returnObj:Ice_BOUpdErrorTableset[],
}

   /** Required : 
      @param libraryID
   */  
export interface LockLibrary_input{
   libraryID:string,
}

export interface LockLibrary_output{
}

   /** Required : 
      @param libraryID
   */  
export interface PromoteToProduction_input{
   libraryID:string,
}

export interface PromoteToProduction_output{
}

export interface RegenerateAllLibraries_output{
   returnObj:Ice_BOUpdErrorTableset[],
}

   /** Required : 
      @param libraryID
   */  
export interface RegenerateLibrary_input{
   libraryID:string,
}

export interface RegenerateLibrary_output{
   returnObj:Ice_BOUpdErrorTableset[],
}

   /** Required : 
      @param libraryID
   */  
export interface ReleaseLibrary_input{
   libraryID:string,
}

export interface ReleaseLibrary_output{
}

   /** Required : 
      @param libraryId
   */  
export interface UninstallLibrary_input{
   libraryId:string,
}

export interface UninstallLibrary_output{
   returnObj:Ice_BOUpdErrorTableset[],
}

