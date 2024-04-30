import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.QuickJobEntrySvc
// Description: Quick Job Entry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", {
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
   Summary: Invoke method ChangeAttributeSetID
   Description: Call this method when the attribute set changes
   OperationID: ChangeAttributeSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAttributeSetID(requestBody:ChangeAttributeSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeAttributeSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/ChangeAttributeSetID", {
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
         resolve(data as ChangeAttributeSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuickJobEngineered
   Description: This method validates the QuickJob.Engineered and potentially changes the Released field.
This method should run when the QuickJob.Engineered field changes.
   OperationID: ChangeQuickJobEngineered
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobEngineered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobEngineered_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuickJobEngineered(requestBody:ChangeQuickJobEngineered_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeQuickJobEngineered_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/ChangeQuickJobEngineered", {
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
         resolve(data as ChangeQuickJobEngineered_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuickJobFirm
   Description: This method validates the QuickJob.Firm and potentially changes the Released and
Engineered fields.
This method should run when the QuickJob.Firm field changes.
   OperationID: ChangeQuickJobFirm
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobFirm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobFirm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuickJobFirm(requestBody:ChangeQuickJobFirm_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeQuickJobFirm_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/ChangeQuickJobFirm", {
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
         resolve(data as ChangeQuickJobFirm_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuickJobPartNum
   Description: This method validates the QuickJob.PartNum and defaults fields associated with the partnum.
This method should run when the QuickJob.PartNum field changes.
   OperationID: ChangeQuickJobPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuickJobPartNum(requestBody:ChangeQuickJobPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeQuickJobPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/ChangeQuickJobPartNum", {
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
         resolve(data as ChangeQuickJobPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuickJobReleased
   Description: This method validates the QuickJob.Released and potentially changes the firm and engineered fields.
This method should run when the QuickJob.Released field changes.
   OperationID: ChangeQuickJobReleased
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobReleased_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobReleased_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuickJobReleased(requestBody:ChangeQuickJobReleased_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeQuickJobReleased_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/ChangeQuickJobReleased", {
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
         resolve(data as ChangeQuickJobReleased_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuickJobWarehouseCode
   Description: This method validates the QuickJob.WarehouseCode and defaults warehousedesc field
associated with the warehousecode.
This method should run when the QuickJob.WarehouseCode field changes.
   OperationID: ChangeQuickJobWarehouseCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuickJobWarehouseCode(requestBody:ChangeQuickJobWarehouseCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeQuickJobWarehouseCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/ChangeQuickJobWarehouseCode", {
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
         resolve(data as ChangeQuickJobWarehouseCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuickJobContract
   Description: Update Quick Job information with WarehouseCode from the Planning Contract
   OperationID: ChangeQuickJobContract
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuickJobContract(requestBody:ChangeQuickJobContract_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeQuickJobContract_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/ChangeQuickJobContract", {
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
         resolve(data as ChangeQuickJobContract_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRevisionNum
   Description: Call this method when Revision changes to maintain inventory tracking
   OperationID: ChangeRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRevisionNum(requestBody:ChangeRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/ChangeRevisionNum", {
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
         resolve(data as ChangeRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateJobNum
   Description: Check if the jobnum exists
   OperationID: ValidateJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateJobNum(requestBody:ValidateJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/ValidateJobNum", {
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
         resolve(data as ValidateJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateJob
   Description: Generate the job.
   OperationID: GenerateJob
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateJob(requestBody:GenerateJob_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateJob_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/GenerateJob", {
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
         resolve(data as GenerateJob_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewQuickJob
   Description: This method is the first thing that should be ran.  It creates a ttQuickJob record in the
dataset that we will use to collect user inputs for this Quick Job Entry process.  This method
creates the record and assigns the next job number, date, firm, released,engineered,and legal number fields
and returns the dataset with the one record.  This dataset is not a database dataset, it
is a temporary dataset with the only record ever in the dataset is the one that you create here.
   OperationID: GetNewQuickJob
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewQuickJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuickJob(requestBody:GetNewQuickJob_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewQuickJob_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/GetNewQuickJob", {
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
         resolve(data as GetNewQuickJob_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:GetPartXRefInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartXRefInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/GetPartXRefInfo", {
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
         resolve(data as GetPartXRefInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindPart
   OperationID: FindPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPart(requestBody:FindPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/FindPart", {
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
         resolve(data as FindPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartFromRowID
   OperationID: GetPartFromRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFromRowID(requestBody:GetPartFromRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartFromRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/GetPartFromRowID", {
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
         resolve(data as GetPartFromRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateJobInfo
   Description: Validates Job Information before create it.
   OperationID: ValidateJobInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateJobInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJobInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateJobInfo(requestBody:ValidateJobInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateJobInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/ValidateJobInfo", {
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
         resolve(data as ValidateJobInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreGenerateJob
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreGenerateJob
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreGenerateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGenerateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreGenerateJob(requestBody:PreGenerateJob_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreGenerateJob_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/PreGenerateJob", {
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
         resolve(data as PreGenerateJob_output)
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
      @param ds
      @param attributeSetID
   */  
export interface ChangeAttributeSetID_input{
   ds:Erp_Tablesets_QuickJobEntryTableset[],
   attributeSetID:number,
}

export interface ChangeAttributeSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickJobEntryTableset,
}
}

   /** Required : 
      @param ipContractID
      @param ds
   */  
export interface ChangeQuickJobContract_input{
      /**  The proposed ContractID  */  
   ipContractID:string,
   ds:Erp_Tablesets_QuickJobEntryTableset[],
}

export interface ChangeQuickJobContract_output{
parameters : {
      /**  output parameters  */  
   ipContractID:string,
   ds:Erp_Tablesets_QuickJobEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuickJobEngineered_input{
   ds:Erp_Tablesets_QuickJobEntryTableset[],
}

export interface ChangeQuickJobEngineered_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickJobEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuickJobFirm_input{
   ds:Erp_Tablesets_QuickJobEntryTableset[],
}

export interface ChangeQuickJobFirm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickJobEntryTableset,
}
}

   /** Required : 
      @param ds
      @param uomCode
   */  
export interface ChangeQuickJobPartNum_input{
   ds:Erp_Tablesets_QuickJobEntryTableset[],
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
}

export interface ChangeQuickJobPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickJobEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuickJobReleased_input{
   ds:Erp_Tablesets_QuickJobEntryTableset[],
}

export interface ChangeQuickJobReleased_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickJobEntryTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeQuickJobWarehouseCode_input{
   ds:Erp_Tablesets_QuickJobEntryTableset[],
}

export interface ChangeQuickJobWarehouseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickJobEntryTableset,
}
}

   /** Required : 
      @param ds
      @param revisionNum
   */  
export interface ChangeRevisionNum_input{
   ds:Erp_Tablesets_QuickJobEntryTableset[],
      /**  The new Revision number  */  
   revisionNum:string,
}

export interface ChangeRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickJobEntryTableset,
}
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuickJobEntryTableset{
   QuickJob:Erp_Tablesets_QuickJobRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QuickJobRow{
      /**  The Job Number  */  
   JobNum:string,
      /**  The Part Number  */  
   PartNum:string,
      /**  The Revision Number  */  
   RevisionNum:string,
      /**  The description for the associated partnum.  */  
   PartDesc:string,
      /**  The quantity for the new job  */  
   Quantity:number,
      /**  Firm?  */  
   Firm:boolean,
      /**  Is the job engineered?  */  
   Engineered:boolean,
      /**  Has the job been released?  */  
   Released:boolean,
      /**  The warehouse code  */  
   WarehouseCode:string,
      /**  The description of the warehouse  */  
   WarehouseDesc:string,
      /**  The bin number  */  
   BinNum:string,
      /**  The description of the bin  */  
   BinDesc:string,
      /**  The Legal Number  */  
   LegalNumber:string,
      /**  The job date field.  */  
   JobDate:string,
   EnableEngineered:boolean,
   EnableReleased:boolean,
   AlternateMethod:string,
   QuantityUOM:string,
      /**  Shedule a job as soon as it was created  */  
   Scheduled:boolean,
   ContractID:string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   TravelerReadyToPrint:boolean,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  ID of related Attribute Class assigned to the Part  */  
   PartAttrClassID:string,
      /**  Attribute Set Description  */  
   DynAttrValueSetDescription:string,
      /**  Attribute Set Short Description  */  
   DynAttrValueSetShortDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   PartTrackInventoryAttributes:boolean,
   PartTrackInventoryByRevision:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
   HasSerialNumbers:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   SerialMaskMaskType:number,
   SerialMaskMask:string,
   SerialMaskExample:string,
   SerialMaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Reference field  */  
   Reference:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  PartNumber  */  
   PartNum:string,
      /**  Serial number prefix  */  
   SNPrefix:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  Used only by SN Assignment  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask the was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
   RowSelected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
   ipPartNum:string,
}

export interface FindPart_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
   opMatchType:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GenerateJob_input{
   ds:Erp_Tablesets_QuickJobEntryTableset[],
}

export interface GenerateJob_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickJobEntryTableset,
   cMessageText:string,
}
}

   /** Required : 
      @param ipJobNum
   */  
export interface GetNewQuickJob_input{
   ipJobNum:string,
}

export interface GetNewQuickJob_output{
   returnObj:Erp_Tablesets_QuickJobEntryTableset[],
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowID_input{
   ipRowType:string,
   ipRowID:string,
}

export interface GetPartFromRowID_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
}
}

   /** Required : 
      @param partNum
      @param sysRowID
      @param rowType
      @param uomCode
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   sysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   uomCode:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
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
      @param ds
   */  
export interface PreGenerateJob_input{
   ds:Erp_Tablesets_QuickJobEntryTableset[],
}

export interface PreGenerateJob_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickJobEntryTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateJobInfo_input{
   ds:Erp_Tablesets_QuickJobEntryTableset[],
}

export interface ValidateJobInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickJobEntryTableset,
}
}

   /** Required : 
      @param jobNum
   */  
export interface ValidateJobNum_input{
      /**  The QuickJobEntry data set  */  
   jobNum:string,
}

export interface ValidateJobNum_output{
   returnObj:boolean,
}

