import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.DMRActnSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/$metadata", {
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
   Description: Get DMRActnSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DMRActnSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRActnRow
   */  
export function get_DMRActnSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/DMRActnSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DMRActnSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DMRActnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DMRActnSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/DMRActnSearches", {
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
   Summary: Calls GetByID to retrieve the DMRActnSearch item
   Description: Calls GetByID to retrieve the DMRActnSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRActnSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param ActionNum Desc: ActionNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   */  
export function get_DMRActnSearches_Company_DMRNum_ActionNum(Company:string, DMRNum:string, ActionNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DMRActnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/DMRActnSearches(" + Company + "," + DMRNum + "," + ActionNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DMRActnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DMRActnSearch for the service
   Description: Calls UpdateExt to update DMRActnSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DMRActnSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param ActionNum Desc: ActionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DMRActnSearches_Company_DMRNum_ActionNum(Company:string, DMRNum:string, ActionNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/DMRActnSearches(" + Company + "," + DMRNum + "," + ActionNum + ")", {
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
   Summary: Call UpdateExt to delete DMRActnSearch item
   Description: Call UpdateExt to delete DMRActnSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DMRActnSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DMRNum Desc: DMRNum   Required: True
      @param ActionNum Desc: ActionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DMRActnSearches_Company_DMRNum_ActionNum(Company:string, DMRNum:string, ActionNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/DMRActnSearches(" + Company + "," + DMRNum + "," + ActionNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRActnListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnListRow)
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
export function get_GetRows(whereClauseDMRActn:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDMRActn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDMRActn=" + whereClauseDMRActn
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/GetRows" + params, {
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(dmRNum:string, actionNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof dmRNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "dmRNum=" + dmRNum
   }
   if(typeof actionNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "actionNum=" + actionNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetVendorDMRSearch
   Description: Purpose: Get the list of a supplier's DMR with the filtered search.
Parameters:  none
Notes:
<param name="whereClause">Stores the filtered search of DMR</param><param name="vendorNum">The current supplier ID</param><param name="pageSize">The number of results to return</param><param name="absolutePage">Display whole page</param><param name="morePages">Display more results</param>
   OperationID: GetVendorDMRSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorDMRSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorDMRSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVendorDMRSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/GetVendorDMRSearch", {
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
   Summary: Invoke method GetNewDMRActn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDMRActn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRActn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDMRActn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/GetNewDMRActn", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DMRActnSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DMRActnListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DMRActnRow[],
}

export interface Erp_Tablesets_DMRActnListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  */  
   "ActionNum":number,
      /**  DMR Action Date.  */  
   "ActionDate":string,
      /**  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  */  
   "ActionType":string,
      /**  DMR Action quantity in base unit of measure.  Must be > ZERO.  */  
   "Quantity":number,
      /**  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  */  
   "DestinationType":string,
      /**  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   "WarehouseCode":string,
      /**  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  */  
   "BinNum":string,
      /**  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  */  
   "JobNum":string,
      /**  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   "DMRSeqNum":number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   "UnitCredit":number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   "DocUnitCredit":number,
      /**  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  */  
   "CreditUM":string,
      /**  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  */  
   "DebitMemoNum":string,
      /**  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  */  
   "DebitMemoLine":number,
      /**  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  */  
   "VendRMANum":string,
      /**  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  */  
   "ActionUserID":string,
      /**  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  */  
   "SysTime":number,
      /**  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  */  
   "CommentText":string,
      /**  DMRs use Reason type "D".  Required for all actions.  */  
   "ReasonCode":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  */  
   "FldWarehouseCode":string,
      /**  The user defined bin number within the warehouse.  */  
   "FldBinNum":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitCredit":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  */  
   "Resolution":string,
      /**  Flag indicating that the part will be returned to the supplier.  */  
   "ReturnToSupplier":boolean,
      /**  This is the supplier's packing slip number for the original receipt of the part.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   "PackLine":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  IssuedComplete  */  
   "IssuedComplete":boolean,
      /**  PCID  */  
   "PCID":string,
      /**  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  */  
   "AcceptIUM":string,
      /**  Indicates if the Warehouse field should be enabled for input.  */  
   "EnableWarehouse":boolean,
      /**  Indicates if the Bin field should be enabled for input.  */  
   "EnableBin":boolean,
      /**  Request to Move  */  
   "RequestMove":boolean,
      /**  Indicates if the RequestMove field should be enabled for input.  */  
   "EnableReqMove":boolean,
      /**  Indicates if the Reason field should be enabled for input.  */  
   "EnableReason":boolean,
      /**  Job Operation Complete  */  
   "OperationComplete":boolean,
   "ReasonDescription":string,
   "RejectType":string,
   "CurrencySwitch":boolean,
   "BaseCurrSymbol":string,
   "CurrSymbol":string,
      /**  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  */  
   "PartTrackSerialNum":boolean,
   "OpenDMR":boolean,
   "ActionTypeDesc":string,
   "LegalNumberMessage":string,
      /**  Plant  */  
   "Plant":string,
      /**  External field for handling unit of measure conversions in the UI.  */  
   "DispQuantity":number,
   "TotRemainQty":number,
      /**  PartNum  */  
   "PartNum":string,
      /**  The plant id of the plant that is controlling the serial processing for this transaction record  */  
   "SerialControlPlant":string,
      /**  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  */  
   "SerialControlPlant2":string,
      /**  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  */  
   "SerialControlPlantIsFromPlt":boolean,
      /**  TranQty  */  
   "TranQty":number,
      /**  TranUOM  */  
   "TranUOM":string,
   "PONum":number,
   "POLine":number,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "BinNumDescription":string,
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
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   "DMRNumPartDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Description  */  
   "RateGrpDescription":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DMRActnRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   "DMRNum":number,
      /**  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  */  
   "ActionNum":number,
      /**  DMR Action Date.  */  
   "ActionDate":string,
      /**  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  */  
   "ActionType":string,
      /**  DMR Action quantity in base unit of measure.  Must be > ZERO.  */  
   "Quantity":number,
      /**  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  */  
   "DestinationType":string,
      /**  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   "WarehouseCode":string,
      /**  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  */  
   "BinNum":string,
      /**  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  */  
   "JobNum":string,
      /**  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   "DMRSeqNum":number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   "UnitCredit":number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   "DocUnitCredit":number,
      /**  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  */  
   "CreditUM":string,
      /**  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  */  
   "DebitMemoNum":string,
      /**  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  */  
   "DebitMemoLine":number,
      /**  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  */  
   "VendRMANum":string,
      /**  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  */  
   "ActionUserID":string,
      /**  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  */  
   "SysTime":number,
      /**  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  */  
   "CommentText":string,
      /**  DMRs use Reason type "D".  Required for all actions.  */  
   "ReasonCode":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  */  
   "FldWarehouseCode":string,
      /**  The user defined bin number within the warehouse.  */  
   "FldBinNum":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitCredit":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  */  
   "Resolution":string,
      /**  Flag indicating that the part will be returned to the supplier.  */  
   "ReturnToSupplier":boolean,
      /**  This is the supplier's packing slip number for the original receipt of the part.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   "PackLine":number,
      /**  Is a boolean and tell us about to disable or not the entire Rejection Screen. DisableRejection checks DisableRejectionChar to enable or disable.  */  
   "DisableRejection":boolean,
      /**  Is a character and has the Company~Debit~ActionNum, has the linkedDebitMemo and helps to check if is needed the DisableRejection.  */  
   "DisableRejectionChar":string,
      /**  Displays the link AP Invoice linked to the Resolution Request Debit memo, Request Correction Invoice, Request supplier credit, the Reference invoice is created.  */  
   "RefInvoiceNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  IssuedComplete  */  
   "IssuedComplete":boolean,
      /**  PCID  */  
   "PCID":string,
      /**  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  */  
   "AcceptIUM":string,
   "ActionTypeDesc":string,
   "BaseCurrSymbol":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
      /**  External field for handling unit of measure conversions in the UI.  */  
   "DispQuantity":number,
      /**  Indicates if the Bin field should be enabled for input.  */  
   "EnableBin":boolean,
      /**  Indicates if the Reason field should be enabled for input.  */  
   "EnableReason":boolean,
      /**  Indicates if the RequestMove field should be enabled for input.  */  
   "EnableReqMove":boolean,
      /**  Indicates if the Warehouse field should be enabled for input.  */  
   "EnableWarehouse":boolean,
   "LegalNumberMessage":string,
   "OpenDMR":boolean,
      /**  Job Operation Complete  */  
   "OperationComplete":boolean,
      /**  PartNum  */  
   "PartNum":string,
      /**  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  */  
   "PartTrackSerialNum":boolean,
      /**  Plant  */  
   "Plant":string,
      /**  PO Currency Code.  */  
   "POCurrencyCode":string,
   "POLine":number,
   "PONum":number,
      /**  DMR item's unit cost in the POs currency.  */  
   "POUnitCost":number,
   "ReasonDescription":string,
   "RejectType":string,
      /**  Request to Move  */  
   "RequestMove":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1POUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2POUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3POUnitCost":number,
      /**  The plant id of the plant that is controlling the serial processing for this transaction record  */  
   "SerialControlPlant":string,
      /**  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  */  
   "SerialControlPlant2":string,
      /**  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  */  
   "SerialControlPlantIsFromPlt":boolean,
   "TotRemainQty":number,
      /**  TranQty  */  
   "TranQty":number,
      /**  TranUOM  */  
   "TranUOM":string,
      /**  Displays the customer name for the Ship To contact related to the RMA.  */  
   "ShipToCustID":string,
      /**  Displays the customer Ship To name related to the RMA.  */  
   "ShipToName":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  Customer that is returning parts on related RMA.  */  
   "CustomerCustID":string,
      /**  The RMA Number that the Return detail is related to.  */  
   "RMANum":number,
      /**  The RMA line that the Return detail is related to.  */  
   "RMALine":number,
      /**  Specifies the ID of the Ship To contact related to the RMA.  */  
   "ShipToID":string,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "BinNumDescription":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "DMRNumPartDescription":string,
   "JobNumPartDescription":string,
   "RateGrpDescription":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param dmRNum
      @param actionNum
   */  
export interface DeleteByID_input{
   dmRNum:number,
   actionNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DMRActnListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  */  
   ActionNum:number,
      /**  DMR Action Date.  */  
   ActionDate:string,
      /**  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  */  
   ActionType:string,
      /**  DMR Action quantity in base unit of measure.  Must be > ZERO.  */  
   Quantity:number,
      /**  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  */  
   DestinationType:string,
      /**  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   WarehouseCode:string,
      /**  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  */  
   BinNum:string,
      /**  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  */  
   JobNum:string,
      /**  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   DMRSeqNum:number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   UnitCredit:number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   DocUnitCredit:number,
      /**  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  */  
   CreditUM:string,
      /**  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  */  
   DebitMemoNum:string,
      /**  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  */  
   DebitMemoLine:number,
      /**  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  */  
   VendRMANum:string,
      /**  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  */  
   ActionUserID:string,
      /**  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  */  
   SysTime:number,
      /**  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  */  
   CommentText:string,
      /**  DMRs use Reason type "D".  Required for all actions.  */  
   ReasonCode:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  */  
   FldWarehouseCode:string,
      /**  The user defined bin number within the warehouse.  */  
   FldBinNum:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Reporting currency value of this field  */  
   Rpt1UnitCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitCredit:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  */  
   Resolution:string,
      /**  Flag indicating that the part will be returned to the supplier.  */  
   ReturnToSupplier:boolean,
      /**  This is the supplier's packing slip number for the original receipt of the part.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackLine:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  IssuedComplete  */  
   IssuedComplete:boolean,
      /**  PCID  */  
   PCID:string,
      /**  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  */  
   AcceptIUM:string,
      /**  Indicates if the Warehouse field should be enabled for input.  */  
   EnableWarehouse:boolean,
      /**  Indicates if the Bin field should be enabled for input.  */  
   EnableBin:boolean,
      /**  Request to Move  */  
   RequestMove:boolean,
      /**  Indicates if the RequestMove field should be enabled for input.  */  
   EnableReqMove:boolean,
      /**  Indicates if the Reason field should be enabled for input.  */  
   EnableReason:boolean,
      /**  Job Operation Complete  */  
   OperationComplete:boolean,
   ReasonDescription:string,
   RejectType:string,
   CurrencySwitch:boolean,
   BaseCurrSymbol:string,
   CurrSymbol:string,
      /**  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  */  
   PartTrackSerialNum:boolean,
   OpenDMR:boolean,
   ActionTypeDesc:string,
   LegalNumberMessage:string,
      /**  Plant  */  
   Plant:string,
      /**  External field for handling unit of measure conversions in the UI.  */  
   DispQuantity:number,
   TotRemainQty:number,
      /**  PartNum  */  
   PartNum:string,
      /**  The plant id of the plant that is controlling the serial processing for this transaction record  */  
   SerialControlPlant:string,
      /**  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  */  
   SerialControlPlant2:string,
      /**  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  */  
   SerialControlPlantIsFromPlt:boolean,
      /**  TranQty  */  
   TranQty:number,
      /**  TranUOM  */  
   TranUOM:string,
   PONum:number,
   POLine:number,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   BinNumDescription:string,
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
      /**  Describes the Part.  System maintained, not user modifiable.  */  
   DMRNumPartDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Description  */  
   RateGrpDescription:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DMRActnListTableset{
   DMRActnList:Erp_Tablesets_DMRActnListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DMRActnRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  */  
   DMRNum:number,
      /**  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  */  
   ActionNum:number,
      /**  DMR Action Date.  */  
   ActionDate:string,
      /**  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  */  
   ActionType:string,
      /**  DMR Action quantity in base unit of measure.  Must be > ZERO.  */  
   Quantity:number,
      /**  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  */  
   DestinationType:string,
      /**  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   WarehouseCode:string,
      /**  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  */  
   BinNum:string,
      /**  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  */  
   JobNum:string,
      /**  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  */  
   DMRSeqNum:number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   UnitCredit:number,
      /**  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  */  
   DocUnitCredit:number,
      /**  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  */  
   CreditUM:string,
      /**  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  */  
   DebitMemoNum:string,
      /**  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  */  
   DebitMemoLine:number,
      /**  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  */  
   VendRMANum:string,
      /**  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  */  
   ActionUserID:string,
      /**  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  */  
   SysTime:number,
      /**  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  */  
   CommentText:string,
      /**  DMRs use Reason type "D".  Required for all actions.  */  
   ReasonCode:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  */  
   FldWarehouseCode:string,
      /**  The user defined bin number within the warehouse.  */  
   FldBinNum:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Reporting currency value of this field  */  
   Rpt1UnitCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitCredit:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  */  
   Resolution:string,
      /**  Flag indicating that the part will be returned to the supplier.  */  
   ReturnToSupplier:boolean,
      /**  This is the supplier's packing slip number for the original receipt of the part.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip.  */  
   PackLine:number,
      /**  Is a boolean and tell us about to disable or not the entire Rejection Screen. DisableRejection checks DisableRejectionChar to enable or disable.  */  
   DisableRejection:boolean,
      /**  Is a character and has the Company~Debit~ActionNum, has the linkedDebitMemo and helps to check if is needed the DisableRejection.  */  
   DisableRejectionChar:string,
      /**  Displays the link AP Invoice linked to the Resolution Request Debit memo, Request Correction Invoice, Request supplier credit, the Reference invoice is created.  */  
   RefInvoiceNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  IssuedComplete  */  
   IssuedComplete:boolean,
      /**  PCID  */  
   PCID:string,
      /**  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  */  
   AcceptIUM:string,
   ActionTypeDesc:string,
   BaseCurrSymbol:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
      /**  External field for handling unit of measure conversions in the UI.  */  
   DispQuantity:number,
      /**  Indicates if the Bin field should be enabled for input.  */  
   EnableBin:boolean,
      /**  Indicates if the Reason field should be enabled for input.  */  
   EnableReason:boolean,
      /**  Indicates if the RequestMove field should be enabled for input.  */  
   EnableReqMove:boolean,
      /**  Indicates if the Warehouse field should be enabled for input.  */  
   EnableWarehouse:boolean,
   LegalNumberMessage:string,
   OpenDMR:boolean,
      /**  Job Operation Complete  */  
   OperationComplete:boolean,
      /**  PartNum  */  
   PartNum:string,
      /**  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  */  
   PartTrackSerialNum:boolean,
      /**  Plant  */  
   Plant:string,
      /**  PO Currency Code.  */  
   POCurrencyCode:string,
   POLine:number,
   PONum:number,
      /**  DMR item's unit cost in the POs currency.  */  
   POUnitCost:number,
   ReasonDescription:string,
   RejectType:string,
      /**  Request to Move  */  
   RequestMove:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1POUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2POUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3POUnitCost:number,
      /**  The plant id of the plant that is controlling the serial processing for this transaction record  */  
   SerialControlPlant:string,
      /**  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  */  
   SerialControlPlant2:string,
      /**  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  */  
   SerialControlPlantIsFromPlt:boolean,
   TotRemainQty:number,
      /**  TranQty  */  
   TranQty:number,
      /**  TranUOM  */  
   TranUOM:string,
      /**  Displays the customer name for the Ship To contact related to the RMA.  */  
   ShipToCustID:string,
      /**  Displays the customer Ship To name related to the RMA.  */  
   ShipToName:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  Customer that is returning parts on related RMA.  */  
   CustomerCustID:string,
      /**  The RMA Number that the Return detail is related to.  */  
   RMANum:number,
      /**  The RMA line that the Return detail is related to.  */  
   RMALine:number,
      /**  Specifies the ID of the Ship To contact related to the RMA.  */  
   ShipToID:string,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   DMRNumPartDescription:string,
   JobNumPartDescription:string,
   RateGrpDescription:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DMRActnSearchTableset{
   DMRActn:Erp_Tablesets_DMRActnRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtDMRActnSearchTableset{
   DMRActn:Erp_Tablesets_DMRActnRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param dmRNum
      @param actionNum
   */  
export interface GetByID_input{
   dmRNum:number,
   actionNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DMRActnSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DMRActnSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DMRActnSearchTableset[],
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
   returnObj:Erp_Tablesets_DMRActnListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param dmRNum
   */  
export interface GetNewDMRActn_input{
   ds:Erp_Tablesets_DMRActnSearchTableset[],
   dmRNum:number,
}

export interface GetNewDMRActn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRActnSearchTableset[],
}
}

   /** Required : 
      @param whereClauseDMRActn
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDMRActn:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DMRActnSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param vendorNum
      @param pageSize
      @param absolutePage
   */  
export interface GetVendorDMRSearch_input{
   whereClause:string,
   vendorNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetVendorDMRSearch_output{
   returnObj:Erp_Tablesets_DMRActnListTableset[],
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
   ds:Erp_Tablesets_UpdExtDMRActnSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDMRActnSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DMRActnSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DMRActnSearchTableset[],
}
}

