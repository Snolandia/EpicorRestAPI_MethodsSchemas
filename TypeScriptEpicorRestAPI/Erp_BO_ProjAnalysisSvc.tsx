import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ProjAnalysisSvc
// Description: Project Analysis Business Object
           Temporary data tables are used to allow export/import of
           projects to/from MS Project.  Public methods are also
           available to build/delete Project Analyis data.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/$metadata", {
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
   Summary: Invoke method BuildAnalysis
   Description: Call this method when the user already selected project(s) to process.
This method expects a LIST-DELIM delimited string of RowIds of all selected
Project records.
   OperationID: BuildAnalysis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAnalysis_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAnalysis_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildAnalysis(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/BuildAnalysis", {
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
   Summary: Invoke method ClearAnalysis
   Description: Call this method to delete or clear all ProjectAnalysis records.
This method expects that the user already confirmed that records will be deleted.
   OperationID: ClearAnalysis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearAnalysis_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAnalysis_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearAnalysis(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/ClearAnalysis", {
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
   Summary: Invoke method DefaultPctComplete
   Description: Get the default Download % Complete code before passing the input parameters
for the Project Download to MS Project.  Call this method before the user
manipulate the MSP Download input parameters.  This method will return the
default value for PctComplete variable.
   OperationID: DefaultPctComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultPctComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultPctComplete(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/DefaultPctComplete", {
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
   Summary: Invoke method GetByProjectID
   Description: This method finds the Project record by ProjectId.
   OperationID: GetByProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByProjectID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/GetByProjectID", {
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
   Summary: Invoke method GetProjectBrw
   Description: This method assembles the Project browse for the main data set.
   OperationID: GetProjectBrw
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetProjectBrw_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProjectBrw_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetProjectBrw(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/GetProjectBrw", {
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
   Summary: Invoke method ProcessMSPDownload
   Description: This method performs the actual Project Download to MS Project.  Call this
method after the user selected the Project and entered the necessary input
parameters. This method returns the data table ttMSPDownload containing all
appropriate project information. The resulting records from the ttMSPDownload
will then need to be outputted as a CSV file (comma delimited).
   OperationID: ProcessMSPDownload
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessMSPDownload_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessMSPDownload_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessMSPDownload(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/ProcessMSPDownload", {
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
   Summary: Invoke method ProcessMSPUpload
   Description: This method performs the actual Project Upload from MS Project.  Call this
method after the user selected the Project and entered the necessary input
parameters. This method expects an input data table ttMSPUpload with data
coming from an external comma delimited file.  The ttMSPUpload table should
only contain data (i.e. if the first line of the external file is just the
field descriptions then this record should not be included in ttMSPUpload.)
   OperationID: ProcessMSPUpload
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessMSPUpload_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessMSPUpload_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessMSPUpload(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjAnalysisSvc/ProcessMSPUpload", {
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
      @param ipGuidList
   */  
export interface BuildAnalysis_input{
      /**  A RowId list of selected Project records.  */  
   ipGuidList:string,
}

export interface BuildAnalysis_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipProjectID
   */  
export interface ClearAnalysis_input{
      /**  ProjectID  */  
   ipProjectID:string,
}

export interface ClearAnalysis_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

export interface DefaultPctComplete_output{
parameters : {
      /**  output parameters  */  
   vPctComplete:string,
}
}

export interface Erp_Tablesets_MSPDownloadRow{
      /**  Name  */  
   Name:string,
      /**  Outline Level  */  
   Level:number,
      /**  Start  */  
   StartDate:string,
      /**  Duration  */  
   Duration:string,
      /**  % Complete  */  
   PctComplete:number,
      /**  Resource Group  */  
   ResGroup:string,
      /**  Resource Names  */  
   ResName:string,
      /**  Predecessors  */  
   Predecessors:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MSPDownloadTableset{
   MSPDownload:Erp_Tablesets_MSPDownloadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MSPUploadRow{
      /**  Upload ID  */  
   KeyID:string,
      /**  Contains the key codes for upload: TableName and Key ID  */  
   KeyName:string,
      /**  Outline Level  */  
   Outline:number,
      /**  Start Date  */  
   StartDate:string,
      /**  Finish Date  */  
   FinishDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MSPUploadTableset{
   MSPUpload:Erp_Tablesets_MSPUploadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ProjAnalysisTableset{
   ProjectBrw:Erp_Tablesets_ProjectBrwRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ProjectBrwRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Full description of Project Management Code.  */  
   Description:string,
      /**  Indicates if this Project is active.  Can be changed directly by the user during entry.  */  
   ActiveProject:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipProjectID
   */  
export interface GetByProjectID_input{
      /**  The Project ID  */  
   ipProjectID:string,
}

export interface GetByProjectID_output{
   returnObj:Erp_Tablesets_ProjAnalysisTableset[],
}

   /** Required : 
      @param whereClauseProject
      @param pageSize
      @param absolutePage
   */  
export interface GetProjectBrw_input{
      /**  Where clause to specify set of ProjectBrw records to return  */  
   whereClauseProject:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetProjectBrw_output{
   returnObj:Erp_Tablesets_ProjAnalysisTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
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
      @param ipProjectID
      @param ipPctComplete
      @param ipPredecessors
      @param ipTasks
      @param ipPhases
      @param ipJobs
      @param ipJobAsm
      @param ipJobOper
      @param ipDuration
   */  
export interface ProcessMSPDownload_input{
      /**  The project ID of the selected Project.  */  
   ipProjectID:string,
      /**  The Download Percent Complete code.  */  
   ipPctComplete:string,
      /**  Include Predecessors in the download.  */  
   ipPredecessors:boolean,
      /**  Include Tasks in the download.  */  
   ipTasks:boolean,
      /**  Include Phases in the download.  */  
   ipPhases:boolean,
      /**  Include Jobs in the download.  */  
   ipJobs:boolean,
      /**  Include Job Assemblies in the download.  */  
   ipJobAsm:boolean,
      /**  Include Job Operations in the download.  */  
   ipJobOper:boolean,
      /**  The operation duration unit (Days or Hours).  */  
   ipDuration:string,
}

export interface ProcessMSPDownload_output{
   returnObj:Erp_Tablesets_MSPDownloadTableset[],
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipProjectID
      @param ipPhases
      @param ipTasks
      @param ipProjJobs
      @param ipPhaseTasks
      @param ipPhaseJobs
      @param ipPhaseStart
      @param ipPhaseEnd
      @param ipTaskStart
      @param ipTaskEnd
      @param ipJobStart
      @param ipJobEnd
      @param ds
   */  
export interface ProcessMSPUpload_input{
      /**  The project ID of the selected Project.  */  
   ipProjectID:string,
      /**  Indicates if Phases should be created.  */  
   ipPhases:boolean,
      /**  Indicates if Tasks should be created.  */  
   ipTasks:boolean,
      /**  Indicates if Project and Job links should be updated.  */  
   ipProjJobs:boolean,
      /**  Indicates if Phase and Task links should be updated.  */  
   ipPhaseTasks:boolean,
      /**  Indicates if Phase and Job links should be updated.  */  
   ipPhaseJobs:boolean,
      /**  Indicates if Phase Start Date should be updated.  */  
   ipPhaseStart:boolean,
      /**  Indicates if Phase End Date should be updated.  */  
   ipPhaseEnd:boolean,
      /**  Indicates if Task Start Date should be updated.  */  
   ipTaskStart:boolean,
      /**  Indicates if Task End Date should be updated.  */  
   ipTaskEnd:boolean,
      /**  Indicates if Job Start Date should be updated.  */  
   ipJobStart:boolean,
      /**  Indicates if Job End Date should be updated.  */  
   ipJobEnd:boolean,
   ds:Erp_Tablesets_MSPUploadTableset[],
}

export interface ProcessMSPUpload_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MSPUploadTableset[],
   opMessage:string,
}
}

