import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CheckRecSearchSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/$metadata", {
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
   Description: Get CheckRecSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CheckRecSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedRow
   */  
export function get_CheckRecSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/CheckRecSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CheckRecSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CheckHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRecSearches(requestBody:Erp_Tablesets_CheckHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/CheckRecSearches", {
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
   Summary: Calls GetByID to retrieve the CheckRecSearch item
   Description: Calls GetByID to retrieve the CheckRecSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckRecSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CheckHedRow
   */  
export function get_CheckRecSearches_Company_HeadNum(Company:string, HeadNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CheckHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/CheckRecSearches(" + Company + "," + HeadNum + ")", {
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
         resolve(data as Erp_Tablesets_CheckHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CheckRecSearch for the service
   Description: Calls UpdateExt to update CheckRecSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CheckRecSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CheckHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CheckRecSearches_Company_HeadNum(Company:string, HeadNum:string, requestBody:Erp_Tablesets_CheckHedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/CheckRecSearches(" + Company + "," + HeadNum + ")", {
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
   Summary: Call UpdateExt to delete CheckRecSearch item
   Description: Call UpdateExt to delete CheckRecSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CheckRecSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param HeadNum Desc: HeadNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CheckRecSearches_Company_HeadNum(Company:string, HeadNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/CheckRecSearches(" + Company + "," + HeadNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedListRow)
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
export function get_GetRows(whereClauseCheckHed:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCheckHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCheckHed=" + whereClauseCheckHed
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/GetRows" + params, {
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
export function get_GetByID(headNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof headNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "headNum=" + headNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewCheckHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCheckHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCheckHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCheckHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCheckHed(requestBody:GetNewCheckHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCheckHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/GetNewCheckHed", {
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
         resolve(data as GetNewCheckHed_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CheckRecSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CheckHedListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CheckHedRow,
}

export interface Erp_Tablesets_CheckHedListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  */  
   "Posted":boolean,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  */  
   "CheckNum":number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   "CheckDate":string,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   "FiscalYear":number,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  */  
   "CheckSrc":string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedCheck":boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Amount that the bank cleared the check for.  */  
   "ClearedAmt":number,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Person who cleared the check (System Set).  */  
   "ClearedPerson":string,
      /**  Date that the check was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  End Date of the Statement that the check was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  employee # for payroll checks  */  
   "EmployeeNum":string,
      /**  Check Amount. Base Currency.  */  
   "CheckAmt":number,
      /**  Check Amount. Document Currency.  */  
   "DocCheckAmt":number,
      /**  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  */  
   "ManualPrint":boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   "EntryPerson":string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   "VendorNum":number,
      /**  Vendors name.  */  
   "Name":string,
      /**  First Address line  */  
   "Address1":string,
      /**  Second Address Line  */  
   "Address2":string,
      /**  Third Address Line  */  
   "Address3":string,
      /**  City portion of address  */  
   "City":string,
      /**  Can be blank.  */  
   "State":string,
      /**  Zip code or Postal code portion of address  */  
   "ZIP":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "Country":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   "BankSlip":string,
      /**  Payment by electronic funds transfer.  Default from the Vendor.  */  
   "ElecPayment":boolean,
      /**  ID of the vendor's bank.  */  
   "VendorBankID":string,
      /**  Supplier Bank Name  */  
   "VendorBankName":string,
      /**  Name on the Bank Account.  */  
   "VendorBankNameOnAccount":string,
      /**  First address line of supplier bank.  */  
   "VendorBankAddress1":string,
      /**  Second address line of supplier bank.  */  
   "VendorBankAddress2":string,
      /**  Third address line of supplier bank.  */  
   "VendorBankAddress3":string,
      /**  City portion of address of supplier bank.  */  
   "VendorBankCity":string,
      /**  Can be blank.  */  
   "VendorBankState":string,
      /**  Postal Code or zip code portion of address of supplier bank.  */  
   "VendorBankPostalCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "VendorBankCountryNum":number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   "VendorBankAcctNumber":string,
      /**  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  */  
   "VendorBankSwiftNum":string,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefCheckNum":string,
      /**  Reporting currency value of this field  */  
   "Rpt1CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Total paid amount in Base  */  
   "PaymentTotal":number,
      /**  Total paid amount in payment currency  */  
   "DocPaymentTotal":number,
      /**  Total paid amount in Rpt1 currency  */  
   "Rpt1PaymentTotal":number,
      /**  Total paid amount in Rpt2 currency  */  
   "Rpt2PaymentTotal":number,
      /**  Total paid amount in Rpt3 currency  */  
   "Rpt3PaymentTotal":number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   "Variance":number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   "DocVariance":number,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt1Variance":number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt2Variance":number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt3Variance":number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   "PaymentBankRate":number,
      /**  Total amount in Bank currency  */  
   "BankTotalAmt":number,
      /**  Total entered flag  */  
   "IsEnterTotal":boolean,
      /**  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  */  
   "LockRate":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  */  
   "UsePendAcct":boolean,
      /**  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  */  
   "ForceDiscount":boolean,
      /**  Reference to first checkhed  */  
   "FirstHeadNum":number,
      /**  Identifies that record is created by 'Apply Debit Memo'.  */  
   "ApplyingPayment":boolean,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   "InvoiceNum":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Amount Bank Paid  */  
   "BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "DocBankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt1BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt2BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt3BankPaidAmt":number,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  NOPaymentStatus  */  
   "NOPaymentStatus":number,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  PayLegalNumber  */  
   "PayLegalNumber":string,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  THPayerType  */  
   "THPayerType":number,
   "VoidDate":string,
   "BaseCurrSymbol":string,
      /**  Indicates if payment to a One-Time Vendor  */  
   "OneTimeVendor":boolean,
   "PaymentStatus":string,
   "PaymentAmount":number,
      /**  To be used by UI for entry  */  
   "VendorID":string,
      /**  Enable the Bank Account Search Button  */  
   "BankAccountEnabled":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   "FullyPaid":boolean,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   "TotalRoundDiff":number,
      /**  Bank Currency Code  */  
   "BankCurrCode":string,
      /**  Payment Total can be entered manually  */  
   "EnterPaymentTotal":boolean,
      /**  label <Payment Currency> -> <Bank Currency>  */  
   "XRateLabelPaymentBank":string,
      /**  label <Payment Currency> --> <Base Currency>  */  
   "XRateLabelPaymentBase":string,
   "BankCurrSymbol":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "ExchangeRateDisabled":boolean,
   "BaseExchRate":boolean,
      /**  It is used for Apply Debit Memo Process  */  
   "DocUnappliedAmt":number,
      /**  It is used for Apply Debit Memo Process  */  
   "UnappliedAmt":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt1UnappliedAmt":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt2UnappliedAmt":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt3UnappliedAmt":number,
      /**  It is used for Apply Debit Memo Process  */  
   "InvType":string,
      /**  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  */  
   "DocUnpostedBal":number,
   "HasLines":boolean,
   "BaseCurrencyCode":string,
   "EnableCurrency":boolean,
   "EnableIsEnterTotal":boolean,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Full description of the bank account.  */  
   "BankAcctIDDescription":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrSymbolDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrSymbolCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrSymbolCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrSymbolCurrSymbol":string,
      /**  Description of the currency  */  
   "BaseCurrSymbolCurrDesc":string,
      /**  Description  */  
   "CashbookLineDescription":string,
      /**  Country name  */  
   "CountryNumDescription":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**  Country name  */  
   "VendorBankCountryNumDescription":string,
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
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  CSF Switzerland - Indicate that Check has urgent Invoice payment  */  
   "UrgentCheck":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CheckHedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  */  
   "Posted":boolean,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   "GroupID":string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   "HeadNum":number,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   "BankAcctID":string,
      /**   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  */  
   "CheckNum":number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   "CheckDate":string,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   "FiscalYear":number,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   "FiscalPeriod":number,
      /**  Voided flag  */  
   "Voided":boolean,
      /**  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  */  
   "CheckSrc":string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedCheck":boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   "ClearedPending":boolean,
      /**  Amount that the bank cleared the check for.  */  
   "ClearedAmt":number,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   "DocClearedAmt":number,
      /**  Person who cleared the check (System Set).  */  
   "ClearedPerson":string,
      /**  Date that the check was cleared in the system (System Set).  */  
   "ClearedDate":string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   "ClearedTime":string,
      /**  End Date of the Statement that the check was cleared on.  */  
   "ClearedStmtEndDate":string,
      /**  employee # for payroll checks  */  
   "EmployeeNum":string,
      /**  Check Amount. Base Currency.  */  
   "CheckAmt":number,
      /**  Check Amount. Document Currency.  */  
   "DocCheckAmt":number,
      /**  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  */  
   "ManualPrint":boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   "EntryPerson":string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   "VendorNum":number,
      /**  Vendors name.  */  
   "Name":string,
      /**  First Address line  */  
   "Address1":string,
      /**  Second Address Line  */  
   "Address2":string,
      /**  Third Address Line  */  
   "Address3":string,
      /**  City portion of address  */  
   "City":string,
      /**  Can be blank.  */  
   "State":string,
      /**  Zip code or Postal code portion of address  */  
   "ZIP":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "Country":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   "BankSlip":string,
      /**  Payment by electronic funds transfer.  Default from the Vendor.  */  
   "ElecPayment":boolean,
      /**  ID of the vendor's bank.  */  
   "VendorBankID":string,
      /**  Supplier Bank Name  */  
   "VendorBankName":string,
      /**  Name on the Bank Account.  */  
   "VendorBankNameOnAccount":string,
      /**  First address line of supplier bank.  */  
   "VendorBankAddress1":string,
      /**  Second address line of supplier bank.  */  
   "VendorBankAddress2":string,
      /**  Third address line of supplier bank.  */  
   "VendorBankAddress3":string,
      /**  City portion of address of supplier bank.  */  
   "VendorBankCity":string,
      /**  Can be blank.  */  
   "VendorBankState":string,
      /**  Postal Code or zip code portion of address of supplier bank.  */  
   "VendorBankPostalCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "VendorBankCountryNum":number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   "VendorBankAcctNumber":string,
      /**  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  */  
   "VendorBankSwiftNum":string,
      /**  This field identifies a bankslip.  */  
   "CashBookNum":number,
      /**  This field identifies a line of a bankslip.  */  
   "CashbookLine":number,
      /**  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefCheckNum":string,
      /**  Reporting currency value of this field  */  
   "Rpt1CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3CheckAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ClearedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ClearedAmt":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Total paid amount in Base  */  
   "PaymentTotal":number,
      /**  Total paid amount in payment currency  */  
   "DocPaymentTotal":number,
      /**  Total paid amount in Rpt1 currency  */  
   "Rpt1PaymentTotal":number,
      /**  Total paid amount in Rpt2 currency  */  
   "Rpt2PaymentTotal":number,
      /**  Total paid amount in Rpt3 currency  */  
   "Rpt3PaymentTotal":number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   "Variance":number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   "DocVariance":number,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt1Variance":number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt2Variance":number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   "Rpt3Variance":number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   "PaymentBankRate":number,
      /**  Total amount in Bank currency  */  
   "BankTotalAmt":number,
      /**  Total entered flag  */  
   "IsEnterTotal":boolean,
      /**  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  */  
   "LockRate":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  */  
   "UsePendAcct":boolean,
      /**  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  */  
   "ForceDiscount":boolean,
      /**  Reference to first checkhed  */  
   "FirstHeadNum":number,
      /**  Identifies that record is created by 'Apply Debit Memo'.  */  
   "ApplyingPayment":boolean,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   "InvoiceNum":string,
      /**  Payment Method Unique Identifier  */  
   "PMUID":number,
      /**  Unique identifier of Petty Cash Desk  */  
   "PCashDeskID":string,
      /**  ID Given by the Bank assigned during matching  */  
   "BankTranID":string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   "PCashRefNum":number,
      /**  Amount Bank Paid  */  
   "BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "DocBankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt1BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt2BankPaidAmt":number,
      /**  Amount Bank Paid  */  
   "Rpt3BankPaidAmt":number,
      /**  Bank Transaction Date  */  
   "BankTransDate":string,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  VendorBankIBANCode  */  
   "VendorBankIBANCode":string,
      /**  OwnReference  */  
   "OwnReference":string,
      /**  NOPaymentStatus  */  
   "NOPaymentStatus":number,
      /**  NOPaymentDirection  */  
   "NOPaymentDirection":string,
      /**  NOPaymentType  */  
   "NOPaymentType":string,
      /**  Norway CSF: The name of created payment file.  */  
   "NOTransferFileName":string,
      /**  Norway CSF: Transaction Reference Number assigned by bank.  */  
   "NOBankTransRef":string,
      /**  BalanceUpdate  */  
   "BalanceUpdate":number,
      /**  BankClearedAmt  */  
   "BankClearedAmt":number,
      /**  BankRecGainLoss  */  
   "BankRecGainLoss":number,
      /**  Bill of Exchange Invoice num this was generated from  */  
   "BOEInvoiceNum":string,
      /**  DocBankRecGainLoss  */  
   "DocBankRecGainLoss":number,
      /**  MsgId  */  
   "MsgId":string,
      /**  MXRecDate  */  
   "MXRecDate":string,
      /**  PayLegalNumber  */  
   "PayLegalNumber":string,
      /**  PayTranDocTypeID  */  
   "PayTranDocTypeID":string,
      /**  Rpt1BankRecGainLoss  */  
   "Rpt1BankRecGainLoss":number,
      /**  Rpt2BankRecGainLoss  */  
   "Rpt2BankRecGainLoss":number,
      /**  Rpt3BankRecGainLoss  */  
   "Rpt3BankRecGainLoss":number,
      /**  TaxPaymInfo  */  
   "TaxPaymInfo":string,
      /**  VoidLegalNumber  */  
   "VoidLegalNumber":string,
      /**  VoidTranDocTypeID  */  
   "VoidTranDocTypeID":string,
      /**  SEGrpNum  */  
   "SEGrpNum":number,
      /**  SEReference  */  
   "SEReference":string,
      /**  SEISGroupedPO3  */  
   "SEISGroupedPO3":boolean,
      /**  SEISExported  */  
   "SEISExported":boolean,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  MXBankAcctNumber  */  
   "MXBankAcctNumber":string,
      /**  MXBankIdentifier  */  
   "MXBankIdentifier":string,
      /**  MXRFC  */  
   "MXRFC":string,
      /**  Indicates that payment is currently excluded from batch in Bank Statement Processing.  */  
   "BankBatchExcluded":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  SEPAPaymentDescription  */  
   "SEPAPaymentDescription":string,
      /**  THPayerType  */  
   "THPayerType":number,
      /**  TH Reference Invoice Num  */  
   "THRefInvoiceNum":string,
      /**  TH Reference Vendor Num  */  
   "THRefVendorNum":number,
      /**  Text entered by the user to indicate the reason a Payment  was voided.  */  
   "VoidedReason":string,
      /**  Regulatory Reporting Code  */  
   "RegulatoryReportingCode":string,
      /**  MXFiscalFolio  */  
   "MXFiscalFolio":string,
      /**  Tax Point Date  */  
   "TaxPointDate":string,
      /**  Standard Entry Class Code  */  
   "SEC":string,
      /**  ACH Transaction Code  */  
   "ACHTranCode":number,
      /**  Form 1099-K Merchant Category Code  */  
   "US1099KMerchCatCode":string,
      /**  US1099KGen  */  
   "US1099KGen":boolean,
      /**  Bank Branch Code of the Supplier Bank  */  
   "VendorBankBranchCode":string,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
      /**  Description  */  
   "Description":string,
      /**  GL Description for the Payment Voiding process  */  
   "VoidDescription":string,
      /**  GL Description for AP - Apply Debit Memo/Prepayment  */  
   "DMDescription":string,
      /**  CSF Mexico DIOT Transaction Type  */  
   "MXDIOTTranType":string,
      /**  ChildPlant  */  
   "ChildPlant":string,
   "BankBatchIDDsp":string,
      /**  Bank Check Amount  */  
   "BankCheckAmt":number,
      /**  Bank Currency Code  */  
   "BankCurrCode":string,
   "BankCurrSymbol":string,
   "BaseCurrencyCode":string,
   "BaseCurrSymbol":string,
   "BaseExchRate":boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   "DisableBankAmt":boolean,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in document currency.  */  
   "DocPreTaxTotal":number,
      /**  It is used for Apply Debit Memo Process  */  
   "DocUnappliedAmt":number,
      /**  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  */  
   "DocUnpostedBal":number,
      /**  Withholding taxes calcullated on applying Debit Memo in document currency  */  
   "DocWhldTotal":number,
   "EnableAssignLN":boolean,
   "EnableCurrency":boolean,
   "EnableIsEnterTotal":boolean,
   "EnableTranDocTypeID":boolean,
   "EnableVoidLN":boolean,
      /**  Payment Total can be entered manually  */  
   "EnterPaymentTotal":boolean,
   "ExchangeRateDisabled":boolean,
      /**  If Payment is created from Bank Reconcilation  */  
   "FromBankRec":boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   "FullyPaid":boolean,
   "HasLines":boolean,
      /**  It is used for Apply Debit Memo Process  */  
   "InvType":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
   "LegalNumberMessage":string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Indicates if the Payment (check) date was chagned by the user.  */  
   "ManualDateChange":boolean,
      /**  Indicates if Exchange rate was manually changed by the user.  */  
   "ManualExRateChange":boolean,
      /**  Indicates if payment to a One-Time Vendor  */  
   "OneTimeVendor":boolean,
   "PaymentAmount":number,
   "PaymentStatus":string,
   "PCReceipt":boolean,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in base currency.  */  
   "PreTaxTotal":number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt1 currency.  */  
   "Rpt1PreTaxTotal":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt1UnappliedAmt":number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt1 currency  */  
   "Rpt1WhldTotal":number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt2 currency.  */  
   "Rpt2PreTaxTotal":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt2UnappliedAmt":number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt2 currency  */  
   "Rpt2WhldTotal":number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt3 currency  */  
   "Rpt3PreTaxTotal":number,
      /**  It is used for Apply Debit Memo Process  */  
   "Rpt3UnappliedAmt":number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt3t currency  */  
   "Rpt3WhldTotal":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "SelectedForAction":boolean,
   "SEPAPaymentDescriptionEnabled":boolean,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   "TotalRoundDiff":number,
      /**  It is used for Apply Debit Memo Process  */  
   "UnappliedAmt":number,
      /**  CSF Switzerland - Indicate that Check has urgent Invoice payment  */  
   "UrgentCheck":boolean,
      /**  To be used by UI for entry  */  
   "VendorID":string,
   "VoidDate":string,
      /**  Withholding taxes calcullated on applying Debit Memo in base currency  */  
   "WhldTotal":number,
      /**  label <Payment Currency> -> <Bank Currency>  */  
   "XRateLabelPaymentBank":string,
      /**  label <Payment Currency> --> <Base Currency>  */  
   "XRateLabelPaymentBase":string,
      /**  Enable the Bank Account Search Button  */  
   "BankAccountEnabled":boolean,
      /**  Full address of Voided Payment  */  
   "FullAddress":string,
      /**  Check Misc Amount. Base Currency.  */  
   "CheckMiscAmt":number,
      /**  Check Misc Amount. Document Currency.  */  
   "DocCheckMiscAmt":number,
      /**  Check Invoice Amount. Document Currency.  */  
   "DocCheckInvAmt":number,
      /**  Check Invoice Amount. Base Currency.  */  
   "CheckInvAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1CheckMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2CheckMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3CheckMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1CheckInvAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2CheckInvAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3CheckInvAmt":number,
   "BitFlag":number,
   "BankAcctIDDescription":string,
   "BankAcctIDBankName":string,
   "BankBranchBankBranchCode":string,
   "BankBranchDescription":string,
   "BaseCurrSymbolCurrDesc":string,
   "BaseCurrSymbolCurrName":string,
   "BaseCurrSymbolCurrSymbol":string,
   "BaseCurrSymbolCurrencyID":string,
   "BaseCurrSymbolDocumentDesc":string,
   "CashbookLineDescription":string,
   "CountryNumDescription":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrName":string,
   "PMUIDName":string,
   "THRefVendorNumName":string,
   "THRefVendorNumVendorID":string,
   "VendorBankCountryNumDescription":string,
   "VendorNumCurrencyCode":string,
   "VendorNumName":string,
   "VendorNumAddress3":string,
   "VendorNumAddress1":string,
   "VendorNumVendorID":string,
   "VendorNumAddress2":string,
   "VendorNumTermsCode":string,
   "VendorNumCountry":string,
   "VendorNumState":string,
   "VendorNumCity":string,
   "VendorNumZIP":string,
   "VendorNumDefaultFOB":string,
   "XbSystSiteIsLegalEntity":boolean,
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
      @param headNum
   */  
export interface DeleteByID_input{
   headNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CheckHedListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  */  
   Posted:boolean,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  */  
   CheckNum:number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   CheckDate:string,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   FiscalYear:number,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Voided flag  */  
   Voided:boolean,
      /**  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  */  
   CheckSrc:string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedCheck:boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Amount that the bank cleared the check for.  */  
   ClearedAmt:number,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Person who cleared the check (System Set).  */  
   ClearedPerson:string,
      /**  Date that the check was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  End Date of the Statement that the check was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  employee # for payroll checks  */  
   EmployeeNum:string,
      /**  Check Amount. Base Currency.  */  
   CheckAmt:number,
      /**  Check Amount. Document Currency.  */  
   DocCheckAmt:number,
      /**  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  */  
   ManualPrint:boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   EntryPerson:string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   VendorNum:number,
      /**  Vendors name.  */  
   Name:string,
      /**  First Address line  */  
   Address1:string,
      /**  Second Address Line  */  
   Address2:string,
      /**  Third Address Line  */  
   Address3:string,
      /**  City portion of address  */  
   City:string,
      /**  Can be blank.  */  
   State:string,
      /**  Zip code or Postal code portion of address  */  
   ZIP:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   Country:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   BankSlip:string,
      /**  Payment by electronic funds transfer.  Default from the Vendor.  */  
   ElecPayment:boolean,
      /**  ID of the vendor's bank.  */  
   VendorBankID:string,
      /**  Supplier Bank Name  */  
   VendorBankName:string,
      /**  Name on the Bank Account.  */  
   VendorBankNameOnAccount:string,
      /**  First address line of supplier bank.  */  
   VendorBankAddress1:string,
      /**  Second address line of supplier bank.  */  
   VendorBankAddress2:string,
      /**  Third address line of supplier bank.  */  
   VendorBankAddress3:string,
      /**  City portion of address of supplier bank.  */  
   VendorBankCity:string,
      /**  Can be blank.  */  
   VendorBankState:string,
      /**  Postal Code or zip code portion of address of supplier bank.  */  
   VendorBankPostalCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   VendorBankCountryNum:number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   VendorBankAcctNumber:string,
      /**  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  */  
   VendorBankSwiftNum:string,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefCheckNum:string,
      /**  Reporting currency value of this field  */  
   Rpt1CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Total paid amount in Base  */  
   PaymentTotal:number,
      /**  Total paid amount in payment currency  */  
   DocPaymentTotal:number,
      /**  Total paid amount in Rpt1 currency  */  
   Rpt1PaymentTotal:number,
      /**  Total paid amount in Rpt2 currency  */  
   Rpt2PaymentTotal:number,
      /**  Total paid amount in Rpt3 currency  */  
   Rpt3PaymentTotal:number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   Variance:number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   DocVariance:number,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt1Variance:number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt2Variance:number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt3Variance:number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   PaymentBankRate:number,
      /**  Total amount in Bank currency  */  
   BankTotalAmt:number,
      /**  Total entered flag  */  
   IsEnterTotal:boolean,
      /**  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  */  
   LockRate:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  */  
   UsePendAcct:boolean,
      /**  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  */  
   ForceDiscount:boolean,
      /**  Reference to first checkhed  */  
   FirstHeadNum:number,
      /**  Identifies that record is created by 'Apply Debit Memo'.  */  
   ApplyingPayment:boolean,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   InvoiceNum:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Amount Bank Paid  */  
   BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   DocBankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt1BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt2BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt3BankPaidAmt:number,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  NOPaymentStatus  */  
   NOPaymentStatus:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  PayLegalNumber  */  
   PayLegalNumber:string,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  THPayerType  */  
   THPayerType:number,
   VoidDate:string,
   BaseCurrSymbol:string,
      /**  Indicates if payment to a One-Time Vendor  */  
   OneTimeVendor:boolean,
   PaymentStatus:string,
   PaymentAmount:number,
      /**  To be used by UI for entry  */  
   VendorID:string,
      /**  Enable the Bank Account Search Button  */  
   BankAccountEnabled:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   FullyPaid:boolean,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   TotalRoundDiff:number,
      /**  Bank Currency Code  */  
   BankCurrCode:string,
      /**  Payment Total can be entered manually  */  
   EnterPaymentTotal:boolean,
      /**  label <Payment Currency> -> <Bank Currency>  */  
   XRateLabelPaymentBank:string,
      /**  label <Payment Currency> --> <Base Currency>  */  
   XRateLabelPaymentBase:string,
   BankCurrSymbol:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   ExchangeRateDisabled:boolean,
   BaseExchRate:boolean,
      /**  It is used for Apply Debit Memo Process  */  
   DocUnappliedAmt:number,
      /**  It is used for Apply Debit Memo Process  */  
   UnappliedAmt:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt1UnappliedAmt:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt2UnappliedAmt:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt3UnappliedAmt:number,
      /**  It is used for Apply Debit Memo Process  */  
   InvType:string,
      /**  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  */  
   DocUnpostedBal:number,
   HasLines:boolean,
   BaseCurrencyCode:string,
   EnableCurrency:boolean,
   EnableIsEnterTotal:boolean,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Full description of the bank account.  */  
   BankAcctIDDescription:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrSymbolDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrSymbolCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrSymbolCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrSymbolCurrSymbol:string,
      /**  Description of the currency  */  
   BaseCurrSymbolCurrDesc:string,
      /**  Description  */  
   CashbookLineDescription:string,
      /**  Country name  */  
   CountryNumDescription:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**  Country name  */  
   VendorBankCountryNumDescription:string,
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
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  CSF Switzerland - Indicate that Check has urgent Invoice payment  */  
   UrgentCheck:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CheckHedListTableset{
   CheckHedList:Erp_Tablesets_CheckHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CheckHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  */  
   Posted:boolean,
      /**  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  */  
   BankAcctID:string,
      /**   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  */  
   CheckNum:number,
      /**  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  */  
   CheckDate:string,
      /**  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  */  
   FiscalYear:number,
      /**  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  */  
   FiscalPeriod:number,
      /**  Voided flag  */  
   Voided:boolean,
      /**  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  */  
   CheckSrc:string,
      /**  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedCheck:boolean,
      /**  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Amount that the bank cleared the check for.  */  
   ClearedAmt:number,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Person who cleared the check (System Set).  */  
   ClearedPerson:string,
      /**  Date that the check was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  End Date of the Statement that the check was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  employee # for payroll checks  */  
   EmployeeNum:string,
      /**  Check Amount. Base Currency.  */  
   CheckAmt:number,
      /**  Check Amount. Document Currency.  */  
   DocCheckAmt:number,
      /**  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  */  
   ManualPrint:boolean,
      /**  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  */  
   EntryPerson:string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   VendorNum:number,
      /**  Vendors name.  */  
   Name:string,
      /**  First Address line  */  
   Address1:string,
      /**  Second Address Line  */  
   Address2:string,
      /**  Third Address Line  */  
   Address3:string,
      /**  City portion of address  */  
   City:string,
      /**  Can be blank.  */  
   State:string,
      /**  Zip code or Postal code portion of address  */  
   ZIP:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   Country:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   BankSlip:string,
      /**  Payment by electronic funds transfer.  Default from the Vendor.  */  
   ElecPayment:boolean,
      /**  ID of the vendor's bank.  */  
   VendorBankID:string,
      /**  Supplier Bank Name  */  
   VendorBankName:string,
      /**  Name on the Bank Account.  */  
   VendorBankNameOnAccount:string,
      /**  First address line of supplier bank.  */  
   VendorBankAddress1:string,
      /**  Second address line of supplier bank.  */  
   VendorBankAddress2:string,
      /**  Third address line of supplier bank.  */  
   VendorBankAddress3:string,
      /**  City portion of address of supplier bank.  */  
   VendorBankCity:string,
      /**  Can be blank.  */  
   VendorBankState:string,
      /**  Postal Code or zip code portion of address of supplier bank.  */  
   VendorBankPostalCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   VendorBankCountryNum:number,
      /**  The Bank account number for the Vendor.  Used with Electronic payments.  */  
   VendorBankAcctNumber:string,
      /**  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  */  
   VendorBankSwiftNum:string,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefCheckNum:string,
      /**  Reporting currency value of this field  */  
   Rpt1CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3CheckAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Total paid amount in Base  */  
   PaymentTotal:number,
      /**  Total paid amount in payment currency  */  
   DocPaymentTotal:number,
      /**  Total paid amount in Rpt1 currency  */  
   Rpt1PaymentTotal:number,
      /**  Total paid amount in Rpt2 currency  */  
   Rpt2PaymentTotal:number,
      /**  Total paid amount in Rpt3 currency  */  
   Rpt3PaymentTotal:number,
      /**  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  */  
   Variance:number,
      /**  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  */  
   DocVariance:number,
      /**  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt1Variance:number,
      /**  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt2Variance:number,
      /**  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  */  
   Rpt3Variance:number,
      /**  Exchange rate from the payment currency to the Bank currency  */  
   PaymentBankRate:number,
      /**  Total amount in Bank currency  */  
   BankTotalAmt:number,
      /**  Total entered flag  */  
   IsEnterTotal:boolean,
      /**  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  */  
   LockRate:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  */  
   UsePendAcct:boolean,
      /**  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  */  
   ForceDiscount:boolean,
      /**  Reference to first checkhed  */  
   FirstHeadNum:number,
      /**  Identifies that record is created by 'Apply Debit Memo'.  */  
   ApplyingPayment:boolean,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  AP Invoice Number for Apply Debit Memo Process.  */  
   InvoiceNum:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Amount Bank Paid  */  
   BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   DocBankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt1BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt2BankPaidAmt:number,
      /**  Amount Bank Paid  */  
   Rpt3BankPaidAmt:number,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  VendorBankIBANCode  */  
   VendorBankIBANCode:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  NOPaymentStatus  */  
   NOPaymentStatus:number,
      /**  NOPaymentDirection  */  
   NOPaymentDirection:string,
      /**  NOPaymentType  */  
   NOPaymentType:string,
      /**  Norway CSF: The name of created payment file.  */  
   NOTransferFileName:string,
      /**  Norway CSF: Transaction Reference Number assigned by bank.  */  
   NOBankTransRef:string,
      /**  BalanceUpdate  */  
   BalanceUpdate:number,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  BankRecGainLoss  */  
   BankRecGainLoss:number,
      /**  Bill of Exchange Invoice num this was generated from  */  
   BOEInvoiceNum:string,
      /**  DocBankRecGainLoss  */  
   DocBankRecGainLoss:number,
      /**  MsgId  */  
   MsgId:string,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  PayLegalNumber  */  
   PayLegalNumber:string,
      /**  PayTranDocTypeID  */  
   PayTranDocTypeID:string,
      /**  Rpt1BankRecGainLoss  */  
   Rpt1BankRecGainLoss:number,
      /**  Rpt2BankRecGainLoss  */  
   Rpt2BankRecGainLoss:number,
      /**  Rpt3BankRecGainLoss  */  
   Rpt3BankRecGainLoss:number,
      /**  TaxPaymInfo  */  
   TaxPaymInfo:string,
      /**  VoidLegalNumber  */  
   VoidLegalNumber:string,
      /**  VoidTranDocTypeID  */  
   VoidTranDocTypeID:string,
      /**  SEGrpNum  */  
   SEGrpNum:number,
      /**  SEReference  */  
   SEReference:string,
      /**  SEISGroupedPO3  */  
   SEISGroupedPO3:boolean,
      /**  SEISExported  */  
   SEISExported:boolean,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  MXBankAcctNumber  */  
   MXBankAcctNumber:string,
      /**  MXBankIdentifier  */  
   MXBankIdentifier:string,
      /**  MXRFC  */  
   MXRFC:string,
      /**  Indicates that payment is currently excluded from batch in Bank Statement Processing.  */  
   BankBatchExcluded:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  SEPAPaymentDescription  */  
   SEPAPaymentDescription:string,
      /**  THPayerType  */  
   THPayerType:number,
      /**  TH Reference Invoice Num  */  
   THRefInvoiceNum:string,
      /**  TH Reference Vendor Num  */  
   THRefVendorNum:number,
      /**  Text entered by the user to indicate the reason a Payment  was voided.  */  
   VoidedReason:string,
      /**  Regulatory Reporting Code  */  
   RegulatoryReportingCode:string,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  Tax Point Date  */  
   TaxPointDate:string,
      /**  Standard Entry Class Code  */  
   SEC:string,
      /**  ACH Transaction Code  */  
   ACHTranCode:number,
      /**  Form 1099-K Merchant Category Code  */  
   US1099KMerchCatCode:string,
      /**  US1099KGen  */  
   US1099KGen:boolean,
      /**  Bank Branch Code of the Supplier Bank  */  
   VendorBankBranchCode:string,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  Description  */  
   Description:string,
      /**  GL Description for the Payment Voiding process  */  
   VoidDescription:string,
      /**  GL Description for AP - Apply Debit Memo/Prepayment  */  
   DMDescription:string,
      /**  CSF Mexico DIOT Transaction Type  */  
   MXDIOTTranType:string,
      /**  ChildPlant  */  
   ChildPlant:string,
   BankBatchIDDsp:string,
      /**  Bank Check Amount  */  
   BankCheckAmt:number,
      /**  Bank Currency Code  */  
   BankCurrCode:string,
   BankCurrSymbol:string,
   BaseCurrencyCode:string,
   BaseCurrSymbol:string,
   BaseExchRate:boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   DisableBankAmt:boolean,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in document currency.  */  
   DocPreTaxTotal:number,
      /**  It is used for Apply Debit Memo Process  */  
   DocUnappliedAmt:number,
      /**  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  */  
   DocUnpostedBal:number,
      /**  Withholding taxes calcullated on applying Debit Memo in document currency  */  
   DocWhldTotal:number,
   EnableAssignLN:boolean,
   EnableCurrency:boolean,
   EnableIsEnterTotal:boolean,
   EnableTranDocTypeID:boolean,
   EnableVoidLN:boolean,
      /**  Payment Total can be entered manually  */  
   EnterPaymentTotal:boolean,
   ExchangeRateDisabled:boolean,
      /**  If Payment is created from Bank Reconcilation  */  
   FromBankRec:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   FullyPaid:boolean,
   HasLines:boolean,
      /**  It is used for Apply Debit Memo Process  */  
   InvType:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumberMessage:string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Indicates if the Payment (check) date was chagned by the user.  */  
   ManualDateChange:boolean,
      /**  Indicates if Exchange rate was manually changed by the user.  */  
   ManualExRateChange:boolean,
      /**  Indicates if payment to a One-Time Vendor  */  
   OneTimeVendor:boolean,
   PaymentAmount:number,
   PaymentStatus:string,
   PCReceipt:boolean,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in base currency.  */  
   PreTaxTotal:number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt1 currency.  */  
   Rpt1PreTaxTotal:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt1UnappliedAmt:number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt1 currency  */  
   Rpt1WhldTotal:number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt2 currency.  */  
   Rpt2PreTaxTotal:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt2UnappliedAmt:number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt2 currency  */  
   Rpt2WhldTotal:number,
      /**  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt3 currency  */  
   Rpt3PreTaxTotal:number,
      /**  It is used for Apply Debit Memo Process  */  
   Rpt3UnappliedAmt:number,
      /**  Withholding taxes calcullated on applying Debit Memo in Rpt3t currency  */  
   Rpt3WhldTotal:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   SelectedForAction:boolean,
   SEPAPaymentDescriptionEnabled:boolean,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   TotalRoundDiff:number,
      /**  It is used for Apply Debit Memo Process  */  
   UnappliedAmt:number,
      /**  CSF Switzerland - Indicate that Check has urgent Invoice payment  */  
   UrgentCheck:boolean,
      /**  To be used by UI for entry  */  
   VendorID:string,
   VoidDate:string,
      /**  Withholding taxes calcullated on applying Debit Memo in base currency  */  
   WhldTotal:number,
      /**  label <Payment Currency> -> <Bank Currency>  */  
   XRateLabelPaymentBank:string,
      /**  label <Payment Currency> --> <Base Currency>  */  
   XRateLabelPaymentBase:string,
      /**  Enable the Bank Account Search Button  */  
   BankAccountEnabled:boolean,
      /**  Full address of Voided Payment  */  
   FullAddress:string,
      /**  Check Misc Amount. Base Currency.  */  
   CheckMiscAmt:number,
      /**  Check Misc Amount. Document Currency.  */  
   DocCheckMiscAmt:number,
      /**  Check Invoice Amount. Document Currency.  */  
   DocCheckInvAmt:number,
      /**  Check Invoice Amount. Base Currency.  */  
   CheckInvAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1CheckMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2CheckMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3CheckMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1CheckInvAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2CheckInvAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3CheckInvAmt:number,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   BankBranchBankBranchCode:string,
   BankBranchDescription:string,
   BaseCurrSymbolCurrDesc:string,
   BaseCurrSymbolCurrName:string,
   BaseCurrSymbolCurrSymbol:string,
   BaseCurrSymbolCurrencyID:string,
   BaseCurrSymbolDocumentDesc:string,
   CashbookLineDescription:string,
   CountryNumDescription:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrName:string,
   PMUIDName:string,
   THRefVendorNumName:string,
   THRefVendorNumVendorID:string,
   VendorBankCountryNumDescription:string,
   VendorNumCurrencyCode:string,
   VendorNumName:string,
   VendorNumAddress3:string,
   VendorNumAddress1:string,
   VendorNumVendorID:string,
   VendorNumAddress2:string,
   VendorNumTermsCode:string,
   VendorNumCountry:string,
   VendorNumState:string,
   VendorNumCity:string,
   VendorNumZIP:string,
   VendorNumDefaultFOB:string,
   XbSystSiteIsLegalEntity:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CheckRecSearchTableset{
   CheckHed:Erp_Tablesets_CheckHedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCheckRecSearchTableset{
   CheckHed:Erp_Tablesets_CheckHedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param headNum
   */  
export interface GetByID_input{
   headNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CheckRecSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CheckRecSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CheckRecSearchTableset[],
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
   returnObj:Erp_Tablesets_CheckHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCheckHed_input{
   ds:Erp_Tablesets_CheckRecSearchTableset[],
}

export interface GetNewCheckHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CheckRecSearchTableset,
}
}

   /** Required : 
      @param whereClauseCheckHed
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCheckHed:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CheckRecSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtCheckRecSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCheckRecSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CheckRecSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CheckRecSearchTableset,
}
}

