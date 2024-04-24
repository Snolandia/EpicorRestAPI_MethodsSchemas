import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.ReportMonitorSvc
// Description: The report monitor service used by System Monitor.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get ReportMonitors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReportMonitors
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysRptLstRow
   */  
export function get_ReportMonitors(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysRptLstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/ReportMonitors", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysRptLstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReportMonitors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysRptLstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysRptLstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReportMonitors(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/ReportMonitors", {
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
   Summary: Calls GetByID to retrieve the ReportMonitor item
   Description: Calls GetByID to retrieve the ReportMonitor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportMonitor
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CreatedOn Desc: CreatedOn   Required: True   Allow empty value : True
      @param RecSeq Desc: RecSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysRptLstRow
   */  
export function get_ReportMonitors_WorkStationID_Company_CreatedOn_RecSeq(WorkStationID:string, Company:string, CreatedOn:string, RecSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SysRptLstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/ReportMonitors(" + WorkStationID + "," + Company + "," + CreatedOn + "," + RecSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SysRptLstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ReportMonitor for the service
   Description: Calls UpdateExt to update ReportMonitor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReportMonitor
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CreatedOn Desc: CreatedOn   Required: True   Allow empty value : True
      @param RecSeq Desc: RecSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysRptLstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ReportMonitors_WorkStationID_Company_CreatedOn_RecSeq(WorkStationID:string, Company:string, CreatedOn:string, RecSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/ReportMonitors(" + WorkStationID + "," + Company + "," + CreatedOn + "," + RecSeq + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete ReportMonitor item
   Description: Call UpdateExt to delete ReportMonitor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReportMonitor
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CreatedOn Desc: CreatedOn   Required: True   Allow empty value : True
      @param RecSeq Desc: RecSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ReportMonitors_WorkStationID_Company_CreatedOn_RecSeq(WorkStationID:string, Company:string, CreatedOn:string, RecSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/ReportMonitors(" + WorkStationID + "," + Company + "," + CreatedOn + "," + RecSeq + ")", {
          method: 'delete',
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
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysRptLstListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysRptLstListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysRptLstListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseSysRptLst:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSysRptLst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSysRptLst=" + whereClauseSysRptLst
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetRows" + params, {
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

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(workStationID:string, company:string, createdOn:string, recSeq:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof workStationID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "workStationID=" + workStationID
   }
   if(typeof company!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "company=" + company
   }
   if(typeof createdOn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "createdOn=" + createdOn
   }
   if(typeof recSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "recSeq=" + recSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetByID" + params, {
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

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetList" + params, {
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

   /**  
   Summary: Invoke method GetReportData
   Description: Get a report's data from the server
   OperationID: GetReportData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetReportData", {
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
   Summary: Invoke method GetReportDefinition
   Description: Get a report's data from the server
   OperationID: GetReportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportDefinition(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetReportDefinition", {
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
   Summary: Invoke method GetRowsKeepIdleTime
   Description: This method reverts the last used time so that we don't prevent
time-out from working. After that call base GetRows.
   OperationID: GetRowsKeepIdleTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsKeepIdleTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsKeepIdleTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsKeepIdleTime(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetRowsKeepIdleTime", {
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
   Summary: Invoke method GetRowsKeepIdleTimeWithBallonInfo
   Description: Retrieves rows along with balloon data.
   OperationID: GetRowsKeepIdleTimeWithBallonInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsKeepIdleTimeWithBallonInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsKeepIdleTimeWithBallonInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsKeepIdleTimeWithBallonInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetRowsKeepIdleTimeWithBallonInfo", {
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
   Summary: Invoke method GetReportBytes
   Description: Gets the report bytes.
   OperationID: GetReportBytes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportBytes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportBytes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportBytes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetReportBytes", {
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
   Summary: Invoke method GetDataExportBytes
   Description: Gets the bytes of exported data.
   OperationID: GetDataExportBytes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataExportBytes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataExportBytes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataExportBytes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetDataExportBytes", {
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
   Summary: Invoke method GetReportBytesAsExcel
   Description: Gets the Financial report in Excel format as bytes.
   OperationID: GetReportBytesAsExcel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportBytesAsExcel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportBytesAsExcel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportBytesAsExcel(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetReportBytesAsExcel", {
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
   Summary: Invoke method GetNewSysRptLst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysRptLst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysRptLst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysRptLst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSysRptLst(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetNewSysRptLst", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetBySysRowID" + params, {
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

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/GetBySysRowIDs" + params, {
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

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysRptLstListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SysRptLstListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysRptLstRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SysRptLstRow[],
}

export interface Ice_Tablesets_SysRptLstListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  User ID  */  
   "UserID":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  Record Sequence  */  
   "RecSeq":number,
      /**  Report Description  */  
   "RptDescription":string,
      /**  System Task Number  */  
   "SysTaskNum":number,
      /**  Name of Computer on which the file is located.  */  
   "HostComputer":string,
      /**  File Name  */  
   "FileName":string,
      /**  Pending, Printing, Printed  */  
   "RptStatus":string,
      /**  LastActionOn  */  
   "LastActionOn":string,
      /**  Last Action  */  
   "LastAction":string,
      /**  Name of Printer to use for Auto Print reports  */  
   "OutPutToPrinter":string,
      /**  Print, Preview, None  */  
   "AutoAction":string,
      /**  Program which calls the print program  */  
   "PrintDriver":string,
      /**  Program which performs the actual printing  */  
   "PrintProgram":string,
      /**  Name of "client" printer, used for auto print  */  
   "PrinterName":string,
      /**  additonal options/settings required by specfic PrintProgram  */  
   "PrintProgramOptions":string,
      /**  Report Page Settings  */  
   "RptPageSettings":string,
      /**  Report Printer Settings  */  
   "RptPrinterSettings":string,
      /**  Report Version  */  
   "RptVersion":string,
      /**  Report Output Type  */  
   "RptOutPutType":string,
      /**  name of computer/workstation that made the request for this report.  */  
   "WorkStationID":string,
      /**  An optional descriptive note about this Report.  This value comes from the report parameter TaskNote field.  */  
   "RptNote":string,
      /**  Indicates that this Report has been Archived.  */  
   "Archived":boolean,
      /**  Date that this Report will be purged.  */  
   "PurgeDate":string,
      /**  Number of lines per page for the specific text report. This was obtained from the XBSyst.TxtLPP..  */  
   "TxtLPP":number,
      /**  Fax Subject  */  
   "FaxSubject":string,
      /**  Fax To  */  
   "FaxTo":string,
      /**  Fax Number  */  
   "FaxNumber":string,
      /**  Email To Address  */  
   "EMailTo":string,
      /**  Email  to CC  */  
   "EMailCC":string,
      /**  Email To BCC  */  
   "EMailBCC":string,
      /**  SSRS URL  */  
   "SSRSURL":string,
      /**  Field to save if file is going to be exported in txt o xml format  */  
   "OutputEDI":string,
      /**  Email Body text  */  
   "EMailBody":string,
      /**  Attachment Type  */  
   "AttachmentType":string,
      /**  SSRSRenderFormat  */  
   "SSRSRenderFormat":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_SysRptLstRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  User ID  */  
   "UserID":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  Record Sequence  */  
   "RecSeq":number,
      /**  Report Description  */  
   "RptDescription":string,
      /**  System Task Number  */  
   "SysTaskNum":number,
      /**  Name of Computer on which the file is located.  */  
   "HostComputer":string,
      /**  File Name  */  
   "FileName":string,
      /**  Pending, Printing, Printed  */  
   "RptStatus":string,
      /**  LastActionOn  */  
   "LastActionOn":string,
      /**  Last Action  */  
   "LastAction":string,
      /**  Name of Printer to use for Auto Print reports  */  
   "OutPutToPrinter":string,
      /**  Print, Preview, None  */  
   "AutoAction":string,
      /**  Program which calls the print program  */  
   "PrintDriver":string,
      /**  Program which performs the actual printing  */  
   "PrintProgram":string,
      /**  Name of "client" printer, used for auto print  */  
   "PrinterName":string,
      /**  additonal options/settings required by specfic PrintProgram  */  
   "PrintProgramOptions":string,
      /**  Report Page Settings  */  
   "RptPageSettings":string,
      /**  Report Printer Settings  */  
   "RptPrinterSettings":string,
      /**  Report Version  */  
   "RptVersion":string,
      /**  Report Output Type  */  
   "RptOutPutType":string,
      /**  name of computer/workstation that made the request for this report.  */  
   "WorkStationID":string,
      /**  An optional descriptive note about this Report.  This value comes from the report parameter TaskNote field.  */  
   "RptNote":string,
      /**  Indicates that this Report has been Archived.  */  
   "Archived":boolean,
      /**  Date that this Report will be purged.  */  
   "PurgeDate":string,
      /**  Number of lines per page for the specific text report. This was obtained from the XBSyst.TxtLPP..  */  
   "TxtLPP":number,
      /**  Fax Subject  */  
   "FaxSubject":string,
      /**  Fax To  */  
   "FaxTo":string,
      /**  Fax Number  */  
   "FaxNumber":string,
      /**  Email To Address  */  
   "EMailTo":string,
      /**  Email  to CC  */  
   "EMailCC":string,
      /**  Email To BCC  */  
   "EMailBCC":string,
      /**  SSRS URL  */  
   "SSRSURL":string,
      /**  Field to save if file is going to be exported in txt o xml format  */  
   "OutputEDI":string,
      /**  Email Body text  */  
   "EMailBody":string,
      /**  Attachment Type  */  
   "AttachmentType":string,
      /**  SSRSRenderFormat  */  
   "SSRSRenderFormat":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ReportID  */  
   "ReportID":string,
      /**  StyleNum  */  
   "StyleNum":number,
      /**  UserDescription  */  
   "UserDescription":string,
      /**  DesignMode  */  
   "DesignMode":string,
      /**  DesignUser  */  
   "DesignUser":string,
      /**  DesignVersionLocalFolder  */  
   "DesignVersionLocalFolder":string,
      /**  StyleDescription  */  
   "StyleDescription":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param workStationID
      @param company
      @param createdOn
      @param recSeq
   */  
export interface DeleteByID_input{
   workStationID:string,
   company:string,
   createdOn:string,
   recSeq:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param workStationID
      @param company
      @param createdOn
      @param recSeq
   */  
export interface GetByID_input{
   workStationID:string,
   company:string,
   createdOn:string,
   recSeq:number,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_ReportMonitorTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_ReportMonitorTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_ReportMonitorTableset[],
}

   /** Required : 
      @param sysRowId
   */  
export interface GetDataExportBytes_input{
      /**  The system row identifier.  */  
   sysRowId:string,
}

export interface GetDataExportBytes_output{
      /**  The bytes of the exported data.  */  
   returnObj:string,
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Ice_Tablesets_SysRptLstListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param workStationID
      @param company
      @param createdOn
   */  
export interface GetNewSysRptLst_input{
   ds:Ice_Tablesets_ReportMonitorTableset[],
   workStationID:string,
   company:string,
   createdOn:string,
}

export interface GetNewSysRptLst_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ReportMonitorTableset[],
}
}

   /** Required : 
      @param sysRowId
      @param currencyInfoList
   */  
export interface GetReportBytesAsExcel_input{
      /**  The system row identifier  */  
   sysRowId:string,
      /**  List of currency code and DecimalsGeneral value for current company  */  
   currencyInfoList:any,      //schema had no properties on an object.
}

export interface GetReportBytesAsExcel_output{
      /**  The bytes for the rendered report in excel format  */  
   returnObj:string,
}

   /** Required : 
      @param sysRowId
   */  
export interface GetReportBytes_input{
      /**  The system row identifier.  */  
   sysRowId:string,
}

export interface GetReportBytes_output{
      /**  The bytes for the rendered report.  */  
   returnObj:string,
}

   /** Required : 
      @param sysRowID
   */  
export interface GetReportData_input{
      /**  The row ID of the report to get the data for  */  
   sysRowID:string,
}

export interface GetReportData_output{
   returnObj:Ice_Tablesets_ReportDataTableset[],
}

   /** Required : 
      @param sysRowID
   */  
export interface GetReportDefinition_input{
      /**  The row ID of the report to get the data for  */  
   sysRowID:string,
}

export interface GetReportDefinition_output{
   returnObj:Ice_Tablesets_ReportDataTableset[],
}

   /** Required : 
      @param whereClauseSysRptLst
      @param getBallonInfo
      @param whereClauseSysTask
      @param whereClauseSysTaskLog
      @param sysMonitorData
   */  
export interface GetRowsKeepIdleTimeWithBallonInfo_input{
      /**  The where clause to restrict data for  */  
   whereClauseSysRptLst:string,
      /**  Include balloon info if true  */  
   getBallonInfo:boolean,
   whereClauseSysTask:string,
   whereClauseSysTaskLog:string,
   sysMonitorData:any,      //schema had no properties on an object.
}

export interface GetRowsKeepIdleTimeWithBallonInfo_output{
   returnObj:Ice_Tablesets_ReportMonitorTableset[],
parameters : {
      /**  output parameters  */  
   sysMonitorData: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param whereClauseSysRptLst
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsKeepIdleTime_input{
      /**  The where clause to restrict data for  */  
   whereClauseSysRptLst:string,
      /**  The page size  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetRowsKeepIdleTime_output{
   returnObj:Ice_Tablesets_ReportMonitorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseSysRptLst
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSysRptLst:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_ReportMonitorTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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

export interface Ice_Tablesets_ReportDataRow{
   Sequence:number,
   Data:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ReportDataTableset{
   ReportData:Ice_Tablesets_ReportDataRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ReportMonitorTableset{
   SysRptLst:Ice_Tablesets_SysRptLstRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SysRptLstListRow{
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
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SysRptLstListTableset{
   SysRptLstList:Ice_Tablesets_SysRptLstListRow[],
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

export interface Ice_Tablesets_UpdExtReportMonitorTableset{
   SysRptLst:Ice_Tablesets_SysRptLstRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtReportMonitorTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtReportMonitorTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_ReportMonitorTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ReportMonitorTableset[],
}
}

