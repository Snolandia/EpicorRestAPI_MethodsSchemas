import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.SsrsReportDesignSvc
// Description: This business object is designed to take care of SSRS Report Designer functionality.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/$metadata", {
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
   Description: Get SsrsReportDesigns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SsrsReportDesigns
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SsrsSysRptLstRow
   */  
export function get_SsrsReportDesigns(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SsrsSysRptLstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/SsrsReportDesigns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SsrsSysRptLstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SsrsReportDesigns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SsrsSysRptLstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SsrsSysRptLstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SsrsReportDesigns(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/SsrsReportDesigns", {
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
   Summary: Calls GetByID to retrieve the SsrsReportDesign item
   Description: Calls GetByID to retrieve the SsrsReportDesign item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SsrsReportDesign
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CreatedOn Desc: CreatedOn   Required: True   Allow empty value : True
      @param RecSeq Desc: RecSeq   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SsrsSysRptLstRow
   */  
export function get_SsrsReportDesigns_WorkStationID_Company_CreatedOn_RecSeq(WorkStationID:string, Company:string, CreatedOn:string, RecSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_SsrsSysRptLstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/SsrsReportDesigns(" + WorkStationID + "," + Company + "," + CreatedOn + "," + RecSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_SsrsSysRptLstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SsrsReportDesign for the service
   Description: Calls UpdateExt to update SsrsReportDesign. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SsrsReportDesign
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CreatedOn Desc: CreatedOn   Required: True   Allow empty value : True
      @param RecSeq Desc: RecSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SsrsSysRptLstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SsrsReportDesigns_WorkStationID_Company_CreatedOn_RecSeq(WorkStationID:string, Company:string, CreatedOn:string, RecSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/SsrsReportDesigns(" + WorkStationID + "," + Company + "," + CreatedOn + "," + RecSeq + ")", {
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
   Summary: Call UpdateExt to delete SsrsReportDesign item
   Description: Call UpdateExt to delete SsrsReportDesign item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SsrsReportDesign
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
export function delete_SsrsReportDesigns_WorkStationID_Company_CreatedOn_RecSeq(WorkStationID:string, Company:string, CreatedOn:string, RecSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/SsrsReportDesigns(" + WorkStationID + "," + Company + "," + CreatedOn + "," + RecSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SsrsSysRptLstListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SsrsSysRptLstListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SsrsSysRptLstListRow)
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
export function get_GetRows(whereClauseSsrsSysRptLst:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSsrsSysRptLst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSsrsSysRptLst=" + whereClauseSsrsSysRptLst
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/GetRows" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/GetList" + params, {
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
   Summary: Invoke method DownloadAndDesignReportDefinition
   Description: Download all SSRS Report Definitions associated with Report Style as a compressed zip and sets the SysRptLst row to Active
   OperationID: DownloadAndDesignReportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadAndDesignReportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadAndDesignReportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DownloadAndDesignReportDefinition(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/DownloadAndDesignReportDefinition", {
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
   Summary: Invoke method ExportToFile
   Description: Download all SSRS Report Definitions associated with Report Style as a compressed zip and sets the SysRptLst row to Active
   OperationID: ExportToFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportToFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportToFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportToFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/ExportToFile", {
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
   Summary: Invoke method GetAvailableDocumentTypes
   Description: Create list of document type output formats
   OperationID: GetAvailableDocumentTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableDocumentTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableDocumentTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/GetAvailableDocumentTypes", {
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
   Summary: Invoke method UploadAndRenderDesign
   Description: Upload the Report Definitions and render the report in the given format
   OperationID: UploadAndRenderDesign
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadAndRenderDesign_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadAndRenderDesign_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadAndRenderDesign(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/UploadAndRenderDesign", {
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
   Summary: Invoke method CommitAndPublish
   Description: Commit and Publish the Report Definition to the ReportStyle location defined.
   OperationID: CommitAndPublish
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitAndPublish_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitAndPublish_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CommitAndPublish(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/CommitAndPublish", {
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
   Summary: Invoke method UploadAndRenderDesignSsrsReportZip
   Description: Upload the Report Definitions and render the report in the given format
   OperationID: UploadAndRenderDesignSsrsReportZip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadAndRenderDesignSsrsReportZip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadAndRenderDesignSsrsReportZip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadAndRenderDesignSsrsReportZip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/UploadAndRenderDesignSsrsReportZip", {
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
   Summary: Invoke method CommitAndPublishSsrsReportZip
   Description: Commit and Publish the Report Definition to the ReportStyle location defined.
   OperationID: CommitAndPublishSsrsReportZip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitAndPublishSsrsReportZip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitAndPublishSsrsReportZip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CommitAndPublishSsrsReportZip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/CommitAndPublishSsrsReportZip", {
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
   Summary: Invoke method CancelDesign
   Description: Cancel the Design removing the design Report Definition from the Report Server
   OperationID: CancelDesign
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelDesign_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelDesign_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelDesign(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/CancelDesign", {
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
   Summary: Invoke method GenerateData
   Description: Generates the report data again using the same parameters. N.B. This method can only be used before the SysTask row is purged
The existing SysRptLst row design status will be cancelled and the new SysRptLst row will become active
   OperationID: GenerateData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/GenerateData", {
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
   Summary: Invoke method DownloadData
   Description: Download the Report Data from the Report Database as Json
   OperationID: DownloadData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DownloadData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/DownloadData", {
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
   Summary: Invoke method GetNewSsrsSysRptLst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSsrsSysRptLst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSsrsSysRptLst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSsrsSysRptLst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSsrsSysRptLst(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/GetNewSsrsSysRptLst", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SsrsReportDesignSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SsrsSysRptLstListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SsrsSysRptLstListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SsrsSysRptLstRow{
   "odatametadata":string,
   "value":Ice_Tablesets_SsrsSysRptLstRow[],
}

export interface Ice_Tablesets_SsrsSysRptLstListRow{
      /**  User ID  */  
   "UserID":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  Record Sequence  */  
   "RecSeq":number,
      /**  Report Description  */  
   "RptDescription":string,
      /**  Program which performs the actual printing  */  
   "PrintProgram":string,
      /**  Date that this Report will be purged.  */  
   "PurgeDate":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ReportID  */  
   "ReportID":string,
      /**  StyleNum  */  
   "StyleNum":number,
      /**  DesignMode  */  
   "DesignMode":string,
      /**  DesignUser  */  
   "DesignUser":string,
      /**  StyleDescription  */  
   "StyleDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_SsrsSysRptLstRow{
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
   "DesignRenderFormat":string,
   "RptDefID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param sysRowID
   */  
export interface CancelDesign_input{
   sysRowID:string,
}

export interface CancelDesign_output{
}

   /** Required : 
      @param sysRowID
   */  
export interface CommitAndPublishSsrsReportZip_input{
   sysRowID:string,
}

export interface CommitAndPublishSsrsReportZip_output{
}

   /** Required : 
      @param sysRowID
      @param compressedReportDefinitions
   */  
export interface CommitAndPublish_input{
   sysRowID:string,
   compressedReportDefinitions:string,
}

export interface CommitAndPublish_output{
}

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
      @param ts
      @param sysRowID
      @param localFolder
   */  
export interface DownloadAndDesignReportDefinition_input{
   ts:Ice_Tablesets_SsrsReportDesignTableset[],
   sysRowID:string,
   localFolder:string,
}

export interface DownloadAndDesignReportDefinition_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ts:Ice_Tablesets_SsrsReportDesignTableset[],
}
}

   /** Required : 
      @param sysRowID
   */  
export interface DownloadData_input{
   sysRowID:string,
}

export interface DownloadData_output{
   returnObj:string,
}

   /** Required : 
      @param ts
      @param sysRowID
      @param localFolder
   */  
export interface ExportToFile_input{
   ts:Ice_Tablesets_SsrsReportDesignTableset[],
   sysRowID:string,
   localFolder:string,
}

export interface ExportToFile_output{
parameters : {
      /**  output parameters  */  
   ts:Ice_Tablesets_SsrsReportDesignTableset[],
}
}

   /** Required : 
      @param sysRowID
   */  
export interface GenerateData_input{
   sysRowID:string,
}

export interface GenerateData_output{
   returnObj:number,
}

export interface GetAvailableDocumentTypes_output{
      /**  A delimeted string of formats.  */  
   returnObj:string,
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
   returnObj:Ice_Tablesets_SsrsReportDesignTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_SsrsReportDesignTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_SsrsReportDesignTableset[],
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
   returnObj:Ice_Tablesets_SsrsReportDesignListTableset[],
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
export interface GetNewSsrsSysRptLst_input{
   ds:Ice_Tablesets_SsrsReportDesignTableset[],
   workStationID:string,
   company:string,
   createdOn:string,
}

export interface GetNewSsrsSysRptLst_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SsrsReportDesignTableset[],
}
}

   /** Required : 
      @param whereClauseSsrsSysRptLst
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSsrsSysRptLst:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_SsrsReportDesignTableset[],
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

export interface Ice_Tablesets_SsrsReportDesignListTableset{
   SsrsSysRptLstList:Ice_Tablesets_SsrsSysRptLstListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SsrsReportDesignTableset{
   SsrsSysRptLst:Ice_Tablesets_SsrsSysRptLstRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SsrsSysRptLstListRow{
      /**  User ID  */  
   UserID:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  Record Sequence  */  
   RecSeq:number,
      /**  Report Description  */  
   RptDescription:string,
      /**  Program which performs the actual printing  */  
   PrintProgram:string,
      /**  Date that this Report will be purged.  */  
   PurgeDate:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ReportID  */  
   ReportID:string,
      /**  StyleNum  */  
   StyleNum:number,
      /**  DesignMode  */  
   DesignMode:string,
      /**  DesignUser  */  
   DesignUser:string,
      /**  StyleDescription  */  
   StyleDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SsrsSysRptLstRow{
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
   DesignRenderFormat:string,
   RptDefID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UpdExtSsrsReportDesignTableset{
   SsrsSysRptLst:Ice_Tablesets_SsrsSysRptLstRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtSsrsReportDesignTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtSsrsReportDesignTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_SsrsReportDesignTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_SsrsReportDesignTableset[],
}
}

   /** Required : 
      @param sysRowID
      @param outputFormat
   */  
export interface UploadAndRenderDesignSsrsReportZip_input{
      /**  SysRptLst.RecSeq  */  
   sysRowID:string,
      /**  i.e. PDF  */  
   outputFormat:string,
}

export interface UploadAndRenderDesignSsrsReportZip_output{
   returnObj:string,
}

   /** Required : 
      @param sysRowID
      @param compressedReportDefinitions
      @param outputFormat
   */  
export interface UploadAndRenderDesign_input{
      /**  SysRptLst.RecSeq  */  
   sysRowID:string,
      /**  Compressed report definitions (zip archive)  */  
   compressedReportDefinitions:string,
      /**  i.e. PDF  */  
   outputFormat:string,
}

export interface UploadAndRenderDesign_output{
   returnObj:string,
}

