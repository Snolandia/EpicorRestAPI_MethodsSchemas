import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.GlbVendorSearchSvc
// Description: Search object for Global Vendors
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/$metadata", {
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
   Description: Get GlbVendorSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbVendorSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbVendorRow
   */  
export function get_GlbVendorSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbVendorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GlbVendorSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbVendorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbVendorSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbVendorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbVendorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbVendorSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GlbVendorSearches", {
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
   Summary: Calls GetByID to retrieve the GlbVendorSearch item
   Description: Calls GetByID to retrieve the GlbVendorSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbVendorSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbVendorNum Desc: GlbVendorNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbVendorRow
   */  
export function get_GlbVendorSearches_Company_GlbCompany_GlbVendorNum(Company:string, GlbCompany:string, GlbVendorNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbVendorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GlbVendorSearches(" + Company + "," + GlbCompany + "," + GlbVendorNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbVendorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlbVendorSearch for the service
   Description: Calls UpdateExt to update GlbVendorSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbVendorSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbVendorNum Desc: GlbVendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbVendorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlbVendorSearches_Company_GlbCompany_GlbVendorNum(Company:string, GlbCompany:string, GlbVendorNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GlbVendorSearches(" + Company + "," + GlbCompany + "," + GlbVendorNum + ")", {
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
   Summary: Call UpdateExt to delete GlbVendorSearch item
   Description: Call UpdateExt to delete GlbVendorSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbVendorSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbVendorNum Desc: GlbVendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlbVendorSearches_Company_GlbCompany_GlbVendorNum(Company:string, GlbCompany:string, GlbVendorNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GlbVendorSearches(" + Company + "," + GlbCompany + "," + GlbVendorNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbVendorListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbVendorListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbVendorListRow)
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
export function get_GetRows(whereClauseGlbVendor:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGlbVendor!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlbVendor=" + whereClauseGlbVendor
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(glbCompany:string, glbVendorNum:string, epicorHeaders?:Headers){
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
   if(typeof glbVendorNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glbVendorNum=" + glbVendorNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GetList" + params, {
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
   Summary: Invoke method RefreshGlbVendorRow
   Description: Refresh global vendor data
   OperationID: RefreshGlbVendorRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshGlbVendorRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshGlbVendorRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshGlbVendorRow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/RefreshGlbVendorRow", {
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
   Summary: Invoke method GetNewGlbVendor
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlbVendor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GetNewGlbVendor", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbVendorListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbVendorListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbVendorRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbVendorRow[],
}

export interface Erp_Tablesets_GlbVendorListRow{
      /**  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  */  
   "Inactive":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  A descriptive Code assigned by the user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  */  
   "VendorID":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "Name":string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
   "Address1":string,
   "Address2":string,
   "Address3":string,
   "City":string,
      /**  Can be blank.  */  
   "State":string,
   "ZIP":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "Country":string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   "TaxPayerID":string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   "PurPoint":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "TermsCode":string,
      /**  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  */  
   "GroupCode":string,
      /**  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  */  
   "Print1099":boolean,
      /**  A user definable field which controls in which box on the 1099 that the amount should be printed.  */  
   "Box1099":number,
      /**  Indicates that for this vendor all invoices must be paid on separate checks.  */  
   "OneCheck":boolean,
      /**  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  */  
   "PrintLabels":boolean,
      /**  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  */  
   "FaxNum":string,
      /**  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   "Comment":string,
      /**  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  */  
   "PayHold":boolean,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  */  
   "PrimPCon":number,
      /**  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  */  
   "AccountRef":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "DefaultFOB":string,
      /**  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
   "TaxRegionCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   "LangNameID":string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   "BorderCrossing":string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   "FormatStr":string,
      /**  Payments to this vendors are made via electronic transfer.  */  
   "ElecPayment":boolean,
      /**  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  */  
   "PrimaryBankID":string,
      /**   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  */  
   "Approved":boolean,
      /**  This is an inter-company vendor.  */  
   "ICVend":boolean,
      /**  Email address of the vendor.  */  
   "EMailAddress":string,
      /**  This vendor is web enabled  */  
   "WebVendor":boolean,
      /**  Vendor URL.  */  
   "VendURL":string,
      /**  Used to calculate on-time delivery performance rating  */  
   "EarlyBuffer":number,
      /**  Used to calculate on-time delivery performance rating  */  
   "LateBuffer":number,
      /**  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   "OnTimeRating":string,
      /**  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  */  
   "QualityRating":string,
      /**  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   "PriceRating":string,
      /**  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   "ServiceRating":string,
      /**  Unique identifier from an external G/L interface  */  
   "ExternalId":string,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   "VendPILimit":number,
      /**  Marks the vendor as a global vendor, available to be sent out to other companies  */  
   "GlobalVendor":boolean,
      /**  Indicates if this vendor participates in the Inter-Company Trading.  */  
   "ICTrader":boolean,
      /**  Owner Company Identifier.  */  
   "GlbCompany":string,
      /**  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   "TaxAuthorityCode":string,
      /**  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "GlbVendorNum":number,
      /**  A descriptive Code assigned by the parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  */  
   "GlbVendorID":string,
      /**  MinOrderValue  */  
   "MinOrderValue":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyBaseCurrCode":string,
   "CalendarID":string,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
   "EDICode":string,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   "OldCompany":string,
      /**  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  */  
   "OldVendorNum":number,
      /**  A descriptive Code assigned by the original parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor. - NOT CURRENTLY IN USE  */  
   "OldVendorID":string,
      /**  Indicates if the user chose to skip this record when linking global vendors.  The user can come back at a later time and choose to link a skipped vendor if they need to.  */  
   "Skipped":boolean,
   "ConsolidatedPurchasing":boolean,
   "LocalPurchasing":boolean,
   "ApplyChrg":boolean,
   "ChrgAmount":number,
   "COD":boolean,
   "CODAmount":number,
   "CODCheck":boolean,
   "CODFreight":boolean,
   "DeclaredAmt":number,
   "DeclaredIns":boolean,
   "DocOnly":boolean,
   "GroundType":string,
   "Hazmat":boolean,
   "NotifyEMail":string,
   "NotifyFlag":boolean,
   "RefNotes":string,
   "ResDelivery":boolean,
   "SatDelivery":boolean,
   "SatPickup":boolean,
   "VerbalConf":boolean,
   "DeliveryType":string,
   "ServAlert":boolean,
   "ServAOD":boolean,
   "ServAuthNum":string,
   "ServDeliveryDate":string,
   "ServHomeDel":boolean,
   "ServInstruct":string,
   "ServPhone":string,
   "ServPOD":boolean,
   "ServRef1":string,
   "ServRef2":string,
   "ServRef3":string,
   "ServRef4":string,
   "ServRef5":string,
   "ServRelease":boolean,
   "ServSatDelivery":boolean,
   "ServSatPickup":boolean,
   "ServSignature":boolean,
   "OverrideCarrier":boolean,
   "OverrideService":boolean,
   "CPay":boolean,
   "AddlHdlgFlag":boolean,
   "CertOfOrigin":boolean,
   "CommercialInvoice":boolean,
   "DeliveryConf":number,
   "FFAddress1":string,
   "FFAddress2":string,
   "FFAddress3":string,
   "FFCity":string,
   "FFCompName":string,
   "FFContact":string,
   "FFCountry":string,
   "FFCountryNum":number,
   "FFID":string,
   "FFPhoneNum":string,
   "FFState":string,
   "FFZip":string,
   "IndividualPackIDs":boolean,
   "IntrntlShip":boolean,
   "LetterOfInstr":boolean,
   "NonStdPkg":boolean,
   "ShipExprtDeclartn":boolean,
   "UPSQuantumView":boolean,
   "UPSQVEmailType":string,
   "UPSQVMemo":string,
   "UPSQVShipFromName":string,
   "RevChargeMethod":string,
   "ManagedCust":boolean,
   "ManagedCustID":string,
   "ManagedCustNum":number,
   "PartPayment":boolean,
   "PMUID":number,
   "HasBank":boolean,
   "PmtAcctRef":string,
   "LegalName":string,
   "OrgRegCode":string,
   "TaxRegReason":string,
   "VendAccountType":string,
   "AdvTaxInv":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  TIN  */  
   "TIN":string,
      /**  TINType  */  
   "TINType":string,
      /**  SecondTINNotice  */  
   "SecondTINNotice":boolean,
      /**  NameControl  */  
   "NameControl":string,
   "DispVendorID":string,
      /**  The VendorId to link to (new or existing)  */  
   "LinkVendorID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbVendorRow{
      /**  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  */  
   "Inactive":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  A descriptive Code assigned by the user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  */  
   "VendorID":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "Name":string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
   "Address1":string,
   "Address2":string,
   "Address3":string,
   "City":string,
      /**  Can be blank.  */  
   "State":string,
   "ZIP":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "Country":string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   "TaxPayerID":string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   "PurPoint":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "TermsCode":string,
      /**  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  */  
   "GroupCode":string,
      /**  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  */  
   "Print1099":boolean,
      /**  A user definable field which controls in which box on the 1099 that the amount should be printed.  */  
   "Box1099":number,
      /**  Indicates that for this vendor all invoices must be paid on separate checks.  */  
   "OneCheck":boolean,
      /**  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  */  
   "PrintLabels":boolean,
      /**  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  */  
   "FaxNum":string,
      /**  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   "Comment":string,
      /**  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  */  
   "PayHold":boolean,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  */  
   "PrimPCon":number,
      /**  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  */  
   "AccountRef":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "DefaultFOB":string,
      /**  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
   "TaxRegionCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   "LangNameID":string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   "BorderCrossing":string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   "FormatStr":string,
      /**  Payments to this vendors are made via electronic transfer.  */  
   "ElecPayment":boolean,
      /**  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  */  
   "PrimaryBankID":string,
      /**   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  */  
   "Approved":boolean,
      /**  This is an inter-company vendor.  */  
   "ICVend":boolean,
      /**  Email address of the vendor.  */  
   "EMailAddress":string,
      /**  This vendor is web enabled  */  
   "WebVendor":boolean,
      /**  Vendor URL.  */  
   "VendURL":string,
      /**  Used to calculate on-time delivery performance rating  */  
   "EarlyBuffer":number,
      /**  Used to calculate on-time delivery performance rating  */  
   "LateBuffer":number,
      /**  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   "OnTimeRating":string,
      /**  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  */  
   "QualityRating":string,
      /**  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   "PriceRating":string,
      /**  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   "ServiceRating":string,
      /**  Unique identifier from an external G/L interface  */  
   "ExternalId":string,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   "VendPILimit":number,
      /**  Marks the vendor as a global vendor, available to be sent out to other companies  */  
   "GlobalVendor":boolean,
      /**  Indicates if this vendor participates in the Inter-Company Trading.  */  
   "ICTrader":boolean,
      /**  Owner Company Identifier.  */  
   "GlbCompany":string,
      /**  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   "TaxAuthorityCode":string,
      /**  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "GlbVendorNum":number,
      /**  A descriptive Code assigned by the parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  */  
   "GlbVendorID":string,
      /**  MinOrderValue  */  
   "MinOrderValue":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyBaseCurrCode":string,
   "CalendarID":string,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
   "EDICode":string,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   "OldCompany":string,
      /**  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  */  
   "OldVendorNum":number,
      /**  A descriptive Code assigned by the original parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor. - NOT CURRENTLY IN USE  */  
   "OldVendorID":string,
      /**  Indicates if the user chose to skip this record when linking global vendors.  The user can come back at a later time and choose to link a skipped vendor if they need to.  */  
   "Skipped":boolean,
   "ConsolidatedPurchasing":boolean,
   "LocalPurchasing":boolean,
   "ApplyChrg":boolean,
   "ChrgAmount":number,
   "COD":boolean,
   "CODAmount":number,
   "CODCheck":boolean,
   "CODFreight":boolean,
   "DeclaredAmt":number,
   "DeclaredIns":boolean,
   "DocOnly":boolean,
   "GroundType":string,
   "Hazmat":boolean,
   "NotifyEMail":string,
   "NotifyFlag":boolean,
   "RefNotes":string,
   "ResDelivery":boolean,
   "SatDelivery":boolean,
   "SatPickup":boolean,
   "VerbalConf":boolean,
   "DeliveryType":string,
   "ServAlert":boolean,
   "ServAOD":boolean,
   "ServAuthNum":string,
   "ServDeliveryDate":string,
   "ServHomeDel":boolean,
   "ServInstruct":string,
   "ServPhone":string,
   "ServPOD":boolean,
   "ServRef1":string,
   "ServRef2":string,
   "ServRef3":string,
   "ServRef4":string,
   "ServRef5":string,
   "ServRelease":boolean,
   "ServSatDelivery":boolean,
   "ServSatPickup":boolean,
   "ServSignature":boolean,
   "OverrideCarrier":boolean,
   "OverrideService":boolean,
   "CPay":boolean,
   "AddlHdlgFlag":boolean,
   "CertOfOrigin":boolean,
   "CommercialInvoice":boolean,
   "DeliveryConf":number,
   "FFAddress1":string,
   "FFAddress2":string,
   "FFAddress3":string,
   "FFCity":string,
   "FFCompName":string,
   "FFContact":string,
   "FFCountry":string,
   "FFCountryNum":number,
   "FFID":string,
   "FFPhoneNum":string,
   "FFState":string,
   "FFZip":string,
   "IndividualPackIDs":boolean,
   "IntrntlShip":boolean,
   "LetterOfInstr":boolean,
   "NonStdPkg":boolean,
   "ShipExprtDeclartn":boolean,
   "UPSQuantumView":boolean,
   "UPSQVEmailType":string,
   "UPSQVMemo":string,
   "UPSQVShipFromName":string,
   "RevChargeMethod":string,
   "ManagedCust":boolean,
   "ManagedCustID":string,
   "ManagedCustNum":number,
   "PartPayment":boolean,
   "PMUID":number,
   "HasBank":boolean,
   "PmtAcctRef":string,
   "LegalName":string,
   "OrgRegCode":string,
   "TaxRegReason":string,
   "VendAccountType":string,
   "AdvTaxInv":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AllowAsAltRemitTo  */  
   "AllowAsAltRemitTo":boolean,
      /**  THBranchID  */  
   "THBranchID":string,
      /**  ParamCode  */  
   "ParamCode":string,
      /**  AGAFIPResponsibilityCode  */  
   "AGAFIPResponsibilityCode":string,
      /**  AGGrossIncomeTaxID  */  
   "AGGrossIncomeTaxID":string,
      /**  AGIDDocumentTypeCode  */  
   "AGIDDocumentTypeCode":string,
      /**  AGProvinceCode  */  
   "AGProvinceCode":string,
      /**  AGUseGoodDefaultMark  */  
   "AGUseGoodDefaultMark":boolean,
      /**  AGApartment  */  
   "AGApartment":string,
      /**  AGExtraStreetNumber  */  
   "AGExtraStreetNumber":string,
      /**  AGFloor  */  
   "AGFloor":string,
      /**  AGLocationCode  */  
   "AGLocationCode":string,
      /**  AGNeighborhood  */  
   "AGNeighborhood":string,
      /**  AGStreet  */  
   "AGStreet":string,
      /**  AGStreetNumber  */  
   "AGStreetNumber":string,
      /**  COOneTimeID  */  
   "COOneTimeID":string,
      /**  NoBankingReference  */  
   "NoBankingReference":boolean,
      /**  PEGoodsContributor  */  
   "PEGoodsContributor":boolean,
      /**  PEWithholdAgent  */  
   "PEWithholdAgent":boolean,
      /**  PECollectionAgent  */  
   "PECollectionAgent":boolean,
      /**  PENotFound  */  
   "PENotFound":boolean,
      /**  PENoAddress  */  
   "PENoAddress":boolean,
      /**  PEIdentityDocType  */  
   "PEIdentityDocType":string,
      /**  COIsOneTimeVend  */  
   "COIsOneTimeVend":boolean,
      /**  PEDocumentID  */  
   "PEDocumentID":string,
      /**  MaxLateDaysPORel  */  
   "MaxLateDaysPORel":number,
      /**  1099 Code  */  
   "Code1099ID":string,
      /**  TIN  */  
   "TIN":string,
      /**  TINType  */  
   "TINType":string,
      /**  SecondTINNotice  */  
   "SecondTINNotice":boolean,
      /**  NameControl  */  
   "NameControl":string,
      /**  ShipViaCode  */  
   "ShipViaCode":string,
      /**  NonUS  */  
   "NonUS":boolean,
      /**  FormTypeID  */  
   "FormTypeID":string,
      /**  INSupplierType  */  
   "INSupplierType":string,
      /**  INCSTNumber  */  
   "INCSTNumber":string,
      /**  INPANNumber  */  
   "INPANNumber":string,
      /**  DEOrgType  */  
   "DEOrgType":string,
      /**  PaymentReporting  */  
   "PaymentReporting":boolean,
      /**  ExternalPurchasing  */  
   "ExternalPurchasing":boolean,
      /**  MXRetentionCode  */  
   "MXRetentionCode":string,
      /**  Reporting1099Name  */  
   "Reporting1099Name":string,
      /**  Reporting1099Name2  */  
   "Reporting1099Name2":string,
      /**  FATCA  */  
   "FATCA":boolean,
      /**  AccountNum  */  
   "AccountNum":string,
      /**  TWGUIRegNum  */  
   "TWGUIRegNum":string,
      /**  MXTARCode  */  
   "MXTARCode":string,
      /**  PEAddressID  */  
   "PEAddressID":string,
      /**  PERetentionRegime  */  
   "PERetentionRegime":string,
      /**  TaxEntityType  */  
   "TaxEntityType":string,
      /**  INGSTComplianceRate  */  
   "INGSTComplianceRate":number,
      /**  INTaxRegistrationID  */  
   "INTaxRegistrationID":string,
      /**  TINValidationStatus  */  
   "TINValidationStatus":number,
      /**  ImporterOfRecord  */  
   "ImporterOfRecord":boolean,
      /**  PLAutomaticAPInvoiceNum  */  
   "PLAutomaticAPInvoiceNum":boolean,
      /**  SEC  */  
   "SEC":string,
      /**  MXDIOTTranType  */  
   "MXDIOTTranType":string,
      /**  US1099KMerchCatCode  */  
   "US1099KMerchCatCode":string,
      /**  MXTaxpayerType  */  
   "MXTaxpayerType":string,
      /**  MXLegalRepRFC  */  
   "MXLegalRepRFC":string,
      /**  MXLegalRepCURP  */  
   "MXLegalRepCURP":string,
      /**  MXLegalRepName  */  
   "MXLegalRepName":string,
      /**  MXLegalRepTaxpayerType  */  
   "MXLegalRepTaxpayerType":string,
      /**  US1099State  */  
   "US1099State":string,
      /**  TaxValidationStatus  */  
   "TaxValidationStatus":number,
      /**  TaxValidationDate  */  
   "TaxValidationDate":string,
      /**  HMRCTaxValidationLog  */  
   "HMRCTaxValidationLog":string,
      /**  ExternalSchemeID  */  
   "ExternalSchemeID":string,
      /**  Municipio Code  */  
   "MXMunicipio":string,
      /**  EInvoice  */  
   "EInvoice":boolean,
      /**  Flag used to mark a Supplier as EDI.  */  
   "EDISupplier":boolean,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
   "DispVendorID":string,
      /**  The VendorId to link to (new or existing)  */  
   "LinkVendorID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param glbCompany
      @param glbVendorNum
   */  
export interface DeleteByID_input{
   glbCompany:string,
   glbVendorNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GlbVendorListRow{
      /**  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  */  
   Inactive:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  A descriptive Code assigned by the user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  */  
   VendorID:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   Name:string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
   Address1:string,
   Address2:string,
   Address3:string,
   City:string,
      /**  Can be blank.  */  
   State:string,
   ZIP:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   Country:string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   TaxPayerID:string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   PurPoint:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   TermsCode:string,
      /**  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  */  
   GroupCode:string,
      /**  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  */  
   Print1099:boolean,
      /**  A user definable field which controls in which box on the 1099 that the amount should be printed.  */  
   Box1099:number,
      /**  Indicates that for this vendor all invoices must be paid on separate checks.  */  
   OneCheck:boolean,
      /**  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  */  
   PrintLabels:boolean,
      /**  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  */  
   FaxNum:string,
      /**  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   Comment:string,
      /**  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  */  
   PayHold:boolean,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  */  
   PrimPCon:number,
      /**  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  */  
   AccountRef:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   DefaultFOB:string,
      /**  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
   TaxRegionCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   FormatStr:string,
      /**  Payments to this vendors are made via electronic transfer.  */  
   ElecPayment:boolean,
      /**  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  */  
   PrimaryBankID:string,
      /**   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  */  
   Approved:boolean,
      /**  This is an inter-company vendor.  */  
   ICVend:boolean,
      /**  Email address of the vendor.  */  
   EMailAddress:string,
      /**  This vendor is web enabled  */  
   WebVendor:boolean,
      /**  Vendor URL.  */  
   VendURL:string,
      /**  Used to calculate on-time delivery performance rating  */  
   EarlyBuffer:number,
      /**  Used to calculate on-time delivery performance rating  */  
   LateBuffer:number,
      /**  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   OnTimeRating:string,
      /**  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  */  
   QualityRating:string,
      /**  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   PriceRating:string,
      /**  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   ServiceRating:string,
      /**  Unique identifier from an external G/L interface  */  
   ExternalId:string,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   VendPILimit:number,
      /**  Marks the vendor as a global vendor, available to be sent out to other companies  */  
   GlobalVendor:boolean,
      /**  Indicates if this vendor participates in the Inter-Company Trading.  */  
   ICTrader:boolean,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   TaxAuthorityCode:string,
      /**  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   GlbVendorNum:number,
      /**  A descriptive Code assigned by the parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  */  
   GlbVendorID:string,
      /**  MinOrderValue  */  
   MinOrderValue:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyBaseCurrCode:string,
   CalendarID:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
   EDICode:string,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  */  
   OldVendorNum:number,
      /**  A descriptive Code assigned by the original parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor. - NOT CURRENTLY IN USE  */  
   OldVendorID:string,
      /**  Indicates if the user chose to skip this record when linking global vendors.  The user can come back at a later time and choose to link a skipped vendor if they need to.  */  
   Skipped:boolean,
   ConsolidatedPurchasing:boolean,
   LocalPurchasing:boolean,
   ApplyChrg:boolean,
   ChrgAmount:number,
   COD:boolean,
   CODAmount:number,
   CODCheck:boolean,
   CODFreight:boolean,
   DeclaredAmt:number,
   DeclaredIns:boolean,
   DocOnly:boolean,
   GroundType:string,
   Hazmat:boolean,
   NotifyEMail:string,
   NotifyFlag:boolean,
   RefNotes:string,
   ResDelivery:boolean,
   SatDelivery:boolean,
   SatPickup:boolean,
   VerbalConf:boolean,
   DeliveryType:string,
   ServAlert:boolean,
   ServAOD:boolean,
   ServAuthNum:string,
   ServDeliveryDate:string,
   ServHomeDel:boolean,
   ServInstruct:string,
   ServPhone:string,
   ServPOD:boolean,
   ServRef1:string,
   ServRef2:string,
   ServRef3:string,
   ServRef4:string,
   ServRef5:string,
   ServRelease:boolean,
   ServSatDelivery:boolean,
   ServSatPickup:boolean,
   ServSignature:boolean,
   OverrideCarrier:boolean,
   OverrideService:boolean,
   CPay:boolean,
   AddlHdlgFlag:boolean,
   CertOfOrigin:boolean,
   CommercialInvoice:boolean,
   DeliveryConf:number,
   FFAddress1:string,
   FFAddress2:string,
   FFAddress3:string,
   FFCity:string,
   FFCompName:string,
   FFContact:string,
   FFCountry:string,
   FFCountryNum:number,
   FFID:string,
   FFPhoneNum:string,
   FFState:string,
   FFZip:string,
   IndividualPackIDs:boolean,
   IntrntlShip:boolean,
   LetterOfInstr:boolean,
   NonStdPkg:boolean,
   ShipExprtDeclartn:boolean,
   UPSQuantumView:boolean,
   UPSQVEmailType:string,
   UPSQVMemo:string,
   UPSQVShipFromName:string,
   RevChargeMethod:string,
   ManagedCust:boolean,
   ManagedCustID:string,
   ManagedCustNum:number,
   PartPayment:boolean,
   PMUID:number,
   HasBank:boolean,
   PmtAcctRef:string,
   LegalName:string,
   OrgRegCode:string,
   TaxRegReason:string,
   VendAccountType:string,
   AdvTaxInv:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  TIN  */  
   TIN:string,
      /**  TINType  */  
   TINType:string,
      /**  SecondTINNotice  */  
   SecondTINNotice:boolean,
      /**  NameControl  */  
   NameControl:string,
   DispVendorID:string,
      /**  The VendorId to link to (new or existing)  */  
   LinkVendorID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbVendorListTableset{
   GlbVendorList:Erp_Tablesets_GlbVendorListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlbVendorRow{
      /**  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  */  
   Inactive:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  A descriptive Code assigned by the user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  */  
   VendorID:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   Name:string,
      /**  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
   Address1:string,
   Address2:string,
   Address3:string,
   City:string,
      /**  Can be blank.  */  
   State:string,
   ZIP:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   Country:string,
      /**  The Tax Payer ID. Used in 1099 processing.  */  
   TaxPayerID:string,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  */  
   PurPoint:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   TermsCode:string,
      /**  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  */  
   GroupCode:string,
      /**  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  */  
   Print1099:boolean,
      /**  A user definable field which controls in which box on the 1099 that the amount should be printed.  */  
   Box1099:number,
      /**  Indicates that for this vendor all invoices must be paid on separate checks.  */  
   OneCheck:boolean,
      /**  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  */  
   PrintLabels:boolean,
      /**  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  */  
   FaxNum:string,
      /**  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   Comment:string,
      /**  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  */  
   PayHold:boolean,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  */  
   PrimPCon:number,
      /**  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  */  
   AccountRef:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   DefaultFOB:string,
      /**  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
   TaxRegionCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   FormatStr:string,
      /**  Payments to this vendors are made via electronic transfer.  */  
   ElecPayment:boolean,
      /**  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  */  
   PrimaryBankID:string,
      /**   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  */  
   Approved:boolean,
      /**  This is an inter-company vendor.  */  
   ICVend:boolean,
      /**  Email address of the vendor.  */  
   EMailAddress:string,
      /**  This vendor is web enabled  */  
   WebVendor:boolean,
      /**  Vendor URL.  */  
   VendURL:string,
      /**  Used to calculate on-time delivery performance rating  */  
   EarlyBuffer:number,
      /**  Used to calculate on-time delivery performance rating  */  
   LateBuffer:number,
      /**  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   OnTimeRating:string,
      /**  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  */  
   QualityRating:string,
      /**  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   PriceRating:string,
      /**  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   ServiceRating:string,
      /**  Unique identifier from an external G/L interface  */  
   ExternalId:string,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   VendPILimit:number,
      /**  Marks the vendor as a global vendor, available to be sent out to other companies  */  
   GlobalVendor:boolean,
      /**  Indicates if this vendor participates in the Inter-Company Trading.  */  
   ICTrader:boolean,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   TaxAuthorityCode:string,
      /**  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   GlbVendorNum:number,
      /**  A descriptive Code assigned by the parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  */  
   GlbVendorID:string,
      /**  MinOrderValue  */  
   MinOrderValue:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyBaseCurrCode:string,
   CalendarID:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
   EDICode:string,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  */  
   OldVendorNum:number,
      /**  A descriptive Code assigned by the original parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor. - NOT CURRENTLY IN USE  */  
   OldVendorID:string,
      /**  Indicates if the user chose to skip this record when linking global vendors.  The user can come back at a later time and choose to link a skipped vendor if they need to.  */  
   Skipped:boolean,
   ConsolidatedPurchasing:boolean,
   LocalPurchasing:boolean,
   ApplyChrg:boolean,
   ChrgAmount:number,
   COD:boolean,
   CODAmount:number,
   CODCheck:boolean,
   CODFreight:boolean,
   DeclaredAmt:number,
   DeclaredIns:boolean,
   DocOnly:boolean,
   GroundType:string,
   Hazmat:boolean,
   NotifyEMail:string,
   NotifyFlag:boolean,
   RefNotes:string,
   ResDelivery:boolean,
   SatDelivery:boolean,
   SatPickup:boolean,
   VerbalConf:boolean,
   DeliveryType:string,
   ServAlert:boolean,
   ServAOD:boolean,
   ServAuthNum:string,
   ServDeliveryDate:string,
   ServHomeDel:boolean,
   ServInstruct:string,
   ServPhone:string,
   ServPOD:boolean,
   ServRef1:string,
   ServRef2:string,
   ServRef3:string,
   ServRef4:string,
   ServRef5:string,
   ServRelease:boolean,
   ServSatDelivery:boolean,
   ServSatPickup:boolean,
   ServSignature:boolean,
   OverrideCarrier:boolean,
   OverrideService:boolean,
   CPay:boolean,
   AddlHdlgFlag:boolean,
   CertOfOrigin:boolean,
   CommercialInvoice:boolean,
   DeliveryConf:number,
   FFAddress1:string,
   FFAddress2:string,
   FFAddress3:string,
   FFCity:string,
   FFCompName:string,
   FFContact:string,
   FFCountry:string,
   FFCountryNum:number,
   FFID:string,
   FFPhoneNum:string,
   FFState:string,
   FFZip:string,
   IndividualPackIDs:boolean,
   IntrntlShip:boolean,
   LetterOfInstr:boolean,
   NonStdPkg:boolean,
   ShipExprtDeclartn:boolean,
   UPSQuantumView:boolean,
   UPSQVEmailType:string,
   UPSQVMemo:string,
   UPSQVShipFromName:string,
   RevChargeMethod:string,
   ManagedCust:boolean,
   ManagedCustID:string,
   ManagedCustNum:number,
   PartPayment:boolean,
   PMUID:number,
   HasBank:boolean,
   PmtAcctRef:string,
   LegalName:string,
   OrgRegCode:string,
   TaxRegReason:string,
   VendAccountType:string,
   AdvTaxInv:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AllowAsAltRemitTo  */  
   AllowAsAltRemitTo:boolean,
      /**  THBranchID  */  
   THBranchID:string,
      /**  ParamCode  */  
   ParamCode:string,
      /**  AGAFIPResponsibilityCode  */  
   AGAFIPResponsibilityCode:string,
      /**  AGGrossIncomeTaxID  */  
   AGGrossIncomeTaxID:string,
      /**  AGIDDocumentTypeCode  */  
   AGIDDocumentTypeCode:string,
      /**  AGProvinceCode  */  
   AGProvinceCode:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGApartment  */  
   AGApartment:string,
      /**  AGExtraStreetNumber  */  
   AGExtraStreetNumber:string,
      /**  AGFloor  */  
   AGFloor:string,
      /**  AGLocationCode  */  
   AGLocationCode:string,
      /**  AGNeighborhood  */  
   AGNeighborhood:string,
      /**  AGStreet  */  
   AGStreet:string,
      /**  AGStreetNumber  */  
   AGStreetNumber:string,
      /**  COOneTimeID  */  
   COOneTimeID:string,
      /**  NoBankingReference  */  
   NoBankingReference:boolean,
      /**  PEGoodsContributor  */  
   PEGoodsContributor:boolean,
      /**  PEWithholdAgent  */  
   PEWithholdAgent:boolean,
      /**  PECollectionAgent  */  
   PECollectionAgent:boolean,
      /**  PENotFound  */  
   PENotFound:boolean,
      /**  PENoAddress  */  
   PENoAddress:boolean,
      /**  PEIdentityDocType  */  
   PEIdentityDocType:string,
      /**  COIsOneTimeVend  */  
   COIsOneTimeVend:boolean,
      /**  PEDocumentID  */  
   PEDocumentID:string,
      /**  MaxLateDaysPORel  */  
   MaxLateDaysPORel:number,
      /**  1099 Code  */  
   Code1099ID:string,
      /**  TIN  */  
   TIN:string,
      /**  TINType  */  
   TINType:string,
      /**  SecondTINNotice  */  
   SecondTINNotice:boolean,
      /**  NameControl  */  
   NameControl:string,
      /**  ShipViaCode  */  
   ShipViaCode:string,
      /**  NonUS  */  
   NonUS:boolean,
      /**  FormTypeID  */  
   FormTypeID:string,
      /**  INSupplierType  */  
   INSupplierType:string,
      /**  INCSTNumber  */  
   INCSTNumber:string,
      /**  INPANNumber  */  
   INPANNumber:string,
      /**  DEOrgType  */  
   DEOrgType:string,
      /**  PaymentReporting  */  
   PaymentReporting:boolean,
      /**  ExternalPurchasing  */  
   ExternalPurchasing:boolean,
      /**  MXRetentionCode  */  
   MXRetentionCode:string,
      /**  Reporting1099Name  */  
   Reporting1099Name:string,
      /**  Reporting1099Name2  */  
   Reporting1099Name2:string,
      /**  FATCA  */  
   FATCA:boolean,
      /**  AccountNum  */  
   AccountNum:string,
      /**  TWGUIRegNum  */  
   TWGUIRegNum:string,
      /**  MXTARCode  */  
   MXTARCode:string,
      /**  PEAddressID  */  
   PEAddressID:string,
      /**  PERetentionRegime  */  
   PERetentionRegime:string,
      /**  TaxEntityType  */  
   TaxEntityType:string,
      /**  INGSTComplianceRate  */  
   INGSTComplianceRate:number,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  TINValidationStatus  */  
   TINValidationStatus:number,
      /**  ImporterOfRecord  */  
   ImporterOfRecord:boolean,
      /**  PLAutomaticAPInvoiceNum  */  
   PLAutomaticAPInvoiceNum:boolean,
      /**  SEC  */  
   SEC:string,
      /**  MXDIOTTranType  */  
   MXDIOTTranType:string,
      /**  US1099KMerchCatCode  */  
   US1099KMerchCatCode:string,
      /**  MXTaxpayerType  */  
   MXTaxpayerType:string,
      /**  MXLegalRepRFC  */  
   MXLegalRepRFC:string,
      /**  MXLegalRepCURP  */  
   MXLegalRepCURP:string,
      /**  MXLegalRepName  */  
   MXLegalRepName:string,
      /**  MXLegalRepTaxpayerType  */  
   MXLegalRepTaxpayerType:string,
      /**  US1099State  */  
   US1099State:string,
      /**  TaxValidationStatus  */  
   TaxValidationStatus:number,
      /**  TaxValidationDate  */  
   TaxValidationDate:string,
      /**  HMRCTaxValidationLog  */  
   HMRCTaxValidationLog:string,
      /**  ExternalSchemeID  */  
   ExternalSchemeID:string,
      /**  Municipio Code  */  
   MXMunicipio:string,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  Flag used to mark a Supplier as EDI.  */  
   EDISupplier:boolean,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
   DispVendorID:string,
      /**  The VendorId to link to (new or existing)  */  
   LinkVendorID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbVendorSearchTableset{
   GlbVendor:Erp_Tablesets_GlbVendorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGlbVendorSearchTableset{
   GlbVendor:Erp_Tablesets_GlbVendorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param glbCompany
      @param glbVendorNum
   */  
export interface GetByID_input{
   glbCompany:string,
   glbVendorNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GlbVendorSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GlbVendorSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GlbVendorSearchTableset[],
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
   returnObj:Erp_Tablesets_GlbVendorListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param glbCompany
   */  
export interface GetNewGlbVendor_input{
   ds:Erp_Tablesets_GlbVendorSearchTableset[],
   glbCompany:string,
}

export interface GetNewGlbVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorSearchTableset[],
}
}

   /** Required : 
      @param whereClauseGlbVendor
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGlbVendor:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GlbVendorSearchTableset[],
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
      @param glbCompany
      @param glbVendorNum
      @param ds
   */  
export interface RefreshGlbVendorRow_input{
      /**  Global Company  */  
   glbCompany:string,
      /**  Global Vendor Number  */  
   glbVendorNum:number,
   ds:Erp_Tablesets_GlbVendorSearchTableset[],
}

export interface RefreshGlbVendorRow_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorSearchTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtGlbVendorSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGlbVendorSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GlbVendorSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbVendorSearchTableset[],
}
}

