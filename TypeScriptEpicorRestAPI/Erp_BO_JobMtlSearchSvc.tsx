import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.JobMtlSearchSvc
// Description: Search object for Job Material
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/$metadata", {
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
   Description: Get JobMtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobMtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobMtlRow
   */  
export function get_JobMtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/JobMtlSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobMtlSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobMtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.JobMtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobMtlSearches(requestBody:Erp_Tablesets_JobMtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/JobMtlSearches", {
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
   Summary: Calls GetByID to retrieve the JobMtlSearch item
   Description: Calls GetByID to retrieve the JobMtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobMtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.JobMtlRow
   */  
export function get_JobMtlSearches_Company_JobNum_AssemblySeq_MtlSeq(Company:string, JobNum:string, AssemblySeq:string, MtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/JobMtlSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_JobMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JobMtlSearch for the service
   Description: Calls UpdateExt to update JobMtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobMtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobMtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JobMtlSearches_Company_JobNum_AssemblySeq_MtlSeq(Company:string, JobNum:string, AssemblySeq:string, MtlSeq:string, requestBody:Erp_Tablesets_JobMtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/JobMtlSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", {
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
   Summary: Call UpdateExt to delete JobMtlSearch item
   Description: Call UpdateExt to delete JobMtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobMtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JobMtlSearches_Company_JobNum_AssemblySeq_MtlSeq(Company:string, JobNum:string, AssemblySeq:string, MtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/JobMtlSearches(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobMtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlListRow)
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
export function get_GetRows(whereClauseJobMtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobMtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobMtl=" + whereClauseJobMtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/GetRows" + params, {
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
export function get_GetByID(jobNum:string, assemblySeq:string, mtlSeq:string, epicorHeaders?:Headers){
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
   if(typeof mtlSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "mtlSeq=" + mtlSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewJobMtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobMtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobMtl(requestBody:GetNewJobMtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewJobMtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/GetNewJobMtl", {
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
         resolve(data as GetNewJobMtl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobMtlSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobMtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobMtlRow,
}

export interface Erp_Tablesets_JobMtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  */  
   "JobComplete":boolean,
      /**  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   "IssuedComplete":boolean,
      /**  Job Number.  */  
   "JobNum":string,
      /**  Assembly sequence number that this material is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   "MtlSeq":number,
      /**  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  */  
   "PartNum":string,
      /**  A description of the material.  */  
   "Description":string,
      /**  Quantity per parent.  Field Service was EstQty in FSCallMt.  */  
   "QtyPer":number,
      /**  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  */  
   "RequiredQty":number,
      /**  Internal unit of measure.  The unit used to measure the material.  */  
   "IUM":string,
      /**   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  */  
   "LeadTime":number,
      /**   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   "RelatedOperation":number,
      /**  The material burden rate for this Job Material.  */  
   "MtlBurRate":number,
      /**  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   "EstMtlBurUnitCost":number,
      /**  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   "EstUnitCost":number,
      /**  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  */  
   "IssuedQty":number,
      /**  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  */  
   "TotalCost":number,
      /**  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  */  
   "MtlBurCost":number,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   "ReqDate":string,
      /**  The warehouse that the material is allocated against.  */  
   "WarehouseCode":string,
      /**  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  */  
   "SalvagePartNum":string,
      /**  Description of Salvageable material.  Use Part.Description for a default.  */  
   "SalvageDescription":string,
      /**  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  */  
   "SalvageQtyPer":number,
      /**  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  */  
   "SalvageUM":string,
      /**  The salvage material burden rate for this Job Material.  */  
   "SalvageMtlBurRate":number,
      /**  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   "SalvageUnitCredit":number,
      /**  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   "SalvageEstMtlBurUnitCredit":number,
      /**  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  */  
   "SalvageQtyToDate":number,
      /**  Total salvage credit to date.  A summary of salvage receipt transactions.  */  
   "SalvageCredit":number,
      /**  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  */  
   "SalvageMtlBurCredit":number,
      /**   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  */  
   "MfgComment":string,
      /**  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  */  
   "VendorNum":number,
      /**  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  */  
   "PurPoint":string,
      /**  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  */  
   "BuyIt":boolean,
      /**  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  */  
   "Ordered":boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  */  
   "PurComment":string,
      /**   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  */  
   "BackFlush":boolean,
      /**  Estimated Scrap.  */  
   "EstScrap":number,
      /**  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   "EstScrapType":string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   "FixedQty":boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   "FindNum":string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Controls if an alert is to be sent when this JobMtl is completed.  */  
   "SndAlrtCmpl":boolean,
      /**  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  */  
   "Direct":boolean,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   "MaterialMtlCost":number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialLabCost":number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialSubCost":number,
      /**  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialBurCost":number,
      /**  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageMtlCredit":number,
      /**  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageLbrCredit":number,
      /**  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageBurCredit":number,
      /**  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageSubCredit":number,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   "APSAddResType":string,
      /**  The service call that this Material belongs to.  */  
   "CallNum":number,
      /**  The Service Call Line that this material relates to.  */  
   "CallLine":number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  FS - Unit Price for the Material in base currency.  */  
   "UnitPrice":number,
      /**  FS - Billable Unit Price for the Material in base currency.  */  
   "BillableUnitPrice":number,
      /**  FS - Billable Price per unit for the material in customers currency.  */  
   "DocBillableUnitPrice":number,
      /**  Problem reason code from the reason master table. type Service call.  */  
   "ResReasonCode":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   "PricePerCode":string,
      /**  Is this a billable material item.  */  
   "Billable":boolean,
      /**  Holds the quantity of the item that has been shipped through misc.  shipments  */  
   "ShippedQty":number,
      /**  FS - Unit Price for the Material in Customer currency.  */  
   "DocUnitPrice":number,
      /**  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  */  
   "QtyStagedToDate":number,
      /**  This material was added after initial setup of the job  */  
   "AddedMtl":boolean,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   "MiscCharge":boolean,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   "MiscCode":string,
      /**  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  */  
   "SCMiscCode":string,
      /**  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   "RFQNeeded":boolean,
      /**  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  RFQ number that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   "RFQStat":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   "GlbRFQ":boolean,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   "WhseAllocFlag":boolean,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   "WIReqDate":string,
      /**  Reporting currency value of this field  */  
   "Rpt1BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  */  
   "BaseRequiredQty":number,
      /**   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  */  
   "BaseUOM":string,
      /**  Material Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**  Required number of designators  */  
   "ReqRefDes":number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   "BasePartNum":string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   "BaseRevisionNum":string,
      /**  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   "SelectForPicking":boolean,
      /**  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  */  
   "StagingWarehouseCode":string,
      /**  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  */  
   "StagingBinNum":string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   "PickError":string,
      /**   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstMtlUnitCost":number,
      /**   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstLbrUnitCost":number,
      /**   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstBurUnitCost":number,
      /**   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstSubUnitCost":number,
      /**   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstMtlUnitCredit":number,
      /**   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstLbrUnitCredit":number,
      /**   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstBurUnitCredit":number,
      /**   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstSubUnitCredit":number,
      /**  The material quantity that has been loaned out to another job.  */  
   "LoanedQty":number,
      /**  The material quantity that has been borrowed from another job.  */  
   "BorrowedQty":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ShowStatusIcon  */  
   "ShowStatusIcon":string,
      /**  The display unit price.  */  
   "DisplayUnitPrice":number,
      /**  The display of extended price.  */  
   "DisplayExtPrice":number,
      /**  The currency switch flag  */  
   "CurrencySwitch":boolean,
      /**  The document display extended price  */  
   "DocDisplayUnitPrice":number,
      /**  The document display extended price  */  
   "DocDisplayExtPrice":number,
      /**  The name of the calling program  */  
   "IPCaller":string,
      /**  The description of the related operation  */  
   "RelatedOperationDesc":string,
      /**  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  */  
   "SubContract":boolean,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   "EnableSndAlrtCmpl":boolean,
      /**  Should the backflush field be enabled?  */  
   "EnableBackflush":boolean,
      /**  Can the backflush be unchecked?  */  
   "AllowBackflushUncheck":boolean,
      /**  Logical used to determine if record is created from PO Entry.  */  
   "RetainValues":boolean,
      /**  Price Per Code Description  */  
   "PricePerCodeDescription":string,
      /**  Flag to allow/disallow the user to see the Job Costs. Since the Object designer is not letting me add a boolean, I added a string.  */  
   "AllowJobCosts":string,
      /**  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  */  
   "EstCost":number,
      /**  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  */  
   "EnableRcvInspReq":boolean,
      /**  Satatus of InspectionRequired image on JobMaterial form.  */  
   "ShowInspRqdImg":boolean,
   "EnableMtlSalvage":boolean,
   "EnablePurDir":boolean,
      /**  BuyIt field for display in the UI.  */  
   "dspBuyIt":boolean,
      /**  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  */  
   "EnableBuyIt":boolean,
      /**  IsBaseCurrency  */  
   "IsBaseCurrency":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  BaseUOM for SalvagePartNum  */  
   "SalvageBaseUOM":string,
   "Rpt1DisplayUnitPrice":number,
   "Rpt2DisplayUnitPrice":number,
   "Rpt3DisplayUnitPrice":number,
   "Rpt1DisplayExtPrice":number,
   "Rpt2DisplayExtPrice":number,
   "Rpt3DisplayExtPrice":number,
      /**  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  */  
   "EnableFixedQty":boolean,
      /**  Display IUM (readonly)  */  
   "DspIUM":string,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   "RDPrefix":string,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   "RDSuffix":string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   "RDStartNum":number,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   "RDEndNum":number,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   "EnableSplitCosts":boolean,
   "IsMtlExtConfig":boolean,
      /**  Description  */  
   "AnalysisCdDescription":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "CallLineLineDesc":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Description of the Miscellaneous Charge. Appears on orders, invoices and in drop-down selection lists.  */  
   "MiscCodeDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Full description of Product Group.  */  
   "ProdCodeDescription":string,
      /**  The Landed Cost Currency Code for this miscellaneous charge.  */  
   "PurMiscCodeLCCurrencyCode":string,
      /**  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  */  
   "PurMiscCodeDescription":string,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   "PurMiscCodeLCDisburseMethod":string,
      /**  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  */  
   "PurMiscCodeLCAmount":number,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDescription":string,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   "RFQLineLineDesc":string,
      /**  Description of the Miscellaneous Charge. Appears on orders, invoices and in drop-down selection lists.  */  
   "SCMiscCodeDescription":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  City portion of the address  */  
   "VendorPPCity":string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "VendorPPPrimPCon":number,
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
      /**  First address line  */  
   "VendorPPAddress1":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JobMtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  */  
   "JobComplete":boolean,
      /**  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   "IssuedComplete":boolean,
      /**  Job Number.  */  
   "JobNum":string,
      /**  Assembly sequence number that this material is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   "MtlSeq":number,
      /**  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  */  
   "PartNum":string,
      /**  A description of the material.  */  
   "Description":string,
      /**  Quantity per parent.  Field Service was EstQty in FSCallMt.  */  
   "QtyPer":number,
      /**  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  */  
   "RequiredQty":number,
      /**  Internal unit of measure.  The unit used to measure the material.  */  
   "IUM":string,
      /**   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  */  
   "LeadTime":number,
      /**   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   "RelatedOperation":number,
      /**  The material burden rate for this Job Material.  */  
   "MtlBurRate":number,
      /**  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   "EstMtlBurUnitCost":number,
      /**  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   "EstUnitCost":number,
      /**  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  */  
   "IssuedQty":number,
      /**  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  */  
   "TotalCost":number,
      /**  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  */  
   "MtlBurCost":number,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   "ReqDate":string,
      /**  The warehouse that the material is allocated against.  */  
   "WarehouseCode":string,
      /**  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  */  
   "SalvagePartNum":string,
      /**  Description of Salvageable material.  Use Part.Description for a default.  */  
   "SalvageDescription":string,
      /**  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  */  
   "SalvageQtyPer":number,
      /**  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  */  
   "SalvageUM":string,
      /**  The salvage material burden rate for this Job Material.  */  
   "SalvageMtlBurRate":number,
      /**  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   "SalvageUnitCredit":number,
      /**  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   "SalvageEstMtlBurUnitCredit":number,
      /**  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  */  
   "SalvageQtyToDate":number,
      /**  Total salvage credit to date.  A summary of salvage receipt transactions.  */  
   "SalvageCredit":number,
      /**  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  */  
   "SalvageMtlBurCredit":number,
      /**   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  */  
   "MfgComment":string,
      /**  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  */  
   "VendorNum":number,
      /**  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  */  
   "PurPoint":string,
      /**  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  */  
   "BuyIt":boolean,
      /**  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  */  
   "Ordered":boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  */  
   "PurComment":string,
      /**   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  */  
   "BackFlush":boolean,
      /**  Estimated Scrap.  */  
   "EstScrap":number,
      /**  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   "EstScrapType":string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   "FixedQty":boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   "FindNum":string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Controls if an alert is to be sent when this JobMtl is completed.  */  
   "SndAlrtCmpl":boolean,
      /**  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  */  
   "Direct":boolean,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   "MaterialMtlCost":number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialLabCost":number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialSubCost":number,
      /**  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialBurCost":number,
      /**  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageMtlCredit":number,
      /**  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageLbrCredit":number,
      /**  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageBurCredit":number,
      /**  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageSubCredit":number,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   "APSAddResType":string,
      /**  The service call that this Material belongs to.  */  
   "CallNum":number,
      /**  The Service Call Line that this material relates to.  */  
   "CallLine":number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  FS - Unit Price for the Material in base currency.  */  
   "UnitPrice":number,
      /**  FS - Billable Unit Price for the Material in base currency.  */  
   "BillableUnitPrice":number,
      /**  FS - Billable Price per unit for the material in customers currency.  */  
   "DocBillableUnitPrice":number,
      /**  Problem reason code from the reason master table. type Service call.  */  
   "ResReasonCode":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   "PricePerCode":string,
      /**  Is this a billable material item.  */  
   "Billable":boolean,
      /**  Holds the quantity of the item that has been shipped through misc.  shipments  */  
   "ShippedQty":number,
      /**  FS - Unit Price for the Material in Customer currency.  */  
   "DocUnitPrice":number,
      /**  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  */  
   "QtyStagedToDate":number,
      /**  This material was added after initial setup of the job  */  
   "AddedMtl":boolean,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   "MiscCharge":boolean,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   "MiscCode":string,
      /**  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  */  
   "SCMiscCode":string,
      /**  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   "RFQNeeded":boolean,
      /**  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  RFQ number that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   "RFQStat":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   "GlbRFQ":boolean,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   "WhseAllocFlag":boolean,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   "WIReqDate":string,
      /**  Reporting currency value of this field  */  
   "Rpt1BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  */  
   "BaseRequiredQty":number,
      /**   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  */  
   "BaseUOM":string,
      /**  Material Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**  Required number of designators  */  
   "ReqRefDes":number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   "BasePartNum":string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   "BaseRevisionNum":string,
      /**  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   "SelectForPicking":boolean,
      /**  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  */  
   "StagingWarehouseCode":string,
      /**  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  */  
   "StagingBinNum":string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   "PickError":string,
      /**   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstMtlUnitCost":number,
      /**   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstLbrUnitCost":number,
      /**   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstBurUnitCost":number,
      /**   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstSubUnitCost":number,
      /**   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstMtlUnitCredit":number,
      /**   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstLbrUnitCredit":number,
      /**   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstBurUnitCredit":number,
      /**   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstSubUnitCredit":number,
      /**  The material quantity that has been loaned out to another job.  */  
   "LoanedQty":number,
      /**  The material quantity that has been borrowed from another job.  */  
   "BorrowedQty":number,
      /**  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  */  
   "ReassignSNAsm":boolean,
      /**  GeneralPlanInfo  */  
   "GeneralPlanInfo":string,
      /**  EstStdDescription  */  
   "EstStdDescription":string,
      /**  PricingUOM  */  
   "PricingUOM":string,
      /**  RemovedFromPlan  */  
   "RemovedFromPlan":boolean,
      /**  IsPOCostingMaintained  */  
   "IsPOCostingMaintained":boolean,
      /**  EstStdType  */  
   "EstStdType":number,
      /**  POCostingFactor  */  
   "POCostingFactor":number,
      /**  PlannedQtyPerUnit  */  
   "PlannedQtyPerUnit":number,
      /**  POCostingDirection  */  
   "POCostingDirection":number,
      /**  POCostingUnitVal  */  
   "POCostingUnitVal":number,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   "OrigStructTag":string,
      /**  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   "OrigGroupSeq":number,
      /**  ShowStatusIcon  */  
   "ShowStatusIcon":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   "LinkToContract":boolean,
      /**  Stores the lot number of the material in the Staging Warehouse/Bin.  */  
   "StagingLotNum":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   "LocationView":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "SalvageAttributeSetID":number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   "SalvagePlanningNumberOfPieces":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "SalvagePlanningAttributeSetID":number,
      /**  The identification of related StageNo.  */  
   "RelatedStage":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "SalvageRevisionNum":string,
      /**  Indicates if the job material should be added or removed from the fulfillment queue.  */  
   "PartAllocQueueAction":string,
      /**  This flag indicates if the job material is ready to be fulfilled.  */  
   "ReadyToFulfill":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  The currency switch flag  */  
   "CurrencySwitch":boolean,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
      /**  The display of extended price.  */  
   "DisplayExtPrice":number,
      /**  The display unit price.  */  
   "DisplayUnitPrice":number,
      /**  The document display extended price  */  
   "DocDisplayExtPrice":number,
      /**  The document display extended price  */  
   "DocDisplayUnitPrice":number,
      /**  BuyIt field for display in the UI.  */  
   "dspBuyIt":boolean,
      /**  Display IUM (readonly)  */  
   "DspIUM":string,
      /**  Should the backflush field be enabled?  */  
   "EnableBackflush":boolean,
      /**  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  */  
   "EnableBuyIt":boolean,
      /**  flag to determine whether the Configure Option should be enabled.  */  
   "EnableConfigure":boolean,
      /**  flag to determine whether the Make Direct field should be enabled.  */  
   "EnableDirect":boolean,
      /**  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  */  
   "EnableFixedQty":boolean,
   "EnableMtlSalvage":boolean,
   "EnablePurDir":boolean,
      /**  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  */  
   "EnableRcvInspReq":boolean,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   "EnableSndAlrtCmpl":boolean,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   "EnableSplitCosts":boolean,
      /**  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  */  
   "EstCost":number,
      /**  The name of the calling program  */  
   "IPCaller":string,
      /**  IsBaseCurrency  */  
   "IsBaseCurrency":boolean,
   "IsMtlConfigurationOn":boolean,
   "IsMtlConfigureOn":boolean,
   "IsMtlExtConfig":boolean,
      /**  IsMtlRevisionApproved  */  
   "IsMtlRevisionApproved":boolean,
      /**  Internal flag to identify if current Part is an Inventory Part.  */  
   "PartExists":boolean,
      /**  Calculated field gets list of available Sites  */  
   "PlantList":string,
      /**  Price Per Code Description  */  
   "PricePerCodeDescription":string,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   "RDEndNum":number,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   "RDPrefix":string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   "RDStartNum":number,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   "RDSuffix":string,
      /**  The description of the related operation  */  
   "RelatedOperationDesc":string,
      /**  Logical used to determine if record is created from PO Entry.  */  
   "RetainValues":boolean,
   "Rpt1DisplayExtPrice":number,
   "Rpt1DisplayUnitPrice":number,
   "Rpt2DisplayExtPrice":number,
   "Rpt2DisplayUnitPrice":number,
   "Rpt3DisplayExtPrice":number,
   "Rpt3DisplayUnitPrice":number,
      /**  BaseUOM for SalvagePartNum  */  
   "SalvageBaseUOM":string,
      /**  Satatus of InspectionRequired image on JobMaterial form.  */  
   "ShowInspRqdImg":boolean,
      /**  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  */  
   "SubContract":boolean,
      /**  Can the backflush be unchecked?  */  
   "AllowBackflushUncheck":boolean,
   "EnableAttributeSetSearch":boolean,
   "EnableSalvageAttributeSetSearch":boolean,
      /**  Number of pieces for inventory attribute tracked parts  */  
   "PlanningNumberOfPiecesDisp":number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "SalvagePlanningNumberOfPiecesDisp":number,
      /**  Indicates if unit price calculation should occur.  When false the unit price will be calculated.  When false the unit price will remain its current value.  */  
   "SkipUnitPriceCalc":boolean,
      /**  Error Status Display  */  
   "ErrorStatusDisplay":string,
      /**  True if this job material is in the fulfillment queue.  */  
   "InPartAllocQueue":boolean,
      /**  Show Fulfillment Queue Actions  */  
   "ShowFulfillmentQueueActions":boolean,
      /**  Indicates this row is selected for action.  */  
   "SelectedForAction":boolean,
      /**  The allocated quantity for this job material.  */  
   "AllocatedQty":number,
      /**  The reserved quantity for this job material.  */  
   "ReservedQty":number,
      /**  The available quantity for this job material.  */  
   "AvailableQty":number,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "AssemblySeqPartNum":string,
   "AssemblySeqDescription":string,
   "CallLineLineDesc":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "JobNumPartDescription":string,
   "JobNumPartNum":string,
   "MiscCodeDescription":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PlantName":string,
   "ProdCodeDescription":string,
   "PurMiscCodeDescription":string,
   "PurMiscCodeLCAmount":number,
   "PurMiscCodeLCDisburseMethod":string,
   "PurMiscCodeLCCurrencyCode":string,
   "ReasonDescription":string,
   "RFQLineLineDesc":string,
   "SalvageAttributeSetIDDescription":string,
   "SalvageAttributeSetIDShortDescription":string,
   "SalvagePartNumPartDescription":string,
   "SalvagePartNumPricePerCode":string,
   "SalvagePartNumTrackInventoryByRevision":boolean,
   "SalvagePartNumTrackSerialNum":boolean,
   "SalvagePartNumTrackDimension":boolean,
   "SalvagePartNumTrackInventoryAttributes":boolean,
   "SalvagePartNumAttrClassID":string,
   "SalvagePartNumSellingFactor":number,
   "SalvagePartNumTrackLots":boolean,
   "SalvagePartNumSalesUM":string,
   "SalvagePartNumIUM":string,
   "SCMiscCodeDescription":string,
   "StageNoDescription":string,
   "VendorNumTermsCode":string,
   "VendorNumVendorID":string,
   "VendorNumZIP":string,
   "VendorNumAddress2":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCountry":string,
   "VendorNumState":string,
   "VendorNumAddress3":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress1":string,
   "VendorNumCity":string,
   "VendorNumName":string,
   "VendorPPState":string,
   "VendorPPAddress2":string,
   "VendorPPCountry":string,
   "VendorPPPrimPCon":number,
   "VendorPPZip":string,
   "VendorPPCity":string,
   "VendorPPAddress1":string,
   "VendorPPAddress3":string,
   "VendorPPName":string,
   "WarehouseCodeDescription":string,
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
      @param mtlSeq
   */  
export interface DeleteByID_input{
   jobNum:string,
   assemblySeq:number,
   mtlSeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_JobMtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  */  
   JobComplete:boolean,
      /**  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   IssuedComplete:boolean,
      /**  Job Number.  */  
   JobNum:string,
      /**  Assembly sequence number that this material is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  */  
   PartNum:string,
      /**  A description of the material.  */  
   Description:string,
      /**  Quantity per parent.  Field Service was EstQty in FSCallMt.  */  
   QtyPer:number,
      /**  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  */  
   RequiredQty:number,
      /**  Internal unit of measure.  The unit used to measure the material.  */  
   IUM:string,
      /**   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  */  
   LeadTime:number,
      /**   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   RelatedOperation:number,
      /**  The material burden rate for this Job Material.  */  
   MtlBurRate:number,
      /**  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstMtlBurUnitCost:number,
      /**  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  */  
   IssuedQty:number,
      /**  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  */  
   TotalCost:number,
      /**  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  */  
   MtlBurCost:number,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   ReqDate:string,
      /**  The warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  */  
   SalvagePartNum:string,
      /**  Description of Salvageable material.  Use Part.Description for a default.  */  
   SalvageDescription:string,
      /**  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
      /**  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  */  
   SalvageUM:string,
      /**  The salvage material burden rate for this Job Material.  */  
   SalvageMtlBurRate:number,
      /**  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
      /**  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageEstMtlBurUnitCredit:number,
      /**  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  */  
   SalvageQtyToDate:number,
      /**  Total salvage credit to date.  A summary of salvage receipt transactions.  */  
   SalvageCredit:number,
      /**  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  */  
   SalvageMtlBurCredit:number,
      /**   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  */  
   MfgComment:string,
      /**  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  */  
   VendorNum:number,
      /**  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  */  
   BuyIt:boolean,
      /**  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  */  
   Ordered:boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  */  
   PurComment:string,
      /**   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  */  
   BackFlush:boolean,
      /**  Estimated Scrap.  */  
   EstScrap:number,
      /**  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   EstScrapType:string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   FixedQty:boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   FindNum:string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Controls if an alert is to be sent when this JobMtl is completed.  */  
   SndAlrtCmpl:boolean,
      /**  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  */  
   Direct:boolean,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   MaterialMtlCost:number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialLabCost:number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialSubCost:number,
      /**  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialBurCost:number,
      /**  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageMtlCredit:number,
      /**  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageLbrCredit:number,
      /**  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageBurCredit:number,
      /**  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageSubCredit:number,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   APSAddResType:string,
      /**  The service call that this Material belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this material relates to.  */  
   CallLine:number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  FS - Unit Price for the Material in base currency.  */  
   UnitPrice:number,
      /**  FS - Billable Unit Price for the Material in base currency.  */  
   BillableUnitPrice:number,
      /**  FS - Billable Price per unit for the material in customers currency.  */  
   DocBillableUnitPrice:number,
      /**  Problem reason code from the reason master table. type Service call.  */  
   ResReasonCode:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   PricePerCode:string,
      /**  Is this a billable material item.  */  
   Billable:boolean,
      /**  Holds the quantity of the item that has been shipped through misc.  shipments  */  
   ShippedQty:number,
      /**  FS - Unit Price for the Material in Customer currency.  */  
   DocUnitPrice:number,
      /**  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  */  
   QtyStagedToDate:number,
      /**  This material was added after initial setup of the job  */  
   AddedMtl:boolean,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   MiscCharge:boolean,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   MiscCode:string,
      /**  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  */  
   SCMiscCode:string,
      /**  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   WIReqDate:string,
      /**  Reporting currency value of this field  */  
   Rpt1BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  */  
   BaseRequiredQty:number,
      /**   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  */  
   BaseUOM:string,
      /**  Material Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  */  
   StagingWarehouseCode:string,
      /**  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstMtlUnitCost:number,
      /**   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstLbrUnitCost:number,
      /**   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstBurUnitCost:number,
      /**   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstSubUnitCost:number,
      /**   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstMtlUnitCredit:number,
      /**   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstLbrUnitCredit:number,
      /**   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstBurUnitCredit:number,
      /**   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstSubUnitCredit:number,
      /**  The material quantity that has been loaned out to another job.  */  
   LoanedQty:number,
      /**  The material quantity that has been borrowed from another job.  */  
   BorrowedQty:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ShowStatusIcon  */  
   ShowStatusIcon:string,
      /**  The display unit price.  */  
   DisplayUnitPrice:number,
      /**  The display of extended price.  */  
   DisplayExtPrice:number,
      /**  The currency switch flag  */  
   CurrencySwitch:boolean,
      /**  The document display extended price  */  
   DocDisplayUnitPrice:number,
      /**  The document display extended price  */  
   DocDisplayExtPrice:number,
      /**  The name of the calling program  */  
   IPCaller:string,
      /**  The description of the related operation  */  
   RelatedOperationDesc:string,
      /**  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  */  
   SubContract:boolean,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   EnableSndAlrtCmpl:boolean,
      /**  Should the backflush field be enabled?  */  
   EnableBackflush:boolean,
      /**  Can the backflush be unchecked?  */  
   AllowBackflushUncheck:boolean,
      /**  Logical used to determine if record is created from PO Entry.  */  
   RetainValues:boolean,
      /**  Price Per Code Description  */  
   PricePerCodeDescription:string,
      /**  Flag to allow/disallow the user to see the Job Costs. Since the Object designer is not letting me add a boolean, I added a string.  */  
   AllowJobCosts:string,
      /**  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  */  
   EstCost:number,
      /**  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  */  
   EnableRcvInspReq:boolean,
      /**  Satatus of InspectionRequired image on JobMaterial form.  */  
   ShowInspRqdImg:boolean,
   EnableMtlSalvage:boolean,
   EnablePurDir:boolean,
      /**  BuyIt field for display in the UI.  */  
   dspBuyIt:boolean,
      /**  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  */  
   EnableBuyIt:boolean,
      /**  IsBaseCurrency  */  
   IsBaseCurrency:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  BaseUOM for SalvagePartNum  */  
   SalvageBaseUOM:string,
   Rpt1DisplayUnitPrice:number,
   Rpt2DisplayUnitPrice:number,
   Rpt3DisplayUnitPrice:number,
   Rpt1DisplayExtPrice:number,
   Rpt2DisplayExtPrice:number,
   Rpt3DisplayExtPrice:number,
      /**  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  */  
   EnableFixedQty:boolean,
      /**  Display IUM (readonly)  */  
   DspIUM:string,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   EnableSplitCosts:boolean,
   IsMtlExtConfig:boolean,
      /**  Description  */  
   AnalysisCdDescription:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   CallLineLineDesc:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Description of the Miscellaneous Charge. Appears on orders, invoices and in drop-down selection lists.  */  
   MiscCodeDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Full description of Product Group.  */  
   ProdCodeDescription:string,
      /**  The Landed Cost Currency Code for this miscellaneous charge.  */  
   PurMiscCodeLCCurrencyCode:string,
      /**  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  */  
   PurMiscCodeDescription:string,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   PurMiscCodeLCDisburseMethod:string,
      /**  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  */  
   PurMiscCodeLCAmount:number,
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDescription:string,
      /**   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  */  
   RFQLineLineDesc:string,
      /**  Description of the Miscellaneous Charge. Appears on orders, invoices and in drop-down selection lists.  */  
   SCMiscCodeDescription:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  City portion of the address  */  
   VendorPPCity:string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   VendorPPPrimPCon:number,
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
      /**  First address line  */  
   VendorPPAddress1:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobMtlListTableset{
   JobMtlList:Erp_Tablesets_JobMtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobMtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  */  
   JobComplete:boolean,
      /**  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   IssuedComplete:boolean,
      /**  Job Number.  */  
   JobNum:string,
      /**  Assembly sequence number that this material is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  */  
   PartNum:string,
      /**  A description of the material.  */  
   Description:string,
      /**  Quantity per parent.  Field Service was EstQty in FSCallMt.  */  
   QtyPer:number,
      /**  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  */  
   RequiredQty:number,
      /**  Internal unit of measure.  The unit used to measure the material.  */  
   IUM:string,
      /**   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  */  
   LeadTime:number,
      /**   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   RelatedOperation:number,
      /**  The material burden rate for this Job Material.  */  
   MtlBurRate:number,
      /**  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstMtlBurUnitCost:number,
      /**  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  */  
   IssuedQty:number,
      /**  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  */  
   TotalCost:number,
      /**  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  */  
   MtlBurCost:number,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   ReqDate:string,
      /**  The warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  */  
   SalvagePartNum:string,
      /**  Description of Salvageable material.  Use Part.Description for a default.  */  
   SalvageDescription:string,
      /**  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
      /**  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  */  
   SalvageUM:string,
      /**  The salvage material burden rate for this Job Material.  */  
   SalvageMtlBurRate:number,
      /**  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
      /**  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageEstMtlBurUnitCredit:number,
      /**  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  */  
   SalvageQtyToDate:number,
      /**  Total salvage credit to date.  A summary of salvage receipt transactions.  */  
   SalvageCredit:number,
      /**  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  */  
   SalvageMtlBurCredit:number,
      /**   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  */  
   MfgComment:string,
      /**  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  */  
   VendorNum:number,
      /**  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  */  
   BuyIt:boolean,
      /**  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  */  
   Ordered:boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  */  
   PurComment:string,
      /**   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  */  
   BackFlush:boolean,
      /**  Estimated Scrap.  */  
   EstScrap:number,
      /**  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   EstScrapType:string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   FixedQty:boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   FindNum:string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Controls if an alert is to be sent when this JobMtl is completed.  */  
   SndAlrtCmpl:boolean,
      /**  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  */  
   Direct:boolean,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   MaterialMtlCost:number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialLabCost:number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialSubCost:number,
      /**  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialBurCost:number,
      /**  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageMtlCredit:number,
      /**  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageLbrCredit:number,
      /**  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageBurCredit:number,
      /**  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageSubCredit:number,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   APSAddResType:string,
      /**  The service call that this Material belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this material relates to.  */  
   CallLine:number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  FS - Unit Price for the Material in base currency.  */  
   UnitPrice:number,
      /**  FS - Billable Unit Price for the Material in base currency.  */  
   BillableUnitPrice:number,
      /**  FS - Billable Price per unit for the material in customers currency.  */  
   DocBillableUnitPrice:number,
      /**  Problem reason code from the reason master table. type Service call.  */  
   ResReasonCode:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   PricePerCode:string,
      /**  Is this a billable material item.  */  
   Billable:boolean,
      /**  Holds the quantity of the item that has been shipped through misc.  shipments  */  
   ShippedQty:number,
      /**  FS - Unit Price for the Material in Customer currency.  */  
   DocUnitPrice:number,
      /**  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  */  
   QtyStagedToDate:number,
      /**  This material was added after initial setup of the job  */  
   AddedMtl:boolean,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   MiscCharge:boolean,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   MiscCode:string,
      /**  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  */  
   SCMiscCode:string,
      /**  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   WIReqDate:string,
      /**  Reporting currency value of this field  */  
   Rpt1BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  */  
   BaseRequiredQty:number,
      /**   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  */  
   BaseUOM:string,
      /**  Material Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  */  
   StagingWarehouseCode:string,
      /**  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstMtlUnitCost:number,
      /**   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstLbrUnitCost:number,
      /**   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstBurUnitCost:number,
      /**   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstSubUnitCost:number,
      /**   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstMtlUnitCredit:number,
      /**   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstLbrUnitCredit:number,
      /**   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstBurUnitCredit:number,
      /**   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstSubUnitCredit:number,
      /**  The material quantity that has been loaned out to another job.  */  
   LoanedQty:number,
      /**  The material quantity that has been borrowed from another job.  */  
   BorrowedQty:number,
      /**  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  */  
   ReassignSNAsm:boolean,
      /**  GeneralPlanInfo  */  
   GeneralPlanInfo:string,
      /**  EstStdDescription  */  
   EstStdDescription:string,
      /**  PricingUOM  */  
   PricingUOM:string,
      /**  RemovedFromPlan  */  
   RemovedFromPlan:boolean,
      /**  IsPOCostingMaintained  */  
   IsPOCostingMaintained:boolean,
      /**  EstStdType  */  
   EstStdType:number,
      /**  POCostingFactor  */  
   POCostingFactor:number,
      /**  PlannedQtyPerUnit  */  
   PlannedQtyPerUnit:number,
      /**  POCostingDirection  */  
   POCostingDirection:number,
      /**  POCostingUnitVal  */  
   POCostingUnitVal:number,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigGroupSeq:number,
      /**  ShowStatusIcon  */  
   ShowStatusIcon:string,
      /**  ContractID  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   LinkToContract:boolean,
      /**  Stores the lot number of the material in the Staging Warehouse/Bin.  */  
   StagingLotNum:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   LocationView:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvageAttributeSetID:number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   SalvagePlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvagePlanningAttributeSetID:number,
      /**  The identification of related StageNo.  */  
   RelatedStage:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   SalvageRevisionNum:string,
      /**  Indicates if the job material should be added or removed from the fulfillment queue.  */  
   PartAllocQueueAction:string,
      /**  This flag indicates if the job material is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  The currency switch flag  */  
   CurrencySwitch:boolean,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**  The display of extended price.  */  
   DisplayExtPrice:number,
      /**  The display unit price.  */  
   DisplayUnitPrice:number,
      /**  The document display extended price  */  
   DocDisplayExtPrice:number,
      /**  The document display extended price  */  
   DocDisplayUnitPrice:number,
      /**  BuyIt field for display in the UI.  */  
   dspBuyIt:boolean,
      /**  Display IUM (readonly)  */  
   DspIUM:string,
      /**  Should the backflush field be enabled?  */  
   EnableBackflush:boolean,
      /**  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  */  
   EnableBuyIt:boolean,
      /**  flag to determine whether the Configure Option should be enabled.  */  
   EnableConfigure:boolean,
      /**  flag to determine whether the Make Direct field should be enabled.  */  
   EnableDirect:boolean,
      /**  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  */  
   EnableFixedQty:boolean,
   EnableMtlSalvage:boolean,
   EnablePurDir:boolean,
      /**  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  */  
   EnableRcvInspReq:boolean,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   EnableSndAlrtCmpl:boolean,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   EnableSplitCosts:boolean,
      /**  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  */  
   EstCost:number,
      /**  The name of the calling program  */  
   IPCaller:string,
      /**  IsBaseCurrency  */  
   IsBaseCurrency:boolean,
   IsMtlConfigurationOn:boolean,
   IsMtlConfigureOn:boolean,
   IsMtlExtConfig:boolean,
      /**  IsMtlRevisionApproved  */  
   IsMtlRevisionApproved:boolean,
      /**  Internal flag to identify if current Part is an Inventory Part.  */  
   PartExists:boolean,
      /**  Calculated field gets list of available Sites  */  
   PlantList:string,
      /**  Price Per Code Description  */  
   PricePerCodeDescription:string,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
      /**  The description of the related operation  */  
   RelatedOperationDesc:string,
      /**  Logical used to determine if record is created from PO Entry.  */  
   RetainValues:boolean,
   Rpt1DisplayExtPrice:number,
   Rpt1DisplayUnitPrice:number,
   Rpt2DisplayExtPrice:number,
   Rpt2DisplayUnitPrice:number,
   Rpt3DisplayExtPrice:number,
   Rpt3DisplayUnitPrice:number,
      /**  BaseUOM for SalvagePartNum  */  
   SalvageBaseUOM:string,
      /**  Satatus of InspectionRequired image on JobMaterial form.  */  
   ShowInspRqdImg:boolean,
      /**  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  */  
   SubContract:boolean,
      /**  Can the backflush be unchecked?  */  
   AllowBackflushUncheck:boolean,
   EnableAttributeSetSearch:boolean,
   EnableSalvageAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts  */  
   PlanningNumberOfPiecesDisp:number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   SalvagePlanningNumberOfPiecesDisp:number,
      /**  Indicates if unit price calculation should occur.  When false the unit price will be calculated.  When false the unit price will remain its current value.  */  
   SkipUnitPriceCalc:boolean,
      /**  Error Status Display  */  
   ErrorStatusDisplay:string,
      /**  True if this job material is in the fulfillment queue.  */  
   InPartAllocQueue:boolean,
      /**  Show Fulfillment Queue Actions  */  
   ShowFulfillmentQueueActions:boolean,
      /**  Indicates this row is selected for action.  */  
   SelectedForAction:boolean,
      /**  The allocated quantity for this job material.  */  
   AllocatedQty:number,
      /**  The reserved quantity for this job material.  */  
   ReservedQty:number,
      /**  The available quantity for this job material.  */  
   AvailableQty:number,
   BitFlag:number,
   AnalysisCdDescription:string,
   AssemblySeqPartNum:string,
   AssemblySeqDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   JobNumPartDescription:string,
   JobNumPartNum:string,
   MiscCodeDescription:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PlantName:string,
   ProdCodeDescription:string,
   PurMiscCodeDescription:string,
   PurMiscCodeLCAmount:number,
   PurMiscCodeLCDisburseMethod:string,
   PurMiscCodeLCCurrencyCode:string,
   ReasonDescription:string,
   RFQLineLineDesc:string,
   SalvageAttributeSetIDDescription:string,
   SalvageAttributeSetIDShortDescription:string,
   SalvagePartNumPartDescription:string,
   SalvagePartNumPricePerCode:string,
   SalvagePartNumTrackInventoryByRevision:boolean,
   SalvagePartNumTrackSerialNum:boolean,
   SalvagePartNumTrackDimension:boolean,
   SalvagePartNumTrackInventoryAttributes:boolean,
   SalvagePartNumAttrClassID:string,
   SalvagePartNumSellingFactor:number,
   SalvagePartNumTrackLots:boolean,
   SalvagePartNumSalesUM:string,
   SalvagePartNumIUM:string,
   SCMiscCodeDescription:string,
   StageNoDescription:string,
   VendorNumTermsCode:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumAddress2:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumState:string,
   VendorNumAddress3:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress1:string,
   VendorNumCity:string,
   VendorNumName:string,
   VendorPPState:string,
   VendorPPAddress2:string,
   VendorPPCountry:string,
   VendorPPPrimPCon:number,
   VendorPPZip:string,
   VendorPPCity:string,
   VendorPPAddress1:string,
   VendorPPAddress3:string,
   VendorPPName:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobMtlSearchTableset{
   JobMtl:Erp_Tablesets_JobMtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtJobMtlSearchTableset{
   JobMtl:Erp_Tablesets_JobMtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param jobNum
      @param assemblySeq
      @param mtlSeq
   */  
export interface GetByID_input{
   jobNum:string,
   assemblySeq:number,
   mtlSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_JobMtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_JobMtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_JobMtlSearchTableset[],
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
   returnObj:Erp_Tablesets_JobMtlListTableset[],
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
export interface GetNewJobMtl_input{
   ds:Erp_Tablesets_JobMtlSearchTableset[],
   jobNum:string,
   assemblySeq:number,
}

export interface GetNewJobMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobMtlSearchTableset,
}
}

   /** Required : 
      @param whereClauseJobMtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseJobMtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_JobMtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtJobMtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtJobMtlSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_JobMtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobMtlSearchTableset,
}
}

