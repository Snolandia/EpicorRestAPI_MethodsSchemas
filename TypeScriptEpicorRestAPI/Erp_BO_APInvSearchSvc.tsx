import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.APInvSearchSvc
// Description: bo/APInvSearch/APInvSearch.p
           AP Invoice Search
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/$metadata", {
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
   Description: Get APInvSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APInvSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvHedRow
   */  
export function get_APInvSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/APInvSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APInvSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APInvHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APInvHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APInvSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/APInvSearches", {
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
   Summary: Calls GetByID to retrieve the APInvSearch item
   Description: Calls GetByID to retrieve the APInvSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvHedRow
   */  
export function get_APInvSearches_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APInvHedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/APInvSearches(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_APInvHedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APInvSearch for the service
   Description: Calls UpdateExt to update APInvSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APInvSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APInvHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APInvSearches_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/APInvSearches(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
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
   Summary: Call UpdateExt to delete APInvSearch item
   Description: Call UpdateExt to delete APInvSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APInvSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APInvSearches_Company_VendorNum_InvoiceNum(Company:string, VendorNum:string, InvoiceNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/APInvSearches(" + Company + "," + VendorNum + "," + InvoiceNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvHedListRow)
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
export function get_GetRows(whereClauseAPInvHed:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAPInvHed!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPInvHed=" + whereClauseAPInvHed
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(vendorNum:string, invoiceNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof vendorNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vendorNum=" + vendorNum
   }
   if(typeof invoiceNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "invoiceNum=" + invoiceNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewAPInvHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPInvHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPInvHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPInvHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPInvHed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/GetNewAPInvHed", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APInvHedListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvHedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APInvHedRow[],
}

export interface Erp_Tablesets_APInvHedListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this is an "open" Payable.  */  
   "OpenPayable":boolean,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "InvoiceNum":string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   "DebitMemo":boolean,
      /**  Invoice date.  */  
   "InvoiceDate":string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   "TaxAmt":number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   "DueDate":string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   "Posted":boolean,
      /**  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  */  
   "FiscalYear":number,
      /**  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  */  
   "FiscalPeriod":number,
      /**  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  */  
   "InvoiceRef":string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   "InvoiceAmt":number,
      /**  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   "DocInvoiceAmt":number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  */  
   "InvoiceHeld":boolean,
      /**  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  */  
   "PayHold":boolean,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   "Description":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  */  
   "CPay":boolean,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  */  
   "CPayInvoiceBal":number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  */  
   "CPayDocInvoiceBal":number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   "ApplyDate":string,
      /**  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  */  
   "CorrectionInv":boolean,
      /**  Indicates that this is pre-payment invoice.  */  
   "PrePayment":boolean,
      /**  Letter of Credit ID.  */  
   "APLOCID":string,
      /**  Transaction Document Type ID  */  
   "TranDocTypeID":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  TWDeclareYear  */  
   "TWDeclareYear":number,
      /**  TWDeclarePeriod  */  
   "TWDeclarePeriod":number,
      /**  Invoice Type  */  
   "InvoiceType":string,
      /**  PLInvoiceReference  */  
   "PLInvoiceReference":string,
   "ScrInvoiceVendorAmt":number,
   "ScrDocInvoiceVendorAmt":number,
   "ScrInvoiceAmt":number,
   "ScrDocInvoiceAmt":number,
   "ScrInvoiceBal":number,
   "ScrDocInvoiceBal":number,
   "ScrUnpostedBal":number,
   "ScrDocUnpostedBal":number,
   "InvoiceVariance":number,
   "DocInvoiceVariance":number,
      /**  Indicates if the CPay invoice is still an open payable at Corporate  */  
   "CPayOpenPayable":boolean,
      /**  Supplier Name  */  
   "VendorNumName":string,
      /**  Supplier ID  */  
   "VendorNumVendorID":string,
   "TranDocTypeDescription":string,
   "Rpt1ScrInvoiceAmt":number,
   "Rpt2ScrInvoiceAmt":number,
   "Rpt3ScrInvoiceAmt":number,
   "Rpt1InvoiceVariance":number,
   "Rpt2InvoiceVariance":number,
   "Rpt3InvoiceVariance":number,
   "Rpt1ScrInvoiceVendorAmt":number,
   "Rpt2ScrInvoiceVendorAmt":number,
   "Rpt3ScrInvoiceVendorAmt":number,
   "IsLcked":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APInvHedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this is an "open" Payable.  */  
   "OpenPayable":boolean,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "InvoiceNum":string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   "DebitMemo":boolean,
      /**  Invoice date.  */  
   "InvoiceDate":string,
      /**  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "TermsCode":string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   "TaxAmt":number,
      /**  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  */  
   "DocTaxAmt":number,
      /**  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  */  
   "DiscountDate":string,
      /**  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   "DiscountAmt":number,
      /**  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   "DocDiscountAmt":number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   "DueDate":string,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   "PayDates":string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   "PayAmounts":string,
      /**  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   "DocPayAmounts":string,
      /**  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  */  
   "GLPosted":boolean,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   "GroupID":string,
      /**  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   "Posted":boolean,
      /**  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  */  
   "FiscalYear":number,
      /**  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  */  
   "FiscalPeriod":number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   "StartUp":boolean,
      /**  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  */  
   "InvoiceRef":string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   "EntryPerson":string,
      /**  Used to establish invoice comments about the overall invoice.  */  
   "InvoiceComment":string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   "InvoiceAmt":number,
      /**  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   "DocInvoiceAmt":number,
      /**  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  */  
   "DocInvoiceVendorAmt":number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   "InvoiceBal":number,
      /**  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  */  
   "DocInvoiceBal":number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "UnpostedBal":number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "DocUnpostedBal":number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  */  
   "InvoiceHeld":boolean,
      /**  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  */  
   "PayHold":boolean,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   "Description":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  */  
   "REFPONum":number,
      /**  The Tax Region for this invoice.  */  
   "TaxRegionCode":string,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  Journal that invoice was posted to.  */  
   "JournalCode":string,
      /**  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  */  
   "UpdateTax":boolean,
      /**  For use by external G/L interfacing.  This field is sign flipped for debit memos.  */  
   "InvoiceVendorAmt":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  External Identification of the Invoice.  */  
   "ExternalID":string,
      /**  Allows user to control discount amount manually or automatically  */  
   "FixedAmt":boolean,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefInvoiceNum":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   "GlbInvoiceNum":string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "DepGainLoss":number,
      /**  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  */  
   "CPay":boolean,
      /**  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  */  
   "CPayLinked":boolean,
      /**  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  */  
   "CPayLegalNumber":string,
      /**  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   "CPayCheckNum":number,
      /**  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   "CPayCheckDate":string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  */  
   "CPayInvoiceBal":number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  */  
   "CPayDocInvoiceBal":number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  */  
   "GLControlType":string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "DocRounding":number,
      /**  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  */  
   "GLControlCode":string,
      /**  Reporting currency value of this field  */  
   "Rpt1DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DiscountAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoiceVendorAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt2PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt3PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnpostedBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnpostedBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnpostedBal":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   "Rpt1CPayInvoiceBal":number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   "Rpt2CPayInvoiceBal":number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   "Rpt3CPayInvoiceBal":number,
      /**  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  */  
   "AllowOverrideLI":boolean,
      /**  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  */  
   "MatchedFromLI":boolean,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   "ApplyDate":string,
      /**  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   "PayDiscDays":string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   "PayDiscPer":string,
      /**  Withholding Tax Amount.  */  
   "WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "DocWithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt1WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt2WithholdAmt":number,
      /**  Withholding Tax Amount.  */  
   "Rpt3WithholdAmt":number,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   "PayDiscPartPay":boolean,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   "PIPayment":string,
      /**  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  */  
   "CorrectionInv":boolean,
      /**  Tax Rate Group Code  */  
   "TaxRateGrpCode":string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   "LockTaxRate":boolean,
      /**  Sweden and Finland Localization Field - Banking Reference  */  
   "SEBankRef":string,
      /**  Sweden and Finland Localization Field - Payment Code  */  
   "SEPayCode":string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   "GUIFormatCode":string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   "GUITaxTypeCode":string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   "GUIDeductCode":string,
      /**  Indicates that this is pre-payment invoice.  */  
   "PrePayment":boolean,
      /**  Letter of Credit ID.  */  
   "APLOCID":string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   "Plant":string,
      /**   Taiwan Localization
Tax Amount Basis  */  
   "GUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in document currrency  */  
   "DocGUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt1 currency  */  
   "Rpt1GUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt2 currency  */  
   "Rpt2GUIImportTaxBasis":number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt3 currency  */  
   "Rpt3GUIImportTaxBasis":number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   "OvrDefTaxDate":boolean,
      /**  Linked flag  */  
   "Linked":boolean,
      /**  The claim reference from the expense group that generated the invoice.  */  
   "ClaimRef":string,
      /**  The employee from the group of expenses that created the invoice.  */  
   "EmpID":string,
      /**  Indicates that Invoice has been selected for payment in a bankfile  */  
   "InBankFile":boolean,
      /**  Credit Note Confirmation Date  */  
   "CNConfirmDate":string,
      /**  Unique ID of the vendor's bank.  */  
   "BankID":string,
      /**  Legal Number for the self assessment.  */  
   "SelfLegalNumber":string,
      /**  Transaction Document Type for the self assessment.  */  
   "SelfTranDocTypeID":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**   Denmark Localization
Card (payment) code  */  
   "CardCode":string,
      /**  Site Code  */  
   "SiteCode":string,
      /**   Denmark Localization
Account Number  */  
   "BankGiroAcctNbr":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Supplier Agent Name  */  
   "SupAgentName":string,
      /**  Supplier Agent Tax Region Number  */  
   "SupAgentTaxRegNo":string,
      /**  Non Deductable Code  */  
   "NonDeductCode":string,
      /**  Asset Type Code  */  
   "AssetTypeCode":string,
      /**  Cash  */  
   "Cash":boolean,
      /**  Credit Card  */  
   "CreditCard":boolean,
      /**  Normal  */  
   "Normal":boolean,
      /**  Card ID  */  
   "CardID":string,
      /**  Card Holder Tax ID  */  
   "CardHolderTaxID":string,
      /**  Card Member Name  */  
   "CardMemberName":string,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Non Deductable Amount  */  
   "NonDeductAmt":number,
      /**  Non Deductable Doc Amount  */  
   "NonDeductDocAmt":number,
      /**  Non Deductable Rpt1 Amount  */  
   "NonDeductRpt1Amt":number,
      /**  Non Deductable Rpt2 Amount  */  
   "NonDeductRpt2Amt":number,
      /**  Non Deductable Rpt3 Amount  */  
   "NonDeductRpt3Amt":number,
      /**  Non Deductable VAT Amount  */  
   "NonDeductVATAmt":number,
      /**  Non Deductable VAT Doc Amount  */  
   "NonDeductVATDocAmt":number,
      /**  Non Deductable VAT Rpt1 Amount  */  
   "NonDeductVATRpt1Amt":number,
      /**  Non Deductable VAT Rpt2 Amount  */  
   "NonDeductVATRpt2Amt":number,
      /**  Non Deductable VAT Rpt3 Amount  */  
   "NonDeductVATRpt3Amt":number,
      /**  Stores the number of the import document.  */  
   "ImportNum":string,
      /**  Country of Import  */  
   "ImportedFrom":string,
      /**  Date of import.  */  
   "ImportedDate":string,
      /**   Indicates that this is Advanced Tax invoice received from
supplier  */  
   "AdvTaxInv":boolean,
      /**   Indicates that the tax is included in the unit price
for this AP Invoice  */  
   "InPrice":boolean,
      /**  Transaction Document Type ID  */  
   "TranDocTypeID":string,
      /**  Reserved for Development - Integer  */  
   "DevInt1":number,
      /**  Reserved for Development - Integer  */  
   "DevInt2":number,
      /**  Reserved for development - decimal  */  
   "DevDec1":number,
      /**  Reserved for development - decimal  */  
   "DevDec2":number,
      /**  Reserved for development - decimal  */  
   "DevDec3":number,
      /**  Reserved for development - decimal  */  
   "DevDec4":number,
      /**  In case of Tax Inclusive Pricing if system-calculated Header related taxes are changed/deleted/added  by the user - this field is set to true by the system.  */  
   "DevLog1":boolean,
      /**  Reserved for development - logical  */  
   "DevLog2":boolean,
      /**  Assigned as "I" when Recurring Invoice has Inactive status.  */  
   "DevChar1":string,
      /**  Reserved for development - character  */  
   "DevChar2":string,
      /**  Reserved for development - date  */  
   "DevDate1":string,
      /**  Reserved for development - date  */  
   "DevDate2":string,
      /**  PaymentNumber  */  
   "PaymentNumber":string,
      /**  CycleCode  */  
   "CycleCode":string,
      /**  Duration  */  
   "Duration":number,
      /**  EndDate  */  
   "EndDate":string,
      /**  MaxValueAmt  */  
   "MaxValueAmt":number,
      /**  DocMaxValueAmt  */  
   "DocMaxValueAmt":number,
      /**  Rpt1MaxValueAmt  */  
   "Rpt1MaxValueAmt":number,
      /**  Rpt2MaxValueAmt  */  
   "Rpt2MaxValueAmt":number,
      /**  Rpt3MaxValueAmt  */  
   "Rpt3MaxValueAmt":number,
      /**  HoldInvoice  */  
   "HoldInvoice":boolean,
      /**  CopyLatestInvoice  */  
   "CopyLatestInvoice":boolean,
      /**  OverrideEndDate  */  
   "OverrideEndDate":boolean,
      /**  CycleInactive  */  
   "CycleInactive":boolean,
      /**  RecurSource  */  
   "RecurSource":boolean,
      /**  InstanceNum  */  
   "InstanceNum":number,
      /**  RecurBalance  */  
   "RecurBalance":number,
      /**  DocRecurBalance  */  
   "DocRecurBalance":number,
      /**  Rpt1RecurBalance  */  
   "Rpt1RecurBalance":number,
      /**  Rpt2RecurBalance  */  
   "Rpt2RecurBalance":number,
      /**  Rpt3RecurBalance  */  
   "Rpt3RecurBalance":number,
      /**  LastDate  */  
   "LastDate":string,
      /**  IsRecurring  */  
   "IsRecurring":boolean,
      /**  InvoiceNumList  */  
   "InvoiceNumList":string,
      /**  IsMaxValue  */  
   "IsMaxValue":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CHISRCodeLine  */  
   "CHISRCodeLine":string,
      /**  DMReason  */  
   "DMReason":string,
      /**  UrgentPayment  */  
   "UrgentPayment":boolean,
      /**  AGDocPageNum  */  
   "AGDocPageNum":string,
      /**  AGCAICAEMark  */  
   "AGCAICAEMark":string,
      /**  AGCAICAENum  */  
   "AGCAICAENum":string,
      /**  AGCAICAEExpirationDate  */  
   "AGCAICAEExpirationDate":string,
      /**  AGAvTaxCreditFlag  */  
   "AGAvTaxCreditFlag":boolean,
      /**  AGUseGoodDefaultMark  */  
   "AGUseGoodDefaultMark":boolean,
      /**  AGCustomsClearanceNum  */  
   "AGCustomsClearanceNum":string,
      /**  AGCustomsCode  */  
   "AGCustomsCode":string,
      /**  AGDestinationCode  */  
   "AGDestinationCode":string,
      /**  Header Number  */  
   "HeadNum":number,
      /**  TranType  */  
   "TranType":string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   "TaxSvcID":string,
      /**  TWDeclareYear  */  
   "TWDeclareYear":number,
      /**  TWDeclarePeriod  */  
   "TWDeclarePeriod":number,
      /**  AP Checking Group ID  */  
   "APChkGrpID":string,
      /**  Invoice Type  */  
   "InvoiceType":string,
      /**  Indicates a computational cost for the invoice  */  
   "PEComputationalCost":string,
      /**  Referenced By BOE  */  
   "ReferencedByBOE":string,
      /**  DUA Reference Number used on Peru Localiation  */  
   "PEDUARefNum":string,
      /**  CustomsNumber  */  
   "CustomsNumber":string,
      /**  ReceivedDate  */  
   "ReceivedDate":string,
      /**  CustOverride  */  
   "CustOverride":number,
      /**  Invoice Number of Invoice Pre-Payment which should be automatically applied to this one during posting process.  */  
   "PrePaymentNum":string,
      /**  Pre-Payment amount in Base Currency.  */  
   "PrePaymentAmt":number,
      /**  Pre-Payment amount in Document Currency.  */  
   "DocPrePaymentAmt":number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   "Rpt1PrePaymentAmt":number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   "Rpt2PrePaymentAmt":number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   "Rpt3PrePaymentAmt":number,
      /**  CSF Peru - AP Payment Number  */  
   "PEAPPayNum":number,
      /**  SCF Peru - Detractions Tax Amount  */  
   "PEDetTaxAmt":number,
      /**  Peru Detraction Tax Currency Code  */  
   "PEDetTaxCurrencyCode":string,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   "PESUNATDepAmt":number,
      /**  Peru Document SUNAT Deposit Amount  */  
   "DocPESUNATDepAmt":number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   "PESUNATDepDate":string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   "PESUNATDepNum":string,
      /**  SUNAT Reference Number. Once a payment is made, the SUNAT returns a reference number used as the receipt number for the payment.  */  
   "PESUNATNum":string,
      /**  Document Tax Amount used in Peru detractions  */  
   "DocPEDetTaxAmt":number,
      /**  MXFiscalFolio  */  
   "MXFiscalFolio":string,
      /**  PEBOEIsMultiGen  */  
   "PEBOEIsMultiGen":boolean,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  PrePayHeadNum  */  
   "PrePayHeadNum":number,
      /**  MXRetentionCode  */  
   "MXRetentionCode":string,
      /**  PE Reference Document ID  */  
   "PERefDocID":string,
      /**  PE Reason Code  */  
   "PEReasonCode":string,
      /**  PE Reason Description  */  
   "PEReasonDesc":string,
      /**  Malaysia Import Declaration Number  */  
   "MYImportNum":string,
      /**  TW GUI Code Seller  */  
   "TWGUIRegNumSeller":string,
      /**  TW GUI Code Buyer  */  
   "TWGUIRegNumBuyer":string,
      /**  MXTARCode  */  
   "MXTARCode":string,
      /**  Flag that indicates if the invoice is a GRNI document.  */  
   "GRNIClearing":boolean,
      /**  CSF Peru - Fiscal Credit Operation Status  */  
   "PEFiscalCreditOperStatus":number,
      /**  CSF Peru - International Tax agreement  */  
   "PEInternatTaxAgr":string,
      /**  CSF Peru - Rent type  */  
   "PERentType":string,
      /**  CSF Peru - Purchase  type  */  
   "PEPurchaseType":string,
      /**  TH Reference Invoice Num  */  
   "THRefInvoiceNum":string,
      /**  TH Reference Vendor Num  */  
   "THRefVendorNum":number,
      /**  Day when a company sums up accounts payable for supplier  */  
   "JPSummarizationDate":string,
      /**  Date of a Payment Statement  */  
   "JPBillingDate":string,
      /**  Legal Number of Payment Statement  */  
   "JPBillingNumber":string,
      /**  SelfInvoice  */  
   "SelfInvoice":boolean,
      /**  Printed  */  
   "Printed":boolean,
      /**  PurPoint  */  
   "PurPoint":string,
      /**  PLInvoiceReference  */  
   "PLInvoiceReference":string,
      /**  INPortCode  */  
   "INPortCode":string,
      /**  Indicates which invoice number has cancelled this invoice.  */  
   "RefCancelledby":string,
      /**  Indicates if this invoice is a cancellation invoice.  */  
   "CancellationInv":boolean,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
      /**  WithholdAcctToInterim  */  
   "WithholdAcctToInterim":boolean,
      /**  APTaxRoundOption  */  
   "APTaxRoundOption":number,
      /**  Source Plant used for multi site GL  */  
   "SourcePlant":string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   "ExtSysType":string,
      /**  URL for drill back to an integrated external system  */  
   "ExtSysURL":string,
      /**  CHQRIBAN  */  
   "CHQRIBAN":string,
      /**  CHQRReference  */  
   "CHQRReference":string,
      /**  Set to True for any invoice that is created via EDI  */  
   "EDIInvoice":boolean,
      /**  This external field will hold Company.AllowMultInvcReceipts flag.  */  
   "AllowMultInvcReceipts":boolean,
      /**  Apply AP Pre Payment Automatically.  */  
   "ApplyAPPrePayAuto":boolean,
   "BankName":string,
   "BaseCurrencyID":string,
      /**  The base currency symbol  */  
   "BaseCurrSymbol":string,
      /**  The bill address in list format  */  
   "BillAddressList":string,
   "CanChangeTaxLiab":boolean,
      /**  IFRS Calculation. If the checkbox is not checked then all the elements below are disabled. If the checkbox is checked, then some elements below become enabled showing default values so that the NPV can be calculated  */  
   "COIFRSCalculation":boolean,
      /**  If true then Colombia IFRS Net Present Value calculation is enabled  */  
   "COIFRSEnabled":boolean,
      /**  Financial Charge  */  
   "COIFRSFinancialCharge":number,
   "COIFRSInterestRate":number,
      /**  Number of Periods for payment  */  
   "COIFRSNumberOfPeriods":number,
      /**  Present Value  */  
   "COIFRSPresentValue":number,
      /**  Flag to indicate if the CPay invoice has been received/trasferred to the corporate.  */  
   "CPayIMReceived":boolean,
      /**  Indicates if the CPay invoice is still an open payable at Corporate  */  
   "CPayOpenPayable":boolean,
   "CumulativeBalance":number,
   "CurrencySwitch":boolean,
   "CurrInstanceNum":number,
      /**  The document currency symbol  */  
   "CurrSymbol":string,
      /**   The flag to indicate if Invoice Header Apply Date is supposed to be Read Only
(There are any detail/misc lines and not DMR Debit Memo invoice)  */  
   "DisableAplDate":boolean,
      /**  Financial Charge  */  
   "DocCOIFRSFinancialCharge":number,
      /**  Present Value  */  
   "DocCOIFRSPresentValue":number,
   "DocCumulativeBalance":number,
      /**  The doc invoice variance amount  */  
   "DocInvoiceVariance":number,
   "DocMiscChrgNonDeducTax":number,
   "DocMiscChrgVariance":number,
   "DocScrHdrExpTotal":number,
   "DocSourceRecurBalance":number,
      /**   Taiwan Localization           
Display Field for Gui Import Tax Basis  */  
   "DspGuiImportTaxBasis":number,
   "EnableAssignLegNum":boolean,
      /**  Indicates when to enable the CPay field.  */  
   "EnableCPay":boolean,
   "EnableDueDate":boolean,
   "EnableExchangeRate":boolean,
   "EnableLockRate":boolean,
   "EnableTaxExRate":boolean,
   "EnableTaxLock":boolean,
      /**  Enable setting of Transaction Document Type  */  
   "EnableTranDocType":boolean,
   "EnableVoidLegNum":boolean,
      /**  Indicates which date to be used to calculate the exchange rate, I for Invoice Date, A for Apply Date.  */  
   "ExchangeRateDate":string,
      /**   Taiwan Localization           
The flag to indicate if GUITaxBasis prompt is available  */  
   "GuiTaxBasisFlag":boolean,
   "HasLegNumCnfg":boolean,
      /**  IBAN Code  */  
   "IBANCode":string,
      /**  for Bill of Exchange  */  
   "InvoiceTypeDesc":string,
      /**  The invoice variance amount  */  
   "InvoiceVariance":number,
   "IsLatestRecurrence":boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Is Only Misc lines exits  */  
   "IsOnlyMiscRecords":boolean,
      /**  LAC Tax Calculation Enabled  */  
   "LACTaxCalcEnabled":boolean,
   "LatestInvoice":number,
   "LatestInvString":string,
   "LegalNumberMessage":string,
      /**  Indicates if lines or misc charges exist for the invoice  */  
   "LineOrMscChrgExists":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
   "MiscChrgNonDeducTax":number,
   "MiscChrgVariance":number,
      /**  NextInvoiceDate = InvcRecurringCycle.LastDate + RecurringCycle.Interval in RecurringCycle.Modifier units  */  
   "NextInvoiceDate":string,
   "NoChangeRecur":boolean,
      /**  Pay Method Type  */  
   "PayMethod":string,
      /**  CSF Peru - Fiscal Credit Operation Status  */  
   "PEFiscalCreditOperStatusDsp":string,
      /**  Peru Localization Field, Field to disable Non-Resident Inovices Fields.  */  
   "PEIsNRInvc":boolean,
      /**  CSF Poland. Vendor uses Invoice reference number  */  
   "PLVendorAutoInvoiceNum":boolean,
   "PostInvtyWipCos":boolean,
      /**   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  */  
   "RecalcAmts":string,
      /**  Recurring Source flag  */  
   "Recurring":boolean,
   "RecurringState":string,
      /**  Financial Charge  */  
   "Rpt1COIFRSFinancialCharge":number,
      /**  Present Value  */  
   "Rpt1COIFRSPresentValue":number,
   "Rpt1CumulativeBalance":number,
   "Rpt1InvoiceVariance":number,
   "Rpt1MiscChrgNonDeducTax":number,
   "Rpt1MiscChrgVariance":number,
   "Rpt1ScrDiscountAmt":number,
   "Rpt1ScrHdrExpTotal":number,
   "Rpt1ScrHdrMiscChrgTotal":number,
   "Rpt1ScrInvLineTotal":number,
   "Rpt1ScrInvoiceAmt":number,
   "Rpt1ScrInvoiceBal":number,
   "Rpt1ScrInvoiceVendorAmt":number,
      /**  Rpt1 Scr LAC Tax Amt  */  
   "Rpt1ScrLACTaxAmt":number,
   "Rpt1ScrRounding":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTotBOEWithholding":number,
   "Rpt1ScrTotDedTaxAmt":number,
   "Rpt1ScrTotInvoiceAmt":number,
   "Rpt1ScrTotReportableAmt":number,
   "Rpt1ScrTotSelfAmt":number,
   "Rpt1ScrTotTaxableAmt":number,
   "Rpt1ScrTotWithholdingAmt":number,
   "Rpt1ScrUnpostedBal":number,
   "Rpt1SourceRecurBalance":number,
      /**  Financial Charge  */  
   "Rpt2COIFRSFinancialCharge":number,
      /**  Present Value  */  
   "Rpt2COIFRSPresentValue":number,
   "Rpt2CumulativeBalance":number,
   "Rpt2InvoiceVariance":number,
   "Rpt2MiscChrgNonDeducTax":number,
   "Rpt2MiscChrgVariance":number,
   "Rpt2ScrDiscountAmt":number,
   "Rpt2ScrHdrExpTotal":number,
   "Rpt2ScrHdrMiscChrgTotal":number,
   "Rpt2ScrInvLineTotal":number,
   "Rpt2ScrInvoiceAmt":number,
   "Rpt2ScrInvoiceBal":number,
   "Rpt2ScrInvoiceVendorAmt":number,
      /**  Rpt2 Scr LAC Tax Amt  */  
   "Rpt2ScrLACTaxAmt":number,
   "Rpt2ScrRounding":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTotBOEWithholding":number,
   "Rpt2ScrTotDedTaxAmt":number,
   "Rpt2ScrTotInvoiceAmt":number,
   "Rpt2ScrTotReportableAmt":number,
   "Rpt2ScrTotSelfAmt":number,
   "Rpt2ScrTotTaxableAmt":number,
   "Rpt2ScrTotWithholdingAmt":number,
   "Rpt2ScrUnpostedBal":number,
   "Rpt2SourceRecurBalance":number,
      /**  Financial Charge  */  
   "Rpt3COIFRSFinancialCharge":number,
      /**  Present Value  */  
   "Rpt3COIFRSPresentValue":number,
   "Rpt3CumulativeBalance":number,
   "Rpt3InvoiceVariance":number,
   "Rpt3MiscChrgNonDeducTax":number,
   "Rpt3MiscChrgVariance":number,
   "Rpt3ScrDiscountAmt":number,
   "Rpt3ScrHdrExpTotal":number,
   "Rpt3ScrHdrMiscChrgTotal":number,
   "Rpt3ScrInvLineTotal":number,
   "Rpt3ScrInvoiceAmt":number,
   "Rpt3ScrInvoiceBal":number,
   "Rpt3ScrInvoiceVendorAmt":number,
      /**  Rpt3 Scr LAC Tax Amt  */  
   "Rpt3ScrLACTaxAmt":number,
   "Rpt3ScrRounding":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTotBOEWithholding":number,
   "Rpt3ScrTotDedTaxAmt":number,
   "Rpt3ScrTotInvoiceAmt":number,
   "Rpt3ScrTotReportableAmt":number,
   "Rpt3ScrTotSelfAmt":number,
   "Rpt3ScrTotTaxableAmt":number,
   "Rpt3ScrTotWithholdingAmt":number,
   "Rpt3ScrUnpostedBal":number,
   "Rpt3SourceRecurBalance":number,
   "RptScrTotWithholdingAmt":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "ScrDiscountAmt":number,
   "ScrDocDiscountAmt":number,
   "ScrDocHdrMiscChrgTotal":number,
   "ScrDocInvLineTotal":number,
   "ScrDocInvoiceAmt":number,
   "ScrDocInvoiceBal":number,
   "ScrDocInvoiceVendorAmt":number,
   "ScrDocRounding":number,
   "ScrDocTaxAmt":number,
   "ScrDocTotBOEWithholding":number,
   "ScrDocTotDedTaxAmt":number,
   "ScrDocTotInvoiceAmt":number,
   "ScrDocTotReportableAmt":number,
   "ScrDocTotSelfAmt":number,
   "ScrDocTotTaxableAmt":number,
   "ScrDocTotWithholdingAmt":number,
   "ScrDocUnpostedBal":number,
   "ScrHdrExpTotal":number,
   "ScrHdrMiscChrgTotal":number,
   "ScrInvLineTotal":number,
   "ScrInvoiceAmt":number,
   "ScrInvoiceBal":number,
   "ScrInvoiceRef":string,
   "ScrInvoiceVendorAmt":number,
      /**  Scr LAC Doc Tax Amt  */  
   "ScrLACDocTaxAmt":number,
      /**  Scr LAC Tax Amt  */  
   "ScrLACTaxAmt":number,
   "ScrRounding":number,
      /**  The screen tax amount  */  
   "ScrTaxAmt":number,
      /**  Total of withholdings of all BOE Lines.  */  
   "ScrTotBOEWithholding":number,
   "ScrTotDedTaxAmt":number,
      /**  Shall be the sum of column 'Tax Amount' for all lines with collection method 'Invoice'  */  
   "ScrTotInvoiceAmt":number,
   "ScrTotReportableAmt":number,
      /**  shall be the sum of column 'Tax Amount' for all lines with collection method 'Self-Assessed' or mehtod 'Self-Assessed'  */  
   "ScrTotSelfAmt":number,
   "ScrTotTaxableAmt":number,
      /**  shall be the sum of column 'Tax Amount' for all lines with collection  method 'Withholding'  */  
   "ScrTotWithholdingAmt":number,
   "ScrUnpostedBal":number,
   "SkipRecurring":boolean,
      /**  Recurrent Invoices functionality  */  
   "SourceInvoiceNum":string,
   "SourceLastDate":string,
   "SourceRecurBalance":number,
      /**  Swift Code  */  
   "SwiftCode":string,
      /**  System Transaction Type: APInvoice/DebitMemo  is used in the filter of TranDocType combo-box.  */  
   "SystemTranType":string,
   "TaxExchangeRate":number,
   "TaxLinesExist":boolean,
   "TaxRateLinesExist":boolean,
   "TotalInstanceNum":number,
      /**  Link to TranDocType table, can be removed when path filed TranDocTypeID is replaced with actual one.  */  
   "TranDocTypeDescription":string,
      /**  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  */  
   "TransApplyDate":string,
   "UseTaxRate":boolean,
      /**  Indicates if the vendor on the invoice is active or not.  */  
   "VendorInactive":boolean,
      /**  Indicates if the vendor on the invoice is in a pay hold state.  */  
   "VendorPayHold":boolean,
   "VNDateReceived":string,
   "VNInvoiceType":string,
      /**  Exchange Rate Label  */  
   "XRateLabel":string,
   "AllowChgAfterPrint":boolean,
      /**  Formatted Supplier Name and Address  */  
   "FormattedVendorNameAddress":string,
      /**  Site is a LegalEntity  */  
   "SiteIsLegalEntity":boolean,
   "BitFlag":number,
   "AGCustomsDescription":string,
   "AGDestinationDescription":string,
   "APInvRecurringCycleInactive":boolean,
   "APInvRecurringCycleDescription":string,
   "APLOCIDDescription":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeDocumentDesc":string,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
   "JournalCodeJrnlDescription":string,
   "PayMethodType":number,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodName":string,
   "RateGrpCodeDescription":string,
   "SourcePlantName":string,
   "TaxRateGrpDescription":string,
   "TaxRegionCodeDescription":string,
   "TermsCodeDescription":string,
   "TermsCodeTermsType":string,
   "THRefVendorNumName":string,
   "THRefVendorNumVendorID":string,
   "VendBankPMUID":number,
   "VendBankCardCode":string,
   "VendBankBankAcctNumber":string,
   "VendBankIBANCode":string,
   "VendBankBankGiroAcctNbr":string,
   "VendBankSwiftNum":string,
   "VendBankLocalBIC":string,
   "VendBankBankName":string,
   "VendorNumCurrencyCode":string,
   "VendorNumZIP":string,
   "VendorNumAddress2":string,
   "VendorNumAddress3":string,
   "VendorNumCity":string,
   "VendorNumAddress1":string,
   "VendorNumCountry":string,
   "VendorNumVendorID":string,
   "VendorNumTermsCode":string,
   "VendorNumDefaultFOB":string,
   "VendorNumState":string,
   "VendorNumName":string,
   "XbSystAPTaxLnLevel":boolean,
   "XbSystIsDiscountforDebitM":boolean,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param vendorNum
      @param invoiceNum
   */  
export interface DeleteByID_input{
   vendorNum:number,
   invoiceNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_APInvHedListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this is an "open" Payable.  */  
   OpenPayable:boolean,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   InvoiceNum:string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   DebitMemo:boolean,
      /**  Invoice date.  */  
   InvoiceDate:string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   TaxAmt:number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  */  
   FiscalPeriod:number,
      /**  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  */  
   InvoiceRef:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  */  
   InvoiceHeld:boolean,
      /**  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  */  
   PayHold:boolean,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   Description:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  */  
   CPay:boolean,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  */  
   CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  */  
   CPayDocInvoiceBal:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Indicates that this is pre-payment invoice.  */  
   PrePayment:boolean,
      /**  Letter of Credit ID.  */  
   APLOCID:string,
      /**  Transaction Document Type ID  */  
   TranDocTypeID:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  TWDeclareYear  */  
   TWDeclareYear:number,
      /**  TWDeclarePeriod  */  
   TWDeclarePeriod:number,
      /**  Invoice Type  */  
   InvoiceType:string,
      /**  PLInvoiceReference  */  
   PLInvoiceReference:string,
   ScrInvoiceVendorAmt:number,
   ScrDocInvoiceVendorAmt:number,
   ScrInvoiceAmt:number,
   ScrDocInvoiceAmt:number,
   ScrInvoiceBal:number,
   ScrDocInvoiceBal:number,
   ScrUnpostedBal:number,
   ScrDocUnpostedBal:number,
   InvoiceVariance:number,
   DocInvoiceVariance:number,
      /**  Indicates if the CPay invoice is still an open payable at Corporate  */  
   CPayOpenPayable:boolean,
      /**  Supplier Name  */  
   VendorNumName:string,
      /**  Supplier ID  */  
   VendorNumVendorID:string,
   TranDocTypeDescription:string,
   Rpt1ScrInvoiceAmt:number,
   Rpt2ScrInvoiceAmt:number,
   Rpt3ScrInvoiceAmt:number,
   Rpt1InvoiceVariance:number,
   Rpt2InvoiceVariance:number,
   Rpt3InvoiceVariance:number,
   Rpt1ScrInvoiceVendorAmt:number,
   Rpt2ScrInvoiceVendorAmt:number,
   Rpt3ScrInvoiceVendorAmt:number,
   IsLcked:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvHedListTableset{
   APInvHedList:Erp_Tablesets_APInvHedListRow[],
   APInvHedTransferList:Erp_Tablesets_APInvHedTransferListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APInvHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this is an "open" Payable.  */  
   OpenPayable:boolean,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   InvoiceNum:string,
      /**   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  */  
   DebitMemo:boolean,
      /**  Invoice date.  */  
   InvoiceDate:string,
      /**  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  */  
   TaxAmt:number,
      /**  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  */  
   DocTaxAmt:number,
      /**  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  */  
   DiscountDate:string,
      /**  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DiscountAmt:number,
      /**  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  */  
   DocDiscountAmt:number,
      /**  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDates:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   PayAmounts:string,
      /**  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   DocPayAmounts:string,
      /**  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  */  
   GLPosted:boolean,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  */  
   FiscalPeriod:number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   StartUp:boolean,
      /**  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  */  
   InvoiceRef:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Used to establish invoice comments about the overall invoice.  */  
   InvoiceComment:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  */  
   DocInvoiceVendorAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnpostedBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   DocUnpostedBal:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  */  
   InvoiceHeld:boolean,
      /**  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  */  
   PayHold:boolean,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   Description:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  */  
   REFPONum:number,
      /**  The Tax Region for this invoice.  */  
   TaxRegionCode:string,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Journal that invoice was posted to.  */  
   JournalCode:string,
      /**  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  */  
   UpdateTax:boolean,
      /**  For use by external G/L interfacing.  This field is sign flipped for debit memos.  */  
   InvoiceVendorAmt:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  External Identification of the Invoice.  */  
   ExternalID:string,
      /**  Allows user to control discount amount manually or automatically  */  
   FixedAmt:boolean,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefInvoiceNum:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceNum:string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   DepGainLoss:number,
      /**  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  */  
   CPay:boolean,
      /**  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  */  
   CPayLinked:boolean,
      /**  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  */  
   CPayLegalNumber:string,
      /**  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   CPayCheckNum:number,
      /**  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  */  
   CPayCheckDate:string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  */  
   CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  */  
   CPayDocInvoiceBal:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  */  
   GLControlType:string,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  */  
   GLControlCode:string,
      /**  Reporting currency value of this field  */  
   Rpt1DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DiscountAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceVendorAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt2PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt3PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnpostedBal:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt1CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt2CPayInvoiceBal:number,
      /**  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  */  
   Rpt3CPayInvoiceBal:number,
      /**  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  */  
   AllowOverrideLI:boolean,
      /**  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  */  
   MatchedFromLI:boolean,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDiscDays:string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   PayDiscPer:string,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PayDiscPartPay:boolean,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   PIPayment:string,
      /**  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden and Finland Localization Field - Banking Reference  */  
   SEBankRef:string,
      /**  Sweden and Finland Localization Field - Payment Code  */  
   SEPayCode:string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Indicates that this is pre-payment invoice.  */  
   PrePayment:boolean,
      /**  Letter of Credit ID.  */  
   APLOCID:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**   Taiwan Localization
Tax Amount Basis  */  
   GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in document currrency  */  
   DocGUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt1 currency  */  
   Rpt1GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt2 currency  */  
   Rpt2GUIImportTaxBasis:number,
      /**   Taiwan Localization
Tax Amount Basis in Rpt3 currency  */  
   Rpt3GUIImportTaxBasis:number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   OvrDefTaxDate:boolean,
      /**  Linked flag  */  
   Linked:boolean,
      /**  The claim reference from the expense group that generated the invoice.  */  
   ClaimRef:string,
      /**  The employee from the group of expenses that created the invoice.  */  
   EmpID:string,
      /**  Indicates that Invoice has been selected for payment in a bankfile  */  
   InBankFile:boolean,
      /**  Credit Note Confirmation Date  */  
   CNConfirmDate:string,
      /**  Unique ID of the vendor's bank.  */  
   BankID:string,
      /**  Legal Number for the self assessment.  */  
   SelfLegalNumber:string,
      /**  Transaction Document Type for the self assessment.  */  
   SelfTranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**   Denmark Localization
Card (payment) code  */  
   CardCode:string,
      /**  Site Code  */  
   SiteCode:string,
      /**   Denmark Localization
Account Number  */  
   BankGiroAcctNbr:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Supplier Agent Name  */  
   SupAgentName:string,
      /**  Supplier Agent Tax Region Number  */  
   SupAgentTaxRegNo:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Card ID  */  
   CardID:string,
      /**  Card Holder Tax ID  */  
   CardHolderTaxID:string,
      /**  Card Member Name  */  
   CardMemberName:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Non Deductable VAT Amount  */  
   NonDeductVATAmt:number,
      /**  Non Deductable VAT Doc Amount  */  
   NonDeductVATDocAmt:number,
      /**  Non Deductable VAT Rpt1 Amount  */  
   NonDeductVATRpt1Amt:number,
      /**  Non Deductable VAT Rpt2 Amount  */  
   NonDeductVATRpt2Amt:number,
      /**  Non Deductable VAT Rpt3 Amount  */  
   NonDeductVATRpt3Amt:number,
      /**  Stores the number of the import document.  */  
   ImportNum:string,
      /**  Country of Import  */  
   ImportedFrom:string,
      /**  Date of import.  */  
   ImportedDate:string,
      /**   Indicates that this is Advanced Tax invoice received from
supplier  */  
   AdvTaxInv:boolean,
      /**   Indicates that the tax is included in the unit price
for this AP Invoice  */  
   InPrice:boolean,
      /**  Transaction Document Type ID  */  
   TranDocTypeID:string,
      /**  Reserved for Development - Integer  */  
   DevInt1:number,
      /**  Reserved for Development - Integer  */  
   DevInt2:number,
      /**  Reserved for development - decimal  */  
   DevDec1:number,
      /**  Reserved for development - decimal  */  
   DevDec2:number,
      /**  Reserved for development - decimal  */  
   DevDec3:number,
      /**  Reserved for development - decimal  */  
   DevDec4:number,
      /**  In case of Tax Inclusive Pricing if system-calculated Header related taxes are changed/deleted/added  by the user - this field is set to true by the system.  */  
   DevLog1:boolean,
      /**  Reserved for development - logical  */  
   DevLog2:boolean,
      /**  Assigned as "I" when Recurring Invoice has Inactive status.  */  
   DevChar1:string,
      /**  Reserved for development - character  */  
   DevChar2:string,
      /**  Reserved for development - date  */  
   DevDate1:string,
      /**  Reserved for development - date  */  
   DevDate2:string,
      /**  PaymentNumber  */  
   PaymentNumber:string,
      /**  CycleCode  */  
   CycleCode:string,
      /**  Duration  */  
   Duration:number,
      /**  EndDate  */  
   EndDate:string,
      /**  MaxValueAmt  */  
   MaxValueAmt:number,
      /**  DocMaxValueAmt  */  
   DocMaxValueAmt:number,
      /**  Rpt1MaxValueAmt  */  
   Rpt1MaxValueAmt:number,
      /**  Rpt2MaxValueAmt  */  
   Rpt2MaxValueAmt:number,
      /**  Rpt3MaxValueAmt  */  
   Rpt3MaxValueAmt:number,
      /**  HoldInvoice  */  
   HoldInvoice:boolean,
      /**  CopyLatestInvoice  */  
   CopyLatestInvoice:boolean,
      /**  OverrideEndDate  */  
   OverrideEndDate:boolean,
      /**  CycleInactive  */  
   CycleInactive:boolean,
      /**  RecurSource  */  
   RecurSource:boolean,
      /**  InstanceNum  */  
   InstanceNum:number,
      /**  RecurBalance  */  
   RecurBalance:number,
      /**  DocRecurBalance  */  
   DocRecurBalance:number,
      /**  Rpt1RecurBalance  */  
   Rpt1RecurBalance:number,
      /**  Rpt2RecurBalance  */  
   Rpt2RecurBalance:number,
      /**  Rpt3RecurBalance  */  
   Rpt3RecurBalance:number,
      /**  LastDate  */  
   LastDate:string,
      /**  IsRecurring  */  
   IsRecurring:boolean,
      /**  InvoiceNumList  */  
   InvoiceNumList:string,
      /**  IsMaxValue  */  
   IsMaxValue:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHISRCodeLine  */  
   CHISRCodeLine:string,
      /**  DMReason  */  
   DMReason:string,
      /**  UrgentPayment  */  
   UrgentPayment:boolean,
      /**  AGDocPageNum  */  
   AGDocPageNum:string,
      /**  AGCAICAEMark  */  
   AGCAICAEMark:string,
      /**  AGCAICAENum  */  
   AGCAICAENum:string,
      /**  AGCAICAEExpirationDate  */  
   AGCAICAEExpirationDate:string,
      /**  AGAvTaxCreditFlag  */  
   AGAvTaxCreditFlag:boolean,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGCustomsClearanceNum  */  
   AGCustomsClearanceNum:string,
      /**  AGCustomsCode  */  
   AGCustomsCode:string,
      /**  AGDestinationCode  */  
   AGDestinationCode:string,
      /**  Header Number  */  
   HeadNum:number,
      /**  TranType  */  
   TranType:string,
      /**  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  */  
   TaxSvcID:string,
      /**  TWDeclareYear  */  
   TWDeclareYear:number,
      /**  TWDeclarePeriod  */  
   TWDeclarePeriod:number,
      /**  AP Checking Group ID  */  
   APChkGrpID:string,
      /**  Invoice Type  */  
   InvoiceType:string,
      /**  Indicates a computational cost for the invoice  */  
   PEComputationalCost:string,
      /**  Referenced By BOE  */  
   ReferencedByBOE:string,
      /**  DUA Reference Number used on Peru Localiation  */  
   PEDUARefNum:string,
      /**  CustomsNumber  */  
   CustomsNumber:string,
      /**  ReceivedDate  */  
   ReceivedDate:string,
      /**  CustOverride  */  
   CustOverride:number,
      /**  Invoice Number of Invoice Pre-Payment which should be automatically applied to this one during posting process.  */  
   PrePaymentNum:string,
      /**  Pre-Payment amount in Base Currency.  */  
   PrePaymentAmt:number,
      /**  Pre-Payment amount in Document Currency.  */  
   DocPrePaymentAmt:number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   Rpt1PrePaymentAmt:number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   Rpt2PrePaymentAmt:number,
      /**  Pre-Payment amount in Reporting Currency.  */  
   Rpt3PrePaymentAmt:number,
      /**  CSF Peru - AP Payment Number  */  
   PEAPPayNum:number,
      /**  SCF Peru - Detractions Tax Amount  */  
   PEDetTaxAmt:number,
      /**  Peru Detraction Tax Currency Code  */  
   PEDetTaxCurrencyCode:string,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   PESUNATDepAmt:number,
      /**  Peru Document SUNAT Deposit Amount  */  
   DocPESUNATDepAmt:number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   PESUNATDepDate:string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   PESUNATDepNum:string,
      /**  SUNAT Reference Number. Once a payment is made, the SUNAT returns a reference number used as the receipt number for the payment.  */  
   PESUNATNum:string,
      /**  Document Tax Amount used in Peru detractions  */  
   DocPEDetTaxAmt:number,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  PEBOEIsMultiGen  */  
   PEBOEIsMultiGen:boolean,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  PrePayHeadNum  */  
   PrePayHeadNum:number,
      /**  MXRetentionCode  */  
   MXRetentionCode:string,
      /**  PE Reference Document ID  */  
   PERefDocID:string,
      /**  PE Reason Code  */  
   PEReasonCode:string,
      /**  PE Reason Description  */  
   PEReasonDesc:string,
      /**  Malaysia Import Declaration Number  */  
   MYImportNum:string,
      /**  TW GUI Code Seller  */  
   TWGUIRegNumSeller:string,
      /**  TW GUI Code Buyer  */  
   TWGUIRegNumBuyer:string,
      /**  MXTARCode  */  
   MXTARCode:string,
      /**  Flag that indicates if the invoice is a GRNI document.  */  
   GRNIClearing:boolean,
      /**  CSF Peru - Fiscal Credit Operation Status  */  
   PEFiscalCreditOperStatus:number,
      /**  CSF Peru - International Tax agreement  */  
   PEInternatTaxAgr:string,
      /**  CSF Peru - Rent type  */  
   PERentType:string,
      /**  CSF Peru - Purchase  type  */  
   PEPurchaseType:string,
      /**  TH Reference Invoice Num  */  
   THRefInvoiceNum:string,
      /**  TH Reference Vendor Num  */  
   THRefVendorNum:number,
      /**  Day when a company sums up accounts payable for supplier  */  
   JPSummarizationDate:string,
      /**  Date of a Payment Statement  */  
   JPBillingDate:string,
      /**  Legal Number of Payment Statement  */  
   JPBillingNumber:string,
      /**  SelfInvoice  */  
   SelfInvoice:boolean,
      /**  Printed  */  
   Printed:boolean,
      /**  PurPoint  */  
   PurPoint:string,
      /**  PLInvoiceReference  */  
   PLInvoiceReference:string,
      /**  INPortCode  */  
   INPortCode:string,
      /**  Indicates which invoice number has cancelled this invoice.  */  
   RefCancelledby:string,
      /**  Indicates if this invoice is a cancellation invoice.  */  
   CancellationInv:boolean,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  WithholdAcctToInterim  */  
   WithholdAcctToInterim:boolean,
      /**  APTaxRoundOption  */  
   APTaxRoundOption:number,
      /**  Source Plant used for multi site GL  */  
   SourcePlant:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
      /**  CHQRIBAN  */  
   CHQRIBAN:string,
      /**  CHQRReference  */  
   CHQRReference:string,
      /**  Set to True for any invoice that is created via EDI  */  
   EDIInvoice:boolean,
      /**  This external field will hold Company.AllowMultInvcReceipts flag.  */  
   AllowMultInvcReceipts:boolean,
      /**  Apply AP Pre Payment Automatically.  */  
   ApplyAPPrePayAuto:boolean,
   BankName:string,
   BaseCurrencyID:string,
      /**  The base currency symbol  */  
   BaseCurrSymbol:string,
      /**  The bill address in list format  */  
   BillAddressList:string,
   CanChangeTaxLiab:boolean,
      /**  IFRS Calculation. If the checkbox is not checked then all the elements below are disabled. If the checkbox is checked, then some elements below become enabled showing default values so that the NPV can be calculated  */  
   COIFRSCalculation:boolean,
      /**  If true then Colombia IFRS Net Present Value calculation is enabled  */  
   COIFRSEnabled:boolean,
      /**  Financial Charge  */  
   COIFRSFinancialCharge:number,
   COIFRSInterestRate:number,
      /**  Number of Periods for payment  */  
   COIFRSNumberOfPeriods:number,
      /**  Present Value  */  
   COIFRSPresentValue:number,
      /**  Flag to indicate if the CPay invoice has been received/trasferred to the corporate.  */  
   CPayIMReceived:boolean,
      /**  Indicates if the CPay invoice is still an open payable at Corporate  */  
   CPayOpenPayable:boolean,
   CumulativeBalance:number,
   CurrencySwitch:boolean,
   CurrInstanceNum:number,
      /**  The document currency symbol  */  
   CurrSymbol:string,
      /**   The flag to indicate if Invoice Header Apply Date is supposed to be Read Only
(There are any detail/misc lines and not DMR Debit Memo invoice)  */  
   DisableAplDate:boolean,
      /**  Financial Charge  */  
   DocCOIFRSFinancialCharge:number,
      /**  Present Value  */  
   DocCOIFRSPresentValue:number,
   DocCumulativeBalance:number,
      /**  The doc invoice variance amount  */  
   DocInvoiceVariance:number,
   DocMiscChrgNonDeducTax:number,
   DocMiscChrgVariance:number,
   DocScrHdrExpTotal:number,
   DocSourceRecurBalance:number,
      /**   Taiwan Localization           
Display Field for Gui Import Tax Basis  */  
   DspGuiImportTaxBasis:number,
   EnableAssignLegNum:boolean,
      /**  Indicates when to enable the CPay field.  */  
   EnableCPay:boolean,
   EnableDueDate:boolean,
   EnableExchangeRate:boolean,
   EnableLockRate:boolean,
   EnableTaxExRate:boolean,
   EnableTaxLock:boolean,
      /**  Enable setting of Transaction Document Type  */  
   EnableTranDocType:boolean,
   EnableVoidLegNum:boolean,
      /**  Indicates which date to be used to calculate the exchange rate, I for Invoice Date, A for Apply Date.  */  
   ExchangeRateDate:string,
      /**   Taiwan Localization           
The flag to indicate if GUITaxBasis prompt is available  */  
   GuiTaxBasisFlag:boolean,
   HasLegNumCnfg:boolean,
      /**  IBAN Code  */  
   IBANCode:string,
      /**  for Bill of Exchange  */  
   InvoiceTypeDesc:string,
      /**  The invoice variance amount  */  
   InvoiceVariance:number,
   IsLatestRecurrence:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Is Only Misc lines exits  */  
   IsOnlyMiscRecords:boolean,
      /**  LAC Tax Calculation Enabled  */  
   LACTaxCalcEnabled:boolean,
   LatestInvoice:number,
   LatestInvString:string,
   LegalNumberMessage:string,
      /**  Indicates if lines or misc charges exist for the invoice  */  
   LineOrMscChrgExists:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   MiscChrgNonDeducTax:number,
   MiscChrgVariance:number,
      /**  NextInvoiceDate = InvcRecurringCycle.LastDate + RecurringCycle.Interval in RecurringCycle.Modifier units  */  
   NextInvoiceDate:string,
   NoChangeRecur:boolean,
      /**  Pay Method Type  */  
   PayMethod:string,
      /**  CSF Peru - Fiscal Credit Operation Status  */  
   PEFiscalCreditOperStatusDsp:string,
      /**  Peru Localization Field, Field to disable Non-Resident Inovices Fields.  */  
   PEIsNRInvc:boolean,
      /**  CSF Poland. Vendor uses Invoice reference number  */  
   PLVendorAutoInvoiceNum:boolean,
   PostInvtyWipCos:boolean,
      /**   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  */  
   RecalcAmts:string,
      /**  Recurring Source flag  */  
   Recurring:boolean,
   RecurringState:string,
      /**  Financial Charge  */  
   Rpt1COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt1COIFRSPresentValue:number,
   Rpt1CumulativeBalance:number,
   Rpt1InvoiceVariance:number,
   Rpt1MiscChrgNonDeducTax:number,
   Rpt1MiscChrgVariance:number,
   Rpt1ScrDiscountAmt:number,
   Rpt1ScrHdrExpTotal:number,
   Rpt1ScrHdrMiscChrgTotal:number,
   Rpt1ScrInvLineTotal:number,
   Rpt1ScrInvoiceAmt:number,
   Rpt1ScrInvoiceBal:number,
   Rpt1ScrInvoiceVendorAmt:number,
      /**  Rpt1 Scr LAC Tax Amt  */  
   Rpt1ScrLACTaxAmt:number,
   Rpt1ScrRounding:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTotBOEWithholding:number,
   Rpt1ScrTotDedTaxAmt:number,
   Rpt1ScrTotInvoiceAmt:number,
   Rpt1ScrTotReportableAmt:number,
   Rpt1ScrTotSelfAmt:number,
   Rpt1ScrTotTaxableAmt:number,
   Rpt1ScrTotWithholdingAmt:number,
   Rpt1ScrUnpostedBal:number,
   Rpt1SourceRecurBalance:number,
      /**  Financial Charge  */  
   Rpt2COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt2COIFRSPresentValue:number,
   Rpt2CumulativeBalance:number,
   Rpt2InvoiceVariance:number,
   Rpt2MiscChrgNonDeducTax:number,
   Rpt2MiscChrgVariance:number,
   Rpt2ScrDiscountAmt:number,
   Rpt2ScrHdrExpTotal:number,
   Rpt2ScrHdrMiscChrgTotal:number,
   Rpt2ScrInvLineTotal:number,
   Rpt2ScrInvoiceAmt:number,
   Rpt2ScrInvoiceBal:number,
   Rpt2ScrInvoiceVendorAmt:number,
      /**  Rpt2 Scr LAC Tax Amt  */  
   Rpt2ScrLACTaxAmt:number,
   Rpt2ScrRounding:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTotBOEWithholding:number,
   Rpt2ScrTotDedTaxAmt:number,
   Rpt2ScrTotInvoiceAmt:number,
   Rpt2ScrTotReportableAmt:number,
   Rpt2ScrTotSelfAmt:number,
   Rpt2ScrTotTaxableAmt:number,
   Rpt2ScrTotWithholdingAmt:number,
   Rpt2ScrUnpostedBal:number,
   Rpt2SourceRecurBalance:number,
      /**  Financial Charge  */  
   Rpt3COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt3COIFRSPresentValue:number,
   Rpt3CumulativeBalance:number,
   Rpt3InvoiceVariance:number,
   Rpt3MiscChrgNonDeducTax:number,
   Rpt3MiscChrgVariance:number,
   Rpt3ScrDiscountAmt:number,
   Rpt3ScrHdrExpTotal:number,
   Rpt3ScrHdrMiscChrgTotal:number,
   Rpt3ScrInvLineTotal:number,
   Rpt3ScrInvoiceAmt:number,
   Rpt3ScrInvoiceBal:number,
   Rpt3ScrInvoiceVendorAmt:number,
      /**  Rpt3 Scr LAC Tax Amt  */  
   Rpt3ScrLACTaxAmt:number,
   Rpt3ScrRounding:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTotBOEWithholding:number,
   Rpt3ScrTotDedTaxAmt:number,
   Rpt3ScrTotInvoiceAmt:number,
   Rpt3ScrTotReportableAmt:number,
   Rpt3ScrTotSelfAmt:number,
   Rpt3ScrTotTaxableAmt:number,
   Rpt3ScrTotWithholdingAmt:number,
   Rpt3ScrUnpostedBal:number,
   Rpt3SourceRecurBalance:number,
   RptScrTotWithholdingAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   ScrDiscountAmt:number,
   ScrDocDiscountAmt:number,
   ScrDocHdrMiscChrgTotal:number,
   ScrDocInvLineTotal:number,
   ScrDocInvoiceAmt:number,
   ScrDocInvoiceBal:number,
   ScrDocInvoiceVendorAmt:number,
   ScrDocRounding:number,
   ScrDocTaxAmt:number,
   ScrDocTotBOEWithholding:number,
   ScrDocTotDedTaxAmt:number,
   ScrDocTotInvoiceAmt:number,
   ScrDocTotReportableAmt:number,
   ScrDocTotSelfAmt:number,
   ScrDocTotTaxableAmt:number,
   ScrDocTotWithholdingAmt:number,
   ScrDocUnpostedBal:number,
   ScrHdrExpTotal:number,
   ScrHdrMiscChrgTotal:number,
   ScrInvLineTotal:number,
   ScrInvoiceAmt:number,
   ScrInvoiceBal:number,
   ScrInvoiceRef:string,
   ScrInvoiceVendorAmt:number,
      /**  Scr LAC Doc Tax Amt  */  
   ScrLACDocTaxAmt:number,
      /**  Scr LAC Tax Amt  */  
   ScrLACTaxAmt:number,
   ScrRounding:number,
      /**  The screen tax amount  */  
   ScrTaxAmt:number,
      /**  Total of withholdings of all BOE Lines.  */  
   ScrTotBOEWithholding:number,
   ScrTotDedTaxAmt:number,
      /**  Shall be the sum of column 'Tax Amount' for all lines with collection method 'Invoice'  */  
   ScrTotInvoiceAmt:number,
   ScrTotReportableAmt:number,
      /**  shall be the sum of column 'Tax Amount' for all lines with collection method 'Self-Assessed' or mehtod 'Self-Assessed'  */  
   ScrTotSelfAmt:number,
   ScrTotTaxableAmt:number,
      /**  shall be the sum of column 'Tax Amount' for all lines with collection  method 'Withholding'  */  
   ScrTotWithholdingAmt:number,
   ScrUnpostedBal:number,
   SkipRecurring:boolean,
      /**  Recurrent Invoices functionality  */  
   SourceInvoiceNum:string,
   SourceLastDate:string,
   SourceRecurBalance:number,
      /**  Swift Code  */  
   SwiftCode:string,
      /**  System Transaction Type: APInvoice/DebitMemo  is used in the filter of TranDocType combo-box.  */  
   SystemTranType:string,
   TaxExchangeRate:number,
   TaxLinesExist:boolean,
   TaxRateLinesExist:boolean,
   TotalInstanceNum:number,
      /**  Link to TranDocType table, can be removed when path filed TranDocTypeID is replaced with actual one.  */  
   TranDocTypeDescription:string,
      /**  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  */  
   TransApplyDate:string,
   UseTaxRate:boolean,
      /**  Indicates if the vendor on the invoice is active or not.  */  
   VendorInactive:boolean,
      /**  Indicates if the vendor on the invoice is in a pay hold state.  */  
   VendorPayHold:boolean,
   VNDateReceived:string,
   VNInvoiceType:string,
      /**  Exchange Rate Label  */  
   XRateLabel:string,
   AllowChgAfterPrint:boolean,
      /**  Formatted Supplier Name and Address  */  
   FormattedVendorNameAddress:string,
      /**  Site is a LegalEntity  */  
   SiteIsLegalEntity:boolean,
   BitFlag:number,
   AGCustomsDescription:string,
   AGDestinationDescription:string,
   APInvRecurringCycleInactive:boolean,
   APInvRecurringCycleDescription:string,
   APLOCIDDescription:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeDocumentDesc:string,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
   JournalCodeJrnlDescription:string,
   PayMethodType:number,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodName:string,
   RateGrpCodeDescription:string,
   SourcePlantName:string,
   TaxRateGrpDescription:string,
   TaxRegionCodeDescription:string,
   TermsCodeDescription:string,
   TermsCodeTermsType:string,
   THRefVendorNumName:string,
   THRefVendorNumVendorID:string,
   VendBankPMUID:number,
   VendBankCardCode:string,
   VendBankBankAcctNumber:string,
   VendBankIBANCode:string,
   VendBankBankGiroAcctNbr:string,
   VendBankSwiftNum:string,
   VendBankLocalBIC:string,
   VendBankBankName:string,
   VendorNumCurrencyCode:string,
   VendorNumZIP:string,
   VendorNumAddress2:string,
   VendorNumAddress3:string,
   VendorNumCity:string,
   VendorNumAddress1:string,
   VendorNumCountry:string,
   VendorNumVendorID:string,
   VendorNumTermsCode:string,
   VendorNumDefaultFOB:string,
   VendorNumState:string,
   VendorNumName:string,
   XbSystAPTaxLnLevel:boolean,
   XbSystIsDiscountforDebitM:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvHedTransferListRow{
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Company Identifier  */  
   Company:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Total invoice Amount (Vendors Currency). This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and the miscellaneous charges/credits records (APInvMsc). This field has a positive sign (debit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  User ID taht entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  The Group that the invoice was associated with during the data entry process. This field is not directly maintainable. it is assigned by the invoice entry program using teh GroupID of the "current" group that the user is working with. It is used as a selection criteria during the posting process.  */  
   GroupID:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and the miscellaneous charges/credits records (APInvMsc). This field has a positive sign (debit memos are negative).  */  
   InvoiceAmt:number,
      /**  Invoice date.  */  
   InvoiceDate:string,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoceHeld= false. This flag can be used for whatever the reason a user may wish to keep an invoice in a data entry group from being posted. This is NOT the same as putting an invoice on PaymentHold.  */  
   InvoiceHeld:boolean,
      /**  Vendor's invoice number.  */  
   InvoiceNum:string,
      /**  The Legal Number for the record. This number is created based on setup parameters in table LegalNumber  */  
   LegalNumber:string,
      /**  The internal VendorNum that ties back to the Vendor master file. This field is not directly maintainable, istead it is assigned from the Vendor. VendorNUmusing VendorID to find the Vendor record.  */  
   VendorNum:number,
      /**  Supplier Name  */  
   VendorNumName:string,
      /**  Supplier ID  */  
   VendorNumVendorID:string,
      /**  This is used to preserve the selected status of the row.  */  
   SelectedForAction:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvSearchTableset{
   APInvHed:Erp_Tablesets_APInvHedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtAPInvSearchTableset{
   APInvHed:Erp_Tablesets_APInvHedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param vendorNum
      @param invoiceNum
   */  
export interface GetByID_input{
   vendorNum:number,
   invoiceNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_APInvSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_APInvSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_APInvSearchTableset[],
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
   returnObj:Erp_Tablesets_APInvHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param vendorNum
   */  
export interface GetNewAPInvHed_input{
   ds:Erp_Tablesets_APInvSearchTableset[],
   vendorNum:number,
}

export interface GetNewAPInvHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvSearchTableset[],
}
}

   /** Required : 
      @param whereClauseAPInvHed
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAPInvHed:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_APInvSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtAPInvSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAPInvSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_APInvSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvSearchTableset[],
}
}

