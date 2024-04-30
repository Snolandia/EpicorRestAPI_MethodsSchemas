import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ProjPhaseSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/$metadata", {
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
   Description: Get ProjPhaseSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProjPhaseSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjPhaseRow
   */  
export function get_ProjPhaseSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjPhaseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/ProjPhaseSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjPhaseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProjPhaseSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProjPhaseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ProjPhaseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProjPhaseSearches(requestBody:Erp_Tablesets_ProjPhaseRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/ProjPhaseSearches", {
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
   Summary: Calls GetByID to retrieve the ProjPhaseSearch item
   Description: Calls GetByID to retrieve the ProjPhaseSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProjPhaseSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param PhaseID Desc: PhaseID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProjPhaseRow
   */  
export function get_ProjPhaseSearches_Company_ProjectID_PhaseID(Company:string, ProjectID:string, PhaseID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProjPhaseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/ProjPhaseSearches(" + Company + "," + ProjectID + "," + PhaseID + ")", {
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
         resolve(data as Erp_Tablesets_ProjPhaseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ProjPhaseSearch for the service
   Description: Calls UpdateExt to update ProjPhaseSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProjPhaseSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param PhaseID Desc: PhaseID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProjPhaseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ProjPhaseSearches_Company_ProjectID_PhaseID(Company:string, ProjectID:string, PhaseID:string, requestBody:Erp_Tablesets_ProjPhaseRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/ProjPhaseSearches(" + Company + "," + ProjectID + "," + PhaseID + ")", {
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
   Summary: Call UpdateExt to delete ProjPhaseSearch item
   Description: Call UpdateExt to delete ProjPhaseSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProjPhaseSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ProjectID Desc: ProjectID   Required: True   Allow empty value : True
      @param PhaseID Desc: PhaseID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ProjPhaseSearches_Company_ProjectID_PhaseID(Company:string, ProjectID:string, PhaseID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/ProjPhaseSearches(" + Company + "," + ProjectID + "," + PhaseID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjPhaseListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjPhaseListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjPhaseListRow)
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
export function get_GetRows(whereClauseProjPhase:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseProjPhase!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseProjPhase=" + whereClauseProjPhase
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(projectID:string, phaseID:string, epicorHeaders?:Headers){
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
   if(typeof phaseID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "phaseID=" + phaseID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/GetByID" + params, {
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
   Summary: Invoke method GetNewProjPhase
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProjPhase
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewProjPhase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProjPhase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewProjPhase(requestBody:GetNewProjPhase_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewProjPhase_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/GetNewProjPhase", {
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
         resolve(data as GetNewProjPhase_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjPhaseSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjPhaseListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ProjPhaseListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjPhaseRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ProjPhaseRow,
}

export interface Erp_Tablesets_ProjPhaseListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Description  */  
   "Description":string,
      /**  Task start date.  */  
   "StartDate":string,
      /**  Task due date.  */  
   "DueDate":string,
      /**  Must be greater than or equal to 0.  */  
   "PercentComplete":number,
      /**  Date this task was complete.  */  
   "DateComplete":string,
      /**  Valid values are "N" = Not started, "I" = In Process, "C" = Completed.  */  
   "PhaseStatus":string,
      /**  This is the duration of the WBS Phase. On the UK software this currently uses field Number09  */  
   "Duration":number,
      /**  Reference to the job number created for the WBS Phase.  */  
   "WBSJobNum":string,
      /**  This is the parent phase for this WBS Phase. On the UK software this currently uses field ShortChar01  */  
   "ParentPhase":string,
      /**  The task ID that is returned from Microsoft Project.  */  
   "MSPTaskID":string,
      /**  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back a alpha numeric string.  */  
   "MSPPredecessor":string,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMapData":string,
      /**  Total budget burden hours for the Project phase.  */  
   "BudTotBurHrs":number,
      /**  Total budget labour cost for the Project phase. This is production and setup combined.  */  
   "BudTotLbrCost":number,
      /**  Total budget burden cost for the Project phase. This is production and setup combined.  */  
   "BudTotBurCost":number,
      /**  Total budget material costs for the Project phase  */  
   "BudTotMtlCost":number,
      /**  Total budget material burden costs for the Project phase.  */  
   "BudTotMtlBurCost":number,
      /**  Manually entered estimate to complete for the labour hours for the project phase  */  
   "ManEstCtcLbrHrs":number,
      /**  Manually entered estimate to complete for the burden hours.  */  
   "ManEstCtcBurHrs":number,
      /**  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project phase.  */  
   "ManEstCtcLbrCost":number,
      /**  Manually entered estimate to complete for the burden cost for the project phase.  */  
   "ManEstCtcBurCost":number,
      /**  Manually entered estimate to complete for the Subcontract cost for the project phase.  */  
   "ManEstCtcSubConCost":number,
      /**  Manually entered estimate to complete for the material cost for the project phase.  */  
   "ManEstCtcMtlCost":number,
      /**  Manually entered estimate to complete for the material burden cost for the project phase.  */  
   "ManEstCtcMtlBurCost":number,
      /**  Total calculated cost to complete labour cost for the Project phase. This will be both production and setup.  */  
   "TotCtcLbrCost":number,
      /**  Total calculated cost to complete burden cost for the Project phase. This will be both production and setup.  */  
   "TotCtcBurCost":number,
      /**  Total calculated cost to complete subcontract cost for the Project phase.  */  
   "TotCtcSubConCost":number,
      /**  Total calculated cost to complete material cost for the Project phase.  */  
   "TotCtcMtlCost":number,
      /**  Total calculated cost to complete material burden cost for the Project phase.  */  
   "TotCtcMtlBurCost":number,
      /**  Total quoted labour hours for the Project phase  */  
   "TotQuotLbrHrs":number,
      /**  Total quoted burden hours for the Project phase.  */  
   "TotQuotBurHrs":number,
      /**  Total quoted labour cost for the Project phase. This will be both production and setup.  */  
   "TotQuotLbrCost":number,
      /**  Total quoted burden cost for the Project phase. This will be both production and setup.  */  
   "TotQuotBurCost":number,
      /**  Total quoted subcontract cost for the Project phase.  */  
   "TotQuotSubContCost":number,
      /**  Total quoted material cost for the Project phase.  */  
   "TotQuotMtlCost":number,
      /**  Total quoted material burden cost for the Project phase.  */  
   "TotQuotMtlBurCost":number,
      /**  This holds the bom level of the phase reletive to the parent.  */  
   "Level":number,
      /**  This is will either be Hours or Days  */  
   "DurationType":string,
      /**  'Roll Child Manual Cost to Complete to this Level  */  
   "RollChildMan":boolean,
      /**  Roll Child Budgets to this Level  */  
   "RollChildBud":boolean,
      /**  Sort Sequence of the project phase.  This field controls where on the project tree the phase needs to be displayed.  */  
   "SortSeq":number,
      /**  Reference to the Measured Work header.  It is used to collect the cost to determine if the Measured Work was profitable or not.  */  
   "MeasuredWorkID":string,
      /**  Total quoted other direct cost for the Project phase.  */  
   "TotQuotODCCost":number,
      /**  Other direct cost manual CTC  */  
   "ManEstCTCODCCost":number,
      /**  Total calculated cost to complete other direct cost for the Project phase.  */  
   "TotCTCODCCost":number,
      /**  Other direct cost Budget Total  */  
   "BudTotODCCost":number,
      /**  Defines the Approvals Method for Time related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  */  
   "TimeApprovalsMethod":string,
      /**  Unique identifier of the workflow group for Time transactions related to this WBS Phase.  */  
   "TimeWFGroupID":string,
      /**  Defines the Approvals Method for Expenses related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  */  
   "ExpenseApprovalsMethod":string,
      /**  Unique identifier of the workflow group for Expense transactions related to this WBS Phase.  */  
   "ExpenseWFGroupID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery.  */  
   "RevMethod":string,
   "WorkResDesc":string,
   "StatusDesc":string,
   "GTActualCost":number,
   "GTBudgetCost":number,
   "GTCalculatedCost":number,
   "GTEstimatedCost":number,
   "GTManualCost":number,
   "GTQuotedCost":number,
   "createWBSJob":boolean,
   "PhaseDesc":string,
   "TimeWFGroupIDDescription":string,
   "ExpenseWFGroupIDDescription":string,
   "EnableApprovals":boolean,
   "TimeDefTaskSetID":string,
   "ExpenseDefTaskSetID":string,
   "ExpenseTaskSetDescription":string,
   "TimeTaskSetDescription":string,
      /**  Flag to indicate whether the PPhaseOper for this ProjPhase should allow updates based on the status of the WBSJobNum.  */  
   "EnableUpdOper":boolean,
      /**  Full description of Project Management Code.  */  
   "ProjectIDDescription":string,
      /**  External field to create a WBS Phase Combo.  */  
   "ProjPhaseID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ProjPhaseRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Description  */  
   "Description":string,
      /**  Task start date.  */  
   "StartDate":string,
      /**  Task due date.  */  
   "DueDate":string,
      /**  Must be greater than or equal to 0.  */  
   "PercentComplete":number,
      /**  Date this task was complete.  */  
   "DateComplete":string,
      /**  Valid values are "N" = Not started, "I" = In Process, "C" = Completed.  */  
   "PhaseStatus":string,
      /**  This is the duration of the WBS Phase. On the UK software this currently uses field Number09  */  
   "Duration":number,
      /**  Reference to the job number created for the WBS Phase.  */  
   "WBSJobNum":string,
      /**  This is the parent phase for this WBS Phase. On the UK software this currently uses field ShortChar01  */  
   "ParentPhase":string,
      /**  The task ID that is returned from Microsoft Project.  */  
   "MSPTaskID":string,
      /**  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back a alpha numeric string.  */  
   "MSPPredecessor":string,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMapData":string,
      /**  Total budget labour hours for the Project phase  */  
   "BudTotLbrHours":number,
      /**  Total budget burden hours for the Project phase.  */  
   "BudTotBurHrs":number,
      /**  Total budget labour cost for the Project phase. This is production and setup combined.  */  
   "BudTotLbrCost":number,
      /**  Total budget burden cost for the Project phase. This is production and setup combined.  */  
   "BudTotBurCost":number,
      /**  Total budget subcontract costs for the Project phase  */  
   "BudTotSubCost":number,
      /**  Total budget material costs for the Project phase  */  
   "BudTotMtlCost":number,
      /**  Total budget material burden costs for the Project phase.  */  
   "BudTotMtlBurCost":number,
      /**  Total estimated labour hours for the Project phase  */  
   "TotEstLbrHrs":number,
      /**  Total estimated burden hours for the Project phase  */  
   "TotEstBurdenHrs":number,
      /**  Total estimated labour cost for the Project phase. This is production and setup combined.  */  
   "TotEstLbrCost":number,
      /**  Total estimated subcontract costs for the Project phase  */  
   "TotEstSubContCost":number,
      /**  Total estimated material costs for the Project phase  */  
   "TotEstMtlCost":number,
      /**  Total actual labour hours for the Project phase  */  
   "TotActLbrHrs":number,
      /**  Total actual burden hours for the Project phase  */  
   "TotActBurHrs":number,
      /**  Total actual labour cost for the Project phase. This is production and setup combined.  */  
   "TotActLbrCost":number,
      /**  Total actual burden cost for the Project phase. This is production and setup combined.  */  
   "TotActBurCost":number,
      /**  Total actual subcontract costs for the Project phase.  */  
   "TotActSubContCost":number,
      /**  Total actual material costs for the Project phase  */  
   "TotActMtlCost":number,
      /**  Total actual material burden costs for the Project phase.  */  
   "TotActMtlBurCost":number,
      /**  Manually entered estimate to complete for the labour hours for the project phase  */  
   "ManEstCtcLbrHrs":number,
      /**  Manually entered estimate to complete for the burden hours.  */  
   "ManEstCtcBurHrs":number,
      /**  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project phase.  */  
   "ManEstCtcLbrCost":number,
      /**  Manually entered estimate to complete for the burden cost for the project phase.  */  
   "ManEstCtcBurCost":number,
      /**  Manually entered estimate to complete for the Subcontract cost for the project phase.  */  
   "ManEstCtcSubConCost":number,
      /**  Manually entered estimate to complete for the material cost for the project phase.  */  
   "ManEstCtcMtlCost":number,
      /**  Manually entered estimate to complete for the material burden cost for the project phase.  */  
   "ManEstCtcMtlBurCost":number,
      /**  Total calculated cost to complete labour hours for the Project phase.  */  
   "TotCtcLbrHours":number,
      /**  Total calculated cost to complete burden hours for the Project phase.  */  
   "TotCtcBurHours":number,
      /**  Total calculated cost to complete labour cost for the Project phase. This will be both production and setup.  */  
   "TotCtcLbrCost":number,
      /**  Total calculated cost to complete burden cost for the Project phase. This will be both production and setup.  */  
   "TotCtcBurCost":number,
      /**  Total calculated cost to complete subcontract cost for the Project phase.  */  
   "TotCtcSubConCost":number,
      /**  Total calculated cost to complete material cost for the Project phase.  */  
   "TotCtcMtlCost":number,
      /**  Total calculated cost to complete material burden cost for the Project phase.  */  
   "TotCtcMtlBurCost":number,
      /**  Total quoted labour hours for the Project phase  */  
   "TotQuotLbrHrs":number,
      /**  Total quoted burden hours for the Project phase.  */  
   "TotQuotBurHrs":number,
      /**  Total quoted labour cost for the Project phase. This will be both production and setup.  */  
   "TotQuotLbrCost":number,
      /**  Total quoted burden cost for the Project phase. This will be both production and setup.  */  
   "TotQuotBurCost":number,
      /**  Total quoted subcontract cost for the Project phase.  */  
   "TotQuotSubContCost":number,
      /**  Total quoted material cost for the Project phase.  */  
   "TotQuotMtlCost":number,
      /**  Total quoted material burden cost for the Project phase.  */  
   "TotQuotMtlBurCost":number,
      /**  This holds the bom level of the phase reletive to the parent.  */  
   "Level":number,
      /**  This is will either be Hours or Days  */  
   "DurationType":string,
      /**  Total estimated burden cost for the Project phase. This is production and setup combined.  */  
   "TotEstBurCost":number,
      /**  Total estimated material burden costs for the Project phase  */  
   "TotEstMtlBurCost":number,
      /**  'Roll Child Manual Cost to Complete to this Level  */  
   "RollChildMan":boolean,
      /**  Roll Child Budgets to this Level  */  
   "RollChildBud":boolean,
      /**  Sort Sequence of the project phase.  This field controls where on the project tree the phase needs to be displayed.  */  
   "SortSeq":number,
      /**  Reference to the Measured Work header.  It is used to collect the cost to determine if the Measured Work was profitable or not.  */  
   "MeasuredWorkID":string,
      /**  Total quoted other direct cost for the Project phase.  */  
   "TotQuotODCCost":number,
      /**  Total estimated other direct costs for the Project phase  */  
   "TotEstODCCost":number,
      /**  Total actual other direct costs for the Project phase.  */  
   "TotActODCCost":number,
      /**  Other direct cost manual CTC  */  
   "ManEstCTCODCCost":number,
      /**  Total calculated cost to complete other direct cost for the Project phase.  */  
   "TotCTCODCCost":number,
      /**  Other direct cost Budget Total  */  
   "BudTotODCCost":number,
      /**  Defines the Approvals Method for Time related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  */  
   "TimeApprovalsMethod":string,
      /**  Unique identifier of the workflow group for Time transactions related to this WBS Phase.  */  
   "TimeWFGroupID":string,
      /**  Defines the Approvals Method for Expenses related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  */  
   "ExpenseApprovalsMethod":string,
      /**  Unique identifier of the workflow group for Expense transactions related to this WBS Phase.  */  
   "ExpenseWFGroupID":string,
      /**  PartNum  */  
   "PartNum":string,
      /**  RevisionNum  */  
   "RevisionNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Invoicing Method  */  
   "InvMethod":string,
      /**  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery.  */  
   "RevMethod":string,
      /**  Sales Order Number  */  
   "OrderNum":number,
      /**  Sales Order Line  */  
   "OrderLine":number,
      /**  If any activity of the job assigned to the Phase has been recognized or invoiced  */  
   "WasRecInvoiced":boolean,
      /**  Date of last Build WBS Phase Analysis run.  */  
   "LastBuildWBSPhaseAnalysisDate":string,
      /**  Percentage of Completion  */  
   "PercentageOfCompletion":number,
      /**  Labor Cost To Be Recognized  */  
   "ToBeRecognizedLbrCost":number,
      /**  Burden Cost To Be Recognized  */  
   "ToBeRecognizedBurCost":number,
      /**  Material Cost To Be Recognized  */  
   "ToBeRecognizedMtlCost":number,
      /**  Subcontract Cost To Be Recognized  */  
   "ToBeRecognizedSubCost":number,
      /**  Material Burden Cost To Be Recognized  */  
   "ToBeRecognizedMtlBurCost":number,
      /**  ODC Cost To Be Recognized  */  
   "ToBeRecognizedODCCost":number,
      /**  Revenue To Be Recognized  */  
   "ToBeRecognizedRevenue":number,
      /**  When true,  Recognize Revenue separately at Child WBS Phases.  When false, Recognize Revenue for this phase and all child phases at this level.  */  
   "RecognizeRevenueAtChildPhaseLevel":boolean,
      /**  To control if the project phase budget values are to be rolled up to the project phase.  */  
   "RollBudgetsToWBSPhase":boolean,
      /**  TotWBSPhaseRev  */  
   "TotWBSPhaseRev":number,
      /**  The sales category code used in the Revenue recognition process.  */  
   "SalesCatID":string,
      /**  ActMtlNonJobCost  */  
   "ActMtlNonJobCost":number,
      /**  AsOfDate  */  
   "AsOfDate":string,
      /**  Number of Recalculation of burden amounts posted to GL by Revenue Recognition process  */  
   "BdnRecSeqPosted":number,
      /**  Number of Recalculation of burden amounts created by Revenue Recognition process  */  
   "BdnRecSeqLastAdded":number,
      /**  Sum of all Actual Burden Charges posted by today  */  
   "BdnRevenueAutoToday":number,
      /**  BillingToDate  */  
   "BillingToDate":number,
      /**  BuildAnalysis  */  
   "BuildAnalysis":boolean,
      /**  The burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActBurdenCost  */  
   "BurdenCostOfSales":number,
      /**  BurdenLbrCstToDate  */  
   "BurdenLbrCstToDate":number,
      /**  The burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   "BurdenRecAutoCstTodate":number,
      /**  The burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process  */  
   "BurdenRecManCstTodate":number,
      /**  BurManPosted  */  
   "BurManPosted":number,
      /**  BurPur  */  
   "BurPur":number,
      /**  Estimated burden cost.  */  
   "EstBurdenCost":number,
      /**  Estimated burden hours.  */  
   "EstBurdenHours":number,
      /**  Estimated labor cost.  */  
   "EstLaborCost":number,
      /**  Estimated labor hours.  */  
   "EstLaborHours":number,
      /**  Estimated material burden cost.  */  
   "EstMtlBurdenCost":number,
      /**  Estimated material cost.  */  
   "EstMtlCost":number,
      /**  Estimated other direct cost.  */  
   "EstODCCost":number,
      /**  Estimated subcontract cost.  */  
   "EstSubcontractCost":number,
      /**  The labour costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActLaborCost.  */  
   "LaborCostOfSales":number,
      /**  LaborLbrCstToDate  */  
   "LaborLbrCstToDate":number,
      /**  The labour costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   "LaborRecAutoCstTodate":number,
      /**  The labor costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   "LaborRecManCstTodate":number,
      /**  LbrManPosted  */  
   "LbrManPosted":number,
      /**  LbrPur  */  
   "LbrPur":number,
      /**  The material costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of Material with a linesource of COS with value from ProjectAnalysis.ActMatCost.  */  
   "MaterialCostOfSales":number,
      /**  The material costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   "MaterialRecAutoCstTodate":number,
      /**  The material costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   "MaterialRecManCstTodate":number,
      /**  The material burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActMatBurdenCost  */  
   "MtlBurdenCostOfSales":number,
      /**  The material burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  */  
   "MtlBurdenRecAutoCstTodate":number,
      /**  The material burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   "MtlBurdenRecManCstTodate":number,
      /**  MtlBurManPosted  */  
   "MtlBurManPosted":number,
      /**  MtlBurPur  */  
   "MtlBurPur":number,
      /**  MtlManPosted  */  
   "MtlManPosted":number,
      /**  MtlPur  */  
   "MtlPur":number,
      /**  NextTmpInvcNum  */  
   "NextTmpInvcNum":number,
      /**  ODCManPosted  */  
   "ODCManPosted":number,
      /**  ODCPur  */  
   "ODCPur":number,
      /**  Other Direct cost Recognition to Date  */  
   "ODCRecAutoCstToDate":number,
      /**  Other Direct Cost Manual Recognition to Date  */  
   "ODCRecManCstTodate":number,
      /**  RecManPosted  */  
   "RecManPosted":number,
      /**  RecogToDtBilling  */  
   "RecogToDtBilling":number,
      /**  RecogToDtLbk  */  
   "RecogToDtLbk":number,
      /**  RecogToDtManual  */  
   "RecogToDtManual":number,
      /**  RetentionDt  */  
   "RetentionDt":number,
      /**  The revenue that has been recognised to date for the project. This is revenue that has been invoiced against the sales order either as an advanced billing or a shipment. This is the sum of ProjectAnalysis records with a Linecode of Revenue with a linesource of Invoice with value from ProjectAnalysis.ActMatCost.  */  
   "RevenueRecAutoToDate":number,
      /**  The revenue that has been recognised to date for the project. This is revenue that has been manually recognised using this process.  */  
   "RevenueRecManToDate":number,
      /**  Reverse  */  
   "Reverse":string,
      /**  RollManEstToCpte  */  
   "RollManEstToCpte":boolean,
      /**  SubCManPosted  */  
   "SubCManPosted":number,
      /**  SubConCostOfSales  */  
   "SubConCostOfSales":number,
      /**  SubConRecAutoCstTodate  */  
   "SubConRecAutoCstTodate":number,
      /**  SubConRecManCstTodate  */  
   "SubConRecManCstTodate":number,
      /**  SubPur  */  
   "SubPur":number,
      /**  Total contract value for the WBS Phase.  */  
   "ConTotValue":number,
      /**  Total contract value for the WBS Phase in the Document currency.  */  
   "DocConTotValue":number,
      /**  Total contract value for the WBS Phase in the Reporting currency.  */  
   "Rpt1ConTotValue":number,
      /**  Total contract value for the WBS Phase in the Reporting currency.  */  
   "Rpt2ConTotValue":number,
      /**  Total contract value for the WBS Phase in the Reporting currency.  */  
   "Rpt3ConTotValue":number,
      /**  Net total contract value for the WBS Phase.  */  
   "ConTotValueNet":number,
      /**  Net total contract value for the WBS Phase in the Document currency.  */  
   "DocConTotValueNet":number,
      /**  Net total contract value for the WBS Phase in the Reporting currency.  */  
   "Rpt1ConTotValueNet":number,
      /**  Net total contract value for the WBS Phase in the Reporting currency.  */  
   "Rpt2ConTotValueNet":number,
      /**  Net total contract value for the WBS Phase in the Reporting currency.  */  
   "Rpt3ConTotValueNet":number,
   "CloseWBSJob":boolean,
   "CurrencyCode":string,
   "DocBudTotBurCost":number,
   "DocBudTotLbrCost":number,
   "DocBudTotMtlBurCost":number,
   "DocBudTotMtlCost":number,
   "DocBudTotODCCost":number,
   "DocGTActualCost":number,
   "DocGTBudgetCost":number,
   "DocGTCalculatedCost":number,
   "DocGTEstimatedCost":number,
   "DocGTManualCost":number,
   "DocGTQuotedCost":number,
   "DocManEstCtcBurCost":number,
   "DocManEstCtcLbrCost":number,
   "DocManEstCtcMtlBurCost":number,
   "DocManEstCtcMtlCost":number,
   "DocManEstCTCODCCost":number,
   "DocManEstCtcSubConCost":number,
   "DocProjectedTotalBurCost":number,
   "DocProjectedTotalCost":number,
   "DocProjectedTotalLbrCost":number,
   "DocProjectedTotalMtlBurCost":number,
   "DocProjectedTotalMtlCost":number,
   "DocProjectedTotalODCCost":number,
   "DocProjectedTotalSubContCost":number,
   "DocTotActSubContCost":number,
   "DocTotCtcBurCost":number,
   "DocTotCtcLbrCost":number,
   "DocTotCtcMtlBurCost":number,
   "DocTotCtcMtlCost":number,
   "DocTotCTCODCCost":number,
   "DocTotCtcSubConCost":number,
   "DocTotEstBurCost":number,
   "DocTotEstLbrCost":number,
   "DocTotEstMtlBurCost":number,
   "DocTotEstMtlCost":number,
   "DocTotEstODCCost":number,
   "DocTotEstSubContCost":number,
   "DocTotQuotBurCost":number,
   "DocTotQuotLbrCost":number,
   "DocTotQuotMtlBurCost":number,
   "DocTotQuotMtlCost":number,
   "DocTotQuotODCCost":number,
   "DocTotQuotSubContCost":number,
   "EnableApprovals":boolean,
      /**  This flag indicates whether ProjPhase.RecognizeRevenueAtChildPhaseLevel should be enabled in the UI.  */  
   "EnableRecognizeRevenueAtChildPhaseLevel":boolean,
      /**  Flag to indicate whether the PPhaseOper for this ProjPhase should allow updates based on the status of the WBSJobNum.  */  
   "EnableUpdOper":boolean,
   "EngineerWBSJob":boolean,
   "ExpenseDefTaskSetID":string,
   "ExpenseTaskSetDescription":string,
   "ExpenseWFGroupIDDescription":string,
   "GTActualCost":number,
   "GTBudgetCost":number,
   "GTCalculatedCost":number,
   "GTEstimatedCost":number,
   "GTManualCost":number,
   "GTQuotedCost":number,
   "IsRootPhase":boolean,
      /**  used to display Due date of the WBS phase job when scheduled  */  
   "JobDueDate":string,
      /**  used to display Start date of the WBS phase job when scheduled  */  
   "JobStartDate":string,
   "ParentPhaseIsRootPhase":boolean,
   "PhaseDesc":string,
   "PInvMethod":string,
   "PRevMethod":string,
   "ProjectedTotalBurCost":number,
   "ProjectedTotalCost":number,
   "ProjectedTotalLbrCost":number,
   "ProjectedTotalMtlBurCost":number,
   "ProjectedTotalMtlCost":number,
   "ProjectedTotalODCCost":number,
   "ProjectedTotalSubContCost":number,
      /**  External Field To create a WBS Phase Combo  */  
   "ProjPhaseID":string,
   "ReleaseWBSJob":boolean,
   "Rpt1BudTotBurCost":number,
   "Rpt1BudTotLbrCost":number,
   "Rpt1BudTotMtlBurCost":number,
   "Rpt1BudTotMtlCost":number,
   "Rpt1BudTotODCCost":number,
   "Rpt1BudTotSubCost":number,
   "Rpt1GTActualCost":number,
   "Rpt1GTBudgetCost":number,
   "Rpt1GTCalculatedCost":number,
   "Rpt1GTEstimatedCost":number,
   "Rpt1GTManualCost":number,
   "Rpt1GTQuotedCost":number,
   "Rpt1ManEstCtcBurCost":number,
   "Rpt1ManEstCtcLbrCost":number,
   "Rpt1ManEstCtcMtlBurCost":number,
   "Rpt1ManEstCtcMtlCost":number,
   "Rpt1ManEstCTCODCCost":number,
   "Rpt1ManEstCtcSubConCost":number,
   "Rpt1ProjectedTotalBurCost":number,
   "Rpt1ProjectedTotalCost":number,
   "Rpt1ProjectedTotalLbrCost":number,
   "Rpt1ProjectedTotalMtlBurCost":number,
   "Rpt1ProjectedTotalMtlCost":number,
   "Rpt1ProjectedTotalODCCost":number,
   "Rpt1ProjectedTotalSubContCost":number,
   "Rpt1TotActBurCost":number,
   "Rpt1TotActLbrCost":number,
   "Rpt1TotActMtlBurCost":number,
   "Rpt1TotActMtlCost":number,
   "Rpt1TotActODCCost":number,
   "Rpt1TotActSubContCost":number,
   "Rpt1TotCtcBurCost":number,
   "Rpt1TotCtcLbrCost":number,
   "Rpt1TotCtcMtlBurCost":number,
   "Rpt1TotCtcMtlCost":number,
   "Rpt1TotCTCODCCost":number,
   "Rpt1TotCtcSubConCost":number,
   "Rpt1TotEstBurCost":number,
   "Rpt1TotEstLbrCost":number,
   "Rpt1TotEstMtlBurCost":number,
   "Rpt1TotEstMtlCost":number,
   "Rpt1TotEstODCCost":number,
   "Rpt1TotEstSubContCost":number,
   "Rpt1TotQuotBurCost":number,
   "Rpt1TotQuotLbrCost":number,
   "Rpt1TotQuotMtlBurCost":number,
   "Rpt1TotQuotMtlCost":number,
   "Rpt1TotQuotODCCost":number,
   "Rpt1TotQuotSubContCost":number,
   "Rpt2BudTotBurCost":number,
   "Rpt2BudTotLbrCost":number,
   "Rpt2BudTotMtlBurCost":number,
   "Rpt2BudTotMtlCost":number,
   "Rpt2BudTotODCCost":number,
   "Rpt2BudTotSubCost":number,
   "Rpt2GTActualCost":number,
   "Rpt2GTBudgetCost":number,
   "Rpt2GTCalculatedCost":number,
   "Rpt2GTEstimatedCost":number,
   "Rpt2GTManualCost":number,
   "Rpt2GTQuotedCost":number,
   "Rpt2ManEstCtcBurCost":number,
   "Rpt2ManEstCtcLbrCost":number,
   "Rpt2ManEstCtcMtlBurCost":number,
   "Rpt2ManEstCtcMtlCost":number,
   "Rpt2ManEstCTCODCCost":number,
   "Rpt2ManEstCtcSubConCost":number,
   "Rpt2ProjectedTotalBurCost":number,
   "Rpt2ProjectedTotalCost":number,
   "Rpt2ProjectedTotalLbrCost":number,
   "Rpt2ProjectedTotalMtlBurCost":number,
   "Rpt2ProjectedTotalMtlCost":number,
   "Rpt2ProjectedTotalODCCost":number,
   "Rpt2ProjectedTotalSubContCost":number,
   "Rpt2TotActBurCost":number,
   "Rpt2TotActLbrCost":number,
   "Rpt2TotActMtlBurCost":number,
   "Rpt2TotActMtlCost":number,
   "Rpt2TotActODCCost":number,
   "Rpt2TotActSubContCost":number,
   "Rpt2TotCtcBurCost":number,
   "Rpt2TotCtcLbrCost":number,
   "Rpt2TotCtcMtlBurCost":number,
   "Rpt2TotCtcMtlCost":number,
   "Rpt2TotCTCODCCost":number,
   "Rpt2TotCtcSubConCost":number,
   "Rpt2TotEstBurCost":number,
   "Rpt2TotEstLbrCost":number,
   "Rpt2TotEstMtlBurCost":number,
   "Rpt2TotEstMtlCost":number,
   "Rpt2TotEstODCCost":number,
   "Rpt2TotEstSubContCost":number,
   "Rpt2TotQuotBurCost":number,
   "Rpt2TotQuotLbrCost":number,
   "Rpt2TotQuotMtlBurCost":number,
   "Rpt2TotQuotMtlCost":number,
   "Rpt2TotQuotODCCost":number,
   "Rpt2TotQuotSubContCost":number,
   "Rpt3BudTotBurCost":number,
   "Rpt3BudTotLbrCost":number,
   "Rpt3BudTotMtlBurCost":number,
   "Rpt3BudTotMtlCost":number,
   "Rpt3BudTotODCCost":number,
   "Rpt3BudTotSubCost":number,
   "Rpt3GTActualCost":number,
   "Rpt3GTBudgetCost":number,
   "Rpt3GTCalculatedCost":number,
   "Rpt3GTEstimatedCost":number,
   "Rpt3GTManualCost":number,
   "Rpt3GTQuotedCost":number,
   "Rpt3ManEstCtcBurCost":number,
   "Rpt3ManEstCtcLbrCost":number,
   "Rpt3ManEstCtcMtlBurCost":number,
   "Rpt3ManEstCtcMtlCost":number,
   "Rpt3ManEstCTCODCCost":number,
   "Rpt3ManEstCtcSubConCost":number,
   "Rpt3ProjectedTotalBurCost":number,
   "Rpt3ProjectedTotalCost":number,
   "Rpt3ProjectedTotalLbrCost":number,
   "Rpt3ProjectedTotalMtlBurCost":number,
   "Rpt3ProjectedTotalMtlCost":number,
   "Rpt3ProjectedTotalODCCost":number,
   "Rpt3ProjectedTotalSubContCost":number,
   "Rpt3TotActBurCost":number,
   "Rpt3TotActLbrCost":number,
   "Rpt3TotActMtlBurCost":number,
   "Rpt3TotActMtlCost":number,
   "Rpt3TotActODCCost":number,
   "Rpt3TotActSubContCost":number,
   "Rpt3TotCtcBurCost":number,
   "Rpt3TotCtcLbrCost":number,
   "Rpt3TotCtcMtlBurCost":number,
   "Rpt3TotCtcMtlCost":number,
   "Rpt3TotCTCODCCost":number,
   "Rpt3TotCtcSubConCost":number,
   "Rpt3TotEstBurCost":number,
   "Rpt3TotEstLbrCost":number,
   "Rpt3TotEstMtlBurCost":number,
   "Rpt3TotEstMtlCost":number,
   "Rpt3TotEstODCCost":number,
   "Rpt3TotEstSubContCost":number,
   "Rpt3TotQuotBurCost":number,
   "Rpt3TotQuotLbrCost":number,
   "Rpt3TotQuotMtlBurCost":number,
   "Rpt3TotQuotMtlCost":number,
   "Rpt3TotQuotODCCost":number,
   "Rpt3TotQuotSubContCost":number,
   "StatusDesc":string,
   "TimeDefTaskSetID":string,
   "TimeTaskSetDescription":string,
   "TimeWFGroupIDDescription":string,
   "WorkResDesc":string,
   "DocBudTotSubCost":number,
   "DocTotActBurCost":number,
   "DocTotActLbrCost":number,
   "DocTotActMtlBurCost":number,
   "DocTotActMtlCost":number,
   "DocTotActODCCost":number,
   "ExpenseApprovalTasksTree":string,
   "TimeApprovalTasksTree":string,
   "BitFlag":number,
   "ParentPhaseDescription":string,
   "ProjectIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "ProjectType_c":string,
   "ShipToNum_c":string,
   "ShipToSameAsProj_c":boolean,
   "Price_c":number,
   "Discount_c":number,
   "ResaleRevenue_c":number,
   "FreightRevenueAmt_c":number,
   "SalesTaxRevenue_c":number,
   "Approved_c":boolean,
   "ApprovedBy_c":string,
   "ApprovedDate_c":string,
   "PartNum_c":string,
   "PartDescription_c":string,
   "CreateRelatedPhases_c":boolean,
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
      @param phaseID
   */  
export interface DeleteByID_input{
   projectID:string,
   phaseID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ProjPhaseListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Description  */  
   Description:string,
      /**  Task start date.  */  
   StartDate:string,
      /**  Task due date.  */  
   DueDate:string,
      /**  Must be greater than or equal to 0.  */  
   PercentComplete:number,
      /**  Date this task was complete.  */  
   DateComplete:string,
      /**  Valid values are "N" = Not started, "I" = In Process, "C" = Completed.  */  
   PhaseStatus:string,
      /**  This is the duration of the WBS Phase. On the UK software this currently uses field Number09  */  
   Duration:number,
      /**  Reference to the job number created for the WBS Phase.  */  
   WBSJobNum:string,
      /**  This is the parent phase for this WBS Phase. On the UK software this currently uses field ShortChar01  */  
   ParentPhase:string,
      /**  The task ID that is returned from Microsoft Project.  */  
   MSPTaskID:string,
      /**  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back a alpha numeric string.  */  
   MSPPredecessor:string,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  Total budget burden hours for the Project phase.  */  
   BudTotBurHrs:number,
      /**  Total budget labour cost for the Project phase. This is production and setup combined.  */  
   BudTotLbrCost:number,
      /**  Total budget burden cost for the Project phase. This is production and setup combined.  */  
   BudTotBurCost:number,
      /**  Total budget material costs for the Project phase  */  
   BudTotMtlCost:number,
      /**  Total budget material burden costs for the Project phase.  */  
   BudTotMtlBurCost:number,
      /**  Manually entered estimate to complete for the labour hours for the project phase  */  
   ManEstCtcLbrHrs:number,
      /**  Manually entered estimate to complete for the burden hours.  */  
   ManEstCtcBurHrs:number,
      /**  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project phase.  */  
   ManEstCtcLbrCost:number,
      /**  Manually entered estimate to complete for the burden cost for the project phase.  */  
   ManEstCtcBurCost:number,
      /**  Manually entered estimate to complete for the Subcontract cost for the project phase.  */  
   ManEstCtcSubConCost:number,
      /**  Manually entered estimate to complete for the material cost for the project phase.  */  
   ManEstCtcMtlCost:number,
      /**  Manually entered estimate to complete for the material burden cost for the project phase.  */  
   ManEstCtcMtlBurCost:number,
      /**  Total calculated cost to complete labour cost for the Project phase. This will be both production and setup.  */  
   TotCtcLbrCost:number,
      /**  Total calculated cost to complete burden cost for the Project phase. This will be both production and setup.  */  
   TotCtcBurCost:number,
      /**  Total calculated cost to complete subcontract cost for the Project phase.  */  
   TotCtcSubConCost:number,
      /**  Total calculated cost to complete material cost for the Project phase.  */  
   TotCtcMtlCost:number,
      /**  Total calculated cost to complete material burden cost for the Project phase.  */  
   TotCtcMtlBurCost:number,
      /**  Total quoted labour hours for the Project phase  */  
   TotQuotLbrHrs:number,
      /**  Total quoted burden hours for the Project phase.  */  
   TotQuotBurHrs:number,
      /**  Total quoted labour cost for the Project phase. This will be both production and setup.  */  
   TotQuotLbrCost:number,
      /**  Total quoted burden cost for the Project phase. This will be both production and setup.  */  
   TotQuotBurCost:number,
      /**  Total quoted subcontract cost for the Project phase.  */  
   TotQuotSubContCost:number,
      /**  Total quoted material cost for the Project phase.  */  
   TotQuotMtlCost:number,
      /**  Total quoted material burden cost for the Project phase.  */  
   TotQuotMtlBurCost:number,
      /**  This holds the bom level of the phase reletive to the parent.  */  
   Level:number,
      /**  This is will either be Hours or Days  */  
   DurationType:string,
      /**  'Roll Child Manual Cost to Complete to this Level  */  
   RollChildMan:boolean,
      /**  Roll Child Budgets to this Level  */  
   RollChildBud:boolean,
      /**  Sort Sequence of the project phase.  This field controls where on the project tree the phase needs to be displayed.  */  
   SortSeq:number,
      /**  Reference to the Measured Work header.  It is used to collect the cost to determine if the Measured Work was profitable or not.  */  
   MeasuredWorkID:string,
      /**  Total quoted other direct cost for the Project phase.  */  
   TotQuotODCCost:number,
      /**  Other direct cost manual CTC  */  
   ManEstCTCODCCost:number,
      /**  Total calculated cost to complete other direct cost for the Project phase.  */  
   TotCTCODCCost:number,
      /**  Other direct cost Budget Total  */  
   BudTotODCCost:number,
      /**  Defines the Approvals Method for Time related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  */  
   TimeApprovalsMethod:string,
      /**  Unique identifier of the workflow group for Time transactions related to this WBS Phase.  */  
   TimeWFGroupID:string,
      /**  Defines the Approvals Method for Expenses related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  */  
   ExpenseApprovalsMethod:string,
      /**  Unique identifier of the workflow group for Expense transactions related to this WBS Phase.  */  
   ExpenseWFGroupID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery.  */  
   RevMethod:string,
   WorkResDesc:string,
   StatusDesc:string,
   GTActualCost:number,
   GTBudgetCost:number,
   GTCalculatedCost:number,
   GTEstimatedCost:number,
   GTManualCost:number,
   GTQuotedCost:number,
   createWBSJob:boolean,
   PhaseDesc:string,
   TimeWFGroupIDDescription:string,
   ExpenseWFGroupIDDescription:string,
   EnableApprovals:boolean,
   TimeDefTaskSetID:string,
   ExpenseDefTaskSetID:string,
   ExpenseTaskSetDescription:string,
   TimeTaskSetDescription:string,
      /**  Flag to indicate whether the PPhaseOper for this ProjPhase should allow updates based on the status of the WBSJobNum.  */  
   EnableUpdOper:boolean,
      /**  Full description of Project Management Code.  */  
   ProjectIDDescription:string,
      /**  External field to create a WBS Phase Combo.  */  
   ProjPhaseID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProjPhaseListTableset{
   ProjPhaseList:Erp_Tablesets_ProjPhaseListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ProjPhaseRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Description  */  
   Description:string,
      /**  Task start date.  */  
   StartDate:string,
      /**  Task due date.  */  
   DueDate:string,
      /**  Must be greater than or equal to 0.  */  
   PercentComplete:number,
      /**  Date this task was complete.  */  
   DateComplete:string,
      /**  Valid values are "N" = Not started, "I" = In Process, "C" = Completed.  */  
   PhaseStatus:string,
      /**  This is the duration of the WBS Phase. On the UK software this currently uses field Number09  */  
   Duration:number,
      /**  Reference to the job number created for the WBS Phase.  */  
   WBSJobNum:string,
      /**  This is the parent phase for this WBS Phase. On the UK software this currently uses field ShortChar01  */  
   ParentPhase:string,
      /**  The task ID that is returned from Microsoft Project.  */  
   MSPTaskID:string,
      /**  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back a alpha numeric string.  */  
   MSPPredecessor:string,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  Total budget labour hours for the Project phase  */  
   BudTotLbrHours:number,
      /**  Total budget burden hours for the Project phase.  */  
   BudTotBurHrs:number,
      /**  Total budget labour cost for the Project phase. This is production and setup combined.  */  
   BudTotLbrCost:number,
      /**  Total budget burden cost for the Project phase. This is production and setup combined.  */  
   BudTotBurCost:number,
      /**  Total budget subcontract costs for the Project phase  */  
   BudTotSubCost:number,
      /**  Total budget material costs for the Project phase  */  
   BudTotMtlCost:number,
      /**  Total budget material burden costs for the Project phase.  */  
   BudTotMtlBurCost:number,
      /**  Total estimated labour hours for the Project phase  */  
   TotEstLbrHrs:number,
      /**  Total estimated burden hours for the Project phase  */  
   TotEstBurdenHrs:number,
      /**  Total estimated labour cost for the Project phase. This is production and setup combined.  */  
   TotEstLbrCost:number,
      /**  Total estimated subcontract costs for the Project phase  */  
   TotEstSubContCost:number,
      /**  Total estimated material costs for the Project phase  */  
   TotEstMtlCost:number,
      /**  Total actual labour hours for the Project phase  */  
   TotActLbrHrs:number,
      /**  Total actual burden hours for the Project phase  */  
   TotActBurHrs:number,
      /**  Total actual labour cost for the Project phase. This is production and setup combined.  */  
   TotActLbrCost:number,
      /**  Total actual burden cost for the Project phase. This is production and setup combined.  */  
   TotActBurCost:number,
      /**  Total actual subcontract costs for the Project phase.  */  
   TotActSubContCost:number,
      /**  Total actual material costs for the Project phase  */  
   TotActMtlCost:number,
      /**  Total actual material burden costs for the Project phase.  */  
   TotActMtlBurCost:number,
      /**  Manually entered estimate to complete for the labour hours for the project phase  */  
   ManEstCtcLbrHrs:number,
      /**  Manually entered estimate to complete for the burden hours.  */  
   ManEstCtcBurHrs:number,
      /**  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project phase.  */  
   ManEstCtcLbrCost:number,
      /**  Manually entered estimate to complete for the burden cost for the project phase.  */  
   ManEstCtcBurCost:number,
      /**  Manually entered estimate to complete for the Subcontract cost for the project phase.  */  
   ManEstCtcSubConCost:number,
      /**  Manually entered estimate to complete for the material cost for the project phase.  */  
   ManEstCtcMtlCost:number,
      /**  Manually entered estimate to complete for the material burden cost for the project phase.  */  
   ManEstCtcMtlBurCost:number,
      /**  Total calculated cost to complete labour hours for the Project phase.  */  
   TotCtcLbrHours:number,
      /**  Total calculated cost to complete burden hours for the Project phase.  */  
   TotCtcBurHours:number,
      /**  Total calculated cost to complete labour cost for the Project phase. This will be both production and setup.  */  
   TotCtcLbrCost:number,
      /**  Total calculated cost to complete burden cost for the Project phase. This will be both production and setup.  */  
   TotCtcBurCost:number,
      /**  Total calculated cost to complete subcontract cost for the Project phase.  */  
   TotCtcSubConCost:number,
      /**  Total calculated cost to complete material cost for the Project phase.  */  
   TotCtcMtlCost:number,
      /**  Total calculated cost to complete material burden cost for the Project phase.  */  
   TotCtcMtlBurCost:number,
      /**  Total quoted labour hours for the Project phase  */  
   TotQuotLbrHrs:number,
      /**  Total quoted burden hours for the Project phase.  */  
   TotQuotBurHrs:number,
      /**  Total quoted labour cost for the Project phase. This will be both production and setup.  */  
   TotQuotLbrCost:number,
      /**  Total quoted burden cost for the Project phase. This will be both production and setup.  */  
   TotQuotBurCost:number,
      /**  Total quoted subcontract cost for the Project phase.  */  
   TotQuotSubContCost:number,
      /**  Total quoted material cost for the Project phase.  */  
   TotQuotMtlCost:number,
      /**  Total quoted material burden cost for the Project phase.  */  
   TotQuotMtlBurCost:number,
      /**  This holds the bom level of the phase reletive to the parent.  */  
   Level:number,
      /**  This is will either be Hours or Days  */  
   DurationType:string,
      /**  Total estimated burden cost for the Project phase. This is production and setup combined.  */  
   TotEstBurCost:number,
      /**  Total estimated material burden costs for the Project phase  */  
   TotEstMtlBurCost:number,
      /**  'Roll Child Manual Cost to Complete to this Level  */  
   RollChildMan:boolean,
      /**  Roll Child Budgets to this Level  */  
   RollChildBud:boolean,
      /**  Sort Sequence of the project phase.  This field controls where on the project tree the phase needs to be displayed.  */  
   SortSeq:number,
      /**  Reference to the Measured Work header.  It is used to collect the cost to determine if the Measured Work was profitable or not.  */  
   MeasuredWorkID:string,
      /**  Total quoted other direct cost for the Project phase.  */  
   TotQuotODCCost:number,
      /**  Total estimated other direct costs for the Project phase  */  
   TotEstODCCost:number,
      /**  Total actual other direct costs for the Project phase.  */  
   TotActODCCost:number,
      /**  Other direct cost manual CTC  */  
   ManEstCTCODCCost:number,
      /**  Total calculated cost to complete other direct cost for the Project phase.  */  
   TotCTCODCCost:number,
      /**  Other direct cost Budget Total  */  
   BudTotODCCost:number,
      /**  Defines the Approvals Method for Time related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  */  
   TimeApprovalsMethod:string,
      /**  Unique identifier of the workflow group for Time transactions related to this WBS Phase.  */  
   TimeWFGroupID:string,
      /**  Defines the Approvals Method for Expenses related to the WBS Phase.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override the value at the Project.  */  
   ExpenseApprovalsMethod:string,
      /**  Unique identifier of the workflow group for Expense transactions related to this WBS Phase.  */  
   ExpenseWFGroupID:string,
      /**  PartNum  */  
   PartNum:string,
      /**  RevisionNum  */  
   RevisionNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Invoicing Method  */  
   InvMethod:string,
      /**  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery.  */  
   RevMethod:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales Order Line  */  
   OrderLine:number,
      /**  If any activity of the job assigned to the Phase has been recognized or invoiced  */  
   WasRecInvoiced:boolean,
      /**  Date of last Build WBS Phase Analysis run.  */  
   LastBuildWBSPhaseAnalysisDate:string,
      /**  Percentage of Completion  */  
   PercentageOfCompletion:number,
      /**  Labor Cost To Be Recognized  */  
   ToBeRecognizedLbrCost:number,
      /**  Burden Cost To Be Recognized  */  
   ToBeRecognizedBurCost:number,
      /**  Material Cost To Be Recognized  */  
   ToBeRecognizedMtlCost:number,
      /**  Subcontract Cost To Be Recognized  */  
   ToBeRecognizedSubCost:number,
      /**  Material Burden Cost To Be Recognized  */  
   ToBeRecognizedMtlBurCost:number,
      /**  ODC Cost To Be Recognized  */  
   ToBeRecognizedODCCost:number,
      /**  Revenue To Be Recognized  */  
   ToBeRecognizedRevenue:number,
      /**  When true,  Recognize Revenue separately at Child WBS Phases.  When false, Recognize Revenue for this phase and all child phases at this level.  */  
   RecognizeRevenueAtChildPhaseLevel:boolean,
      /**  To control if the project phase budget values are to be rolled up to the project phase.  */  
   RollBudgetsToWBSPhase:boolean,
      /**  TotWBSPhaseRev  */  
   TotWBSPhaseRev:number,
      /**  The sales category code used in the Revenue recognition process.  */  
   SalesCatID:string,
      /**  ActMtlNonJobCost  */  
   ActMtlNonJobCost:number,
      /**  AsOfDate  */  
   AsOfDate:string,
      /**  Number of Recalculation of burden amounts posted to GL by Revenue Recognition process  */  
   BdnRecSeqPosted:number,
      /**  Number of Recalculation of burden amounts created by Revenue Recognition process  */  
   BdnRecSeqLastAdded:number,
      /**  Sum of all Actual Burden Charges posted by today  */  
   BdnRevenueAutoToday:number,
      /**  BillingToDate  */  
   BillingToDate:number,
      /**  BuildAnalysis  */  
   BuildAnalysis:boolean,
      /**  The burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActBurdenCost  */  
   BurdenCostOfSales:number,
      /**  BurdenLbrCstToDate  */  
   BurdenLbrCstToDate:number,
      /**  The burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   BurdenRecAutoCstTodate:number,
      /**  The burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process  */  
   BurdenRecManCstTodate:number,
      /**  BurManPosted  */  
   BurManPosted:number,
      /**  BurPur  */  
   BurPur:number,
      /**  Estimated burden cost.  */  
   EstBurdenCost:number,
      /**  Estimated burden hours.  */  
   EstBurdenHours:number,
      /**  Estimated labor cost.  */  
   EstLaborCost:number,
      /**  Estimated labor hours.  */  
   EstLaborHours:number,
      /**  Estimated material burden cost.  */  
   EstMtlBurdenCost:number,
      /**  Estimated material cost.  */  
   EstMtlCost:number,
      /**  Estimated other direct cost.  */  
   EstODCCost:number,
      /**  Estimated subcontract cost.  */  
   EstSubcontractCost:number,
      /**  The labour costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActLaborCost.  */  
   LaborCostOfSales:number,
      /**  LaborLbrCstToDate  */  
   LaborLbrCstToDate:number,
      /**  The labour costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   LaborRecAutoCstTodate:number,
      /**  The labor costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   LaborRecManCstTodate:number,
      /**  LbrManPosted  */  
   LbrManPosted:number,
      /**  LbrPur  */  
   LbrPur:number,
      /**  The material costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of Material with a linesource of COS with value from ProjectAnalysis.ActMatCost.  */  
   MaterialCostOfSales:number,
      /**  The material costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  */  
   MaterialRecAutoCstTodate:number,
      /**  The material costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   MaterialRecManCstTodate:number,
      /**  The material burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActMatBurdenCost  */  
   MtlBurdenCostOfSales:number,
      /**  The material burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  */  
   MtlBurdenRecAutoCstTodate:number,
      /**  The material burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  */  
   MtlBurdenRecManCstTodate:number,
      /**  MtlBurManPosted  */  
   MtlBurManPosted:number,
      /**  MtlBurPur  */  
   MtlBurPur:number,
      /**  MtlManPosted  */  
   MtlManPosted:number,
      /**  MtlPur  */  
   MtlPur:number,
      /**  NextTmpInvcNum  */  
   NextTmpInvcNum:number,
      /**  ODCManPosted  */  
   ODCManPosted:number,
      /**  ODCPur  */  
   ODCPur:number,
      /**  Other Direct cost Recognition to Date  */  
   ODCRecAutoCstToDate:number,
      /**  Other Direct Cost Manual Recognition to Date  */  
   ODCRecManCstTodate:number,
      /**  RecManPosted  */  
   RecManPosted:number,
      /**  RecogToDtBilling  */  
   RecogToDtBilling:number,
      /**  RecogToDtLbk  */  
   RecogToDtLbk:number,
      /**  RecogToDtManual  */  
   RecogToDtManual:number,
      /**  RetentionDt  */  
   RetentionDt:number,
      /**  The revenue that has been recognised to date for the project. This is revenue that has been invoiced against the sales order either as an advanced billing or a shipment. This is the sum of ProjectAnalysis records with a Linecode of Revenue with a linesource of Invoice with value from ProjectAnalysis.ActMatCost.  */  
   RevenueRecAutoToDate:number,
      /**  The revenue that has been recognised to date for the project. This is revenue that has been manually recognised using this process.  */  
   RevenueRecManToDate:number,
      /**  Reverse  */  
   Reverse:string,
      /**  RollManEstToCpte  */  
   RollManEstToCpte:boolean,
      /**  SubCManPosted  */  
   SubCManPosted:number,
      /**  SubConCostOfSales  */  
   SubConCostOfSales:number,
      /**  SubConRecAutoCstTodate  */  
   SubConRecAutoCstTodate:number,
      /**  SubConRecManCstTodate  */  
   SubConRecManCstTodate:number,
      /**  SubPur  */  
   SubPur:number,
      /**  Total contract value for the WBS Phase.  */  
   ConTotValue:number,
      /**  Total contract value for the WBS Phase in the Document currency.  */  
   DocConTotValue:number,
      /**  Total contract value for the WBS Phase in the Reporting currency.  */  
   Rpt1ConTotValue:number,
      /**  Total contract value for the WBS Phase in the Reporting currency.  */  
   Rpt2ConTotValue:number,
      /**  Total contract value for the WBS Phase in the Reporting currency.  */  
   Rpt3ConTotValue:number,
      /**  Net total contract value for the WBS Phase.  */  
   ConTotValueNet:number,
      /**  Net total contract value for the WBS Phase in the Document currency.  */  
   DocConTotValueNet:number,
      /**  Net total contract value for the WBS Phase in the Reporting currency.  */  
   Rpt1ConTotValueNet:number,
      /**  Net total contract value for the WBS Phase in the Reporting currency.  */  
   Rpt2ConTotValueNet:number,
      /**  Net total contract value for the WBS Phase in the Reporting currency.  */  
   Rpt3ConTotValueNet:number,
   CloseWBSJob:boolean,
   CurrencyCode:string,
   DocBudTotBurCost:number,
   DocBudTotLbrCost:number,
   DocBudTotMtlBurCost:number,
   DocBudTotMtlCost:number,
   DocBudTotODCCost:number,
   DocGTActualCost:number,
   DocGTBudgetCost:number,
   DocGTCalculatedCost:number,
   DocGTEstimatedCost:number,
   DocGTManualCost:number,
   DocGTQuotedCost:number,
   DocManEstCtcBurCost:number,
   DocManEstCtcLbrCost:number,
   DocManEstCtcMtlBurCost:number,
   DocManEstCtcMtlCost:number,
   DocManEstCTCODCCost:number,
   DocManEstCtcSubConCost:number,
   DocProjectedTotalBurCost:number,
   DocProjectedTotalCost:number,
   DocProjectedTotalLbrCost:number,
   DocProjectedTotalMtlBurCost:number,
   DocProjectedTotalMtlCost:number,
   DocProjectedTotalODCCost:number,
   DocProjectedTotalSubContCost:number,
   DocTotActSubContCost:number,
   DocTotCtcBurCost:number,
   DocTotCtcLbrCost:number,
   DocTotCtcMtlBurCost:number,
   DocTotCtcMtlCost:number,
   DocTotCTCODCCost:number,
   DocTotCtcSubConCost:number,
   DocTotEstBurCost:number,
   DocTotEstLbrCost:number,
   DocTotEstMtlBurCost:number,
   DocTotEstMtlCost:number,
   DocTotEstODCCost:number,
   DocTotEstSubContCost:number,
   DocTotQuotBurCost:number,
   DocTotQuotLbrCost:number,
   DocTotQuotMtlBurCost:number,
   DocTotQuotMtlCost:number,
   DocTotQuotODCCost:number,
   DocTotQuotSubContCost:number,
   EnableApprovals:boolean,
      /**  This flag indicates whether ProjPhase.RecognizeRevenueAtChildPhaseLevel should be enabled in the UI.  */  
   EnableRecognizeRevenueAtChildPhaseLevel:boolean,
      /**  Flag to indicate whether the PPhaseOper for this ProjPhase should allow updates based on the status of the WBSJobNum.  */  
   EnableUpdOper:boolean,
   EngineerWBSJob:boolean,
   ExpenseDefTaskSetID:string,
   ExpenseTaskSetDescription:string,
   ExpenseWFGroupIDDescription:string,
   GTActualCost:number,
   GTBudgetCost:number,
   GTCalculatedCost:number,
   GTEstimatedCost:number,
   GTManualCost:number,
   GTQuotedCost:number,
   IsRootPhase:boolean,
      /**  used to display Due date of the WBS phase job when scheduled  */  
   JobDueDate:string,
      /**  used to display Start date of the WBS phase job when scheduled  */  
   JobStartDate:string,
   ParentPhaseIsRootPhase:boolean,
   PhaseDesc:string,
   PInvMethod:string,
   PRevMethod:string,
   ProjectedTotalBurCost:number,
   ProjectedTotalCost:number,
   ProjectedTotalLbrCost:number,
   ProjectedTotalMtlBurCost:number,
   ProjectedTotalMtlCost:number,
   ProjectedTotalODCCost:number,
   ProjectedTotalSubContCost:number,
      /**  External Field To create a WBS Phase Combo  */  
   ProjPhaseID:string,
   ReleaseWBSJob:boolean,
   Rpt1BudTotBurCost:number,
   Rpt1BudTotLbrCost:number,
   Rpt1BudTotMtlBurCost:number,
   Rpt1BudTotMtlCost:number,
   Rpt1BudTotODCCost:number,
   Rpt1BudTotSubCost:number,
   Rpt1GTActualCost:number,
   Rpt1GTBudgetCost:number,
   Rpt1GTCalculatedCost:number,
   Rpt1GTEstimatedCost:number,
   Rpt1GTManualCost:number,
   Rpt1GTQuotedCost:number,
   Rpt1ManEstCtcBurCost:number,
   Rpt1ManEstCtcLbrCost:number,
   Rpt1ManEstCtcMtlBurCost:number,
   Rpt1ManEstCtcMtlCost:number,
   Rpt1ManEstCTCODCCost:number,
   Rpt1ManEstCtcSubConCost:number,
   Rpt1ProjectedTotalBurCost:number,
   Rpt1ProjectedTotalCost:number,
   Rpt1ProjectedTotalLbrCost:number,
   Rpt1ProjectedTotalMtlBurCost:number,
   Rpt1ProjectedTotalMtlCost:number,
   Rpt1ProjectedTotalODCCost:number,
   Rpt1ProjectedTotalSubContCost:number,
   Rpt1TotActBurCost:number,
   Rpt1TotActLbrCost:number,
   Rpt1TotActMtlBurCost:number,
   Rpt1TotActMtlCost:number,
   Rpt1TotActODCCost:number,
   Rpt1TotActSubContCost:number,
   Rpt1TotCtcBurCost:number,
   Rpt1TotCtcLbrCost:number,
   Rpt1TotCtcMtlBurCost:number,
   Rpt1TotCtcMtlCost:number,
   Rpt1TotCTCODCCost:number,
   Rpt1TotCtcSubConCost:number,
   Rpt1TotEstBurCost:number,
   Rpt1TotEstLbrCost:number,
   Rpt1TotEstMtlBurCost:number,
   Rpt1TotEstMtlCost:number,
   Rpt1TotEstODCCost:number,
   Rpt1TotEstSubContCost:number,
   Rpt1TotQuotBurCost:number,
   Rpt1TotQuotLbrCost:number,
   Rpt1TotQuotMtlBurCost:number,
   Rpt1TotQuotMtlCost:number,
   Rpt1TotQuotODCCost:number,
   Rpt1TotQuotSubContCost:number,
   Rpt2BudTotBurCost:number,
   Rpt2BudTotLbrCost:number,
   Rpt2BudTotMtlBurCost:number,
   Rpt2BudTotMtlCost:number,
   Rpt2BudTotODCCost:number,
   Rpt2BudTotSubCost:number,
   Rpt2GTActualCost:number,
   Rpt2GTBudgetCost:number,
   Rpt2GTCalculatedCost:number,
   Rpt2GTEstimatedCost:number,
   Rpt2GTManualCost:number,
   Rpt2GTQuotedCost:number,
   Rpt2ManEstCtcBurCost:number,
   Rpt2ManEstCtcLbrCost:number,
   Rpt2ManEstCtcMtlBurCost:number,
   Rpt2ManEstCtcMtlCost:number,
   Rpt2ManEstCTCODCCost:number,
   Rpt2ManEstCtcSubConCost:number,
   Rpt2ProjectedTotalBurCost:number,
   Rpt2ProjectedTotalCost:number,
   Rpt2ProjectedTotalLbrCost:number,
   Rpt2ProjectedTotalMtlBurCost:number,
   Rpt2ProjectedTotalMtlCost:number,
   Rpt2ProjectedTotalODCCost:number,
   Rpt2ProjectedTotalSubContCost:number,
   Rpt2TotActBurCost:number,
   Rpt2TotActLbrCost:number,
   Rpt2TotActMtlBurCost:number,
   Rpt2TotActMtlCost:number,
   Rpt2TotActODCCost:number,
   Rpt2TotActSubContCost:number,
   Rpt2TotCtcBurCost:number,
   Rpt2TotCtcLbrCost:number,
   Rpt2TotCtcMtlBurCost:number,
   Rpt2TotCtcMtlCost:number,
   Rpt2TotCTCODCCost:number,
   Rpt2TotCtcSubConCost:number,
   Rpt2TotEstBurCost:number,
   Rpt2TotEstLbrCost:number,
   Rpt2TotEstMtlBurCost:number,
   Rpt2TotEstMtlCost:number,
   Rpt2TotEstODCCost:number,
   Rpt2TotEstSubContCost:number,
   Rpt2TotQuotBurCost:number,
   Rpt2TotQuotLbrCost:number,
   Rpt2TotQuotMtlBurCost:number,
   Rpt2TotQuotMtlCost:number,
   Rpt2TotQuotODCCost:number,
   Rpt2TotQuotSubContCost:number,
   Rpt3BudTotBurCost:number,
   Rpt3BudTotLbrCost:number,
   Rpt3BudTotMtlBurCost:number,
   Rpt3BudTotMtlCost:number,
   Rpt3BudTotODCCost:number,
   Rpt3BudTotSubCost:number,
   Rpt3GTActualCost:number,
   Rpt3GTBudgetCost:number,
   Rpt3GTCalculatedCost:number,
   Rpt3GTEstimatedCost:number,
   Rpt3GTManualCost:number,
   Rpt3GTQuotedCost:number,
   Rpt3ManEstCtcBurCost:number,
   Rpt3ManEstCtcLbrCost:number,
   Rpt3ManEstCtcMtlBurCost:number,
   Rpt3ManEstCtcMtlCost:number,
   Rpt3ManEstCTCODCCost:number,
   Rpt3ManEstCtcSubConCost:number,
   Rpt3ProjectedTotalBurCost:number,
   Rpt3ProjectedTotalCost:number,
   Rpt3ProjectedTotalLbrCost:number,
   Rpt3ProjectedTotalMtlBurCost:number,
   Rpt3ProjectedTotalMtlCost:number,
   Rpt3ProjectedTotalODCCost:number,
   Rpt3ProjectedTotalSubContCost:number,
   Rpt3TotActBurCost:number,
   Rpt3TotActLbrCost:number,
   Rpt3TotActMtlBurCost:number,
   Rpt3TotActMtlCost:number,
   Rpt3TotActODCCost:number,
   Rpt3TotActSubContCost:number,
   Rpt3TotCtcBurCost:number,
   Rpt3TotCtcLbrCost:number,
   Rpt3TotCtcMtlBurCost:number,
   Rpt3TotCtcMtlCost:number,
   Rpt3TotCTCODCCost:number,
   Rpt3TotCtcSubConCost:number,
   Rpt3TotEstBurCost:number,
   Rpt3TotEstLbrCost:number,
   Rpt3TotEstMtlBurCost:number,
   Rpt3TotEstMtlCost:number,
   Rpt3TotEstODCCost:number,
   Rpt3TotEstSubContCost:number,
   Rpt3TotQuotBurCost:number,
   Rpt3TotQuotLbrCost:number,
   Rpt3TotQuotMtlBurCost:number,
   Rpt3TotQuotMtlCost:number,
   Rpt3TotQuotODCCost:number,
   Rpt3TotQuotSubContCost:number,
   StatusDesc:string,
   TimeDefTaskSetID:string,
   TimeTaskSetDescription:string,
   TimeWFGroupIDDescription:string,
   WorkResDesc:string,
   DocBudTotSubCost:number,
   DocTotActBurCost:number,
   DocTotActLbrCost:number,
   DocTotActMtlBurCost:number,
   DocTotActMtlCost:number,
   DocTotActODCCost:number,
   ExpenseApprovalTasksTree:string,
   TimeApprovalTasksTree:string,
   BitFlag:number,
   ParentPhaseDescription:string,
   ProjectIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   ProjectType_c:string,
   ShipToNum_c:string,
   ShipToSameAsProj_c:boolean,
   Price_c:number,
   Discount_c:number,
   ResaleRevenue_c:number,
   FreightRevenueAmt_c:number,
   SalesTaxRevenue_c:number,
   Approved_c:boolean,
   ApprovedBy_c:string,
   ApprovedDate_c:string,
   PartNum_c:string,
   PartDescription_c:string,
   CreateRelatedPhases_c:boolean,
}

export interface Erp_Tablesets_ProjPhaseSearchTableset{
   ProjPhase:Erp_Tablesets_ProjPhaseRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtProjPhaseSearchTableset{
   ProjPhase:Erp_Tablesets_ProjPhaseRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param projectID
      @param phaseID
   */  
export interface GetByID_input{
   projectID:string,
   phaseID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ProjPhaseSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ProjPhaseSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ProjPhaseSearchTableset[],
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
   returnObj:Erp_Tablesets_ProjPhaseListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param projectID
   */  
export interface GetNewProjPhase_input{
   ds:Erp_Tablesets_ProjPhaseSearchTableset[],
   projectID:string,
}

export interface GetNewProjPhase_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProjPhaseSearchTableset,
}
}

   /** Required : 
      @param whereClauseProjPhase
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseProjPhase:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ProjPhaseSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtProjPhaseSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtProjPhaseSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ProjPhaseSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProjPhaseSearchTableset,
}
}

