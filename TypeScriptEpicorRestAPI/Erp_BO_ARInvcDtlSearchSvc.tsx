import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ARInvcDtlSearchSvc
// Description: bo/ARInvcDtlSearch
           Search used to find AR Invoice Lines (InvcDtl)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/$metadata", {
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
   Description: Get ARInvcDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARInvcDtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRow
   */  
export function get_ARInvcDtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/ARInvcDtlSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARInvcDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARInvcDtlSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/ARInvcDtlSearches", {
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
   Summary: Calls GetByID to retrieve the ARInvcDtlSearch item
   Description: Calls GetByID to retrieve the ARInvcDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARInvcDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   */  
export function get_ARInvcDtlSearches_Company_InvoiceNum_InvoiceLine(Company:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InvcDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/ARInvcDtlSearches(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InvcDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARInvcDtlSearch for the service
   Description: Calls UpdateExt to update ARInvcDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARInvcDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARInvcDtlSearches_Company_InvoiceNum_InvoiceLine(Company:string, InvoiceNum:string, InvoiceLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/ARInvcDtlSearches(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", {
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
   Summary: Call UpdateExt to delete ARInvcDtlSearch item
   Description: Call UpdateExt to delete ARInvcDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARInvcDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARInvcDtlSearches_Company_InvoiceNum_InvoiceLine(Company:string, InvoiceNum:string, InvoiceLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/ARInvcDtlSearches(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlListRow)
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
export function get_GetRows(whereClauseInvcDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseInvcDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInvcDtl=" + whereClauseInvcDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/GetRows" + params, {
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
export function get_GetByID(invoiceNum:string, invoiceLine:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof invoiceNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "invoiceNum=" + invoiceNum
   }
   if(typeof invoiceLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "invoiceLine=" + invoiceLine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetListAlternalSearch
   Description: Allows use of InvcHead filter but returns only InvcDtl records.
   OperationID: GetListAlternalSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListAlternalSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListAlternalSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListAlternalSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/GetListAlternalSearch", {
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
   Summary: Invoke method GetNewInvcDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInvcDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInvcDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/GetNewInvcDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcDtlListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcDtlRow[],
}

export interface Erp_Tablesets_InvcDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Foreign key to the InvcHead.  */  
   "InvoiceNum":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   "InvoiceLine":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  */  
   "LineType":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  */  
   "XRevisionNum":string,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   "PartNum":string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   "LineDesc":string,
      /**  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  */  
   "IUM":string,
      /**  Our Current Revision Number for this Part.  */  
   "RevisionNum":string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   "POLine":string,
      /**  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  */  
   "TaxExempt":string,
      /**  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  */  
   "TaxCatID":string,
      /**   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  */  
   "Commissionable":boolean,
      /**   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  */  
   "DiscountPercent":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "UnitPrice":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "DocUnitPrice":number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  */  
   "OurOrderQty":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "ExtPrice":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "DocExtPrice":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "Discount":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "DocDiscount":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "TotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "DocTotalMiscChrg":number,
      /**  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  */  
   "ProdCode":string,
      /**  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  */  
   "OurShipQty":number,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  The packing slip line number that is being invoiced.  */  
   "PackLine":number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   "OrderNum":number,
      /**  The associated sales order line number.  */  
   "OrderLine":number,
      /**  Contains the release number of the order line item that is being invoiced.  */  
   "OrderRelNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   "ShipToNum":string,
      /**  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  */  
   "ShipDate":string,
      /**  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  */  
   "ShipViaCode":string,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   "AdvanceBillCredit":number,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   "DocAdvanceBillCredit":number,
      /**  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  */  
   "CustNum":number,
      /**  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  */  
   "InvoiceComment":string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   "ShpConNum":number,
      /**  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "MtlBurUnitCost":number,
      /**  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  */  
   "COSPostingReqd":boolean,
      /**   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   "COSPosted":boolean,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   "CallNum":number,
      /**  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  */  
   "CallCode":string,
      /**   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   "RMANum":number,
      /**   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  */  
   "RMALine":number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   "SalesCatID":string,
      /**   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  */  
   "JournalCode":string,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  */  
   "SellingOrderQty":number,
      /**  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  */  
   "SellingShipQty":number,
      /**  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Project Id that links the invoice detail  to the Project table.  */  
   "ProjectID":string,
      /**  Milestone id that links the invoice detail  to the ProjectMilestone.  */  
   "MilestoneID":string,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  */  
   "ListPrice":number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  */  
   "OrdBasedPrice":number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  */  
   "DocOrdBasedPrice":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "AdvGainLoss":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Sales representative commission rate.  */  
   "RepRate1":number,
      /**  Sales representative commission rate.  */  
   "RepRate2":number,
      /**  Sales representative commission rate.  */  
   "RepRate3":number,
      /**  Sales representative commission rate.  */  
   "RepRate4":number,
      /**  Sales representative commission rate.  */  
   "RepRate5":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit1":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit2":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit3":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit4":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit5":number,
      /**  Bill To Customer Number used for consolidated invoices  */  
   "BTCustNum":number,
      /**  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCMtlUnitCost":number,
      /**  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCLbrUnitCost":number,
      /**  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCBurUnitCost":number,
      /**  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCSubUnitCost":number,
      /**  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCMtlBurUnitCost":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  */  
   "RevChargeMethod":string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   "OverrideReverseCharge":boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   "RevChargeApplied":boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPrice":number,
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
      /**  Reporting currency value of this field  */  
   "Rpt1TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt1AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt2AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt3AdvGainLoss":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping adress country Number.  */  
   "OTSCountryNum":number,
      /**  Value is copied from PartTran for PE  */  
   "Plant":string,
      /**  value is copied from PartTran for PE  */  
   "WarehouseCode":string,
      /**  value is copied from PartTran for PE  */  
   "CallLine":number,
      /**  Drop Shipment Pack Line  */  
   "DropShipPackLine":number,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  FK to the Finance Charges table  */  
   "FinChargeCode":string,
      /**  Reference to the ABT, it is GUID, used in PostingEngine  */  
   "ABTUID":string,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "InUnitPrice":number,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "DocInUnitPrice":number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "InExtPrice":number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "DocInExtPrice":number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "InDiscount":number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "DocInDiscount":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   "InTotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   "DocInTotalMiscChrg":number,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  */  
   "InListPrice":number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  */  
   "DocInListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  */  
   "InOrdBasedPrice":number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  */  
   "DocInOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InUnitPrice":number,
      /**  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  */  
   "CorrectionDtl":boolean,
      /**  Asset number of the linked Asset Disposal transaction.  */  
   "AssetNum":string,
      /**  Unique number to identify the linked Asset Disposal transaction.  */  
   "DisposalNum":number,
      /**   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  */  
   "PBLineType":string,
      /**  Invoice line reference  */  
   "InvoiceLineRef":number,
      /**  Invoice Number Reference  */  
   "InvoiceRef":number,
      /**  Lot Number.  This field should be set according to the linked Shipment Line.  */  
   "LotNum":string,
      /**  Reference to the draft invoice line created in Invoice Preparation  */  
   "PBInvoiceLine":number,
      /**  Contains the value of the AC_RAHead.RAID client accommodation.  */  
   "RAID":number,
      /**  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  */  
   "RADtlID":number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Starting date the revenue is deferred.  */  
   "DefRevStart":string,
      /**  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  */  
   "ChargeDefRev":boolean,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "EnableRMAUpdate":boolean,
   "EnableRMADelete":boolean,
      /**  Group associated to the invoice  */  
   "GroupID":string,
      /**  ExtPrice-disc+misc charges.  */  
   "LineTotal":number,
      /**  ExtPrice-disc+misc charges.  */  
   "DocLineTotal":number,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   "CurrencySwitch":boolean,
      /**  Line tax amount  */  
   "LineTax":number,
      /**  Doc line tax  */  
   "DocLineTax":number,
      /**  Tax buton sensitive or not.  */  
   "IsTaxBtnSensitive":boolean,
      /**  Is commission button sensitive  */  
   "IsCommisBtnSensitive":boolean,
      /**  PO number for display.  */  
   "DispPONum":string,
      /**  original tax category  */  
   "OrigTaxCat":string,
      /**  Currency display symbol  */  
   "DisplaySymbol":string,
      /**  1st sales rep of the invoice.  */  
   "SalesRepCode1":string,
      /**  2nd sales rep of the invoice header.  */  
   "SalesRepCode2":string,
      /**  3rd sales rep code of the invoice header.  */  
   "SalesRepCode3":string,
      /**  4th sales rep code of the invoice header.  */  
   "SalesRepCode4":string,
      /**  5th salesrep code of the invoice header.  */  
   "SalesRepCode5":string,
      /**  Ship to display address  */  
   "DispShipToAddr":string,
      /**  Set to true if intrastat is enabled.  */  
   "IsIntrastatSensitive":boolean,
      /**  1st sales rep name  */  
   "SalesRepName1":string,
      /**  2nd sales rep name  */  
   "SalesRepName2":string,
      /**  3rd sales rep name  */  
   "SalesRepName3":string,
      /**  4th sales rep name  */  
   "SalesRepName4":string,
      /**  5th sales rep name  */  
   "SalesRepName5":string,
      /**  Invoice header type  */  
   "InvoiceType":string,
      /**  OrderUM display  */  
   "OrderUM":string,
      /**  Document display symbol.  */  
   "DocDisplaySymbol":string,
      /**  display discount  */  
   "LessDiscount":number,
      /**  Document discount amount  */  
   "DocLessDiscount":number,
      /**  Display selling ship qty  */  
   "DspSellingShipQty":number,
      /**  Display ext price  */  
   "DspExtPrice":number,
      /**  Display document ext price  */  
   "DspDocExtPrice":number,
      /**  Display discount  */  
   "DspDiscount":number,
      /**  Display document discount  */  
   "DspDocDiscount":number,
      /**  Display total misc. charges  */  
   "DspTotalMiscChrg":number,
      /**  Display document total misc. charge  */  
   "DspDocTotalMiscChrg":number,
      /**  Display our ship qty  */  
   "DspOurShipQty":number,
      /**  Display less discount  */  
   "DspLessDiscount":number,
      /**  Display document less discount  */  
   "DspDocLessDiscount":number,
      /**  Display advance bill credit  */  
   "DspAdvanceBillCredit":number,
      /**  Display documents advance bill credit  */  
   "DspDocAdvanceBillCredit":number,
      /**  Display line tax  */  
   "DspLineTax":number,
      /**  Display document line tax  */  
   "DspDocLineTax":number,
      /**  Display line total  */  
   "DspLineTotal":number,
      /**  Display document line total  */  
   "DspDocLineTotal":number,
      /**  Adv bill enabled flag  */  
   "AdvBillEnabled":boolean,
   "DspTaxExempt":string,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  Invoice Header Legal Number  */  
   "InvLegalNum":string,
      /**  Invoice Detail Customer Name  */  
   "CustomerName":string,
      /**  Ship Head Legal Number  */  
   "ShpLegalNum":string,
      /**  Invoice Date from InvcHead.  */  
   "InvoiceDate":string,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   "SoldToCustID":string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   "SoldToCustName":string,
      /**  CustID associated with the InvcDtl.BTCustNum field.  */  
   "BillToCustID":string,
      /**  Customer Name associated with the InvcDtl.BTCustNum field.  */  
   "BTCustName":string,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   "CustID":string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   "CustName":string,
      /**  Invoice head due date.  */  
   "DueDate":string,
      /**  Terms code from InvcHead.  */  
   "TermsCode":string,
      /**  Open invoice flag from InvcHead.  */  
   "OpenInvoice":boolean,
      /**  Posted flag from the InvcHead.  */  
   "Posted":boolean,
      /**  Currency code from InvcHead.  */  
   "CurrencyCode":string,
   "AllowTaxCodeUpd":boolean,
   "ShipToContactEMailAddress":string,
   "ShipToContactFaxNum":string,
   "ShipToContactName":string,
   "ShipToContactPhoneNum":string,
   "Rpt1DspAdvanceBillCredit":number,
   "Rpt2DspAdvanceBillCredit":number,
   "Rpt3DspAdvanceBillCredit":number,
   "Rpt1DspDiscount":number,
   "Rpt2DspDiscount":number,
   "Rpt3DspDiscount":number,
   "Rpt1DspExtPrice":number,
   "Rpt2DspExtPrice":number,
   "Rpt3DspExtPrice":number,
   "Rpt1DspLessDiscount":number,
   "Rpt2DspLessDiscount":number,
   "Rpt3DspLessDiscount":number,
   "Rpt1DspLineTax":number,
   "Rpt2DspLineTax":number,
   "Rpt3DspLineTax":number,
   "Rpt1DspLineTotal":number,
   "Rpt2DspLineTotal":number,
   "Rpt3DspLineTotal":number,
   "Rpt1DspTotalMiscChrg":number,
   "Rpt2DspTotalMiscChrg":number,
   "Rpt3DspTotalMiscChrg":number,
   "Rpt1LineTax":number,
   "Rpt2LineTax":number,
   "Rpt3LineTax":number,
   "Rpt1LineTotal":number,
   "Rpt2LineTotal":number,
   "Rpt3LineTotal":number,
      /**  Drop Shipment  */  
   "DropShipment":boolean,
   "DspUnitPrice":number,
   "DocDspUnitPrice":number,
   "Rpt1DspUnitPrice":number,
   "Rpt2DspUnitPrice":number,
   "Rpt3DspUnitPrice":number,
   "InPrice":boolean,
      /**  Display Invoice Reference  */  
   "DspInvoiceRef":number,
   "DispGLAcct":string,
      /**  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  */  
   "RASchedExists":boolean,
      /**  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  */  
   "DeleteRASchedule":boolean,
   "RADesc":string,
   "ContractSuspended":boolean,
      /**  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  */  
   "CheckAmortAmounts":boolean,
      /**  Description of the Call Type Code.  */  
   "CallCodeCallDescription":string,
      /**  Description of the service contract.  */  
   "ContractCodeContractDescription":string,
      /**  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  */  
   "ContractNumSuspended":boolean,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   "CustCntPhoneNum":string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   "CustCntFaxNum":string,
      /**  Contact's middle name.  */  
   "CustCntMiddleName":string,
      /**  Contact's first name.  */  
   "CustCntFirstName":string,
      /**  Full name of the contact.  */  
   "CustCntName":string,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   "CustCntCorpName":string,
      /**  Contact's last name.  */  
   "CustCntLastName":string,
      /**  The member's name on the credit card.  */  
   "InvoiceNumCardMemberName":string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "InvoiceNumTermsCode":string,
      /**  Journal  Description.  */  
   "JournalCodeJrnlDescription":string,
      /**  Description  */  
   "MilestoneIDDescription":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "OrderLineLineDesc":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  Country name  */  
   "OTSCntryDescription":string,
      /**  Line description.  */  
   "PackLineLineDesc":string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   "PackNumName":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
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
      /**  Full description of Product Group.  */  
   "ProdCodeDescription":string,
      /**  Full description of Project Management Code.  */  
   "ProjectIDDescription":string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   "RMALineLineDesc":string,
      /**  Description of the sales category.  */  
   "SalesCatIDDescription":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "ShipToCustCustID":string,
      /**  The full name of the customer.  */  
   "ShipToCustName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "ShipToCustBTName":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  Full description for the Sales Tax category.  */  
   "TaxCatIDDescription":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InvcDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Foreign key to the InvcHead.  */  
   "InvoiceNum":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   "InvoiceLine":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  */  
   "LineType":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  */  
   "XRevisionNum":string,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   "PartNum":string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   "LineDesc":string,
      /**  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  */  
   "IUM":string,
      /**  Our Current Revision Number for this Part.  */  
   "RevisionNum":string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   "POLine":string,
      /**  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  */  
   "TaxExempt":string,
      /**  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  */  
   "TaxCatID":string,
      /**   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  */  
   "Commissionable":boolean,
      /**   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  */  
   "DiscountPercent":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "UnitPrice":number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "DocUnitPrice":number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  */  
   "OurOrderQty":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "ExtPrice":number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "DocExtPrice":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "Discount":number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "DocDiscount":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "TotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "DocTotalMiscChrg":number,
      /**  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  */  
   "ProdCode":string,
      /**  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  */  
   "OurShipQty":number,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  The packing slip line number that is being invoiced.  */  
   "PackLine":number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   "OrderNum":number,
      /**  The associated sales order line number.  */  
   "OrderLine":number,
      /**  Contains the release number of the order line item that is being invoiced.  */  
   "OrderRelNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   "ShipToNum":string,
      /**  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  */  
   "ShipDate":string,
      /**  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  */  
   "ShipViaCode":string,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   "AdvanceBillCredit":number,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   "DocAdvanceBillCredit":number,
      /**  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  */  
   "CustNum":number,
      /**  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  */  
   "InvoiceComment":string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   "ShpConNum":number,
      /**  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   "MtlBurUnitCost":number,
      /**  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  */  
   "COSPostingReqd":boolean,
      /**   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   "COSPosted":boolean,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   "CallNum":number,
      /**  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  */  
   "CallCode":string,
      /**   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   "RMANum":number,
      /**   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  */  
   "RMALine":number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   "SalesCatID":string,
      /**   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  */  
   "JournalCode":string,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  */  
   "SellingOrderQty":number,
      /**  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  */  
   "SellingShipQty":number,
      /**  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Project Id that links the invoice detail  to the Project table.  */  
   "ProjectID":string,
      /**  Milestone id that links the invoice detail  to the ProjectMilestone.  */  
   "MilestoneID":string,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  */  
   "ListPrice":number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  */  
   "OrdBasedPrice":number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  */  
   "DocOrdBasedPrice":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "AdvGainLoss":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Sales representative commission rate.  */  
   "RepRate1":number,
      /**  Sales representative commission rate.  */  
   "RepRate2":number,
      /**  Sales representative commission rate.  */  
   "RepRate3":number,
      /**  Sales representative commission rate.  */  
   "RepRate4":number,
      /**  Sales representative commission rate.  */  
   "RepRate5":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit1":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit2":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit3":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit4":number,
      /**  Sales representative commission percentage.  */  
   "RepSplit5":number,
      /**  Bill To Customer Number used for consolidated invoices  */  
   "BTCustNum":number,
      /**  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCMtlUnitCost":number,
      /**  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCLbrUnitCost":number,
      /**  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCBurUnitCost":number,
      /**  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCSubUnitCost":number,
      /**  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   "JCMtlBurUnitCost":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  */  
   "RevChargeMethod":string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   "OverrideReverseCharge":boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   "RevChargeApplied":boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AdvanceBillCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPrice":number,
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
      /**  Reporting currency value of this field  */  
   "Rpt1TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt1AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt2AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt3AdvGainLoss":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping adress country Number.  */  
   "OTSCountryNum":number,
      /**  Value is copied from PartTran for PE  */  
   "Plant":string,
      /**  value is copied from PartTran for PE  */  
   "WarehouseCode":string,
      /**  value is copied from PartTran for PE  */  
   "CallLine":number,
      /**  Drop Shipment Pack Line  */  
   "DropShipPackLine":number,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  FK to the Finance Charges table  */  
   "FinChargeCode":string,
      /**  Reference to the ABT, it is GUID, used in PostingEngine  */  
   "ABTUID":string,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "InUnitPrice":number,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   "DocInUnitPrice":number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "InExtPrice":number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   "DocInExtPrice":number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "InDiscount":number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   "DocInDiscount":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   "InTotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   "DocInTotalMiscChrg":number,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  */  
   "InListPrice":number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  */  
   "DocInListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  */  
   "InOrdBasedPrice":number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  */  
   "DocInOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InListPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InOrdBasedPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InUnitPrice":number,
      /**  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  */  
   "CorrectionDtl":boolean,
      /**  Asset number of the linked Asset Disposal transaction.  */  
   "AssetNum":string,
      /**  Unique number to identify the linked Asset Disposal transaction.  */  
   "DisposalNum":number,
      /**   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  */  
   "PBLineType":string,
      /**  Invoice line reference  */  
   "InvoiceLineRef":number,
      /**  Invoice Number Reference  */  
   "InvoiceRef":number,
      /**  Lot Number.  This field should be set according to the linked Shipment Line.  */  
   "LotNum":string,
      /**  Reference to the draft invoice line created in Invoice Preparation  */  
   "PBInvoiceLine":number,
      /**  Contains the value of the AC_RAHead.RAID client accommodation.  */  
   "RAID":number,
      /**  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  */  
   "RADtlID":number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   "DeferredRev":boolean,
      /**  Revenue Amortization Code.  */  
   "RACode":string,
      /**  Starting date the revenue is deferred.  */  
   "DefRevStart":string,
      /**  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  */  
   "ChargeDefRev":boolean,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  DefRevPosted  */  
   "DefRevPosted":boolean,
      /**  Unit price of Invoice linked to Bill of Exchange in original currency.  */  
   "LinkedInvcUnitPrice":number,
      /**  Withholding Tax Amount in reporting currency  */  
   "DspWithholdAmt":number,
      /**  Withholding Tax Amount in document currency  */  
   "DocDspWithholdAmt":number,
      /**  Withholding tax amount in reporting currency  */  
   "Rpt1DspWithholdAmt":number,
      /**  Withholding tax amount in reporting currency  */  
   "Rpt2DspWithholdAmt":number,
      /**  Withholding tax amount in reporting currency  */  
   "Rpt3DspWithholdAmt":number,
      /**  Currency code from linked Invoice Header  */  
   "LinkedCurrencyCode":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  PEBOEHeadNum  */  
   "PEBOEHeadNum":number,
      /**  MXSellingShipQty  */  
   "MXSellingShipQty":number,
      /**  MXUnitPrice  */  
   "MXUnitPrice":number,
      /**  DocMXUnitPrice  */  
   "DocMXUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1MXUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MXUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MXUnitPrice":number,
      /**  CustCostCenter  */  
   "CustCostCenter":string,
      /**  DEIsServices  */  
   "DEIsServices":boolean,
      /**  DEIsSecurityFinancialDerivative  */  
   "DEIsSecurityFinancialDerivative":boolean,
      /**  DEInternationalSecuritiesID  */  
   "DEInternationalSecuritiesID":string,
      /**  DEIsInvestment  */  
   "DEIsInvestment":boolean,
      /**  DEPayStatCode  */  
   "DEPayStatCode":string,
      /**  DefRevEndDate  */  
   "DefRevEndDate":string,
      /**  EntityUseCode  */  
   "EntityUseCode":string,
      /**  Indicates tha this invoice Line was reclassified.  */  
   "Reclassified":boolean,
      /**  Enables the user the ability to override the Percent or Amount of revenue to be deferred  */  
   "PartiallyDefer":boolean,
      /**  Percentage of revenue to be deferred for this line item  */  
   "DeferredPercent":number,
      /**  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  */  
   "Reclass":boolean,
      /**  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  */  
   "DeferredOnly":boolean,
      /**  Reclassification Code. This field will be required if Reclass is checked.  */  
   "ReclassCodeID":string,
      /**  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  */  
   "ReclassReasonCode":string,
      /**  Internal comments for reclassification entered by the user.  */  
   "ReclassComments":string,
      /**  Deferred Revenue Amount in base currency  */  
   "DeferredRevAmt":number,
      /**  Deferred Revenue Amount in document currency  */  
   "DocDeferredRevAmt":number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   "Rpt1DeferredRevAmt":number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   "Rpt2DeferredRevAmt":number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   "Rpt3DeferredRevAmt":number,
      /**  ChargeReclass  */  
   "ChargeReclass":boolean,
      /**  DEDenomination  */  
   "DEDenomination":string,
      /**  DropShipPONum  */  
   "DropShipPONum":number,
      /**  DocInAdvanceBillCredit  */  
   "DocInAdvanceBillCredit":number,
      /**  InAdvanceBillCredit  */  
   "InAdvanceBillCredit":number,
      /**  Rpt1InAdvanceBillCredit  */  
   "Rpt1InAdvanceBillCredit":number,
      /**  Rpt2InAdvanceBillCredit  */  
   "Rpt2InAdvanceBillCredit":number,
      /**  Rpt3InAdvanceBillCredit  */  
   "Rpt3InAdvanceBillCredit":number,
      /**  MYIndustryCode  */  
   "MYIndustryCode":string,
      /**  The dockingstation of the shipto address.  For future use.  */  
   "DockingStation":string,
      /**  ConsolidateLines  */  
   "ConsolidateLines":boolean,
      /**  MXCustomsDuty  */  
   "MXCustomsDuty":string,
      /**  CommodityCode  */  
   "CommodityCode":string,
      /**  MXProdServCode  */  
   "MXProdServCode":string,
      /**  Quote number to which this line item detail record is associated with.  */  
   "QuoteNum":number,
      /**  Quote Line number from which this invoice line was created from.  */  
   "QuoteLine":number,
      /**  True if transaction is related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  MXCustomsUMFrom  */  
   "MXCustomsUMFrom":string,
      /**  PE Detraction good or service code  */  
   "PEDetrGoodServiceCode":string,
      /**  PETaxExempt  */  
   "PETaxExempt":string,
      /**  Order number on the Invoicing Company.  */  
   "CColOrderNum":number,
      /**  Order number line the Invoicing Company.  */  
   "CColOrderLine":number,
      /**  Order number release the Invoicing Company.  */  
   "CColOrderRel":number,
      /**  Invoice Line reference on the Invoicing Company.  */  
   "CColInvoiceLineRef":number,
      /**  Packing slip number on the Invoicing Company.  */  
   "CColPackNum":number,
      /**  Packing slip line number on the Invoicing Company.  */  
   "CColPackLine":number,
      /**  Drop shipment packing slip number on the Invoicing Company.  */  
   "CColDropShipPackSlip":string,
      /**  Drop shipment packing slip line number on the Invoicing Company.  */  
   "CColDropShipPackSlipLine":number,
      /**  Ship To Customer ID from the Invoice Line in the subsidiary company.  */  
   "CColShipToCustID":string,
      /**  Ship To from the Invoice Line in the subsidiary company.  */  
   "CColShipToNum":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Exempt Reason Code  */  
   "ExemptReasonCode":string,
      /**  Associates the Call Line record back its linked jobnum  */  
   "JobNum":string,
      /**  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  */  
   "ServiceSource":string,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  */  
   "AssemblySeq":number,
      /**  Job Mtl seq used to create invoice line from service call job  */  
   "MtlSeq":number,
      /**  Job subcontract oper seq used to create invoice line from service call job  */  
   "OprSeq":number,
      /**  Indicates the labor type of the LaborDtl used to create invoice from service call job.  */  
   "LaborType":string,
      /**  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  */  
   "BillableLaborHrs":number,
      /**  Billable rate used to create invoice line from labor related to service call job. In base currency.  */  
   "BillableLaborRate":number,
      /**  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  */  
   "ServiceSourceType":string,
      /**  TotalCovenantDiscount  */  
   "TotalCovenantDiscount":number,
      /**  DocCovenantDiscount  */  
   "DocCovenantDiscount":number,
      /**  Rpt1CovenantDiscount  */  
   "Rpt1CovenantDiscount":number,
      /**  Rpt2CovenantDiscount  */  
   "Rpt2CovenantDiscount":number,
      /**  Rpt3CovenantDiscount  */  
   "Rpt3CovenantDiscount":number,
      /**  TotalInCovenantDiscount  */  
   "TotalInCovenantDiscount":number,
      /**  DocInCovenantDiscount  */  
   "DocInCovenantDiscount":number,
      /**  Rpt1InCovenantDiscount  */  
   "Rpt1InCovenantDiscount":number,
      /**  Rpt2InCovenantDiscount  */  
   "Rpt2InCovenantDiscount":number,
      /**  Rpt3InCovenantDiscount  */  
   "Rpt3InCovenantDiscount":number,
      /**  Adv bill enabled flag  */  
   "AdvBillEnabled":boolean,
   "AllowTaxCodeUpd":boolean,
      /**  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  */  
   "AllowUpdPartDefer":boolean,
      /**  CustID associated with the InvcDtl.BTCustNum field.  */  
   "BillToCustID":string,
      /**  Customer Name associated with the InvcDtl.BTCustNum field.  */  
   "BTCustName":string,
      /**  The date and time that the record was last changed  */  
   "ChangeDateTime":string,
      /**  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  */  
   "CheckAmortAmounts":boolean,
   "CNGTIDescription1":string,
   "CNGTIDescription2":string,
   "CNGTIDescription3":string,
      /**  CSF China, discount tax amount  */  
   "CNGTIDiscountTaxAmount":number,
   "CNGTIIUM":string,
   "CNGTINetAmount":number,
   "CNGTIPartDescription":string,
   "CNGTISpecification":string,
   "CNGTITaxAmount":number,
   "CNGTITaxCode":string,
   "CNGTITaxPercent":number,
   "CNGTITotalAmount":number,
      /**  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  */  
   "CNGTIUnitPrice":number,
   "ContractSuspended":boolean,
      /**  Currency code from InvcHead.  */  
   "CurrencyCode":string,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   "CurrencySwitch":boolean,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   "CustID":string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   "CustName":string,
      /**  Invoice Detail Customer Name  */  
   "CustomerName":string,
      /**  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  */  
   "DeleteRASchedule":boolean,
   "DispGLAcct":string,
      /**  Currency display symbol  */  
   "DisplaySymbol":string,
      /**  PO number for display.  */  
   "DispPONum":string,
      /**  Ship to display address  */  
   "DispShipToAddr":string,
      /**  Document display symbol.  */  
   "DocDisplaySymbol":string,
   "DocDspUnitPrice":number,
      /**  Document discount amount  */  
   "DocLessDiscount":number,
      /**  Doc line tax  */  
   "DocLineTax":number,
      /**  ExtPrice-disc+misc charges.  */  
   "DocLineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "DocPEDetAmt":number,
      /**  Drop Shipment  */  
   "DropShipment":boolean,
      /**  Display advance bill credit  */  
   "DspAdvanceBillCredit":number,
      /**  Display discount  */  
   "DspDiscount":number,
      /**  Display documents advance bill credit  */  
   "DspDocAdvanceBillCredit":number,
      /**  Display document discount  */  
   "DspDocDiscount":number,
      /**  Display document ext price  */  
   "DspDocExtPrice":number,
      /**  Display document less discount  */  
   "DspDocLessDiscount":number,
      /**  Display document line tax  */  
   "DspDocLineTax":number,
      /**  Display document line total  */  
   "DspDocLineTotal":number,
      /**  Display document total misc. charge  */  
   "DspDocTotalMiscChrg":number,
      /**  Display ext price  */  
   "DspExtPrice":number,
      /**  Display Invoice Reference  */  
   "DspInvoiceRef":number,
      /**  Display less discount  */  
   "DspLessDiscount":number,
      /**  Display line tax  */  
   "DspLineTax":number,
      /**  Display line total  */  
   "DspLineTotal":number,
      /**  Display our ship qty  */  
   "DspOurShipQty":number,
      /**  Display selling ship qty  */  
   "DspSellingShipQty":number,
   "DspTaxExempt":string,
      /**  Display total misc. charges  */  
   "DspTotalMiscChrg":number,
   "DspUnitPrice":number,
      /**  Invoice head due date.  */  
   "DueDate":string,
      /**  FSA Technician  */  
   "EmpID":string,
   "EnableDspWithholdAmt":boolean,
   "EnableRMADelete":boolean,
   "EnableRMAUpdate":boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   "FSAAction":string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "FSACallCode":string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "FSAContractCode":string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "FSAContractNum":number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   "FSAEmpID":string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   "FSAEquipmentInstallID":number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   "FSAEquipmentPartNum":string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   "FSAWarrantyCode":string,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  Group associated to the invoice  */  
   "GroupID":string,
   "InPrice":boolean,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
      /**  Invoice Header Legal Number  */  
   "InvLegalNum":string,
      /**  Invoice Date from InvcHead.  */  
   "InvoiceDate":string,
      /**  Invoice header type  */  
   "InvoiceType":string,
      /**  Is commission button sensitive  */  
   "IsCommisBtnSensitive":boolean,
      /**  Set to true if intrastat is enabled.  */  
   "IsIntrastatSensitive":boolean,
      /**  Tax buton sensitive or not.  */  
   "IsTaxBtnSensitive":boolean,
      /**  display discount  */  
   "LessDiscount":number,
      /**  Line tax amount  */  
   "LineTax":number,
      /**  ExtPrice-disc+misc charges.  */  
   "LineTotal":number,
   "LinkedCurrencySymbol":string,
      /**  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  */  
   "NoShipTaxRgnInfo":boolean,
      /**  Open invoice flag from InvcHead.  */  
   "OpenInvoice":boolean,
      /**  OrderUM display  */  
   "OrderUM":string,
      /**  original tax category  */  
   "OrigTaxCat":string,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "PEDetAmt":number,
      /**  PE Detraction good or service code description  */  
   "PEDetrGoodServiceCodeDesc":string,
   "PEDspCurrencySymbol":string,
      /**  PE VAT Exemption Reason  */  
   "PEVATExemptionReason":string,
      /**  Posted flag from the InvcHead.  */  
   "Posted":boolean,
   "RADesc":string,
      /**  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  */  
   "RASchedExists":boolean,
      /**  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  */  
   "RemoveManAdTax":boolean,
   "Rpt1DspAdvanceBillCredit":number,
   "Rpt1DspDiscount":number,
   "Rpt1DspExtPrice":number,
   "Rpt1DspLessDiscount":number,
   "Rpt1DspLineTax":number,
   "Rpt1DspLineTotal":number,
   "Rpt1DspTotalMiscChrg":number,
   "Rpt1DspUnitPrice":number,
   "Rpt1LineTax":number,
   "Rpt1LineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt1PEDetAmt":number,
   "Rpt2DspAdvanceBillCredit":number,
   "Rpt2DspDiscount":number,
   "Rpt2DspExtPrice":number,
   "Rpt2DspLessDiscount":number,
   "Rpt2DspLineTax":number,
   "Rpt2DspLineTotal":number,
   "Rpt2DspTotalMiscChrg":number,
   "Rpt2DspUnitPrice":number,
   "Rpt2LineTax":number,
   "Rpt2LineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt2PEDetAmt":number,
   "Rpt3DspAdvanceBillCredit":number,
   "Rpt3DspDiscount":number,
   "Rpt3DspExtPrice":number,
   "Rpt3DspLessDiscount":number,
   "Rpt3DspLineTax":number,
   "Rpt3DspLineTotal":number,
   "Rpt3DspTotalMiscChrg":number,
   "Rpt3DspUnitPrice":number,
   "Rpt3LineTax":number,
   "Rpt3LineTotal":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt3PEDetAmt":number,
      /**  1st sales rep of the invoice.  */  
   "SalesRepCode1":string,
      /**  2nd sales rep of the invoice header.  */  
   "SalesRepCode2":string,
      /**  3rd sales rep code of the invoice header.  */  
   "SalesRepCode3":string,
      /**  4th sales rep code of the invoice header.  */  
   "SalesRepCode4":string,
      /**  5th salesrep code of the invoice header.  */  
   "SalesRepCode5":string,
      /**  1st sales rep name  */  
   "SalesRepName1":string,
      /**  2nd sales rep name  */  
   "SalesRepName2":string,
      /**  3rd sales rep name  */  
   "SalesRepName3":string,
      /**  4th sales rep name  */  
   "SalesRepName4":string,
      /**  5th sales rep name  */  
   "SalesRepName5":string,
   "ShipToContactEMailAddress":string,
   "ShipToContactFaxNum":string,
   "ShipToContactName":string,
   "ShipToContactPhoneNum":string,
      /**  Ship Head Legal Number  */  
   "ShpLegalNum":string,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   "SoldToCustID":string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   "SoldToCustName":string,
      /**  Terms code from InvcHead.  */  
   "TermsCode":string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   "WarrantyCode":string,
      /**  This flag allow updating Reclassification data.  */  
   "AllowReclassify":boolean,
      /**  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  */  
   "LineAmtRecalcd":boolean,
      /**  Set to true if extra trade statistics is enabled.  */  
   "IsExtrastatSensitive":boolean,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   "TrackInventoryByRevision":boolean,
   "BitFlag":number,
   "CallCodeCallDescription":string,
   "CommodityCodeDescription":string,
   "ContractCodeContractDescription":string,
   "ContractNumSuspended":boolean,
   "CustCntName":string,
   "CustCntMiddleName":string,
   "CustCntFirstName":string,
   "CustCntFaxNum":string,
   "CustCntCorpName":string,
   "CustCntPhoneNum":string,
   "CustCntLastName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "CustNumAllowShipTo3":boolean,
   "CustNumBTName":string,
   "InvoiceNumTermsCode":string,
   "InvoiceNumCardMemberName":string,
   "JournalCodeJrnlDescription":string,
   "MilestoneIDDescription":string,
   "MXProdServCodeDesc":string,
   "OrderLineLineDesc":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "OTSCntryEUMember":boolean,
   "OTSCntryISOCode":string,
   "OTSCntryDescription":string,
   "PackLineLineDesc":string,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "ProdCodeDescription":string,
   "ProjectIDDescription":string,
   "ReclassCodeDescription":string,
   "ReclassReasonDescription":string,
   "RMALineLineDesc":string,
   "SalesCatIDDescription":string,
   "ShipToCustCustID":string,
   "ShipToCustName":string,
   "ShipToCustBTName":string,
   "ShipToNumInactive":boolean,
   "ShipToNumName":string,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "TaxCatIDDescription":string,
   "TaxRegionDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param invoiceNum
      @param invoiceLine
   */  
export interface DeleteByID_input{
   invoiceNum:number,
   invoiceLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ARInvcDtlSearchTableset{
   InvcDtl:Erp_Tablesets_InvcDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InvcDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  */  
   LineType:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  */  
   XRevisionNum:string,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   PartNum:string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   LineDesc:string,
      /**  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  */  
   IUM:string,
      /**  Our Current Revision Number for this Part.  */  
   RevisionNum:string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   POLine:string,
      /**  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  */  
   TaxExempt:string,
      /**  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  */  
   TaxCatID:string,
      /**   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  */  
   Commissionable:boolean,
      /**   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  */  
   DiscountPercent:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   UnitPrice:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocUnitPrice:number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  */  
   OurOrderQty:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocExtPrice:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   Discount:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   TotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   DocTotalMiscChrg:number,
      /**  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  */  
   ProdCode:string,
      /**  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  */  
   OurShipQty:number,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  The packing slip line number that is being invoiced.  */  
   PackLine:number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   OrderNum:number,
      /**  The associated sales order line number.  */  
   OrderLine:number,
      /**  Contains the release number of the order line item that is being invoiced.  */  
   OrderRelNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   ShipToNum:string,
      /**  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  */  
   ShipDate:string,
      /**  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  */  
   ShipViaCode:string,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   AdvanceBillCredit:number,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   DocAdvanceBillCredit:number,
      /**  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  */  
   CustNum:number,
      /**  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  */  
   InvoiceComment:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   ShpConNum:number,
      /**  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlBurUnitCost:number,
      /**  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  */  
   COSPostingReqd:boolean,
      /**   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   COSPosted:boolean,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   CallNum:number,
      /**  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  */  
   CallCode:string,
      /**   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  */  
   RMALine:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  */  
   JournalCode:string,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  */  
   SellingOrderQty:number,
      /**  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  */  
   SellingShipQty:number,
      /**  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Project Id that links the invoice detail  to the Project table.  */  
   ProjectID:string,
      /**  Milestone id that links the invoice detail  to the ProjectMilestone.  */  
   MilestoneID:string,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  */  
   ListPrice:number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  */  
   OrdBasedPrice:number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  */  
   DocOrdBasedPrice:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   AdvGainLoss:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Sales representative commission rate.  */  
   RepRate1:number,
      /**  Sales representative commission rate.  */  
   RepRate2:number,
      /**  Sales representative commission rate.  */  
   RepRate3:number,
      /**  Sales representative commission rate.  */  
   RepRate4:number,
      /**  Sales representative commission rate.  */  
   RepRate5:number,
      /**  Sales representative commission percentage.  */  
   RepSplit1:number,
      /**  Sales representative commission percentage.  */  
   RepSplit2:number,
      /**  Sales representative commission percentage.  */  
   RepSplit3:number,
      /**  Sales representative commission percentage.  */  
   RepSplit4:number,
      /**  Sales representative commission percentage.  */  
   RepSplit5:number,
      /**  Bill To Customer Number used for consolidated invoices  */  
   BTCustNum:number,
      /**  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCMtlUnitCost:number,
      /**  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCLbrUnitCost:number,
      /**  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCBurUnitCost:number,
      /**  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCSubUnitCost:number,
      /**  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCMtlBurUnitCost:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  */  
   RevChargeMethod:string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   OverrideReverseCharge:boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   RevChargeApplied:boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPrice:number,
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
      /**  Reporting currency value of this field  */  
   Rpt1TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3AdvGainLoss:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping adress country Number.  */  
   OTSCountryNum:number,
      /**  Value is copied from PartTran for PE  */  
   Plant:string,
      /**  value is copied from PartTran for PE  */  
   WarehouseCode:string,
      /**  value is copied from PartTran for PE  */  
   CallLine:number,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  FK to the Finance Charges table  */  
   FinChargeCode:string,
      /**  Reference to the ABT, it is GUID, used in PostingEngine  */  
   ABTUID:string,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   InUnitPrice:number,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocInUnitPrice:number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   InExtPrice:number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocInExtPrice:number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   InDiscount:number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocInDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   InTotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   DocInTotalMiscChrg:number,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  */  
   InListPrice:number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  */  
   DocInListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  */  
   InOrdBasedPrice:number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  */  
   DocInOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt2InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt3InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InUnitPrice:number,
      /**  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  */  
   CorrectionDtl:boolean,
      /**  Asset number of the linked Asset Disposal transaction.  */  
   AssetNum:string,
      /**  Unique number to identify the linked Asset Disposal transaction.  */  
   DisposalNum:number,
      /**   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  */  
   PBLineType:string,
      /**  Invoice line reference  */  
   InvoiceLineRef:number,
      /**  Invoice Number Reference  */  
   InvoiceRef:number,
      /**  Lot Number.  This field should be set according to the linked Shipment Line.  */  
   LotNum:string,
      /**  Reference to the draft invoice line created in Invoice Preparation  */  
   PBInvoiceLine:number,
      /**  Contains the value of the AC_RAHead.RAID client accommodation.  */  
   RAID:number,
      /**  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  */  
   RADtlID:number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  */  
   ChargeDefRev:boolean,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   EnableRMAUpdate:boolean,
   EnableRMADelete:boolean,
      /**  Group associated to the invoice  */  
   GroupID:string,
      /**  ExtPrice-disc+misc charges.  */  
   LineTotal:number,
      /**  ExtPrice-disc+misc charges.  */  
   DocLineTotal:number,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
      /**  Line tax amount  */  
   LineTax:number,
      /**  Doc line tax  */  
   DocLineTax:number,
      /**  Tax buton sensitive or not.  */  
   IsTaxBtnSensitive:boolean,
      /**  Is commission button sensitive  */  
   IsCommisBtnSensitive:boolean,
      /**  PO number for display.  */  
   DispPONum:string,
      /**  original tax category  */  
   OrigTaxCat:string,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  1st sales rep of the invoice.  */  
   SalesRepCode1:string,
      /**  2nd sales rep of the invoice header.  */  
   SalesRepCode2:string,
      /**  3rd sales rep code of the invoice header.  */  
   SalesRepCode3:string,
      /**  4th sales rep code of the invoice header.  */  
   SalesRepCode4:string,
      /**  5th salesrep code of the invoice header.  */  
   SalesRepCode5:string,
      /**  Ship to display address  */  
   DispShipToAddr:string,
      /**  Set to true if intrastat is enabled.  */  
   IsIntrastatSensitive:boolean,
      /**  1st sales rep name  */  
   SalesRepName1:string,
      /**  2nd sales rep name  */  
   SalesRepName2:string,
      /**  3rd sales rep name  */  
   SalesRepName3:string,
      /**  4th sales rep name  */  
   SalesRepName4:string,
      /**  5th sales rep name  */  
   SalesRepName5:string,
      /**  Invoice header type  */  
   InvoiceType:string,
      /**  OrderUM display  */  
   OrderUM:string,
      /**  Document display symbol.  */  
   DocDisplaySymbol:string,
      /**  display discount  */  
   LessDiscount:number,
      /**  Document discount amount  */  
   DocLessDiscount:number,
      /**  Display selling ship qty  */  
   DspSellingShipQty:number,
      /**  Display ext price  */  
   DspExtPrice:number,
      /**  Display document ext price  */  
   DspDocExtPrice:number,
      /**  Display discount  */  
   DspDiscount:number,
      /**  Display document discount  */  
   DspDocDiscount:number,
      /**  Display total misc. charges  */  
   DspTotalMiscChrg:number,
      /**  Display document total misc. charge  */  
   DspDocTotalMiscChrg:number,
      /**  Display our ship qty  */  
   DspOurShipQty:number,
      /**  Display less discount  */  
   DspLessDiscount:number,
      /**  Display document less discount  */  
   DspDocLessDiscount:number,
      /**  Display advance bill credit  */  
   DspAdvanceBillCredit:number,
      /**  Display documents advance bill credit  */  
   DspDocAdvanceBillCredit:number,
      /**  Display line tax  */  
   DspLineTax:number,
      /**  Display document line tax  */  
   DspDocLineTax:number,
      /**  Display line total  */  
   DspLineTotal:number,
      /**  Display document line total  */  
   DspDocLineTotal:number,
      /**  Adv bill enabled flag  */  
   AdvBillEnabled:boolean,
   DspTaxExempt:string,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  Invoice Header Legal Number  */  
   InvLegalNum:string,
      /**  Invoice Detail Customer Name  */  
   CustomerName:string,
      /**  Ship Head Legal Number  */  
   ShpLegalNum:string,
      /**  Invoice Date from InvcHead.  */  
   InvoiceDate:string,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   SoldToCustID:string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   SoldToCustName:string,
      /**  CustID associated with the InvcDtl.BTCustNum field.  */  
   BillToCustID:string,
      /**  Customer Name associated with the InvcDtl.BTCustNum field.  */  
   BTCustName:string,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   CustID:string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   CustName:string,
      /**  Invoice head due date.  */  
   DueDate:string,
      /**  Terms code from InvcHead.  */  
   TermsCode:string,
      /**  Open invoice flag from InvcHead.  */  
   OpenInvoice:boolean,
      /**  Posted flag from the InvcHead.  */  
   Posted:boolean,
      /**  Currency code from InvcHead.  */  
   CurrencyCode:string,
   AllowTaxCodeUpd:boolean,
   ShipToContactEMailAddress:string,
   ShipToContactFaxNum:string,
   ShipToContactName:string,
   ShipToContactPhoneNum:string,
   Rpt1DspAdvanceBillCredit:number,
   Rpt2DspAdvanceBillCredit:number,
   Rpt3DspAdvanceBillCredit:number,
   Rpt1DspDiscount:number,
   Rpt2DspDiscount:number,
   Rpt3DspDiscount:number,
   Rpt1DspExtPrice:number,
   Rpt2DspExtPrice:number,
   Rpt3DspExtPrice:number,
   Rpt1DspLessDiscount:number,
   Rpt2DspLessDiscount:number,
   Rpt3DspLessDiscount:number,
   Rpt1DspLineTax:number,
   Rpt2DspLineTax:number,
   Rpt3DspLineTax:number,
   Rpt1DspLineTotal:number,
   Rpt2DspLineTotal:number,
   Rpt3DspLineTotal:number,
   Rpt1DspTotalMiscChrg:number,
   Rpt2DspTotalMiscChrg:number,
   Rpt3DspTotalMiscChrg:number,
   Rpt1LineTax:number,
   Rpt2LineTax:number,
   Rpt3LineTax:number,
   Rpt1LineTotal:number,
   Rpt2LineTotal:number,
   Rpt3LineTotal:number,
      /**  Drop Shipment  */  
   DropShipment:boolean,
   DspUnitPrice:number,
   DocDspUnitPrice:number,
   Rpt1DspUnitPrice:number,
   Rpt2DspUnitPrice:number,
   Rpt3DspUnitPrice:number,
   InPrice:boolean,
      /**  Display Invoice Reference  */  
   DspInvoiceRef:number,
   DispGLAcct:string,
      /**  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  */  
   RASchedExists:boolean,
      /**  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  */  
   DeleteRASchedule:boolean,
   RADesc:string,
   ContractSuspended:boolean,
      /**  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  */  
   CheckAmortAmounts:boolean,
      /**  Description of the Call Type Code.  */  
   CallCodeCallDescription:string,
      /**  Description of the service contract.  */  
   ContractCodeContractDescription:string,
      /**  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  */  
   ContractNumSuspended:boolean,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   CustCntPhoneNum:string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   CustCntFaxNum:string,
      /**  Contact's middle name.  */  
   CustCntMiddleName:string,
      /**  Contact's first name.  */  
   CustCntFirstName:string,
      /**  Full name of the contact.  */  
   CustCntName:string,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   CustCntCorpName:string,
      /**  Contact's last name.  */  
   CustCntLastName:string,
      /**  The member's name on the credit card.  */  
   InvoiceNumCardMemberName:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   InvoiceNumTermsCode:string,
      /**  Journal  Description.  */  
   JournalCodeJrnlDescription:string,
      /**  Description  */  
   MilestoneIDDescription:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   OrderLineLineDesc:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  Country name  */  
   OTSCntryDescription:string,
      /**  Line description.  */  
   PackLineLineDesc:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  */  
   PackNumName:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
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
      /**  Full description of Product Group.  */  
   ProdCodeDescription:string,
      /**  Full description of Project Management Code.  */  
   ProjectIDDescription:string,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   RMALineLineDesc:string,
      /**  Description of the sales category.  */  
   SalesCatIDDescription:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   ShipToCustCustID:string,
      /**  The full name of the customer.  */  
   ShipToCustName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   ShipToCustBTName:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  Full description for the Sales Tax category.  */  
   TaxCatIDDescription:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcDtlListTableset{
   InvcDtlList:Erp_Tablesets_InvcDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InvcDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  */  
   LineType:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  */  
   XRevisionNum:string,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   PartNum:string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   LineDesc:string,
      /**  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  */  
   IUM:string,
      /**  Our Current Revision Number for this Part.  */  
   RevisionNum:string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   POLine:string,
      /**  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  */  
   TaxExempt:string,
      /**  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  */  
   TaxCatID:string,
      /**   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  */  
   Commissionable:boolean,
      /**   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  */  
   DiscountPercent:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   UnitPrice:number,
      /**  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocUnitPrice:number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  */  
   OurOrderQty:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocExtPrice:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   Discount:number,
      /**   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   TotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   DocTotalMiscChrg:number,
      /**  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  */  
   ProdCode:string,
      /**  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  */  
   OurShipQty:number,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  The packing slip line number that is being invoiced.  */  
   PackLine:number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   OrderNum:number,
      /**  The associated sales order line number.  */  
   OrderLine:number,
      /**  Contains the release number of the order line item that is being invoiced.  */  
   OrderRelNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   ShipToNum:string,
      /**  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  */  
   ShipDate:string,
      /**  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  */  
   ShipViaCode:string,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   AdvanceBillCredit:number,
      /**  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  */  
   DocAdvanceBillCredit:number,
      /**  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  */  
   CustNum:number,
      /**  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  */  
   InvoiceComment:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   ShpConNum:number,
      /**  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  */  
   MtlBurUnitCost:number,
      /**  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  */  
   COSPostingReqd:boolean,
      /**   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   COSPosted:boolean,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   CallNum:number,
      /**  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  */  
   CallCode:string,
      /**   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  */  
   RMALine:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  */  
   JournalCode:string,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  */  
   SellingOrderQty:number,
      /**  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  */  
   SellingShipQty:number,
      /**  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Project Id that links the invoice detail  to the Project table.  */  
   ProjectID:string,
      /**  Milestone id that links the invoice detail  to the ProjectMilestone.  */  
   MilestoneID:string,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  */  
   ListPrice:number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  */  
   OrdBasedPrice:number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  */  
   DocOrdBasedPrice:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   AdvGainLoss:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Sales representative commission rate.  */  
   RepRate1:number,
      /**  Sales representative commission rate.  */  
   RepRate2:number,
      /**  Sales representative commission rate.  */  
   RepRate3:number,
      /**  Sales representative commission rate.  */  
   RepRate4:number,
      /**  Sales representative commission rate.  */  
   RepRate5:number,
      /**  Sales representative commission percentage.  */  
   RepSplit1:number,
      /**  Sales representative commission percentage.  */  
   RepSplit2:number,
      /**  Sales representative commission percentage.  */  
   RepSplit3:number,
      /**  Sales representative commission percentage.  */  
   RepSplit4:number,
      /**  Sales representative commission percentage.  */  
   RepSplit5:number,
      /**  Bill To Customer Number used for consolidated invoices  */  
   BTCustNum:number,
      /**  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCMtlUnitCost:number,
      /**  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCLbrUnitCost:number,
      /**  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCBurUnitCost:number,
      /**  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCSubUnitCost:number,
      /**  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  */  
   JCMtlBurUnitCost:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  */  
   RevChargeMethod:string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   OverrideReverseCharge:boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   RevChargeApplied:boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3AdvanceBillCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPrice:number,
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
      /**  Reporting currency value of this field  */  
   Rpt1TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3AdvGainLoss:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping adress country Number.  */  
   OTSCountryNum:number,
      /**  Value is copied from PartTran for PE  */  
   Plant:string,
      /**  value is copied from PartTran for PE  */  
   WarehouseCode:string,
      /**  value is copied from PartTran for PE  */  
   CallLine:number,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  FK to the Finance Charges table  */  
   FinChargeCode:string,
      /**  Reference to the ABT, it is GUID, used in PostingEngine  */  
   ABTUID:string,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   InUnitPrice:number,
      /**  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  */  
   DocInUnitPrice:number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   InExtPrice:number,
      /**  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  */  
   DocInExtPrice:number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   InDiscount:number,
      /**   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  */  
   DocInDiscount:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   InTotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  */  
   DocInTotalMiscChrg:number,
      /**  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  */  
   InListPrice:number,
      /**  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  */  
   DocInListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  */  
   InOrdBasedPrice:number,
      /**  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  */  
   DocInOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt2InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt3InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InListPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InOrdBasedPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InUnitPrice:number,
      /**  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  */  
   CorrectionDtl:boolean,
      /**  Asset number of the linked Asset Disposal transaction.  */  
   AssetNum:string,
      /**  Unique number to identify the linked Asset Disposal transaction.  */  
   DisposalNum:number,
      /**   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  */  
   PBLineType:string,
      /**  Invoice line reference  */  
   InvoiceLineRef:number,
      /**  Invoice Number Reference  */  
   InvoiceRef:number,
      /**  Lot Number.  This field should be set according to the linked Shipment Line.  */  
   LotNum:string,
      /**  Reference to the draft invoice line created in Invoice Preparation  */  
   PBInvoiceLine:number,
      /**  Contains the value of the AC_RAHead.RAID client accommodation.  */  
   RAID:number,
      /**  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  */  
   RADtlID:number,
      /**  Indicates if revenue is deferred for contracts assigned to this group.  */  
   DeferredRev:boolean,
      /**  Revenue Amortization Code.  */  
   RACode:string,
      /**  Starting date the revenue is deferred.  */  
   DefRevStart:string,
      /**  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  */  
   ChargeDefRev:boolean,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  DefRevPosted  */  
   DefRevPosted:boolean,
      /**  Unit price of Invoice linked to Bill of Exchange in original currency.  */  
   LinkedInvcUnitPrice:number,
      /**  Withholding Tax Amount in reporting currency  */  
   DspWithholdAmt:number,
      /**  Withholding Tax Amount in document currency  */  
   DocDspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt1DspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt2DspWithholdAmt:number,
      /**  Withholding tax amount in reporting currency  */  
   Rpt3DspWithholdAmt:number,
      /**  Currency code from linked Invoice Header  */  
   LinkedCurrencyCode:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  PEBOEHeadNum  */  
   PEBOEHeadNum:number,
      /**  MXSellingShipQty  */  
   MXSellingShipQty:number,
      /**  MXUnitPrice  */  
   MXUnitPrice:number,
      /**  DocMXUnitPrice  */  
   DocMXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1MXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2MXUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3MXUnitPrice:number,
      /**  CustCostCenter  */  
   CustCostCenter:string,
      /**  DEIsServices  */  
   DEIsServices:boolean,
      /**  DEIsSecurityFinancialDerivative  */  
   DEIsSecurityFinancialDerivative:boolean,
      /**  DEInternationalSecuritiesID  */  
   DEInternationalSecuritiesID:string,
      /**  DEIsInvestment  */  
   DEIsInvestment:boolean,
      /**  DEPayStatCode  */  
   DEPayStatCode:string,
      /**  DefRevEndDate  */  
   DefRevEndDate:string,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  Indicates tha this invoice Line was reclassified.  */  
   Reclassified:boolean,
      /**  Enables the user the ability to override the Percent or Amount of revenue to be deferred  */  
   PartiallyDefer:boolean,
      /**  Percentage of revenue to be deferred for this line item  */  
   DeferredPercent:number,
      /**  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  */  
   Reclass:boolean,
      /**  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  */  
   DeferredOnly:boolean,
      /**  Reclassification Code. This field will be required if Reclass is checked.  */  
   ReclassCodeID:string,
      /**  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  */  
   ReclassReasonCode:string,
      /**  Internal comments for reclassification entered by the user.  */  
   ReclassComments:string,
      /**  Deferred Revenue Amount in base currency  */  
   DeferredRevAmt:number,
      /**  Deferred Revenue Amount in document currency  */  
   DocDeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt1DeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt2DeferredRevAmt:number,
      /**  Reporting currency value of Deferred Revenue Amount  */  
   Rpt3DeferredRevAmt:number,
      /**  ChargeReclass  */  
   ChargeReclass:boolean,
      /**  DEDenomination  */  
   DEDenomination:string,
      /**  DropShipPONum  */  
   DropShipPONum:number,
      /**  DocInAdvanceBillCredit  */  
   DocInAdvanceBillCredit:number,
      /**  InAdvanceBillCredit  */  
   InAdvanceBillCredit:number,
      /**  Rpt1InAdvanceBillCredit  */  
   Rpt1InAdvanceBillCredit:number,
      /**  Rpt2InAdvanceBillCredit  */  
   Rpt2InAdvanceBillCredit:number,
      /**  Rpt3InAdvanceBillCredit  */  
   Rpt3InAdvanceBillCredit:number,
      /**  MYIndustryCode  */  
   MYIndustryCode:string,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  ConsolidateLines  */  
   ConsolidateLines:boolean,
      /**  MXCustomsDuty  */  
   MXCustomsDuty:string,
      /**  CommodityCode  */  
   CommodityCode:string,
      /**  MXProdServCode  */  
   MXProdServCode:string,
      /**  Quote number to which this line item detail record is associated with.  */  
   QuoteNum:number,
      /**  Quote Line number from which this invoice line was created from.  */  
   QuoteLine:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  MXCustomsUMFrom  */  
   MXCustomsUMFrom:string,
      /**  PE Detraction good or service code  */  
   PEDetrGoodServiceCode:string,
      /**  PETaxExempt  */  
   PETaxExempt:string,
      /**  Order number on the Invoicing Company.  */  
   CColOrderNum:number,
      /**  Order number line the Invoicing Company.  */  
   CColOrderLine:number,
      /**  Order number release the Invoicing Company.  */  
   CColOrderRel:number,
      /**  Invoice Line reference on the Invoicing Company.  */  
   CColInvoiceLineRef:number,
      /**  Packing slip number on the Invoicing Company.  */  
   CColPackNum:number,
      /**  Packing slip line number on the Invoicing Company.  */  
   CColPackLine:number,
      /**  Drop shipment packing slip number on the Invoicing Company.  */  
   CColDropShipPackSlip:string,
      /**  Drop shipment packing slip line number on the Invoicing Company.  */  
   CColDropShipPackSlipLine:number,
      /**  Ship To Customer ID from the Invoice Line in the subsidiary company.  */  
   CColShipToCustID:string,
      /**  Ship To from the Invoice Line in the subsidiary company.  */  
   CColShipToNum:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Exempt Reason Code  */  
   ExemptReasonCode:string,
      /**  Associates the Call Line record back its linked jobnum  */  
   JobNum:string,
      /**  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  */  
   ServiceSource:string,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  */  
   AssemblySeq:number,
      /**  Job Mtl seq used to create invoice line from service call job  */  
   MtlSeq:number,
      /**  Job subcontract oper seq used to create invoice line from service call job  */  
   OprSeq:number,
      /**  Indicates the labor type of the LaborDtl used to create invoice from service call job.  */  
   LaborType:string,
      /**  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  */  
   BillableLaborHrs:number,
      /**  Billable rate used to create invoice line from labor related to service call job. In base currency.  */  
   BillableLaborRate:number,
      /**  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  */  
   ServiceSourceType:string,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  Adv bill enabled flag  */  
   AdvBillEnabled:boolean,
   AllowTaxCodeUpd:boolean,
      /**  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  */  
   AllowUpdPartDefer:boolean,
      /**  CustID associated with the InvcDtl.BTCustNum field.  */  
   BillToCustID:string,
      /**  Customer Name associated with the InvcDtl.BTCustNum field.  */  
   BTCustName:string,
      /**  The date and time that the record was last changed  */  
   ChangeDateTime:string,
      /**  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  */  
   CheckAmortAmounts:boolean,
   CNGTIDescription1:string,
   CNGTIDescription2:string,
   CNGTIDescription3:string,
      /**  CSF China, discount tax amount  */  
   CNGTIDiscountTaxAmount:number,
   CNGTIIUM:string,
   CNGTINetAmount:number,
   CNGTIPartDescription:string,
   CNGTISpecification:string,
   CNGTITaxAmount:number,
   CNGTITaxCode:string,
   CNGTITaxPercent:number,
   CNGTITotalAmount:number,
      /**  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  */  
   CNGTIUnitPrice:number,
   ContractSuspended:boolean,
      /**  Currency code from InvcHead.  */  
   CurrencyCode:string,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   CustID:string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   CustName:string,
      /**  Invoice Detail Customer Name  */  
   CustomerName:string,
      /**  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  */  
   DeleteRASchedule:boolean,
   DispGLAcct:string,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  PO number for display.  */  
   DispPONum:string,
      /**  Ship to display address  */  
   DispShipToAddr:string,
      /**  Document display symbol.  */  
   DocDisplaySymbol:string,
   DocDspUnitPrice:number,
      /**  Document discount amount  */  
   DocLessDiscount:number,
      /**  Doc line tax  */  
   DocLineTax:number,
      /**  ExtPrice-disc+misc charges.  */  
   DocLineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   DocPEDetAmt:number,
      /**  Drop Shipment  */  
   DropShipment:boolean,
      /**  Display advance bill credit  */  
   DspAdvanceBillCredit:number,
      /**  Display discount  */  
   DspDiscount:number,
      /**  Display documents advance bill credit  */  
   DspDocAdvanceBillCredit:number,
      /**  Display document discount  */  
   DspDocDiscount:number,
      /**  Display document ext price  */  
   DspDocExtPrice:number,
      /**  Display document less discount  */  
   DspDocLessDiscount:number,
      /**  Display document line tax  */  
   DspDocLineTax:number,
      /**  Display document line total  */  
   DspDocLineTotal:number,
      /**  Display document total misc. charge  */  
   DspDocTotalMiscChrg:number,
      /**  Display ext price  */  
   DspExtPrice:number,
      /**  Display Invoice Reference  */  
   DspInvoiceRef:number,
      /**  Display less discount  */  
   DspLessDiscount:number,
      /**  Display line tax  */  
   DspLineTax:number,
      /**  Display line total  */  
   DspLineTotal:number,
      /**  Display our ship qty  */  
   DspOurShipQty:number,
      /**  Display selling ship qty  */  
   DspSellingShipQty:number,
   DspTaxExempt:string,
      /**  Display total misc. charges  */  
   DspTotalMiscChrg:number,
   DspUnitPrice:number,
      /**  Invoice head due date.  */  
   DueDate:string,
      /**  FSA Technician  */  
   EmpID:string,
   EnableDspWithholdAmt:boolean,
   EnableRMADelete:boolean,
   EnableRMAUpdate:boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   FSACallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   FSAContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   FSAContractNum:number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   FSAEmpID:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   FSAWarrantyCode:string,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  Group associated to the invoice  */  
   GroupID:string,
   InPrice:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Invoice Header Legal Number  */  
   InvLegalNum:string,
      /**  Invoice Date from InvcHead.  */  
   InvoiceDate:string,
      /**  Invoice header type  */  
   InvoiceType:string,
      /**  Is commission button sensitive  */  
   IsCommisBtnSensitive:boolean,
      /**  Set to true if intrastat is enabled.  */  
   IsIntrastatSensitive:boolean,
      /**  Tax buton sensitive or not.  */  
   IsTaxBtnSensitive:boolean,
      /**  display discount  */  
   LessDiscount:number,
      /**  Line tax amount  */  
   LineTax:number,
      /**  ExtPrice-disc+misc charges.  */  
   LineTotal:number,
   LinkedCurrencySymbol:string,
      /**  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  */  
   NoShipTaxRgnInfo:boolean,
      /**  Open invoice flag from InvcHead.  */  
   OpenInvoice:boolean,
      /**  OrderUM display  */  
   OrderUM:string,
      /**  original tax category  */  
   OrigTaxCat:string,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   PEDetAmt:number,
      /**  PE Detraction good or service code description  */  
   PEDetrGoodServiceCodeDesc:string,
   PEDspCurrencySymbol:string,
      /**  PE VAT Exemption Reason  */  
   PEVATExemptionReason:string,
      /**  Posted flag from the InvcHead.  */  
   Posted:boolean,
   RADesc:string,
      /**  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  */  
   RASchedExists:boolean,
      /**  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  */  
   RemoveManAdTax:boolean,
   Rpt1DspAdvanceBillCredit:number,
   Rpt1DspDiscount:number,
   Rpt1DspExtPrice:number,
   Rpt1DspLessDiscount:number,
   Rpt1DspLineTax:number,
   Rpt1DspLineTotal:number,
   Rpt1DspTotalMiscChrg:number,
   Rpt1DspUnitPrice:number,
   Rpt1LineTax:number,
   Rpt1LineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt1PEDetAmt:number,
   Rpt2DspAdvanceBillCredit:number,
   Rpt2DspDiscount:number,
   Rpt2DspExtPrice:number,
   Rpt2DspLessDiscount:number,
   Rpt2DspLineTax:number,
   Rpt2DspLineTotal:number,
   Rpt2DspTotalMiscChrg:number,
   Rpt2DspUnitPrice:number,
   Rpt2LineTax:number,
   Rpt2LineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt2PEDetAmt:number,
   Rpt3DspAdvanceBillCredit:number,
   Rpt3DspDiscount:number,
   Rpt3DspExtPrice:number,
   Rpt3DspLessDiscount:number,
   Rpt3DspLineTax:number,
   Rpt3DspLineTotal:number,
   Rpt3DspTotalMiscChrg:number,
   Rpt3DspUnitPrice:number,
   Rpt3LineTax:number,
   Rpt3LineTotal:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt3PEDetAmt:number,
      /**  1st sales rep of the invoice.  */  
   SalesRepCode1:string,
      /**  2nd sales rep of the invoice header.  */  
   SalesRepCode2:string,
      /**  3rd sales rep code of the invoice header.  */  
   SalesRepCode3:string,
      /**  4th sales rep code of the invoice header.  */  
   SalesRepCode4:string,
      /**  5th salesrep code of the invoice header.  */  
   SalesRepCode5:string,
      /**  1st sales rep name  */  
   SalesRepName1:string,
      /**  2nd sales rep name  */  
   SalesRepName2:string,
      /**  3rd sales rep name  */  
   SalesRepName3:string,
      /**  4th sales rep name  */  
   SalesRepName4:string,
      /**  5th sales rep name  */  
   SalesRepName5:string,
   ShipToContactEMailAddress:string,
   ShipToContactFaxNum:string,
   ShipToContactName:string,
   ShipToContactPhoneNum:string,
      /**  Ship Head Legal Number  */  
   ShpLegalNum:string,
      /**  CustID associated with the InvcDtl.CustNum field.  */  
   SoldToCustID:string,
      /**  Customer Name associated with the InvcDtl.CustNum field.  */  
   SoldToCustName:string,
      /**  Terms code from InvcHead.  */  
   TermsCode:string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   WarrantyCode:string,
      /**  This flag allow updating Reclassification data.  */  
   AllowReclassify:boolean,
      /**  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  */  
   LineAmtRecalcd:boolean,
      /**  Set to true if extra trade statistics is enabled.  */  
   IsExtrastatSensitive:boolean,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   TrackInventoryByRevision:boolean,
   BitFlag:number,
   CallCodeCallDescription:string,
   CommodityCodeDescription:string,
   ContractCodeContractDescription:string,
   ContractNumSuspended:boolean,
   CustCntName:string,
   CustCntMiddleName:string,
   CustCntFirstName:string,
   CustCntFaxNum:string,
   CustCntCorpName:string,
   CustCntPhoneNum:string,
   CustCntLastName:string,
   CustNumCustID:string,
   CustNumName:string,
   CustNumAllowShipTo3:boolean,
   CustNumBTName:string,
   InvoiceNumTermsCode:string,
   InvoiceNumCardMemberName:string,
   JournalCodeJrnlDescription:string,
   MilestoneIDDescription:string,
   MXProdServCodeDesc:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   OTSCntryEUMember:boolean,
   OTSCntryISOCode:string,
   OTSCntryDescription:string,
   PackLineLineDesc:string,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumAttrClassID:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackInventoryByRevision:boolean,
   ProdCodeDescription:string,
   ProjectIDDescription:string,
   ReclassCodeDescription:string,
   ReclassReasonDescription:string,
   RMALineLineDesc:string,
   SalesCatIDDescription:string,
   ShipToCustCustID:string,
   ShipToCustName:string,
   ShipToCustBTName:string,
   ShipToNumInactive:boolean,
   ShipToNumName:string,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   TaxCatIDDescription:string,
   TaxRegionDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtARInvcDtlSearchTableset{
   InvcDtl:Erp_Tablesets_InvcDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param invoiceNum
      @param invoiceLine
   */  
export interface GetByID_input{
   invoiceNum:number,
   invoiceLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ARInvcDtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ARInvcDtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ARInvcDtlSearchTableset[],
}

   /** Required : 
      @param invcHeadWhereClause
      @param invcDtlWhereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListAlternalSearch_input{
      /**  Whereclause for invcHead table.  */  
   invcHeadWhereClause:string,
      /**  Whereclause for InvcDtl table.  */  
   invcDtlWhereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListAlternalSearch_output{
   returnObj:Erp_Tablesets_ARInvcDtlSearchTableset[],
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
   returnObj:Erp_Tablesets_InvcDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param invoiceNum
   */  
export interface GetNewInvcDtl_input{
   ds:Erp_Tablesets_ARInvcDtlSearchTableset[],
   invoiceNum:number,
}

export interface GetNewInvcDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcDtlSearchTableset[],
}
}

   /** Required : 
      @param whereClauseInvcDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseInvcDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ARInvcDtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtARInvcDtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtARInvcDtlSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ARInvcDtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvcDtlSearchTableset[],
}
}

