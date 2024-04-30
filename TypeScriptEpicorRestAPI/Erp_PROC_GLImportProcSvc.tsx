import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.PROC.GLImportProcSvc
// Description: GL Import process
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", {
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
   Summary: Invoke method GetServerTempPath
   Description: Return Path to upload import file
   OperationID: GetServerTempPath
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetServerTempPath_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetServerTempPath_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetServerTempPath(requestBody:GetServerTempPath_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetServerTempPath_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/GetServerTempPath", {
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
         resolve(data as GetServerTempPath_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeBookID
   Description: Method to call when changing the Book.
   OperationID: ChangeBookID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBookID(requestBody:ChangeBookID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeBookID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/ChangeBookID", {
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
         resolve(data as ChangeBookID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeEntryMode
   Description: Method to call when changing the Entry Mode.
   OperationID: ChangeEntryMode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeEntryMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEntryMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEntryMode(requestBody:ChangeEntryMode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeEntryMode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/ChangeEntryMode", {
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
         resolve(data as ChangeEntryMode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFiscalPeriod
   Description: Method to call when changing the Fiscal Period.
   OperationID: ChangeFiscalPeriod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFiscalPeriod(requestBody:ChangeFiscalPeriod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFiscalPeriod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/ChangeFiscalPeriod", {
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
         resolve(data as ChangeFiscalPeriod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFiscalPeriodType
   Description: Method to call when changing the Fiscal Period Type.
   OperationID: ChangeFiscalPeriodType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFiscalPeriodType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalPeriodType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFiscalPeriodType(requestBody:ChangeFiscalPeriodType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFiscalPeriodType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/ChangeFiscalPeriodType", {
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
         resolve(data as ChangeFiscalPeriodType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFiscalYear
   Description: Method to call when changing the Fiscal Year.
   OperationID: ChangeFiscalYear
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFiscalYear(requestBody:ChangeFiscalYear_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFiscalYear_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/ChangeFiscalYear", {
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
         resolve(data as ChangeFiscalYear_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFiscalYearSuffix
   Description: Method to call when changing the Fiscal Year Suffix.
   OperationID: ChangeFiscalYearSuffix
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFiscalYearSuffix(requestBody:ChangeFiscalYearSuffix_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFiscalYearSuffix_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/ChangeFiscalYearSuffix", {
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
         resolve(data as ChangeFiscalYearSuffix_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeJournalCode
   Description: Method to call when changing the Journal Code
   OperationID: ChangeJournalCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJournalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJournalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJournalCode(requestBody:ChangeJournalCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJournalCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/ChangeJournalCode", {
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
         resolve(data as ChangeJournalCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckGroupID
   Description: Purpose:
Parameters:
<param name="ipGroupID">Group ID</param><param name="ds">Import parameters.</param><param name="opMessage">Information messages to be displayed by the UI</param>
Notes:
   OperationID: CheckGroupID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckGroupID(requestBody:CheckGroupID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckGroupID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/CheckGroupID", {
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
         resolve(data as CheckGroupID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckFiscalYear
   Description: Method to call before updating the journal group. This method will check the
date that the user entered to verify it is in the current fiscal year and period.
If it is not then opMessage will be assigned with message text.  If it is
then the Fiscal Period and Year will be updated.
   OperationID: CheckFiscalYear
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckFiscalYear(requestBody:CheckFiscalYear_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckFiscalYear_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/CheckFiscalYear", {
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
         resolve(data as CheckFiscalYear_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetApplicationDefaults
   Description: Purpose: to load params when form is opened
Parameters:
<param name="ds"></param>
Notes:
   OperationID: GetApplicationDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetApplicationDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApplicationDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetApplicationDefaults(requestBody:GetApplicationDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetApplicationDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/GetApplicationDefaults", {
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
         resolve(data as GetApplicationDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetApplicationDefaultsExt
   Description: Purpose: to load params when form is opened
Parameters:
<param name="ds"></param><param name="clearGroup">True if group should be empty</param><param name="ipGroup">Group ID</param>
Notes:
   OperationID: GetApplicationDefaultsExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetApplicationDefaultsExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApplicationDefaultsExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetApplicationDefaultsExt(requestBody:GetApplicationDefaultsExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetApplicationDefaultsExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/GetApplicationDefaultsExt", {
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
         resolve(data as GetApplicationDefaultsExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultsAndApplicationDefaultsExt
   Description: Purpose: to load params when form is opened
Parameters:
<param name="ds"></param>
Notes:
   OperationID: GetDefaultsAndApplicationDefaultsExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaultsAndApplicationDefaultsExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultsAndApplicationDefaultsExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultsAndApplicationDefaultsExt(requestBody:GetDefaultsAndApplicationDefaultsExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultsAndApplicationDefaultsExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/GetDefaultsAndApplicationDefaultsExt", {
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
         resolve(data as GetDefaultsAndApplicationDefaultsExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearAndGetApplicationDefaults
   Description: Purpose: to load params when form is opened
Parameters:
<param name="ds"></param>
Notes:
   OperationID: ClearAndGetApplicationDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ClearAndGetApplicationDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAndGetApplicationDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearAndGetApplicationDefaults(requestBody:ClearAndGetApplicationDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ClearAndGetApplicationDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/ClearAndGetApplicationDefaults", {
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
         resolve(data as ClearAndGetApplicationDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFiscalPeriodList
   Description: Returns fiscal period list in code/description format
   OperationID: GetFiscalPeriodList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFiscalPeriodList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalPeriodList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFiscalPeriodList(requestBody:GetFiscalPeriodList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFiscalPeriodList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/GetFiscalPeriodList", {
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
         resolve(data as GetFiscalPeriodList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTokenList
   Description: Returns a comma separated list of valid tokens for the given datatype.
   OperationID: Get_GetTokenList
      @param tokenDataType Desc: Type of token for which you want the list of valid values. Valid Types are; Date, FiscalPeriod, FiscalYear   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetTokenList(tokenDataType:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tokenDataType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tokenDataType=" + tokenDataType
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTokenList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/GetTokenList" + params, {
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
         resolve(data as GetTokenList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTokenValue
   Description: Returns a token list of values based on a type that is passed in.
   OperationID: Get_GetTokenValue
      @param pcValue Desc: Type of token   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetTokenValue(pcValue:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof pcValue!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pcValue=" + pcValue
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTokenValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/GetTokenValue" + params, {
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
         resolve(data as GetTokenValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SubmitToAgent
   Description: Submits this report to a System Agent. The system agent will run the task based on the defined schedule.
   OperationID: SubmitToAgent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SubmitToAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitToAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitToAgent(requestBody:SubmitToAgent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SubmitToAgent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/SubmitToAgent", {
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
         resolve(data as SubmitToAgent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaults
   Description: Use to get the current parameter defaults that the user has established for this report.
Note: This is automatically run as part of the GetNewParameters method.
In cases where the ParamSetID would be blank (this is most cases) you would not need to call this method.
It is provided to provide the ability to get the defaults after the user has enter a value into the field
designated as ParamSetID.
As is the case in GLFinancial Reports the GLFinancialParam.GLReportID is used as the ParamSetID field.
Another possible use would be to Reset the screen to default values.
   OperationID: GetDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaults(requestBody:GetDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/GetDefaults", {
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
         resolve(data as GetDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewParameters
   Description: Creates a new (parameter record) in the dataset.
Note: A parameter dataset should never contain more than one record.
   OperationID: Get_GetNewParameters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetNewParameters(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewParameters_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/GetNewParameters", {
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
         resolve(data as GetNewParameters_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetParamsFromAgent
   Description: Gets existing parameter values from the Task Agent and returns them in the in the dataset.
Note: Parameters are stored as individual fields in the database. This method is
used to retrieve those values and return them in the specific dataset.
   OperationID: Get_GetParamsFromAgent
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamsFromAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetParamsFromAgent(agentID:string, agentSchedNum:string, agentTaskNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof agentID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "agentID=" + agentID
   }
   if(typeof agentSchedNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "agentSchedNum=" + agentSchedNum
   }
   if(typeof agentTaskNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "agentTaskNum=" + agentTaskNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetParamsFromAgent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/GetParamsFromAgent" + params, {
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
         resolve(data as GetParamsFromAgent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetParamTaskDef
   Description: Use to get the specified ProcessSet Task defaults that the user has established for this report.
It is provided to provide the ability to get the defaults after the user has enter a value into the field
designated as ParamSetID.
   OperationID: GetParamTaskDef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetParamTaskDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamTaskDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetParamTaskDef(requestBody:GetParamTaskDef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetParamTaskDef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/GetParamTaskDef", {
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
         resolve(data as GetParamTaskDef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveDefaults
   Description: Use to remove the current parameter defaults that the user has established for this report.
   OperationID: RemoveDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemoveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveDefaults(requestBody:RemoveDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/RemoveDefaults", {
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
         resolve(data as RemoveDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RunDirect
   Description: Use to run the process directly from the client instead of submitting to a System Agent.
   OperationID: RunDirect
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RunDirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunDirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunDirect(requestBody:RunDirect_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RunDirect_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/RunDirect", {
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
         resolve(data as RunDirect_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveDefaults
   Description: Use to save the current parameters as the users defaults for this report
   OperationID: SaveDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveDefaults(requestBody:SaveDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/SaveDefaults", {
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
         resolve(data as SaveDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveProcessTask
   Description: Use to save the current parameters as the users defaults for this report
<param name="maintProgram">UI Maintenance program </param><param name="ds" />
   OperationID: SaveProcessTask
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveProcessTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveProcessTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveProcessTask(requestBody:SaveProcessTask_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveProcessTask_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/SaveProcessTask", {
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
         resolve(data as SaveProcessTask_output)
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
      @param proposeBookID
      @param ds
   */  
export interface ChangeBookID_input{
      /**  The proposed Book ID  */  
   proposeBookID:string,
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface ChangeBookID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param proposedBookMode
      @param ds
   */  
export interface ChangeEntryMode_input{
      /**  The proposed Entry Mode  */  
   proposedBookMode:string,
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface ChangeEntryMode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param proposedPeriodType
      @param ds
   */  
export interface ChangeFiscalPeriodType_input{
      /**  The proposed Fiscal Period Type  */  
   proposedPeriodType:string,
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface ChangeFiscalPeriodType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param proposedFiscalPeriod
      @param ds
   */  
export interface ChangeFiscalPeriod_input{
      /**  The proposed Fiscal Period  */  
   proposedFiscalPeriod:number,
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface ChangeFiscalPeriod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param proposedFiscalYearSuffix
      @param ds
   */  
export interface ChangeFiscalYearSuffix_input{
      /**  The proposed Fiscal Year Suffix  */  
   proposedFiscalYearSuffix:string,
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface ChangeFiscalYearSuffix_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param proposedFiscalYear
      @param ds
   */  
export interface ChangeFiscalYear_input{
      /**  The proposed Fiscal Year  */  
   proposedFiscalYear:number,
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface ChangeFiscalYear_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param ipJournalCode
      @param ds
   */  
export interface ChangeJournalCode_input{
      /**  The proposed Journal Code  */  
   ipJournalCode:string,
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface ChangeJournalCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param ds
      @param cGroupID
      @param cJEDate
   */  
export interface CheckFiscalYear_input{
   ds:Erp_Tablesets_GLImportProcTableset[],
      /**  Group Id field  */  
   cGroupID:string,
      /**  JEDate proposed value  */  
   cJEDate:string,
}

export interface CheckFiscalYear_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param ipGroupID
      @param ds
   */  
export interface CheckGroupID_input{
   ipGroupID:string,
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface CheckGroupID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
   opMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ClearAndGetApplicationDefaults_input{
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface ClearAndGetApplicationDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

export interface Erp_Tablesets_GLImportProcParamRow{
      /**  GL Group ID to import.  */  
   GroupID:string,
      /**  Extended text to describe the journal header.  Defaults to all GLJrnDtl.CommentText.  */  
   CommentText:string,
      /**  Flag to determine if the Imported Group will be posted.  */  
   Post:boolean,
      /**  Selected date format that will be imported.  */  
   InpDateFormat:string,
      /**  Selected numeric format that will be imported.  */  
   InpNumFormat:string,
      /**  Indicates what mode the GL transactions will be entered.  Valid values are (S) for Single Book and (M) for Multi-Book.  */  
   BookMode:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Unique code that identifies the currency.  */  
   CurrencyCode:string,
   RateGrpCode:string,
      /**  Default Journal Date for all entries made in this group.  */  
   JEDate:string,
      /**  Fiscal Year to which all entries in this group will be posted.  */  
   FiscalYear:number,
      /**  The Fiscal Period to which all entries in this group will be posted.  */  
   FiscalPeriod:number,
      /**  A code that defines a journal.  */  
   JournalCode:string,
      /**  Fiscal Year Suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period where derived from.  */  
   FiscalCalendarID:string,
      /**  Indicates what type of fiscal periods can be selected for the group.  Values are: O - Ordinary periods, C - Closing Periods.  */  
   FiscalPeriodType:string,
   FiscalCalendarDesc:string,
   RateGrpDescription:string,
   JournalCodeDesc:string,
   BookDescription:string,
   CurrencyCodeDesc:string,
      /**  Used by the UI for row rules.  Indicates if the group has GLJrnhed records.  */  
   HasDetails:boolean,
      /**  Selected Delimiter to use when parsing the import/export file  */  
   CSVListDelimiter:string,
   ClientImportFileName:string,
   ServerImportFileName:string,
      /**  Options for the system’s handling of invalid lines found in the import file. 'Skip Invalid Lines' means that the GL Import skips invalid lines and imports the valid ones. 'Cancel Import' means that if any lines are found invalid, then the process should roll back all imported data without creating any Journals.  */  
   InvalidLinesHandlingOp:string,
   SysRowID:string,
   AutoAction:string,
   PrinterName:string,
   AgentSchedNum:number,
   AgentID:string,
   AgentTaskNum:number,
   RecurringTask:boolean,
   RptPageSettings:string,
   RptPrinterSettings:string,
   RptVersion:string,
   ReportStyleNum:number,
   WorkstationID:string,
   TaskNote:string,
   ArchiveCode:number,
   DateFormat:string,
   NumericFormat:string,
   AgentCompareString:string,
   ProcessID:string,
   ProcessCompany:string,
   ProcessSystemCode:string,
   ProcessTaskNum:number,
   DecimalsGeneral:number,
   DecimalsCost:number,
   DecimalsPrice:number,
   GlbDecimalsGeneral:number,
   GlbDecimalsCost:number,
   GlbDecimalsPrice:number,
   FaxSubject:string,
   FaxTo:string,
   FaxNumber:string,
   EMailTo:string,
   EMailCC:string,
   EMailBCC:string,
   EMailBody:string,
   AttachmentType:string,
   ReportCurrencyCode:string,
   ReportCultureCode:string,
   SSRSRenderFormat:string,
   UIXml:string,
   PrintReportParameters:boolean,
   SSRSEnableRouting:boolean,
   DesignMode:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLImportProcTableset{
   GLImportProcParam:Erp_Tablesets_GLImportProcParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param clearGroup
      @param ipGroup
   */  
export interface GetApplicationDefaultsExt_input{
   ds:Erp_Tablesets_GLImportProcTableset[],
   clearGroup:boolean,
   ipGroup:string,
}

export interface GetApplicationDefaultsExt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetApplicationDefaults_input{
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface GetApplicationDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetDefaultsAndApplicationDefaultsExt_input{
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface GetDefaultsAndApplicationDefaultsExt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetDefaults_input{
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface GetDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param fiscalCalendarID
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalPeriod
      @param fiscalPeriodType
   */  
export interface GetFiscalPeriodList_input{
      /**  Fiscal Calendar ID  */  
   fiscalCalendarID:string,
      /**  Fiscal Year  */  
   fiscalYear:number,
      /**  Fiscal Year Suffix  */  
   fiscalYearSuffix:string,
      /**  Fiscal Period  */  
   fiscalPeriod:number,
      /**  Fiscal Period Type  */  
   fiscalPeriodType:string,
}

export interface GetFiscalPeriodList_output{
parameters : {
      /**  output parameters  */  
   fiscalPeriodList:string,
}
}

export interface GetNewParameters_output{
   returnObj:Erp_Tablesets_GLImportProcTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetParamTaskDef_input{
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface GetParamTaskDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLImportProcTableset,
}
}

   /** Required : 
      @param agentID
      @param agentSchedNum
      @param agentTaskNum
   */  
export interface GetParamsFromAgent_input{
   agentID:string,
   agentSchedNum:number,
   agentTaskNum:number,
}

export interface GetParamsFromAgent_output{
   returnObj:Erp_Tablesets_GLImportProcTableset[],
}

   /** Required : 
      @param fileName
      @param folder
   */  
export interface GetServerTempPath_input{
      /**  File name  */  
   fileName:string,
      /**  Special folder  */  
   folder:number,
}

export interface GetServerTempPath_output{
      /**  Full server path  */  
   returnObj:string,
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
      @param pcValue
   */  
export interface GetTokenValue_input{
      /**  Type of token  */  
   pcValue:string,
}

export interface GetTokenValue_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   pcTokenValue:string,
}
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

   /** Required : 
      @param paramSetID
   */  
export interface RemoveDefaults_input{
      /**  The defaults are stored with a key of Company,UserID,ProgramID,ParamSetID and FieldName
            The values of all of these, except ParamSetID are controlled by the backend logic.
            In most cases the ParamSetID is blank. Usually for a single program the user can only have one set of defaults.
            This parameter provides multi parameters sets to be associated with a single report.
            As is the case of GL Financial Reports. The user picks from a list of reports to be run.
            In this case you would pass the GLFinancialParam.GLReportID as the ParamSetID  */  
   paramSetID:string,
}

export interface RemoveDefaults_output{
}

   /** Required : 
      @param ds
   */  
export interface RunDirect_input{
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface RunDirect_output{
}

   /** Required : 
      @param ds
   */  
export interface SaveDefaults_input{
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface SaveDefaults_output{
}

   /** Required : 
      @param maintProgram
      @param ds
   */  
export interface SaveProcessTask_input{
   maintProgram:string,
   ds:Erp_Tablesets_GLImportProcTableset[],
}

export interface SaveProcessTask_output{
}

   /** Required : 
      @param ds
      @param agentID
      @param agentSchedNum
      @param agentTaskNum
      @param maintProgram
   */  
export interface SubmitToAgent_input{
   ds:Erp_Tablesets_GLImportProcTableset[],
      /**  Agent ID that will run this task  */  
   agentID:string,
      /**  Identifies the agent schedule of when this task should be run.
           Set to zero if you want to run this immediately.  */  
   agentSchedNum:number,
      /**  Identifies the agent task number within the schedule that is to be updated.
           Set to zero if you want to create a new task.  */  
   agentTaskNum:number,
      /**  Identifies the Maintenance program to run  */  
   maintProgram:string,
}

export interface SubmitToAgent_output{
}

