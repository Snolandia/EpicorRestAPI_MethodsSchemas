import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ScheduleEngineSvc
// Description: For scheduling jobs, assemblies and operations.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/$metadata", {
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
   Summary: Invoke method ReadExtSchedule
   Description: Load ExtSchedule dataset from a XML file
   OperationID: ReadExtSchedule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReadExtSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReadExtSchedule(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReadExtSchedule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/ReadExtSchedule", {
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
         resolve(data as ReadExtSchedule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessExtSchedule
   Description: Process data from External Schedule system receiving Operation Dates in ExtSchedule dataset
   OperationID: ProcessExtSchedule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessExtSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessExtSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessExtSchedule(requestBody:ProcessExtSchedule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessExtSchedule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/ProcessExtSchedule", {
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
         resolve(data as ProcessExtSchedule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AcceptChanges
   Description: This method commits a job. Move Whatif to scheduled.
   OperationID: AcceptChanges
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AcceptChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AcceptChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AcceptChanges(requestBody:AcceptChanges_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AcceptChanges_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/AcceptChanges", {
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
         resolve(data as AcceptChanges_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeProductionComplete
   Description: This method does stuff.
   OperationID: ChangeProductionComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeProductionComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProductionComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeProductionComplete(requestBody:ChangeProductionComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeProductionComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/ChangeProductionComplete", {
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
         resolve(data as ChangeProductionComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeResource
   Description: This method will change
the resource on a resourcetimeused record.
   OperationID: ChangeResource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeResource(requestBody:ChangeResource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeResource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/ChangeResource", {
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
         resolve(data as ChangeResource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSetupComplete
   Description: This method does stuff.
   OperationID: ChangeSetupComplete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSetupComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSetupComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSetupComplete(requestBody:ChangeSetupComplete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSetupComplete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/ChangeSetupComplete", {
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
         resolve(data as ChangeSetupComplete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLoadLevelDflts
   Description: This method does stuff .
   OperationID: GetLoadLevelDflts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLoadLevelDflts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLoadLevelDflts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLoadLevelDflts(requestBody:GetLoadLevelDflts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLoadLevelDflts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/GetLoadLevelDflts", {
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
         resolve(data as GetLoadLevelDflts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMultiSchedTypeCodes
   Description: Returns the list of Schedule Type Code and Descriptions needed to schedule in multi-job
MultiSchedTypeCodes is used when scheduling initially in Multi-Job
   OperationID: GetMultiSchedTypeCodes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMultiSchedTypeCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMultiSchedTypeCodes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMultiSchedTypeCodes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/GetMultiSchedTypeCodes", {
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
         resolve(data as GetMultiSchedTypeCodes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSchedTypeCodes
   Description: Returns the list of Schedule Type Code and Descriptions . Three lists are returned
SchedTypecodes is used when moving the entire job,
OperationOnlySchedTypecodes is used only for operations.
   OperationID: GetSchedTypeCodes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSchedTypeCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSchedTypeCodes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSchedTypeCodes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/GetSchedTypeCodes", {
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
         resolve(data as GetSchedTypeCodes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetScheduleRecord
   Description: This method allows the UI to retrieve a blank Schedule record.
   OperationID: GetScheduleRecord
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetScheduleRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetScheduleRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetScheduleRecord(requestBody:GetScheduleRecord_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetScheduleRecord_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/GetScheduleRecord", {
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
         resolve(data as GetScheduleRecord_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadChildJobs
   OperationID: LoadChildJobs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadChildJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadChildJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadChildJobs(requestBody:LoadChildJobs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadChildJobs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/LoadChildJobs", {
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
         resolve(data as LoadChildJobs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadParentJobs
   OperationID: LoadParentJobs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadParentJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadParentJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadParentJobs(requestBody:LoadParentJobs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadParentJobs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/LoadParentJobs", {
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
         resolve(data as LoadParentJobs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadLeveling
   Description: Load method.
   OperationID: LoadLeveling
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadLeveling_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadLeveling_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadLeveling(requestBody:LoadLeveling_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadLeveling_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/LoadLeveling", {
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
         resolve(data as LoadLeveling_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveJobItem
   Description: Procedure to move an Operation Detail.
   OperationID: MoveJobItem
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveJobItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveJobItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveJobItem(requestBody:MoveJobItem_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveJobItem_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/MoveJobItem", {
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
         resolve(data as MoveJobItem_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewParamsForJob
   Description: Get New Schedule Engine Parameters for a specific Job.
   OperationID: GetNewParamsForJob
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewParamsForJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewParamsForJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewParamsForJob(requestBody:GetNewParamsForJob_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewParamsForJob_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/GetNewParamsForJob", {
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
         resolve(data as GetNewParamsForJob_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveSchedBoardItem
   Description: Procedure to move an Operation Detail, used for moving a scheduling board
item, allows the movement of a locked job.
   OperationID: MoveSchedBoardItem
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveSchedBoardItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveSchedBoardItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveSchedBoardItem(requestBody:MoveSchedBoardItem_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveSchedBoardItem_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/MoveSchedBoardItem", {
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
         resolve(data as MoveSchedBoardItem_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveSchedule
   Description: This method does stuff .
   OperationID: SaveSchedule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveSchedule(requestBody:SaveSchedule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveSchedule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/SaveSchedule", {
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
         resolve(data as SaveSchedule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetMachines
   Description: This method does stuff. Assign  JobOper.WIMachines from ScheduleEngine.Machines.
   OperationID: SetMachines
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetMachines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetMachines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetMachines(requestBody:SetMachines_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetMachines_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/SetMachines", {
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
         resolve(data as SetMachines_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UndoChanges
   Description: This method commits a job. Move Whatif to scheduled .
   OperationID: UndoChanges
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UndoChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UndoChanges(requestBody:UndoChanges_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UndoChanges_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/UndoChanges", {
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
         resolve(data as UndoChanges_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSchedulingMultiJobFlags
   Description: Get the flags needed for multi job scheduling
   OperationID: GetSchedulingMultiJobFlags
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSchedulingMultiJobFlags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSchedulingMultiJobFlags(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSchedulingMultiJobFlags_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/GetSchedulingMultiJobFlags", {
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
         resolve(data as GetSchedulingMultiJobFlags_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSchedulingFlags
   Description: Get the flags needed for scheduling
   OperationID: GetSchedulingFlags
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSchedulingFlags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSchedulingFlags(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSchedulingFlags_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ScheduleEngineSvc/GetSchedulingFlags", {
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
         resolve(data as GetSchedulingFlags_output)
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
      @param JobsMoved
      @param ds
   */  
export interface AcceptChanges_input{
   JobsMoved:string,
   ds:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface AcceptChanges_output{
}

   /** Required : 
      @param ds
   */  
export interface ChangeProductionComplete_input{
   ds:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface ChangeProductionComplete_output{
}

   /** Required : 
      @param ds
      @param ipAllocNum
      @param ipResourceID
      @param ipBlocksChanged
   */  
export interface ChangeResource_input{
   ds:Erp_Tablesets_ScheduleEngineTableset[],
   ipAllocNum:number,
      /**  The ResourceTimeUsed ResourceID  */  
   ipResourceID:string,
      /**  Determines wether the number of scheduling blocks changed or not  */  
   ipBlocksChanged:boolean,
}

export interface ChangeResource_output{
parameters : {
      /**  output parameters  */  
   WarnLogTxt:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeSetupComplete_input{
   ds:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface ChangeSetupComplete_output{
}

export interface Erp_Tablesets_ExtScheduleRow{
   AssemblySeq:number,
   Company:string,
   DueDate:string,
   DueHour:number,
   JobNum:string,
   MoveDueDate:string,
   MoveDueHour:number,
   OprSeq:number,
   QueStartDate:string,
   QueStartHour:number,
   StartDate:string,
   StartHour:number,
   StatusDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExtScheduleTableset{
   ExtSchedule:Erp_Tablesets_ExtScheduleRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ScheduleEngineRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   OpDtlSeq:number,
   StartDate:string,
   StartTime:number,
   EndDate:string,
   EndTime:number,
   WhatIf:boolean,
   Finite:boolean,
   SchedTypeCode:string,
      /**  expected values are 'Start' / 'End'  */  
   ScheduleDirection:string,
   SetupComplete:boolean,
   ProductionComplete:boolean,
   ScheduleID:string,
   CommentText:string,
   loadLevelBy:string,
   ConsiderPriority:boolean,
   LLStartDate:string,
   LLNewStartDate:string,
   OverrideMtlCon:boolean,
   LLCutOffDate:string,
      /**   Used to override the JCSyst.AllowSchedulingBeforeToday.
Values: 0 - false, 1 - true and 2 - ignored  */  
   OverRideHistDateSetting:number,
   ResourceID:string,
   ResourceGrpID:string,
   AllocNum:number,
   Machines:number,
      /**  Flag to indicate whether the job expected production yield quantities should be recalculated for this jobs if ProductionYield = true and there are operations that have been flagged for recalculation.  */  
   RecalcExpProdYld:boolean,
      /**  Indicates whether the selected (What-If) Resource should be written back to the Job Operation Detail record.   In the case where the user wants to select a specific resource but have global or job schedule select a new resource by availability when re-scheduling the job they would uncheck this box.  If the "Update Job Operation Detail" check box is true AND the number of scheduling blocks is 1 then write the new resource back to the Job Operation just like selecting the resource manually in job  */  
   UpdateJobOpDtl:boolean,
      /**  it contains the list of Job numbers to save  */  
   JobNumList:string,
   JobEngineered:boolean,
      /**  Default value for the this flag at every place where the scheduling UI is called to instruct to the scheduling engine looks for any assembly or material that has a direct job link and those linked jobs get rescheduled as well to be just in time to supply the main job.  */  
   UseSchedulingMultiJob:boolean,
      /**  When Schedule Multi Job option is selected this option is used to have the ability to ignore locks for Jobs.  */  
   SchedulingMultiJobIgnoreLocks:boolean,
      /**  Used to Minimize WIP between jobs  */  
   SchedulingMultiJobMinimizeWIP:boolean,
   JobType:string,
      /**  Allows moving Jobs across plants within the company and not only for the plant where user is logged on.  */  
   SchedulingMultiJobMoveJobsAcrossPlants:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ScheduleEngineTableset{
   ScheduleEngine:Erp_Tablesets_ScheduleEngineRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GetLoadLevelDflts_input{
   ds:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface GetLoadLevelDflts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ScheduleEngineTableset,
}
}

export interface GetMultiSchedTypeCodes_output{
parameters : {
      /**  output parameters  */  
   MultiSchedTypeCodes:string,
}
}

   /** Required : 
      @param jobNum
      @param kitTime
      @param ignoreMtlConstraints
   */  
export interface GetNewParamsForJob_input{
      /**  Job Number  */  
   jobNum:string,
      /**  Kit Time defined on Job  */  
   kitTime:number,
      /**  Ignore Material Constraints defined on Job  */  
   ignoreMtlConstraints:boolean,
}

export interface GetNewParamsForJob_output{
   returnObj:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface GetSchedTypeCodes_output{
parameters : {
      /**  output parameters  */  
   SchedTypecodes:string,
   OperationOnlySchedTypecodes:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetScheduleRecord_input{
   ds:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface GetScheduleRecord_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ScheduleEngineTableset,
}
}

export interface GetSchedulingFlags_output{
parameters : {
      /**  output parameters  */  
   schedulingMultiJobActive:boolean,
   minimizeWIPFlag:boolean,
   allowMoveJobsAcrossPlants:boolean,
   autoLoadParentJobs:boolean,
   autoLoadChildJobs:boolean,
   BWSchedStartTime:number,
   schedulingDirection:string,
}
}

export interface GetSchedulingMultiJobFlags_output{
parameters : {
      /**  output parameters  */  
   schedulingMultiJobActive:boolean,
   minimizeWIPFlag:boolean,
   allowMoveJobsAcrossPlants:boolean,
   autoLoadParentJobs:boolean,
   autoLoadChildJobs:boolean,
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
      @param jobNum
      @param company
   */  
export interface LoadChildJobs_input{
   jobNum:string,
   company:string,
}

export interface LoadChildJobs_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface LoadLeveling_input{
   ds:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface LoadLeveling_output{
}

   /** Required : 
      @param jobNum
      @param company
   */  
export interface LoadParentJobs_input{
   jobNum:string,
   company:string,
}

export interface LoadParentJobs_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface MoveJobItem_input{
   ds:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface MoveJobItem_output{
parameters : {
      /**  output parameters  */  
   l_finished:boolean,
   c_WarnLogTxt:string,
}
}

   /** Required : 
      @param ds
   */  
export interface MoveSchedBoardItem_input{
   ds:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface MoveSchedBoardItem_output{
parameters : {
      /**  output parameters  */  
   l_finished:boolean,
   c_WarnLogTxt:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessExtSchedule_input{
   ds:Erp_Tablesets_ExtScheduleTableset[],
}

export interface ProcessExtSchedule_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ExtScheduleTableset,
}
}

export interface ReadExtSchedule_output{
   returnObj:Erp_Tablesets_ExtScheduleTableset[],
}

   /** Required : 
      @param ds
   */  
export interface SaveSchedule_input{
   ds:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface SaveSchedule_output{
}

   /** Required : 
      @param ds
   */  
export interface SetMachines_input{
   ds:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface SetMachines_output{
}

   /** Required : 
      @param JobsMoved
      @param ds
   */  
export interface UndoChanges_input{
   JobsMoved:string,
   ds:Erp_Tablesets_ScheduleEngineTableset[],
}

export interface UndoChanges_output{
}

