import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.GlbCustomerSearchSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/$metadata", {
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
   Description: Get GlbCustomerSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCustomerSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCustomerRow
   */  
export function get_GlbCustomerSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustomerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GlbCustomerSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustomerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCustomerSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCustomerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCustomerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbCustomerSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GlbCustomerSearches", {
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
   Summary: Calls GetByID to retrieve the GlbCustomerSearch item
   Description: Calls GetByID to retrieve the GlbCustomerSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCustomerSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbCustNum Desc: GlbCustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCustomerRow
   */  
export function get_GlbCustomerSearches_Company_GlbCompany_GlbCustNum(Company:string, GlbCompany:string, GlbCustNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbCustomerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GlbCustomerSearches(" + Company + "," + GlbCompany + "," + GlbCustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbCustomerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlbCustomerSearch for the service
   Description: Calls UpdateExt to update GlbCustomerSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCustomerSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbCustNum Desc: GlbCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCustomerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlbCustomerSearches_Company_GlbCompany_GlbCustNum(Company:string, GlbCompany:string, GlbCustNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GlbCustomerSearches(" + Company + "," + GlbCompany + "," + GlbCustNum + ")", {
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
   Summary: Call UpdateExt to delete GlbCustomerSearch item
   Description: Call UpdateExt to delete GlbCustomerSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCustomerSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbCustNum Desc: GlbCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlbCustomerSearches_Company_GlbCompany_GlbCustNum(Company:string, GlbCompany:string, GlbCustNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GlbCustomerSearches(" + Company + "," + GlbCompany + "," + GlbCustNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCustomerListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustomerListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustomerListRow)
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
export function get_GetRows(whereClauseGlbCustomer:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGlbCustomer!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlbCustomer=" + whereClauseGlbCustomer
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GetRows" + params, {
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
export function get_GetByID(glbCompany:string, glbCustNum:string, epicorHeaders?:Headers){
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
   if(typeof glbCustNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glbCustNum=" + glbCustNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewGlbCustomer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlbCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GetNewGlbCustomer", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustomerListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbCustomerListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustomerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbCustomerRow[],
}

export interface Erp_Tablesets_GlbCustomerListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the owner company  */  
   "GlbCustID":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the owner company  */  
   "GlbCustNum":number,
   "Name":string,
   "Address1":string,
   "Address2":string,
   "Address3":string,
   "City":string,
   "State":string,
   "Zip":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  Optional field used to record the customer's State Tax Identification number, which is used on Sales Acknowledgments.  */  
   "ResaleID":string,
      /**   Contains the default SalesRep for the specific customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference Orders.
It can be left blank or must be valid in the SalesRep master file.  */  
   "SalesRepCode":string,
      /**  The Sales Territory for the Customer.  */  
   "TerritoryID":string,
      /**  Contains the key of the default ship to for a customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in shipto maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  */  
   "ShipToNum":string,
      /**  Establishes the default sales terms that should be used for this customer. This field can't be left blank, it must be valid in the Terms file. A default may be supplied by XaSyst.TermsCode if not blank.  It supplies the default in Order entry and Invoice entry.  */  
   "TermsCode":string,
      /**  Contains the default ShipVia for a customer. This is an optional field, it can be left blank or it must be valid in the ShipVia master file.  */  
   "ShipViaCode":string,
      /**  Controls the selection for printing of Accounts Receivable statements for a customer.  */  
   "PrintStatements":boolean,
      /**  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  */  
   "PrintLabels":boolean,
      /**   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgments.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know  if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  */  
   "PrintAck":boolean,
      /**  Controls whether or not the customer included in the finance charge calculation process.  */  
   "FinCharges":boolean,
      /**  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   "CreditHold":boolean,
      /**  Customer Group code for a customer.  This can be blank or it must be valid in the CustsGrup file. This field will be used as a sort and selection parameter for reporting.  */  
   "GroupCode":string,
      /**  An optional field used to establish a default purchasing discount percentage for a customer. This value is supplied to order entry as a default for line item discount percent.  */  
   "DiscountPercent":number,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  */  
   "PrimPCon":number,
      /**  The same as the PrimPCon except that this is the Billing contact and this is used as a default in invoice entry.  */  
   "PrimBCon":number,
      /**  Same as PrimPCon except that this the Shipping contact and is used as a default in Packing Slip entry.  */  
   "PrimSCon":number,
      /**   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   "Comment":string,
      /**  The date when they were established as a customer. Use the system date as a default when creating new customers. This is user maintainable.  */  
   "EstDate":string,
      /**  Fax telephone number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  */  
   "FaxNum":string,
      /**  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**  Indicates the reason why  customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  */  
   "TaxExempt":string,
      /**  The ID that establishes link to the default QMarkUp record which provides default markup percents used by quote entry for this customer. This ID is not directly entered. Instead it is derived via the user entering the description of the QMarkUp record. This can be left blank, else must be valid.  */  
   "MarkUpID":string,
      /**   ** 6.0 extended functionality
Represents the day of the week that this customer is billed. The valid values are 0-7 where 0=All,1=Sun,2=Mon,...,7=Sat.  
** (where the bill-frequency = 'W' (weekly)
** (where bill-frequency = 'M' (monthly) this field is 1 -> 31
    representing the day of the month to bill on.
This is used during the "Get Shipments" function of invoice entry. For example, if the customer has BillDay = 4(Wed),  the Get Shipments function will select all the packing slips with a ship date that is less  than or equal to the latest Wednesday's date.
** The same also applies to monthly billing (1-31)  */  
   "BillDay":number,
      /**  "Combine" Multiple Packing Slips into one Invoice.  NOTE: The field name does not correctly represent what this actually does !  This value is used during the "Get Shipments" function of invoice entry to control how invoices should be created when there are multiple packing slips for the same customer. Basically, if this value is YES then packing slips for the same Order, Fiscal Period are combined into a single invoice. If this value is NO then each packing slip will create a single invoice.  */  
   "OneInvPerPS":boolean,
      /**  Default FOB policy for a customers orders.  Order Entry uses this as a default to OrderHed.FOB.  */  
   "DefaultFOB":string,
      /**  Indicates that Open Orders are to be included in the credit limit checking. This checkbox will also include open service contracts.  */  
   "CreditIncludeOrders":boolean,
      /**  Date that the next credit check should be made for that customer.  */  
   "CreditReviewDate":string,
   "CreditHoldDate":string,
   "CreditHoldSource":string,
   "CreditClearUserID":string,
   "CreditClearDate":string,
   "CreditClearTime":string,
      /**  This is the Trading Partner ID that is used for incoming and outgoing EDI.  */  
   "EDICode":string,
      /**  EDI test mode.  When customers are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  */  
   "EDITest":boolean,
      /**  Identifies which EDI package the customer is using.  If not null in must be valid in the EDITrnsl table.  */  
   "EDITranslator":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   "LangNameID":string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   "BorderCrossing":string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   "FormatStr":string,
   "BTName":string,
   "BTAddress1":string,
   "BTAddress2":string,
   "BTAddress3":string,
   "BTCity":string,
   "BTState":string,
   "BTZip":string,
      /**  Country part of Bill-to address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   "BTCountryNum":number,
      /**  Country is used as part of the bill-to address. It can be left blank.  */  
   "BTCountry":string,
      /**  The bill-to address Phone Number for the customer.  */  
   "BTPhoneNum":string,
      /**  The bill-to address Fax telephone number for the customer. Optional field.  */  
   "BTFaxNum":string,
      /**  Optional bill-to address format.  Controls the address format used on crystal forms.  */  
   "BTFormatStr":string,
      /**  The unique Customer Number of the Parent.  */  
   "ParentCustNum":number,
   "TaxRegionCode":string,
      /**  This is an inter-company customer.  */  
   "ICCust":boolean,
      /**  The day of the month that service contracts that are marked for recurring invoices are billed for this customer.  If the Invoice group invoice date is greater than or equal to this date then the invoice will be generated.  */  
   "ContBillDay":number,
      /**  Email address of the customer.  */  
   "EMailAddress":string,
      /**  Indicates if the customer has any qualifications on completeness of the order before it can be shipped. The valid values are; "O" - Order must be 100% complete,  "L" - Order Line must be 100% complete, "blank" - None.  This setting is a default for orders of a specific customer. See OrderHed.ShipOrderComplete, OrderDtl.ShipLineComplete  */  
   "ShippingQualifier":string,
      /**  Code used to relate a AllocPri record to the customer.  This is used as a default to OrderHed.AllocPriCode for order for this customer.  */  
   "AllocPriorityCode":string,
      /**  Used with Global alerts  */  
   "LinkPortNum":number,
      /**  Indicates if this customer is for eCommerce.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and StoreFront DB (VntgSF).  */  
   "WebCustomer":boolean,
      /**   Describe the type of Customer this is.
SUS = Suspect
PRO =  Prospect
CUS = Customer  */  
   "CustomerType":string,
      /**  Indicates that this contact is not included in marketing lists  */  
   "NoContact":boolean,
      /**  This customers territory cannot be changed by any process that changes territories  */  
   "TerritoryLock":boolean,
      /**  Customers Website URL .  */  
   "CustURL":string,
      /**  The sales territory that the system will assign based on new values in the Sales territory boundary table.  */  
   "PendingTerritoryID":string,
   "ExtID":string,
      /**  APK - added for consolidation accross multiple SO's for the same customer  */  
   "ConsolidateSO":boolean,
      /**  BillFrequency  */  
   "BillFrequency":string,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   "CreditIncludePI":boolean,
      /**  Marks the customer as a global customer, available to be sent out to other companies  */  
   "GlobalCust":boolean,
      /**  Owner Company Identifier.  */  
   "GlbCompany":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   "CustID":string,
      /**  Indicates if this customer participates in the Inter-Company Trading.  */  
   "ICTrader":boolean,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   "CustNum":number,
      /**  Indicates that Open Orders are to be included in the global credit limit checking. This checkbox will also include open service contracts.  */  
   "GlobalCredIncOrd":boolean,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   "GlobalCredIncPI":boolean,
      /**  A unique code that identifies the currency.  */  
   "GlobalCurrencyCode":string,
      /**  Indicates if customer has been placed into a "Global Credit Hold" status. Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  */  
   "GlobalCreditHold":string,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   "OldCompany":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  */  
   "OldCustNum":number,
      /**  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  */  
   "OldCustID":string,
      /**  Establishes the tax authority for this customer.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   "TaxAuthorityCode":string,
      /**  This flag indicates if an external delivery note is required for the customer.  This field is available only when send shipments for financial integration is turned on.  This will provide the default for the ShipHead record.  */  
   "ExternalDeliveryNote":boolean,
   "ExternalID":string,
   "CheckDuplicatePO":boolean,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit.  Credit limit of zero is considered as having unlimited credit.  */  
   "CreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   "CustPILimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit.  */  
   "GlobalCreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   "GlobalPILimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  */  
   "DocGlobalCreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  */  
   "DocGlobalPILimit":number,
      /**  Indicates whether RFQ Attachments are allowed for this Customer  */  
   "RfqAttachAllow":boolean,
      /**   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based discount.
"ADD" = means that the customer could get the order value based discount in addition to the default order discount.  */  
   "DiscountQualifier":string,
      /**  Indicates if the user chose to skip this record when linking global customers.  The user can come back at a later time and choose to link a skipped customer if they need to.  */  
   "Skipped":boolean,
   "AllowAltBillTo":boolean,
   "ApplyChrg":boolean,
   "ChrgAmount":number,
   "COD":boolean,
   "CODAmount":number,
   "CODCheck":boolean,
   "CODFreight":boolean,
   "DeclaredAmt":number,
   "DeclaredIns":boolean,
   "DemandAddAction":string,
   "DemandAddLeadTime":number,
   "DemandAutoAccept":boolean,
   "DemandCancelAction":string,
   "DemandCancelLeadTime":number,
   "DemandChangeAction":string,
   "DemandChangeDateAction":string,
   "DemandChangeDateLeadTime":number,
   "DemandChangeLeadTime":number,
   "DemandDateType":string,
   "DemandDayOfWeek":number,
   "DemandDeliveryDays":number,
   "DemandNewLineAction":string,
   "DemandNewLineLeadTime":number,
   "DemandQtyChangeAction":string,
   "DemandQtyChangeLeadTime":number,
   "DemandUseSysDate":boolean,
   "DocOnly":boolean,
   "GroundType":string,
   "Hazmat":boolean,
   "NotifyEMail":string,
   "NotifyFlag":boolean,
   "RefNotes":string,
   "ResDelivery":boolean,
   "SatDelivery":boolean,
   "SatPickup":boolean,
   "TradingPartnerName":string,
   "VerbalConf":boolean,
   "PeriodicityCode":number,
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
   "CreditDays":number,
   "EarlyBuffer":number,
   "LateBuffer":number,
   "OverrideCarrier":boolean,
   "OverrideService":boolean,
   "DemandUnitPriceDiff":boolean,
   "DemandUnitPriceDiffAction":string,
   "AddressVal":boolean,
   "ExcFromVal":boolean,
   "RebateForm":string,
   "RebateVendorNum":number,
   "CreditCardOrder":boolean,
   "DemandCheckForPart":boolean,
   "DemandCheckForPartAction":string,
   "ChangeDate":string,
   "ChangedBy":string,
   "ChangeTime":number,
   "ChargeCode":string,
   "AddlHdlgFlag":boolean,
   "CertOfOrigin":boolean,
   "CommercialInvoice":boolean,
   "DeliveryConf":number,
   "ETCAddrChg":boolean,
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
   "ARCreditTotal":number,
   "PICreditTotal":number,
   "SOCreditTotal":number,
   "TaxMethod":string,
   "TaxRoundRule":number,
   "AcrossNatAcc":boolean,
   "NACreditIsShare":boolean,
   "NACreditPreferenceList":string,
   "NACreditSharedPrc":number,
   "NAParentCreditIsUsed":boolean,
   "NAParentCreditPrc":number,
   "OverrideRlsClass":boolean,
   "ValidPayer":boolean,
   "ValidShipTo":boolean,
   "ValidSoldTo":boolean,
   "AllowOTS":boolean,
   "ManagedVendID":string,
   "ManagedVendNum":number,
   "ThirdPLCust":boolean,
   "NARlsClassCode":string,
   "AutoGenPromNotes":boolean,
   "DirectDebiting":boolean,
   "PartPayment":boolean,
   "ReservePriorityCode":string,
   "NAParentsCreditUsed":number,
   "NASharedCreditUsed":number,
   "NAOwnCreditUsed":number,
   "GlbNACreditIsShare":boolean,
   "GlbNACreditSharedPrc":number,
   "GlbNAParentCreditIsUsed":boolean,
   "GlbNAParentCreditPrc":number,
   "GlbNAParentsCreditUsed":number,
   "GlbNASharedCreditUsed":number,
   "ReminderCode":string,
   "AllowShipTo3":boolean,
   "NACreditUpdate":string,
   "OTSSaveAs":string,
   "CustPartOpts":string,
   "HasBank":boolean,
   "PMUID":number,
   "DemandCheckForRev":boolean,
   "DemandCheckForRevAction":string,
   "OrderHoldForReview":boolean,
   "ShipToTerrList":string,
   "AcctRefNumber":string,
   "DemandCheckCUMM":boolean,
   "DemandCheckCUMMAction":string,
   "DemandCloseNoMatch":boolean,
   "DemandCloseRejSkd":boolean,
   "DemandPricing":string,
   "DmdCheckPartialShip":boolean,
   "DmdCheckShipAction":string,
   "InvPerPackLine":boolean,
   "LegalName":string,
   "OrgRegCode":string,
   "OurBankCode":string,
      /**  Defines the tolerance for price difference validations  */  
   "PriceTolerance":number,
   "TaxRegReason":string,
   "CheckConfirmCapPromise":boolean,
   "CheckDateCapPromise":boolean,
   "CheckUpdateCapPromise":boolean,
   "DemandCapPromiseAction":string,
   "DemandCapPromiseDate":string,
   "DemandCapPromiseUpdate":string,
   "DemandSplitSched":boolean,
   "DueDateCriteria":string,
   "ERSOrder":boolean,
   "PBTerms":number,
   "PeriodicBilling":boolean,
   "PreferredBank":string,
   "SICCode":number,
   "ICCode":string,
   "OTSmartString":boolean,
   "DeferredRev":boolean,
   "RACode":string,
   "DemandCheckCfgAction":string,
   "DemandCheckConfig":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Customer.CustID to link to (new or existing)  */  
   "LinkCustID":string,
   "DisplayHold":string,
   "DisplayCustomerType":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbCustomerRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the owner company  */  
   "GlbCustID":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the owner company  */  
   "GlbCustNum":number,
   "Name":string,
   "Address1":string,
   "Address2":string,
   "Address3":string,
   "City":string,
   "State":string,
   "Zip":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  Optional field used to record the customer's State Tax Identification number, which is used on Sales Acknowledgments.  */  
   "ResaleID":string,
      /**   Contains the default SalesRep for the specific customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference Orders.
It can be left blank or must be valid in the SalesRep master file.  */  
   "SalesRepCode":string,
      /**  The Sales Territory for the Customer.  */  
   "TerritoryID":string,
      /**  Contains the key of the default ship to for a customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in shipto maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  */  
   "ShipToNum":string,
      /**  Establishes the default sales terms that should be used for this customer. This field can't be left blank, it must be valid in the Terms file. A default may be supplied by XaSyst.TermsCode if not blank.  It supplies the default in Order entry and Invoice entry.  */  
   "TermsCode":string,
      /**  Contains the default ShipVia for a customer. This is an optional field, it can be left blank or it must be valid in the ShipVia master file.  */  
   "ShipViaCode":string,
      /**  Controls the selection for printing of Accounts Receivable statements for a customer.  */  
   "PrintStatements":boolean,
      /**  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  */  
   "PrintLabels":boolean,
      /**   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgments.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know  if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  */  
   "PrintAck":boolean,
      /**  Controls whether or not the customer included in the finance charge calculation process.  */  
   "FinCharges":boolean,
      /**  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   "CreditHold":boolean,
      /**  Customer Group code for a customer.  This can be blank or it must be valid in the CustsGrup file. This field will be used as a sort and selection parameter for reporting.  */  
   "GroupCode":string,
      /**  An optional field used to establish a default purchasing discount percentage for a customer. This value is supplied to order entry as a default for line item discount percent.  */  
   "DiscountPercent":number,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  */  
   "PrimPCon":number,
      /**  The same as the PrimPCon except that this is the Billing contact and this is used as a default in invoice entry.  */  
   "PrimBCon":number,
      /**  Same as PrimPCon except that this the Shipping contact and is used as a default in Packing Slip entry.  */  
   "PrimSCon":number,
      /**   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   "Comment":string,
      /**  The date when they were established as a customer. Use the system date as a default when creating new customers. This is user maintainable.  */  
   "EstDate":string,
      /**  Fax telephone number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  */  
   "FaxNum":string,
      /**  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  */  
   "PhoneNum":string,
      /**  Indicates the reason why  customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  */  
   "TaxExempt":string,
      /**  The ID that establishes link to the default QMarkUp record which provides default markup percents used by quote entry for this customer. This ID is not directly entered. Instead it is derived via the user entering the description of the QMarkUp record. This can be left blank, else must be valid.  */  
   "MarkUpID":string,
      /**   ** 6.0 extended functionality
Represents the day of the week that this customer is billed. The valid values are 0-7 where 0=All,1=Sun,2=Mon,...,7=Sat.  
** (where the bill-frequency = 'W' (weekly)
** (where bill-frequency = 'M' (monthly) this field is 1 -> 31
    representing the day of the month to bill on.
This is used during the "Get Shipments" function of invoice entry. For example, if the customer has BillDay = 4(Wed),  the Get Shipments function will select all the packing slips with a ship date that is less  than or equal to the latest Wednesday's date.
** The same also applies to monthly billing (1-31)  */  
   "BillDay":number,
      /**  "Combine" Multiple Packing Slips into one Invoice.  NOTE: The field name does not correctly represent what this actually does !  This value is used during the "Get Shipments" function of invoice entry to control how invoices should be created when there are multiple packing slips for the same customer. Basically, if this value is YES then packing slips for the same Order, Fiscal Period are combined into a single invoice. If this value is NO then each packing slip will create a single invoice.  */  
   "OneInvPerPS":boolean,
      /**  Default FOB policy for a customers orders.  Order Entry uses this as a default to OrderHed.FOB.  */  
   "DefaultFOB":string,
      /**  Indicates that Open Orders are to be included in the credit limit checking. This checkbox will also include open service contracts.  */  
   "CreditIncludeOrders":boolean,
      /**  Date that the next credit check should be made for that customer.  */  
   "CreditReviewDate":string,
   "CreditHoldDate":string,
   "CreditHoldSource":string,
   "CreditClearUserID":string,
   "CreditClearDate":string,
   "CreditClearTime":string,
      /**  This is the Trading Partner ID that is used for incoming and outgoing EDI.  */  
   "EDICode":string,
      /**  EDI test mode.  When customers are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  */  
   "EDITest":boolean,
      /**  Identifies which EDI package the customer is using.  If not null in must be valid in the EDITrnsl table.  */  
   "EDITranslator":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   "LangNameID":string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   "BorderCrossing":string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   "FormatStr":string,
   "BTName":string,
   "BTAddress1":string,
   "BTAddress2":string,
   "BTAddress3":string,
   "BTCity":string,
   "BTState":string,
   "BTZip":string,
      /**  Country part of Bill-to address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   "BTCountryNum":number,
      /**  Country is used as part of the bill-to address. It can be left blank.  */  
   "BTCountry":string,
      /**  The bill-to address Phone Number for the customer.  */  
   "BTPhoneNum":string,
      /**  The bill-to address Fax telephone number for the customer. Optional field.  */  
   "BTFaxNum":string,
      /**  Optional bill-to address format.  Controls the address format used on crystal forms.  */  
   "BTFormatStr":string,
      /**  The unique Customer Number of the Parent.  */  
   "ParentCustNum":number,
   "TaxRegionCode":string,
      /**  This is an inter-company customer.  */  
   "ICCust":boolean,
      /**  The day of the month that service contracts that are marked for recurring invoices are billed for this customer.  If the Invoice group invoice date is greater than or equal to this date then the invoice will be generated.  */  
   "ContBillDay":number,
      /**  Email address of the customer.  */  
   "EMailAddress":string,
      /**  Indicates if the customer has any qualifications on completeness of the order before it can be shipped. The valid values are; "O" - Order must be 100% complete,  "L" - Order Line must be 100% complete, "blank" - None.  This setting is a default for orders of a specific customer. See OrderHed.ShipOrderComplete, OrderDtl.ShipLineComplete  */  
   "ShippingQualifier":string,
      /**  Code used to relate a AllocPri record to the customer.  This is used as a default to OrderHed.AllocPriCode for order for this customer.  */  
   "AllocPriorityCode":string,
      /**  Used with Global alerts  */  
   "LinkPortNum":number,
      /**  Indicates if this customer is for eCommerce.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and StoreFront DB (VntgSF).  */  
   "WebCustomer":boolean,
      /**   Describe the type of Customer this is.
SUS = Suspect
PRO =  Prospect
CUS = Customer  */  
   "CustomerType":string,
      /**  Indicates that this contact is not included in marketing lists  */  
   "NoContact":boolean,
      /**  This customers territory cannot be changed by any process that changes territories  */  
   "TerritoryLock":boolean,
      /**  Customers Website URL .  */  
   "CustURL":string,
      /**  The sales territory that the system will assign based on new values in the Sales territory boundary table.  */  
   "PendingTerritoryID":string,
   "ExtID":string,
      /**  APK - added for consolidation accross multiple SO's for the same customer  */  
   "ConsolidateSO":boolean,
      /**  BillFrequency  */  
   "BillFrequency":string,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   "CreditIncludePI":boolean,
      /**  Marks the customer as a global customer, available to be sent out to other companies  */  
   "GlobalCust":boolean,
      /**  Owner Company Identifier.  */  
   "GlbCompany":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   "CustID":string,
      /**  Indicates if this customer participates in the Inter-Company Trading.  */  
   "ICTrader":boolean,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   "CustNum":number,
      /**  Indicates that Open Orders are to be included in the global credit limit checking. This checkbox will also include open service contracts.  */  
   "GlobalCredIncOrd":boolean,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   "GlobalCredIncPI":boolean,
      /**  A unique code that identifies the currency.  */  
   "GlobalCurrencyCode":string,
      /**  Indicates if customer has been placed into a "Global Credit Hold" status. Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  */  
   "GlobalCreditHold":string,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   "OldCompany":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  */  
   "OldCustNum":number,
      /**  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  */  
   "OldCustID":string,
      /**  Establishes the tax authority for this customer.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   "TaxAuthorityCode":string,
      /**  This flag indicates if an external delivery note is required for the customer.  This field is available only when send shipments for financial integration is turned on.  This will provide the default for the ShipHead record.  */  
   "ExternalDeliveryNote":boolean,
   "ExternalID":string,
   "CheckDuplicatePO":boolean,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit.  Credit limit of zero is considered as having unlimited credit.  */  
   "CreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   "CustPILimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit.  */  
   "GlobalCreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   "GlobalPILimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  */  
   "DocGlobalCreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  */  
   "DocGlobalPILimit":number,
      /**  Indicates whether RFQ Attachments are allowed for this Customer  */  
   "RfqAttachAllow":boolean,
      /**   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based discount.
"ADD" = means that the customer could get the order value based discount in addition to the default order discount.  */  
   "DiscountQualifier":string,
      /**  Indicates if the user chose to skip this record when linking global customers.  The user can come back at a later time and choose to link a skipped customer if they need to.  */  
   "Skipped":boolean,
   "AllowAltBillTo":boolean,
   "ApplyChrg":boolean,
   "ChrgAmount":number,
   "COD":boolean,
   "CODAmount":number,
   "CODCheck":boolean,
   "CODFreight":boolean,
   "DeclaredAmt":number,
   "DeclaredIns":boolean,
   "DemandAddAction":string,
   "DemandAddLeadTime":number,
   "DemandAutoAccept":boolean,
   "DemandCancelAction":string,
   "DemandCancelLeadTime":number,
   "DemandChangeAction":string,
   "DemandChangeDateAction":string,
   "DemandChangeDateLeadTime":number,
   "DemandChangeLeadTime":number,
   "DemandDateType":string,
   "DemandDayOfWeek":number,
   "DemandDeliveryDays":number,
   "DemandNewLineAction":string,
   "DemandNewLineLeadTime":number,
   "DemandQtyChangeAction":string,
   "DemandQtyChangeLeadTime":number,
   "DemandUseSysDate":boolean,
   "DocOnly":boolean,
   "GroundType":string,
   "Hazmat":boolean,
   "NotifyEMail":string,
   "NotifyFlag":boolean,
   "RefNotes":string,
   "ResDelivery":boolean,
   "SatDelivery":boolean,
   "SatPickup":boolean,
   "TradingPartnerName":string,
   "VerbalConf":boolean,
   "PeriodicityCode":number,
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
   "CreditDays":number,
   "EarlyBuffer":number,
   "LateBuffer":number,
   "OverrideCarrier":boolean,
   "OverrideService":boolean,
   "DemandUnitPriceDiff":boolean,
   "DemandUnitPriceDiffAction":string,
   "AddressVal":boolean,
   "ExcFromVal":boolean,
   "RebateForm":string,
   "RebateVendorNum":number,
   "CreditCardOrder":boolean,
   "DemandCheckForPart":boolean,
   "DemandCheckForPartAction":string,
   "ChangeDate":string,
   "ChangedBy":string,
   "ChangeTime":number,
   "ChargeCode":string,
   "AddlHdlgFlag":boolean,
   "CertOfOrigin":boolean,
   "CommercialInvoice":boolean,
   "DeliveryConf":number,
   "ETCAddrChg":boolean,
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
   "ARCreditTotal":number,
   "PICreditTotal":number,
   "SOCreditTotal":number,
   "TaxMethod":string,
   "TaxRoundRule":number,
   "AcrossNatAcc":boolean,
   "NACreditIsShare":boolean,
   "NACreditPreferenceList":string,
   "NACreditSharedPrc":number,
   "NAParentCreditIsUsed":boolean,
   "NAParentCreditPrc":number,
   "OverrideRlsClass":boolean,
   "ValidPayer":boolean,
   "ValidShipTo":boolean,
   "ValidSoldTo":boolean,
   "AllowOTS":boolean,
   "ManagedVendID":string,
   "ManagedVendNum":number,
   "ThirdPLCust":boolean,
   "NARlsClassCode":string,
   "AutoGenPromNotes":boolean,
   "DirectDebiting":boolean,
   "PartPayment":boolean,
   "ReservePriorityCode":string,
   "NAParentsCreditUsed":number,
   "NASharedCreditUsed":number,
   "NAOwnCreditUsed":number,
   "GlbNACreditIsShare":boolean,
   "GlbNACreditSharedPrc":number,
   "GlbNAParentCreditIsUsed":boolean,
   "GlbNAParentCreditPrc":number,
   "GlbNAParentsCreditUsed":number,
   "GlbNASharedCreditUsed":number,
   "ReminderCode":string,
   "AllowShipTo3":boolean,
   "NACreditUpdate":string,
   "OTSSaveAs":string,
   "CustPartOpts":string,
   "HasBank":boolean,
   "PMUID":number,
   "DemandCheckForRev":boolean,
   "DemandCheckForRevAction":string,
   "OrderHoldForReview":boolean,
   "ShipToTerrList":string,
   "AcctRefNumber":string,
   "DemandCheckCUMM":boolean,
   "DemandCheckCUMMAction":string,
   "DemandCloseNoMatch":boolean,
   "DemandCloseRejSkd":boolean,
   "DemandPricing":string,
   "DmdCheckPartialShip":boolean,
   "DmdCheckShipAction":string,
   "InvPerPackLine":boolean,
   "LegalName":string,
   "OrgRegCode":string,
   "OurBankCode":string,
      /**  Defines the tolerance for price difference validations  */  
   "PriceTolerance":number,
   "TaxRegReason":string,
   "CheckConfirmCapPromise":boolean,
   "CheckDateCapPromise":boolean,
   "CheckUpdateCapPromise":boolean,
   "DemandCapPromiseAction":string,
   "DemandCapPromiseDate":string,
   "DemandCapPromiseUpdate":string,
   "DemandSplitSched":boolean,
   "DueDateCriteria":string,
   "ERSOrder":boolean,
   "PBTerms":number,
   "PeriodicBilling":boolean,
   "PreferredBank":string,
   "SICCode":number,
   "ICCode":string,
   "OTSmartString":boolean,
   "DeferredRev":boolean,
   "RACode":string,
   "DemandCheckCfgAction":string,
   "DemandCheckConfig":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  THBranchID  */  
   "THBranchID":string,
      /**  CustPricingSchema  */  
   "CustPricingSchema":string,
      /**  ParamCode  */  
   "ParamCode":string,
      /**  AGAFIPResponsibilityCode  */  
   "AGAFIPResponsibilityCode":string,
      /**  AGBillToProvinceCode  */  
   "AGBillToProvinceCode":string,
      /**  AGGrossIncomeTaxID  */  
   "AGGrossIncomeTaxID":string,
      /**  AGIDDocTypeCode  */  
   "AGIDDocTypeCode":string,
      /**  AGIDDocumentNumber  */  
   "AGIDDocumentNumber":string,
      /**  AGProvinceCode  */  
   "AGProvinceCode":string,
      /**  AGUseGoodDefaultMark  */  
   "AGUseGoodDefaultMark":boolean,
      /**  Collections  */  
   "Collections":boolean,
      /**  CollectionsDate  */  
   "CollectionsDate":string,
      /**  DateCollectionPosted  */  
   "DateCollectionPosted":string,
      /**  MXMunicipio  */  
   "MXMunicipio":string,
      /**  PEIdentityDocType  */  
   "PEIdentityDocType":string,
      /**  PEDocumentID  */  
   "PEDocumentID":string,
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
      /**  EntityUseCode  */  
   "EntityUseCode":string,
      /**  InvcOrderCmpDflt  */  
   "InvcOrderCmpDflt":boolean,
      /**  EInvoice  */  
   "EInvoice":boolean,
      /**  RegistrationCode  */  
   "RegistrationCode":string,
      /**  EAddress  */  
   "EAddress":string,
      /**  DemandCheckForRunOutPart  */  
   "DemandCheckForRunOutPart":boolean,
      /**  DemandCheckForRunOutPartAction  */  
   "DemandCheckForRunOutPartAction":string,
      /**  EInvCompanyIDAttr  */  
   "EInvCompanyIDAttr":string,
      /**  INCSTNumber  */  
   "INCSTNumber":string,
      /**  INPANNumber  */  
   "INPANNumber":string,
      /**  COOneTimeID  */  
   "COOneTimeID":string,
      /**  COIsOneTimeCust  */  
   "COIsOneTimeCust":boolean,
      /**  DEOrgType  */  
   "DEOrgType":string,
      /**  PEGuaranteeName  */  
   "PEGuaranteeName":string,
      /**  PEGuaranteeAddress1  */  
   "PEGuaranteeAddress1":string,
      /**  PEGuaranteeAddress2  */  
   "PEGuaranteeAddress2":string,
      /**  PEGuaranteeAddress3  */  
   "PEGuaranteeAddress3":string,
      /**  PEGuaranteeCity  */  
   "PEGuaranteeCity":string,
      /**  PEGuaranteeState  */  
   "PEGuaranteeState":string,
      /**  PEGuaranteeZip  */  
   "PEGuaranteeZip":string,
      /**  PEGuaranteeCountry  */  
   "PEGuaranteeCountry":string,
      /**  PEGuaranteePhoneNum  */  
   "PEGuaranteePhoneNum":string,
      /**  PEGuaranteeTaxID  */  
   "PEGuaranteeTaxID":string,
      /**  OurSupplierCode  */  
   "OurSupplierCode":string,
      /**  ECCType  */  
   "ECCType":string,
      /**  MYIndustryCode  */  
   "MYIndustryCode":string,
      /**  SyncToExternalCRM  */  
   "SyncToExternalCRM":boolean,
      /**  ExternalCRMGlbCustomerID  */  
   "ExternalCRMGlbCustomerID":string,
      /**  ExternalCRMGlbCustomerType  */  
   "ExternalCRMGlbCustomerType":string,
      /**  ExternalCRMLastSync  */  
   "ExternalCRMLastSync":string,
      /**  ExternalCRMSyncRequired  */  
   "ExternalCRMSyncRequired":boolean,
      /**  Ownership  */  
   "Ownership":string,
      /**  Industry  */  
   "Industry":string,
      /**  AnnualRevenue  */  
   "AnnualRevenue":number,
      /**  NumberOfEmployees  */  
   "NumberOfEmployees":number,
      /**  TickerLocation  */  
   "TickerLocation":string,
      /**  TickerSymbol  */  
   "TickerSymbol":string,
      /**  Rating  */  
   "Rating":string,
      /**  TWGUIRegNum  */  
   "TWGUIRegNum":string,
      /**  MXAccountNumber  */  
   "MXAccountNumber":string,
      /**  ConsolidateLinesPerPart  */  
   "ConsolidateLinesPerPart":boolean,
      /**  TWTaxPayerType  */  
   "TWTaxPayerType":number,
      /**  TWDeductGUIFormatCode  */  
   "TWDeductGUIFormatCode":string,
      /**  MXCURP  */  
   "MXCURP":string,
      /**  PEAddressID  */  
   "PEAddressID":string,
      /**  PEPerceptionRegime  */  
   "PEPerceptionRegime":string,
      /**  TaxEntityType  */  
   "TaxEntityType":string,
      /**  INGSTComplianceRate  */  
   "INGSTComplianceRate":number,
      /**  INTaxRegistrationID  */  
   "INTaxRegistrationID":string,
      /**  MXPurchaseType  */  
   "MXPurchaseType":string,
      /**  SendToFSA  */  
   "SendToFSA":boolean,
      /**  MXGeneralPublic  */  
   "MXGeneralPublic":boolean,
      /**  AgingCreditHold  */  
   "AgingCreditHold":boolean,
      /**  AgingCreditHoldDate  */  
   "AgingCreditHoldDate":string,
      /**  AgingCreditHoldSource  */  
   "AgingCreditHoldSource":string,
      /**  AgingCreditClearUserID  */  
   "AgingCreditClearUserID":string,
      /**  AgingCreditClearDate  */  
   "AgingCreditClearDate":string,
      /**  AgingCreditCode  */  
   "AgingCreditCode":string,
      /**  ImporterOfRecord  */  
   "ImporterOfRecord":boolean,
      /**  SEC  */  
   "SEC":string,
      /**  EInvEndpointIDAttr  */  
   "EInvEndpointIDAttr":string,
      /**  Indicates whether sales orders from this sold to customer should be treated as Blind Shipments by Manifest.  */  
   "UseBlindShipping":boolean,
      /**  ELIEinvoice  */  
   "ELIEinvoice":boolean,
      /**  ELIDefReportID  */  
   "ELIDefReportID":string,
      /**  ELIDefStyleNum  */  
   "ELIDefStyleNum":number,
      /**  ELIDefToMail  */  
   "ELIDefToMail":string,
      /**  ELIDefCCMail  */  
   "ELIDefCCMail":string,
      /**  ELIDefMailTempID  */  
   "ELIDefMailTempID":string,
      /**  ELISendMail  */  
   "ELISendMail":boolean,
      /**  COFiscalResp1  */  
   "COFiscalResp1":string,
      /**  COFiscalResp2  */  
   "COFiscalResp2":string,
      /**  COFiscalResp3  */  
   "COFiscalResp3":string,
      /**  COOperType  */  
   "COOperType":string,
      /**  Central Collection  */  
   "CentralCollection":boolean,
      /**  NettingVendorNum  */  
   "NettingVendorNum":number,
      /**  EORINumber  */  
   "EORINumber":string,
      /**  AGIsElectronicCreditInvEligible  */  
   "AGIsElectronicCreditInvEligible":boolean,
      /**  TaxValidationStatus  */  
   "TaxValidationStatus":number,
      /**  TaxValidationDate  */  
   "TaxValidationDate":string,
      /**  HMRCTaxValidationLog  */  
   "HMRCTaxValidationLog":string,
      /**  Inactive  */  
   "Inactive":boolean,
      /**  ExternalSchemeID  */  
   "ExternalSchemeID":string,
      /**  ELIOperatorCode  */  
   "ELIOperatorCode":string,
      /**  ELISendingOption  */  
   "ELISendingOption":number,
      /**  ELIOperatorID  */  
   "ELIOperatorID":string,
      /**  EInvExternalID  */  
   "EInvExternalID":string,
      /**  MXTaxRegime  */  
   "MXTaxRegime":string,
      /**  ExclusionMonth  */  
   "ExclusionMonth":number,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  FSMRegionCode  */  
   "FSMRegionCode":string,
      /**  FSMArea  */  
   "FSMArea":string,
      /**  ELIRcptDefStyleNum  */  
   "ELIRcptDefStyleNum":number,
      /**  CovenantDiscPercent  */  
   "CovenantDiscPercent":number,
   "DisplayCustomerType":string,
      /**  Customer.CustID to link to (new or existing)  */  
   "LinkCustID":string,
   "DisplayHold":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param glbCompany
      @param glbCustNum
   */  
export interface DeleteByID_input{
   glbCompany:string,
   glbCustNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GlbCustomerListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the owner company  */  
   GlbCustID:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the owner company  */  
   GlbCustNum:number,
   Name:string,
   Address1:string,
   Address2:string,
   Address3:string,
   City:string,
   State:string,
   Zip:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  Optional field used to record the customer's State Tax Identification number, which is used on Sales Acknowledgments.  */  
   ResaleID:string,
      /**   Contains the default SalesRep for the specific customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference Orders.
It can be left blank or must be valid in the SalesRep master file.  */  
   SalesRepCode:string,
      /**  The Sales Territory for the Customer.  */  
   TerritoryID:string,
      /**  Contains the key of the default ship to for a customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in shipto maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  */  
   ShipToNum:string,
      /**  Establishes the default sales terms that should be used for this customer. This field can't be left blank, it must be valid in the Terms file. A default may be supplied by XaSyst.TermsCode if not blank.  It supplies the default in Order entry and Invoice entry.  */  
   TermsCode:string,
      /**  Contains the default ShipVia for a customer. This is an optional field, it can be left blank or it must be valid in the ShipVia master file.  */  
   ShipViaCode:string,
      /**  Controls the selection for printing of Accounts Receivable statements for a customer.  */  
   PrintStatements:boolean,
      /**  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  */  
   PrintLabels:boolean,
      /**   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgments.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know  if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  */  
   PrintAck:boolean,
      /**  Controls whether or not the customer included in the finance charge calculation process.  */  
   FinCharges:boolean,
      /**  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   CreditHold:boolean,
      /**  Customer Group code for a customer.  This can be blank or it must be valid in the CustsGrup file. This field will be used as a sort and selection parameter for reporting.  */  
   GroupCode:string,
      /**  An optional field used to establish a default purchasing discount percentage for a customer. This value is supplied to order entry as a default for line item discount percent.  */  
   DiscountPercent:number,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  */  
   PrimPCon:number,
      /**  The same as the PrimPCon except that this is the Billing contact and this is used as a default in invoice entry.  */  
   PrimBCon:number,
      /**  Same as PrimPCon except that this the Shipping contact and is used as a default in Packing Slip entry.  */  
   PrimSCon:number,
      /**   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   Comment:string,
      /**  The date when they were established as a customer. Use the system date as a default when creating new customers. This is user maintainable.  */  
   EstDate:string,
      /**  Fax telephone number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  */  
   FaxNum:string,
      /**  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  Indicates the reason why  customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  */  
   TaxExempt:string,
      /**  The ID that establishes link to the default QMarkUp record which provides default markup percents used by quote entry for this customer. This ID is not directly entered. Instead it is derived via the user entering the description of the QMarkUp record. This can be left blank, else must be valid.  */  
   MarkUpID:string,
      /**   ** 6.0 extended functionality
Represents the day of the week that this customer is billed. The valid values are 0-7 where 0=All,1=Sun,2=Mon,...,7=Sat.  
** (where the bill-frequency = 'W' (weekly)
** (where bill-frequency = 'M' (monthly) this field is 1 -> 31
    representing the day of the month to bill on.
This is used during the "Get Shipments" function of invoice entry. For example, if the customer has BillDay = 4(Wed),  the Get Shipments function will select all the packing slips with a ship date that is less  than or equal to the latest Wednesday's date.
** The same also applies to monthly billing (1-31)  */  
   BillDay:number,
      /**  "Combine" Multiple Packing Slips into one Invoice.  NOTE: The field name does not correctly represent what this actually does !  This value is used during the "Get Shipments" function of invoice entry to control how invoices should be created when there are multiple packing slips for the same customer. Basically, if this value is YES then packing slips for the same Order, Fiscal Period are combined into a single invoice. If this value is NO then each packing slip will create a single invoice.  */  
   OneInvPerPS:boolean,
      /**  Default FOB policy for a customers orders.  Order Entry uses this as a default to OrderHed.FOB.  */  
   DefaultFOB:string,
      /**  Indicates that Open Orders are to be included in the credit limit checking. This checkbox will also include open service contracts.  */  
   CreditIncludeOrders:boolean,
      /**  Date that the next credit check should be made for that customer.  */  
   CreditReviewDate:string,
   CreditHoldDate:string,
   CreditHoldSource:string,
   CreditClearUserID:string,
   CreditClearDate:string,
   CreditClearTime:string,
      /**  This is the Trading Partner ID that is used for incoming and outgoing EDI.  */  
   EDICode:string,
      /**  EDI test mode.  When customers are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  */  
   EDITest:boolean,
      /**  Identifies which EDI package the customer is using.  If not null in must be valid in the EDITrnsl table.  */  
   EDITranslator:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   FormatStr:string,
   BTName:string,
   BTAddress1:string,
   BTAddress2:string,
   BTAddress3:string,
   BTCity:string,
   BTState:string,
   BTZip:string,
      /**  Country part of Bill-to address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   BTCountryNum:number,
      /**  Country is used as part of the bill-to address. It can be left blank.  */  
   BTCountry:string,
      /**  The bill-to address Phone Number for the customer.  */  
   BTPhoneNum:string,
      /**  The bill-to address Fax telephone number for the customer. Optional field.  */  
   BTFaxNum:string,
      /**  Optional bill-to address format.  Controls the address format used on crystal forms.  */  
   BTFormatStr:string,
      /**  The unique Customer Number of the Parent.  */  
   ParentCustNum:number,
   TaxRegionCode:string,
      /**  This is an inter-company customer.  */  
   ICCust:boolean,
      /**  The day of the month that service contracts that are marked for recurring invoices are billed for this customer.  If the Invoice group invoice date is greater than or equal to this date then the invoice will be generated.  */  
   ContBillDay:number,
      /**  Email address of the customer.  */  
   EMailAddress:string,
      /**  Indicates if the customer has any qualifications on completeness of the order before it can be shipped. The valid values are; "O" - Order must be 100% complete,  "L" - Order Line must be 100% complete, "blank" - None.  This setting is a default for orders of a specific customer. See OrderHed.ShipOrderComplete, OrderDtl.ShipLineComplete  */  
   ShippingQualifier:string,
      /**  Code used to relate a AllocPri record to the customer.  This is used as a default to OrderHed.AllocPriCode for order for this customer.  */  
   AllocPriorityCode:string,
      /**  Used with Global alerts  */  
   LinkPortNum:number,
      /**  Indicates if this customer is for eCommerce.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and StoreFront DB (VntgSF).  */  
   WebCustomer:boolean,
      /**   Describe the type of Customer this is.
SUS = Suspect
PRO =  Prospect
CUS = Customer  */  
   CustomerType:string,
      /**  Indicates that this contact is not included in marketing lists  */  
   NoContact:boolean,
      /**  This customers territory cannot be changed by any process that changes territories  */  
   TerritoryLock:boolean,
      /**  Customers Website URL .  */  
   CustURL:string,
      /**  The sales territory that the system will assign based on new values in the Sales territory boundary table.  */  
   PendingTerritoryID:string,
   ExtID:string,
      /**  APK - added for consolidation accross multiple SO's for the same customer  */  
   ConsolidateSO:boolean,
      /**  BillFrequency  */  
   BillFrequency:string,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   CreditIncludePI:boolean,
      /**  Marks the customer as a global customer, available to be sent out to other companies  */  
   GlobalCust:boolean,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  Indicates if this customer participates in the Inter-Company Trading.  */  
   ICTrader:boolean,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   CustNum:number,
      /**  Indicates that Open Orders are to be included in the global credit limit checking. This checkbox will also include open service contracts.  */  
   GlobalCredIncOrd:boolean,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   GlobalCredIncPI:boolean,
      /**  A unique code that identifies the currency.  */  
   GlobalCurrencyCode:string,
      /**  Indicates if customer has been placed into a "Global Credit Hold" status. Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  */  
   GlobalCreditHold:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  */  
   OldCustNum:number,
      /**  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  */  
   OldCustID:string,
      /**  Establishes the tax authority for this customer.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   TaxAuthorityCode:string,
      /**  This flag indicates if an external delivery note is required for the customer.  This field is available only when send shipments for financial integration is turned on.  This will provide the default for the ShipHead record.  */  
   ExternalDeliveryNote:boolean,
   ExternalID:string,
   CheckDuplicatePO:boolean,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit.  Credit limit of zero is considered as having unlimited credit.  */  
   CreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   CustPILimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit.  */  
   GlobalCreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   GlobalPILimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  */  
   DocGlobalCreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  */  
   DocGlobalPILimit:number,
      /**  Indicates whether RFQ Attachments are allowed for this Customer  */  
   RfqAttachAllow:boolean,
      /**   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based discount.
"ADD" = means that the customer could get the order value based discount in addition to the default order discount.  */  
   DiscountQualifier:string,
      /**  Indicates if the user chose to skip this record when linking global customers.  The user can come back at a later time and choose to link a skipped customer if they need to.  */  
   Skipped:boolean,
   AllowAltBillTo:boolean,
   ApplyChrg:boolean,
   ChrgAmount:number,
   COD:boolean,
   CODAmount:number,
   CODCheck:boolean,
   CODFreight:boolean,
   DeclaredAmt:number,
   DeclaredIns:boolean,
   DemandAddAction:string,
   DemandAddLeadTime:number,
   DemandAutoAccept:boolean,
   DemandCancelAction:string,
   DemandCancelLeadTime:number,
   DemandChangeAction:string,
   DemandChangeDateAction:string,
   DemandChangeDateLeadTime:number,
   DemandChangeLeadTime:number,
   DemandDateType:string,
   DemandDayOfWeek:number,
   DemandDeliveryDays:number,
   DemandNewLineAction:string,
   DemandNewLineLeadTime:number,
   DemandQtyChangeAction:string,
   DemandQtyChangeLeadTime:number,
   DemandUseSysDate:boolean,
   DocOnly:boolean,
   GroundType:string,
   Hazmat:boolean,
   NotifyEMail:string,
   NotifyFlag:boolean,
   RefNotes:string,
   ResDelivery:boolean,
   SatDelivery:boolean,
   SatPickup:boolean,
   TradingPartnerName:string,
   VerbalConf:boolean,
   PeriodicityCode:number,
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
   CreditDays:number,
   EarlyBuffer:number,
   LateBuffer:number,
   OverrideCarrier:boolean,
   OverrideService:boolean,
   DemandUnitPriceDiff:boolean,
   DemandUnitPriceDiffAction:string,
   AddressVal:boolean,
   ExcFromVal:boolean,
   RebateForm:string,
   RebateVendorNum:number,
   CreditCardOrder:boolean,
   DemandCheckForPart:boolean,
   DemandCheckForPartAction:string,
   ChangeDate:string,
   ChangedBy:string,
   ChangeTime:number,
   ChargeCode:string,
   AddlHdlgFlag:boolean,
   CertOfOrigin:boolean,
   CommercialInvoice:boolean,
   DeliveryConf:number,
   ETCAddrChg:boolean,
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
   ARCreditTotal:number,
   PICreditTotal:number,
   SOCreditTotal:number,
   TaxMethod:string,
   TaxRoundRule:number,
   AcrossNatAcc:boolean,
   NACreditIsShare:boolean,
   NACreditPreferenceList:string,
   NACreditSharedPrc:number,
   NAParentCreditIsUsed:boolean,
   NAParentCreditPrc:number,
   OverrideRlsClass:boolean,
   ValidPayer:boolean,
   ValidShipTo:boolean,
   ValidSoldTo:boolean,
   AllowOTS:boolean,
   ManagedVendID:string,
   ManagedVendNum:number,
   ThirdPLCust:boolean,
   NARlsClassCode:string,
   AutoGenPromNotes:boolean,
   DirectDebiting:boolean,
   PartPayment:boolean,
   ReservePriorityCode:string,
   NAParentsCreditUsed:number,
   NASharedCreditUsed:number,
   NAOwnCreditUsed:number,
   GlbNACreditIsShare:boolean,
   GlbNACreditSharedPrc:number,
   GlbNAParentCreditIsUsed:boolean,
   GlbNAParentCreditPrc:number,
   GlbNAParentsCreditUsed:number,
   GlbNASharedCreditUsed:number,
   ReminderCode:string,
   AllowShipTo3:boolean,
   NACreditUpdate:string,
   OTSSaveAs:string,
   CustPartOpts:string,
   HasBank:boolean,
   PMUID:number,
   DemandCheckForRev:boolean,
   DemandCheckForRevAction:string,
   OrderHoldForReview:boolean,
   ShipToTerrList:string,
   AcctRefNumber:string,
   DemandCheckCUMM:boolean,
   DemandCheckCUMMAction:string,
   DemandCloseNoMatch:boolean,
   DemandCloseRejSkd:boolean,
   DemandPricing:string,
   DmdCheckPartialShip:boolean,
   DmdCheckShipAction:string,
   InvPerPackLine:boolean,
   LegalName:string,
   OrgRegCode:string,
   OurBankCode:string,
      /**  Defines the tolerance for price difference validations  */  
   PriceTolerance:number,
   TaxRegReason:string,
   CheckConfirmCapPromise:boolean,
   CheckDateCapPromise:boolean,
   CheckUpdateCapPromise:boolean,
   DemandCapPromiseAction:string,
   DemandCapPromiseDate:string,
   DemandCapPromiseUpdate:string,
   DemandSplitSched:boolean,
   DueDateCriteria:string,
   ERSOrder:boolean,
   PBTerms:number,
   PeriodicBilling:boolean,
   PreferredBank:string,
   SICCode:number,
   ICCode:string,
   OTSmartString:boolean,
   DeferredRev:boolean,
   RACode:string,
   DemandCheckCfgAction:string,
   DemandCheckConfig:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Customer.CustID to link to (new or existing)  */  
   LinkCustID:string,
   DisplayHold:string,
   DisplayCustomerType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCustomerListTableset{
   GlbCustomerList:Erp_Tablesets_GlbCustomerListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlbCustomerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the owner company  */  
   GlbCustID:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the owner company  */  
   GlbCustNum:number,
   Name:string,
   Address1:string,
   Address2:string,
   Address3:string,
   City:string,
   State:string,
   Zip:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  Optional field used to record the customer's State Tax Identification number, which is used on Sales Acknowledgments.  */  
   ResaleID:string,
      /**   Contains the default SalesRep for the specific customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference Orders.
It can be left blank or must be valid in the SalesRep master file.  */  
   SalesRepCode:string,
      /**  The Sales Territory for the Customer.  */  
   TerritoryID:string,
      /**  Contains the key of the default ship to for a customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in shipto maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  */  
   ShipToNum:string,
      /**  Establishes the default sales terms that should be used for this customer. This field can't be left blank, it must be valid in the Terms file. A default may be supplied by XaSyst.TermsCode if not blank.  It supplies the default in Order entry and Invoice entry.  */  
   TermsCode:string,
      /**  Contains the default ShipVia for a customer. This is an optional field, it can be left blank or it must be valid in the ShipVia master file.  */  
   ShipViaCode:string,
      /**  Controls the selection for printing of Accounts Receivable statements for a customer.  */  
   PrintStatements:boolean,
      /**  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  */  
   PrintLabels:boolean,
      /**   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgments.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know  if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  */  
   PrintAck:boolean,
      /**  Controls whether or not the customer included in the finance charge calculation process.  */  
   FinCharges:boolean,
      /**  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   CreditHold:boolean,
      /**  Customer Group code for a customer.  This can be blank or it must be valid in the CustsGrup file. This field will be used as a sort and selection parameter for reporting.  */  
   GroupCode:string,
      /**  An optional field used to establish a default purchasing discount percentage for a customer. This value is supplied to order entry as a default for line item discount percent.  */  
   DiscountPercent:number,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  */  
   PrimPCon:number,
      /**  The same as the PrimPCon except that this is the Billing contact and this is used as a default in invoice entry.  */  
   PrimBCon:number,
      /**  Same as PrimPCon except that this the Shipping contact and is used as a default in Packing Slip entry.  */  
   PrimSCon:number,
      /**   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   Comment:string,
      /**  The date when they were established as a customer. Use the system date as a default when creating new customers. This is user maintainable.  */  
   EstDate:string,
      /**  Fax telephone number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  */  
   FaxNum:string,
      /**  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  Indicates the reason why  customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  */  
   TaxExempt:string,
      /**  The ID that establishes link to the default QMarkUp record which provides default markup percents used by quote entry for this customer. This ID is not directly entered. Instead it is derived via the user entering the description of the QMarkUp record. This can be left blank, else must be valid.  */  
   MarkUpID:string,
      /**   ** 6.0 extended functionality
Represents the day of the week that this customer is billed. The valid values are 0-7 where 0=All,1=Sun,2=Mon,...,7=Sat.  
** (where the bill-frequency = 'W' (weekly)
** (where bill-frequency = 'M' (monthly) this field is 1 -> 31
    representing the day of the month to bill on.
This is used during the "Get Shipments" function of invoice entry. For example, if the customer has BillDay = 4(Wed),  the Get Shipments function will select all the packing slips with a ship date that is less  than or equal to the latest Wednesday's date.
** The same also applies to monthly billing (1-31)  */  
   BillDay:number,
      /**  "Combine" Multiple Packing Slips into one Invoice.  NOTE: The field name does not correctly represent what this actually does !  This value is used during the "Get Shipments" function of invoice entry to control how invoices should be created when there are multiple packing slips for the same customer. Basically, if this value is YES then packing slips for the same Order, Fiscal Period are combined into a single invoice. If this value is NO then each packing slip will create a single invoice.  */  
   OneInvPerPS:boolean,
      /**  Default FOB policy for a customers orders.  Order Entry uses this as a default to OrderHed.FOB.  */  
   DefaultFOB:string,
      /**  Indicates that Open Orders are to be included in the credit limit checking. This checkbox will also include open service contracts.  */  
   CreditIncludeOrders:boolean,
      /**  Date that the next credit check should be made for that customer.  */  
   CreditReviewDate:string,
   CreditHoldDate:string,
   CreditHoldSource:string,
   CreditClearUserID:string,
   CreditClearDate:string,
   CreditClearTime:string,
      /**  This is the Trading Partner ID that is used for incoming and outgoing EDI.  */  
   EDICode:string,
      /**  EDI test mode.  When customers are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  */  
   EDITest:boolean,
      /**  Identifies which EDI package the customer is using.  If not null in must be valid in the EDITrnsl table.  */  
   EDITranslator:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  */  
   LangNameID:string,
      /**  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  */  
   BorderCrossing:string,
      /**  Optional Custom address format.  Controls the address format used on crystal forms.  */  
   FormatStr:string,
   BTName:string,
   BTAddress1:string,
   BTAddress2:string,
   BTAddress3:string,
   BTCity:string,
   BTState:string,
   BTZip:string,
      /**  Country part of Bill-to address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   BTCountryNum:number,
      /**  Country is used as part of the bill-to address. It can be left blank.  */  
   BTCountry:string,
      /**  The bill-to address Phone Number for the customer.  */  
   BTPhoneNum:string,
      /**  The bill-to address Fax telephone number for the customer. Optional field.  */  
   BTFaxNum:string,
      /**  Optional bill-to address format.  Controls the address format used on crystal forms.  */  
   BTFormatStr:string,
      /**  The unique Customer Number of the Parent.  */  
   ParentCustNum:number,
   TaxRegionCode:string,
      /**  This is an inter-company customer.  */  
   ICCust:boolean,
      /**  The day of the month that service contracts that are marked for recurring invoices are billed for this customer.  If the Invoice group invoice date is greater than or equal to this date then the invoice will be generated.  */  
   ContBillDay:number,
      /**  Email address of the customer.  */  
   EMailAddress:string,
      /**  Indicates if the customer has any qualifications on completeness of the order before it can be shipped. The valid values are; "O" - Order must be 100% complete,  "L" - Order Line must be 100% complete, "blank" - None.  This setting is a default for orders of a specific customer. See OrderHed.ShipOrderComplete, OrderDtl.ShipLineComplete  */  
   ShippingQualifier:string,
      /**  Code used to relate a AllocPri record to the customer.  This is used as a default to OrderHed.AllocPriCode for order for this customer.  */  
   AllocPriorityCode:string,
      /**  Used with Global alerts  */  
   LinkPortNum:number,
      /**  Indicates if this customer is for eCommerce.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and StoreFront DB (VntgSF).  */  
   WebCustomer:boolean,
      /**   Describe the type of Customer this is.
SUS = Suspect
PRO =  Prospect
CUS = Customer  */  
   CustomerType:string,
      /**  Indicates that this contact is not included in marketing lists  */  
   NoContact:boolean,
      /**  This customers territory cannot be changed by any process that changes territories  */  
   TerritoryLock:boolean,
      /**  Customers Website URL .  */  
   CustURL:string,
      /**  The sales territory that the system will assign based on new values in the Sales territory boundary table.  */  
   PendingTerritoryID:string,
   ExtID:string,
      /**  APK - added for consolidation accross multiple SO's for the same customer  */  
   ConsolidateSO:boolean,
      /**  BillFrequency  */  
   BillFrequency:string,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   CreditIncludePI:boolean,
      /**  Marks the customer as a global customer, available to be sent out to other companies  */  
   GlobalCust:boolean,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  Indicates if this customer participates in the Inter-Company Trading.  */  
   ICTrader:boolean,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   CustNum:number,
      /**  Indicates that Open Orders are to be included in the global credit limit checking. This checkbox will also include open service contracts.  */  
   GlobalCredIncOrd:boolean,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   GlobalCredIncPI:boolean,
      /**  A unique code that identifies the currency.  */  
   GlobalCurrencyCode:string,
      /**  Indicates if customer has been placed into a "Global Credit Hold" status. Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  */  
   GlobalCreditHold:string,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  */  
   OldCustNum:number,
      /**  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  */  
   OldCustID:string,
      /**  Establishes the tax authority for this customer.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  */  
   TaxAuthorityCode:string,
      /**  This flag indicates if an external delivery note is required for the customer.  This field is available only when send shipments for financial integration is turned on.  This will provide the default for the ShipHead record.  */  
   ExternalDeliveryNote:boolean,
   ExternalID:string,
   CheckDuplicatePO:boolean,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit.  Credit limit of zero is considered as having unlimited credit.  */  
   CreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   CustPILimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit.  */  
   GlobalCreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  */  
   GlobalPILimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  */  
   DocGlobalCreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  */  
   DocGlobalPILimit:number,
      /**  Indicates whether RFQ Attachments are allowed for this Customer  */  
   RfqAttachAllow:boolean,
      /**   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based discount.
"ADD" = means that the customer could get the order value based discount in addition to the default order discount.  */  
   DiscountQualifier:string,
      /**  Indicates if the user chose to skip this record when linking global customers.  The user can come back at a later time and choose to link a skipped customer if they need to.  */  
   Skipped:boolean,
   AllowAltBillTo:boolean,
   ApplyChrg:boolean,
   ChrgAmount:number,
   COD:boolean,
   CODAmount:number,
   CODCheck:boolean,
   CODFreight:boolean,
   DeclaredAmt:number,
   DeclaredIns:boolean,
   DemandAddAction:string,
   DemandAddLeadTime:number,
   DemandAutoAccept:boolean,
   DemandCancelAction:string,
   DemandCancelLeadTime:number,
   DemandChangeAction:string,
   DemandChangeDateAction:string,
   DemandChangeDateLeadTime:number,
   DemandChangeLeadTime:number,
   DemandDateType:string,
   DemandDayOfWeek:number,
   DemandDeliveryDays:number,
   DemandNewLineAction:string,
   DemandNewLineLeadTime:number,
   DemandQtyChangeAction:string,
   DemandQtyChangeLeadTime:number,
   DemandUseSysDate:boolean,
   DocOnly:boolean,
   GroundType:string,
   Hazmat:boolean,
   NotifyEMail:string,
   NotifyFlag:boolean,
   RefNotes:string,
   ResDelivery:boolean,
   SatDelivery:boolean,
   SatPickup:boolean,
   TradingPartnerName:string,
   VerbalConf:boolean,
   PeriodicityCode:number,
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
   CreditDays:number,
   EarlyBuffer:number,
   LateBuffer:number,
   OverrideCarrier:boolean,
   OverrideService:boolean,
   DemandUnitPriceDiff:boolean,
   DemandUnitPriceDiffAction:string,
   AddressVal:boolean,
   ExcFromVal:boolean,
   RebateForm:string,
   RebateVendorNum:number,
   CreditCardOrder:boolean,
   DemandCheckForPart:boolean,
   DemandCheckForPartAction:string,
   ChangeDate:string,
   ChangedBy:string,
   ChangeTime:number,
   ChargeCode:string,
   AddlHdlgFlag:boolean,
   CertOfOrigin:boolean,
   CommercialInvoice:boolean,
   DeliveryConf:number,
   ETCAddrChg:boolean,
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
   ARCreditTotal:number,
   PICreditTotal:number,
   SOCreditTotal:number,
   TaxMethod:string,
   TaxRoundRule:number,
   AcrossNatAcc:boolean,
   NACreditIsShare:boolean,
   NACreditPreferenceList:string,
   NACreditSharedPrc:number,
   NAParentCreditIsUsed:boolean,
   NAParentCreditPrc:number,
   OverrideRlsClass:boolean,
   ValidPayer:boolean,
   ValidShipTo:boolean,
   ValidSoldTo:boolean,
   AllowOTS:boolean,
   ManagedVendID:string,
   ManagedVendNum:number,
   ThirdPLCust:boolean,
   NARlsClassCode:string,
   AutoGenPromNotes:boolean,
   DirectDebiting:boolean,
   PartPayment:boolean,
   ReservePriorityCode:string,
   NAParentsCreditUsed:number,
   NASharedCreditUsed:number,
   NAOwnCreditUsed:number,
   GlbNACreditIsShare:boolean,
   GlbNACreditSharedPrc:number,
   GlbNAParentCreditIsUsed:boolean,
   GlbNAParentCreditPrc:number,
   GlbNAParentsCreditUsed:number,
   GlbNASharedCreditUsed:number,
   ReminderCode:string,
   AllowShipTo3:boolean,
   NACreditUpdate:string,
   OTSSaveAs:string,
   CustPartOpts:string,
   HasBank:boolean,
   PMUID:number,
   DemandCheckForRev:boolean,
   DemandCheckForRevAction:string,
   OrderHoldForReview:boolean,
   ShipToTerrList:string,
   AcctRefNumber:string,
   DemandCheckCUMM:boolean,
   DemandCheckCUMMAction:string,
   DemandCloseNoMatch:boolean,
   DemandCloseRejSkd:boolean,
   DemandPricing:string,
   DmdCheckPartialShip:boolean,
   DmdCheckShipAction:string,
   InvPerPackLine:boolean,
   LegalName:string,
   OrgRegCode:string,
   OurBankCode:string,
      /**  Defines the tolerance for price difference validations  */  
   PriceTolerance:number,
   TaxRegReason:string,
   CheckConfirmCapPromise:boolean,
   CheckDateCapPromise:boolean,
   CheckUpdateCapPromise:boolean,
   DemandCapPromiseAction:string,
   DemandCapPromiseDate:string,
   DemandCapPromiseUpdate:string,
   DemandSplitSched:boolean,
   DueDateCriteria:string,
   ERSOrder:boolean,
   PBTerms:number,
   PeriodicBilling:boolean,
   PreferredBank:string,
   SICCode:number,
   ICCode:string,
   OTSmartString:boolean,
   DeferredRev:boolean,
   RACode:string,
   DemandCheckCfgAction:string,
   DemandCheckConfig:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  THBranchID  */  
   THBranchID:string,
      /**  CustPricingSchema  */  
   CustPricingSchema:string,
      /**  ParamCode  */  
   ParamCode:string,
      /**  AGAFIPResponsibilityCode  */  
   AGAFIPResponsibilityCode:string,
      /**  AGBillToProvinceCode  */  
   AGBillToProvinceCode:string,
      /**  AGGrossIncomeTaxID  */  
   AGGrossIncomeTaxID:string,
      /**  AGIDDocTypeCode  */  
   AGIDDocTypeCode:string,
      /**  AGIDDocumentNumber  */  
   AGIDDocumentNumber:string,
      /**  AGProvinceCode  */  
   AGProvinceCode:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  Collections  */  
   Collections:boolean,
      /**  CollectionsDate  */  
   CollectionsDate:string,
      /**  DateCollectionPosted  */  
   DateCollectionPosted:string,
      /**  MXMunicipio  */  
   MXMunicipio:string,
      /**  PEIdentityDocType  */  
   PEIdentityDocType:string,
      /**  PEDocumentID  */  
   PEDocumentID:string,
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
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  InvcOrderCmpDflt  */  
   InvcOrderCmpDflt:boolean,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  RegistrationCode  */  
   RegistrationCode:string,
      /**  EAddress  */  
   EAddress:string,
      /**  DemandCheckForRunOutPart  */  
   DemandCheckForRunOutPart:boolean,
      /**  DemandCheckForRunOutPartAction  */  
   DemandCheckForRunOutPartAction:string,
      /**  EInvCompanyIDAttr  */  
   EInvCompanyIDAttr:string,
      /**  INCSTNumber  */  
   INCSTNumber:string,
      /**  INPANNumber  */  
   INPANNumber:string,
      /**  COOneTimeID  */  
   COOneTimeID:string,
      /**  COIsOneTimeCust  */  
   COIsOneTimeCust:boolean,
      /**  DEOrgType  */  
   DEOrgType:string,
      /**  PEGuaranteeName  */  
   PEGuaranteeName:string,
      /**  PEGuaranteeAddress1  */  
   PEGuaranteeAddress1:string,
      /**  PEGuaranteeAddress2  */  
   PEGuaranteeAddress2:string,
      /**  PEGuaranteeAddress3  */  
   PEGuaranteeAddress3:string,
      /**  PEGuaranteeCity  */  
   PEGuaranteeCity:string,
      /**  PEGuaranteeState  */  
   PEGuaranteeState:string,
      /**  PEGuaranteeZip  */  
   PEGuaranteeZip:string,
      /**  PEGuaranteeCountry  */  
   PEGuaranteeCountry:string,
      /**  PEGuaranteePhoneNum  */  
   PEGuaranteePhoneNum:string,
      /**  PEGuaranteeTaxID  */  
   PEGuaranteeTaxID:string,
      /**  OurSupplierCode  */  
   OurSupplierCode:string,
      /**  ECCType  */  
   ECCType:string,
      /**  MYIndustryCode  */  
   MYIndustryCode:string,
      /**  SyncToExternalCRM  */  
   SyncToExternalCRM:boolean,
      /**  ExternalCRMGlbCustomerID  */  
   ExternalCRMGlbCustomerID:string,
      /**  ExternalCRMGlbCustomerType  */  
   ExternalCRMGlbCustomerType:string,
      /**  ExternalCRMLastSync  */  
   ExternalCRMLastSync:string,
      /**  ExternalCRMSyncRequired  */  
   ExternalCRMSyncRequired:boolean,
      /**  Ownership  */  
   Ownership:string,
      /**  Industry  */  
   Industry:string,
      /**  AnnualRevenue  */  
   AnnualRevenue:number,
      /**  NumberOfEmployees  */  
   NumberOfEmployees:number,
      /**  TickerLocation  */  
   TickerLocation:string,
      /**  TickerSymbol  */  
   TickerSymbol:string,
      /**  Rating  */  
   Rating:string,
      /**  TWGUIRegNum  */  
   TWGUIRegNum:string,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  ConsolidateLinesPerPart  */  
   ConsolidateLinesPerPart:boolean,
      /**  TWTaxPayerType  */  
   TWTaxPayerType:number,
      /**  TWDeductGUIFormatCode  */  
   TWDeductGUIFormatCode:string,
      /**  MXCURP  */  
   MXCURP:string,
      /**  PEAddressID  */  
   PEAddressID:string,
      /**  PEPerceptionRegime  */  
   PEPerceptionRegime:string,
      /**  TaxEntityType  */  
   TaxEntityType:string,
      /**  INGSTComplianceRate  */  
   INGSTComplianceRate:number,
      /**  INTaxRegistrationID  */  
   INTaxRegistrationID:string,
      /**  MXPurchaseType  */  
   MXPurchaseType:string,
      /**  SendToFSA  */  
   SendToFSA:boolean,
      /**  MXGeneralPublic  */  
   MXGeneralPublic:boolean,
      /**  AgingCreditHold  */  
   AgingCreditHold:boolean,
      /**  AgingCreditHoldDate  */  
   AgingCreditHoldDate:string,
      /**  AgingCreditHoldSource  */  
   AgingCreditHoldSource:string,
      /**  AgingCreditClearUserID  */  
   AgingCreditClearUserID:string,
      /**  AgingCreditClearDate  */  
   AgingCreditClearDate:string,
      /**  AgingCreditCode  */  
   AgingCreditCode:string,
      /**  ImporterOfRecord  */  
   ImporterOfRecord:boolean,
      /**  SEC  */  
   SEC:string,
      /**  EInvEndpointIDAttr  */  
   EInvEndpointIDAttr:string,
      /**  Indicates whether sales orders from this sold to customer should be treated as Blind Shipments by Manifest.  */  
   UseBlindShipping:boolean,
      /**  ELIEinvoice  */  
   ELIEinvoice:boolean,
      /**  ELIDefReportID  */  
   ELIDefReportID:string,
      /**  ELIDefStyleNum  */  
   ELIDefStyleNum:number,
      /**  ELIDefToMail  */  
   ELIDefToMail:string,
      /**  ELIDefCCMail  */  
   ELIDefCCMail:string,
      /**  ELIDefMailTempID  */  
   ELIDefMailTempID:string,
      /**  ELISendMail  */  
   ELISendMail:boolean,
      /**  COFiscalResp1  */  
   COFiscalResp1:string,
      /**  COFiscalResp2  */  
   COFiscalResp2:string,
      /**  COFiscalResp3  */  
   COFiscalResp3:string,
      /**  COOperType  */  
   COOperType:string,
      /**  Central Collection  */  
   CentralCollection:boolean,
      /**  NettingVendorNum  */  
   NettingVendorNum:number,
      /**  EORINumber  */  
   EORINumber:string,
      /**  AGIsElectronicCreditInvEligible  */  
   AGIsElectronicCreditInvEligible:boolean,
      /**  TaxValidationStatus  */  
   TaxValidationStatus:number,
      /**  TaxValidationDate  */  
   TaxValidationDate:string,
      /**  HMRCTaxValidationLog  */  
   HMRCTaxValidationLog:string,
      /**  Inactive  */  
   Inactive:boolean,
      /**  ExternalSchemeID  */  
   ExternalSchemeID:string,
      /**  ELIOperatorCode  */  
   ELIOperatorCode:string,
      /**  ELISendingOption  */  
   ELISendingOption:number,
      /**  ELIOperatorID  */  
   ELIOperatorID:string,
      /**  EInvExternalID  */  
   EInvExternalID:string,
      /**  MXTaxRegime  */  
   MXTaxRegime:string,
      /**  ExclusionMonth  */  
   ExclusionMonth:number,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  FSMRegionCode  */  
   FSMRegionCode:string,
      /**  FSMArea  */  
   FSMArea:string,
      /**  ELIRcptDefStyleNum  */  
   ELIRcptDefStyleNum:number,
      /**  CovenantDiscPercent  */  
   CovenantDiscPercent:number,
   DisplayCustomerType:string,
      /**  Customer.CustID to link to (new or existing)  */  
   LinkCustID:string,
   DisplayHold:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCustomerSearchTableset{
   GlbCustomer:Erp_Tablesets_GlbCustomerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGlbCustomerSearchTableset{
   GlbCustomer:Erp_Tablesets_GlbCustomerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param glbCompany
      @param glbCustNum
   */  
export interface GetByID_input{
   glbCompany:string,
   glbCustNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GlbCustomerSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GlbCustomerSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GlbCustomerSearchTableset[],
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
   returnObj:Erp_Tablesets_GlbCustomerListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param glbCompany
   */  
export interface GetNewGlbCustomer_input{
   ds:Erp_Tablesets_GlbCustomerSearchTableset[],
   glbCompany:string,
}

export interface GetNewGlbCustomer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCustomerSearchTableset[],
}
}

   /** Required : 
      @param whereClauseGlbCustomer
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGlbCustomer:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GlbCustomerSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtGlbCustomerSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGlbCustomerSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GlbCustomerSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCustomerSearchTableset[],
}
}

