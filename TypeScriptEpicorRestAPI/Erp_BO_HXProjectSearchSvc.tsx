import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.HXProjectSearchSvc
// Description: The HXProjectSearch bo.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/$metadata", {
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
   Description: Get HXProjectSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HXProjectSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HXProjectRow
   */  
export function get_HXProjectSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HXProjectRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/HXProjectSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HXProjectRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HXProjectSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HXProjectRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.HXProjectRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HXProjectSearches(requestBody:Erp_Tablesets_HXProjectRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/HXProjectSearches", {
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
   Summary: Calls GetByID to retrieve the HXProjectSearch item
   Description: Calls GetByID to retrieve the HXProjectSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HXProjectSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param Revision Desc: Revision   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.HXProjectRow
   */  
export function get_HXProjectSearches_Company_ProjectID_Revision(Company:string, ProjectID:string, Revision:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_HXProjectRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/HXProjectSearches(" + Company + "," + ProjectID + "," + Revision + ")", {
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
         resolve(data as Erp_Tablesets_HXProjectRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update HXProjectSearch for the service
   Description: Calls UpdateExt to update HXProjectSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HXProjectSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param Revision Desc: Revision   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.HXProjectRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_HXProjectSearches_Company_ProjectID_Revision(Company:string, ProjectID:string, Revision:string, requestBody:Erp_Tablesets_HXProjectRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/HXProjectSearches(" + Company + "," + ProjectID + "," + Revision + ")", {
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
   Summary: Call UpdateExt to delete HXProjectSearch item
   Description: Call UpdateExt to delete HXProjectSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HXProjectSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param Revision Desc: Revision   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_HXProjectSearches_Company_ProjectID_Revision(Company:string, ProjectID:string, Revision:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/HXProjectSearches(" + Company + "," + ProjectID + "," + Revision + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HXProjectListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HXProjectListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HXProjectListRow)
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
export function get_GetRows(whereClauseHXProject:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseHXProject!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseHXProject=" + whereClauseHXProject
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/GetRows" + params, {
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(projectID:string, revision:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof projectID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "projectID=" + projectID
   }
   if(typeof revision!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "revision=" + revision
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewHXProject
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHXProject
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewHXProject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHXProject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewHXProject(requestBody:GetNewHXProject_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewHXProject_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/GetNewHXProject", {
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
         resolve(data as GetNewHXProject_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.HXProjectSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HXProjectListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HXProjectListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HXProjectRow{
   "odatametadata":string,
   "value":Erp_Tablesets_HXProjectRow,
}

export interface Erp_Tablesets_HXProjectListRow{
   "ActiveProject":boolean,
   "BinNum":string,
   "CloseAccrual":boolean,
   "CommentText":string,
   "Company":string,
   "ConBTCustNum":number,
   "ConCustNum":number,
   "ConEndDate":string,
   "ConHrsInvc":string,
   "ConInvMeth":string,
   "ConListCode":string,
   "ConOverCeiling":boolean,
   "ConProjectedEnd":string,
   "ConProjMgr":string,
   "ConReference":string,
   "ConRevMethod":string,
   "ConStartDate":string,
   "ConTotInv":number,
   "ConTotValue":number,
   "CreatePrjJob":boolean,
   "CurrencyCode":string,
   "Description":string,
   "DocConTotInv":number,
   "DocConTotValue":number,
   "DocPBCeilingBur":number,
   "DocPBCeilingFees":number,
   "DocPBCeilingLbr":number,
   "DocPBCeilingMisc":number,
   "DocPBCeilingMtl":number,
   "DocPBCeilingMtlBur":number,
   "DocPBCeilingSub":number,
   "DocPBCeilingTotal":number,
   "DocPBFeeLbrCharge":number,
   "DocPBFeeMiscCharge":number,
   "DocPBFeeMtlCharge":number,
   "DocPBFeeSubCharge":number,
   "DocPPCeilingFees":number,
   "DocPPCeilingTotal":number,
   "DocTotLiqToDate":number,
   "DocTotPPToDate":number,
   "EndDate":string,
   "ExchangeRate":number,
   "HoldPrdInv":boolean,
   "LockRate":boolean,
   "MarkUpID":string,
   "NextTmpInvcNum":number,
   "PBBurMarkUp":number,
   "PBCeilingBur":number,
   "PBCeilingFees":number,
   "PBCeilingLbr":number,
   "PBCeilingMisc":number,
   "PBCeilingMtl":number,
   "PBCeilingMtlBur":number,
   "PBCeilingSub":number,
   "PBCeilingTotal":number,
   "PBDocInvoicedBur":number,
   "PBDocInvoicedFees":number,
   "PBDocInvoicedLbr":number,
   "PBDocInvoicedMisc":number,
   "PBDocInvoicedMtl":number,
   "PBDocInvoicedMtlBur":number,
   "PBDocInvoicedSub":number,
   "PBFeeApply":string,
   "PBFeeApplyOn":string,
   "PBFeeInvoiceText":string,
   "PBFeeLbrApply":string,
   "PBFeeLbrCharge":number,
   "PBFeeLbrType":string,
   "PBFeeMiscApply":string,
   "PBFeeMiscCharge":number,
   "PBFeeMiscType":string,
   "PBFeeMtlApply":string,
   "PBFeeMtlCharge":number,
   "PBFeeMtlType":string,
   "PBFeeProject":number,
   "PBFeeSubApply":string,
   "PBFeeSubCharge":number,
   "PBFeeSubType":string,
   "PBFeeType":string,
   "PBIndCeilingEmp":boolean,
   "PBIndCeilingPRole":boolean,
   "PBIndCeilingSup":boolean,
   "PBLbMarkUp":number,
   "PBMiscMarkUp":number,
   "PBMtlBurMarkUp":number,
   "PBMtlMarkUp":number,
   "PBOverridenMU":boolean,
   "PBPrjRtSrc":string,
   "PBRetentionPcnt":number,
   "PBRetentionProc":string,
   "PBSubMarkUp":number,
   "PersonList":string,
   "PPActive":boolean,
   "PPAllowPcnt":number,
   "PPCeilingFees":number,
   "PPCeilingTotal":number,
   "PrimaryAsmSeq":number,
   "PrimaryJob":string,
   "PrimaryMtl":number,
   "ProdCode":string,
   "ProjectID":string,
   "RateGrpCode":string,
   "RetentionPrcnt":number,
   "RetentionProc":string,
   "Revision":number,
   "Rpt1ConTotInv":number,
   "Rpt1ConTotValue":number,
   "Rpt1PBCeilingBur":number,
   "Rpt1PBCeilingFees":number,
   "Rpt1PBCeilingLbr":number,
   "Rpt1PBCeilingMisc":number,
   "Rpt1PBCeilingMtl":number,
   "Rpt1PBCeilingMtlBur":number,
   "Rpt1PBCeilingSub":number,
   "Rpt1PBCeilingTotal":number,
   "Rpt1PBFeeLbrCharge":number,
   "Rpt1PBFeeMiscCharge":number,
   "Rpt1PBFeeMtlCharge":number,
   "Rpt1PBFeeSubCharge":number,
   "Rpt1PPCeilingFees":number,
   "Rpt1PPCeilingTotal":number,
   "Rpt1TotLiqToDate":number,
   "Rpt1TotPPToDate":number,
   "Rpt2ConTotInv":number,
   "Rpt2ConTotValue":number,
   "Rpt2PBCeilingBur":number,
   "Rpt2PBCeilingFees":number,
   "Rpt2PBCeilingLbr":number,
   "Rpt2PBCeilingMisc":number,
   "Rpt2PBCeilingMtl":number,
   "Rpt2PBCeilingMtlBur":number,
   "Rpt2PBCeilingSub":number,
   "Rpt2PBCeilingTotal":number,
   "Rpt2PBFeeLbrCharge":number,
   "Rpt2PBFeeMiscCharge":number,
   "Rpt2PBFeeMtlCharge":number,
   "Rpt2PBFeeSubCharge":number,
   "Rpt2PPCeilingFees":number,
   "Rpt2PPCeilingTotal":number,
   "Rpt2TotLiqToDate":number,
   "Rpt2TotPPToDate":number,
   "Rpt3ConTotInv":number,
   "Rpt3ConTotValue":number,
   "Rpt3PBCeilingBur":number,
   "Rpt3PBCeilingFees":number,
   "Rpt3PBCeilingLbr":number,
   "Rpt3PBCeilingMisc":number,
   "Rpt3PBCeilingMtl":number,
   "Rpt3PBCeilingMtlBur":number,
   "Rpt3PBCeilingSub":number,
   "Rpt3PBCeilingTotal":number,
   "Rpt3PBFeeLbrCharge":number,
   "Rpt3PBFeeMiscCharge":number,
   "Rpt3PBFeeMtlCharge":number,
   "Rpt3PBFeeSubCharge":number,
   "Rpt3PPCeilingFees":number,
   "Rpt3PPCeilingTotal":number,
   "Rpt3TotLiqToDate":number,
   "Rpt3TotPPToDate":number,
   "SalesCatID":string,
   "StartDate":string,
   "TotLiqToDate":number,
   "TotPPToDate":number,
   "UserMap":string,
   "UserMapData":string,
   "WarehouseCode":string,
   "MtlTaxCatID":string,
   "LbrTaxCatID":string,
   "FeeTaxCatID":string,
   "ODCTaxCatID":string,
   "SubTaxCatID":string,
   "BdnTaxCatID":string,
   "RetTaxCatID":string,
   "TaxOnNetOfRet":boolean,
   "CeilTaxCatID":string,
   "SysRevID":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_HXProjectRow{
   "ActiveProject":boolean,
   "BinNum":string,
   "CloseAccrual":boolean,
   "CommentText":string,
   "Company":string,
   "ConBTCustNum":number,
   "ConCustNum":number,
   "ConEndDate":string,
   "ConHrsInvc":string,
   "ConInvMeth":string,
   "ConListCode":string,
   "ConOverCeiling":boolean,
   "ConProjectedEnd":string,
   "ConProjMgr":string,
   "ConReference":string,
   "ConRevMethod":string,
   "ConStartDate":string,
   "ConTotInv":number,
   "ConTotValue":number,
   "CreatePrjJob":boolean,
   "CurrencyCode":string,
   "Description":string,
   "DocConTotInv":number,
   "DocConTotValue":number,
   "DocPBCeilingBur":number,
   "DocPBCeilingFees":number,
   "DocPBCeilingLbr":number,
   "DocPBCeilingMisc":number,
   "DocPBCeilingMtl":number,
   "DocPBCeilingMtlBur":number,
   "DocPBCeilingSub":number,
   "DocPBCeilingTotal":number,
   "DocPBFeeLbrCharge":number,
   "DocPBFeeMiscCharge":number,
   "DocPBFeeMtlCharge":number,
   "DocPBFeeSubCharge":number,
   "DocPPCeilingFees":number,
   "DocPPCeilingTotal":number,
   "DocTotLiqToDate":number,
   "DocTotPPToDate":number,
   "EndDate":string,
   "ExchangeRate":number,
   "HoldPrdInv":boolean,
   "LockRate":boolean,
   "MarkUpID":string,
   "NextTmpInvcNum":number,
   "PBBurMarkUp":number,
   "PBCeilingBur":number,
   "PBCeilingFees":number,
   "PBCeilingLbr":number,
   "PBCeilingMisc":number,
   "PBCeilingMtl":number,
   "PBCeilingMtlBur":number,
   "PBCeilingSub":number,
   "PBCeilingTotal":number,
   "PBDocInvoicedBur":number,
   "PBDocInvoicedFees":number,
   "PBDocInvoicedLbr":number,
   "PBDocInvoicedMisc":number,
   "PBDocInvoicedMtl":number,
   "PBDocInvoicedMtlBur":number,
   "PBDocInvoicedSub":number,
   "PBFeeApply":string,
   "PBFeeApplyOn":string,
   "PBFeeInvoiceText":string,
   "PBFeeLbrApply":string,
   "PBFeeLbrCharge":number,
   "PBFeeLbrType":string,
   "PBFeeMiscApply":string,
   "PBFeeMiscCharge":number,
   "PBFeeMiscType":string,
   "PBFeeMtlApply":string,
   "PBFeeMtlCharge":number,
   "PBFeeMtlType":string,
   "PBFeeProject":number,
   "PBFeeSubApply":string,
   "PBFeeSubCharge":number,
   "PBFeeSubType":string,
   "PBFeeType":string,
   "PBIndCeilingEmp":boolean,
   "PBIndCeilingPRole":boolean,
   "PBIndCeilingSup":boolean,
   "PBLbMarkUp":number,
   "PBMiscMarkUp":number,
   "PBMtlBurMarkUp":number,
   "PBMtlMarkUp":number,
   "PBOverridenMU":boolean,
   "PBPrjRtSrc":string,
   "PBRetentionPcnt":number,
   "PBRetentionProc":string,
   "PBSubMarkUp":number,
   "PersonList":string,
   "PPActive":boolean,
   "PPAllowPcnt":number,
   "PPCeilingFees":number,
   "PPCeilingTotal":number,
   "PrimaryAsmSeq":number,
   "PrimaryJob":string,
   "PrimaryMtl":number,
   "ProdCode":string,
   "ProjectID":string,
   "RateGrpCode":string,
   "RetentionPrcnt":number,
   "RetentionProc":string,
   "Revision":number,
   "Rpt1ConTotInv":number,
   "Rpt1ConTotValue":number,
   "Rpt1PBCeilingBur":number,
   "Rpt1PBCeilingFees":number,
   "Rpt1PBCeilingLbr":number,
   "Rpt1PBCeilingMisc":number,
   "Rpt1PBCeilingMtl":number,
   "Rpt1PBCeilingMtlBur":number,
   "Rpt1PBCeilingSub":number,
   "Rpt1PBCeilingTotal":number,
   "Rpt1PBFeeLbrCharge":number,
   "Rpt1PBFeeMiscCharge":number,
   "Rpt1PBFeeMtlCharge":number,
   "Rpt1PBFeeSubCharge":number,
   "Rpt1PPCeilingFees":number,
   "Rpt1PPCeilingTotal":number,
   "Rpt1TotLiqToDate":number,
   "Rpt1TotPPToDate":number,
   "Rpt2ConTotInv":number,
   "Rpt2ConTotValue":number,
   "Rpt2PBCeilingBur":number,
   "Rpt2PBCeilingFees":number,
   "Rpt2PBCeilingLbr":number,
   "Rpt2PBCeilingMisc":number,
   "Rpt2PBCeilingMtl":number,
   "Rpt2PBCeilingMtlBur":number,
   "Rpt2PBCeilingSub":number,
   "Rpt2PBCeilingTotal":number,
   "Rpt2PBFeeLbrCharge":number,
   "Rpt2PBFeeMiscCharge":number,
   "Rpt2PBFeeMtlCharge":number,
   "Rpt2PBFeeSubCharge":number,
   "Rpt2PPCeilingFees":number,
   "Rpt2PPCeilingTotal":number,
   "Rpt2TotLiqToDate":number,
   "Rpt2TotPPToDate":number,
   "Rpt3ConTotInv":number,
   "Rpt3ConTotValue":number,
   "Rpt3PBCeilingBur":number,
   "Rpt3PBCeilingFees":number,
   "Rpt3PBCeilingLbr":number,
   "Rpt3PBCeilingMisc":number,
   "Rpt3PBCeilingMtl":number,
   "Rpt3PBCeilingMtlBur":number,
   "Rpt3PBCeilingSub":number,
   "Rpt3PBCeilingTotal":number,
   "Rpt3PBFeeLbrCharge":number,
   "Rpt3PBFeeMiscCharge":number,
   "Rpt3PBFeeMtlCharge":number,
   "Rpt3PBFeeSubCharge":number,
   "Rpt3PPCeilingFees":number,
   "Rpt3PPCeilingTotal":number,
   "Rpt3TotLiqToDate":number,
   "Rpt3TotPPToDate":number,
   "SalesCatID":string,
   "StartDate":string,
   "TotLiqToDate":number,
   "TotPPToDate":number,
   "UserMap":string,
   "UserMapData":string,
   "WarehouseCode":string,
   "MtlTaxCatID":string,
   "LbrTaxCatID":string,
   "FeeTaxCatID":string,
   "ODCTaxCatID":string,
   "SubTaxCatID":string,
   "BdnTaxCatID":string,
   "RetTaxCatID":string,
   "TaxOnNetOfRet":boolean,
   "CeilTaxCatID":string,
   "SysRevID":number,
   "SysRowID":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  LastAction  */  
   "LastAction":string,
      /**  ActionDate  */  
   "ActionDate":string,
   "BitFlag":number,
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
      @param projectID
      @param revision
   */  
export interface DeleteByID_input{
   projectID:string,
   revision:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_HXProjectListRow{
   ActiveProject:boolean,
   BinNum:string,
   CloseAccrual:boolean,
   CommentText:string,
   Company:string,
   ConBTCustNum:number,
   ConCustNum:number,
   ConEndDate:string,
   ConHrsInvc:string,
   ConInvMeth:string,
   ConListCode:string,
   ConOverCeiling:boolean,
   ConProjectedEnd:string,
   ConProjMgr:string,
   ConReference:string,
   ConRevMethod:string,
   ConStartDate:string,
   ConTotInv:number,
   ConTotValue:number,
   CreatePrjJob:boolean,
   CurrencyCode:string,
   Description:string,
   DocConTotInv:number,
   DocConTotValue:number,
   DocPBCeilingBur:number,
   DocPBCeilingFees:number,
   DocPBCeilingLbr:number,
   DocPBCeilingMisc:number,
   DocPBCeilingMtl:number,
   DocPBCeilingMtlBur:number,
   DocPBCeilingSub:number,
   DocPBCeilingTotal:number,
   DocPBFeeLbrCharge:number,
   DocPBFeeMiscCharge:number,
   DocPBFeeMtlCharge:number,
   DocPBFeeSubCharge:number,
   DocPPCeilingFees:number,
   DocPPCeilingTotal:number,
   DocTotLiqToDate:number,
   DocTotPPToDate:number,
   EndDate:string,
   ExchangeRate:number,
   HoldPrdInv:boolean,
   LockRate:boolean,
   MarkUpID:string,
   NextTmpInvcNum:number,
   PBBurMarkUp:number,
   PBCeilingBur:number,
   PBCeilingFees:number,
   PBCeilingLbr:number,
   PBCeilingMisc:number,
   PBCeilingMtl:number,
   PBCeilingMtlBur:number,
   PBCeilingSub:number,
   PBCeilingTotal:number,
   PBDocInvoicedBur:number,
   PBDocInvoicedFees:number,
   PBDocInvoicedLbr:number,
   PBDocInvoicedMisc:number,
   PBDocInvoicedMtl:number,
   PBDocInvoicedMtlBur:number,
   PBDocInvoicedSub:number,
   PBFeeApply:string,
   PBFeeApplyOn:string,
   PBFeeInvoiceText:string,
   PBFeeLbrApply:string,
   PBFeeLbrCharge:number,
   PBFeeLbrType:string,
   PBFeeMiscApply:string,
   PBFeeMiscCharge:number,
   PBFeeMiscType:string,
   PBFeeMtlApply:string,
   PBFeeMtlCharge:number,
   PBFeeMtlType:string,
   PBFeeProject:number,
   PBFeeSubApply:string,
   PBFeeSubCharge:number,
   PBFeeSubType:string,
   PBFeeType:string,
   PBIndCeilingEmp:boolean,
   PBIndCeilingPRole:boolean,
   PBIndCeilingSup:boolean,
   PBLbMarkUp:number,
   PBMiscMarkUp:number,
   PBMtlBurMarkUp:number,
   PBMtlMarkUp:number,
   PBOverridenMU:boolean,
   PBPrjRtSrc:string,
   PBRetentionPcnt:number,
   PBRetentionProc:string,
   PBSubMarkUp:number,
   PersonList:string,
   PPActive:boolean,
   PPAllowPcnt:number,
   PPCeilingFees:number,
   PPCeilingTotal:number,
   PrimaryAsmSeq:number,
   PrimaryJob:string,
   PrimaryMtl:number,
   ProdCode:string,
   ProjectID:string,
   RateGrpCode:string,
   RetentionPrcnt:number,
   RetentionProc:string,
   Revision:number,
   Rpt1ConTotInv:number,
   Rpt1ConTotValue:number,
   Rpt1PBCeilingBur:number,
   Rpt1PBCeilingFees:number,
   Rpt1PBCeilingLbr:number,
   Rpt1PBCeilingMisc:number,
   Rpt1PBCeilingMtl:number,
   Rpt1PBCeilingMtlBur:number,
   Rpt1PBCeilingSub:number,
   Rpt1PBCeilingTotal:number,
   Rpt1PBFeeLbrCharge:number,
   Rpt1PBFeeMiscCharge:number,
   Rpt1PBFeeMtlCharge:number,
   Rpt1PBFeeSubCharge:number,
   Rpt1PPCeilingFees:number,
   Rpt1PPCeilingTotal:number,
   Rpt1TotLiqToDate:number,
   Rpt1TotPPToDate:number,
   Rpt2ConTotInv:number,
   Rpt2ConTotValue:number,
   Rpt2PBCeilingBur:number,
   Rpt2PBCeilingFees:number,
   Rpt2PBCeilingLbr:number,
   Rpt2PBCeilingMisc:number,
   Rpt2PBCeilingMtl:number,
   Rpt2PBCeilingMtlBur:number,
   Rpt2PBCeilingSub:number,
   Rpt2PBCeilingTotal:number,
   Rpt2PBFeeLbrCharge:number,
   Rpt2PBFeeMiscCharge:number,
   Rpt2PBFeeMtlCharge:number,
   Rpt2PBFeeSubCharge:number,
   Rpt2PPCeilingFees:number,
   Rpt2PPCeilingTotal:number,
   Rpt2TotLiqToDate:number,
   Rpt2TotPPToDate:number,
   Rpt3ConTotInv:number,
   Rpt3ConTotValue:number,
   Rpt3PBCeilingBur:number,
   Rpt3PBCeilingFees:number,
   Rpt3PBCeilingLbr:number,
   Rpt3PBCeilingMisc:number,
   Rpt3PBCeilingMtl:number,
   Rpt3PBCeilingMtlBur:number,
   Rpt3PBCeilingSub:number,
   Rpt3PBCeilingTotal:number,
   Rpt3PBFeeLbrCharge:number,
   Rpt3PBFeeMiscCharge:number,
   Rpt3PBFeeMtlCharge:number,
   Rpt3PBFeeSubCharge:number,
   Rpt3PPCeilingFees:number,
   Rpt3PPCeilingTotal:number,
   Rpt3TotLiqToDate:number,
   Rpt3TotPPToDate:number,
   SalesCatID:string,
   StartDate:string,
   TotLiqToDate:number,
   TotPPToDate:number,
   UserMap:string,
   UserMapData:string,
   WarehouseCode:string,
   MtlTaxCatID:string,
   LbrTaxCatID:string,
   FeeTaxCatID:string,
   ODCTaxCatID:string,
   SubTaxCatID:string,
   BdnTaxCatID:string,
   RetTaxCatID:string,
   TaxOnNetOfRet:boolean,
   CeilTaxCatID:string,
   SysRevID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HXProjectListTableset{
   HXProjectList:Erp_Tablesets_HXProjectListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_HXProjectRow{
   ActiveProject:boolean,
   BinNum:string,
   CloseAccrual:boolean,
   CommentText:string,
   Company:string,
   ConBTCustNum:number,
   ConCustNum:number,
   ConEndDate:string,
   ConHrsInvc:string,
   ConInvMeth:string,
   ConListCode:string,
   ConOverCeiling:boolean,
   ConProjectedEnd:string,
   ConProjMgr:string,
   ConReference:string,
   ConRevMethod:string,
   ConStartDate:string,
   ConTotInv:number,
   ConTotValue:number,
   CreatePrjJob:boolean,
   CurrencyCode:string,
   Description:string,
   DocConTotInv:number,
   DocConTotValue:number,
   DocPBCeilingBur:number,
   DocPBCeilingFees:number,
   DocPBCeilingLbr:number,
   DocPBCeilingMisc:number,
   DocPBCeilingMtl:number,
   DocPBCeilingMtlBur:number,
   DocPBCeilingSub:number,
   DocPBCeilingTotal:number,
   DocPBFeeLbrCharge:number,
   DocPBFeeMiscCharge:number,
   DocPBFeeMtlCharge:number,
   DocPBFeeSubCharge:number,
   DocPPCeilingFees:number,
   DocPPCeilingTotal:number,
   DocTotLiqToDate:number,
   DocTotPPToDate:number,
   EndDate:string,
   ExchangeRate:number,
   HoldPrdInv:boolean,
   LockRate:boolean,
   MarkUpID:string,
   NextTmpInvcNum:number,
   PBBurMarkUp:number,
   PBCeilingBur:number,
   PBCeilingFees:number,
   PBCeilingLbr:number,
   PBCeilingMisc:number,
   PBCeilingMtl:number,
   PBCeilingMtlBur:number,
   PBCeilingSub:number,
   PBCeilingTotal:number,
   PBDocInvoicedBur:number,
   PBDocInvoicedFees:number,
   PBDocInvoicedLbr:number,
   PBDocInvoicedMisc:number,
   PBDocInvoicedMtl:number,
   PBDocInvoicedMtlBur:number,
   PBDocInvoicedSub:number,
   PBFeeApply:string,
   PBFeeApplyOn:string,
   PBFeeInvoiceText:string,
   PBFeeLbrApply:string,
   PBFeeLbrCharge:number,
   PBFeeLbrType:string,
   PBFeeMiscApply:string,
   PBFeeMiscCharge:number,
   PBFeeMiscType:string,
   PBFeeMtlApply:string,
   PBFeeMtlCharge:number,
   PBFeeMtlType:string,
   PBFeeProject:number,
   PBFeeSubApply:string,
   PBFeeSubCharge:number,
   PBFeeSubType:string,
   PBFeeType:string,
   PBIndCeilingEmp:boolean,
   PBIndCeilingPRole:boolean,
   PBIndCeilingSup:boolean,
   PBLbMarkUp:number,
   PBMiscMarkUp:number,
   PBMtlBurMarkUp:number,
   PBMtlMarkUp:number,
   PBOverridenMU:boolean,
   PBPrjRtSrc:string,
   PBRetentionPcnt:number,
   PBRetentionProc:string,
   PBSubMarkUp:number,
   PersonList:string,
   PPActive:boolean,
   PPAllowPcnt:number,
   PPCeilingFees:number,
   PPCeilingTotal:number,
   PrimaryAsmSeq:number,
   PrimaryJob:string,
   PrimaryMtl:number,
   ProdCode:string,
   ProjectID:string,
   RateGrpCode:string,
   RetentionPrcnt:number,
   RetentionProc:string,
   Revision:number,
   Rpt1ConTotInv:number,
   Rpt1ConTotValue:number,
   Rpt1PBCeilingBur:number,
   Rpt1PBCeilingFees:number,
   Rpt1PBCeilingLbr:number,
   Rpt1PBCeilingMisc:number,
   Rpt1PBCeilingMtl:number,
   Rpt1PBCeilingMtlBur:number,
   Rpt1PBCeilingSub:number,
   Rpt1PBCeilingTotal:number,
   Rpt1PBFeeLbrCharge:number,
   Rpt1PBFeeMiscCharge:number,
   Rpt1PBFeeMtlCharge:number,
   Rpt1PBFeeSubCharge:number,
   Rpt1PPCeilingFees:number,
   Rpt1PPCeilingTotal:number,
   Rpt1TotLiqToDate:number,
   Rpt1TotPPToDate:number,
   Rpt2ConTotInv:number,
   Rpt2ConTotValue:number,
   Rpt2PBCeilingBur:number,
   Rpt2PBCeilingFees:number,
   Rpt2PBCeilingLbr:number,
   Rpt2PBCeilingMisc:number,
   Rpt2PBCeilingMtl:number,
   Rpt2PBCeilingMtlBur:number,
   Rpt2PBCeilingSub:number,
   Rpt2PBCeilingTotal:number,
   Rpt2PBFeeLbrCharge:number,
   Rpt2PBFeeMiscCharge:number,
   Rpt2PBFeeMtlCharge:number,
   Rpt2PBFeeSubCharge:number,
   Rpt2PPCeilingFees:number,
   Rpt2PPCeilingTotal:number,
   Rpt2TotLiqToDate:number,
   Rpt2TotPPToDate:number,
   Rpt3ConTotInv:number,
   Rpt3ConTotValue:number,
   Rpt3PBCeilingBur:number,
   Rpt3PBCeilingFees:number,
   Rpt3PBCeilingLbr:number,
   Rpt3PBCeilingMisc:number,
   Rpt3PBCeilingMtl:number,
   Rpt3PBCeilingMtlBur:number,
   Rpt3PBCeilingSub:number,
   Rpt3PBCeilingTotal:number,
   Rpt3PBFeeLbrCharge:number,
   Rpt3PBFeeMiscCharge:number,
   Rpt3PBFeeMtlCharge:number,
   Rpt3PBFeeSubCharge:number,
   Rpt3PPCeilingFees:number,
   Rpt3PPCeilingTotal:number,
   Rpt3TotLiqToDate:number,
   Rpt3TotPPToDate:number,
   SalesCatID:string,
   StartDate:string,
   TotLiqToDate:number,
   TotPPToDate:number,
   UserMap:string,
   UserMapData:string,
   WarehouseCode:string,
   MtlTaxCatID:string,
   LbrTaxCatID:string,
   FeeTaxCatID:string,
   ODCTaxCatID:string,
   SubTaxCatID:string,
   BdnTaxCatID:string,
   RetTaxCatID:string,
   TaxOnNetOfRet:boolean,
   CeilTaxCatID:string,
   SysRevID:number,
   SysRowID:string,
      /**  ContractID  */  
   ContractID:string,
      /**  LastAction  */  
   LastAction:string,
      /**  ActionDate  */  
   ActionDate:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_HXProjectSearchTableset{
   HXProject:Erp_Tablesets_HXProjectRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtHXProjectSearchTableset{
   HXProject:Erp_Tablesets_HXProjectRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param projectID
      @param revision
   */  
export interface GetByID_input{
   projectID:string,
   revision:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_HXProjectSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_HXProjectSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_HXProjectSearchTableset[],
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
   returnObj:Erp_Tablesets_HXProjectListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param projectID
   */  
export interface GetNewHXProject_input{
   ds:Erp_Tablesets_HXProjectSearchTableset[],
   projectID:string,
}

export interface GetNewHXProject_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HXProjectSearchTableset,
}
}

   /** Required : 
      @param whereClauseHXProject
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseHXProject:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_HXProjectSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtHXProjectSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtHXProjectSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_HXProjectSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_HXProjectSearchTableset,
}
}

