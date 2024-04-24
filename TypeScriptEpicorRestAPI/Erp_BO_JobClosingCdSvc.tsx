import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.JobClosingCdSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/$metadata", {
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
   Description: Get JobClosingCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobClosingCds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobClosingCdRow
   */  
export function get_JobClosingCds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobClosingCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/JobClosingCds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobClosingCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobClosingCds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobClosingCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JobClosingCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobClosingCds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/JobClosingCds", {
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
   Summary: Calls GetByID to retrieve the JobClosingCd item
   Description: Calls GetByID to retrieve the JobClosingCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobClosingCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobClosingCode Desc: JobClosingCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobClosingCdRow
   */  
export function get_JobClosingCds_Company_JobClosingCode(Company:string, JobClosingCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobClosingCdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/JobClosingCds(" + Company + "," + JobClosingCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_JobClosingCdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JobClosingCd for the service
   Description: Calls UpdateExt to update JobClosingCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobClosingCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobClosingCode Desc: JobClosingCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobClosingCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JobClosingCds_Company_JobClosingCode(Company:string, JobClosingCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/JobClosingCds(" + Company + "," + JobClosingCode + ")", {
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
   Summary: Call UpdateExt to delete JobClosingCd item
   Description: Call UpdateExt to delete JobClosingCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobClosingCd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobClosingCode Desc: JobClosingCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JobClosingCds_Company_JobClosingCode(Company:string, JobClosingCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/JobClosingCds(" + Company + "," + JobClosingCode + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobClosingCdListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobClosingCdListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobClosingCdListRow)
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
export function get_GetRows(whereClauseJobClosingCd:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobClosingCd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobClosingCd=" + whereClauseJobClosingCd
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(jobClosingCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof jobClosingCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "jobClosingCode=" + jobClosingCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/GetList" + params, {
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
   Summary: Invoke method GetNewJobClosingCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobClosingCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobClosingCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobClosingCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobClosingCd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/GetNewJobClosingCd", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingCdSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobClosingCdListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobClosingCdListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobClosingCdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobClosingCdRow[],
}

export interface Erp_Tablesets_JobClosingCdListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code to identify the job closing record  */  
   "JobClosingCode":string,
      /**  Description field  */  
   "Description":string,
      /**  Indicates that this job closing record can be used for job completion.  */  
   "JobCompletion":boolean,
      /**  Indicates that this job closing record can be used for job closing.  */  
   "JobClosing":boolean,
      /**  If set to yes then this record has the default values for the job completion process.  */  
   "JobCompletionDefault":boolean,
      /**  If set to yes then this  record has the default values for the job closing process.  */  
   "JobClosingDefault":boolean,
      /**  Material Quantity Under Percent. Threshold for the Material Quantity under completed.  */  
   "MtlQtyPercent":number,
      /**  Material Cost Under Percent. Threshold for the Material Cost under completed.  */  
   "MtlCostPercent":number,
      /**  Operation Quantity Under Percent. Threshold for the Operation Quantity under completed.  */  
   "OprQtyPercent":number,
      /**  Operation Cost Under Percent. Threshold for the Operation Cost under completed.  */  
   "OprCostPercent":number,
      /**  SubContract Quantity Under Percent. Threshold for the SubContract Quantity under completed.  */  
   "SubQtyPercent":number,
      /**  SubContract Cost Percent. Threshold for the SubContract Cost under completed.  */  
   "SubCostPercent":number,
      /**  Material Quantity Percent. Threshold for the Material Quantity  over completed.  */  
   "MtlQtyOverPercent":number,
      /**  Material Cost Over Percent. Threshold for the Material Cost over completed.  */  
   "MtlCostOverPercent":number,
      /**  Operation Quantity Over Percent. Threshold for the Operation Quantity over completed.  */  
   "OprQtyOverPercent":number,
      /**  Operation Cost Over Percent. Threshold for the Operation Cost over completed.  */  
   "OprCostOverPercent":number,
      /**  SubContract Quantity Over Percent. Threshold for the SubContract Quantity over completed.  */  
   "SubQtyOverPercent":number,
      /**  SubContract Cost Over Percent. Threshold for the SubContract Cost over completed.  */  
   "SubCostOverPercent":number,
      /**  Job Cost Under Amount. Under threshold for the Total Job Cost.  */  
   "JobCostAmount":number,
      /**  Job Cost Over Amount. Over Threshold for the Total Job Cost.  */  
   "JobCostOverAmount":number,
      /**  If Set to yes then the materials will be backflushed during the job completion process. (for future use).  */  
   "Backflush":boolean,
      /**  If set to yes then jobs pending for inspection are completed in the auto completion process.  The auto closing process will not process any pending inspection jobs.  */  
   "PendingInspection":boolean,
      /**  If set to yes then job operations using resources in other Sites than the job header Site are allowed to be completed in the auto completion process and the auto closing process.  */  
   "MultiplePlants":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JobClosingCdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code to identify the job closing record  */  
   "JobClosingCode":string,
      /**  Description field  */  
   "Description":string,
      /**  Indicates that this job closing record can be used for job completion.  */  
   "JobCompletion":boolean,
      /**  Indicates that this job closing record can be used for job closing.  */  
   "JobClosing":boolean,
      /**  If set to yes then this record has the default values for the job completion process.  */  
   "JobCompletionDefault":boolean,
      /**  If set to yes then this  record has the default values for the job closing process.  */  
   "JobClosingDefault":boolean,
      /**  Material Quantity Under Percent. Threshold for the Material Quantity under completed.  */  
   "MtlQtyPercent":number,
      /**  Material Cost Under Percent. Threshold for the Material Cost under completed.  */  
   "MtlCostPercent":number,
      /**  Operation Quantity Under Percent. Threshold for the Operation Quantity under completed.  */  
   "OprQtyPercent":number,
      /**  Operation Cost Under Percent. Threshold for the Operation Cost under completed.  */  
   "OprCostPercent":number,
      /**  SubContract Quantity Under Percent. Threshold for the SubContract Quantity under completed.  */  
   "SubQtyPercent":number,
      /**  SubContract Cost Percent. Threshold for the SubContract Cost under completed.  */  
   "SubCostPercent":number,
      /**  Material Quantity Percent. Threshold for the Material Quantity  over completed.  */  
   "MtlQtyOverPercent":number,
      /**  Material Cost Over Percent. Threshold for the Material Cost over completed.  */  
   "MtlCostOverPercent":number,
      /**  Operation Quantity Over Percent. Threshold for the Operation Quantity over completed.  */  
   "OprQtyOverPercent":number,
      /**  Operation Cost Over Percent. Threshold for the Operation Cost over completed.  */  
   "OprCostOverPercent":number,
      /**  SubContract Quantity Over Percent. Threshold for the SubContract Quantity over completed.  */  
   "SubQtyOverPercent":number,
      /**  SubContract Cost Over Percent. Threshold for the SubContract Cost over completed.  */  
   "SubCostOverPercent":number,
      /**  Job Cost Under Amount. Under threshold for the Total Job Cost.  */  
   "JobCostAmount":number,
      /**  Job Cost Over Amount. Over Threshold for the Total Job Cost.  */  
   "JobCostOverAmount":number,
      /**  If Set to yes then the materials will be backflushed during the job completion process. (for future use).  */  
   "Backflush":boolean,
      /**  If set to yes then jobs pending for inspection are completed in the auto completion process.  The auto closing process will not process any pending inspection jobs.  */  
   "PendingInspection":boolean,
      /**  If set to yes then job operations using resources in other Sites than the job header Site are allowed to be completed in the auto completion process and the auto closing process.  */  
   "MultiplePlants":boolean,
      /**  IgnoreCompleted  */  
   "IgnoreCompleted":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param jobClosingCode
   */  
export interface DeleteByID_input{
   jobClosingCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_JobClosingCdListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code to identify the job closing record  */  
   JobClosingCode:string,
      /**  Description field  */  
   Description:string,
      /**  Indicates that this job closing record can be used for job completion.  */  
   JobCompletion:boolean,
      /**  Indicates that this job closing record can be used for job closing.  */  
   JobClosing:boolean,
      /**  If set to yes then this record has the default values for the job completion process.  */  
   JobCompletionDefault:boolean,
      /**  If set to yes then this  record has the default values for the job closing process.  */  
   JobClosingDefault:boolean,
      /**  Material Quantity Under Percent. Threshold for the Material Quantity under completed.  */  
   MtlQtyPercent:number,
      /**  Material Cost Under Percent. Threshold for the Material Cost under completed.  */  
   MtlCostPercent:number,
      /**  Operation Quantity Under Percent. Threshold for the Operation Quantity under completed.  */  
   OprQtyPercent:number,
      /**  Operation Cost Under Percent. Threshold for the Operation Cost under completed.  */  
   OprCostPercent:number,
      /**  SubContract Quantity Under Percent. Threshold for the SubContract Quantity under completed.  */  
   SubQtyPercent:number,
      /**  SubContract Cost Percent. Threshold for the SubContract Cost under completed.  */  
   SubCostPercent:number,
      /**  Material Quantity Percent. Threshold for the Material Quantity  over completed.  */  
   MtlQtyOverPercent:number,
      /**  Material Cost Over Percent. Threshold for the Material Cost over completed.  */  
   MtlCostOverPercent:number,
      /**  Operation Quantity Over Percent. Threshold for the Operation Quantity over completed.  */  
   OprQtyOverPercent:number,
      /**  Operation Cost Over Percent. Threshold for the Operation Cost over completed.  */  
   OprCostOverPercent:number,
      /**  SubContract Quantity Over Percent. Threshold for the SubContract Quantity over completed.  */  
   SubQtyOverPercent:number,
      /**  SubContract Cost Over Percent. Threshold for the SubContract Cost over completed.  */  
   SubCostOverPercent:number,
      /**  Job Cost Under Amount. Under threshold for the Total Job Cost.  */  
   JobCostAmount:number,
      /**  Job Cost Over Amount. Over Threshold for the Total Job Cost.  */  
   JobCostOverAmount:number,
      /**  If Set to yes then the materials will be backflushed during the job completion process. (for future use).  */  
   Backflush:boolean,
      /**  If set to yes then jobs pending for inspection are completed in the auto completion process.  The auto closing process will not process any pending inspection jobs.  */  
   PendingInspection:boolean,
      /**  If set to yes then job operations using resources in other Sites than the job header Site are allowed to be completed in the auto completion process and the auto closing process.  */  
   MultiplePlants:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobClosingCdListTableset{
   JobClosingCdList:Erp_Tablesets_JobClosingCdListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobClosingCdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code to identify the job closing record  */  
   JobClosingCode:string,
      /**  Description field  */  
   Description:string,
      /**  Indicates that this job closing record can be used for job completion.  */  
   JobCompletion:boolean,
      /**  Indicates that this job closing record can be used for job closing.  */  
   JobClosing:boolean,
      /**  If set to yes then this record has the default values for the job completion process.  */  
   JobCompletionDefault:boolean,
      /**  If set to yes then this  record has the default values for the job closing process.  */  
   JobClosingDefault:boolean,
      /**  Material Quantity Under Percent. Threshold for the Material Quantity under completed.  */  
   MtlQtyPercent:number,
      /**  Material Cost Under Percent. Threshold for the Material Cost under completed.  */  
   MtlCostPercent:number,
      /**  Operation Quantity Under Percent. Threshold for the Operation Quantity under completed.  */  
   OprQtyPercent:number,
      /**  Operation Cost Under Percent. Threshold for the Operation Cost under completed.  */  
   OprCostPercent:number,
      /**  SubContract Quantity Under Percent. Threshold for the SubContract Quantity under completed.  */  
   SubQtyPercent:number,
      /**  SubContract Cost Percent. Threshold for the SubContract Cost under completed.  */  
   SubCostPercent:number,
      /**  Material Quantity Percent. Threshold for the Material Quantity  over completed.  */  
   MtlQtyOverPercent:number,
      /**  Material Cost Over Percent. Threshold for the Material Cost over completed.  */  
   MtlCostOverPercent:number,
      /**  Operation Quantity Over Percent. Threshold for the Operation Quantity over completed.  */  
   OprQtyOverPercent:number,
      /**  Operation Cost Over Percent. Threshold for the Operation Cost over completed.  */  
   OprCostOverPercent:number,
      /**  SubContract Quantity Over Percent. Threshold for the SubContract Quantity over completed.  */  
   SubQtyOverPercent:number,
      /**  SubContract Cost Over Percent. Threshold for the SubContract Cost over completed.  */  
   SubCostOverPercent:number,
      /**  Job Cost Under Amount. Under threshold for the Total Job Cost.  */  
   JobCostAmount:number,
      /**  Job Cost Over Amount. Over Threshold for the Total Job Cost.  */  
   JobCostOverAmount:number,
      /**  If Set to yes then the materials will be backflushed during the job completion process. (for future use).  */  
   Backflush:boolean,
      /**  If set to yes then jobs pending for inspection are completed in the auto completion process.  The auto closing process will not process any pending inspection jobs.  */  
   PendingInspection:boolean,
      /**  If set to yes then job operations using resources in other Sites than the job header Site are allowed to be completed in the auto completion process and the auto closing process.  */  
   MultiplePlants:boolean,
      /**  IgnoreCompleted  */  
   IgnoreCompleted:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobClosingCdTableset{
   JobClosingCd:Erp_Tablesets_JobClosingCdRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtJobClosingCdTableset{
   JobClosingCd:Erp_Tablesets_JobClosingCdRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param jobClosingCode
   */  
export interface GetByID_input{
   jobClosingCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_JobClosingCdTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_JobClosingCdTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_JobClosingCdTableset[],
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
   returnObj:Erp_Tablesets_JobClosingCdListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewJobClosingCd_input{
   ds:Erp_Tablesets_JobClosingCdTableset[],
}

export interface GetNewJobClosingCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobClosingCdTableset[],
}
}

   /** Required : 
      @param whereClauseJobClosingCd
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseJobClosingCd:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_JobClosingCdTableset[],
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
   ds:Erp_Tablesets_UpdExtJobClosingCdTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtJobClosingCdTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_JobClosingCdTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobClosingCdTableset[],
}
}

