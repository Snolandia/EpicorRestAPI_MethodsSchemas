import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GlbPerConSearchSvc
// Description: GlbPerCon search object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/$metadata", {
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
   Description: Get GlbPerConSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbPerConSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbPerConRow
   */  
export function get_GlbPerConSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPerConRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GlbPerConSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPerConRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbPerConSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbPerConRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GlbPerConRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbPerConSearches(requestBody:Erp_Tablesets_GlbPerConRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GlbPerConSearches", {
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
   Summary: Calls GetByID to retrieve the GlbPerConSearch item
   Description: Calls GetByID to retrieve the GlbPerConSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbPerConSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbPerConID Desc: GlbPerConID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GlbPerConRow
   */  
export function get_GlbPerConSearches_Company_GlbCompany_GlbPerConID(Company:string, GlbCompany:string, GlbPerConID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbPerConRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GlbPerConSearches(" + Company + "," + GlbCompany + "," + GlbPerConID + ")", {
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
         resolve(data as Erp_Tablesets_GlbPerConRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlbPerConSearch for the service
   Description: Calls UpdateExt to update GlbPerConSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbPerConSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbPerConID Desc: GlbPerConID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbPerConRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlbPerConSearches_Company_GlbCompany_GlbPerConID(Company:string, GlbCompany:string, GlbPerConID:string, requestBody:Erp_Tablesets_GlbPerConRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GlbPerConSearches(" + Company + "," + GlbCompany + "," + GlbPerConID + ")", {
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
   Summary: Call UpdateExt to delete GlbPerConSearch item
   Description: Call UpdateExt to delete GlbPerConSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbPerConSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbPerConID Desc: GlbPerConID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlbPerConSearches_Company_GlbCompany_GlbPerConID(Company:string, GlbCompany:string, GlbPerConID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GlbPerConSearches(" + Company + "," + GlbCompany + "," + GlbPerConID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbPerConListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPerConListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPerConListRow)
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
export function get_GetRows(whereClauseGlbPerCon:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGlbPerCon!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlbPerCon=" + whereClauseGlbPerCon
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GetRows" + params, {
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
export function get_GetByID(glbCompany:string, glbPerConID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof glbCompany!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glbCompany=" + glbCompany
   }
   if(typeof glbPerConID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glbPerConID=" + glbPerConID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewGlbPerCon
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbPerCon
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGlbPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlbPerCon(requestBody:GetNewGlbPerCon_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGlbPerCon_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GetNewGlbPerCon", {
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
         resolve(data as GetNewGlbPerCon_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPerConListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbPerConListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPerConRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbPerConRow,
}

export interface Erp_Tablesets_GlbPerConListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Full name of the contact.  */  
   "Name":string,
      /**  Contact's first name.  */  
   "FirstName":string,
      /**  Contact's middle name.  */  
   "MiddleName":string,
      /**  Contact's last name.  */  
   "LastName":string,
      /**  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  */  
   "PRName":string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   "Func":string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   "FaxNum":string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   "PhoneNum":string,
      /**  The contact's email address.  */  
   "EMailAddress":string,
      /**  The contact's cell phone number.  */  
   "CellPhoneNum":string,
      /**  The contact's pager number.  */  
   "PagerNum":string,
      /**  The contact's home number.  */  
   "HomeNum":string,
      /**  The contact's alternate phone number.  */  
   "AltNum":string,
      /**  Contact's prefix.  */  
   "Prefix":string,
      /**  Contact's suffix.  */  
   "Suffix":string,
      /**  Contact's initials.  */  
   "Initials":string,
      /**  Contact's website.  */  
   "WebSite":string,
      /**  Contact's IM.  */  
   "IM":string,
      /**  Contact's Twitter.  */  
   "Twitter":string,
      /**  Contact's LinkedIn.  */  
   "LinkedIn":string,
      /**  Contact's FaceBook.  */  
   "FaceBook":string,
      /**  User defined Link 1.  */  
   "WebLink1":string,
      /**  User defined Link 2.  */  
   "WebLink2":string,
      /**  User defined Link 3.  */  
   "WebLink3":string,
      /**  User defined Link 4.  */  
   "WebLink4":string,
      /**  User defined Link 5.  */  
   "WebLink5":string,
      /**  Address line 1  */  
   "Address1":string,
      /**  Address line 2  */  
   "Address2":string,
      /**  Address line 3  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  State/Province  */  
   "State":string,
      /**  Zip/Postal Code  */  
   "Zip":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   "CountryNum":number,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   "CorpName":string,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   "RoleCode":string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   "Comment":string,
      /**  Contact's title.  */  
   "ContactTitle":string,
      /**  The name of the person this contact reports to.  */  
   "ReportsTo":string,
      /**  Contact's payroll last name.  */  
   "PRLastName":string,
      /**  Contact's payroll first name.  */  
   "PRFirstName":string,
      /**  Contact's payroll middle name.  */  
   "PRMiddleName":string,
      /**  The System User ID.  */  
   "DcdUserID":string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   "PhotoFile":string,
      /**  Owner Company Identifier.  */  
   "GlbCompany":string,
      /**  The Owner's PerConID field identifies the PerCon and is used as the primary key.  */  
   "GlbPerConID":number,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   "OldCompany":string,
      /**  The Original Owner's PerConID field identifies the PerCon and is used as the primary key.   NOT CURRENTLY IN USE  */  
   "OldPerConID":number,
      /**  Indicates if the user chose to skip this record when linking global PerCon's.  The user can come back at a later time and choose to link a skipped PerCon if they need to.  */  
   "Skipped":boolean,
      /**  Marks the PerCon as a global PerCon, available to be sent out to other companies.  */  
   "GlobalPerCon":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Full name of the contact. A descriptive Name assigned by the parent company user to uniquely identify the PerCon record.  */  
   "GlbName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the PerCon is Global (master or linked)  */  
   "GlbFlag":boolean,
   "LinkPerConID":number,
   "LinkName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbPerConRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Full name of the contact.  */  
   "Name":string,
      /**  Contact's first name.  */  
   "FirstName":string,
      /**  Contact's middle name.  */  
   "MiddleName":string,
      /**  Contact's last name.  */  
   "LastName":string,
      /**  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  */  
   "PRName":string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   "Func":string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   "FaxNum":string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   "PhoneNum":string,
      /**  The contact's email address.  */  
   "EMailAddress":string,
      /**  The contact's cell phone number.  */  
   "CellPhoneNum":string,
      /**  The contact's pager number.  */  
   "PagerNum":string,
      /**  The contact's home number.  */  
   "HomeNum":string,
      /**  The contact's alternate phone number.  */  
   "AltNum":string,
      /**  Contact's prefix.  */  
   "Prefix":string,
      /**  Contact's suffix.  */  
   "Suffix":string,
      /**  Contact's initials.  */  
   "Initials":string,
      /**  Contact's website.  */  
   "WebSite":string,
      /**  Contact's IM.  */  
   "IM":string,
      /**  Contact's Twitter.  */  
   "Twitter":string,
      /**  Contact's LinkedIn.  */  
   "LinkedIn":string,
      /**  Contact's FaceBook.  */  
   "FaceBook":string,
      /**  User defined Link 1.  */  
   "WebLink1":string,
      /**  User defined Link 2.  */  
   "WebLink2":string,
      /**  User defined Link 3.  */  
   "WebLink3":string,
      /**  User defined Link 4.  */  
   "WebLink4":string,
      /**  User defined Link 5.  */  
   "WebLink5":string,
      /**  Address line 1  */  
   "Address1":string,
      /**  Address line 2  */  
   "Address2":string,
      /**  Address line 3  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  State/Province  */  
   "State":string,
      /**  Zip/Postal Code  */  
   "Zip":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   "CountryNum":number,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   "CorpName":string,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   "RoleCode":string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   "Comment":string,
      /**  Contact's title.  */  
   "ContactTitle":string,
      /**  The name of the person this contact reports to.  */  
   "ReportsTo":string,
      /**  Contact's payroll last name.  */  
   "PRLastName":string,
      /**  Contact's payroll first name.  */  
   "PRFirstName":string,
      /**  Contact's payroll middle name.  */  
   "PRMiddleName":string,
      /**  The System User ID.  */  
   "DcdUserID":string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   "PhotoFile":string,
      /**  Owner Company Identifier.  */  
   "GlbCompany":string,
      /**  The Owner's PerConID field identifies the PerCon and is used as the primary key.  */  
   "GlbPerConID":number,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   "OldCompany":string,
      /**  The Original Owner's PerConID field identifies the PerCon and is used as the primary key.   NOT CURRENTLY IN USE  */  
   "OldPerConID":number,
      /**  Indicates if the user chose to skip this record when linking global PerCon's.  The user can come back at a later time and choose to link a skipped PerCon if they need to.  */  
   "Skipped":boolean,
      /**  Marks the PerCon as a global PerCon, available to be sent out to other companies.  */  
   "GlobalPerCon":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Full name of the contact. A descriptive Name assigned by the parent company user to uniquely identify the PerCon record.  */  
   "GlbName":string,
   "HCMLinked":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ImageID  */  
   "ImageID":string,
      /**  Indicates if the PerCon is Global (master or linked)  */  
   "GlbFlag":boolean,
   "LinkName":string,
   "LinkPerConID":number,
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
      @param glbCompany
      @param glbPerConID
   */  
export interface DeleteByID_input{
   glbCompany:string,
   glbPerConID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GlbPerConListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Full name of the contact.  */  
   Name:string,
      /**  Contact's first name.  */  
   FirstName:string,
      /**  Contact's middle name.  */  
   MiddleName:string,
      /**  Contact's last name.  */  
   LastName:string,
      /**  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  */  
   PRName:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   FaxNum:string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  The contact's email address.  */  
   EMailAddress:string,
      /**  The contact's cell phone number.  */  
   CellPhoneNum:string,
      /**  The contact's pager number.  */  
   PagerNum:string,
      /**  The contact's home number.  */  
   HomeNum:string,
      /**  The contact's alternate phone number.  */  
   AltNum:string,
      /**  Contact's prefix.  */  
   Prefix:string,
      /**  Contact's suffix.  */  
   Suffix:string,
      /**  Contact's initials.  */  
   Initials:string,
      /**  Contact's website.  */  
   WebSite:string,
      /**  Contact's IM.  */  
   IM:string,
      /**  Contact's Twitter.  */  
   Twitter:string,
      /**  Contact's LinkedIn.  */  
   LinkedIn:string,
      /**  Contact's FaceBook.  */  
   FaceBook:string,
      /**  User defined Link 1.  */  
   WebLink1:string,
      /**  User defined Link 2.  */  
   WebLink2:string,
      /**  User defined Link 3.  */  
   WebLink3:string,
      /**  User defined Link 4.  */  
   WebLink4:string,
      /**  User defined Link 5.  */  
   WebLink5:string,
      /**  Address line 1  */  
   Address1:string,
      /**  Address line 2  */  
   Address2:string,
      /**  Address line 3  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   CountryNum:number,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   CorpName:string,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   RoleCode:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Contact's title.  */  
   ContactTitle:string,
      /**  The name of the person this contact reports to.  */  
   ReportsTo:string,
      /**  Contact's payroll last name.  */  
   PRLastName:string,
      /**  Contact's payroll first name.  */  
   PRFirstName:string,
      /**  Contact's payroll middle name.  */  
   PRMiddleName:string,
      /**  The System User ID.  */  
   DcdUserID:string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   PhotoFile:string,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  The Owner's PerConID field identifies the PerCon and is used as the primary key.  */  
   GlbPerConID:number,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  The Original Owner's PerConID field identifies the PerCon and is used as the primary key.   NOT CURRENTLY IN USE  */  
   OldPerConID:number,
      /**  Indicates if the user chose to skip this record when linking global PerCon's.  The user can come back at a later time and choose to link a skipped PerCon if they need to.  */  
   Skipped:boolean,
      /**  Marks the PerCon as a global PerCon, available to be sent out to other companies.  */  
   GlobalPerCon:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Full name of the contact. A descriptive Name assigned by the parent company user to uniquely identify the PerCon record.  */  
   GlbName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the PerCon is Global (master or linked)  */  
   GlbFlag:boolean,
   LinkPerConID:number,
   LinkName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbPerConListTableset{
   GlbPerConList:Erp_Tablesets_GlbPerConListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlbPerConRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Full name of the contact.  */  
   Name:string,
      /**  Contact's first name.  */  
   FirstName:string,
      /**  Contact's middle name.  */  
   MiddleName:string,
      /**  Contact's last name.  */  
   LastName:string,
      /**  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  */  
   PRName:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   FaxNum:string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  The contact's email address.  */  
   EMailAddress:string,
      /**  The contact's cell phone number.  */  
   CellPhoneNum:string,
      /**  The contact's pager number.  */  
   PagerNum:string,
      /**  The contact's home number.  */  
   HomeNum:string,
      /**  The contact's alternate phone number.  */  
   AltNum:string,
      /**  Contact's prefix.  */  
   Prefix:string,
      /**  Contact's suffix.  */  
   Suffix:string,
      /**  Contact's initials.  */  
   Initials:string,
      /**  Contact's website.  */  
   WebSite:string,
      /**  Contact's IM.  */  
   IM:string,
      /**  Contact's Twitter.  */  
   Twitter:string,
      /**  Contact's LinkedIn.  */  
   LinkedIn:string,
      /**  Contact's FaceBook.  */  
   FaceBook:string,
      /**  User defined Link 1.  */  
   WebLink1:string,
      /**  User defined Link 2.  */  
   WebLink2:string,
      /**  User defined Link 3.  */  
   WebLink3:string,
      /**  User defined Link 4.  */  
   WebLink4:string,
      /**  User defined Link 5.  */  
   WebLink5:string,
      /**  Address line 1  */  
   Address1:string,
      /**  Address line 2  */  
   Address2:string,
      /**  Address line 3  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   CountryNum:number,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   CorpName:string,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   RoleCode:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Contact's title.  */  
   ContactTitle:string,
      /**  The name of the person this contact reports to.  */  
   ReportsTo:string,
      /**  Contact's payroll last name.  */  
   PRLastName:string,
      /**  Contact's payroll first name.  */  
   PRFirstName:string,
      /**  Contact's payroll middle name.  */  
   PRMiddleName:string,
      /**  The System User ID.  */  
   DcdUserID:string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   PhotoFile:string,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  The Owner's PerConID field identifies the PerCon and is used as the primary key.  */  
   GlbPerConID:number,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  The Original Owner's PerConID field identifies the PerCon and is used as the primary key.   NOT CURRENTLY IN USE  */  
   OldPerConID:number,
      /**  Indicates if the user chose to skip this record when linking global PerCon's.  The user can come back at a later time and choose to link a skipped PerCon if they need to.  */  
   Skipped:boolean,
      /**  Marks the PerCon as a global PerCon, available to be sent out to other companies.  */  
   GlobalPerCon:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Full name of the contact. A descriptive Name assigned by the parent company user to uniquely identify the PerCon record.  */  
   GlbName:string,
   HCMLinked:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ImageID  */  
   ImageID:string,
      /**  Indicates if the PerCon is Global (master or linked)  */  
   GlbFlag:boolean,
   LinkName:string,
   LinkPerConID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbPerConSearchTableset{
   GlbPerCon:Erp_Tablesets_GlbPerConRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGlbPerConSearchTableset{
   GlbPerCon:Erp_Tablesets_GlbPerConRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param glbCompany
      @param glbPerConID
   */  
export interface GetByID_input{
   glbCompany:string,
   glbPerConID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GlbPerConSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GlbPerConSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GlbPerConSearchTableset[],
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
   returnObj:Erp_Tablesets_GlbPerConListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param glbCompany
   */  
export interface GetNewGlbPerCon_input{
   ds:Erp_Tablesets_GlbPerConSearchTableset[],
   glbCompany:string,
}

export interface GetNewGlbPerCon_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbPerConSearchTableset,
}
}

   /** Required : 
      @param whereClauseGlbPerCon
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGlbPerCon:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GlbPerConSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtGlbPerConSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGlbPerConSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GlbPerConSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbPerConSearchTableset,
}
}

