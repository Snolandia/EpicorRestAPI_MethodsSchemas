import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.FARevalueRegSearchSvc
// Description: class FARevalueRegSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/$metadata", {
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
   Description: Get FARevalueRegSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FARevalueRegSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueRegSearchRow
   */  
export function get_FARevalueRegSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/FARevalueRegSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FARevalueRegSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FARevalueRegSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FARevalueRegSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FARevalueRegSearches(requestBody:Erp_Tablesets_FARevalueRegSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/FARevalueRegSearches", {
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
   Summary: Calls GetByID to retrieve the FARevalueRegSearch item
   Description: Calls GetByID to retrieve the FARevalueRegSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FARevalueRegSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FARevalueRegSearchRow
   */  
export function get_FARevalueRegSearches_Company_AssetNum_RevalueNum_AssetRegID(Company:string, AssetNum:string, RevalueNum:string, AssetRegID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FARevalueRegSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/FARevalueRegSearches(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")", {
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
         resolve(data as Erp_Tablesets_FARevalueRegSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FARevalueRegSearch for the service
   Description: Calls UpdateExt to update FARevalueRegSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FARevalueRegSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FARevalueRegSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FARevalueRegSearches_Company_AssetNum_RevalueNum_AssetRegID(Company:string, AssetNum:string, RevalueNum:string, AssetRegID:string, requestBody:Erp_Tablesets_FARevalueRegSearchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/FARevalueRegSearches(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")", {
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
   Summary: Call UpdateExt to delete FARevalueRegSearch item
   Description: Call UpdateExt to delete FARevalueRegSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FARevalueRegSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param RevalueNum Desc: RevalueNum   Required: True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FARevalueRegSearches_Company_AssetNum_RevalueNum_AssetRegID(Company:string, AssetNum:string, RevalueNum:string, AssetRegID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/FARevalueRegSearches(" + Company + "," + AssetNum + "," + RevalueNum + "," + AssetRegID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FARevalueRegListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegListRow)
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
export function get_GetRows(whereClauseFARevalueRegSearch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFARevalueRegSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFARevalueRegSearch=" + whereClauseFARevalueRegSearch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(assetNum:string, revalueNum:string, assetRegID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof assetNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assetNum=" + assetNum
   }
   if(typeof revalueNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "revalueNum=" + revalueNum
   }
   if(typeof assetRegID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assetRegID=" + assetRegID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewFARevalueRegSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFARevalueRegSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFARevalueRegSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFARevalueRegSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFARevalueRegSearch(requestBody:GetNewFARevalueRegSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFARevalueRegSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/GetNewFARevalueRegSearch", {
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
         resolve(data as GetNewFARevalueRegSearch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FARevalueRegSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FARevalueRegListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FARevalueRegSearchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FARevalueRegSearchRow,
}

export interface Erp_Tablesets_FARevalueRegListRow{
      /**  Asset Number  */  
   "AssetNum":string,
      /**  Unique number to identify the Revaluation activity of an asset.  */  
   "RevalueNum":number,
      /**  Identifier of the Asset Register.  */  
   "AssetRegID":string,
      /**  Uniquue identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FARevalueRegSearchRow{
      /**  Company  */  
   "Company":string,
      /**  Asset Number  */  
   "AssetNum":string,
      /**  Unique number to identify the Revaluation activity of an asset.  */  
   "RevalueNum":number,
      /**  Identifier of the Asset Register.  */  
   "AssetRegID":string,
      /**  The original Current Asset Cost in base currency before running the Asset Revaluation process.  */  
   "OrigCurrentCost":number,
      /**  The original Current Asset Cost in document currency before running the Asset Revaluation process.  */  
   "DocOrigCurrentCost":number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   "Rpt1OrigCurrentCost":number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   "Rpt2OrigCurrentCost":number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   "Rpt3OrigCurrentCost":number,
      /**  Book Value before revaluation in base currency.  */  
   "OrigBookValue":number,
      /**  Book Value before revaluation in document currency.  */  
   "DocOrigBookValue":number,
      /**  Book Value before revaluation in reporting currency.  */  
   "Rpt1OrigBookValue":number,
      /**  Book Value before revaluation in reporting currency.  */  
   "Rpt2OrigBookValue":number,
      /**  Book Value before revaluation in reporting currency.  */  
   "Rpt3OrigBookValue":number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in base curreny.  */  
   "OrigTotalDepn":number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in document curreny.  */  
   "DocOrigTotalDepn":number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   "Rpt1OrigTotalDepn":number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   "Rpt2OrigTotalDepn":number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   "Rpt3OrigTotalDepn":number,
      /**  Revaluation Gain or Loss in base currency. The difference between Original Book Value and New Book Value  */  
   "RevalueGainLoss":number,
      /**  Revaluation Gain or Loss in document currency. The difference between Original Book Value and New Book Value  */  
   "DocRevalueGainLoss":number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   "Rpt1RevalueGainLoss":number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   "Rpt2RevalueGainLoss":number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   "Rpt3RevalueGainLoss":number,
      /**  Revaluation Surplus in base currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   "RevalueSurplus":number,
      /**  Revaluation Surplus in document currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   "DocRevalueSurplus":number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   "Rpt1RevalueSurplus":number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   "Rpt2RevalueSurplus":number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   "Rpt3RevalueSurplus":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in base currency.  */  
   "GrantAmt":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in document currency.  */  
   "DocGrantAmt":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt1GrantAmt":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt2GrantAmt":number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt3GrantAmt":number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in base currency.  */  
   "GrantDepnAmt":number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in document currency.  */  
   "DocGrantDepnAmt":number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt1GrantDepnAmt":number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt2GrantDepnAmt":number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   "Rpt3GrantDepnAmt":number,
      /**  Grant Book Value at the moment of revaluation in base currency.  */  
   "UnusedGrantAmt":number,
      /**  Grant Book Value at the moment of revaluation in document currency.  */  
   "DocUnusedGrantAmt":number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   "Rpt1UnusedGrantAmt":number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   "Rpt2UnusedGrantAmt":number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   "Rpt3UnusedGrantAmt":number,
      /**  The Depreciation value in the base currency posted to the GL after Revaluation Date.  */  
   "PostedFutrDepnAmt":number,
      /**  The Depreciation value in the documnet currency posted to the GL after Revaluation Date.  */  
   "DocPostedFutrDepnAmt":number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt1PostedFutrDepnAmt":number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt2PostedFutrDepnAmt":number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt3PostedFutrDepnAmt":number,
      /**  The Grant Depreciation value in the base currency posted to the GL  after Revaluation Date.  */  
   "PostedFutrGrantDepnAmt":number,
      /**  The Grant Depreciation value in the document currency posted to the GL  after Revaluation Date.  */  
   "DocPostedFutrGrantDepnAmt":number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt1PostedFutrGrantDepnAmt":number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt2PostedFutrGrantDepnAmt":number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   "Rpt3PostedFutrGrantDepnAmt":number,
      /**  New Estimated Life  */  
   "NewAssetLife":number,
      /**  New Life Modifier. Available Values (PERIODS or YEARS)  */  
   "NewLifeModifier":string,
      /**  New Residual value of the asset in base currency. By default it is equaled current value.  */  
   "NewResidualValue":number,
      /**  New Residual value of the asset in document currency. By default it is equaled current value.  */  
   "DocNewResidualValue":number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   "Rpt1NewResidualValue":number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   "Rpt2NewResidualValue":number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   "Rpt3NewResidualValue":number,
      /**  Revision Identifier for this row. It is incremented upon oach write.  */  
   "SysRevID":number,
      /**  Uniquue identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Value of Depreciation on Disposal/Revaluation setting of the asset, that was used to create the Revaluation.  */  
   "DepOnDisposal":number,
      /**  Accumulated depreciation in the period of revaluation.  */  
   "OrigCurrPerDepn":number,
      /**  Accumulated depreciation in the period of revaluation in document currency.  */  
   "DocOrigCurrPerDepn":number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   "Rpt1OrigCurrPerDepn":number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   "Rpt2OrigCurrPerDepn":number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   "Rpt3OrigCurrPerDepn":number,
      /**  Accumulated grant depreciation in the period of revaluation.  */  
   "OrigCurrPerGrantDepn":number,
      /**  Accumulated grant depreciation in the period of revaluation in document currency.  */  
   "DocOrigCurrPerGrantDepn":number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   "Rpt1OrigCurrPerGrantDepn":number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   "Rpt2OrigCurrPerGrantDepn":number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   "Rpt3OrigCurrPerGrantDepn":number,
   "CurrencyCode":string,
   "DocNewBookValue":number,
   "NewBookValue":number,
   "Rpt1NewBookValue":number,
   "Rpt2NewBookValue":number,
   "Rpt3NewBookValue":number,
   "BitFlag":number,
   "FARevalueReadyToPost":boolean,
   "FARevaluePostedBy":string,
   "FARevalueDocNewBookValue":number,
   "FARevaluePosted":boolean,
   "FARevalueRpt3NewBookValue":number,
   "FARevalueDescription":string,
   "FARevaluePostDate":string,
   "FARevalueNewBookValue":number,
   "FARevalueCurrencyCode":string,
   "FARevalueValuationDate":string,
   "FARevalueApplyDate":string,
   "FARevalueRpt2NewBookValue":number,
   "FARevalueRpt1NewBookValue":number,
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
      @param assetNum
      @param revalueNum
      @param assetRegID
   */  
export interface DeleteByID_input{
   assetNum:string,
   revalueNum:number,
   assetRegID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_FARevalueRegListRow{
      /**  Asset Number  */  
   AssetNum:string,
      /**  Unique number to identify the Revaluation activity of an asset.  */  
   RevalueNum:number,
      /**  Identifier of the Asset Register.  */  
   AssetRegID:string,
      /**  Uniquue identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FARevalueRegSearchListTableset{
   FARevalueRegList:Erp_Tablesets_FARevalueRegListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FARevalueRegSearchRow{
      /**  Company  */  
   Company:string,
      /**  Asset Number  */  
   AssetNum:string,
      /**  Unique number to identify the Revaluation activity of an asset.  */  
   RevalueNum:number,
      /**  Identifier of the Asset Register.  */  
   AssetRegID:string,
      /**  The original Current Asset Cost in base currency before running the Asset Revaluation process.  */  
   OrigCurrentCost:number,
      /**  The original Current Asset Cost in document currency before running the Asset Revaluation process.  */  
   DocOrigCurrentCost:number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   Rpt1OrigCurrentCost:number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   Rpt2OrigCurrentCost:number,
      /**  The original Current Asset Cost in reporting currency before running the Asset Revaluation process.  */  
   Rpt3OrigCurrentCost:number,
      /**  Book Value before revaluation in base currency.  */  
   OrigBookValue:number,
      /**  Book Value before revaluation in document currency.  */  
   DocOrigBookValue:number,
      /**  Book Value before revaluation in reporting currency.  */  
   Rpt1OrigBookValue:number,
      /**  Book Value before revaluation in reporting currency.  */  
   Rpt2OrigBookValue:number,
      /**  Book Value before revaluation in reporting currency.  */  
   Rpt3OrigBookValue:number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in base curreny.  */  
   OrigTotalDepn:number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in document curreny.  */  
   DocOrigTotalDepn:number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   Rpt1OrigTotalDepn:number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   Rpt2OrigTotalDepn:number,
      /**  Accumulated depreciation before revaluation (up to revaluation date) in reporting curreny.  */  
   Rpt3OrigTotalDepn:number,
      /**  Revaluation Gain or Loss in base currency. The difference between Original Book Value and New Book Value  */  
   RevalueGainLoss:number,
      /**  Revaluation Gain or Loss in document currency. The difference between Original Book Value and New Book Value  */  
   DocRevalueGainLoss:number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   Rpt1RevalueGainLoss:number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   Rpt2RevalueGainLoss:number,
      /**  Revaluation Gain or Loss in reporting currency. The difference between Original Book Value and New Book Value  */  
   Rpt3RevalueGainLoss:number,
      /**  Revaluation Surplus in base currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   RevalueSurplus:number,
      /**  Revaluation Surplus in document currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   DocRevalueSurplus:number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   Rpt1RevalueSurplus:number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   Rpt2RevalueSurplus:number,
      /**  Revaluation Surplus in reporting currency. Increase of the asset value that remains after reversing of previous loss (if any).  */  
   Rpt3RevalueSurplus:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in base currency.  */  
   GrantAmt:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in document currency.  */  
   DocGrantAmt:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt1GrantAmt:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt2GrantAmt:number,
      /**  The Grant Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt3GrantAmt:number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in base currency.  */  
   GrantDepnAmt:number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in document currency.  */  
   DocGrantDepnAmt:number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt1GrantDepnAmt:number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt2GrantDepnAmt:number,
      /**  The Grant Depreciation Amount awarded to an asset to reduce the depreciation charge in reporting currency.  */  
   Rpt3GrantDepnAmt:number,
      /**  Grant Book Value at the moment of revaluation in base currency.  */  
   UnusedGrantAmt:number,
      /**  Grant Book Value at the moment of revaluation in document currency.  */  
   DocUnusedGrantAmt:number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   Rpt1UnusedGrantAmt:number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   Rpt2UnusedGrantAmt:number,
      /**  Grant Book Value at the moment of revaluation in reporting currency.  */  
   Rpt3UnusedGrantAmt:number,
      /**  The Depreciation value in the base currency posted to the GL after Revaluation Date.  */  
   PostedFutrDepnAmt:number,
      /**  The Depreciation value in the documnet currency posted to the GL after Revaluation Date.  */  
   DocPostedFutrDepnAmt:number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt1PostedFutrDepnAmt:number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt2PostedFutrDepnAmt:number,
      /**  The Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt3PostedFutrDepnAmt:number,
      /**  The Grant Depreciation value in the base currency posted to the GL  after Revaluation Date.  */  
   PostedFutrGrantDepnAmt:number,
      /**  The Grant Depreciation value in the document currency posted to the GL  after Revaluation Date.  */  
   DocPostedFutrGrantDepnAmt:number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt1PostedFutrGrantDepnAmt:number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt2PostedFutrGrantDepnAmt:number,
      /**  The Grant Depreciation value in the reporting currency posted to the GL after Revaluation Date.  */  
   Rpt3PostedFutrGrantDepnAmt:number,
      /**  New Estimated Life  */  
   NewAssetLife:number,
      /**  New Life Modifier. Available Values (PERIODS or YEARS)  */  
   NewLifeModifier:string,
      /**  New Residual value of the asset in base currency. By default it is equaled current value.  */  
   NewResidualValue:number,
      /**  New Residual value of the asset in document currency. By default it is equaled current value.  */  
   DocNewResidualValue:number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   Rpt1NewResidualValue:number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   Rpt2NewResidualValue:number,
      /**  New Residual value of the asset in reporting currency. By default it is equaled current value.  */  
   Rpt3NewResidualValue:number,
      /**  Revision Identifier for this row. It is incremented upon oach write.  */  
   SysRevID:number,
      /**  Uniquue identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Value of Depreciation on Disposal/Revaluation setting of the asset, that was used to create the Revaluation.  */  
   DepOnDisposal:number,
      /**  Accumulated depreciation in the period of revaluation.  */  
   OrigCurrPerDepn:number,
      /**  Accumulated depreciation in the period of revaluation in document currency.  */  
   DocOrigCurrPerDepn:number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   Rpt1OrigCurrPerDepn:number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   Rpt2OrigCurrPerDepn:number,
      /**  Accumulated depreciation in the period of revaluation in reporting currency.  */  
   Rpt3OrigCurrPerDepn:number,
      /**  Accumulated grant depreciation in the period of revaluation.  */  
   OrigCurrPerGrantDepn:number,
      /**  Accumulated grant depreciation in the period of revaluation in document currency.  */  
   DocOrigCurrPerGrantDepn:number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   Rpt1OrigCurrPerGrantDepn:number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   Rpt2OrigCurrPerGrantDepn:number,
      /**  Accumulated grant depreciation in the period of revaluation in reporting currency.  */  
   Rpt3OrigCurrPerGrantDepn:number,
   CurrencyCode:string,
   DocNewBookValue:number,
   NewBookValue:number,
   Rpt1NewBookValue:number,
   Rpt2NewBookValue:number,
   Rpt3NewBookValue:number,
   BitFlag:number,
   FARevalueReadyToPost:boolean,
   FARevaluePostedBy:string,
   FARevalueDocNewBookValue:number,
   FARevaluePosted:boolean,
   FARevalueRpt3NewBookValue:number,
   FARevalueDescription:string,
   FARevaluePostDate:string,
   FARevalueNewBookValue:number,
   FARevalueCurrencyCode:string,
   FARevalueValuationDate:string,
   FARevalueApplyDate:string,
   FARevalueRpt2NewBookValue:number,
   FARevalueRpt1NewBookValue:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FARevalueRegSearchTableset{
   FARevalueRegSearch:Erp_Tablesets_FARevalueRegSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtFARevalueRegSearchTableset{
   FARevalueRegSearch:Erp_Tablesets_FARevalueRegSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param assetNum
      @param revalueNum
      @param assetRegID
   */  
export interface GetByID_input{
   assetNum:string,
   revalueNum:number,
   assetRegID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_FARevalueRegSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_FARevalueRegSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_FARevalueRegSearchTableset[],
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
   returnObj:Erp_Tablesets_FARevalueRegSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param assetNum
      @param revalueNum
   */  
export interface GetNewFARevalueRegSearch_input{
   ds:Erp_Tablesets_FARevalueRegSearchTableset[],
   assetNum:string,
   revalueNum:number,
}

export interface GetNewFARevalueRegSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueRegSearchTableset,
}
}

   /** Required : 
      @param whereClauseFARevalueRegSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFARevalueRegSearch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_FARevalueRegSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtFARevalueRegSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtFARevalueRegSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_FARevalueRegSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FARevalueRegSearchTableset,
}
}

