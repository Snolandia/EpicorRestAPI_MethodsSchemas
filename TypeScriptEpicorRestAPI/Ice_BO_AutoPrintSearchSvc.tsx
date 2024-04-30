import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.AutoPrintSearchSvc
// Description: This service is used by the BAM on BPM Data Directives to search for reports for Autoprint.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/$metadata", {
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
   Summary: Invoke method GetRowsAutoPrint
   Description: This method searches for reports that can be set up for AutoPrinting on BAM.
   OperationID: GetRowsAutoPrint
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsAutoPrint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsAutoPrint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsAutoPrint(requestBody:GetRowsAutoPrint_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsAutoPrint_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/GetRowsAutoPrint", {
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
         resolve(data as GetRowsAutoPrint_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListAutoPrint
   Description: This method searches for reports that can be set up for AutoPrinting on BAM.
   OperationID: GetListAutoPrint
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListAutoPrint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListAutoPrint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListAutoPrint(requestBody:GetListAutoPrint_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListAutoPrint_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/GetListAutoPrint", {
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
         resolve(data as GetListAutoPrint_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAutoReportSettings
   Description: Adds a new row in the AutoReport table and returns the parameters for the service.
Invokes GetNewParameters on the service and returns list of parameters that the report expects.
Used by AutoPrint Action setup on BPM Data Directives
   OperationID: GetNewAutoReportSettings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAutoReportSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAutoReportSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAutoReportSettings(requestBody:GetNewAutoReportSettings_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAutoReportSettings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/GetNewAutoReportSettings", {
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
         resolve(data as GetNewAutoReportSettings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLookupForRptCriteriaFilter
   Description: Gets the adapter name and lookup field for the Report criteria filter.
   OperationID: GetLookupForRptCriteriaFilter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLookupForRptCriteriaFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupForRptCriteriaFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLookupForRptCriteriaFilter(requestBody:GetLookupForRptCriteriaFilter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLookupForRptCriteriaFilter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/GetLookupForRptCriteriaFilter", {
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
         resolve(data as GetLookupForRptCriteriaFilter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLookupForBAQReportFilter
   Description: Gets the adapter name and lookup field for the BAQ Report filter.
   OperationID: GetLookupForBAQReportFilter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLookupForBAQReportFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupForBAQReportFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLookupForBAQReportFilter(requestBody:GetLookupForBAQReportFilter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLookupForBAQReportFilter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AutoPrintSearchSvc/GetLookupForBAQReportFilter", {
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
         resolve(data as GetLookupForBAQReportFilter_output)
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
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListAutoPrint_input{
      /**  Where Clause for the search  */  
   whereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListAutoPrint_output{
   returnObj:Ice_Tablesets_AutoPrintSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param reportId
      @param filterName
   */  
export interface GetLookupForBAQReportFilter_input{
      /**  The report identifier.  */  
   reportId:string,
      /**  Name of the filter.  */  
   filterName:string,
}

export interface GetLookupForBAQReportFilter_output{
parameters : {
      /**  output parameters  */  
   adapterName:string,
   lookupField:string,
}
}

   /** Required : 
      @param reportId
      @param reportStyleNum
      @param filterName
   */  
export interface GetLookupForRptCriteriaFilter_input{
      /**  The report identifier.  */  
   reportId:string,
      /**  The report style number.  */  
   reportStyleNum:number,
      /**  Name of the filter.  */  
   filterName:string,
}

export interface GetLookupForRptCriteriaFilter_output{
parameters : {
      /**  output parameters  */  
   adapterName:string,
   lookupField:string,
}
}

   /** Required : 
      @param reportID
      @param styleNum
      @param isBAQReport
      @param reportSettingsDS
   */  
export interface GetNewAutoReportSettings_input{
      /**  Report identifier.  */  
   reportID:string,
      /**  Style number for the report.  */  
   styleNum:number,
      /**  if set to `true` indicates the style points to a BAQ report.  */  
   isBAQReport:boolean,
   reportSettingsDS:Ice_Tablesets_AutoRptSettingsTableset[],
}

export interface GetNewAutoReportSettings_output{
parameters : {
      /**  output parameters  */  
   reportSettingsDS:Ice_Tablesets_AutoRptSettingsTableset,
}
}

   /** Required : 
      @param tableName
      @param systemCode
      @param reportID
      @param reportDesc
      @param reportDataDefID
      @param reportType
      @param reportTableCondition
      @param baqReportID
      @param baqReportDesc
      @param onlyBAQReports
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsAutoPrint_input{
      /**  Name of table that the BPM Data Directive is for  */  
   tableName:string,
      /**  SystemCode of the BAM/BPM table  */  
   systemCode:string,
      /**  ReportID search criteria (used as StartsWith)  */  
   reportID:string,
      /**  Report Description search criteria (used as StartsWith)  */  
   reportDesc:string,
      /**  Report Data Definition ID search criteria (used as StartsWith)  */  
   reportDataDefID:string,
      /**  Report Type search criteria, selected from a dropdown (Base Definition, Crystal,Outbound EDI, Epicor Financial Report, Bartender Labels, SQL Server Reporting)  */  
   reportType:string,
      /**  Report table search criteria, selected from a dropdown (IsPrimaryOnReport/1[tableName] is Primary on Report, IsSecondaryOnReport/2=[tableName] is not Primary on Report, IsUsedOnReport/3=[tableName] is used on Report at any level, None/0=(Search for all reports, irrespective of table used)  */  
   reportTableCondition:number,
      /**  BAQ Report ID (used as StartsWith)  */  
   baqReportID:string,
      /**  BAQ Report Description (used as StartsWith)  */  
   baqReportDesc:string,
      /**  Only search for BAQ reports  */  
   onlyBAQReports:boolean,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsAutoPrint_output{
   returnObj:Ice_Tablesets_AutoPrintSearchTableset[],
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

export interface Ice_Tablesets_AutoPrintSearchRow{
      /**  Report ID from Ice.Report  */  
   ReportID:string,
      /**  Report Data Definition's Description  */  
   ReportDescription:string,
      /**  Report Type from ReportStyle.RptTypeID  */  
   ReportTypeID:string,
      /**  Report Data Definition ID  */  
   ReportDataDefinitionID:string,
      /**  BAQReport ID from BAQReport.BAQRptID  */  
   BAQReportID:string,
      /**  BAQ Report's Description from BAQReport.Description  */  
   BAQReportDescription:string,
      /**  Style Description from ReportStyle.RptDescription  */  
   StyleDescription:string,
      /**  Style Num from ReportStyle.StyleNum  */  
   StyleNum:number,
      /**  Indicates if search result row represents a BAQ Report  */  
   IsBAQReport:boolean,
      /**  Is SystemRpt from ReportStyle.SystemRpt  */  
   SystemRpt:boolean,
      /**  BO that handles the report  */  
   AutoProgram:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AutoPrintSearchTableset{
   AutoPrintSearch:Ice_Tablesets_AutoPrintSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_AutoReportRow{
      /**  BO that handles the report  */  
   AutoProgram:string,
      /**  Report ID from Ice.Report  */  
   ReportID:string,
      /**  Report style description  */  
   StyleDescription:string,
      /**  Data Definition ID  */  
   ReportDataDefinitionID:string,
      /**  Report Type  */  
   ReportTypeID:string,
      /**  Indicates if this represents a BAQ Report  */  
   IsBAQReport:boolean,
      /**  Task Note  */  
   TaskNote:string,
      /**  When to run report - Immediate, Queued  */  
   RunSchedule:string,
      /**  Printer settings merged into one string  */  
   PrinterSettings:string,
      /**  Report Page Settings as a string  */  
   PageSettings:string,
      /**  Printer Name  */  
   PrinterName:string,
      /**  Report.RptDescription  */  
   ReportDescription:string,
      /**   Printer Selection: 'SEL' or 'NEW'
Indicates if user selected a predefined printer from AutoPrinter combo or they set up a new one on the form.  */  
   PrintSel:string,
      /**  Printer selected by the user via the Print dialog instead of the combo  */  
   NewPrinterName:string,
      /**   Printer quantity radio button selection. If Quantity comes from a constant or from a table.field
Values: "CONS", "DYN"  */  
   PrintQtySel:string,
      /**  Constant value selected for Print Quantity  */  
   PrintQtyConstant:number,
      /**  Table name if Print Quantity is dynamic  */  
   PrintQtyTableName:string,
      /**  Column from which dynamic Print Qty is taken  */  
   PrintQtyColumnName:string,
      /**  Printer action: Print, Preview  */  
   PrintAction:string,
      /**  StyleNum  */  
   StyleNum:number,
      /**  Default SysAgent ID  */  
   DefaultSysAgentID:string,
      /**  This field stores the type name of the Tableset that GetNewParameters returns. It will be used in BPM later to instantiate the report parameters tableset.  */  
   ParametersTablesetType:string,
      /**  SysAgent.SysPassword  */  
   SysAgentPwd:string,
      /**  SysAgent.SysUserID  */  
   SysAgentUserID:string,
      /**  Output format selected by user for SSRS reports  */  
   OutputFormat:string,
      /**  Printer Settings for the client side printer  */  
   NewPrinterSettings:string,
      /**  Page Settings for the client side printer  */  
   NewPageSettings:string,
      /**  Maps to the SSRSEnableRouting report parameter. If enabled, sets the report parameter value.  */  
   SSRSEnableRouting:boolean,
      /**  Indicates if this represents a Dynamic Criteria Report  */  
   IsDynamicCriteriaReport:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AutoRptParametersRow{
      /**  Name of the Parameter  */  
   ParameterName:string,
      /**  Data type of parameter  */  
   ParameterType:string,
      /**  User selected prompt  */  
   ParameterAction:string,
      /**  Report ID  */  
   ReportID:string,
      /**  Type of action selected by user:
        TableField=0, Constant=1, BAQConstant=2, Expression=3,BPMCallContext=4,None=5  */  
   ActionType:number,
      /**  Label for the parameter to display on the AutoPrint settings dialog,  */  
   ParameterLabel:string,
      /**  Indicates if this represents a Report Criteria Set's Prompt or Filter (for dynamic criteria reports). These are not submitted directly, they are built into a XML document.  */  
   IsCriteria:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AutoRptSettingsTableset{
   AutoReport:Ice_Tablesets_AutoReportRow[],
   AutoRptParameters:Ice_Tablesets_AutoRptParametersRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

