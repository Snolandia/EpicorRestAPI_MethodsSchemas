import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.BatchOpsSvc
// Description: File        : bo/BatchOps/BatchOps.p
            
Purpose     : To  create a batch Job.
A Batch Job is created with the operations pulled from the primary job (first job selected) and
the necessary raw material requirements.
The operations are processed on all jobs begining at or ending at the specified operation. This
is only done per the single assembly of the operation.
All these operations will be marked as complete on the source job. Only the operations from the
primary job will transfered to the new Batch Job.
All related Raw materials from all jobs that are being batched are transfered to the Batch Job.
If bathcing the first operation of the assembly then the unrelated materials will be transfered also.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BatchOpsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BatchOpsSvc/$metadata", {
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
   Summary: Invoke method DoBatching
   Description: Combines the given list of job operations from different jobs into a single "bathced" job.
   OperationID: DoBatching
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DoBatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoBatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DoBatching(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BatchOpsSvc/DoBatching", {
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
   Summary: Invoke method IsFullSerial
   Description: Dummy method IsFullSerial
   OperationID: IsFullSerial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsFullSerial_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsFullSerial(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BatchOpsSvc/IsFullSerial", {
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
   Summary: Invoke method SetFinalOprOnBatchedJob
   Description: Purpose: SETS THE AUTO RECEIVE OPERATION ON THE BATCHED JOB.
            
Parameters:  none
Notes:
   OperationID: SetFinalOprOnBatchedJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFinalOprOnBatchedJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetFinalOprOnBatchedJob(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BatchOpsSvc/SetFinalOprOnBatchedJob", {
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
      @param jobProcessMode
      @param pullDirection
      @param autoReceive
      @param finalOpr
      @param opRowIDList
   */  
export interface DoBatching_input{
      /**  Process Mode for the new job. Values: S(Sequential) or C(Concurrent).  */  
   jobProcessMode:string,
      /**  Direction to pull operations beginning at the specified operation.
           Can be Forward or Backward  */  
   pullDirection:string,
      /**  Auto Receive  */  
   autoReceive:boolean,
      /**  Final Operation  */  
   finalOpr:boolean,
      /**  Comma separated list of Operations (JobOper.RowIdent) to begin pulling into batched job.  */  
   opRowIDList:string,
}

export interface DoBatching_output{
parameters : {
      /**  output parameters  */  
   newJobNum:string,
}
}

export interface IsFullSerial_output{
}

export interface SetFinalOprOnBatchedJob_output{
}

