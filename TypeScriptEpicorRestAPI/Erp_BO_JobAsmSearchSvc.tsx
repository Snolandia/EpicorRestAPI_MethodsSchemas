import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.JobAsmSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/$metadata", {
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
   Description: Get JobAsmSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobAsmSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobAsmblRow
   */  
export function get_JobAsmSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/JobAsmSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobAsmSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobAsmSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/JobAsmSearches", {
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
   Summary: Calls GetByID to retrieve the JobAsmSearch item
   Description: Calls GetByID to retrieve the JobAsmSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobAsmSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   */  
export function get_JobAsmSearches_Company_JobNum_AssemblySeq(Company:string, JobNum:string, AssemblySeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobAsmblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/JobAsmSearches(" + Company + "," + JobNum + "," + AssemblySeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_JobAsmblRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JobAsmSearch for the service
   Description: Calls UpdateExt to update JobAsmSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobAsmSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JobAsmSearches_Company_JobNum_AssemblySeq(Company:string, JobNum:string, AssemblySeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/JobAsmSearches(" + Company + "," + JobNum + "," + AssemblySeq + ")", {
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
   Summary: Call UpdateExt to delete JobAsmSearch item
   Description: Call UpdateExt to delete JobAsmSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobAsmSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JobAsmSearches_Company_JobNum_AssemblySeq(Company:string, JobNum:string, AssemblySeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/JobAsmSearches(" + Company + "," + JobNum + "," + AssemblySeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobAsmblListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblListRow)
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
export function get_GetRows(whereClauseJobAsmbl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobAsmbl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobAsmbl=" + whereClauseJobAsmbl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(jobNum:string, assemblySeq:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof jobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "jobNum=" + jobNum
   }
   if(typeof assemblySeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assemblySeq=" + assemblySeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewJobAsmbl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobAsmbl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobAsmbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobAsmbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobAsmbl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/GetNewJobAsmbl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobAsmblListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobAsmblRow[],
}

export interface Erp_Tablesets_JobAsmblListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  */  
   "JobComplete":boolean,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   "AssemblySeq":number,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   "PartNum":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "Description":string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  The production quantity required for this assembly per one of it's parent part.  */  
   "QtyPer":number,
      /**  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  */  
   "IUM":string,
      /**   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  */  
   "RequiredQty":number,
      /**  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  */  
   "PullQty":number,
      /**  This is the warehouse that the material is allocated against.  */  
   "WarehouseCode":string,
      /**  The material burden rate for this Job Assembly.  */  
   "MtlBurRate":number,
      /**  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  */  
   "EstUnitCost":number,
      /**  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  */  
   "EstMtlBurUnitCost":number,
      /**  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  */  
   "OverRunQty":number,
      /**  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  */  
   "StartDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   "StartHour":number,
      /**  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   "DueHour":number,
      /**  Sequence number of the Parent Assembly.  */  
   "Parent":number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  */  
   "PriorPeer":number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  */  
   "NextPeer":number,
      /**  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  */  
   "Child":number,
      /**  Total cost to date, of this component that was issued from stock.  */  
   "TotalCost":number,
      /**  Total material burden cost to date, of this component that was issued from stock.  */  
   "MtlBurCost":number,
      /**  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  */  
   "IssuedQty":number,
      /**  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  */  
   "DrawNum":string,
      /**  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   "IssuedComplete":boolean,
      /**  Editor widget for Job Assembly comments.  */  
   "CommentText":string,
      /**  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  */  
   "InCopyList":boolean,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   "BomSequence":number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   "BomLevel":number,
      /**  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  */  
   "WIStartDate":string,
      /**  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   "WIStartHour":number,
      /**  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   "WIDueDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   "WIDueHour":number,
      /**  This Level Actual Labor Cost.  */  
   "TLALaborCost":number,
      /**  This Level Actual Burden Cost.  */  
   "TLABurdenCost":number,
      /**  This Level Actual Material Cost.  */  
   "TLAMaterialCost":number,
      /**  This Level Actual Subcontract Cost.  */  
   "TLASubcontractCost":number,
      /**  This Level Actual Material Burden Cost.  */  
   "TLAMtlBurCost":number,
      /**  This Level Actual Setup Hours.  */  
   "TLASetupHours":number,
      /**  This Level Actual Production Hours.  */  
   "TLAProdHours":number,
      /**  This Level Estimated Labor Cost.  */  
   "TLELaborCost":number,
      /**  This Level Estimated Burden Cost.  */  
   "TLEBurdenCost":number,
      /**  This Level Estimated Material Cost.  */  
   "TLEMaterialCost":number,
      /**  This Level Estimated Subcontract Cost.  */  
   "TLESubcontractCost":number,
      /**  This Level Estimated Material Burden Cost.  */  
   "TLEMtlBurCost":number,
      /**  This Level Estimated Setup Hours.  */  
   "TLESetupHours":number,
      /**  This Level Estimated Production Hours.  */  
   "TLEProdHours":number,
      /**  Lower Level Actual Labor Cost.  */  
   "LLALaborCost":number,
      /**  Lower Level Burden Labor Cost.  */  
   "LLABurdenCost":number,
      /**  Lower Level Actual Material Cost.  */  
   "LLAMaterialCost":number,
      /**  Lower Level Actual Subcontractor Cost.  */  
   "LLASubcontractCost":number,
      /**  Lower Level Actual Material Burden Cost.  */  
   "LLAMtlBurCost":number,
      /**  Lower Level Actual Setup Hours.  */  
   "LLASetupHours":number,
      /**  Lower Level Actual Production Hours.  */  
   "LLAProdHours":number,
      /**  Lower Level Estimated Labor Cost.  */  
   "LLELaborCost":number,
      /**  Lower Level Estimated Burden Cost.  */  
   "LLEBurdenCost":number,
      /**  Lower Level Estimated Material Cost.  */  
   "LLEMaterialCost":number,
      /**  Lower Level Estimated Subcontract Cost.  */  
   "LLESubcontractCost":number,
      /**  Lower Level Estimated Material Burden Cost.  */  
   "LLEMtlBurCost":number,
      /**  Lower Level Estimated Setup Hours.  */  
   "LLESetupHours":number,
      /**  Lower Level Estimated Production Hours.  */  
   "LLEProdHours":number,
      /**   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   "FindNum":string,
      /**  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  */  
   "ReceivedToStock":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  */  
   "Direct":boolean,
      /**   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   "RelatedOperation":number,
      /**  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialLabCost":number,
      /**  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialMtlCost":number,
      /**  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialSubCost":number,
      /**  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialBurCost":number,
      /**  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialLabCost":number,
      /**  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialMtlCost":number,
      /**  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialSubCost":number,
      /**  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialBurCost":number,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   "TotalMtlMtlCost":number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "TotalMtlLabCost":number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "TotalMtlSubCost":number,
      /**  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "TotalMtlBurCost":number,
      /**  The service call that this assembly belongs to.  */  
   "CallNum":number,
      /**  The Service Call Line that this assembly relates to.  */  
   "CallLine":number,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   "RestoreFlag":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  The date when the configuration was completed for the assembly.  */  
   "LastConfigDate":string,
      /**  The system time when the configuration was completed for the assembly.  */  
   "LastConfigTime":number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   "LastConfigUserID":string,
      /**  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  */  
   "OrigRequiredQty":number,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMapData":string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   "WhseAllocFlag":boolean,
      /**  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  */  
   "TLAMaterialMtlBurCost":number,
      /**  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  */  
   "LLAMaterialMtlBurCost":number,
      /**  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompLabCost":number,
      /**  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompMtlCost":number,
      /**  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompSubCost":number,
      /**  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompBurCost":number,
      /**  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompMtlBurCost":number,
      /**  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompLabCost":number,
      /**  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompMtlCost":number,
      /**  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompSubCost":number,
      /**  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompBurCost":number,
      /**  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompMtlBurCost":number,
      /**  Assembly Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Assembly Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**  Original Material Sequence. Used in the configurator.  */  
   "OrigMtlSeq":number,
      /**  Original Rule Tag. Used in the Configurator.  */  
   "OrigRuleTag":string,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   "BasePartNum":string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   "BaseRevisionNum":string,
      /**   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstMtlUnitCost":number,
      /**   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstLbrUnitCost":number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstBurUnitCost":number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstSubUnitCost":number,
      /**  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  */  
   "PlanAsAsm":boolean,
      /**  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  */  
   "PAARef":string,
      /**  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  */  
   "PAAFirm":boolean,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  Required number of designators  */  
   "ReqRefDes":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Related Operation Description  */  
   "RelatedOperationDesc":string,
      /**  Parent PartNum  */  
   "ParentPartNum":string,
      /**  Parent RevisionNum  */  
   "ParentRev":string,
      /**  Parent Description  */  
   "ParentDescription":string,
      /**  Calculated Available Quantity  */  
   "AvailableQty":number,
      /**  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  */  
   "ParentAssemblySeq":number,
      /**  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  */  
   "ChildAssemblySeq":number,
      /**  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  */  
   "AddAsmAs":string,
      /**  The order JobAsmbl records should be displayed.  */  
   "DisplayOrder":number,
   "EnablePurDir":boolean,
   "EnableMtlSalvage":boolean,
      /**  The internal unit of measure for this assembly.  Same as IUM but readOnly  */  
   "DispIUM":string,
   "PartmasterPart":boolean,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   "bAvailQty":number,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   "bUseAvailQty":boolean,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   "EnableAsmSplitCosts":boolean,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   "FirmProcEnable":boolean,
      /**  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  */  
   "FirmProcess":boolean,
      /**  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   "RDPrefix":string,
      /**  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   "RDSuffix":string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   "RDStartNum":number,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   "RDEndNum":number,
      /**  Description  */  
   "AnalysisCdDescription":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "CallLineLineDesc":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
   "AttributeSetDescription":string,
   "AttributeSetShortDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JobAsmblRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  */  
   "JobComplete":boolean,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   "AssemblySeq":number,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   "PartNum":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "Description":string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  The production quantity required for this assembly per one of it's parent part.  */  
   "QtyPer":number,
      /**  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  */  
   "IUM":string,
      /**   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  */  
   "RequiredQty":number,
      /**  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  */  
   "PullQty":number,
      /**  This is the warehouse that the material is allocated against.  */  
   "WarehouseCode":string,
      /**  The material burden rate for this Job Assembly.  */  
   "MtlBurRate":number,
      /**  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  */  
   "EstUnitCost":number,
      /**  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  */  
   "EstMtlBurUnitCost":number,
      /**  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  */  
   "OverRunQty":number,
      /**  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  */  
   "StartDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   "StartHour":number,
      /**  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   "DueHour":number,
      /**  Sequence number of the Parent Assembly.  */  
   "Parent":number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  */  
   "PriorPeer":number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  */  
   "NextPeer":number,
      /**  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  */  
   "Child":number,
      /**  Total cost to date, of this component that was issued from stock.  */  
   "TotalCost":number,
      /**  Total material burden cost to date, of this component that was issued from stock.  */  
   "MtlBurCost":number,
      /**  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  */  
   "IssuedQty":number,
      /**  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  */  
   "DrawNum":string,
      /**  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   "IssuedComplete":boolean,
      /**  Editor widget for Job Assembly comments.  */  
   "CommentText":string,
      /**  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  */  
   "InCopyList":boolean,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   "BomSequence":number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   "BomLevel":number,
      /**  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  */  
   "WIStartDate":string,
      /**  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   "WIStartHour":number,
      /**  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   "WIDueDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   "WIDueHour":number,
      /**  This Level Actual Labor Cost.  */  
   "TLALaborCost":number,
      /**  This Level Actual Burden Cost.  */  
   "TLABurdenCost":number,
      /**  This Level Actual Material Cost.  */  
   "TLAMaterialCost":number,
      /**  This Level Actual Subcontract Cost.  */  
   "TLASubcontractCost":number,
      /**  This Level Actual Material Burden Cost.  */  
   "TLAMtlBurCost":number,
      /**  This Level Actual Setup Hours.  */  
   "TLASetupHours":number,
      /**  This Level Actual Production Hours.  */  
   "TLAProdHours":number,
      /**  This Level Estimated Labor Cost.  */  
   "TLELaborCost":number,
      /**  This Level Estimated Burden Cost.  */  
   "TLEBurdenCost":number,
      /**  This Level Estimated Material Cost.  */  
   "TLEMaterialCost":number,
      /**  This Level Estimated Subcontract Cost.  */  
   "TLESubcontractCost":number,
      /**  This Level Estimated Material Burden Cost.  */  
   "TLEMtlBurCost":number,
      /**  This Level Estimated Setup Hours.  */  
   "TLESetupHours":number,
      /**  This Level Estimated Production Hours.  */  
   "TLEProdHours":number,
      /**  Lower Level Actual Labor Cost.  */  
   "LLALaborCost":number,
      /**  Lower Level Burden Labor Cost.  */  
   "LLABurdenCost":number,
      /**  Lower Level Actual Material Cost.  */  
   "LLAMaterialCost":number,
      /**  Lower Level Actual Subcontractor Cost.  */  
   "LLASubcontractCost":number,
      /**  Lower Level Actual Material Burden Cost.  */  
   "LLAMtlBurCost":number,
      /**  Lower Level Actual Setup Hours.  */  
   "LLASetupHours":number,
      /**  Lower Level Actual Production Hours.  */  
   "LLAProdHours":number,
      /**  Lower Level Estimated Labor Cost.  */  
   "LLELaborCost":number,
      /**  Lower Level Estimated Burden Cost.  */  
   "LLEBurdenCost":number,
      /**  Lower Level Estimated Material Cost.  */  
   "LLEMaterialCost":number,
      /**  Lower Level Estimated Subcontract Cost.  */  
   "LLESubcontractCost":number,
      /**  Lower Level Estimated Material Burden Cost.  */  
   "LLEMtlBurCost":number,
      /**  Lower Level Estimated Setup Hours.  */  
   "LLESetupHours":number,
      /**  Lower Level Estimated Production Hours.  */  
   "LLEProdHours":number,
      /**   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   "FindNum":string,
      /**  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  */  
   "ReceivedToStock":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  */  
   "Direct":boolean,
      /**   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   "RelatedOperation":number,
      /**  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialLabCost":number,
      /**  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialMtlCost":number,
      /**  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialSubCost":number,
      /**  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialBurCost":number,
      /**  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialLabCost":number,
      /**  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialMtlCost":number,
      /**  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialSubCost":number,
      /**  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialBurCost":number,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   "TotalMtlMtlCost":number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "TotalMtlLabCost":number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "TotalMtlSubCost":number,
      /**  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "TotalMtlBurCost":number,
      /**  The service call that this assembly belongs to.  */  
   "CallNum":number,
      /**  The Service Call Line that this assembly relates to.  */  
   "CallLine":number,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   "RestoreFlag":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  The date when the configuration was completed for the assembly.  */  
   "LastConfigDate":string,
      /**  The system time when the configuration was completed for the assembly.  */  
   "LastConfigTime":number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   "LastConfigUserID":string,
      /**  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  */  
   "OrigRequiredQty":number,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMapData":string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   "WhseAllocFlag":boolean,
      /**  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  */  
   "TLAMaterialMtlBurCost":number,
      /**  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  */  
   "LLAMaterialMtlBurCost":number,
      /**  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompLabCost":number,
      /**  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompMtlCost":number,
      /**  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompSubCost":number,
      /**  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompBurCost":number,
      /**  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompMtlBurCost":number,
      /**  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompLabCost":number,
      /**  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompMtlCost":number,
      /**  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompSubCost":number,
      /**  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompBurCost":number,
      /**  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompMtlBurCost":number,
      /**  Assembly Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Assembly Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**  Original Material Sequence. Used in the configurator.  */  
   "OrigMtlSeq":number,
      /**  Original Rule Tag. Used in the Configurator.  */  
   "OrigRuleTag":string,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   "BasePartNum":string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   "BaseRevisionNum":string,
      /**   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstMtlUnitCost":number,
      /**   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstLbrUnitCost":number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstBurUnitCost":number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstSubUnitCost":number,
      /**  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  */  
   "PlanAsAsm":boolean,
      /**  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  */  
   "PAARef":string,
      /**  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  */  
   "PAAFirm":boolean,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  Required number of designators  */  
   "ReqRefDes":number,
      /**  Reassign Serial Numbers Assembly  */  
   "ReassignSNAsm":boolean,
      /**  This Level Actual Other Direct Cost.  */  
   "TLAODCCost":number,
      /**  AssemblyMatch  */  
   "AssemblyMatch":string,
      /**  JdfStatus  */  
   "JdfStatus":string,
      /**  PressDevice  */  
   "PressDevice":string,
      /**  DigitalFileName  */  
   "DigitalFileName":string,
      /**  PrepressJobName  */  
   "PrepressJobName":string,
      /**  JdfPrepressAction  */  
   "JdfPrepressAction":string,
      /**  SendToPress  */  
   "SendToPress":boolean,
      /**  RemovedFromPlan  */  
   "RemovedFromPlan":boolean,
      /**  SendToPressInitiator  */  
   "SendToPressInitiator":number,
      /**  OperationType  */  
   "OperationType":number,
      /**  SendToPrePress  */  
   "SendToPrePress":boolean,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PartPlanInfo  */  
   "PartPlanInfo":string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   "OrigStructTag":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   "LinkToContract":boolean,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   "KBConfigProdID":number,
      /**  Calculated Available Quantity  */  
   "AvailableQty":number,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   "bUseAvailQty":boolean,
      /**  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  */  
   "ChildAssemblySeq":number,
      /**  The internal unit of measure for this assembly.  Same as IUM but readOnly  */  
   "DispIUM":string,
      /**  The order JobAsmbl records should be displayed.  */  
   "DisplayOrder":number,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   "EnableAsmSplitCosts":boolean,
   "EnableMtlSalvage":boolean,
   "EnablePurDir":boolean,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   "FirmProcEnable":boolean,
      /**  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  */  
   "FirmProcess":boolean,
      /**  External field for EQSyst GetCostsFromInventory  */  
   "GetCostsFromInventory":boolean,
      /**  External field to hold JCSyst.GetCostsFromTemplate value  */  
   "GetCostsFromTemplate":boolean,
      /**  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  */  
   "ParentAssemblySeq":number,
      /**  Parent Description  */  
   "ParentDescription":string,
      /**  Parent PartNum  */  
   "ParentPartNum":string,
      /**  Parent RevisionNum  */  
   "ParentRev":string,
      /**  Internal flag to identify if current Part is an Inventory Part.  */  
   "PartExists":boolean,
   "PartmasterPart":boolean,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   "RDEndNum":number,
      /**  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   "RDPrefix":string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   "RDStartNum":number,
      /**  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   "RDSuffix":string,
      /**  Related Operation Description  */  
   "RelatedOperationDesc":string,
      /**  For Internal use ONLY to set a flag calculated from BO to show a warning message to the user when there exists some inconsistences between records on JobAsml table that can cause infinite loop when BOM Resequence.  */  
   "ShowWarningBOMResequence":boolean,
      /**  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  */  
   "AddAsmAs":string,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   "bAvailQty":number,
   "EnableAttributeSetSearch":boolean,
   "AttributeSetShortDescription":string,
   "AttributeSetDescription":string,
   "AttrClassID":string,
      /**  This Level Total Actual Cost (TLAMaterialCost + TLALaborCost + TLABurdenCost + TLASubcontractCost + TLAMtlBurCost)  */  
   "TLATotalCost":number,
      /**  The Level Estimated Total Cost (TLEMaterialCost + TLELaborCost + TLEBurdenCost + TLESubcontractCost + TLEMtlBurCost)  */  
   "TLETotalCost":number,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "CallLineLineDesc":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "JobNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumPricePerCode":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PlantName":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param jobNum
      @param assemblySeq
   */  
export interface DeleteByID_input{
   jobNum:string,
   assemblySeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_JobAsmSearchTableset{
   JobAsmbl:Erp_Tablesets_JobAsmblRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobAsmblListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  */  
   JobComplete:boolean,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   PartNum:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   Description:string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  The production quantity required for this assembly per one of it's parent part.  */  
   QtyPer:number,
      /**  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  */  
   IUM:string,
      /**   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  */  
   RequiredQty:number,
      /**  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  */  
   PullQty:number,
      /**  This is the warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  The material burden rate for this Job Assembly.  */  
   MtlBurRate:number,
      /**  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  */  
   EstUnitCost:number,
      /**  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  */  
   EstMtlBurUnitCost:number,
      /**  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  */  
   OverRunQty:number,
      /**  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  */  
   StartDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   StartHour:number,
      /**  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   DueHour:number,
      /**  Sequence number of the Parent Assembly.  */  
   Parent:number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  */  
   PriorPeer:number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  */  
   NextPeer:number,
      /**  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  */  
   Child:number,
      /**  Total cost to date, of this component that was issued from stock.  */  
   TotalCost:number,
      /**  Total material burden cost to date, of this component that was issued from stock.  */  
   MtlBurCost:number,
      /**  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  */  
   IssuedQty:number,
      /**  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  */  
   DrawNum:string,
      /**  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   IssuedComplete:boolean,
      /**  Editor widget for Job Assembly comments.  */  
   CommentText:string,
      /**  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  */  
   InCopyList:boolean,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   BomSequence:number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   BomLevel:number,
      /**  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  */  
   WIStartDate:string,
      /**  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   WIStartHour:number,
      /**  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   WIDueHour:number,
      /**  This Level Actual Labor Cost.  */  
   TLALaborCost:number,
      /**  This Level Actual Burden Cost.  */  
   TLABurdenCost:number,
      /**  This Level Actual Material Cost.  */  
   TLAMaterialCost:number,
      /**  This Level Actual Subcontract Cost.  */  
   TLASubcontractCost:number,
      /**  This Level Actual Material Burden Cost.  */  
   TLAMtlBurCost:number,
      /**  This Level Actual Setup Hours.  */  
   TLASetupHours:number,
      /**  This Level Actual Production Hours.  */  
   TLAProdHours:number,
      /**  This Level Estimated Labor Cost.  */  
   TLELaborCost:number,
      /**  This Level Estimated Burden Cost.  */  
   TLEBurdenCost:number,
      /**  This Level Estimated Material Cost.  */  
   TLEMaterialCost:number,
      /**  This Level Estimated Subcontract Cost.  */  
   TLESubcontractCost:number,
      /**  This Level Estimated Material Burden Cost.  */  
   TLEMtlBurCost:number,
      /**  This Level Estimated Setup Hours.  */  
   TLESetupHours:number,
      /**  This Level Estimated Production Hours.  */  
   TLEProdHours:number,
      /**  Lower Level Actual Labor Cost.  */  
   LLALaborCost:number,
      /**  Lower Level Burden Labor Cost.  */  
   LLABurdenCost:number,
      /**  Lower Level Actual Material Cost.  */  
   LLAMaterialCost:number,
      /**  Lower Level Actual Subcontractor Cost.  */  
   LLASubcontractCost:number,
      /**  Lower Level Actual Material Burden Cost.  */  
   LLAMtlBurCost:number,
      /**  Lower Level Actual Setup Hours.  */  
   LLASetupHours:number,
      /**  Lower Level Actual Production Hours.  */  
   LLAProdHours:number,
      /**  Lower Level Estimated Labor Cost.  */  
   LLELaborCost:number,
      /**  Lower Level Estimated Burden Cost.  */  
   LLEBurdenCost:number,
      /**  Lower Level Estimated Material Cost.  */  
   LLEMaterialCost:number,
      /**  Lower Level Estimated Subcontract Cost.  */  
   LLESubcontractCost:number,
      /**  Lower Level Estimated Material Burden Cost.  */  
   LLEMtlBurCost:number,
      /**  Lower Level Estimated Setup Hours.  */  
   LLESetupHours:number,
      /**  Lower Level Estimated Production Hours.  */  
   LLEProdHours:number,
      /**   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   FindNum:string,
      /**  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  */  
   ReceivedToStock:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  */  
   Direct:boolean,
      /**   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   RelatedOperation:number,
      /**  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialLabCost:number,
      /**  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialMtlCost:number,
      /**  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialSubCost:number,
      /**  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialBurCost:number,
      /**  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialLabCost:number,
      /**  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialMtlCost:number,
      /**  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialSubCost:number,
      /**  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialBurCost:number,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   TotalMtlMtlCost:number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlLabCost:number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlSubCost:number,
      /**  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlBurCost:number,
      /**  The service call that this assembly belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this assembly relates to.  */  
   CallLine:number,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  */  
   OrigRequiredQty:number,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  */  
   TLAMaterialMtlBurCost:number,
      /**  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  */  
   LLAMaterialMtlBurCost:number,
      /**  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompLabCost:number,
      /**  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompMtlCost:number,
      /**  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompSubCost:number,
      /**  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompBurCost:number,
      /**  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompMtlBurCost:number,
      /**  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompLabCost:number,
      /**  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompMtlCost:number,
      /**  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompSubCost:number,
      /**  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompBurCost:number,
      /**  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompMtlBurCost:number,
      /**  Assembly Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Assembly Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**  Original Material Sequence. Used in the configurator.  */  
   OrigMtlSeq:number,
      /**  Original Rule Tag. Used in the Configurator.  */  
   OrigRuleTag:string,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstMtlUnitCost:number,
      /**   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstLbrUnitCost:number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstBurUnitCost:number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstSubUnitCost:number,
      /**  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  */  
   PlanAsAsm:boolean,
      /**  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  */  
   PAARef:string,
      /**  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  */  
   PAAFirm:boolean,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Related Operation Description  */  
   RelatedOperationDesc:string,
      /**  Parent PartNum  */  
   ParentPartNum:string,
      /**  Parent RevisionNum  */  
   ParentRev:string,
      /**  Parent Description  */  
   ParentDescription:string,
      /**  Calculated Available Quantity  */  
   AvailableQty:number,
      /**  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  */  
   ParentAssemblySeq:number,
      /**  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  */  
   ChildAssemblySeq:number,
      /**  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  */  
   AddAsmAs:string,
      /**  The order JobAsmbl records should be displayed.  */  
   DisplayOrder:number,
   EnablePurDir:boolean,
   EnableMtlSalvage:boolean,
      /**  The internal unit of measure for this assembly.  Same as IUM but readOnly  */  
   DispIUM:string,
   PartmasterPart:boolean,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   bAvailQty:number,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   bUseAvailQty:boolean,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   EnableAsmSplitCosts:boolean,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   FirmProcEnable:boolean,
      /**  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  */  
   FirmProcess:boolean,
      /**  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  Description  */  
   AnalysisCdDescription:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   CallLineLineDesc:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
   AttributeSetDescription:string,
   AttributeSetShortDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobAsmblListTableset{
   JobAsmblList:Erp_Tablesets_JobAsmblListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobAsmblRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  */  
   JobComplete:boolean,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   PartNum:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   Description:string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  The production quantity required for this assembly per one of it's parent part.  */  
   QtyPer:number,
      /**  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  */  
   IUM:string,
      /**   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  */  
   RequiredQty:number,
      /**  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  */  
   PullQty:number,
      /**  This is the warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  The material burden rate for this Job Assembly.  */  
   MtlBurRate:number,
      /**  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  */  
   EstUnitCost:number,
      /**  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  */  
   EstMtlBurUnitCost:number,
      /**  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  */  
   OverRunQty:number,
      /**  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  */  
   StartDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   StartHour:number,
      /**  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   DueHour:number,
      /**  Sequence number of the Parent Assembly.  */  
   Parent:number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  */  
   PriorPeer:number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  */  
   NextPeer:number,
      /**  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  */  
   Child:number,
      /**  Total cost to date, of this component that was issued from stock.  */  
   TotalCost:number,
      /**  Total material burden cost to date, of this component that was issued from stock.  */  
   MtlBurCost:number,
      /**  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  */  
   IssuedQty:number,
      /**  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  */  
   DrawNum:string,
      /**  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   IssuedComplete:boolean,
      /**  Editor widget for Job Assembly comments.  */  
   CommentText:string,
      /**  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  */  
   InCopyList:boolean,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   BomSequence:number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   BomLevel:number,
      /**  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  */  
   WIStartDate:string,
      /**  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   WIStartHour:number,
      /**  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   WIDueHour:number,
      /**  This Level Actual Labor Cost.  */  
   TLALaborCost:number,
      /**  This Level Actual Burden Cost.  */  
   TLABurdenCost:number,
      /**  This Level Actual Material Cost.  */  
   TLAMaterialCost:number,
      /**  This Level Actual Subcontract Cost.  */  
   TLASubcontractCost:number,
      /**  This Level Actual Material Burden Cost.  */  
   TLAMtlBurCost:number,
      /**  This Level Actual Setup Hours.  */  
   TLASetupHours:number,
      /**  This Level Actual Production Hours.  */  
   TLAProdHours:number,
      /**  This Level Estimated Labor Cost.  */  
   TLELaborCost:number,
      /**  This Level Estimated Burden Cost.  */  
   TLEBurdenCost:number,
      /**  This Level Estimated Material Cost.  */  
   TLEMaterialCost:number,
      /**  This Level Estimated Subcontract Cost.  */  
   TLESubcontractCost:number,
      /**  This Level Estimated Material Burden Cost.  */  
   TLEMtlBurCost:number,
      /**  This Level Estimated Setup Hours.  */  
   TLESetupHours:number,
      /**  This Level Estimated Production Hours.  */  
   TLEProdHours:number,
      /**  Lower Level Actual Labor Cost.  */  
   LLALaborCost:number,
      /**  Lower Level Burden Labor Cost.  */  
   LLABurdenCost:number,
      /**  Lower Level Actual Material Cost.  */  
   LLAMaterialCost:number,
      /**  Lower Level Actual Subcontractor Cost.  */  
   LLASubcontractCost:number,
      /**  Lower Level Actual Material Burden Cost.  */  
   LLAMtlBurCost:number,
      /**  Lower Level Actual Setup Hours.  */  
   LLASetupHours:number,
      /**  Lower Level Actual Production Hours.  */  
   LLAProdHours:number,
      /**  Lower Level Estimated Labor Cost.  */  
   LLELaborCost:number,
      /**  Lower Level Estimated Burden Cost.  */  
   LLEBurdenCost:number,
      /**  Lower Level Estimated Material Cost.  */  
   LLEMaterialCost:number,
      /**  Lower Level Estimated Subcontract Cost.  */  
   LLESubcontractCost:number,
      /**  Lower Level Estimated Material Burden Cost.  */  
   LLEMtlBurCost:number,
      /**  Lower Level Estimated Setup Hours.  */  
   LLESetupHours:number,
      /**  Lower Level Estimated Production Hours.  */  
   LLEProdHours:number,
      /**   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   FindNum:string,
      /**  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  */  
   ReceivedToStock:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  */  
   Direct:boolean,
      /**   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   RelatedOperation:number,
      /**  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialLabCost:number,
      /**  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialMtlCost:number,
      /**  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialSubCost:number,
      /**  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialBurCost:number,
      /**  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialLabCost:number,
      /**  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialMtlCost:number,
      /**  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialSubCost:number,
      /**  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialBurCost:number,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   TotalMtlMtlCost:number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlLabCost:number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlSubCost:number,
      /**  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlBurCost:number,
      /**  The service call that this assembly belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this assembly relates to.  */  
   CallLine:number,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  */  
   OrigRequiredQty:number,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  */  
   TLAMaterialMtlBurCost:number,
      /**  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  */  
   LLAMaterialMtlBurCost:number,
      /**  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompLabCost:number,
      /**  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompMtlCost:number,
      /**  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompSubCost:number,
      /**  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompBurCost:number,
      /**  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompMtlBurCost:number,
      /**  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompLabCost:number,
      /**  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompMtlCost:number,
      /**  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompSubCost:number,
      /**  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompBurCost:number,
      /**  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompMtlBurCost:number,
      /**  Assembly Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Assembly Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**  Original Material Sequence. Used in the configurator.  */  
   OrigMtlSeq:number,
      /**  Original Rule Tag. Used in the Configurator.  */  
   OrigRuleTag:string,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstMtlUnitCost:number,
      /**   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstLbrUnitCost:number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstBurUnitCost:number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstSubUnitCost:number,
      /**  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  */  
   PlanAsAsm:boolean,
      /**  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  */  
   PAARef:string,
      /**  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  */  
   PAAFirm:boolean,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  Reassign Serial Numbers Assembly  */  
   ReassignSNAsm:boolean,
      /**  This Level Actual Other Direct Cost.  */  
   TLAODCCost:number,
      /**  AssemblyMatch  */  
   AssemblyMatch:string,
      /**  JdfStatus  */  
   JdfStatus:string,
      /**  PressDevice  */  
   PressDevice:string,
      /**  DigitalFileName  */  
   DigitalFileName:string,
      /**  PrepressJobName  */  
   PrepressJobName:string,
      /**  JdfPrepressAction  */  
   JdfPrepressAction:string,
      /**  SendToPress  */  
   SendToPress:boolean,
      /**  RemovedFromPlan  */  
   RemovedFromPlan:boolean,
      /**  SendToPressInitiator  */  
   SendToPressInitiator:number,
      /**  OperationType  */  
   OperationType:number,
      /**  SendToPrePress  */  
   SendToPrePress:boolean,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PartPlanInfo  */  
   PartPlanInfo:string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  ContractID  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   LinkToContract:boolean,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  Calculated Available Quantity  */  
   AvailableQty:number,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   bUseAvailQty:boolean,
      /**  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  */  
   ChildAssemblySeq:number,
      /**  The internal unit of measure for this assembly.  Same as IUM but readOnly  */  
   DispIUM:string,
      /**  The order JobAsmbl records should be displayed.  */  
   DisplayOrder:number,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   EnableAsmSplitCosts:boolean,
   EnableMtlSalvage:boolean,
   EnablePurDir:boolean,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   FirmProcEnable:boolean,
      /**  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  */  
   FirmProcess:boolean,
      /**  External field for EQSyst GetCostsFromInventory  */  
   GetCostsFromInventory:boolean,
      /**  External field to hold JCSyst.GetCostsFromTemplate value  */  
   GetCostsFromTemplate:boolean,
      /**  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  */  
   ParentAssemblySeq:number,
      /**  Parent Description  */  
   ParentDescription:string,
      /**  Parent PartNum  */  
   ParentPartNum:string,
      /**  Parent RevisionNum  */  
   ParentRev:string,
      /**  Internal flag to identify if current Part is an Inventory Part.  */  
   PartExists:boolean,
   PartmasterPart:boolean,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
      /**  Related Operation Description  */  
   RelatedOperationDesc:string,
      /**  For Internal use ONLY to set a flag calculated from BO to show a warning message to the user when there exists some inconsistences between records on JobAsml table that can cause infinite loop when BOM Resequence.  */  
   ShowWarningBOMResequence:boolean,
      /**  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  */  
   AddAsmAs:string,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   bAvailQty:number,
   EnableAttributeSetSearch:boolean,
   AttributeSetShortDescription:string,
   AttributeSetDescription:string,
   AttrClassID:string,
      /**  This Level Total Actual Cost (TLAMaterialCost + TLALaborCost + TLABurdenCost + TLASubcontractCost + TLAMtlBurCost)  */  
   TLATotalCost:number,
      /**  The Level Estimated Total Cost (TLEMaterialCost + TLELaborCost + TLEBurdenCost + TLESubcontractCost + TLEMtlBurCost)  */  
   TLETotalCost:number,
   BitFlag:number,
   AnalysisCdDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   JobNumPartDescription:string,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumTrackInventoryAttributes:boolean,
   PlantName:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtJobAsmSearchTableset{
   JobAsmbl:Erp_Tablesets_JobAsmblRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param jobNum
      @param assemblySeq
   */  
export interface GetByID_input{
   jobNum:string,
   assemblySeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_JobAsmSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_JobAsmSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_JobAsmSearchTableset[],
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
   returnObj:Erp_Tablesets_JobAsmblListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param jobNum
   */  
export interface GetNewJobAsmbl_input{
   ds:Erp_Tablesets_JobAsmSearchTableset[],
   jobNum:string,
}

export interface GetNewJobAsmbl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAsmSearchTableset[],
}
}

   /** Required : 
      @param whereClauseJobAsmbl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseJobAsmbl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_JobAsmSearchTableset[],
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

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtJobAsmSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtJobAsmSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_JobAsmSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAsmSearchTableset[],
}
}

