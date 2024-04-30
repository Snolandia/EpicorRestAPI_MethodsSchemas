import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PayMethodSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/$metadata", {
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
   Description: Get PayMethodSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PayMethodSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodRow
   */  
export function get_PayMethodSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/PayMethodSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PayMethodSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PayMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PayMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PayMethodSearches(requestBody:Erp_Tablesets_PayMethodRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/PayMethodSearches", {
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
   Summary: Calls GetByID to retrieve the PayMethodSearch item
   Description: Calls GetByID to retrieve the PayMethodSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayMethodSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PayMethodRow
   */  
export function get_PayMethodSearches_Company_PMUID(Company:string, PMUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PayMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/PayMethodSearches(" + Company + "," + PMUID + ")", {
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
         resolve(data as Erp_Tablesets_PayMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PayMethodSearch for the service
   Description: Calls UpdateExt to update PayMethodSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PayMethodSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PayMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PayMethodSearches_Company_PMUID(Company:string, PMUID:string, requestBody:Erp_Tablesets_PayMethodRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/PayMethodSearches(" + Company + "," + PMUID + ")", {
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
   Summary: Call UpdateExt to delete PayMethodSearch item
   Description: Call UpdateExt to delete PayMethodSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PayMethodSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PMUID Desc: PMUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PayMethodSearches_Company_PMUID(Company:string, PMUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/PayMethodSearches(" + Company + "," + PMUID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PayMethodListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow)
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
export function get_GetRows(whereClausePayMethod:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePayMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePayMethod=" + whereClausePayMethod
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(pmUID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof pmUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pmUID=" + pmUID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/GetByID" + params, {
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
   Summary: Invoke method GetNewPayMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPayMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPayMethod(requestBody:GetNewPayMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPayMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/GetNewPayMethod", {
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
         resolve(data as GetNewPayMethod_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PayMethodSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PayMethodListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PayMethodRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PayMethodRow,
}

export interface Erp_Tablesets_PayMethodListRow{
      /**  Company  */  
   "Company":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Name of the payment method  */  
   "Name":string,
      /**   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  */  
   "Type":number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   "EFTHeadUID":number,
      /**  Payment Instrument Type  */  
   "PIType":string,
      /**  Payment Instrument Approve flag  */  
   "PIApprove":boolean,
      /**  System Row ID - GUID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PayMethodRow{
      /**  Company  */  
   "Company":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Name of the payment method  */  
   "Name":string,
      /**   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  */  
   "Type":number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   "EFTHeadUID":number,
      /**  This will be the default filename for the output file created by the electronic interface  */  
   "OutputFile":string,
      /**  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  */  
   "OnlyBankCurr":boolean,
      /**   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  */  
   "PMSource":number,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   "SummarizePerCustomer":boolean,
      /**  Default Payment Code  */  
   "DefPayCode":string,
      /**  Auto Bank Reconciliation  */  
   "AutoBankRec":boolean,
      /**  Sender Reference  */  
   "SenderRef":string,
      /**  Registration Number  */  
   "RegNum":string,
      /**  Checkbox to indicate test transmissions  */  
   "Test":boolean,
      /**  Reimbursable  */  
   "Reimbursable":boolean,
      /**  Inactive flag  */  
   "Inactive":boolean,
      /**  Contains the overpayment threshold allowed for ar invoices in bank file import.  */  
   "OverPayPct":number,
      /**  Contains the underpayment threshold allowed for ar invoices in bank file import.  */  
   "UnderPayPct":number,
      /**  Payment Instrument Type  */  
   "PIType":string,
      /**  Payment Instrument Generation Method  */  
   "PIGenMethod":number,
      /**  Payment Instrument Approve flag  */  
   "PIApprove":boolean,
      /**  Marks this PayMethod as global, available to be sent out to other companies.  */  
   "GlobalPayMethod":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**   Denmark Localization
Card (payment) code  */  
   "CardCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  System Row ID - GUID  */  
   "SysRowID":string,
      /**  DepositSlips  */  
   "DepositSlips":number,
      /**  IsPositiveBalance  */  
   "IsPositiveBalance":boolean,
      /**  Specifies how the payments are processed in a bank - individually or in a batch  */  
   "APGrouping":number,
      /**  When this check box is selected, the application uses identifiers generated via an EI program during processing  */  
   "APIDGeneration":boolean,
      /**  Allows the user to specify how the receipts are processed in a bank - individually or in a batch  */  
   "ARGrouping":number,
      /**  When this check box is selected, the application uses identifiers generated via an EI program during processing  */  
   "ARIDGeneration":boolean,
      /**  Specify at what moment the application groups AR receipts in batches  */  
   "ARIDTiming":number,
      /**  EFTDebitMemoHandlingCode  */  
   "EFTDebitMemoHandlingCode":string,
      /**  EFTDebitMemoDueDate  */  
   "EFTDebitMemoDueDate":string,
      /**  EFTProductNumDate  */  
   "EFTProductNumDate":string,
      /**  EFTProductNumber  */  
   "EFTProductNumber":number,
      /**  SEPO3Payment  */  
   "SEPO3Payment":boolean,
      /**  SECrossBrdPayMethod  */  
   "SECrossBrdPayMethod":string,
      /**  SECurrPocket  */  
   "SECurrPocket":string,
      /**  SEErrorHandling  */  
   "SEErrorHandling":string,
      /**  SEUseIBAN  */  
   "SEUseIBAN":string,
      /**  SEPath  */  
   "SEPath":string,
      /**  SECreateErrorLog  */  
   "SECreateErrorLog":boolean,
      /**  SEFileForEachPayCurr  */  
   "SEFileForEachPayCurr":boolean,
      /**  NOPaymentList  */  
   "NOPaymentList":boolean,
      /**  NOTelepayPayment  */  
   "NOTelepayPayment":boolean,
      /**  NOTelepayReply  */  
   "NOTelepayReply":boolean,
      /**  DEFeeRule  */  
   "DEFeeRule":string,
      /**  DESerialNum  */  
   "DESerialNum":number,
      /**  DEStateNum  */  
   "DEStateNum":string,
      /**  DELastUseDate  */  
   "DELastUseDate":string,
      /**  MXPaidAs  */  
   "MXPaidAs":string,
      /**  MXPaymentNum  */  
   "MXPaymentNum":number,
      /**  MXTotalPayments  */  
   "MXTotalPayments":number,
      /**  The field specifies the mexican type of the payment: 2 – Check, 3 – Transfer, 0 – Other  */  
   "MXPaymentType":number,
      /**  MXSATCode  */  
   "MXSATCode":string,
      /**  MXSATDesc  */  
   "MXSATDesc":string,
      /**  PymtProposal  */  
   "PymtProposal":boolean,
      /**  AutoCheckNum  */  
   "AutoCheckNum":boolean,
      /**  EnterPymtTotal  */  
   "EnterPymtTotal":boolean,
      /**  CheckNumSeq  */  
   "CheckNumSeq":number,
      /**  Form 1099-K Transaction Type  */  
   "US1099KTranType":string,
      /**  Form 1099-K Third Party Network Amount Threshold  */  
   "US1099KAmtThreshold":number,
      /**  Form 1099-K Third Party Network Transaction Threshold  */  
   "US1099KTranThreshold":number,
      /**  COPayForm  */  
   "COPayForm":string,
      /**  COPayMethod  */  
   "COPayMethod":string,
      /**  UNCL4461  */  
   "TypeCode":string,
      /**  Indicates if the threshold fields are enabled  */  
   "EnableThresholds":boolean,
   "IsCZLocalization":boolean,
      /**  Shows a char representation of a PMSource: 0 = AP, 1 = AR.  */  
   "PMSourceModule":string,
      /**  EnableAPInfo  */  
   "EnableAPInfo":boolean,
   "COPayMethodDesc":string,
   "TypeDescription":string,
   "BitFlag":number,
   "EFTHeadName":string,
   "EFTHeadType":number,
   "PITypeDescription":string,
   "XbSystELIEinvoice":boolean,
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
      @param pmUID
   */  
export interface DeleteByID_input{
   pmUID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PayMethodListRow{
      /**  Company  */  
   Company:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Name of the payment method  */  
   Name:string,
      /**   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  */  
   Type:number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   EFTHeadUID:number,
      /**  Payment Instrument Type  */  
   PIType:string,
      /**  Payment Instrument Approve flag  */  
   PIApprove:boolean,
      /**  System Row ID - GUID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PayMethodListTableset{
   PayMethodList:Erp_Tablesets_PayMethodListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PayMethodRow{
      /**  Company  */  
   Company:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Name of the payment method  */  
   Name:string,
      /**   Indicated the type of payment with the following options: 
?	0 = Manual (default)
?	1 = Electronic Interface
?	2 = Check Printing
?	3 = Generated Payment Instrument
?	4 = Received Payment Instrument
?	5 = Future Payment Instrument Printing
?	6 = Manual Payment Instrument
?	7 = In Cash
?	8 = On-site
?	9 = MICR Check Printing  */  
   Type:number,
      /**  Indicates the electronic interface that shall be used for the payment method  */  
   EFTHeadUID:number,
      /**  This will be the default filename for the output file created by the electronic interface  */  
   OutputFile:string,
      /**  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  */  
   OnlyBankCurr:boolean,
      /**   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  */  
   PMSource:number,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   SummarizePerCustomer:boolean,
      /**  Default Payment Code  */  
   DefPayCode:string,
      /**  Auto Bank Reconciliation  */  
   AutoBankRec:boolean,
      /**  Sender Reference  */  
   SenderRef:string,
      /**  Registration Number  */  
   RegNum:string,
      /**  Checkbox to indicate test transmissions  */  
   Test:boolean,
      /**  Reimbursable  */  
   Reimbursable:boolean,
      /**  Inactive flag  */  
   Inactive:boolean,
      /**  Contains the overpayment threshold allowed for ar invoices in bank file import.  */  
   OverPayPct:number,
      /**  Contains the underpayment threshold allowed for ar invoices in bank file import.  */  
   UnderPayPct:number,
      /**  Payment Instrument Type  */  
   PIType:string,
      /**  Payment Instrument Generation Method  */  
   PIGenMethod:number,
      /**  Payment Instrument Approve flag  */  
   PIApprove:boolean,
      /**  Marks this PayMethod as global, available to be sent out to other companies.  */  
   GlobalPayMethod:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  System Row ID - GUID  */  
   SysRowID:string,
      /**  DepositSlips  */  
   DepositSlips:number,
      /**  IsPositiveBalance  */  
   IsPositiveBalance:boolean,
      /**  Specifies how the payments are processed in a bank - individually or in a batch  */  
   APGrouping:number,
      /**  When this check box is selected, the application uses identifiers generated via an EI program during processing  */  
   APIDGeneration:boolean,
      /**  Allows the user to specify how the receipts are processed in a bank - individually or in a batch  */  
   ARGrouping:number,
      /**  When this check box is selected, the application uses identifiers generated via an EI program during processing  */  
   ARIDGeneration:boolean,
      /**  Specify at what moment the application groups AR receipts in batches  */  
   ARIDTiming:number,
      /**  EFTDebitMemoHandlingCode  */  
   EFTDebitMemoHandlingCode:string,
      /**  EFTDebitMemoDueDate  */  
   EFTDebitMemoDueDate:string,
      /**  EFTProductNumDate  */  
   EFTProductNumDate:string,
      /**  EFTProductNumber  */  
   EFTProductNumber:number,
      /**  SEPO3Payment  */  
   SEPO3Payment:boolean,
      /**  SECrossBrdPayMethod  */  
   SECrossBrdPayMethod:string,
      /**  SECurrPocket  */  
   SECurrPocket:string,
      /**  SEErrorHandling  */  
   SEErrorHandling:string,
      /**  SEUseIBAN  */  
   SEUseIBAN:string,
      /**  SEPath  */  
   SEPath:string,
      /**  SECreateErrorLog  */  
   SECreateErrorLog:boolean,
      /**  SEFileForEachPayCurr  */  
   SEFileForEachPayCurr:boolean,
      /**  NOPaymentList  */  
   NOPaymentList:boolean,
      /**  NOTelepayPayment  */  
   NOTelepayPayment:boolean,
      /**  NOTelepayReply  */  
   NOTelepayReply:boolean,
      /**  DEFeeRule  */  
   DEFeeRule:string,
      /**  DESerialNum  */  
   DESerialNum:number,
      /**  DEStateNum  */  
   DEStateNum:string,
      /**  DELastUseDate  */  
   DELastUseDate:string,
      /**  MXPaidAs  */  
   MXPaidAs:string,
      /**  MXPaymentNum  */  
   MXPaymentNum:number,
      /**  MXTotalPayments  */  
   MXTotalPayments:number,
      /**  The field specifies the mexican type of the payment: 2 – Check, 3 – Transfer, 0 – Other  */  
   MXPaymentType:number,
      /**  MXSATCode  */  
   MXSATCode:string,
      /**  MXSATDesc  */  
   MXSATDesc:string,
      /**  PymtProposal  */  
   PymtProposal:boolean,
      /**  AutoCheckNum  */  
   AutoCheckNum:boolean,
      /**  EnterPymtTotal  */  
   EnterPymtTotal:boolean,
      /**  CheckNumSeq  */  
   CheckNumSeq:number,
      /**  Form 1099-K Transaction Type  */  
   US1099KTranType:string,
      /**  Form 1099-K Third Party Network Amount Threshold  */  
   US1099KAmtThreshold:number,
      /**  Form 1099-K Third Party Network Transaction Threshold  */  
   US1099KTranThreshold:number,
      /**  COPayForm  */  
   COPayForm:string,
      /**  COPayMethod  */  
   COPayMethod:string,
      /**  UNCL4461  */  
   TypeCode:string,
      /**  Indicates if the threshold fields are enabled  */  
   EnableThresholds:boolean,
   IsCZLocalization:boolean,
      /**  Shows a char representation of a PMSource: 0 = AP, 1 = AR.  */  
   PMSourceModule:string,
      /**  EnableAPInfo  */  
   EnableAPInfo:boolean,
   COPayMethodDesc:string,
   TypeDescription:string,
   BitFlag:number,
   EFTHeadName:string,
   EFTHeadType:number,
   PITypeDescription:string,
   XbSystELIEinvoice:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PayMethodSearchTableset{
   PayMethod:Erp_Tablesets_PayMethodRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPayMethodSearchTableset{
   PayMethod:Erp_Tablesets_PayMethodRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param pmUID
   */  
export interface GetByID_input{
   pmUID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PayMethodSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PayMethodSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PayMethodSearchTableset[],
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
   returnObj:Erp_Tablesets_PayMethodListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPayMethod_input{
   ds:Erp_Tablesets_PayMethodSearchTableset[],
}

export interface GetNewPayMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodSearchTableset,
}
}

   /** Required : 
      @param whereClausePayMethod
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePayMethod:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PayMethodSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtPayMethodSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPayMethodSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PayMethodSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PayMethodSearchTableset,
}
}

