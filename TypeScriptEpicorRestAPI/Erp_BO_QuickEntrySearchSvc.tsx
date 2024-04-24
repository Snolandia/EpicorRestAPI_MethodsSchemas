import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.QuickEntrySearchSvc
// Description: The QuickEntrySearch bo. Used for the QuickEntrySearch Combo.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/$metadata", {
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
   Description: Get QuickEntrySearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickEntrySearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryRow
   */  
export function get_QuickEntrySearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/QuickEntrySearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickEntrySearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuickEntryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuickEntryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuickEntrySearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/QuickEntrySearches", {
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
   Summary: Calls GetByID to retrieve the QuickEntrySearch item
   Description: Calls GetByID to retrieve the QuickEntrySearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntrySearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param QuickEntryType Desc: QuickEntryType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuickEntryRow
   */  
export function get_QuickEntrySearches_Company_EmpID_QuickEntryType_QuickEntryCode(Company:string, EmpID:string, QuickEntryType:string, QuickEntryCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuickEntryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/QuickEntrySearches(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuickEntryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuickEntrySearch for the service
   Description: Calls UpdateExt to update QuickEntrySearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickEntrySearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param QuickEntryType Desc: QuickEntryType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuickEntryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuickEntrySearches_Company_EmpID_QuickEntryType_QuickEntryCode(Company:string, EmpID:string, QuickEntryType:string, QuickEntryCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/QuickEntrySearches(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", {
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
   Summary: Call UpdateExt to delete QuickEntrySearch item
   Description: Call UpdateExt to delete QuickEntrySearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickEntrySearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param QuickEntryType Desc: QuickEntryType   Required: True   Allow empty value : True
      @param QuickEntryCode Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuickEntrySearches_Company_EmpID_QuickEntryType_QuickEntryCode(Company:string, EmpID:string, QuickEntryType:string, QuickEntryCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/QuickEntrySearches(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryListRow)
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
export function get_GetRows(whereClauseQuickEntry:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseQuickEntry!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuickEntry=" + whereClauseQuickEntry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(empID:string, quickEntryType:string, quickEntryCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof empID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "empID=" + empID
   }
   if(typeof quickEntryType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "quickEntryType=" + quickEntryType
   }
   if(typeof quickEntryCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "quickEntryCode=" + quickEntryCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewQuickEntry
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickEntry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuickEntry(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/GetNewQuickEntry", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuickEntryListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuickEntryRow[],
}

export interface Erp_Tablesets_QuickEntryListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "EmpID":string,
      /**  Defines whether the Quick Entry Code relates to Time or Expenses.  */  
   "QuickEntryType":string,
      /**  Unique identifier of this Quick Entry Code.  */  
   "QuickEntryCode":string,
      /**  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  */  
   "LaborType":string,
      /**  This value is used to set the value for the Project.  */  
   "ProjectID":string,
      /**  This value is used to set the value for WBS Phase.  */  
   "PhaseID":string,
      /**  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  */  
   "TimeTypCd":string,
      /**  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  */  
   "JobNum":string,
      /**  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  */  
   "AssemblySeq":number,
      /**  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  */  
   "OprSeq":number,
      /**  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  */  
   "RoleCode":string,
      /**  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  */  
   "IndirectCode":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  */  
   "IndirectExpense":boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  */  
   "PMUID":number,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  */  
   "MiscCode":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  */  
   "Reimbursable":boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  */  
   "TaxRegionCode":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  */  
   "CurrencyCode":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  */  
   "TaxIncluded":boolean,
      /**  The Expense Code for the labor transaction.  */  
   "ExpenseCode":string,
      /**  The Resource Group in which the labor is performed.  */  
   "ResourceGrpID":string,
      /**  The Resource that was used to do the work.  */  
   "ResourceID":string,
      /**  Labor hours.  */  
   "LaborHrs":number,
      /**  The currency the claim amounts are in.  */  
   "ClaimCurrencyCode":string,
      /**  The expense category.  */  
   "ExpenseCategory":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuickEntryRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "EmpID":string,
      /**  Defines whether the Quick Entry Code relates to Time or Expenses.  */  
   "QuickEntryType":string,
      /**  Unique identifier of this Quick Entry Code.  */  
   "QuickEntryCode":string,
      /**  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  */  
   "LaborType":string,
      /**  This value is used to set the value for the Project.  */  
   "ProjectID":string,
      /**  This value is used to set the value for WBS Phase.  */  
   "PhaseID":string,
      /**  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  */  
   "TimeTypCd":string,
      /**  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  */  
   "JobNum":string,
      /**  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  */  
   "AssemblySeq":number,
      /**  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  */  
   "OprSeq":number,
      /**  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  */  
   "RoleCode":string,
      /**  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  */  
   "IndirectCode":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  */  
   "IndirectExpense":boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  */  
   "PMUID":number,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  */  
   "MiscCode":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  */  
   "Reimbursable":boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  */  
   "TaxRegionCode":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  */  
   "CurrencyCode":string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  */  
   "TaxIncluded":boolean,
      /**  The Expense Code for the labor transaction.  */  
   "ExpenseCode":string,
      /**  The Resource Group in which the labor is performed.  */  
   "ResourceGrpID":string,
      /**  The Resource that was used to do the work.  */  
   "ResourceID":string,
      /**  Labor hours.  */  
   "LaborHrs":number,
      /**  The currency the claim amounts are in.  */  
   "ClaimCurrencyCode":string,
      /**  The expense category.  */  
   "ExpenseCategory":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param empID
      @param quickEntryType
      @param quickEntryCode
   */  
export interface DeleteByID_input{
   empID:string,
   quickEntryType:string,
   quickEntryCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_QuickEntryListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  Defines whether the Quick Entry Code relates to Time or Expenses.  */  
   QuickEntryType:string,
      /**  Unique identifier of this Quick Entry Code.  */  
   QuickEntryCode:string,
      /**  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  */  
   LaborType:string,
      /**  This value is used to set the value for the Project.  */  
   ProjectID:string,
      /**  This value is used to set the value for WBS Phase.  */  
   PhaseID:string,
      /**  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  */  
   TimeTypCd:string,
      /**  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  */  
   JobNum:string,
      /**  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  */  
   AssemblySeq:number,
      /**  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  */  
   OprSeq:number,
      /**  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  */  
   RoleCode:string,
      /**  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  */  
   IndirectCode:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  */  
   IndirectExpense:boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  */  
   PMUID:number,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  */  
   MiscCode:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  */  
   Reimbursable:boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  */  
   TaxRegionCode:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  */  
   CurrencyCode:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  */  
   TaxIncluded:boolean,
      /**  The Expense Code for the labor transaction.  */  
   ExpenseCode:string,
      /**  The Resource Group in which the labor is performed.  */  
   ResourceGrpID:string,
      /**  The Resource that was used to do the work.  */  
   ResourceID:string,
      /**  Labor hours.  */  
   LaborHrs:number,
      /**  The currency the claim amounts are in.  */  
   ClaimCurrencyCode:string,
      /**  The expense category.  */  
   ExpenseCategory:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuickEntryListTableset{
   QuickEntryList:Erp_Tablesets_QuickEntryListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QuickEntryRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   EmpID:string,
      /**  Defines whether the Quick Entry Code relates to Time or Expenses.  */  
   QuickEntryType:string,
      /**  Unique identifier of this Quick Entry Code.  */  
   QuickEntryCode:string,
      /**  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  */  
   LaborType:string,
      /**  This value is used to set the value for the Project.  */  
   ProjectID:string,
      /**  This value is used to set the value for WBS Phase.  */  
   PhaseID:string,
      /**  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  */  
   TimeTypCd:string,
      /**  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  */  
   JobNum:string,
      /**  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  */  
   AssemblySeq:number,
      /**  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  */  
   OprSeq:number,
      /**  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  */  
   RoleCode:string,
      /**  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  */  
   IndirectCode:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  */  
   IndirectExpense:boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  */  
   PMUID:number,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  */  
   MiscCode:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  */  
   Reimbursable:boolean,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  */  
   TaxRegionCode:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  */  
   CurrencyCode:string,
      /**  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  */  
   TaxIncluded:boolean,
      /**  The Expense Code for the labor transaction.  */  
   ExpenseCode:string,
      /**  The Resource Group in which the labor is performed.  */  
   ResourceGrpID:string,
      /**  The Resource that was used to do the work.  */  
   ResourceID:string,
      /**  Labor hours.  */  
   LaborHrs:number,
      /**  The currency the claim amounts are in.  */  
   ClaimCurrencyCode:string,
      /**  The expense category.  */  
   ExpenseCategory:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuickEntrySearchTableset{
   QuickEntry:Erp_Tablesets_QuickEntryRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtQuickEntrySearchTableset{
   QuickEntry:Erp_Tablesets_QuickEntryRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param empID
      @param quickEntryType
      @param quickEntryCode
   */  
export interface GetByID_input{
   empID:string,
   quickEntryType:string,
   quickEntryCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_QuickEntrySearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_QuickEntrySearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_QuickEntrySearchTableset[],
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
   returnObj:Erp_Tablesets_QuickEntryListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param empID
      @param quickEntryType
   */  
export interface GetNewQuickEntry_input{
   ds:Erp_Tablesets_QuickEntrySearchTableset[],
   empID:string,
   quickEntryType:string,
}

export interface GetNewQuickEntry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntrySearchTableset[],
}
}

   /** Required : 
      @param whereClauseQuickEntry
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseQuickEntry:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_QuickEntrySearchTableset[],
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
   ds:Erp_Tablesets_UpdExtQuickEntrySearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtQuickEntrySearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_QuickEntrySearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuickEntrySearchTableset[],
}
}

