import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.QuoteDtlSearchSvc
// Description: Quote Detail Search Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/$metadata", {
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
   Description: Get QuoteDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlRow
   */  
export function get_QuoteDtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/QuoteDtlSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuoteDtlSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/QuoteDtlSearches", {
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
   Summary: Calls GetByID to retrieve the QuoteDtlSearch item
   Description: Calls GetByID to retrieve the QuoteDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   */  
export function get_QuoteDtlSearches_Company_QuoteNum_QuoteLine(Company:string, QuoteNum:string, QuoteLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QuoteDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/QuoteDtlSearches(" + Company + "," + QuoteNum + "," + QuoteLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QuoteDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuoteDtlSearch for the service
   Description: Calls UpdateExt to update QuoteDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuoteDtlSearches_Company_QuoteNum_QuoteLine(Company:string, QuoteNum:string, QuoteLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/QuoteDtlSearches(" + Company + "," + QuoteNum + "," + QuoteLine + ")", {
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
   Summary: Call UpdateExt to delete QuoteDtlSearch item
   Description: Call UpdateExt to delete QuoteDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QuoteNum Desc: QuoteNum   Required: True
      @param QuoteLine Desc: QuoteLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuoteDtlSearches_Company_QuoteNum_QuoteLine(Company:string, QuoteNum:string, QuoteLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/QuoteDtlSearches(" + Company + "," + QuoteNum + "," + QuoteLine + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlListRow)
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
export function get_GetRows(whereClauseQuoteDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseQuoteDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuoteDtl=" + whereClauseQuoteDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/GetRows" + params, {
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
export function get_GetByID(quoteNum:string, quoteLine:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof quoteNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "quoteNum=" + quoteNum
   }
   if(typeof quoteLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "quoteLine=" + quoteLine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetListCustom
   Description: This methods will return all of the QuoteDtlSearch records which will be a subset
of the QuoteDtl records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (QuoteDtlList) we need our own public method.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/GetListCustom", {
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
   Summary: Invoke method GetNewQuoteDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuoteDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/GetNewQuoteDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteDtlListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QuoteDtlRow[],
}

export interface Erp_Tablesets_QuoteDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  */  
   "Ordered":boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   "PartNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  */  
   "XPartNum":string,
      /**  Contains comments about the detail line item. These will be printed on the Quote form.  */  
   "QuoteComment":string,
      /**  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  */  
   "LeadTime":string,
      /**  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   "Template":boolean,
      /**  Engineering Drawing Number. An optional field.  */  
   "DrawNum":string,
      /**  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  */  
   "JobComment":string,
      /**  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  */  
   "MfgDetail":boolean,
      /**  Indicates the Tax Category for this record. Defaults from the Part Master.  */  
   "TaxCatID":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  */  
   "CustNum":number,
      /**  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   "Quoted":boolean,
      /**  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   "Expired":boolean,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   "WIStartDate":string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   "WIStartHour":number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueDate":string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueHour":number,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  The quantity expected to be ordered. (In selling unit of measure)  */  
   "SellingExpectedQty":number,
      /**  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SellingExpectedUM":string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  */  
   "ConfidencePct":number,
      /**  The date this line was last updated  */  
   "LastUpdate":string,
      /**  The last User Is that updated this Quote  */  
   "LastDcdUserID":string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Discount":number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  */  
   "DocDiscount":number,
      /**  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   "ExpectedRevenue":number,
      /**  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   "DocExpectedRevenue":number,
      /**  The requested ship date for the sales order  */  
   "ReqShipDate":string,
      /**  The quantity to be used when a Sales order is created. (In selling unit of measure)  */  
   "OrderQty":number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingExpFactor":number,
      /**  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  */  
   "MultiRel":boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLine":string,
      /**  A Code which uniquely identifies a SalesCat record.  */  
   "SalesCatID":string,
      /**  Replicated from QuoteHed to easier sorting  */  
   "TerritoryID":string,
      /**   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   "CurrentStage":string,
      /**  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  */  
   "CreatedFrom":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  The date when the configuration was completed for the assembly.  */  
   "LastConfigDate":string,
      /**  The system time when the configuration was completed for the assembly.  */  
   "LastConfigTime":number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   "LastConfigUserID":string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   "ConfigUnitPrice":number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   "ConfigBaseUnitPrice":number,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  This is the Price List used to determine the starting base price.  */  
   "PriceListCode":string,
      /**  This is the Price List used to determine the break % or amount.  */  
   "BreakListCode":string,
      /**  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  */  
   "PricingQty":number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   "ListPrice":number,
      /**   Same as List price except that this field contains the list price in
QuoteHed).  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   "OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  */  
   "DocOrdBasedPrice":number,
      /**  This is the Price Group ID used to price the quote line with.  */  
   "PriceGroupCode":string,
      /**  Indicates if the user selected a price list different from the default.  */  
   "OverridePriceList":boolean,
      /**  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  */  
   "PricingValue":number,
      /**  This is the unit price based on the expected quantity.  */  
   "ExpUnitPrice":number,
      /**  This is the unit price (in customer currency) based on the expected quantity.  */  
   "DocExpUnitPrice":number,
      /**   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  */  
   "ExpPricePerCode":string,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  */  
   "MiscQtyNum":number,
      /**  The Quote Line has been Engineered.  */  
   "Engineer":boolean,
      /**  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  */  
   "ReadyToQuote":boolean,
      /**  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  */  
   "KitAllowUpdate":boolean,
      /**  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  */  
   "KitShipComplete":boolean,
      /**  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  */  
   "KitBackFlush":boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   "KitPrintCompsPS":boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   "KitPrintCompsInv":boolean,
      /**  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  */  
   "KitPricing":string,
      /**  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  */  
   "KitParentLine":number,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  */  
   "KitQtyPer":number,
      /**  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  */  
   "DisplaySeq":number,
      /**  Project ID of linked project.  Must exist on the Project table. Can be blank.  */  
   "ProjectID":string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  To indicate whether or not the line is make direct  */  
   "MakeDirect":boolean,
      /**  Must exist on ProjPhase table if entered  */  
   "PhaseID":string,
      /**   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   "KitFlag":string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  */  
   "KitsLoaded":boolean,
      /**  Non-blank value prevents taxes from being calculated for this line item  */  
   "TaxExempt":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   "OwnershipStatus":string,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExpectedRevenue":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExpectedRevenue":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExpectedRevenue":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExpUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExpUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExpUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3OrdBasedPrice":number,
      /**  Extended Price for the quote line, rounded according to the Base currency Round rule  */  
   "ExtPriceDtl":number,
      /**  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  */  
   "DocExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPriceDtl":number,
      /**  Reserved for future use  */  
   "InDiscount":number,
      /**  Reserved for future use  */  
   "DocInDiscount":number,
      /**  Reserved for future use  */  
   "InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "DocInExpectedRevenue":number,
      /**  Reserved for future use  */  
   "InListPrice":number,
      /**  Reserved for future use  */  
   "DocInListPrice":number,
      /**  Reserved for future use  */  
   "InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "DocInOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "DocInExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt1InDiscount":number,
      /**  Reserved for future use  */  
   "Rpt2InDiscount":number,
      /**  Reserved for future use  */  
   "Rpt3InDiscount":number,
      /**  Reserved for future use  */  
   "Rpt1InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "Rpt2InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "Rpt3InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "Rpt1InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt2InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt3InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt1InListPrice":number,
      /**  Reserved for future use  */  
   "Rpt2InListPrice":number,
      /**  Reserved for future use  */  
   "Rpt3InListPrice":number,
      /**  Reserved for future use  */  
   "Rpt1InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "Rpt2InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "Rpt3InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "InExtPriceDtl":number,
      /**  Reserved for future use  */  
   "DocInExtPriceDtl":number,
      /**  Reserved for future use  */  
   "Rpt1InExtPriceDtl":number,
      /**  Reserved for future use  */  
   "Rpt2InExtPriceDtl":number,
      /**  Reserved for future use  */  
   "Rpt3InExtPriceDtl":number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   "WorstCsPct":number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   "BestCsPct":number,
      /**  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   "WorstCsRevenue":number,
      /**  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   "DocWorstCsRevenue":number,
   "Rpt1WorstCsRevenue":number,
   "Rpt2WorstCsRevenue":number,
   "Rpt3WorstCsRevenue":number,
      /**  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   "BestCsRevenue":number,
      /**  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   "DocBestCsRevenue":number,
   "Rpt1BestCsRevenue":number,
   "Rpt2BestCsRevenue":number,
   "Rpt3BestCsRevenue":number,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   "KitCompOrigSeq":number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   "KitCompOrigPart":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
   "DiscBreakListCode":string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
   "DiscListPrice":number,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
   "OverrideDiscPriceList":boolean,
      /**  Demand Contract Line  */  
   "DemandContractLine":number,
      /**  Demand Header sequence number to which this record is related.  */  
   "DemandHedSeq":number,
      /**  Demand Detail Sequence number to which this record is related.  */  
   "DemandDtlSeq":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ICPOLine":number,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   "ICPONum":number,
      /**  Indicates if this quote line is linked to an inter-company PO line.  */  
   "Linked":boolean,
      /**  Indicates if the price of the quote line can be changed.  */  
   "LockPrice":boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   "LockQty":boolean,
      /**  Indicates that the line item was closed before any shipments were made against it.  */  
   "VoidLine":boolean,
      /**  Indicate that the item or the product group has a warranty.  */  
   "Warranty":boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  Editor widget for Warranty comments.  */  
   "WarrantyComment":string,
      /**  EstimateGUID  */  
   "EstimateGUID":string,
      /**  EstimateUserID  */  
   "EstimateUserID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  NeedByDate  */  
   "NeedByDate":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol from QuoteHed  */  
   "CurrSymbol":string,
   "BaseExtPrice":number,
   "DocExtPrice":number,
   "BasePotential":number,
   "DocPotential":number,
   "BaseMiscAmt":number,
   "DocMiscAmt":number,
      /**  Indicates whether the part is/can be configured  */  
   "Configured":string,
      /**  Indicates whether to Refresh the QuoteQty table  */  
   "RefreshQty":boolean,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
      /**  If yes, then a new non-standard part was added with no description and validation needs to be run again  */  
   "CheckPartDescription":boolean,
      /**  Delimited list of Available Price Lists  */  
   "AvailPriceLists":string,
      /**  If yes, the line will be copied to the Order  */  
   "OrderWorthy":boolean,
   "LineStatus":string,
   "QuantityToOrder":number,
   "ShipByDate":string,
   "OrderUM":string,
   "OrderUnitPrice":number,
   "DocOrderUnitPrice":number,
      /**  PLM Flag  */  
   "CodePLM":boolean,
      /**  Flag indicating whether to enable CodePLM or not  */  
   "EnablePLM":boolean,
      /**  The description for Kit Flag. "P" = Parent, "C" = Component.  */  
   "KitFlagDescription":string,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   "KitDisable":boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   "KitChangeParms":boolean,
   "QtyBearing":boolean,
   "Rpt1BasePotential":number,
   "Rpt2BasePotential":number,
   "Rpt3BasePotential":number,
   "Rpt1BaseExtPrice":number,
   "Rpt2BaseExtPrice":number,
   "Rpt3BaseExtPrice":number,
   "Rpt1BaseMiscAmt":number,
   "Rpt2BaseMiscAmt":number,
   "Rpt3BaseMiscAmt":number,
   "Rpt1OrderUnitPrice":number,
   "Rpt2OrderUnitPrice":number,
   "Rpt3OrderUnitPrice":number,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Indicates if the discount fields should be disabled for the current quote line detail.  */  
   "DisableDiscounts":boolean,
      /**  Used to displayed UOM for expected quantity for detail line  */  
   "DspExpectedUM":string,
   "KitOrderQtyUOM":string,
      /**  Description  */  
   "AnalysisCdDescription":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  Description of the price list.  */  
   "PriceBreakListDescription":string,
      /**  Price Group description  */  
   "PriceGroupDescription":string,
      /**  Full description of Product Group.  */  
   "ProdCodeDescription":string,
      /**  A unique code that identifies the currency.  */  
   "QuoteNumCurrencyCode":string,
      /**  Description of the sales category.  */  
   "SalesCatIDDescription":string,
      /**  Full description for the Sales Tax category.  */  
   "TaxCatIDDescription":string,
      /**  Description of the territory.  */  
   "TerritoryIDTerritoryDesc":string,
      /**  Date that the quoter considered the quoting process for this quote complete.  */  
   "DateQuoted":string,
      /**  The date when this quote expires.  */  
   "ExpirationDate":string,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   "PONum":string,
      /**  Valid values are "win" "lose" "next" "next" is the default  */  
   "Conclusion":string,
      /**  Display unit price based on the expected quantity.  */  
   "DspExpUnitPrice":number,
      /**  Display Document unit price based on the expected quantity.  */  
   "DocDspExpUnitPrice":number,
      /**  Display unit price based on the expected quantity.  */  
   "Rpt1DspExpUnitPrice":number,
      /**  Display unit price based on the expected quantity.  */  
   "Rpt2DspExpUnitPrice":number,
      /**  Display unit price based on the expected quantity.  */  
   "Rpt3DspExpUnitPrice":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "DspDiscount":number,
      /**  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "DocDspDiscount":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt1DspDiscount":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt2DspDiscount":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt3DspDiscount":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QuoteDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   "QuoteNum":number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   "QuoteLine":number,
      /**  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  */  
   "Ordered":boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   "PartNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  */  
   "XPartNum":string,
      /**  Contains comments about the detail line item. These will be printed on the Quote form.  */  
   "QuoteComment":string,
      /**  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  */  
   "LeadTime":string,
      /**  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   "Template":boolean,
      /**  Engineering Drawing Number. An optional field.  */  
   "DrawNum":string,
      /**  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  */  
   "JobComment":string,
      /**  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  */  
   "MfgDetail":boolean,
      /**  Indicates the Tax Category for this record. Defaults from the Part Master.  */  
   "TaxCatID":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  */  
   "CustNum":number,
      /**  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   "Quoted":boolean,
      /**  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   "Expired":boolean,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   "WIStartDate":string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   "WIStartHour":number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueDate":string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   "WIDueHour":number,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  The quantity expected to be ordered. (In selling unit of measure)  */  
   "SellingExpectedQty":number,
      /**  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SellingExpectedUM":string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  */  
   "ConfidencePct":number,
      /**  The date this line was last updated  */  
   "LastUpdate":string,
      /**  The last User Is that updated this Quote  */  
   "LastDcdUserID":string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Discount":number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  */  
   "DocDiscount":number,
      /**  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   "ExpectedRevenue":number,
      /**  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   "DocExpectedRevenue":number,
      /**  The requested ship date for the sales order  */  
   "ReqShipDate":string,
      /**  The quantity to be used when a Sales order is created. (In selling unit of measure)  */  
   "OrderQty":number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingExpFactor":number,
      /**  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  */  
   "MultiRel":boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLine":string,
      /**  A Code which uniquely identifies a SalesCat record.  */  
   "SalesCatID":string,
      /**  Replicated from QuoteHed to easier sorting  */  
   "TerritoryID":string,
      /**   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   "CurrentStage":string,
      /**  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  */  
   "CreatedFrom":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
      /**  The date when the configuration was completed for the assembly.  */  
   "LastConfigDate":string,
      /**  The system time when the configuration was completed for the assembly.  */  
   "LastConfigTime":number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   "LastConfigUserID":string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   "ConfigUnitPrice":number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   "ConfigBaseUnitPrice":number,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  This is the Price List used to determine the starting base price.  */  
   "PriceListCode":string,
      /**  This is the Price List used to determine the break % or amount.  */  
   "BreakListCode":string,
      /**  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  */  
   "PricingQty":number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   "ListPrice":number,
      /**   Same as List price except that this field contains the list price in
QuoteHed).  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   "OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  */  
   "DocOrdBasedPrice":number,
      /**  This is the Price Group ID used to price the quote line with.  */  
   "PriceGroupCode":string,
      /**  Indicates if the user selected a price list different from the default.  */  
   "OverridePriceList":boolean,
      /**  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  */  
   "PricingValue":number,
      /**  This is the unit price based on the expected quantity.  */  
   "ExpUnitPrice":number,
      /**  This is the unit price (in customer currency) based on the expected quantity.  */  
   "DocExpUnitPrice":number,
      /**   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  */  
   "ExpPricePerCode":string,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  */  
   "MiscQtyNum":number,
      /**  The Quote Line has been Engineered.  */  
   "Engineer":boolean,
      /**  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  */  
   "ReadyToQuote":boolean,
      /**  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  */  
   "KitAllowUpdate":boolean,
      /**  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  */  
   "KitShipComplete":boolean,
      /**  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  */  
   "KitBackFlush":boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   "KitPrintCompsPS":boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   "KitPrintCompsInv":boolean,
      /**  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  */  
   "KitPricing":string,
      /**  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  */  
   "KitParentLine":number,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  */  
   "KitQtyPer":number,
      /**  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  */  
   "DisplaySeq":number,
      /**  Project ID of linked project.  Must exist on the Project table. Can be blank.  */  
   "ProjectID":string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  To indicate whether or not the line is make direct  */  
   "MakeDirect":boolean,
      /**  Must exist on ProjPhase table if entered  */  
   "PhaseID":string,
      /**   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   "KitFlag":string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  */  
   "KitsLoaded":boolean,
      /**  Non-blank value prevents taxes from being calculated for this line item  */  
   "TaxExempt":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   "OwnershipStatus":string,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExpectedRevenue":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExpectedRevenue":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExpectedRevenue":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExpUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExpUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExpUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2OrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3OrdBasedPrice":number,
      /**  Extended Price for the quote line, rounded according to the Base currency Round rule  */  
   "ExtPriceDtl":number,
      /**  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  */  
   "DocExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPriceDtl":number,
      /**  Reserved for future use  */  
   "InDiscount":number,
      /**  Reserved for future use  */  
   "DocInDiscount":number,
      /**  Reserved for future use  */  
   "InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "DocInExpectedRevenue":number,
      /**  Reserved for future use  */  
   "InListPrice":number,
      /**  Reserved for future use  */  
   "DocInListPrice":number,
      /**  Reserved for future use  */  
   "InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "DocInOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "DocInExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt1InDiscount":number,
      /**  Reserved for future use  */  
   "Rpt2InDiscount":number,
      /**  Reserved for future use  */  
   "Rpt3InDiscount":number,
      /**  Reserved for future use  */  
   "Rpt1InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "Rpt2InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "Rpt3InExpectedRevenue":number,
      /**  Reserved for future use  */  
   "Rpt1InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt2InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt3InExpUnitPrice":number,
      /**  Reserved for future use  */  
   "Rpt1InListPrice":number,
      /**  Reserved for future use  */  
   "Rpt2InListPrice":number,
      /**  Reserved for future use  */  
   "Rpt3InListPrice":number,
      /**  Reserved for future use  */  
   "Rpt1InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "Rpt2InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "Rpt3InOrdBasedPrice":number,
      /**  Reserved for future use  */  
   "InExtPriceDtl":number,
      /**  Reserved for future use  */  
   "DocInExtPriceDtl":number,
      /**  Reserved for future use  */  
   "Rpt1InExtPriceDtl":number,
      /**  Reserved for future use  */  
   "Rpt2InExtPriceDtl":number,
      /**  Reserved for future use  */  
   "Rpt3InExtPriceDtl":number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   "WorstCsPct":number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   "BestCsPct":number,
      /**  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   "WorstCsRevenue":number,
      /**  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   "DocWorstCsRevenue":number,
   "Rpt1WorstCsRevenue":number,
   "Rpt2WorstCsRevenue":number,
   "Rpt3WorstCsRevenue":number,
      /**  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   "BestCsRevenue":number,
      /**  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   "DocBestCsRevenue":number,
   "Rpt1BestCsRevenue":number,
   "Rpt2BestCsRevenue":number,
   "Rpt3BestCsRevenue":number,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   "KitCompOrigSeq":number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   "KitCompOrigPart":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
   "DiscBreakListCode":string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
   "DiscListPrice":number,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
   "OverrideDiscPriceList":boolean,
      /**  Demand Contract Line  */  
   "DemandContractLine":number,
      /**  Demand Header sequence number to which this record is related.  */  
   "DemandHedSeq":number,
      /**  Demand Detail Sequence number to which this record is related.  */  
   "DemandDtlSeq":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ICPOLine":number,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   "ICPONum":number,
      /**  Indicates if this quote line is linked to an inter-company PO line.  */  
   "Linked":boolean,
      /**  Indicates if the price of the quote line can be changed.  */  
   "LockPrice":boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   "LockQty":boolean,
      /**  Indicates that the line item was closed before any shipments were made against it.  */  
   "VoidLine":boolean,
      /**  Indicate that the item or the product group has a warranty.  */  
   "Warranty":boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  Editor widget for Warranty comments.  */  
   "WarrantyComment":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  EstimateGUID  */  
   "EstimateGUID":string,
      /**  RFQCurrBaseEst  */  
   "RFQCurrBaseEst":string,
      /**  RFQTemplate  */  
   "RFQTemplate":string,
      /**  CreateEstimate  */  
   "CreateEstimate":boolean,
      /**  Rating  */  
   "Rating":string,
      /**  EstimateUserID  */  
   "EstimateUserID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  NeedByDate  */  
   "NeedByDate":string,
      /**  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  */  
   "ProcessMode":string,
      /**  ECC Quote Number  */  
   "ECCQuoteNum":string,
      /**  ECC Quote Line  */  
   "ECCQuoteLine":number,
      /**  ECC Comment Ref  */  
   "ECCCmmtRef":string,
      /**  ECCComment  */  
   "ECCComment":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**  Total tax in base currency. Tax detail for the line.  */  
   "Tax":number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   "DocTax":number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   "Rpt1Tax":number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   "Rpt2Tax":number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   "Rpt3Tax":number,
      /**  If true, the QuoteDtlTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  Indicates if no tax recalculation by the system is supposed to be done.  */  
   "NoTaxRecalc":boolean,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   "TotalSATax":number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   "DocTotalSATax":number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   "Rpt1TotalSATax":number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   "Rpt2TotalSATax":number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   "Rpt3TotalSATax":number,
      /**  EntityUseCode  */  
   "EntityUseCode":string,
      /**  This field holds the id of this quote line in the External CRM  */  
   "ExternalCRMQuoteLineID":string,
      /**  Type for returns: Blank, (C)redit or (S)tandard  */  
   "ReturnLineType":string,
      /**  Base price before any price breaks and discounts  */  
   "MSRP":number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   "DocMSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   "Rpt1MSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   "Rpt2MSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   "Rpt3MSRP":number,
      /**  Distributor end customer price.  */  
   "EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   "DocEndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   "Rpt1EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   "Rpt2EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   "Rpt3EndCustomerPrice":number,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   "MFCustNum":number,
      /**  Mark For ShipToNum  */  
   "MFShipToNum":string,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   "UseOTMF":boolean,
      /**  One Time Mark For Contact Name  */  
   "OTMFName":string,
      /**  One Time Mark For first line of the ShipTo address.  */  
   "OTMFAddress1":string,
      /**  One Time Mark For second line of the ShipTo address.  */  
   "OTMFAddress2":string,
      /**  One Time Mark For third line of the ShipTo address.  */  
   "OTMFAddress3":string,
      /**  City portion of the One Time Mark For address.  */  
   "OTMFCity":string,
      /**  The state or province portion of the One Time Mark For address.  */  
   "OTMFState":string,
      /**  The zip or postal code portion of the One Time Mark For address.  */  
   "OTMFZIP":string,
      /**  One Time Mark For Contact Name  */  
   "OTMFContact":string,
      /**  Fax number for the One Time Mark For.  */  
   "OTMFFaxNum":string,
      /**  Phone number for the One Time Mark For  */  
   "OTMFPhoneNum":string,
      /**  Country number for the One Time Mark For  */  
   "OTMFCountryNum":number,
      /**  Promotional Price offered to Dealer and Distributors  */  
   "PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   "DocPromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   "Rpt1PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   "Rpt2PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   "Rpt3PromotionalPrice":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  */  
   "AttributeSetID":number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   "KBConfigProdID":number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   "KBOriginalConfigProdID":number,
      /**  Currency.CurrSymbol for BASE  */  
   "BaseCurrSymbol":string,
   "BaseExtPrice":number,
   "BaseMiscAmt":number,
   "BasePotential":number,
      /**  If yes, then a new non-standard part was added with no description and validation needs to be run again  */  
   "CheckPartDescription":boolean,
      /**  PLM Flag  */  
   "CodePLM":boolean,
      /**  Valid values are "win" "lose" "next" "next" is the default  */  
   "Conclusion":string,
   "ConfigType":string,
      /**  Indicates whether the part is/can be configured  */  
   "Configured":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol from QuoteHed  */  
   "CurrSymbol":string,
      /**  Date that the quoter considered the quoting process for this quote complete.  */  
   "DateQuoted":string,
      /**  Indicates if the discount fields should be disabled for the current quote line detail.  */  
   "DisableDiscounts":boolean,
      /**  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "DocDspDiscount":number,
      /**  Display Document unit price based on the expected quantity.  */  
   "DocDspExpUnitPrice":number,
   "DocExtPrice":number,
   "DocMiscAmt":number,
   "DocOrderUnitPrice":number,
   "DocPotential":number,
   "DocTotalPrice":number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   "DocTotalQuote":number,
      /**  Total Withholding Tax amount for the Quote Line  */  
   "DocTotalWHTax":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "DspDiscount":number,
      /**  Used to displayed UOM for expected quantity for detail line  */  
   "DspExpectedUM":string,
   "EnableRenewalNbr":boolean,
      /**  The date when this quote expires.  */  
   "ExpirationDate":string,
      /**  Indicates whether the part has at least one Complement  */  
   "HasComplement":boolean,
   "HasCoParts":boolean,
      /**  Indicates if this Quote line has an associated credit memo (only for dealer portal)  */  
   "HasCreditMemo":boolean,
      /**  Indicates whether the part has at least one Downgrade  */  
   "HasDowngrade":boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   "HasSubstitute":boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   "HasUpgrade":boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   "KitChangeParms":boolean,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   "KitDisable":boolean,
      /**  The description for Kit Flag. "P" = Parent, "C" = Component.  */  
   "KitFlagDescription":string,
   "KitOrderQtyUOM":string,
   "LineStatus":string,
      /**  Contains the Mark For Address  */  
   "MarkForAddrList":string,
   "MFCustID":string,
   "OrderUM":string,
   "OrderUnitPrice":number,
      /**  If yes, the line will be copied to the Order  */  
   "OrderWorthy":boolean,
      /**  Internal flag to identify if the Part is an Inventory Part.  */  
   "PartExists":boolean,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   "PONum":string,
   "QtyBearing":boolean,
   "QuantityToOrder":number,
      /**  Indicates whether to Refresh the QuoteQty table  */  
   "RefreshQty":boolean,
      /**  The flag to indicate if the logic should delete quote line related manually added and manual taxes if the user populates Tax Exempt field previously blank  */  
   "RemoveManAdTax":boolean,
   "Rpt1BaseExtPrice":number,
   "Rpt1BaseMiscAmt":number,
   "Rpt1BasePotential":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt1DspDiscount":number,
      /**  Display unit price based on the expected quantity.  */  
   "Rpt1DspExpUnitPrice":number,
   "Rpt1OrderUnitPrice":number,
   "Rpt1TotalPrice":number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   "Rpt1TotalQuote":number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   "Rpt1TotalWHTax":number,
   "Rpt2BaseExtPrice":number,
   "Rpt2BaseMiscAmt":number,
   "Rpt2BasePotential":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt2DspDiscount":number,
      /**  Display unit price based on the expected quantity.  */  
   "Rpt2DspExpUnitPrice":number,
   "Rpt2OrderUnitPrice":number,
   "Rpt2TotalPrice":number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   "Rpt2TotalQuote":number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   "Rpt2TotalWHTax":number,
   "Rpt3BaseExtPrice":number,
   "Rpt3BaseMiscAmt":number,
   "Rpt3BasePotential":number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt3DspDiscount":number,
      /**  Display unit price based on the expected quantity.  */  
   "Rpt3DspExpUnitPrice":number,
   "Rpt3OrderUnitPrice":number,
   "Rpt3TotalPrice":number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   "Rpt3TotalQuote":number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   "Rpt3TotalWHTax":number,
      /**  Selected row  */  
   "Selected":boolean,
   "ShipByDate":string,
   "TotalPrice":number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   "TotalQuote":number,
      /**  Total Withholding Tax amount for the Quote Line  */  
   "TotalWHTax":number,
      /**   Indicates that a QuoteAsm.QtyPer field was updated with out updating the RequiredQty field on the sub tables.
*** FUTURE USE  */  
   "UpdateReq":boolean,
      /**  Indicates that the Quote should be used as the BOM when creating a job for the linked order  */  
   "UseQuoteBOM":boolean,
      /**  Delimited list of Available Price Lists  */  
   "AvailPriceLists":string,
      /**  Display unit price based on the expected quantity.  */  
   "DspExpUnitPrice":number,
   "ECCLineCRQ":number,
      /**  Allow enable/disable for the Dynamic Attributes button on a Quote Line  */  
   "EnableDynAttrButton":boolean,
      /**  Flag indicating whether to enable CodePLM or not  */  
   "EnablePLM":boolean,
   "MarkForAddressFormatted":string,
   "InventoryAttributeSetID":number,
      /**  The amount of discount for display  */  
   "LessDiscount":number,
      /**  The amount of discount for display in Doc currency  */  
   "DocLessDiscount":number,
      /**  The amount of discount for display in reporting currency  */  
   "Rpt1LessDiscount":number,
      /**  The amount of discount for display in reporting currency  */  
   "Rpt2LessDiscount":number,
      /**  The amount of discount for display in reporting currency  */  
   "Rpt3LessDiscount":number,
      /**   This flag indicates if taxes can be modified by user:
True: Taxes are from Tax Engine (Vantage). They can be adjusted/deleted.
False: Taxes are from TaxConnect. They cannot be adjusted/deleted.
AllowTaxCodeUpd depends on TaxConnectCalc value. If TaxConnectCalc is True, AllowTaxCodeUpd will be False. Otherwise, it will be True.  */  
   "AllowTaxCodeUpd":boolean,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "CustomerBTName":string,
   "CustomerName":string,
   "CustomerCustID":string,
   "DiscBreakListCodeListDescription":string,
   "DiscBreakListCodeEndDate":string,
   "DiscBreakListCodeStartDate":string,
   "MFShipToNumInactive":boolean,
   "OTMFCountryDescription":string,
   "PartNumDefaultAttributeSetID":number,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PriceBreakListDescription":string,
   "PriceGroupDescription":string,
   "ProdCodeDescription":string,
   "QuoteNumInPrice":boolean,
   "QuoteNumCurrencyCode":string,
   "SalesCatIDDescription":string,
   "TaxCatIDDescription":string,
   "TaxRegionDescription":string,
   "TaxRegionTaxConnectCalc":boolean,
   "TerritoryIDTerritoryDesc":string,
   "WarrantyCodeWarrDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param quoteNum
      @param quoteLine
   */  
export interface DeleteByID_input{
   quoteNum:number,
   quoteLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_QuoteDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  */  
   Ordered:boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  */  
   XPartNum:string,
      /**  Contains comments about the detail line item. These will be printed on the Quote form.  */  
   QuoteComment:string,
      /**  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  */  
   LeadTime:string,
      /**  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   Template:boolean,
      /**  Engineering Drawing Number. An optional field.  */  
   DrawNum:string,
      /**  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  */  
   JobComment:string,
      /**  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  */  
   MfgDetail:boolean,
      /**  Indicates the Tax Category for this record. Defaults from the Part Master.  */  
   TaxCatID:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  */  
   CustNum:number,
      /**  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   Quoted:boolean,
      /**  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   Expired:boolean,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIStartHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueHour:number,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  The quantity expected to be ordered. (In selling unit of measure)  */  
   SellingExpectedQty:number,
      /**  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SellingExpectedUM:string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  */  
   ConfidencePct:number,
      /**  The date this line was last updated  */  
   LastUpdate:string,
      /**  The last User Is that updated this Quote  */  
   LastDcdUserID:string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Discount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  */  
   DocDiscount:number,
      /**  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   ExpectedRevenue:number,
      /**  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   DocExpectedRevenue:number,
      /**  The requested ship date for the sales order  */  
   ReqShipDate:string,
      /**  The quantity to be used when a Sales order is created. (In selling unit of measure)  */  
   OrderQty:number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingExpFactor:number,
      /**  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  */  
   MultiRel:boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  A Code which uniquely identifies a SalesCat record.  */  
   SalesCatID:string,
      /**  Replicated from QuoteHed to easier sorting  */  
   TerritoryID:string,
      /**   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   CurrentStage:string,
      /**  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  */  
   CreatedFrom:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitPrice:number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitPrice:number,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  This is the Price List used to determine the starting base price.  */  
   PriceListCode:string,
      /**  This is the Price List used to determine the break % or amount.  */  
   BreakListCode:string,
      /**  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  */  
   PricingQty:number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   ListPrice:number,
      /**   Same as List price except that this field contains the list price in
QuoteHed).  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  */  
   DocOrdBasedPrice:number,
      /**  This is the Price Group ID used to price the quote line with.  */  
   PriceGroupCode:string,
      /**  Indicates if the user selected a price list different from the default.  */  
   OverridePriceList:boolean,
      /**  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  */  
   PricingValue:number,
      /**  This is the unit price based on the expected quantity.  */  
   ExpUnitPrice:number,
      /**  This is the unit price (in customer currency) based on the expected quantity.  */  
   DocExpUnitPrice:number,
      /**   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  */  
   ExpPricePerCode:string,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  */  
   MiscQtyNum:number,
      /**  The Quote Line has been Engineered.  */  
   Engineer:boolean,
      /**  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  */  
   ReadyToQuote:boolean,
      /**  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  */  
   KitAllowUpdate:boolean,
      /**  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  */  
   KitShipComplete:boolean,
      /**  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  */  
   KitBackFlush:boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   KitPrintCompsPS:boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   KitPrintCompsInv:boolean,
      /**  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  */  
   KitPricing:string,
      /**  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  */  
   KitParentLine:number,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  */  
   KitQtyPer:number,
      /**  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  */  
   DisplaySeq:number,
      /**  Project ID of linked project.  Must exist on the Project table. Can be blank.  */  
   ProjectID:string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  To indicate whether or not the line is make direct  */  
   MakeDirect:boolean,
      /**  Must exist on ProjPhase table if entered  */  
   PhaseID:string,
      /**   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   KitFlag:string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  */  
   KitsLoaded:boolean,
      /**  Non-blank value prevents taxes from being calculated for this line item  */  
   TaxExempt:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3OrdBasedPrice:number,
      /**  Extended Price for the quote line, rounded according to the Base currency Round rule  */  
   ExtPriceDtl:number,
      /**  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPriceDtl:number,
      /**  Reserved for future use  */  
   InDiscount:number,
      /**  Reserved for future use  */  
   DocInDiscount:number,
      /**  Reserved for future use  */  
   InExpectedRevenue:number,
      /**  Reserved for future use  */  
   DocInExpectedRevenue:number,
      /**  Reserved for future use  */  
   InListPrice:number,
      /**  Reserved for future use  */  
   DocInListPrice:number,
      /**  Reserved for future use  */  
   InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   DocInOrdBasedPrice:number,
      /**  Reserved for future use  */  
   InExpUnitPrice:number,
      /**  Reserved for future use  */  
   DocInExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt1InDiscount:number,
      /**  Reserved for future use  */  
   Rpt2InDiscount:number,
      /**  Reserved for future use  */  
   Rpt3InDiscount:number,
      /**  Reserved for future use  */  
   Rpt1InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt2InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt3InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt1InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt2InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt3InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt1InListPrice:number,
      /**  Reserved for future use  */  
   Rpt2InListPrice:number,
      /**  Reserved for future use  */  
   Rpt3InListPrice:number,
      /**  Reserved for future use  */  
   Rpt1InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   Rpt2InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   Rpt3InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   InExtPriceDtl:number,
      /**  Reserved for future use  */  
   DocInExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt1InExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt2InExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt3InExtPriceDtl:number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   WorstCsPct:number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   BestCsPct:number,
      /**  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   WorstCsRevenue:number,
      /**  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   DocWorstCsRevenue:number,
   Rpt1WorstCsRevenue:number,
   Rpt2WorstCsRevenue:number,
   Rpt3WorstCsRevenue:number,
      /**  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   BestCsRevenue:number,
      /**  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   DocBestCsRevenue:number,
   Rpt1BestCsRevenue:number,
   Rpt2BestCsRevenue:number,
   Rpt3BestCsRevenue:number,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   KitCompOrigSeq:number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   KitCompOrigPart:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
   DiscBreakListCode:string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
   DiscListPrice:number,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
   OverrideDiscPriceList:boolean,
      /**  Demand Contract Line  */  
   DemandContractLine:number,
      /**  Demand Header sequence number to which this record is related.  */  
   DemandHedSeq:number,
      /**  Demand Detail Sequence number to which this record is related.  */  
   DemandDtlSeq:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  Indicates if this quote line is linked to an inter-company PO line.  */  
   Linked:boolean,
      /**  Indicates if the price of the quote line can be changed.  */  
   LockPrice:boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Indicates that the line item was closed before any shipments were made against it.  */  
   VoidLine:boolean,
      /**  Indicate that the item or the product group has a warranty.  */  
   Warranty:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  EstimateGUID  */  
   EstimateGUID:string,
      /**  EstimateUserID  */  
   EstimateUserID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  NeedByDate  */  
   NeedByDate:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol from QuoteHed  */  
   CurrSymbol:string,
   BaseExtPrice:number,
   DocExtPrice:number,
   BasePotential:number,
   DocPotential:number,
   BaseMiscAmt:number,
   DocMiscAmt:number,
      /**  Indicates whether the part is/can be configured  */  
   Configured:string,
      /**  Indicates whether to Refresh the QuoteQty table  */  
   RefreshQty:boolean,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  If yes, then a new non-standard part was added with no description and validation needs to be run again  */  
   CheckPartDescription:boolean,
      /**  Delimited list of Available Price Lists  */  
   AvailPriceLists:string,
      /**  If yes, the line will be copied to the Order  */  
   OrderWorthy:boolean,
   LineStatus:string,
   QuantityToOrder:number,
   ShipByDate:string,
   OrderUM:string,
   OrderUnitPrice:number,
   DocOrderUnitPrice:number,
      /**  PLM Flag  */  
   CodePLM:boolean,
      /**  Flag indicating whether to enable CodePLM or not  */  
   EnablePLM:boolean,
      /**  The description for Kit Flag. "P" = Parent, "C" = Component.  */  
   KitFlagDescription:string,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   KitDisable:boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   KitChangeParms:boolean,
   QtyBearing:boolean,
   Rpt1BasePotential:number,
   Rpt2BasePotential:number,
   Rpt3BasePotential:number,
   Rpt1BaseExtPrice:number,
   Rpt2BaseExtPrice:number,
   Rpt3BaseExtPrice:number,
   Rpt1BaseMiscAmt:number,
   Rpt2BaseMiscAmt:number,
   Rpt3BaseMiscAmt:number,
   Rpt1OrderUnitPrice:number,
   Rpt2OrderUnitPrice:number,
   Rpt3OrderUnitPrice:number,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Indicates if the discount fields should be disabled for the current quote line detail.  */  
   DisableDiscounts:boolean,
      /**  Used to displayed UOM for expected quantity for detail line  */  
   DspExpectedUM:string,
   KitOrderQtyUOM:string,
      /**  Description  */  
   AnalysisCdDescription:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  Description of the price list.  */  
   PriceBreakListDescription:string,
      /**  Price Group description  */  
   PriceGroupDescription:string,
      /**  Full description of Product Group.  */  
   ProdCodeDescription:string,
      /**  A unique code that identifies the currency.  */  
   QuoteNumCurrencyCode:string,
      /**  Description of the sales category.  */  
   SalesCatIDDescription:string,
      /**  Full description for the Sales Tax category.  */  
   TaxCatIDDescription:string,
      /**  Description of the territory.  */  
   TerritoryIDTerritoryDesc:string,
      /**  Date that the quoter considered the quoting process for this quote complete.  */  
   DateQuoted:string,
      /**  The date when this quote expires.  */  
   ExpirationDate:string,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   PONum:string,
      /**  Valid values are "win" "lose" "next" "next" is the default  */  
   Conclusion:string,
      /**  Display unit price based on the expected quantity.  */  
   DspExpUnitPrice:number,
      /**  Display Document unit price based on the expected quantity.  */  
   DocDspExpUnitPrice:number,
      /**  Display unit price based on the expected quantity.  */  
   Rpt1DspExpUnitPrice:number,
      /**  Display unit price based on the expected quantity.  */  
   Rpt2DspExpUnitPrice:number,
      /**  Display unit price based on the expected quantity.  */  
   Rpt3DspExpUnitPrice:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DspDiscount:number,
      /**  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DocDspDiscount:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1DspDiscount:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2DspDiscount:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3DspDiscount:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteDtlListTableset{
   QuoteDtlList:Erp_Tablesets_QuoteDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QuoteDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  */  
   Ordered:boolean,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  */  
   XPartNum:string,
      /**  Contains comments about the detail line item. These will be printed on the Quote form.  */  
   QuoteComment:string,
      /**  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  */  
   LeadTime:string,
      /**  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  */  
   Template:boolean,
      /**  Engineering Drawing Number. An optional field.  */  
   DrawNum:string,
      /**  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  */  
   JobComment:string,
      /**  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  */  
   MfgDetail:boolean,
      /**  Indicates the Tax Category for this record. Defaults from the Part Master.  */  
   TaxCatID:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  */  
   CustNum:number,
      /**  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   Quoted:boolean,
      /**  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  */  
   Expired:boolean,
      /**  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  */  
   WIStartDate:string,
      /**  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  */  
   WIStartHour:number,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueDate:string,
      /**  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  */  
   WIDueHour:number,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  The quantity expected to be ordered. (In selling unit of measure)  */  
   SellingExpectedQty:number,
      /**  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SellingExpectedUM:string,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  */  
   ConfidencePct:number,
      /**  The date this line was last updated  */  
   LastUpdate:string,
      /**  The last User Is that updated this Quote  */  
   LastDcdUserID:string,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Discount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  */  
   DocDiscount:number,
      /**  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   ExpectedRevenue:number,
      /**  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   DocExpectedRevenue:number,
      /**  The requested ship date for the sales order  */  
   ReqShipDate:string,
      /**  The quantity to be used when a Sales order is created. (In selling unit of measure)  */  
   OrderQty:number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingExpFactor:number,
      /**  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  */  
   MultiRel:boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  A Code which uniquely identifies a SalesCat record.  */  
   SalesCatID:string,
      /**  Replicated from QuoteHed to easier sorting  */  
   TerritoryID:string,
      /**   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  */  
   CurrentStage:string,
      /**  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  */  
   CreatedFrom:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitPrice:number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitPrice:number,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  This is the Price List used to determine the starting base price.  */  
   PriceListCode:string,
      /**  This is the Price List used to determine the break % or amount.  */  
   BreakListCode:string,
      /**  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  */  
   PricingQty:number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   ListPrice:number,
      /**   Same as List price except that this field contains the list price in
QuoteHed).  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  */  
   DocOrdBasedPrice:number,
      /**  This is the Price Group ID used to price the quote line with.  */  
   PriceGroupCode:string,
      /**  Indicates if the user selected a price list different from the default.  */  
   OverridePriceList:boolean,
      /**  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  */  
   PricingValue:number,
      /**  This is the unit price based on the expected quantity.  */  
   ExpUnitPrice:number,
      /**  This is the unit price (in customer currency) based on the expected quantity.  */  
   DocExpUnitPrice:number,
      /**   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  */  
   ExpPricePerCode:string,
      /**  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  */  
   MiscQtyNum:number,
      /**  The Quote Line has been Engineered.  */  
   Engineer:boolean,
      /**  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  */  
   ReadyToQuote:boolean,
      /**  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  */  
   KitAllowUpdate:boolean,
      /**  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  */  
   KitShipComplete:boolean,
      /**  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  */  
   KitBackFlush:boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   KitPrintCompsPS:boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  */  
   KitPrintCompsInv:boolean,
      /**  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  */  
   KitPricing:string,
      /**  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  */  
   KitParentLine:number,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  */  
   KitQtyPer:number,
      /**  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  */  
   DisplaySeq:number,
      /**  Project ID of linked project.  Must exist on the Project table. Can be blank.  */  
   ProjectID:string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  To indicate whether or not the line is make direct  */  
   MakeDirect:boolean,
      /**  Must exist on ProjPhase table if entered  */  
   PhaseID:string,
      /**   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   KitFlag:string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  */  
   KitsLoaded:boolean,
      /**  Non-blank value prevents taxes from being calculated for this line item  */  
   TaxExempt:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExpectedRevenue:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExpUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2OrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3OrdBasedPrice:number,
      /**  Extended Price for the quote line, rounded according to the Base currency Round rule  */  
   ExtPriceDtl:number,
      /**  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPriceDtl:number,
      /**  Reserved for future use  */  
   InDiscount:number,
      /**  Reserved for future use  */  
   DocInDiscount:number,
      /**  Reserved for future use  */  
   InExpectedRevenue:number,
      /**  Reserved for future use  */  
   DocInExpectedRevenue:number,
      /**  Reserved for future use  */  
   InListPrice:number,
      /**  Reserved for future use  */  
   DocInListPrice:number,
      /**  Reserved for future use  */  
   InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   DocInOrdBasedPrice:number,
      /**  Reserved for future use  */  
   InExpUnitPrice:number,
      /**  Reserved for future use  */  
   DocInExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt1InDiscount:number,
      /**  Reserved for future use  */  
   Rpt2InDiscount:number,
      /**  Reserved for future use  */  
   Rpt3InDiscount:number,
      /**  Reserved for future use  */  
   Rpt1InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt2InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt3InExpectedRevenue:number,
      /**  Reserved for future use  */  
   Rpt1InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt2InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt3InExpUnitPrice:number,
      /**  Reserved for future use  */  
   Rpt1InListPrice:number,
      /**  Reserved for future use  */  
   Rpt2InListPrice:number,
      /**  Reserved for future use  */  
   Rpt3InListPrice:number,
      /**  Reserved for future use  */  
   Rpt1InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   Rpt2InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   Rpt3InOrdBasedPrice:number,
      /**  Reserved for future use  */  
   InExtPriceDtl:number,
      /**  Reserved for future use  */  
   DocInExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt1InExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt2InExtPriceDtl:number,
      /**  Reserved for future use  */  
   Rpt3InExtPriceDtl:number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  */  
   WorstCsPct:number,
      /**  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  */  
   BestCsPct:number,
      /**  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   WorstCsRevenue:number,
      /**  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   DocWorstCsRevenue:number,
   Rpt1WorstCsRevenue:number,
   Rpt2WorstCsRevenue:number,
   Rpt3WorstCsRevenue:number,
      /**  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   BestCsRevenue:number,
      /**  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   DocBestCsRevenue:number,
   Rpt1BestCsRevenue:number,
   Rpt2BestCsRevenue:number,
   Rpt3BestCsRevenue:number,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   KitCompOrigSeq:number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   KitCompOrigPart:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
   DiscBreakListCode:string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
   DiscListPrice:number,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
   OverrideDiscPriceList:boolean,
      /**  Demand Contract Line  */  
   DemandContractLine:number,
      /**  Demand Header sequence number to which this record is related.  */  
   DemandHedSeq:number,
      /**  Demand Detail Sequence number to which this record is related.  */  
   DemandDtlSeq:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  Indicates if this quote line is linked to an inter-company PO line.  */  
   Linked:boolean,
      /**  Indicates if the price of the quote line can be changed.  */  
   LockPrice:boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Indicates that the line item was closed before any shipments were made against it.  */  
   VoidLine:boolean,
      /**  Indicate that the item or the product group has a warranty.  */  
   Warranty:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  EstimateGUID  */  
   EstimateGUID:string,
      /**  RFQCurrBaseEst  */  
   RFQCurrBaseEst:string,
      /**  RFQTemplate  */  
   RFQTemplate:string,
      /**  CreateEstimate  */  
   CreateEstimate:boolean,
      /**  Rating  */  
   Rating:string,
      /**  EstimateUserID  */  
   EstimateUserID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  NeedByDate  */  
   NeedByDate:string,
      /**  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  */  
   ProcessMode:string,
      /**  ECC Quote Number  */  
   ECCQuoteNum:string,
      /**  ECC Quote Line  */  
   ECCQuoteLine:number,
      /**  ECC Comment Ref  */  
   ECCCmmtRef:string,
      /**  ECCComment  */  
   ECCComment:string,
      /**  ContractID  */  
   ContractID:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Tax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   DocTax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Rpt1Tax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Rpt2Tax:number,
      /**  Total tax in base currency. Tax detail for the line.  */  
   Rpt3Tax:number,
      /**  If true, the QuoteDtlTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  Indicates if no tax recalculation by the system is supposed to be done.  */  
   NoTaxRecalc:boolean,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   TotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   DocTotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   Rpt1TotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   Rpt2TotalSATax:number,
      /**  Total Quote Self Assessed Taxes for the Quote Line  */  
   Rpt3TotalSATax:number,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  This field holds the id of this quote line in the External CRM  */  
   ExternalCRMQuoteLineID:string,
      /**  Type for returns: Blank, (C)redit or (S)tandard  */  
   ReturnLineType:string,
      /**  Base price before any price breaks and discounts  */  
   MSRP:number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   DocMSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   Rpt1MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   Rpt2MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency converted..  */  
   Rpt3MSRP:number,
      /**  Distributor end customer price.  */  
   EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   DocEndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   Rpt1EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   Rpt2EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency converted.  */  
   Rpt3EndCustomerPrice:number,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  Mark For ShipToNum  */  
   MFShipToNum:string,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   UseOTMF:boolean,
      /**  One Time Mark For Contact Name  */  
   OTMFName:string,
      /**  One Time Mark For first line of the ShipTo address.  */  
   OTMFAddress1:string,
      /**  One Time Mark For second line of the ShipTo address.  */  
   OTMFAddress2:string,
      /**  One Time Mark For third line of the ShipTo address.  */  
   OTMFAddress3:string,
      /**  City portion of the One Time Mark For address.  */  
   OTMFCity:string,
      /**  The state or province portion of the One Time Mark For address.  */  
   OTMFState:string,
      /**  The zip or postal code portion of the One Time Mark For address.  */  
   OTMFZIP:string,
      /**  One Time Mark For Contact Name  */  
   OTMFContact:string,
      /**  Fax number for the One Time Mark For.  */  
   OTMFFaxNum:string,
      /**  Phone number for the One Time Mark For  */  
   OTMFPhoneNum:string,
      /**  Country number for the One Time Mark For  */  
   OTMFCountryNum:number,
      /**  Promotional Price offered to Dealer and Distributors  */  
   PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  */  
   DocPromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   Rpt1PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   Rpt2PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  */  
   Rpt3PromotionalPrice:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  */  
   AttributeSetID:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   KBOriginalConfigProdID:number,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
   BaseExtPrice:number,
   BaseMiscAmt:number,
   BasePotential:number,
      /**  If yes, then a new non-standard part was added with no description and validation needs to be run again  */  
   CheckPartDescription:boolean,
      /**  PLM Flag  */  
   CodePLM:boolean,
      /**  Valid values are "win" "lose" "next" "next" is the default  */  
   Conclusion:string,
   ConfigType:string,
      /**  Indicates whether the part is/can be configured  */  
   Configured:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol from QuoteHed  */  
   CurrSymbol:string,
      /**  Date that the quoter considered the quoting process for this quote complete.  */  
   DateQuoted:string,
      /**  Indicates if the discount fields should be disabled for the current quote line detail.  */  
   DisableDiscounts:boolean,
      /**  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DocDspDiscount:number,
      /**  Display Document unit price based on the expected quantity.  */  
   DocDspExpUnitPrice:number,
   DocExtPrice:number,
   DocMiscAmt:number,
   DocOrderUnitPrice:number,
   DocPotential:number,
   DocTotalPrice:number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   DocTotalQuote:number,
      /**  Total Withholding Tax amount for the Quote Line  */  
   DocTotalWHTax:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DspDiscount:number,
      /**  Used to displayed UOM for expected quantity for detail line  */  
   DspExpectedUM:string,
   EnableRenewalNbr:boolean,
      /**  The date when this quote expires.  */  
   ExpirationDate:string,
      /**  Indicates whether the part has at least one Complement  */  
   HasComplement:boolean,
   HasCoParts:boolean,
      /**  Indicates if this Quote line has an associated credit memo (only for dealer portal)  */  
   HasCreditMemo:boolean,
      /**  Indicates whether the part has at least one Downgrade  */  
   HasDowngrade:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasSubstitute:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasUpgrade:boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   KitChangeParms:boolean,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   KitDisable:boolean,
      /**  The description for Kit Flag. "P" = Parent, "C" = Component.  */  
   KitFlagDescription:string,
   KitOrderQtyUOM:string,
   LineStatus:string,
      /**  Contains the Mark For Address  */  
   MarkForAddrList:string,
   MFCustID:string,
   OrderUM:string,
   OrderUnitPrice:number,
      /**  If yes, the line will be copied to the Order  */  
   OrderWorthy:boolean,
      /**  Internal flag to identify if the Part is an Inventory Part.  */  
   PartExists:boolean,
      /**  This is an optional field used to enter the customers Purchase Order Number.  */  
   PONum:string,
   QtyBearing:boolean,
   QuantityToOrder:number,
      /**  Indicates whether to Refresh the QuoteQty table  */  
   RefreshQty:boolean,
      /**  The flag to indicate if the logic should delete quote line related manually added and manual taxes if the user populates Tax Exempt field previously blank  */  
   RemoveManAdTax:boolean,
   Rpt1BaseExtPrice:number,
   Rpt1BaseMiscAmt:number,
   Rpt1BasePotential:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1DspDiscount:number,
      /**  Display unit price based on the expected quantity.  */  
   Rpt1DspExpUnitPrice:number,
   Rpt1OrderUnitPrice:number,
   Rpt1TotalPrice:number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   Rpt1TotalQuote:number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   Rpt1TotalWHTax:number,
   Rpt2BaseExtPrice:number,
   Rpt2BaseMiscAmt:number,
   Rpt2BasePotential:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2DspDiscount:number,
      /**  Display unit price based on the expected quantity.  */  
   Rpt2DspExpUnitPrice:number,
   Rpt2OrderUnitPrice:number,
   Rpt2TotalPrice:number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   Rpt2TotalQuote:number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   Rpt2TotalWHTax:number,
   Rpt3BaseExtPrice:number,
   Rpt3BaseMiscAmt:number,
   Rpt3BasePotential:number,
      /**  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3DspDiscount:number,
      /**  Display unit price based on the expected quantity.  */  
   Rpt3DspExpUnitPrice:number,
   Rpt3OrderUnitPrice:number,
   Rpt3TotalPrice:number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   Rpt3TotalQuote:number,
      /**  Total Withholding Tax Amount for the Quote Line  */  
   Rpt3TotalWHTax:number,
      /**  Selected row  */  
   Selected:boolean,
   ShipByDate:string,
   TotalPrice:number,
      /**   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  */  
   TotalQuote:number,
      /**  Total Withholding Tax amount for the Quote Line  */  
   TotalWHTax:number,
      /**   Indicates that a QuoteAsm.QtyPer field was updated with out updating the RequiredQty field on the sub tables.
*** FUTURE USE  */  
   UpdateReq:boolean,
      /**  Indicates that the Quote should be used as the BOM when creating a job for the linked order  */  
   UseQuoteBOM:boolean,
      /**  Delimited list of Available Price Lists  */  
   AvailPriceLists:string,
      /**  Display unit price based on the expected quantity.  */  
   DspExpUnitPrice:number,
   ECCLineCRQ:number,
      /**  Allow enable/disable for the Dynamic Attributes button on a Quote Line  */  
   EnableDynAttrButton:boolean,
      /**  Flag indicating whether to enable CodePLM or not  */  
   EnablePLM:boolean,
   MarkForAddressFormatted:string,
   InventoryAttributeSetID:number,
      /**  The amount of discount for display  */  
   LessDiscount:number,
      /**  The amount of discount for display in Doc currency  */  
   DocLessDiscount:number,
      /**  The amount of discount for display in reporting currency  */  
   Rpt1LessDiscount:number,
      /**  The amount of discount for display in reporting currency  */  
   Rpt2LessDiscount:number,
      /**  The amount of discount for display in reporting currency  */  
   Rpt3LessDiscount:number,
      /**   This flag indicates if taxes can be modified by user:
True: Taxes are from Tax Engine (Vantage). They can be adjusted/deleted.
False: Taxes are from TaxConnect. They cannot be adjusted/deleted.
AllowTaxCodeUpd depends on TaxConnectCalc value. If TaxConnectCalc is True, AllowTaxCodeUpd will be False. Otherwise, it will be True.  */  
   AllowTaxCodeUpd:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   CustomerBTName:string,
   CustomerName:string,
   CustomerCustID:string,
   DiscBreakListCodeListDescription:string,
   DiscBreakListCodeEndDate:string,
   DiscBreakListCodeStartDate:string,
   MFShipToNumInactive:boolean,
   OTMFCountryDescription:string,
   PartNumDefaultAttributeSetID:number,
   PartNumAttrClassID:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PriceBreakListDescription:string,
   PriceGroupDescription:string,
   ProdCodeDescription:string,
   QuoteNumInPrice:boolean,
   QuoteNumCurrencyCode:string,
   SalesCatIDDescription:string,
   TaxCatIDDescription:string,
   TaxRegionDescription:string,
   TaxRegionTaxConnectCalc:boolean,
   TerritoryIDTerritoryDesc:string,
   WarrantyCodeWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QuoteDtlSearchTableset{
   QuoteDtl:Erp_Tablesets_QuoteDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtQuoteDtlSearchTableset{
   QuoteDtl:Erp_Tablesets_QuoteDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param quoteNum
      @param quoteLine
   */  
export interface GetByID_input{
   quoteNum:number,
   quoteLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_QuoteDtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_QuoteDtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_QuoteDtlSearchTableset[],
}

   /** Required : 
      @param whereClauseQuoteDtl
      @param whereClauseQuoteHed
      @param whereClauseCustomer
      @param conclusion
      @param sortBy
      @param pageSize
      @param absolutePage
   */  
export interface GetListCustom_input{
      /**  The where clause to restrict data for QuoteDtl  */  
   whereClauseQuoteDtl:string,
      /**  The where clause to restrict data for QuoteHed  */  
   whereClauseQuoteHed:string,
      /**  The where clause to restrict data for Customer  */  
   whereClauseCustomer:string,
      /**  Won, NotWon, All  */  
   conclusion:string,
      /**  sortBy Selected  */  
   sortBy:string,
      /**  The page size, used only for UI adapter  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adapter  */  
   absolutePage:number,
}

export interface GetListCustom_output{
   returnObj:Erp_Tablesets_QuoteDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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
   returnObj:Erp_Tablesets_QuoteDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param quoteNum
   */  
export interface GetNewQuoteDtl_input{
   ds:Erp_Tablesets_QuoteDtlSearchTableset[],
   quoteNum:number,
}

export interface GetNewQuoteDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteDtlSearchTableset[],
}
}

   /** Required : 
      @param whereClauseQuoteDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseQuoteDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_QuoteDtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtQuoteDtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtQuoteDtlSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_QuoteDtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_QuoteDtlSearchTableset[],
}
}

