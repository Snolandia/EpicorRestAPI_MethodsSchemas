import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.SysMonitorSvc
// Description: The System Monitor service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/$metadata", {
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
   Summary: Invoke method GetMonitorDataKeepIdleTime
   Description: Gets the task data for the user.
   OperationID: GetMonitorDataKeepIdleTime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMonitorDataKeepIdleTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMonitorDataKeepIdleTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMonitorDataKeepIdleTime(requestBody:GetMonitorDataKeepIdleTime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMonitorDataKeepIdleTime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/GetMonitorDataKeepIdleTime", {
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
         resolve(data as GetMonitorDataKeepIdleTime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckForTaskUpdatesKeepIdleTime
   Description: Checks for Ice.SysRptLst and/or Ice.SysTask updates. This may return false positives.
   OperationID: CheckForTaskUpdatesKeepIdleTime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckForTaskUpdatesKeepIdleTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForTaskUpdatesKeepIdleTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckForTaskUpdatesKeepIdleTime(requestBody:CheckForTaskUpdatesKeepIdleTime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckForTaskUpdatesKeepIdleTime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/CheckForTaskUpdatesKeepIdleTime", {
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
         resolve(data as CheckForTaskUpdatesKeepIdleTime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CancelTask
   Description: Use to terminate a running task.
   OperationID: CancelTask
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CancelTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelTask(requestBody:CancelTask_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CancelTask_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/CancelTask", {
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
         resolve(data as CancelTask_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetScheduledTasks
   Description: To return the SysMonitorSchedDataSet which contains the scheduled tasks for a user.
   OperationID: GetScheduledTasks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetScheduledTasks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetScheduledTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetScheduledTasks(requestBody:GetScheduledTasks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetScheduledTasks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/GetScheduledTasks", {
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
         resolve(data as GetScheduledTasks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaskHistory
   Description: To return Task history records for the current user for a specified number of days.
   OperationID: GetTaskHistory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTaskHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaskHistory(requestBody:GetTaskHistory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTaskHistory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/GetTaskHistory", {
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
         resolve(data as GetTaskHistory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTReports
   Description: To return the SysMonitorDataSet which contains the SysTask and SysRptLst tables.
   OperationID: GetTReports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTReports(requestBody:GetTReports_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTReports_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/GetTReports", {
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
         resolve(data as GetTReports_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReports
   Description: To return the SysMonitorDataSet which contains the SysRptLst tables.
   OperationID: GetReports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReports(requestBody:GetReports_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReports_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/GetReports", {
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
         resolve(data as GetReports_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCompanyList
   Description: Return list of company current user has access to.
   OperationID: GetCompanyList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompanyList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCompanyList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/GetCompanyList", {
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
         resolve(data as GetCompanyList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateSysMonitorDS
   Description: Use to commit updates and deletions of the SysMonitor dataset to the database.
Does NOT support adding new records.
Does NOT support deletion of SysTask records.
   OperationID: UpdateSysMonitorDS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateSysMonitorDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSysMonitorDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSysMonitorDS(requestBody:UpdateSysMonitorDS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateSysMonitorDS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/UpdateSysMonitorDS", {
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
         resolve(data as UpdateSysMonitorDS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateSysMonitorSched
   Description: Use to commit deletions of the SysMonitor dataset to the database.
Does NOT support adding or updating of records.
   OperationID: UpdateSysMonitorSched
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateSysMonitorSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSysMonitorSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSysMonitorSched(requestBody:UpdateSysMonitorSched_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateSysMonitorSched_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SysMonitorSvc/UpdateSysMonitorSched", {
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
         resolve(data as UpdateSysMonitorSched_output)
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
      @param sysTaskNum
   */  
export interface CancelTask_input{
      /**  System Task Number to be terminated.  */  
   sysTaskNum:number,
}

export interface CancelTask_output{
}

   /** Required : 
      @param sysRptLstSysRevId
      @param workstationId
      @param sysTaskSysRevId
      @param historyOnly
      @param startedOn
      @param retrieveAllTasks
   */  
export interface CheckForTaskUpdatesKeepIdleTime_input{
      /**  The last Ice.SysRptLst.SysRevId value previously queried. Less than zero if checking not necessary.  */  
   sysRptLstSysRevId:number,
      /**  The workstation identifier.  */  
   workstationId:string,
      /**  The last Ice.SysTask.SysRevId value previously queried. Less than zero if checking not necessary.  */  
   sysTaskSysRevId:number,
      /**  `true` if only completed tasks should be queried. Otherwise, all tasks will be returned.  */  
   historyOnly:boolean,
      /**  The date to start querying from. This should be UTC time.  */  
   startedOn:string,
      /**  `true` if all Ice.SysTask rows should be returned. This can only be used by an administrator.  */  
   retrieveAllTasks:boolean,
}

export interface CheckForTaskUpdatesKeepIdleTime_output{
parameters : {
      /**  output parameters  */  
   newerSysRptLstSysRevId:number,
   newerSysTaskSysRevId:number,
}
}

export interface GetCompanyList_output{
   returnObj:string,
}

   /** Required : 
      @param querySysRptLst
      @param workstationId
      @param querySysTask
      @param querySysTaskLog
      @param historyOnly
      @param startedOn
      @param retrieveAllTasks
   */  
export interface GetMonitorDataKeepIdleTime_input{
      /**  `true` if Ice.SysRptLst rows should be returned.  */  
   querySysRptLst:boolean,
      /**  The workstation identifier.  */  
   workstationId:string,
      /**  `true` if Ice.SysTask rows should be returned.  */  
   querySysTask:boolean,
      /**  `true` if Ice.SysTaskLog rows should be returned.  */  
   querySysTaskLog:boolean,
      /**  `true` if only completed tasks should be queried. Otherwise, all tasks will be returned.  */  
   historyOnly:boolean,
      /**  The UTC date/time to start querying from.  */  
   startedOn:string,
      /**  `true` if all Ice.SysTask rows should be returned. This can only be used by an administrator.  */  
   retrieveAllTasks:boolean,
}

export interface GetMonitorDataKeepIdleTime_output{
   returnObj:Ice_Tablesets_SysMonitorTableset[],
}

   /** Required : 
      @param rptUserID
      @param rptWorkStationID
      @param RetrivalType
      @param interval
   */  
export interface GetReports_input{
      /**  User ID for which you want SysRptLst records.
            Leave this blank to consider all users for available reports.  */  
   rptUserID:string,
      /**  Computer/Workstation name for which you want SysRptLst records.  This an obsolete parameter and will be removed.
            Leave this blank to consider ALL workstations for available reports  */  
   rptWorkStationID:string,
      /**  Retrival type.  */  
   RetrivalType:string,
      /**  Retrival interval  */  
   interval:number,
}

export interface GetReports_output{
   returnObj:Ice_Tablesets_SysMonitorTableset[],
}

   /** Required : 
      @param userIDent
   */  
export interface GetScheduledTasks_input{
      /**  User ID for which you want the schedule tasks.
            Leave blank to consider all users.  */  
   userIDent:string,
}

export interface GetScheduledTasks_output{
   returnObj:Ice_Tablesets_SysMonitorSchedTableset[],
}

   /** Required : 
      @param rptUserID
      @param rptWorkStationID
   */  
export interface GetTReports_input{
      /**  User ID for which you want SysRptLst and SysTask records.
            Leave this blank to consider all users for available reports.  */  
   rptUserID:string,
      /**  Computer/Workstation name for which you want SysRptLst records.
            Leave this blank to consider ALL workstations for available reports  */  
   rptWorkStationID:string,
}

export interface GetTReports_output{
   returnObj:Ice_Tablesets_SysMonitorTableset[],
}

   /** Required : 
      @param taskNumOfDays
      @param rptUserID
   */  
export interface GetTaskHistory_input{
      /**  The number of days from today you wish to retrieve task history for.  */  
   taskNumOfDays:number,
      /**  User ID for which you want SysRptLst and SysTask records.
            Leave this blank to consider all users for available reports.  */  
   rptUserID:string,
}

export interface GetTaskHistory_output{
   returnObj:Ice_Tablesets_SysMonitorTaskHistTableset[],
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

export interface Ice_Tablesets_SysAgentTaskRow{
      /**  System Agent Number  */  
   AgentID:string,
      /**  System Agent Scheduling Number  */  
   AgentSchedNum:number,
      /**  System Agent Task Number  */  
   AgentTaskNum:number,
      /**  System Task Description  */  
   TaskDesc:string,
      /**  Valid Values:  Process, Report  */  
   TaskType:string,
      /**  Run Procedure  */  
   RunProcedure:string,
      /**  Method (internal procedure) of the "RunProcedure" that this task will perform.  */  
   RunMethod:string,
      /**  SubmittedOn  */  
   SubmittedOn:string,
      /**  Submitted by user  */  
   SubmitUser:string,
      /**   Name of .net program which is used to maintain the parameters.
Example: Epicor.Mfg.UI.xx/xxxxxxx.dll  */  
   ParamMaintProgram:string,
      /**  Current Company when the task was created.  */  
   Company:string,
      /**  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  */  
   TaskNote:string,
      /**  ProcessSetSystemCode  */  
   ProcessSetSystemCode:string,
      /**  Unique ID for Process  */  
   ProcessID:string,
      /**  ProcessTask.SysTaskNum that originated the schedule  */  
   ProcessTaskNum:number,
      /**  IsSystemTask  */  
   IsSystemTask:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ProcessSetCompany  */  
   ProcessSetCompany:string,
      /**  Next Run on  */  
   NextRunOn:string,
   SchedDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysMonitorSchedTableset{
   SysAgentTask:Ice_Tablesets_SysAgentTaskRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SysMonitorTableset{
   SysRptLst:Ice_Tablesets_SysRptLstRow[],
   SysTask:Ice_Tablesets_SysTaskRow[],
   SysTaskLog:Ice_Tablesets_SysTaskLogRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SysMonitorTaskHistTableset{
   SysTaskHist:Ice_Tablesets_SysTaskHistRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SysRptLstRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  User ID  */  
   UserID:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  Record Sequence  */  
   RecSeq:number,
      /**  Report Description  */  
   RptDescription:string,
      /**  System Task Number  */  
   SysTaskNum:number,
      /**  Name of Computer on which the file is located.  */  
   HostComputer:string,
      /**  File Name  */  
   FileName:string,
      /**  Pending, Printing, Printed  */  
   RptStatus:string,
      /**  LastActionOn  */  
   LastActionOn:string,
      /**  Last Action  */  
   LastAction:string,
      /**  Name of Printer to use for Auto Print reports  */  
   OutPutToPrinter:string,
      /**  Print, Preview, None  */  
   AutoAction:string,
      /**  Program which calls the print program  */  
   PrintDriver:string,
      /**  Program which performs the actual printing  */  
   PrintProgram:string,
      /**  Name of "client" printer, used for auto print  */  
   PrinterName:string,
      /**  additonal options/settings required by specfic PrintProgram  */  
   PrintProgramOptions:string,
      /**  Report Page Settings  */  
   RptPageSettings:string,
      /**  Report Printer Settings  */  
   RptPrinterSettings:string,
      /**  Report Version  */  
   RptVersion:string,
      /**  Report Output Type  */  
   RptOutPutType:string,
      /**  name of computer/workstation that made the request for this report.  */  
   WorkStationID:string,
      /**  An optional descriptive note about this Report.  This value comes from the report parameter TaskNote field.  */  
   RptNote:string,
      /**  Indicates that this Report has been Archived.  */  
   Archived:boolean,
      /**  Date that this Report will be purged.  */  
   PurgeDate:string,
      /**  Number of lines per page for the specific text report. This was obtained from the XBSyst.TxtLPP..  */  
   TxtLPP:number,
      /**  Fax Subject  */  
   FaxSubject:string,
      /**  Fax To  */  
   FaxTo:string,
      /**  Fax Number  */  
   FaxNumber:string,
      /**  Email To Address  */  
   EMailTo:string,
      /**  Email  to CC  */  
   EMailCC:string,
      /**  Email To BCC  */  
   EMailBCC:string,
      /**  SSRS URL  */  
   SSRSURL:string,
      /**  Field to save if file is going to be exported in txt o xml format  */  
   OutputEDI:string,
      /**  Email Body text  */  
   EMailBody:string,
      /**  Attachment Type  */  
   AttachmentType:string,
      /**  SSRSRenderFormat  */  
   SSRSRenderFormat:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ReportID  */  
   ReportID:string,
      /**  StyleNum  */  
   StyleNum:number,
      /**  UserDescription  */  
   UserDescription:string,
      /**  DesignMode  */  
   DesignMode:string,
      /**  DesignUser  */  
   DesignUser:string,
      /**  DesignVersionLocalFolder  */  
   DesignVersionLocalFolder:string,
      /**  StyleDescription  */  
   StyleDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysTaskHistRow{
      /**  System Task Number  */  
   SysTaskNum:number,
      /**  Task Description  */  
   TaskDescription:string,
      /**   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  */  
   TaskType:string,
      /**  Date-time field that the task Started On in UTC time zone  */  
   StartedOn:string,
      /**  Date-time field that the task Ended On in UTC time zone  */  
   EndedOn:string,
      /**  User who submitrted the task  */  
   SubmitUser:string,
      /**  Values are; Active, Complete, Cancelled, Error.  */  
   TaskStatus:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Task Agent ID  */  
   AgentID:string,
      /**  Task Agent Scheduling Number  */  
   AgentSchedNum:number,
      /**  Task Agent Task Number  */  
   AgentTaskNum:number,
      /**  Run Procedure  */  
   RunProcedure:string,
      /**  Values are "Agent" or "Client".  */  
   InitiatorSource:string,
      /**  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  */  
   ActivityMsg:string,
      /**  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  */  
   History:boolean,
      /**  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  */  
   TaskNote:string,
      /**  LastActivityOn  */  
   LastActivityOn:string,
      /**  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  */  
   UserPIDInfo:string,
      /**  Unique ID for Process  */  
   ProcessID:string,
      /**  IsSystemTask  */  
   IsSystemTask:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ProgressPercent  */  
   ProgressPercent:number,
      /**  EdgeCorrelationID  */  
   EdgeCorrelationID:string,
   ErrorMsg:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysTaskLogRow{
      /**  System Task Number  */  
   SysTaskNum:number,
      /**  Entry Number  */  
   EntryNum:number,
      /**  EnteredOn  */  
   EnteredOn:string,
      /**  Error indicator  */  
   IsError:boolean,
      /**  Message Text  */  
   MsgText:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MsgType  */  
   MsgType:string,
   MsgTypeDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysTaskRow{
      /**  System Task Number  */  
   SysTaskNum:number,
      /**  Task Description  */  
   TaskDescription:string,
      /**   Used to control what program is used to initiate the running of the program that this task is suppose to run.
Example: TextRpt will run Task/TextRpt.p
                 DSRpt will run Task/DataSetRpt.p  */  
   TaskType:string,
      /**  Date-time field that the task Started On in UTC time zone  */  
   StartedOn:string,
      /**  Date-time field that the task Ended On in UTC time zone  */  
   EndedOn:string,
      /**  User who submitrted the task  */  
   SubmitUser:string,
      /**  Values are; Active, Complete, Cancelled, Error.  */  
   TaskStatus:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Task Agent ID  */  
   AgentID:string,
      /**  Task Agent Scheduling Number  */  
   AgentSchedNum:number,
      /**  Task Agent Task Number  */  
   AgentTaskNum:number,
      /**  Run Procedure  */  
   RunProcedure:string,
      /**  Values are "Agent" or "Client".  */  
   InitiatorSource:string,
      /**  A message string that the processing program periodically updates to provide an indication of the activity that it is working on.  */  
   ActivityMsg:string,
      /**  Indicates if this task is considered as Historical. This is primarily used for filtering of records. The System Task monitor will not show records which are marked as History = Yes.  As tasks complete sucessfully this field gets set to Yes. If they happen to have an error, this will be set by the user so they have a chance to acknowledge the error.  */  
   History:boolean,
      /**  An optional descriptive note about this Task.  This value comes from the parameter TaskNote field.  */  
   TaskNote:string,
      /**  LastActivityOn  */  
   LastActivityOn:string,
      /**  AStores the Progess DB connection user number and the appserver Process ID. Very useful when trying to related a task to a progress appserver agent.  */  
   UserPIDInfo:string,
      /**  Unique ID for Process  */  
   ProcessID:string,
      /**  IsSystemTask  */  
   IsSystemTask:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ProgressPercent  */  
   ProgressPercent:number,
      /**  EdgeCorrelationID  */  
   EdgeCorrelationID:string,
   ErrorMsg:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ds
   */  
export interface UpdateSysMonitorDS_input{
   ds:Ice_Tablesets_SysMonitorTableset[],
}

export interface UpdateSysMonitorDS_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SysMonitorTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateSysMonitorSched_input{
   ds:Ice_Tablesets_SysMonitorSchedTableset[],
}

export interface UpdateSysMonitorSched_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SysMonitorSchedTableset,
}
}

