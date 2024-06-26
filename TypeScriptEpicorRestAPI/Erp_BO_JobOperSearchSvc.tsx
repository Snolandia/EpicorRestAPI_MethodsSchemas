import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.JobOperSearchSvc
// Description: Search object for Job Operations
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/$metadata", {
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
   Description: Get JobOperSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobOperSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobOperRow
   */  
export function get_JobOperSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobOperRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/JobOperSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobOperRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobOperSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobOperRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.JobOperRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobOperSearches(requestBody:Erp_Tablesets_JobOperRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/JobOperSearches", {
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
   Summary: Calls GetByID to retrieve the JobOperSearch item
   Description: Calls GetByID to retrieve the JobOperSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobOperSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.JobOperRow
   */  
export function get_JobOperSearches_Company_JobNum_AssemblySeq_OprSeq(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobOperRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/JobOperSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")", {
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
         resolve(data as Erp_Tablesets_JobOperRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JobOperSearch for the service
   Description: Calls UpdateExt to update JobOperSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobOperSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobOperRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JobOperSearches_Company_JobNum_AssemblySeq_OprSeq(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, requestBody:Erp_Tablesets_JobOperRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/JobOperSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")", {
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
   Summary: Call UpdateExt to delete JobOperSearch item
   Description: Call UpdateExt to delete JobOperSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobOperSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JobOperSearches_Company_JobNum_AssemblySeq_OprSeq(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/JobOperSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobOperListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobOperListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobOperListRow)
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
export function get_GetRows(whereClauseJobOper:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobOper!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobOper=" + whereClauseJobOper
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/GetRows" + params, {
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(jobNum:string, assemblySeq:string, oprSeq:string, epicorHeaders?:Headers){
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
   if(typeof oprSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "oprSeq=" + oprSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewJobOper
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobOper
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewJobOper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobOper_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobOper(requestBody:GetNewJobOper_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewJobOper_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/GetNewJobOper", {
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
         resolve(data as GetNewJobOper_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobOperSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobOperListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobOperListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobOperRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobOperRow,
}

export interface Erp_Tablesets_JobOperListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobOper records are also marked.  This is used to make database access to open operation records more efficient.  */  
   "JobComplete":boolean,
      /**   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  */  
   "OpComplete":boolean,
      /**  Job Number  */  
   "JobNum":string,
      /**  Assembly Sequence # that this Operation is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  */  
   "OpCode":string,
      /**   The Operation standard ID.  This links the JobOper to the OpStd master file.  This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   "OpStdID":string,
      /**  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  */  
   "EstSetHours":number,
      /**   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  */  
   "EstProdHours":number,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   "ProdStandard":number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   "StdFormat":string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   "StdBasis":string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   "OpsPerPart":number,
      /**  Production Quantity per one of the Parent Item.  */  
   "QtyPer":number,
      /**  Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   "QueStartDate":string,
      /**  Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   "QueStartHour":number,
      /**  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   "StartDate":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   "StartHour":number,
      /**  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   "DueHour":number,
      /**  Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   "MoveDueDate":string,
      /**  Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   "MoveDueHour":number,
      /**  Labor rate used for estimated production labor costs. Default from the OpMaster.ProdLabRate.  */  
   "ProdLabRate":number,
      /**  Labor rate for estimated setup labor costs. Default from the OpMaster.SetupLabRate.  */  
   "SetupLabRate":number,
      /**  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.ProdBurRate.  */  
   "ProdBurRate":number,
      /**  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.SetupBurRate.  */  
   "SetupBurRate":number,
      /**  This indicates if this is an "added operation". An added operation is one that was not planned on.  */  
   "AddedOper":boolean,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   "Machines":number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   "SetUpCrewSize":number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   "ProdCrewSize":number,
      /**  A flag indicating if the production is complete for this operation. It is updated via Labor Entry.  */  
   "ProdComplete":boolean,
      /**  Flag that indicates if Setup is complete on this operation. This flag is only used when the operation has EstSetupHours > 0.00.  */  
   "SetupComplete":boolean,
      /**  Total Actual Production Hours. A summary of non-setup LaborDtl.BurdenHrs. This includes REWORK hours.  This is maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActReworkHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H").  */  
   "ActProdHours":number,
      /**  Total Actual Production Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "P" and Rework = Yes. This number is also included as part of the JobOPer.ActProdHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActProdHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   "ActProdRwkHours":number,
      /**  Actual setup hours.  A summary of setup (LaborDtl.LaborType = S) labor transactions hours (LaborDtl.Burden). Actual Setup hours reduce the shop load if the system is configured to remove load based on hours (JCSyst.RemoveLoad = "H").  */  
   "ActSetupHours":number,
      /**  Total Actual Setup Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "S" and Rework = Yes. This number is also included as part of the JobOPer.ActSetupHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActSetHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   "ActSetupRwkHours":number,
      /**   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  */  
   "QtyCompleted":number,
      /**  Setup function percent complete.  Maintained via labor entry.  */  
   "SetupPctComplete":number,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   "SubContract":boolean,
      /**  Inventory UOM  */  
   "IUM":string,
      /**  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  */  
   "EstUnitCost":number,
      /**  Hours required is calculated as days * 8.  */  
   "DaysOut":number,
      /**  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  */  
   "PartNum":string,
      /**  Description used only for subcontract operations  */  
   "Description":string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   "PurPoint":string,
      /**  Editor widget for Job operation comments.  */  
   "CommentText":string,
      /**   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   "SchedRelation":string,
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   "RunQty":number,
      /**   This field is blank or contains the UserID. When not blank it indicates that the operations schedule has been changed and is considered as being in a "What If" mode.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   "WIName":string,
      /**  This is the What-If number of machines that this operation will run on at the same time.  Setup by and for scheduling from the Machines field.  */  
   "WIMachines":number,
      /**  What-if Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   "WIQueStartDate":string,
      /**  What-if Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   "WIQueStartHour":number,
      /**  What if Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   "WIStartDate":string,
      /**  This field is established by scheduling. It represents the What If "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   "WIStartHour":number,
      /**  What If Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   "WIDueDate":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   "WIDueHour":number,
      /**  What-If Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   "WIMoveDueDate":string,
      /**  What-if Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   "WIMoveDueHour":number,
      /**  The Number of Hours per machine per day that this operations "What If" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining ShopLoad records.  */  
   "WIHoursPerMachine":number,
      /**  Date at which the operations current outstanding "What-If" load starts at.  Updated by the JobOper write trigger. (See LoadDate)  */  
   "WILoadDate":string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding "What-If"  load. Related to WILoadDate.  */  
   "WILoadHour":number,
      /**  Total Burden cost to date. This is update via the LaborDtl\Write.p trigger procedure. It includes ALL burden costs (Setup, Production and Rework)  */  
   "ActBurCost":number,
      /**   FOR NON-SUBCONTRACT OPERATIONS: Total of "ALL" labor costs to date. This includes Setup, Production and Rework. Updated via the LaborDtl.Write.p trigger.
FOR SUBCONTRACT OPERATIONS: The Total Cost, updated via the receipt process.  */  
   "ActLabCost":number,
      /**  Total Rework Burden cost todate. This value is also included in the ActBurCost total. It includes both setup & production rework. Updated via LaborDtl\Write.P trigger.  */  
   "ReworkBurCost":number,
      /**  Total Rework Labor cost to date. This value is also included in the ActLabCost field. This includes both Setup & Production. Updated via the LaborDtl\Write.p trigger.  */  
   "ReworkLabCost":number,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   "MiscAmt":number,
      /**  The Number of Hours per machine per day that this operations "actual" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining the ShopLoad records.  */  
   "HoursPerMachine":number,
      /**   Date at which the operations current outstanding load starts at.
Ex: Op schedule is 2/1/97 - 2/10/97, initially LoadDate = 2/1/97. As load is relieved through labor processing the LoadDate moves forward accordingly. When 1/2 completed the LoadDate would be 2/5/97. This field is primarily used by the Scheduling Board to calculate the graphical image of outstanding load.  Updated by the JobOper write trigger.  */  
   "LoadDate":string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding load. Related to LoadDate.  */  
   "LoadHour":number,
      /**  Internally used field to prevent redundant read of JobOper during execution of "Reloader" program. (See WrkCenter.ReloadNum)  */  
   "ReloadNum":number,
      /**  Controls if an alert is to be sent when this JobOper is completed.  */  
   "SndAlrtCmpl":boolean,
      /**  Indicates if  Inspection is required when items are received to this JobOper (subcontract only). Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  Identical to JobHead.JobEngineered.  ShopLoad capacity is only allocated to Jobs where JobEngineered = YES.  */  
   "JobEngineered":boolean,
      /**   The estimated set up hours per machine.
Default from OpStd.SetupHours.  Used to calculate JobOper.EstSetupHours.  */  
   "EstSetHoursPerMch":number,
      /**   Part Revision number.
Pertains to subcontracting operations only.   An optional field.   Related JobAsmbl.RevisionNum is used as the default.  */  
   "RevisionNum":string,
      /**  Currently not used. Prep for future development.  */  
   "AutoReceiptDate":string,
      /**  The labor date of the last labor transaction that was posted to this operation.  Used by the JobOper write trigger Auto Receieve logic.  */  
   "LastLaborDate":string,
      /**  The service call that this operation belongs to.  */  
   "CallNum":number,
      /**  The Service Call Line that this operation relates to.  */  
   "CallLine":number,
      /**  Labor rate used for  time on an operation.  Time per hour per technician. in base currency.  */  
   "LaborRate":number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. in base currency. This field considers the percentage coverage of a warranty or contract.  */  
   "BillableLaborRate":number,
      /**  Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. Does not consider warranty or contract  */  
   "DocLaborRate":number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. considers warranty or contract  */  
   "DocBillableLaborRate":number,
      /**  FS - Is this a billable operation.  */  
   "Billable":boolean,
      /**  FS - Unit Price for the subcontract in base currency.  */  
   "UnitPrice":number,
      /**  FS - Billable Unit Price for the subcontract in base currency.  */  
   "BillableUnitPrice":number,
      /**  FS - Billable Price per unit for the subcontract in customers currency.  */  
   "DocBillableUnitPrice":number,
      /**  FS - Unit Price for the for the Subcontract in Customer currency.  */  
   "DocUnitPrice":number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   "LaborEntryMethod":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   "PricePerCode":string,
      /**  The quantity requested for first article inspection.  */  
   "FAQty":number,
      /**  The "to date" quantity that has been moved to the input Warehouse/Bin of the subsequent operations ResourceGroup/Resource input Warehouse/Bin.  This is NOT A balance.  It is a "to date" value.  It is not reduced as it is consumed.  Used in calculation of "Outstanding" WIP in the Request Material/WIP program (ame30-dg.w).  Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the WIP material in/out of the staging area (Issues, Returns).  */  
   "QtyStagedToDate":number,
      /**  A flag to indicate that this job operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   "RFQNeeded":boolean,
      /**  The number of vendor quotes that are required for this job subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  RFQ number that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   "RFQStat":string,
      /**  Used to group operation to save on setups.  */  
   "SetupGroup":string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   "RestoreFlag":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**   Identifies the primary JobOpDtl to be used for setup.  The setup time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = S or B.  */  
   "PrimarySetupOpDtl":number,
      /**   Identifies the primary JobOpDtl to be used for production.  The production run time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = P or B.  */  
   "PrimaryProdOpDtl":number,
      /**  Operation Description.  */  
   "OpDesc":string,
      /**  Kit Date. Not directly maintanable. Updated via the scheduling process.  */  
   "KitDate":string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   "GlbRFQ":boolean,
      /**  Booked Unit Cost  */  
   "BookedUnitCost":number,
      /**   Initially defaulted to false. This flag is set to true at the time JobOper.ProdComplete is set to true if JobHead.ProductionYield = true and OpMaster. PrdYldRecalcExpected = true and the actual completed qty for the operation vs. the expected completion qty is out of variance based on the under percentage set in OpMaster. This flag is used by the production yield recalculation logic to determine if recalculation is required for a job.
This field is maintained by the system only.  */  
   "RecalcExpProdYld":boolean,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMapData":string,
      /**  When true this would signify that this operation was rough cut scheduled - meaning the operation would have start and end dates but no supporting resourcetimeused or shopload records.  */  
   "RoughCutSched":boolean,
      /**  Scheduling Comments  */  
   "SchedComment":string,
      /**  Reporting currency value of this field  */  
   "Rpt1BillableLaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt2BillableLaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt3BillableLaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt1BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1LaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt2LaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt3LaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   "SNRequiredOpr":boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   "SNRequiredSubConShip":boolean,
      /**  Operation Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Operation Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   "SendAheadType":string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   "SendAheadOffset":number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   "PrjRoleList":string,
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   "TearDwnEndDate":string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   "TearDwnEndHour":number,
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   "WITearDwnEndDate":string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   "WITearDwnEndHour":number,
   "UseAllRoles":boolean,
      /**  The PartNum for the asset. This should be disabled for a service call job, in which case the asset information would be transferred from the service call line when an operation is created for the job.  */  
   "AssetPartNum":string,
      /**  Serial number of the asset.  */  
   "SerialNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   "QtyPerCycle":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The calculated production quantity  */  
   "ProductionQty":number,
      /**  The calculated scrap quantity  */  
   "ScrapQty":number,
      /**  The calculated estimated labor hours  */  
   "EstLabHours":number,
      /**  The display service labor rate  */  
   "DisplayServLaborRate":number,
      /**  The display service amount.  */  
   "DisplayServAmt":number,
      /**  The converted display service labor rate.  */  
   "DocDisplayServLaborRate":number,
      /**  The converted display service amount.  */  
   "DocDisplayServAmt":number,
   "DisplayExtPrice":number,
      /**  Final operation  */  
   "FinalOpr":boolean,
      /**  Auto receive flag  */  
   "AutoReceive":boolean,
      /**  Calculated display unit price  */  
   "DisplayUnitPrice":number,
      /**  The currency switch flag.  */  
   "CurrencySwitch":boolean,
      /**  The document display unit price  */  
   "DocDisplayUnitPrice":number,
      /**  The document display extended price  */  
   "DocDisplayExtPrice":number,
      /**  Contains the value of which icon to display in tree for joboper  */  
   "ShowStatusIcon":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   "EnableSndAlrtCmpl":boolean,
      /**  Field to determine to enable or disable autoreceive.  */  
   "EnableAutoReceive":boolean,
   "OpStdDescription":string,
      /**  The Resource Group ID of the primary production operation detail.  */  
   "PrimaryResourceGrpID":string,
      /**  Primary Resource Group Description  */  
   "PrimaryResourceGrpDesc":string,
      /**  This is the description of the Method for Labor Entry.  Can be "Time and Quantity" for 'T', "Quantity Only" for 'Q' or "Backflush" for 'B'.  */  
   "LaborEntryMethodDesc":string,
      /**  Indicates if the scheduling resources should be refreshed when the op code changes.  */  
   "RefreshResources":boolean,
      /**  StdFormat Description  */  
   "StdFormatDescription":string,
      /**  StdBasis Description  */  
   "StdBasisDescription":string,
      /**  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   "PrimaryProdOpDtlDesc":string,
      /**  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   "PrimarySetupOpDtlDesc":string,
      /**  For SubContract Operations equals to the ActLaborCost  */  
   "ActSubCost":number,
      /**  For non subconctract operations JobOper.EstSetHours * JobOper.SetupBurRate + JobOper.EstProdHours * JobOper.ProdBurRate  */  
   "EstBurdenCost":number,
      /**  For non subcontract operations : JobOper.EstSetHours * JobOper.SetupCrewSize * JobOper.SetupLabRate +JobOper.EstProdHours * JobOper.ProdCrewSize * JobOper.ProdLabRate  */  
   "EstLaborCost":number,
      /**  For SubContract operations: JobOper.EstUnitCost * JobOper.RunQty  */  
   "EstSubCost":number,
      /**  Flag to allow/disallow the user to see the Job Costs.  */  
   "AllowJobCosts":string,
      /**  The total Load Hours calculated by summing the SetUpLoadHrs + ProdLoadHrs.  */  
   "LoadHrs":number,
      /**  IsBaseCurrency  */  
   "IsBaseCurrency":boolean,
   "EnableSNRequiredOpr":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "Rpt1DisplayServLaborRate":number,
   "Rpt2DisplayServLaborRate":number,
   "Rpt3DisplayServLaborRate":number,
   "Rpt1DisplayServAmt":number,
   "Rpt2DisplayServAmt":number,
   "Rpt3DisplayServAmt":number,
   "Rpt1DisplayUnitPrice":number,
   "Rpt2DisplayUnitPrice":number,
   "Rpt3DisplayUnitPrice":number,
   "Rpt1DisplayExtPrice":number,
   "Rpt2DisplayExtPrice":number,
   "Rpt3DisplayExtPrice":number,
      /**  This external field is used as a flag to determine when to enable/disable the SNRequiredSubConShip field on UI screen.  */  
   "EnableSNReqSubConShip":boolean,
      /**  Display IUM field (readonly)  */  
   "DspIUM":string,
      /**  Description  */  
   "AnalysisCdDescription":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "CallLineLineDesc":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   "OpCodeOpDesc":string,
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
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   "RFQLineLineDesc":string,
      /**  Description of Setup Group.  */  
   "SetupGroupDescription":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Second address line  */  
   "VendorPPAddress2":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "VendorPPCountry":string,
      /**  State portion of the address  */  
   "VendorPPState":string,
      /**  Third address line  */  
   "VendorPPAddress3":string,
      /**  Purchase Point Name...can't be blank.  */  
   "VendorPPName":string,
      /**  Postal Code or Zip code portion of the address  */  
   "VendorPPZip":string,
      /**  City portion of the address  */  
   "VendorPPCity":string,
      /**  First address line  */  
   "VendorPPAddress1":string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "VendorPPPrimPCon":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JobOperRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobOper records are also marked.  This is used to make database access to open operation records more efficient.  */  
   "JobComplete":boolean,
      /**   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  */  
   "OpComplete":boolean,
      /**  Job Number  */  
   "JobNum":string,
      /**  Assembly Sequence # that this Operation is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  */  
   "OpCode":string,
      /**   The Operation standard ID.  This links the JobOper to the OpStd master file.  This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   "OpStdID":string,
      /**  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  */  
   "EstSetHours":number,
      /**   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  */  
   "EstProdHours":number,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   "ProdStandard":number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   "StdFormat":string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   "StdBasis":string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   "OpsPerPart":number,
      /**  Production Quantity per one of the Parent Item.  */  
   "QtyPer":number,
      /**  Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   "QueStartDate":string,
      /**  Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   "QueStartHour":number,
      /**  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   "StartDate":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   "StartHour":number,
      /**  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   "DueHour":number,
      /**  Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   "MoveDueDate":string,
      /**  Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   "MoveDueHour":number,
      /**  Labor rate used for estimated production labor costs. Default from the OpMaster.ProdLabRate.  */  
   "ProdLabRate":number,
      /**  Labor rate for estimated setup labor costs. Default from the OpMaster.SetupLabRate.  */  
   "SetupLabRate":number,
      /**  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.ProdBurRate.  */  
   "ProdBurRate":number,
      /**  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.SetupBurRate.  */  
   "SetupBurRate":number,
      /**  This indicates if this is an "added operation". An added operation is one that was not planned on.  */  
   "AddedOper":boolean,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   "Machines":number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   "SetUpCrewSize":number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   "ProdCrewSize":number,
      /**  A flag indicating if the production is complete for this operation. It is updated via Labor Entry.  */  
   "ProdComplete":boolean,
      /**  Flag that indicates if Setup is complete on this operation. This flag is only used when the operation has EstSetupHours > 0.00.  */  
   "SetupComplete":boolean,
      /**  Total Actual Production Hours. A summary of non-setup LaborDtl.BurdenHrs. This includes REWORK hours.  This is maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActReworkHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H").  */  
   "ActProdHours":number,
      /**  Total Actual Production Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "P" and Rework = Yes. This number is also included as part of the JobOPer.ActProdHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActProdHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   "ActProdRwkHours":number,
      /**  Actual setup hours.  A summary of setup (LaborDtl.LaborType = S) labor transactions hours (LaborDtl.Burden). Actual Setup hours reduce the shop load if the system is configured to remove load based on hours (JCSyst.RemoveLoad = "H").  */  
   "ActSetupHours":number,
      /**  Total Actual Setup Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "S" and Rework = Yes. This number is also included as part of the JobOPer.ActSetupHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActSetHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   "ActSetupRwkHours":number,
      /**   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  */  
   "QtyCompleted":number,
      /**  Setup function percent complete.  Maintained via labor entry.  */  
   "SetupPctComplete":number,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   "SubContract":boolean,
      /**  Inventory UOM  */  
   "IUM":string,
      /**  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  */  
   "EstUnitCost":number,
      /**  Hours required is calculated as days * 8.  */  
   "DaysOut":number,
      /**  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  */  
   "PartNum":string,
      /**  Description used only for subcontract operations  */  
   "Description":string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   "PurPoint":string,
      /**  Editor widget for Job operation comments.  */  
   "CommentText":string,
      /**   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   "SchedRelation":string,
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   "RunQty":number,
      /**   This field is blank or contains the UserID. When not blank it indicates that the operations schedule has been changed and is considered as being in a "What If" mode.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   "WIName":string,
      /**  This is the What-If number of machines that this operation will run on at the same time.  Setup by and for scheduling from the Machines field.  */  
   "WIMachines":number,
      /**  What-if Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   "WIQueStartDate":string,
      /**  What-if Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   "WIQueStartHour":number,
      /**  What if Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   "WIStartDate":string,
      /**  This field is established by scheduling. It represents the What If "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   "WIStartHour":number,
      /**  What If Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   "WIDueDate":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   "WIDueHour":number,
      /**  What-If Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   "WIMoveDueDate":string,
      /**  What-if Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   "WIMoveDueHour":number,
      /**  The Number of Hours per machine per day that this operations "What If" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining ShopLoad records.  */  
   "WIHoursPerMachine":number,
      /**  Date at which the operations current outstanding "What-If" load starts at.  Updated by the JobOper write trigger. (See LoadDate)  */  
   "WILoadDate":string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding "What-If"  load. Related to WILoadDate.  */  
   "WILoadHour":number,
      /**  Total Burden cost to date. This is update via the LaborDtl\Write.p trigger procedure. It includes ALL burden costs (Setup, Production and Rework)  */  
   "ActBurCost":number,
      /**   FOR NON-SUBCONTRACT OPERATIONS: Total of "ALL" labor costs to date. This includes Setup, Production and Rework. Updated via the LaborDtl.Write.p trigger.
FOR SUBCONTRACT OPERATIONS: The Total Cost, updated via the receipt process.  */  
   "ActLabCost":number,
      /**  Total Rework Burden cost todate. This value is also included in the ActBurCost total. It includes both setup & production rework. Updated via LaborDtl\Write.P trigger.  */  
   "ReworkBurCost":number,
      /**  Total Rework Labor cost to date. This value is also included in the ActLabCost field. This includes both Setup & Production. Updated via the LaborDtl\Write.p trigger.  */  
   "ReworkLabCost":number,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   "MiscAmt":number,
      /**  The Number of Hours per machine per day that this operations "actual" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining the ShopLoad records.  */  
   "HoursPerMachine":number,
      /**   Date at which the operations current outstanding load starts at.
Ex: Op schedule is 2/1/97 - 2/10/97, initially LoadDate = 2/1/97. As load is relieved through labor processing the LoadDate moves forward accordingly. When 1/2 completed the LoadDate would be 2/5/97. This field is primarily used by the Scheduling Board to calculate the graphical image of outstanding load.  Updated by the JobOper write trigger.  */  
   "LoadDate":string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding load. Related to LoadDate.  */  
   "LoadHour":number,
      /**  Internally used field to prevent redundant read of JobOper during execution of "Reloader" program. (See WrkCenter.ReloadNum)  */  
   "ReloadNum":number,
      /**  Controls if an alert is to be sent when this JobOper is completed.  */  
   "SndAlrtCmpl":boolean,
      /**  Indicates if  Inspection is required when items are received to this JobOper (subcontract only). Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  Identical to JobHead.JobEngineered.  ShopLoad capacity is only allocated to Jobs where JobEngineered = YES.  */  
   "JobEngineered":boolean,
      /**   The estimated set up hours per machine.
Default from OpStd.SetupHours.  Used to calculate JobOper.EstSetupHours.  */  
   "EstSetHoursPerMch":number,
      /**   Part Revision number.
Pertains to subcontracting operations only.   An optional field.   Related JobAsmbl.RevisionNum is used as the default.  */  
   "RevisionNum":string,
      /**  Currently not used. Prep for future development.  */  
   "AutoReceiptDate":string,
      /**  The labor date of the last labor transaction that was posted to this operation.  Used by the JobOper write trigger Auto Receieve logic.  */  
   "LastLaborDate":string,
      /**  The service call that this operation belongs to.  */  
   "CallNum":number,
      /**  The Service Call Line that this operation relates to.  */  
   "CallLine":number,
      /**  Labor rate used for  time on an operation.  Time per hour per technician. in base currency.  */  
   "LaborRate":number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. in base currency. This field considers the percentage coverage of a warranty or contract.  */  
   "BillableLaborRate":number,
      /**  Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. Does not consider warranty or contract  */  
   "DocLaborRate":number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. considers warranty or contract  */  
   "DocBillableLaborRate":number,
      /**  FS - Is this a billable operation.  */  
   "Billable":boolean,
      /**  FS - Unit Price for the subcontract in base currency.  */  
   "UnitPrice":number,
      /**  FS - Billable Unit Price for the subcontract in base currency.  */  
   "BillableUnitPrice":number,
      /**  FS - Billable Price per unit for the subcontract in customers currency.  */  
   "DocBillableUnitPrice":number,
      /**  FS - Unit Price for the for the Subcontract in Customer currency.  */  
   "DocUnitPrice":number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   "LaborEntryMethod":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   "PricePerCode":string,
      /**  The quantity requested for first article inspection.  */  
   "FAQty":number,
      /**  The "to date" quantity that has been moved to the input Warehouse/Bin of the subsequent operations ResourceGroup/Resource input Warehouse/Bin.  This is NOT A balance.  It is a "to date" value.  It is not reduced as it is consumed.  Used in calculation of "Outstanding" WIP in the Request Material/WIP program (ame30-dg.w).  Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the WIP material in/out of the staging area (Issues, Returns).  */  
   "QtyStagedToDate":number,
      /**  A flag to indicate that this job operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   "RFQNeeded":boolean,
      /**  The number of vendor quotes that are required for this job subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  RFQ number that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   "RFQStat":string,
      /**  Used to group operation to save on setups.  */  
   "SetupGroup":string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   "RestoreFlag":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**   Identifies the primary JobOpDtl to be used for setup.  The setup time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = S or B.  */  
   "PrimarySetupOpDtl":number,
      /**   Identifies the primary JobOpDtl to be used for production.  The production run time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = P or B.  */  
   "PrimaryProdOpDtl":number,
      /**  Operation Description.  */  
   "OpDesc":string,
      /**  Kit Date. Not directly maintanable. Updated via the scheduling process.  */  
   "KitDate":string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   "GlbRFQ":boolean,
      /**  Booked Unit Cost  */  
   "BookedUnitCost":number,
      /**   Initially defaulted to false. This flag is set to true at the time JobOper.ProdComplete is set to true if JobHead.ProductionYield = true and OpMaster. PrdYldRecalcExpected = true and the actual completed qty for the operation vs. the expected completion qty is out of variance based on the under percentage set in OpMaster. This flag is used by the production yield recalculation logic to determine if recalculation is required for a job.
This field is maintained by the system only.  */  
   "RecalcExpProdYld":boolean,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMapData":string,
      /**  When true this would signify that this operation was rough cut scheduled - meaning the operation would have start and end dates but no supporting resourcetimeused or shopload records.  */  
   "RoughCutSched":boolean,
      /**  Scheduling Comments  */  
   "SchedComment":string,
      /**  Reporting currency value of this field  */  
   "Rpt1BillableLaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt2BillableLaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt3BillableLaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt1BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1LaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt2LaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt3LaborRate":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   "SNRequiredOpr":boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   "SNRequiredSubConShip":boolean,
      /**  Operation Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Operation Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   "SendAheadType":string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   "SendAheadOffset":number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   "PrjRoleList":string,
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   "TearDwnEndDate":string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   "TearDwnEndHour":number,
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   "WITearDwnEndDate":string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   "WITearDwnEndHour":number,
   "UseAllRoles":boolean,
      /**  The PartNum for the asset. This should be disabled for a service call job, in which case the asset information would be transferred from the service call line when an operation is created for the job.  */  
   "AssetPartNum":string,
      /**  Serial number of the asset.  */  
   "SerialNumber":string,
      /**  ActualStartDate  */  
   "ActualStartDate":string,
      /**  ActualStartHour  */  
   "ActualStartHour":number,
      /**  ActualEndDate  */  
   "ActualEndDate":string,
      /**  ActualEndHour  */  
   "ActualEndHour":number,
      /**  FSJobStatus  */  
   "FSJobStatus":number,
      /**  Instructions  */  
   "Instructions":string,
      /**  ProdUOM  */  
   "ProdUOM":string,
      /**  GeneralPlanInfo  */  
   "GeneralPlanInfo":string,
      /**  EstStdDescription  */  
   "EstStdDescription":string,
      /**  JDFOpCompleted  */  
   "JDFOpCompleted":boolean,
      /**  RemovedfromPlan  */  
   "RemovedfromPlan":boolean,
      /**  EstStdType  */  
   "EstStdType":number,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  PctReg  */  
   "PctReg":number,
      /**  SetupMaterial  */  
   "SetupMaterial":number,
      /**  MaterialColorRating  */  
   "MaterialColorRating":number,
      /**  MiscInfo1  */  
   "MiscInfo1":string,
      /**  MiscInfo2  */  
   "MiscInfo2":string,
      /**  SetupURL  */  
   "SetupURL":string,
      /**  ExpPctUp  */  
   "ExpPctUp":number,
      /**  ExpCycTm  */  
   "ExpCycTm":number,
      /**  ExpGood  */  
   "ExpGood":number,
      /**  NonProdLimit  */  
   "NonProdLimit":number,
      /**  AutoSpcEnable  */  
   "AutoSpcEnable":boolean,
      /**  AutoSpcPeriod  */  
   "AutoSpcPeriod":number,
      /**  PartQualEnable  */  
   "PartQualEnable":boolean,
      /**  AutoSpcSubgroup  */  
   "AutoSpcSubgroup":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MobileOperation  */  
   "MobileOperation":boolean,
      /**  ReWork  */  
   "ReWork":boolean,
      /**  RequestMove  */  
   "RequestMove":boolean,
      /**  ContractID  */  
   "ContractID":string,
      /**  PrinterID  */  
   "PrinterID":string,
      /**  LastPrintedDate  */  
   "LastPrintedDate":string,
      /**  LastPCIDPrinted  */  
   "LastPCIDPrinted":string,
      /**  CurrentPkgCode  */  
   "CurrentPkgCode":string,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   "QtyPerCycle":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The identification of related StageNo.  */  
   "StageNumber":string,
      /**  TemplateID  */  
   "TemplateID":string,
      /**  The sum of LaborDtl ScrapQty for this operation.  */  
   "ActScrapQty":number,
      /**  Auto receive flag  */  
   "AutoReceive":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  The currency switch flag.  */  
   "CurrencySwitch":boolean,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
   "DisplayExtPrice":number,
      /**  The display service amount.  */  
   "DisplayServAmt":number,
      /**  The display service labor rate  */  
   "DisplayServLaborRate":number,
      /**  Calculated display unit price  */  
   "DisplayUnitPrice":number,
      /**  The document display extended price  */  
   "DocDisplayExtPrice":number,
      /**  The converted display service amount.  */  
   "DocDisplayServAmt":number,
      /**  The converted display service labor rate.  */  
   "DocDisplayServLaborRate":number,
      /**  The document display unit price  */  
   "DocDisplayUnitPrice":number,
      /**  Display IUM field (readonly)  */  
   "DspIUM":string,
      /**  Field to determine to enable or disable autoreceive.  */  
   "EnableAutoReceive":boolean,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   "EnableSndAlrtCmpl":boolean,
      /**  This external field is used as a flag to determine when to enable/disable the SNRequiredSubConShip field on UI screen.  */  
   "EnableSNReqSubConShip":boolean,
   "EnableSNRequiredOpr":boolean,
      /**  For non subconctract operations JobOper.EstSetHours * JobOper.SetupBurRate + JobOper.EstProdHours * JobOper.ProdBurRate  */  
   "EstBurdenCost":number,
      /**  The calculated estimated labor hours  */  
   "EstLabHours":number,
      /**  For non subcontract operations : JobOper.EstSetHours * JobOper.SetupCrewSize * JobOper.SetupLabRate +JobOper.EstProdHours * JobOper.ProdCrewSize * JobOper.ProdLabRate  */  
   "EstLaborCost":number,
      /**  For SubContract operations: JobOper.EstUnitCost * JobOper.RunQty  */  
   "EstSubCost":number,
      /**  Final operation  */  
   "FinalOpr":boolean,
      /**  IsBaseCurrency  */  
   "IsBaseCurrency":boolean,
      /**  This is the description of the Method for Labor Entry.  Can be "Time and Quantity" for 'T', "Quantity Only" for 'Q', "Backflush" for 'B' or "Time and Backflush Qty" for 'X'  */  
   "LaborEntryMethodDesc":string,
      /**  The total Load Hours calculated by summing the SetUpLoadHrs + ProdLoadHrs.  */  
   "LoadHrs":number,
   "OpStdDescription":string,
      /**  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   "PrimaryProdOpDtlDesc":string,
      /**  Primary Resource Group Description  */  
   "PrimaryResourceGrpDesc":string,
      /**  The Resource Group ID of the primary production operation detail.  */  
   "PrimaryResourceGrpID":string,
      /**  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   "PrimarySetupOpDtlDesc":string,
      /**  The calculated production quantity  */  
   "ProductionQty":number,
      /**  Indicates if the scheduling resources should be refreshed when the op code changes.  */  
   "RefreshResources":boolean,
   "Rpt1DisplayExtPrice":number,
   "Rpt1DisplayServAmt":number,
   "Rpt1DisplayServLaborRate":number,
   "Rpt1DisplayUnitPrice":number,
   "Rpt2DisplayExtPrice":number,
   "Rpt2DisplayServAmt":number,
   "Rpt2DisplayServLaborRate":number,
   "Rpt2DisplayUnitPrice":number,
   "Rpt3DisplayExtPrice":number,
   "Rpt3DisplayServAmt":number,
   "Rpt3DisplayServLaborRate":number,
   "Rpt3DisplayUnitPrice":number,
      /**  The calculated scrap quantity  */  
   "ScrapQty":number,
      /**  Contains the value of which icon to display in tree for joboper  */  
   "ShowStatusIcon":string,
      /**  StdBasis Description  */  
   "StdBasisDescription":string,
      /**  StdFormat Description  */  
   "StdFormatDescription":string,
      /**  For SubContract Operations equals to the ActLaborCost  */  
   "ActSubCost":number,
   "EnableAttributeSetSearch":boolean,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "AssemblySeqDescription":string,
   "CallLineLineDesc":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "JobNumPartDescription":string,
   "OpCodeOpDesc":string,
   "PartNumAttrClassID":string,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
   "PartNumPartDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackLots":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "RFQLineLineDesc":string,
   "SetupGroupDescription":string,
   "StageNoDescription":string,
   "VendorNumTermsCode":string,
   "VendorNumDefaultFOB":string,
   "VendorNumName":string,
   "VendorNumCountry":string,
   "VendorNumAddress2":string,
   "VendorNumCurrencyCode":string,
   "VendorNumZIP":string,
   "VendorNumState":string,
   "VendorNumAddress1":string,
   "VendorNumAddress3":string,
   "VendorNumCity":string,
   "VendorNumVendorID":string,
   "VendorPPZip":string,
   "VendorPPCity":string,
   "VendorPPAddress2":string,
   "VendorPPPrimPCon":number,
   "VendorPPAddress1":string,
   "VendorPPCountry":string,
   "VendorPPState":string,
   "VendorPPName":string,
   "VendorPPAddress3":string,
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
      @param assemblySeq
      @param oprSeq
   */  
export interface DeleteByID_input{
   jobNum:string,
   assemblySeq:number,
   oprSeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_JobOperListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobOper records are also marked.  This is used to make database access to open operation records more efficient.  */  
   JobComplete:boolean,
      /**   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  */  
   OpComplete:boolean,
      /**  Job Number  */  
   JobNum:string,
      /**  Assembly Sequence # that this Operation is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**   The Operation standard ID.  This links the JobOper to the OpStd master file.  This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   OpStdID:string,
      /**  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  */  
   EstSetHours:number,
      /**   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  */  
   EstProdHours:number,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  Production Quantity per one of the Parent Item.  */  
   QtyPer:number,
      /**  Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   QueStartDate:string,
      /**  Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   QueStartHour:number,
      /**  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   StartDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   StartHour:number,
      /**  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   DueHour:number,
      /**  Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   MoveDueDate:string,
      /**  Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   MoveDueHour:number,
      /**  Labor rate used for estimated production labor costs. Default from the OpMaster.ProdLabRate.  */  
   ProdLabRate:number,
      /**  Labor rate for estimated setup labor costs. Default from the OpMaster.SetupLabRate.  */  
   SetupLabRate:number,
      /**  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.ProdBurRate.  */  
   ProdBurRate:number,
      /**  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.SetupBurRate.  */  
   SetupBurRate:number,
      /**  This indicates if this is an "added operation". An added operation is one that was not planned on.  */  
   AddedOper:boolean,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   Machines:number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  A flag indicating if the production is complete for this operation. It is updated via Labor Entry.  */  
   ProdComplete:boolean,
      /**  Flag that indicates if Setup is complete on this operation. This flag is only used when the operation has EstSetupHours > 0.00.  */  
   SetupComplete:boolean,
      /**  Total Actual Production Hours. A summary of non-setup LaborDtl.BurdenHrs. This includes REWORK hours.  This is maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActReworkHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H").  */  
   ActProdHours:number,
      /**  Total Actual Production Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "P" and Rework = Yes. This number is also included as part of the JobOPer.ActProdHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActProdHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   ActProdRwkHours:number,
      /**  Actual setup hours.  A summary of setup (LaborDtl.LaborType = S) labor transactions hours (LaborDtl.Burden). Actual Setup hours reduce the shop load if the system is configured to remove load based on hours (JCSyst.RemoveLoad = "H").  */  
   ActSetupHours:number,
      /**  Total Actual Setup Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "S" and Rework = Yes. This number is also included as part of the JobOPer.ActSetupHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActSetHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   ActSetupRwkHours:number,
      /**   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  */  
   QtyCompleted:number,
      /**  Setup function percent complete.  Maintained via labor entry.  */  
   SetupPctComplete:number,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  Inventory UOM  */  
   IUM:string,
      /**  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  Hours required is calculated as days * 8.  */  
   DaysOut:number,
      /**  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  */  
   PartNum:string,
      /**  Description used only for subcontract operations  */  
   Description:string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Editor widget for Job operation comments.  */  
   CommentText:string,
      /**   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   SchedRelation:string,
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   RunQty:number,
      /**   This field is blank or contains the UserID. When not blank it indicates that the operations schedule has been changed and is considered as being in a "What If" mode.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   WIName:string,
      /**  This is the What-If number of machines that this operation will run on at the same time.  Setup by and for scheduling from the Machines field.  */  
   WIMachines:number,
      /**  What-if Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   WIQueStartDate:string,
      /**  What-if Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   WIQueStartHour:number,
      /**  What if Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   WIStartDate:string,
      /**  This field is established by scheduling. It represents the What If "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   WIStartHour:number,
      /**  What If Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   WIDueHour:number,
      /**  What-If Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   WIMoveDueDate:string,
      /**  What-if Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   WIMoveDueHour:number,
      /**  The Number of Hours per machine per day that this operations "What If" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining ShopLoad records.  */  
   WIHoursPerMachine:number,
      /**  Date at which the operations current outstanding "What-If" load starts at.  Updated by the JobOper write trigger. (See LoadDate)  */  
   WILoadDate:string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding "What-If"  load. Related to WILoadDate.  */  
   WILoadHour:number,
      /**  Total Burden cost to date. This is update via the LaborDtl\Write.p trigger procedure. It includes ALL burden costs (Setup, Production and Rework)  */  
   ActBurCost:number,
      /**   FOR NON-SUBCONTRACT OPERATIONS: Total of "ALL" labor costs to date. This includes Setup, Production and Rework. Updated via the LaborDtl.Write.p trigger.
FOR SUBCONTRACT OPERATIONS: The Total Cost, updated via the receipt process.  */  
   ActLabCost:number,
      /**  Total Rework Burden cost todate. This value is also included in the ActBurCost total. It includes both setup & production rework. Updated via LaborDtl\Write.P trigger.  */  
   ReworkBurCost:number,
      /**  Total Rework Labor cost to date. This value is also included in the ActLabCost field. This includes both Setup & Production. Updated via the LaborDtl\Write.p trigger.  */  
   ReworkLabCost:number,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   MiscAmt:number,
      /**  The Number of Hours per machine per day that this operations "actual" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining the ShopLoad records.  */  
   HoursPerMachine:number,
      /**   Date at which the operations current outstanding load starts at.
Ex: Op schedule is 2/1/97 - 2/10/97, initially LoadDate = 2/1/97. As load is relieved through labor processing the LoadDate moves forward accordingly. When 1/2 completed the LoadDate would be 2/5/97. This field is primarily used by the Scheduling Board to calculate the graphical image of outstanding load.  Updated by the JobOper write trigger.  */  
   LoadDate:string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding load. Related to LoadDate.  */  
   LoadHour:number,
      /**  Internally used field to prevent redundant read of JobOper during execution of "Reloader" program. (See WrkCenter.ReloadNum)  */  
   ReloadNum:number,
      /**  Controls if an alert is to be sent when this JobOper is completed.  */  
   SndAlrtCmpl:boolean,
      /**  Indicates if  Inspection is required when items are received to this JobOper (subcontract only). Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Identical to JobHead.JobEngineered.  ShopLoad capacity is only allocated to Jobs where JobEngineered = YES.  */  
   JobEngineered:boolean,
      /**   The estimated set up hours per machine.
Default from OpStd.SetupHours.  Used to calculate JobOper.EstSetupHours.  */  
   EstSetHoursPerMch:number,
      /**   Part Revision number.
Pertains to subcontracting operations only.   An optional field.   Related JobAsmbl.RevisionNum is used as the default.  */  
   RevisionNum:string,
      /**  Currently not used. Prep for future development.  */  
   AutoReceiptDate:string,
      /**  The labor date of the last labor transaction that was posted to this operation.  Used by the JobOper write trigger Auto Receieve logic.  */  
   LastLaborDate:string,
      /**  The service call that this operation belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this operation relates to.  */  
   CallLine:number,
      /**  Labor rate used for  time on an operation.  Time per hour per technician. in base currency.  */  
   LaborRate:number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. in base currency. This field considers the percentage coverage of a warranty or contract.  */  
   BillableLaborRate:number,
      /**  Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. Does not consider warranty or contract  */  
   DocLaborRate:number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. considers warranty or contract  */  
   DocBillableLaborRate:number,
      /**  FS - Is this a billable operation.  */  
   Billable:boolean,
      /**  FS - Unit Price for the subcontract in base currency.  */  
   UnitPrice:number,
      /**  FS - Billable Unit Price for the subcontract in base currency.  */  
   BillableUnitPrice:number,
      /**  FS - Billable Price per unit for the subcontract in customers currency.  */  
   DocBillableUnitPrice:number,
      /**  FS - Unit Price for the for the Subcontract in Customer currency.  */  
   DocUnitPrice:number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   PricePerCode:string,
      /**  The quantity requested for first article inspection.  */  
   FAQty:number,
      /**  The "to date" quantity that has been moved to the input Warehouse/Bin of the subsequent operations ResourceGroup/Resource input Warehouse/Bin.  This is NOT A balance.  It is a "to date" value.  It is not reduced as it is consumed.  Used in calculation of "Outstanding" WIP in the Request Material/WIP program (ame30-dg.w).  Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the WIP material in/out of the staging area (Issues, Returns).  */  
   QtyStagedToDate:number,
      /**  A flag to indicate that this job operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this job subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**   Identifies the primary JobOpDtl to be used for setup.  The setup time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = S or B.  */  
   PrimarySetupOpDtl:number,
      /**   Identifies the primary JobOpDtl to be used for production.  The production run time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = P or B.  */  
   PrimaryProdOpDtl:number,
      /**  Operation Description.  */  
   OpDesc:string,
      /**  Kit Date. Not directly maintanable. Updated via the scheduling process.  */  
   KitDate:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Booked Unit Cost  */  
   BookedUnitCost:number,
      /**   Initially defaulted to false. This flag is set to true at the time JobOper.ProdComplete is set to true if JobHead.ProductionYield = true and OpMaster. PrdYldRecalcExpected = true and the actual completed qty for the operation vs. the expected completion qty is out of variance based on the under percentage set in OpMaster. This flag is used by the production yield recalculation logic to determine if recalculation is required for a job.
This field is maintained by the system only.  */  
   RecalcExpProdYld:boolean,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  When true this would signify that this operation was rough cut scheduled - meaning the operation would have start and end dates but no supporting resourcetimeused or shopload records.  */  
   RoughCutSched:boolean,
      /**  Scheduling Comments  */  
   SchedComment:string,
      /**  Reporting currency value of this field  */  
   Rpt1BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt1BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt2LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt3LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   SNRequiredOpr:boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   SNRequiredSubConShip:boolean,
      /**  Operation Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Operation Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   SendAheadType:string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   SendAheadOffset:number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   PrjRoleList:string,
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   TearDwnEndDate:string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   TearDwnEndHour:number,
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   WITearDwnEndDate:string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   WITearDwnEndHour:number,
   UseAllRoles:boolean,
      /**  The PartNum for the asset. This should be disabled for a service call job, in which case the asset information would be transferred from the service call line when an operation is created for the job.  */  
   AssetPartNum:string,
      /**  Serial number of the asset.  */  
   SerialNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The calculated production quantity  */  
   ProductionQty:number,
      /**  The calculated scrap quantity  */  
   ScrapQty:number,
      /**  The calculated estimated labor hours  */  
   EstLabHours:number,
      /**  The display service labor rate  */  
   DisplayServLaborRate:number,
      /**  The display service amount.  */  
   DisplayServAmt:number,
      /**  The converted display service labor rate.  */  
   DocDisplayServLaborRate:number,
      /**  The converted display service amount.  */  
   DocDisplayServAmt:number,
   DisplayExtPrice:number,
      /**  Final operation  */  
   FinalOpr:boolean,
      /**  Auto receive flag  */  
   AutoReceive:boolean,
      /**  Calculated display unit price  */  
   DisplayUnitPrice:number,
      /**  The currency switch flag.  */  
   CurrencySwitch:boolean,
      /**  The document display unit price  */  
   DocDisplayUnitPrice:number,
      /**  The document display extended price  */  
   DocDisplayExtPrice:number,
      /**  Contains the value of which icon to display in tree for joboper  */  
   ShowStatusIcon:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   EnableSndAlrtCmpl:boolean,
      /**  Field to determine to enable or disable autoreceive.  */  
   EnableAutoReceive:boolean,
   OpStdDescription:string,
      /**  The Resource Group ID of the primary production operation detail.  */  
   PrimaryResourceGrpID:string,
      /**  Primary Resource Group Description  */  
   PrimaryResourceGrpDesc:string,
      /**  This is the description of the Method for Labor Entry.  Can be "Time and Quantity" for 'T', "Quantity Only" for 'Q' or "Backflush" for 'B'.  */  
   LaborEntryMethodDesc:string,
      /**  Indicates if the scheduling resources should be refreshed when the op code changes.  */  
   RefreshResources:boolean,
      /**  StdFormat Description  */  
   StdFormatDescription:string,
      /**  StdBasis Description  */  
   StdBasisDescription:string,
      /**  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   PrimaryProdOpDtlDesc:string,
      /**  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   PrimarySetupOpDtlDesc:string,
      /**  For SubContract Operations equals to the ActLaborCost  */  
   ActSubCost:number,
      /**  For non subconctract operations JobOper.EstSetHours * JobOper.SetupBurRate + JobOper.EstProdHours * JobOper.ProdBurRate  */  
   EstBurdenCost:number,
      /**  For non subcontract operations : JobOper.EstSetHours * JobOper.SetupCrewSize * JobOper.SetupLabRate +JobOper.EstProdHours * JobOper.ProdCrewSize * JobOper.ProdLabRate  */  
   EstLaborCost:number,
      /**  For SubContract operations: JobOper.EstUnitCost * JobOper.RunQty  */  
   EstSubCost:number,
      /**  Flag to allow/disallow the user to see the Job Costs.  */  
   AllowJobCosts:string,
      /**  The total Load Hours calculated by summing the SetUpLoadHrs + ProdLoadHrs.  */  
   LoadHrs:number,
      /**  IsBaseCurrency  */  
   IsBaseCurrency:boolean,
   EnableSNRequiredOpr:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   Rpt1DisplayServLaborRate:number,
   Rpt2DisplayServLaborRate:number,
   Rpt3DisplayServLaborRate:number,
   Rpt1DisplayServAmt:number,
   Rpt2DisplayServAmt:number,
   Rpt3DisplayServAmt:number,
   Rpt1DisplayUnitPrice:number,
   Rpt2DisplayUnitPrice:number,
   Rpt3DisplayUnitPrice:number,
   Rpt1DisplayExtPrice:number,
   Rpt2DisplayExtPrice:number,
   Rpt3DisplayExtPrice:number,
      /**  This external field is used as a flag to determine when to enable/disable the SNRequiredSubConShip field on UI screen.  */  
   EnableSNReqSubConShip:boolean,
      /**  Display IUM field (readonly)  */  
   DspIUM:string,
      /**  Description  */  
   AnalysisCdDescription:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   CallLineLineDesc:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   OpCodeOpDesc:string,
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
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   RFQLineLineDesc:string,
      /**  Description of Setup Group.  */  
   SetupGroupDescription:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Second address line  */  
   VendorPPAddress2:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   VendorPPCountry:string,
      /**  State portion of the address  */  
   VendorPPState:string,
      /**  Third address line  */  
   VendorPPAddress3:string,
      /**  Purchase Point Name...can't be blank.  */  
   VendorPPName:string,
      /**  Postal Code or Zip code portion of the address  */  
   VendorPPZip:string,
      /**  City portion of the address  */  
   VendorPPCity:string,
      /**  First address line  */  
   VendorPPAddress1:string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   VendorPPPrimPCon:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobOperListTableset{
   JobOperList:Erp_Tablesets_JobOperListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobOperRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobOper records are also marked.  This is used to make database access to open operation records more efficient.  */  
   JobComplete:boolean,
      /**   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  */  
   OpComplete:boolean,
      /**  Job Number  */  
   JobNum:string,
      /**  Assembly Sequence # that this Operation is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**   The Operation standard ID.  This links the JobOper to the OpStd master file.  This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   OpStdID:string,
      /**  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  */  
   EstSetHours:number,
      /**   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  */  
   EstProdHours:number,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  Production Quantity per one of the Parent Item.  */  
   QtyPer:number,
      /**  Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   QueStartDate:string,
      /**  Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   QueStartHour:number,
      /**  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   StartDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   StartHour:number,
      /**  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   DueHour:number,
      /**  Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   MoveDueDate:string,
      /**  Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   MoveDueHour:number,
      /**  Labor rate used for estimated production labor costs. Default from the OpMaster.ProdLabRate.  */  
   ProdLabRate:number,
      /**  Labor rate for estimated setup labor costs. Default from the OpMaster.SetupLabRate.  */  
   SetupLabRate:number,
      /**  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.ProdBurRate.  */  
   ProdBurRate:number,
      /**  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.SetupBurRate.  */  
   SetupBurRate:number,
      /**  This indicates if this is an "added operation". An added operation is one that was not planned on.  */  
   AddedOper:boolean,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   Machines:number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  A flag indicating if the production is complete for this operation. It is updated via Labor Entry.  */  
   ProdComplete:boolean,
      /**  Flag that indicates if Setup is complete on this operation. This flag is only used when the operation has EstSetupHours > 0.00.  */  
   SetupComplete:boolean,
      /**  Total Actual Production Hours. A summary of non-setup LaborDtl.BurdenHrs. This includes REWORK hours.  This is maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActReworkHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H").  */  
   ActProdHours:number,
      /**  Total Actual Production Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "P" and Rework = Yes. This number is also included as part of the JobOPer.ActProdHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActProdHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   ActProdRwkHours:number,
      /**  Actual setup hours.  A summary of setup (LaborDtl.LaborType = S) labor transactions hours (LaborDtl.Burden). Actual Setup hours reduce the shop load if the system is configured to remove load based on hours (JCSyst.RemoveLoad = "H").  */  
   ActSetupHours:number,
      /**  Total Actual Setup Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "S" and Rework = Yes. This number is also included as part of the JobOPer.ActSetupHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActSetHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   ActSetupRwkHours:number,
      /**   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  */  
   QtyCompleted:number,
      /**  Setup function percent complete.  Maintained via labor entry.  */  
   SetupPctComplete:number,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  Inventory UOM  */  
   IUM:string,
      /**  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  Hours required is calculated as days * 8.  */  
   DaysOut:number,
      /**  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  */  
   PartNum:string,
      /**  Description used only for subcontract operations  */  
   Description:string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Editor widget for Job operation comments.  */  
   CommentText:string,
      /**   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   SchedRelation:string,
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   RunQty:number,
      /**   This field is blank or contains the UserID. When not blank it indicates that the operations schedule has been changed and is considered as being in a "What If" mode.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   WIName:string,
      /**  This is the What-If number of machines that this operation will run on at the same time.  Setup by and for scheduling from the Machines field.  */  
   WIMachines:number,
      /**  What-if Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   WIQueStartDate:string,
      /**  What-if Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   WIQueStartHour:number,
      /**  What if Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   WIStartDate:string,
      /**  This field is established by scheduling. It represents the What If "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   WIStartHour:number,
      /**  What If Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   WIDueHour:number,
      /**  What-If Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   WIMoveDueDate:string,
      /**  What-if Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   WIMoveDueHour:number,
      /**  The Number of Hours per machine per day that this operations "What If" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining ShopLoad records.  */  
   WIHoursPerMachine:number,
      /**  Date at which the operations current outstanding "What-If" load starts at.  Updated by the JobOper write trigger. (See LoadDate)  */  
   WILoadDate:string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding "What-If"  load. Related to WILoadDate.  */  
   WILoadHour:number,
      /**  Total Burden cost to date. This is update via the LaborDtl\Write.p trigger procedure. It includes ALL burden costs (Setup, Production and Rework)  */  
   ActBurCost:number,
      /**   FOR NON-SUBCONTRACT OPERATIONS: Total of "ALL" labor costs to date. This includes Setup, Production and Rework. Updated via the LaborDtl.Write.p trigger.
FOR SUBCONTRACT OPERATIONS: The Total Cost, updated via the receipt process.  */  
   ActLabCost:number,
      /**  Total Rework Burden cost todate. This value is also included in the ActBurCost total. It includes both setup & production rework. Updated via LaborDtl\Write.P trigger.  */  
   ReworkBurCost:number,
      /**  Total Rework Labor cost to date. This value is also included in the ActLabCost field. This includes both Setup & Production. Updated via the LaborDtl\Write.p trigger.  */  
   ReworkLabCost:number,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   MiscAmt:number,
      /**  The Number of Hours per machine per day that this operations "actual" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining the ShopLoad records.  */  
   HoursPerMachine:number,
      /**   Date at which the operations current outstanding load starts at.
Ex: Op schedule is 2/1/97 - 2/10/97, initially LoadDate = 2/1/97. As load is relieved through labor processing the LoadDate moves forward accordingly. When 1/2 completed the LoadDate would be 2/5/97. This field is primarily used by the Scheduling Board to calculate the graphical image of outstanding load.  Updated by the JobOper write trigger.  */  
   LoadDate:string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding load. Related to LoadDate.  */  
   LoadHour:number,
      /**  Internally used field to prevent redundant read of JobOper during execution of "Reloader" program. (See WrkCenter.ReloadNum)  */  
   ReloadNum:number,
      /**  Controls if an alert is to be sent when this JobOper is completed.  */  
   SndAlrtCmpl:boolean,
      /**  Indicates if  Inspection is required when items are received to this JobOper (subcontract only). Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Identical to JobHead.JobEngineered.  ShopLoad capacity is only allocated to Jobs where JobEngineered = YES.  */  
   JobEngineered:boolean,
      /**   The estimated set up hours per machine.
Default from OpStd.SetupHours.  Used to calculate JobOper.EstSetupHours.  */  
   EstSetHoursPerMch:number,
      /**   Part Revision number.
Pertains to subcontracting operations only.   An optional field.   Related JobAsmbl.RevisionNum is used as the default.  */  
   RevisionNum:string,
      /**  Currently not used. Prep for future development.  */  
   AutoReceiptDate:string,
      /**  The labor date of the last labor transaction that was posted to this operation.  Used by the JobOper write trigger Auto Receieve logic.  */  
   LastLaborDate:string,
      /**  The service call that this operation belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this operation relates to.  */  
   CallLine:number,
      /**  Labor rate used for  time on an operation.  Time per hour per technician. in base currency.  */  
   LaborRate:number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. in base currency. This field considers the percentage coverage of a warranty or contract.  */  
   BillableLaborRate:number,
      /**  Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. Does not consider warranty or contract  */  
   DocLaborRate:number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. considers warranty or contract  */  
   DocBillableLaborRate:number,
      /**  FS - Is this a billable operation.  */  
   Billable:boolean,
      /**  FS - Unit Price for the subcontract in base currency.  */  
   UnitPrice:number,
      /**  FS - Billable Unit Price for the subcontract in base currency.  */  
   BillableUnitPrice:number,
      /**  FS - Billable Price per unit for the subcontract in customers currency.  */  
   DocBillableUnitPrice:number,
      /**  FS - Unit Price for the for the Subcontract in Customer currency.  */  
   DocUnitPrice:number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   PricePerCode:string,
      /**  The quantity requested for first article inspection.  */  
   FAQty:number,
      /**  The "to date" quantity that has been moved to the input Warehouse/Bin of the subsequent operations ResourceGroup/Resource input Warehouse/Bin.  This is NOT A balance.  It is a "to date" value.  It is not reduced as it is consumed.  Used in calculation of "Outstanding" WIP in the Request Material/WIP program (ame30-dg.w).  Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the WIP material in/out of the staging area (Issues, Returns).  */  
   QtyStagedToDate:number,
      /**  A flag to indicate that this job operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this job subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**   Identifies the primary JobOpDtl to be used for setup.  The setup time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = S or B.  */  
   PrimarySetupOpDtl:number,
      /**   Identifies the primary JobOpDtl to be used for production.  The production run time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = P or B.  */  
   PrimaryProdOpDtl:number,
      /**  Operation Description.  */  
   OpDesc:string,
      /**  Kit Date. Not directly maintanable. Updated via the scheduling process.  */  
   KitDate:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Booked Unit Cost  */  
   BookedUnitCost:number,
      /**   Initially defaulted to false. This flag is set to true at the time JobOper.ProdComplete is set to true if JobHead.ProductionYield = true and OpMaster. PrdYldRecalcExpected = true and the actual completed qty for the operation vs. the expected completion qty is out of variance based on the under percentage set in OpMaster. This flag is used by the production yield recalculation logic to determine if recalculation is required for a job.
This field is maintained by the system only.  */  
   RecalcExpProdYld:boolean,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  When true this would signify that this operation was rough cut scheduled - meaning the operation would have start and end dates but no supporting resourcetimeused or shopload records.  */  
   RoughCutSched:boolean,
      /**  Scheduling Comments  */  
   SchedComment:string,
      /**  Reporting currency value of this field  */  
   Rpt1BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt1BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt2LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt3LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  */  
   SNRequiredOpr:boolean,
      /**  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  */  
   SNRequiredSubConShip:boolean,
      /**  Operation Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Operation Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  */  
   SendAheadType:string,
      /**   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  */  
   SendAheadOffset:number,
      /**  Delimited list of PrjRoleCd codes that are allowed for this operation.  */  
   PrjRoleList:string,
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   TearDwnEndDate:string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   TearDwnEndHour:number,
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   WITearDwnEndDate:string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   WITearDwnEndHour:number,
   UseAllRoles:boolean,
      /**  The PartNum for the asset. This should be disabled for a service call job, in which case the asset information would be transferred from the service call line when an operation is created for the job.  */  
   AssetPartNum:string,
      /**  Serial number of the asset.  */  
   SerialNumber:string,
      /**  ActualStartDate  */  
   ActualStartDate:string,
      /**  ActualStartHour  */  
   ActualStartHour:number,
      /**  ActualEndDate  */  
   ActualEndDate:string,
      /**  ActualEndHour  */  
   ActualEndHour:number,
      /**  FSJobStatus  */  
   FSJobStatus:number,
      /**  Instructions  */  
   Instructions:string,
      /**  ProdUOM  */  
   ProdUOM:string,
      /**  GeneralPlanInfo  */  
   GeneralPlanInfo:string,
      /**  EstStdDescription  */  
   EstStdDescription:string,
      /**  JDFOpCompleted  */  
   JDFOpCompleted:boolean,
      /**  RemovedfromPlan  */  
   RemovedfromPlan:boolean,
      /**  EstStdType  */  
   EstStdType:number,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  PctReg  */  
   PctReg:number,
      /**  SetupMaterial  */  
   SetupMaterial:number,
      /**  MaterialColorRating  */  
   MaterialColorRating:number,
      /**  MiscInfo1  */  
   MiscInfo1:string,
      /**  MiscInfo2  */  
   MiscInfo2:string,
      /**  SetupURL  */  
   SetupURL:string,
      /**  ExpPctUp  */  
   ExpPctUp:number,
      /**  ExpCycTm  */  
   ExpCycTm:number,
      /**  ExpGood  */  
   ExpGood:number,
      /**  NonProdLimit  */  
   NonProdLimit:number,
      /**  AutoSpcEnable  */  
   AutoSpcEnable:boolean,
      /**  AutoSpcPeriod  */  
   AutoSpcPeriod:number,
      /**  PartQualEnable  */  
   PartQualEnable:boolean,
      /**  AutoSpcSubgroup  */  
   AutoSpcSubgroup:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MobileOperation  */  
   MobileOperation:boolean,
      /**  ReWork  */  
   ReWork:boolean,
      /**  RequestMove  */  
   RequestMove:boolean,
      /**  ContractID  */  
   ContractID:string,
      /**  PrinterID  */  
   PrinterID:string,
      /**  LastPrintedDate  */  
   LastPrintedDate:string,
      /**  LastPCIDPrinted  */  
   LastPCIDPrinted:string,
      /**  CurrentPkgCode  */  
   CurrentPkgCode:string,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The identification of related StageNo.  */  
   StageNumber:string,
      /**  TemplateID  */  
   TemplateID:string,
      /**  The sum of LaborDtl ScrapQty for this operation.  */  
   ActScrapQty:number,
      /**  Auto receive flag  */  
   AutoReceive:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  The currency switch flag.  */  
   CurrencySwitch:boolean,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
   DisplayExtPrice:number,
      /**  The display service amount.  */  
   DisplayServAmt:number,
      /**  The display service labor rate  */  
   DisplayServLaborRate:number,
      /**  Calculated display unit price  */  
   DisplayUnitPrice:number,
      /**  The document display extended price  */  
   DocDisplayExtPrice:number,
      /**  The converted display service amount.  */  
   DocDisplayServAmt:number,
      /**  The converted display service labor rate.  */  
   DocDisplayServLaborRate:number,
      /**  The document display unit price  */  
   DocDisplayUnitPrice:number,
      /**  Display IUM field (readonly)  */  
   DspIUM:string,
      /**  Field to determine to enable or disable autoreceive.  */  
   EnableAutoReceive:boolean,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   EnableSndAlrtCmpl:boolean,
      /**  This external field is used as a flag to determine when to enable/disable the SNRequiredSubConShip field on UI screen.  */  
   EnableSNReqSubConShip:boolean,
   EnableSNRequiredOpr:boolean,
      /**  For non subconctract operations JobOper.EstSetHours * JobOper.SetupBurRate + JobOper.EstProdHours * JobOper.ProdBurRate  */  
   EstBurdenCost:number,
      /**  The calculated estimated labor hours  */  
   EstLabHours:number,
      /**  For non subcontract operations : JobOper.EstSetHours * JobOper.SetupCrewSize * JobOper.SetupLabRate +JobOper.EstProdHours * JobOper.ProdCrewSize * JobOper.ProdLabRate  */  
   EstLaborCost:number,
      /**  For SubContract operations: JobOper.EstUnitCost * JobOper.RunQty  */  
   EstSubCost:number,
      /**  Final operation  */  
   FinalOpr:boolean,
      /**  IsBaseCurrency  */  
   IsBaseCurrency:boolean,
      /**  This is the description of the Method for Labor Entry.  Can be "Time and Quantity" for 'T', "Quantity Only" for 'Q', "Backflush" for 'B' or "Time and Backflush Qty" for 'X'  */  
   LaborEntryMethodDesc:string,
      /**  The total Load Hours calculated by summing the SetUpLoadHrs + ProdLoadHrs.  */  
   LoadHrs:number,
   OpStdDescription:string,
      /**  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   PrimaryProdOpDtlDesc:string,
      /**  Primary Resource Group Description  */  
   PrimaryResourceGrpDesc:string,
      /**  The Resource Group ID of the primary production operation detail.  */  
   PrimaryResourceGrpID:string,
      /**  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   PrimarySetupOpDtlDesc:string,
      /**  The calculated production quantity  */  
   ProductionQty:number,
      /**  Indicates if the scheduling resources should be refreshed when the op code changes.  */  
   RefreshResources:boolean,
   Rpt1DisplayExtPrice:number,
   Rpt1DisplayServAmt:number,
   Rpt1DisplayServLaborRate:number,
   Rpt1DisplayUnitPrice:number,
   Rpt2DisplayExtPrice:number,
   Rpt2DisplayServAmt:number,
   Rpt2DisplayServLaborRate:number,
   Rpt2DisplayUnitPrice:number,
   Rpt3DisplayExtPrice:number,
   Rpt3DisplayServAmt:number,
   Rpt3DisplayServLaborRate:number,
   Rpt3DisplayUnitPrice:number,
      /**  The calculated scrap quantity  */  
   ScrapQty:number,
      /**  Contains the value of which icon to display in tree for joboper  */  
   ShowStatusIcon:string,
      /**  StdBasis Description  */  
   StdBasisDescription:string,
      /**  StdFormat Description  */  
   StdFormatDescription:string,
      /**  For SubContract Operations equals to the ActLaborCost  */  
   ActSubCost:number,
   EnableAttributeSetSearch:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   AssemblySeqDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   JobNumPartDescription:string,
   OpCodeOpDesc:string,
   PartNumAttrClassID:string,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackLots:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackInventoryByRevision:boolean,
   RFQLineLineDesc:string,
   SetupGroupDescription:string,
   StageNoDescription:string,
   VendorNumTermsCode:string,
   VendorNumDefaultFOB:string,
   VendorNumName:string,
   VendorNumCountry:string,
   VendorNumAddress2:string,
   VendorNumCurrencyCode:string,
   VendorNumZIP:string,
   VendorNumState:string,
   VendorNumAddress1:string,
   VendorNumAddress3:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorPPZip:string,
   VendorPPCity:string,
   VendorPPAddress2:string,
   VendorPPPrimPCon:number,
   VendorPPAddress1:string,
   VendorPPCountry:string,
   VendorPPState:string,
   VendorPPName:string,
   VendorPPAddress3:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobOperSearchTableset{
   JobOper:Erp_Tablesets_JobOperRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtJobOperSearchTableset{
   JobOper:Erp_Tablesets_JobOperRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param jobNum
      @param assemblySeq
      @param oprSeq
   */  
export interface GetByID_input{
   jobNum:string,
   assemblySeq:number,
   oprSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_JobOperSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_JobOperSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_JobOperSearchTableset[],
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
   returnObj:Erp_Tablesets_JobOperListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param jobNum
      @param assemblySeq
   */  
export interface GetNewJobOper_input{
   ds:Erp_Tablesets_JobOperSearchTableset[],
   jobNum:string,
   assemblySeq:number,
}

export interface GetNewJobOper_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobOperSearchTableset,
}
}

   /** Required : 
      @param whereClauseJobOper
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseJobOper:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_JobOperSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtJobOperSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtJobOperSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_JobOperSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobOperSearchTableset,
}
}

