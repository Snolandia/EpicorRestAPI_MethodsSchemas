import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.SsrsReportAnalyzerSvc
// Description: Analyzes SSRS reports for a specific report style.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SsrsReportAnalyzerSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SsrsReportAnalyzerSvc/$metadata", {
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
   Summary: Invoke method SummarizeReportAnalysis
   Description: Analyzes all reports and summarizes the results.
   OperationID: SummarizeReportAnalysis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SummarizeReportAnalysis_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SummarizeReportAnalysis(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SsrsReportAnalyzerSvc/SummarizeReportAnalysis", {
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
   Summary: Invoke method AnalyzeReportDataDefinition
   Description: Analyzes the report data definition analyzing all report styles that use the definition.
   OperationID: AnalyzeReportDataDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AnalyzeReportDataDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AnalyzeReportDataDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AnalyzeReportDataDefinition(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SsrsReportAnalyzerSvc/AnalyzeReportDataDefinition", {
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
   Summary: Invoke method AnalyzeReportStyle
   Description: Analyzes the report style.
   OperationID: AnalyzeReportStyle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AnalyzeReportStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AnalyzeReportStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AnalyzeReportStyle(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.SsrsReportAnalyzerSvc/AnalyzeReportStyle", {
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
      @param reportDefinitionId
   */  
export interface AnalyzeReportDataDefinition_input{
      /**  The report definition identifier.  */  
   reportDefinitionId:string,
}

export interface AnalyzeReportDataDefinition_output{
   returnObj:Ice_Tablesets_SsrsReportAnalyzerTableset[],
}

   /** Required : 
      @param reportId
      @param styleNum
   */  
export interface AnalyzeReportStyle_input{
      /**  The report identifier.  */  
   reportId:string,
      /**  The style number.  */  
   styleNum:number,
}

export interface AnalyzeReportStyle_output{
   returnObj:Ice_Tablesets_SsrsReportAnalyzerTableset[],
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

export interface Ice_Tablesets_AnalyzerResultsRow{
   IssueText:string,
   IssueType:number,
   ReportDataDefinition:string,
   ReportPath:string,
   Sequence:number,
   TableName:string,
   ColumnName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SsrsReportAnalyzerTableset{
   AnalyzerResults:Ice_Tablesets_AnalyzerResultsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface SummarizeReportAnalysis_output{
   returnObj:Ice_Tablesets_SsrsReportAnalyzerTableset[],
}

