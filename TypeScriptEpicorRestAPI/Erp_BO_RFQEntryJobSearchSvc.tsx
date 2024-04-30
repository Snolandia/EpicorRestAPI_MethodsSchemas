import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.RFQEntryJobSearchSvc
// Description: This is a Job Search object used in RFQEntry.
The GetRows of this objects returns the jobs
that are relevant in Add from Job function in RFQEntry.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get RFQEntryJobSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQEntryJobSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadRow
   */  
export function get_RFQEntryJobSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/RFQEntryJobSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQEntryJobSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.JobHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RFQEntryJobSearches(requestBody:Erp_Tablesets_JobHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/RFQEntryJobSearches", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RFQEntryJobSearch item
   Description: Calls GetByID to retrieve the RFQEntryJobSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQEntryJobSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.JobHeadRow
   */  
export function get_RFQEntryJobSearches_Company_JobNum(Company:string, JobNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/RFQEntryJobSearches(" + Company + "," + JobNum + ")", {
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
         resolve(data as Erp_Tablesets_JobHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RFQEntryJobSearch for the service
   Description: Calls UpdateExt to update RFQEntryJobSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQEntryJobSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RFQEntryJobSearches_Company_JobNum(Company:string, JobNum:string, requestBody:Erp_Tablesets_JobHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/RFQEntryJobSearches(" + Company + "," + JobNum + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete RFQEntryJobSearch item
   Description: Call UpdateExt to delete RFQEntryJobSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQEntryJobSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RFQEntryJobSearches_Company_JobNum(Company:string, JobNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/RFQEntryJobSearches(" + Company + "," + JobNum + ")", {
          method: 'delete',
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseJobHead:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobHead=" + whereClauseJobHead
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/GetRows" + params, {
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
         resolve(data as GetRows_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(jobNum:string, epicorHeaders?:Headers){
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/GetByID" + params, {
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
         resolve(data as GetByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/GetList" + params, {
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
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewJobHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewJobHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobHead(requestBody:GetNewJobHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewJobHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/GetNewJobHead", {
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
         resolve(data as GetNewJobHead_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/DeleteByID", {
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
         resolve(data as DeleteByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/GetBySysRowID" + params, {
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
         resolve(data as GetBySysRowID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/GetBySysRowIDs" + params, {
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
         resolve(data as GetBySysRowIDs_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/Update", {
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
         resolve(data as Update_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryJobSearchSvc/UpdateExt", {
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
         resolve(data as UpdateExt_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobHeadRow,
}

export interface Erp_Tablesets_JobHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   "JobClosed":boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   "ClosedDate":string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   "JobComplete":boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   "JobCompletionDate":string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   "JobEngineered":boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   "JobReleased":boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   "JobHeld":boolean,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   "JobNum":string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   "PartNum":string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   "DrawNum":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "PartDescription":string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   "ProdQty":number,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   "IUM":string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "StartDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "StartHour":number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   "DueHour":number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   "ReqDueDate":string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   "JobCode":string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   "QuoteNum":number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   "QuoteLine":number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  Editor widget for Job header comments.  */  
   "CommentText":string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   "ExpenseCode":string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   "InCopyList":boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   "WIName":string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "WIStartDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "WIStartHour":number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   "Candidate":boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   "SchedCode":string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   "SchedLocked":boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   "ProjectID":string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   "WIPCleared":boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   "JobFirm":boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   "PersonList":string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   "PersonID":string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   "ProdTeamID":string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   "QtyCompleted":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   "DatePurged":string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   "TravelerReadyToPrint":boolean,
      /**  The last date the job traveler was mass printed.  */  
   "TravelerLastPrinted":string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   "StatusReadyToPrint":boolean,
      /**  The last date the job status was mass printed.  */  
   "StatusLastPrinted":string,
      /**  The Service Call number that this Job is linked to.  */  
   "CallNum":number,
      /**  The Service Call Line that this Job is linked to.  */  
   "CallLine":number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   "JobType":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  The help desk case that created this job.  */  
   "HDCaseNum":number,
      /**  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  */  
   "ProductionYield":boolean,
      /**   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  */  
   "EquipID":string,
      /**   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  */  
   "PlanNum":number,
      /**  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   "IssueTopicID1":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  PersonIDName  */  
   "PersonIDName":string,
   "SOExists":boolean,
      /**  Part Description  */  
   "PartNumPartDescription":string,
      /**  Track Dimension  */  
   "PartNumTrackDimension":boolean,
      /**  Track Lots  */  
   "PartNumTrackLots":boolean,
      /**  Track Serial Num  */  
   "PartNumTrackSerialNum":boolean,
   "EquipOEM":string,
   "EquipModel":string,
   "EquipTypeID":string,
   "EquipLocID":string,
      /**  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  */  
   "PMJob":boolean,
   "EquipDescription":string,
   "JobTypeName":string,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  ID of related Attribute Class  */  
   "AttrClassID":string,
      /**  Description of values in set  */  
   "AttrDescription":string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   "ShortDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JobHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   "JobClosed":boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   "ClosedDate":string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   "JobComplete":boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   "JobCompletionDate":string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   "JobEngineered":boolean,
      /**   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff1":boolean,
      /**   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff2":boolean,
      /**   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff3":boolean,
      /**  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff4":boolean,
      /**  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff5":boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   "JobReleased":boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   "JobHeld":boolean,
      /**  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  */  
   "SchedStatus":string,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   "JobNum":string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   "PartNum":string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   "DrawNum":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "PartDescription":string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   "ProdQty":number,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   "IUM":string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "StartDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "StartHour":number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   "DueHour":number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   "ReqDueDate":string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   "JobCode":string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   "QuoteNum":number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   "QuoteLine":number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  UserChar1  */  
   "UserChar1":string,
      /**  UserChar2  */  
   "UserChar2":string,
      /**  UserChar3  */  
   "UserChar3":string,
      /**  UserChar4  */  
   "UserChar4":string,
      /**  UserDate1  */  
   "UserDate1":string,
      /**  UserDate2  */  
   "UserDate2":string,
      /**  UserDate3  */  
   "UserDate3":string,
      /**  UserDate4  */  
   "UserDate4":string,
      /**  UserDecimal1  */  
   "UserDecimal1":number,
      /**  UserDecimal2  */  
   "UserDecimal2":number,
      /**  UserInteger1  */  
   "UserInteger1":number,
      /**  UserInteger2  */  
   "UserInteger2":number,
      /**  Editor widget for Job header comments.  */  
   "CommentText":string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   "ExpenseCode":string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   "InCopyList":boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   "WIName":string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "WIStartDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "WIStartHour":number,
      /**  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   "WIDueDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   "WIDueHour":number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   "Candidate":boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   "SchedCode":string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   "SchedLocked":boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   "ProjectID":string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   "WIPCleared":boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   "JobFirm":boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   "PersonList":string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   "PersonID":string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   "ProdTeamID":string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   "QtyCompleted":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   "DatePurged":string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   "TravelerReadyToPrint":boolean,
      /**  The last date the job traveler was mass printed.  */  
   "TravelerLastPrinted":string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   "StatusReadyToPrint":boolean,
      /**  The last date the job status was mass printed.  */  
   "StatusLastPrinted":string,
      /**  The Service Call number that this Job is linked to.  */  
   "CallNum":number,
      /**  The Service Call Line that this Job is linked to.  */  
   "CallLine":number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   "JobType":string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   "RestoreFlag":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Indicates that the quantity on this job is locked  */  
   "LockQty":boolean,
      /**  The help desk case that created this job.  */  
   "HDCaseNum":number,
      /**   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  */  
   "ProcessMode":string,
      /**  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  */  
   "PlannedActionDate":string,
      /**  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  */  
   "PlannedKitDate":string,
      /**  The task ID that is returned from Microsoft Project.  */  
   "MSPTaskID":string,
      /**  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  */  
   "MSPPredecessor":string,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMapData":string,
      /**  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  */  
   "ProductionYield":boolean,
      /**  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  */  
   "OrigProdQty":number,
      /**  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  */  
   "PreserveOrigQtys":boolean,
      /**  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  */  
   "NoAutoCompletion":boolean,
      /**  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  */  
   "NoAutoClosing":boolean,
      /**  The user that created this Job.  */  
   "CreatedBy":string,
      /**  The date that this Job was created.  */  
   "CreateDate":string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   "WhseAllocFlag":boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   "OwnershipStatus":string,
      /**  Holds the internal object id of PDM parts.  */  
   "PDMObjID":string,
      /**  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   "ExportRequested":string,
      /**  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  */  
   "SplitMfgCostElements":boolean,
      /**  Cross Reference Part Num. Used for alternate serial mask support.  */  
   "XRefPartNum":string,
      /**   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  */  
   "XRefPartType":string,
      /**  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  */  
   "XRefCustNum":number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   "BasePartNum":string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   "BaseRevisionNum":string,
      /**  Indicates if the job was rough cut scheduled.  */  
   "RoughCutScheduled":boolean,
      /**   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  */  
   "EquipID":string,
      /**   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  */  
   "PlanNum":number,
      /**  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  */  
   "MaintPriority":string,
      /**  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  */  
   "SplitJob":boolean,
      /**  Indicates the type of prefix which is used for create jobs in MRP  */  
   "NumberSource":boolean,
      /**  The Meter Reading value entered at time of Job Closing.  */  
   "CloseMeterReading":number,
      /**  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   "IssueTopicID1":string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   "IssueTopicID2":string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   "IssueTopicID3":string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   "IssueTopicID4":string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   "IssueTopicID5":string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   "IssueTopicID6":string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   "IssueTopicID7":string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   "IssueTopicID8":string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   "IssueTopicID9":string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   "IssueTopicID10":string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   "IssueTopics":string,
      /**  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  */  
   "ResTopicID1":string,
      /**  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  */  
   "ResTopicID2":string,
      /**  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  */  
   "ResTopicID3":string,
      /**  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  */  
   "ResTopicID4":string,
      /**  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  */  
   "ResTopicID5":string,
      /**  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  */  
   "ResTopicID6":string,
      /**  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  */  
   "ResTopicID7":string,
      /**  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  */  
   "ResTopicID8":string,
      /**  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  */  
   "ResTopicID9":string,
      /**  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  */  
   "ResTopicID10":string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   "ResTopics":string,
      /**  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  */  
   "Forward":boolean,
      /**  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   "SchedSeq":number,
      /**  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  */  
   "PAAExists":boolean,
      /**  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  */  
   "DtlsWithinLeadTime":boolean,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  */  
   "RoughCut":boolean,
      /**  PlanGUID  */  
   "PlanGUID":string,
      /**  PlanUserID  */  
   "PlanUserID":string,
      /**  LastChangedBy  */  
   "LastChangedBy":string,
      /**  LastChangedOn  */  
   "LastChangedOn":string,
      /**  EPMExportLevel  */  
   "EPMExportLevel":number,
      /**  JobWorkflowState  */  
   "JobWorkflowState":string,
      /**  JobCSR  */  
   "JobCSR":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  LastExternalMESDate  */  
   "LastExternalMESDate":string,
      /**  LastScheduleDate  */  
   "LastScheduleDate":string,
      /**  LastScheduleProc  */  
   "LastScheduleProc":string,
      /**  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   "SchedPriority":number,
      /**  It indicates the days a job is going to be late in relation to its required due date  */  
   "DaysLate":number,
      /**  ContractID  */  
   "ContractID":string,
      /**  Logical field to indicate if this record has been read by project analysis process  */  
   "ProjProcessed":boolean,
      /**  SyncReqBy  */  
   "SyncReqBy":boolean,
      /**  CustName  */  
   "CustName":string,
      /**  CustID  */  
   "CustID":string,
      /**  IsCSRSet  */  
   "IsCSRSet":boolean,
      /**  UnReadyCostProcess  */  
   "UnReadyCostProcess":boolean,
      /**  ProcSuspendedUpdates  */  
   "ProcSuspendedUpdates":string,
      /**  DateTime field to indicate when this record has been read by project analysis process  */  
   "ProjProcessedDate":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   "KBConfigProdID":number,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   "UseAdvancedStaging":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  PersonIDName  */  
   "PersonIDName":string,
      /**  This flag indicates if the job is ready to be fulfilled.  */  
   "ReadyToFulfill":boolean,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  FSMServiceReportID  */  
   "FSMServiceReportID":string,
   "AdvanceLaborRate":boolean,
      /**  Calculated field is set Not UnReadyCostProcess  */  
   "dspReadyCostProcess":boolean,
      /**  Determine if jobengineered is enabled or disabled.  */  
   "EnableJobEngineered":boolean,
      /**  Should JobFirm be enabled or disabled?  */  
   "EnableJobFirm":boolean,
      /**  Determine if jobreleased is enabled or disabled.  */  
   "EnableJobReleased":boolean,
   "EnableMaterialStatus":boolean,
   "EnableProject":boolean,
      /**  Is the job allowed to be engineered?  */  
   "EngineerAllowed":boolean,
   "EquipLocDesc":string,
      /**  If some fields except ToFirm have been updated  */  
   "ExtUpdated":boolean,
      /**   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  */  
   "FinalOpDueDate":string,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   "FirmProcEnable":boolean,
      /**  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  */  
   "FirmProcess":boolean,
      /**  Job has at least one assembly with flag Plan as Assembly.  */  
   "HasPlanAsAsm":boolean,
      /**  Depending on the engineered job flag, is the header information enabled?  */  
   "HeaderSensitive":boolean,
      /**  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  */  
   "IgnoreMtlConstraints":boolean,
   "JobTypeName":string,
      /**  If part is backflush the kit time is ignored.  */  
   "KitTime":number,
      /**  Locked Qty Flag  */  
   "LockedQty":boolean,
   "NewMeter":number,
      /**  The old Job Number when JobFirm is changed from no to yes.  */  
   "OldJobNum":string,
      /**  The order qty  */  
   "OrderQty":number,
      /**  Logical field signifying whether JobHead.PartNum is a valid part master part.  */  
   "PartmasterPart":boolean,
   "PhaseDescription":string,
      /**  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  */  
   "PMJob":boolean,
      /**  Process Mode Description  */  
   "ProcessModeDescription":string,
      /**  Receive Time field for Job Part entered on Job  */  
   "ReceiveTime":number,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
   "SOExists":boolean,
   "StockQty":number,
      /**  To be Firmed  */  
   "ToFirm":boolean,
      /**  Description for XRefPartType  */  
   "XRefPartTypeDesc":string,
      /**  The audit change description for the jobaudit record.  */  
   "ChangeDescription":string,
   "ClearDataset":boolean,
      /**  True if more than one co-part exists  */  
   "IsCoPart":boolean,
      /**  The identifier of related Process Manufacturing.  */  
   "PartRevProcessMfgID":string,
      /**  Type of Process Manufacturing.  */  
   "PartRevProcessMfgType":string,
      /**  Determines if the Service Job has to be synchronized with Epicor FSI application.  */  
   "SendToFSA":boolean,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "CallLineLineDesc":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "EquipMeterUOM":string,
   "EquipSerialNum":string,
   "EquipLocID":string,
   "EquipPlant":string,
   "EquipDescription":string,
   "EquipBrand":string,
   "EquipModel":string,
   "EquipCurrentMeter":number,
   "EquipTypeID":string,
   "EquipOEM":string,
   "ExpenseCodeDescription":string,
   "HDCaseDescription":string,
   "IssueTopicID1Description":string,
   "IssueTopicID10Description":string,
   "IssueTopicID2Description":string,
   "IssueTopicID3Description":string,
   "IssueTopicID4Description":string,
   "IssueTopicID5Description":string,
   "IssueTopicID6Description":string,
   "IssueTopicID7Description":string,
   "IssueTopicID8Description":string,
   "IssueTopicID9Description":string,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumLocationIDNumReq":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumAttrClassID":string,
   "PlantName":string,
   "PlantMaintPlant":string,
   "ProdCodeDescription":string,
   "ProdTeamIDDescription":string,
   "ProdTeamIDName":string,
   "ProjectIDDescription":string,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
   "ResTopicID1Description":string,
   "ResTopicID10Description":string,
   "ResTopicID2Description":string,
   "ResTopicID3Description":string,
   "ResTopicID4Description":string,
   "ResTopicID5Description":string,
   "ResTopicID6Description":string,
   "ResTopicID7Description":string,
   "ResTopicID8Description":string,
   "ResTopicID9Description":string,
   "SchedCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
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
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param jobNum
   */  
export interface DeleteByID_input{
   jobNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_JobHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   JobClosed:boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   ClosedDate:string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   JobComplete:boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   JobCompletionDate:string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   JobEngineered:boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   JobReleased:boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   JobHeld:boolean,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   DrawNum:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   PartDescription:string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   ProdQty:number,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   IUM:string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   StartDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   StartHour:number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   DueHour:number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   ReqDueDate:string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   JobCode:string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   QuoteNum:number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   QuoteLine:number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  Editor widget for Job header comments.  */  
   CommentText:string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   ExpenseCode:string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   InCopyList:boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   WIName:string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   WIStartDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   WIStartHour:number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   Candidate:boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   SchedCode:string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   SchedLocked:boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   ProjectID:string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   WIPCleared:boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   JobFirm:boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   PersonList:string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   PersonID:string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   ProdTeamID:string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   QtyCompleted:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   DatePurged:string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   TravelerReadyToPrint:boolean,
      /**  The last date the job traveler was mass printed.  */  
   TravelerLastPrinted:string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   StatusReadyToPrint:boolean,
      /**  The last date the job status was mass printed.  */  
   StatusLastPrinted:string,
      /**  The Service Call number that this Job is linked to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is linked to.  */  
   CallLine:number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   JobType:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  The help desk case that created this job.  */  
   HDCaseNum:number,
      /**  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  */  
   ProductionYield:boolean,
      /**   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  */  
   EquipID:string,
      /**   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  */  
   PlanNum:number,
      /**  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   IssueTopicID1:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  PersonIDName  */  
   PersonIDName:string,
   SOExists:boolean,
      /**  Part Description  */  
   PartNumPartDescription:string,
      /**  Track Dimension  */  
   PartNumTrackDimension:boolean,
      /**  Track Lots  */  
   PartNumTrackLots:boolean,
      /**  Track Serial Num  */  
   PartNumTrackSerialNum:boolean,
   EquipOEM:string,
   EquipModel:string,
   EquipTypeID:string,
   EquipLocID:string,
      /**  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  */  
   PMJob:boolean,
   EquipDescription:string,
   JobTypeName:string,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  Description of values in set  */  
   AttrDescription:string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   ShortDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobHeadListTableset{
   JobHeadList:Erp_Tablesets_JobHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   JobClosed:boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   ClosedDate:string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   JobComplete:boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   JobCompletionDate:string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   JobEngineered:boolean,
      /**   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff1:boolean,
      /**   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff2:boolean,
      /**   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff3:boolean,
      /**  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff4:boolean,
      /**  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff5:boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   JobReleased:boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   JobHeld:boolean,
      /**  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  */  
   SchedStatus:string,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   DrawNum:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   PartDescription:string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   ProdQty:number,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   IUM:string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   StartDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   StartHour:number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   DueHour:number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   ReqDueDate:string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   JobCode:string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   QuoteNum:number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   QuoteLine:number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  UserChar1  */  
   UserChar1:string,
      /**  UserChar2  */  
   UserChar2:string,
      /**  UserChar3  */  
   UserChar3:string,
      /**  UserChar4  */  
   UserChar4:string,
      /**  UserDate1  */  
   UserDate1:string,
      /**  UserDate2  */  
   UserDate2:string,
      /**  UserDate3  */  
   UserDate3:string,
      /**  UserDate4  */  
   UserDate4:string,
      /**  UserDecimal1  */  
   UserDecimal1:number,
      /**  UserDecimal2  */  
   UserDecimal2:number,
      /**  UserInteger1  */  
   UserInteger1:number,
      /**  UserInteger2  */  
   UserInteger2:number,
      /**  Editor widget for Job header comments.  */  
   CommentText:string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   ExpenseCode:string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   InCopyList:boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   WIName:string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   WIStartDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   WIStartHour:number,
      /**  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   WIDueHour:number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   Candidate:boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   SchedCode:string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   SchedLocked:boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   ProjectID:string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   WIPCleared:boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   JobFirm:boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   PersonList:string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   PersonID:string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   ProdTeamID:string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   QtyCompleted:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   DatePurged:string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   TravelerReadyToPrint:boolean,
      /**  The last date the job traveler was mass printed.  */  
   TravelerLastPrinted:string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   StatusReadyToPrint:boolean,
      /**  The last date the job status was mass printed.  */  
   StatusLastPrinted:string,
      /**  The Service Call number that this Job is linked to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is linked to.  */  
   CallLine:number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   JobType:string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Indicates that the quantity on this job is locked  */  
   LockQty:boolean,
      /**  The help desk case that created this job.  */  
   HDCaseNum:number,
      /**   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  */  
   ProcessMode:string,
      /**  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  */  
   PlannedActionDate:string,
      /**  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  */  
   PlannedKitDate:string,
      /**  The task ID that is returned from Microsoft Project.  */  
   MSPTaskID:string,
      /**  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  */  
   MSPPredecessor:string,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  */  
   ProductionYield:boolean,
      /**  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  */  
   OrigProdQty:number,
      /**  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  */  
   PreserveOrigQtys:boolean,
      /**  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  */  
   NoAutoCompletion:boolean,
      /**  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  */  
   NoAutoClosing:boolean,
      /**  The user that created this Job.  */  
   CreatedBy:string,
      /**  The date that this Job was created.  */  
   CreateDate:string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  Holds the internal object id of PDM parts.  */  
   PDMObjID:string,
      /**  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   ExportRequested:string,
      /**  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  */  
   SplitMfgCostElements:boolean,
      /**  Cross Reference Part Num. Used for alternate serial mask support.  */  
   XRefPartNum:string,
      /**   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  */  
   XRefPartType:string,
      /**  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  */  
   XRefCustNum:number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**  Indicates if the job was rough cut scheduled.  */  
   RoughCutScheduled:boolean,
      /**   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  */  
   EquipID:string,
      /**   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  */  
   PlanNum:number,
      /**  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  */  
   MaintPriority:string,
      /**  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  */  
   SplitJob:boolean,
      /**  Indicates the type of prefix which is used for create jobs in MRP  */  
   NumberSource:boolean,
      /**  The Meter Reading value entered at time of Job Closing.  */  
   CloseMeterReading:number,
      /**  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   IssueTopicID1:string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   IssueTopicID2:string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   IssueTopicID3:string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   IssueTopicID4:string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   IssueTopicID5:string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   IssueTopicID6:string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   IssueTopicID7:string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   IssueTopicID8:string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   IssueTopicID9:string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   IssueTopicID10:string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   IssueTopics:string,
      /**  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  */  
   ResTopicID1:string,
      /**  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  */  
   ResTopicID2:string,
      /**  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  */  
   ResTopicID3:string,
      /**  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  */  
   ResTopicID4:string,
      /**  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  */  
   ResTopicID5:string,
      /**  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  */  
   ResTopicID6:string,
      /**  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  */  
   ResTopicID7:string,
      /**  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  */  
   ResTopicID8:string,
      /**  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  */  
   ResTopicID9:string,
      /**  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  */  
   ResTopicID10:string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   ResTopics:string,
      /**  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  */  
   Forward:boolean,
      /**  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   SchedSeq:number,
      /**  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  */  
   PAAExists:boolean,
      /**  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  */  
   DtlsWithinLeadTime:boolean,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  */  
   RoughCut:boolean,
      /**  PlanGUID  */  
   PlanGUID:string,
      /**  PlanUserID  */  
   PlanUserID:string,
      /**  LastChangedBy  */  
   LastChangedBy:string,
      /**  LastChangedOn  */  
   LastChangedOn:string,
      /**  EPMExportLevel  */  
   EPMExportLevel:number,
      /**  JobWorkflowState  */  
   JobWorkflowState:string,
      /**  JobCSR  */  
   JobCSR:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  LastExternalMESDate  */  
   LastExternalMESDate:string,
      /**  LastScheduleDate  */  
   LastScheduleDate:string,
      /**  LastScheduleProc  */  
   LastScheduleProc:string,
      /**  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   SchedPriority:number,
      /**  It indicates the days a job is going to be late in relation to its required due date  */  
   DaysLate:number,
      /**  ContractID  */  
   ContractID:string,
      /**  Logical field to indicate if this record has been read by project analysis process  */  
   ProjProcessed:boolean,
      /**  SyncReqBy  */  
   SyncReqBy:boolean,
      /**  CustName  */  
   CustName:string,
      /**  CustID  */  
   CustID:string,
      /**  IsCSRSet  */  
   IsCSRSet:boolean,
      /**  UnReadyCostProcess  */  
   UnReadyCostProcess:boolean,
      /**  ProcSuspendedUpdates  */  
   ProcSuspendedUpdates:string,
      /**  DateTime field to indicate when this record has been read by project analysis process  */  
   ProjProcessedDate:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   UseAdvancedStaging:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  PersonIDName  */  
   PersonIDName:string,
      /**  This flag indicates if the job is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  FSMServiceReportID  */  
   FSMServiceReportID:string,
   AdvanceLaborRate:boolean,
      /**  Calculated field is set Not UnReadyCostProcess  */  
   dspReadyCostProcess:boolean,
      /**  Determine if jobengineered is enabled or disabled.  */  
   EnableJobEngineered:boolean,
      /**  Should JobFirm be enabled or disabled?  */  
   EnableJobFirm:boolean,
      /**  Determine if jobreleased is enabled or disabled.  */  
   EnableJobReleased:boolean,
   EnableMaterialStatus:boolean,
   EnableProject:boolean,
      /**  Is the job allowed to be engineered?  */  
   EngineerAllowed:boolean,
   EquipLocDesc:string,
      /**  If some fields except ToFirm have been updated  */  
   ExtUpdated:boolean,
      /**   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  */  
   FinalOpDueDate:string,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   FirmProcEnable:boolean,
      /**  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  */  
   FirmProcess:boolean,
      /**  Job has at least one assembly with flag Plan as Assembly.  */  
   HasPlanAsAsm:boolean,
      /**  Depending on the engineered job flag, is the header information enabled?  */  
   HeaderSensitive:boolean,
      /**  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  */  
   IgnoreMtlConstraints:boolean,
   JobTypeName:string,
      /**  If part is backflush the kit time is ignored.  */  
   KitTime:number,
      /**  Locked Qty Flag  */  
   LockedQty:boolean,
   NewMeter:number,
      /**  The old Job Number when JobFirm is changed from no to yes.  */  
   OldJobNum:string,
      /**  The order qty  */  
   OrderQty:number,
      /**  Logical field signifying whether JobHead.PartNum is a valid part master part.  */  
   PartmasterPart:boolean,
   PhaseDescription:string,
      /**  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  */  
   PMJob:boolean,
      /**  Process Mode Description  */  
   ProcessModeDescription:string,
      /**  Receive Time field for Job Part entered on Job  */  
   ReceiveTime:number,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
   SOExists:boolean,
   StockQty:number,
      /**  To be Firmed  */  
   ToFirm:boolean,
      /**  Description for XRefPartType  */  
   XRefPartTypeDesc:string,
      /**  The audit change description for the jobaudit record.  */  
   ChangeDescription:string,
   ClearDataset:boolean,
      /**  True if more than one co-part exists  */  
   IsCoPart:boolean,
      /**  The identifier of related Process Manufacturing.  */  
   PartRevProcessMfgID:string,
      /**  Type of Process Manufacturing.  */  
   PartRevProcessMfgType:string,
      /**  Determines if the Service Job has to be synchronized with Epicor FSI application.  */  
   SendToFSA:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   EquipMeterUOM:string,
   EquipSerialNum:string,
   EquipLocID:string,
   EquipPlant:string,
   EquipDescription:string,
   EquipBrand:string,
   EquipModel:string,
   EquipCurrentMeter:number,
   EquipTypeID:string,
   EquipOEM:string,
   ExpenseCodeDescription:string,
   HDCaseDescription:string,
   IssueTopicID1Description:string,
   IssueTopicID10Description:string,
   IssueTopicID2Description:string,
   IssueTopicID3Description:string,
   IssueTopicID4Description:string,
   IssueTopicID5Description:string,
   IssueTopicID6Description:string,
   IssueTopicID7Description:string,
   IssueTopicID8Description:string,
   IssueTopicID9Description:string,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumLocationIDNumReq:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PlantName:string,
   PlantMaintPlant:string,
   ProdCodeDescription:string,
   ProdTeamIDDescription:string,
   ProdTeamIDName:string,
   ProjectIDDescription:string,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
   ResTopicID1Description:string,
   ResTopicID10Description:string,
   ResTopicID2Description:string,
   ResTopicID3Description:string,
   ResTopicID4Description:string,
   ResTopicID5Description:string,
   ResTopicID6Description:string,
   ResTopicID7Description:string,
   ResTopicID8Description:string,
   ResTopicID9Description:string,
   SchedCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQEntryJobSearchTableset{
   JobHead:Erp_Tablesets_JobHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtRFQEntryJobSearchTableset{
   JobHead:Erp_Tablesets_JobHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param jobNum
   */  
export interface GetByID_input{
   jobNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_RFQEntryJobSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_RFQEntryJobSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_RFQEntryJobSearchTableset[],
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
   returnObj:Erp_Tablesets_JobHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewJobHead_input{
   ds:Erp_Tablesets_RFQEntryJobSearchTableset[],
}

export interface GetNewJobHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryJobSearchTableset,
}
}

   /** Required : 
      @param whereClauseJobHead
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseJobHead:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_RFQEntryJobSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtRFQEntryJobSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtRFQEntryJobSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_RFQEntryJobSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQEntryJobSearchTableset,
}
}

