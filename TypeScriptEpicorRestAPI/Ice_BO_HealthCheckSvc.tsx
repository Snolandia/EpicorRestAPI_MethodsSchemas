import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.HealthCheckSvc
// Description: Health Check implementation testing status of ERP application, database, task and reporting services
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/$metadata", {
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
   Summary: Invoke method ErpAlive
   Description: Check if application server is running
   OperationID: ErpAlive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ErpAlive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ErpAlive(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/ErpAlive", {
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
   Summary: Invoke method DatabaseAlive
   Description: Checks if the database is responding.
   OperationID: DatabaseAlive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DatabaseAlive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DatabaseAlive(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/DatabaseAlive", {
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
   Summary: Invoke method ReportServerAlive
   Description: Checks whether the Report Server is accessible.
   OperationID: ReportServerAlive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportServerAlive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReportServerAlive(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/ReportServerAlive", {
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
   Summary: Invoke method ListCompanies
   Description: Return company identifiers that the current user has access to.
   OperationID: ListCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListCompanies_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListCompanies(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/ListCompanies", {
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
   Summary: Invoke method StartProcess
   Description: Submit the test process to the task agent.
   OperationID: StartProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartProcess(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/StartProcess", {
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
   Summary: Invoke method StartProcessOnAgent
   Description: Submit the test process to the task agent
   OperationID: StartProcessOnAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartProcessOnAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartProcessOnAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartProcessOnAgent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/StartProcessOnAgent", {
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
   Summary: Invoke method ProcessStatus
   Description: Checks the status of the process that was started earlier in M:Ice.Services.BO.HealthCheckSvc.StartProcess(System.String).
   OperationID: ProcessStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/ProcessStatus", {
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
   Summary: Invoke method StartPrint
   Description: Submit the test print to the task agent.
   OperationID: StartPrint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartPrint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartPrint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartPrint(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/StartPrint", {
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
   Summary: Invoke method StartPrintOnAgent
   Description: Submit the test print to the task agent
   OperationID: StartPrintOnAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartPrintOnAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartPrintOnAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartPrintOnAgent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/StartPrintOnAgent", {
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
   Summary: Invoke method PrintStatus
   Description: Get the current status of the print
   OperationID: PrintStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrintStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrintStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/PrintStatus", {
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
   Summary: Invoke method CountImmediateSched
   OperationID: CountImmediateSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountImmediateSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountImmediateSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountImmediateSched(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/CountImmediateSched", {
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
   Summary: Invoke method GetTaskDetails
   Description: Get details of tasks.
   OperationID: GetTaskDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaskDetails(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.HealthCheckSvc/GetTaskDetails", {
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
      @param cutOffMinutes
   */  
export interface CountImmediateSched_input{
   cutOffMinutes:number,
}

export interface CountImmediateSched_output{
parameters : {
      /**  output parameters  */  
   count:number,
   earliest:string,
}
}

export interface DatabaseAlive_output{
      /**  The execution time in milliseconds.  */  
   returnObj:number,
}

export interface ErpAlive_output{
}

export interface GetTaskDetails_output{
   returnObj:string,
}

export interface ListCompanies_output{
      /**  The companies that the user has access to.  */  
   returnObj:string,
}

   /** Required : 
      @param id
      @param submitTime
   */  
export interface PrintStatus_input{
      /**  The process identifier.  */  
   id:string,
      /**  The submit time.  */  
   submitTime:string,
}

export interface PrintStatus_output{
      /**  The !:Ice.BO.HealthCheck.TaskStatus for the process.  */  
   returnObj:number,
}

   /** Required : 
      @param id
      @param submitTime
   */  
export interface ProcessStatus_input{
      /**  The process identifier.  */  
   id:string,
      /**  The submit time.  */  
   submitTime:string,
}

export interface ProcessStatus_output{
      /**  The !:Ice.BO.HealthCheck.TaskStatus for the process.  */  
   returnObj:number,
}

export interface ReportServerAlive_output{
}

   /** Required : 
      @param companyID
      @param agentID
   */  
export interface StartPrintOnAgent_input{
      /**  If not specified will execute against current company  */  
   companyID:string,
      /**  Agent ID to run against  */  
   agentID:string,
}

export interface StartPrintOnAgent_output{
      /**  A JSON serialized object that holds the identifier and submit time.  */  
   returnObj:string,
}

   /** Required : 
      @param companyID
   */  
export interface StartPrint_input{
      /**  If not specified will execute against current company.  */  
   companyID:string,
}

export interface StartPrint_output{
      /**  A JSON serialized object that holds the identifier and submit time.  */  
   returnObj:string,
}

   /** Required : 
      @param companyID
      @param agentID
   */  
export interface StartProcessOnAgent_input{
      /**  If not specified will execute against current company  */  
   companyID:string,
      /**  Agent ID to run against  */  
   agentID:string,
}

export interface StartProcessOnAgent_output{
      /**  A JSON serialized object that holds the identifier and submit time.  */  
   returnObj:string,
}

   /** Required : 
      @param companyID
   */  
export interface StartProcess_input{
      /**  If not specified will execute against current company  */  
   companyID:string,
}

export interface StartProcess_output{
      /**  A JSON serialized object that holds the identifier and submit time.  */  
   returnObj:string,
}

