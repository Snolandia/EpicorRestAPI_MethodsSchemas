import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ARInvSearchSvc
// Description: bo/APInvSearch
           AP Invoice Search object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/$metadata", {
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
   Description: Get ARInvSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARInvSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcHeadRow
   */  
export function get_ARInvSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/ARInvSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARInvSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InvcHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARInvSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/ARInvSearches", {
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
   Summary: Calls GetByID to retrieve the ARInvSearch item
   Description: Calls GetByID to retrieve the ARInvSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARInvSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcHeadRow
   */  
export function get_ARInvSearches_Company_InvoiceNum(Company:string, InvoiceNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InvcHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/ARInvSearches(" + Company + "," + InvoiceNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InvcHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARInvSearch for the service
   Description: Calls UpdateExt to update ARInvSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARInvSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARInvSearches_Company_InvoiceNum(Company:string, InvoiceNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/ARInvSearches(" + Company + "," + InvoiceNum + ")", {
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
   Summary: Call UpdateExt to delete ARInvSearch item
   Description: Call UpdateExt to delete ARInvSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARInvSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARInvSearches_Company_InvoiceNum(Company:string, InvoiceNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/ARInvSearches(" + Company + "," + InvoiceNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadListRow)
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
export function get_GetRows(whereClauseInvcHead:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseInvcHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInvcHead=" + whereClauseInvcHead
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(invoiceNum:string, epicorHeaders?:Headers){
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetARInvoiceRelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for AR Invoice
   OperationID: GetARInvoiceRelationshipMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARInvoiceRelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARInvoiceRelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetARInvoiceRelationshipMap(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetARInvoiceRelationshipMap", {
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
   Summary: Invoke method GetListARTaxConfirmSearch
   Description: Returns InvcHead records which have Taxes waiting for Confirmation.
   OperationID: GetListARTaxConfirmSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListARTaxConfirmSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListARTaxConfirmSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListARTaxConfirmSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetListARTaxConfirmSearch", {
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
   Summary: Invoke method GetRefInvoicesForBOE
   Description: This procedure returns the invoices for BOE selection
   OperationID: GetRefInvoicesForBOE
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRefInvoicesForBOE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRefInvoicesForBOE_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRefInvoicesForBOE(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetRefInvoicesForBOE", {
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
   Summary: Invoke method GetInvoicesByOrder
   Description: This procedure returns InvcHead records for a given sales order.
   OperationID: GetInvoicesByOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvoicesByOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoicesByOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvoicesByOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetInvoicesByOrder", {
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
   Summary: Invoke method GetListBOEReferences
   OperationID: GetListBOEReferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListBOEReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListBOEReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListBOEReferences(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetListBOEReferences", {
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
   Summary: Invoke method GetListForAGCAEA
   Description: Returns List Dataset filtered by caea. Used in AGCAEAInvoiceTracker.
   OperationID: GetListForAGCAEA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForAGCAEA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForAGCAEA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForAGCAEA(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetListForAGCAEA", {
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
   Summary: Invoke method GetRowsForCashReceipt
   Description: Invokes GetRows filtering on Invoices for the specified Cash Receipt
   OperationID: GetRowsForCashReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForCashReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForCashReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForCashReceipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetRowsForCashReceipt", {
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
   Summary: Invoke method GetRowsForQuote
   Description: Invokes GetRows filtering on Invoices for the specified Quote
   OperationID: GetRowsForQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForQuote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetRowsForQuote", {
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
   Summary: Invoke method GetNewInvcHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInvcHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInvcHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetNewInvcHead", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcHeadRow[],
}

export interface Erp_Tablesets_InvcHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if invoice is "open".  */  
   "OpenInvoice":boolean,
      /**  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  */  
   "ClosedDate":string,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   "CreditMemo":boolean,
      /**  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  */  
   "UnappliedCash":boolean,
      /**   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   "CheckRef":string,
      /**  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  */  
   "InvoiceSuffix":string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  */  
   "GroupID":string,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   "Posted":boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "InvoiceNum":number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   "InvoiceType":string,
      /**  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  */  
   "DeferredRevenue":boolean,
      /**  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  */  
   "OrderNum":number,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   "CustNum":number,
      /**  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  */  
   "PONum":string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   "EntryPerson":string,
      /**  Defaults from sales order ORderHed.FOB  */  
   "FOB":string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "TermsCode":string,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   "InvoiceDate":string,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   "DueDate":string,
      /**  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  */  
   "FiscalYear":number,
      /**  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  */  
   "FiscalPeriod":number,
      /**  Once posted, maintenance is not allowed.  */  
   "GLPosted":boolean,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   "InvoiceAmt":number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   "DocInvoiceAmt":number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   "InvoiceBal":number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   "DocInvoiceBal":number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "UnpostedBal":number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "DocUnpostedBal":number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   "DepositCredit":number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   "DocDepositCredit":number,
      /**  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  */  
   "SalesRepList":string,
      /**   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   "InvoiceRef":number,
      /**  Value of this field is reference to invoice which has been cancelled by current invoice.  */  
   "RefCancelled":number,
      /**  Value of this field is reference to invoice that cancelled this invoice.  */  
   "RefCancelledBy":number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   "StartUp":boolean,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   "PayDates":string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   "PayAmounts":string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   "DocPayAmounts":string,
      /**  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  */  
   "PayDiscDate":string,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   "PayDiscAmt":number,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   "DocPayDiscAmt":number,
      /**  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  */  
   "BillConNum":number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  */  
   "InvoiceHeld":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  Journal that invoice was posted to.  */  
   "JournalCode":string,
      /**  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  */  
   "LineType":string,
      /**   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   "RMANum":number,
      /**  The Site that the invoice is relate to.  */  
   "Plant":string,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   "CardType":string,
      /**  The expiration month of the credit card.  */  
   "ExpirationMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpirationYear":number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   "CardID":string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  External Identifier  */  
   "ExternalID":string,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefInvoiceNum":string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "DepGainLoss":number,
      /**  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  */  
   "DNComments":string,
      /**  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  */  
   "DNCustNbr":string,
      /**   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  */  
   "DebitNote":boolean,
      /**  This is populated from ShipHead.CustNum representing the Sold To customer.  */  
   "SoldToCustNum":number,
      /**  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  */  
   "Consolidated":boolean,
      /**  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  */  
   "BillToInvoiceAddress":boolean,
      /**  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  */  
   "SoldToInvoiceAddress":boolean,
      /**  Stores the encrypted credit card number  */  
   "ProcessCard":string,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   "RepComm1":number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   "RepComm2":number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   "RepComm3":number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   "RepComm4":number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   "RepComm5":number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   "RepRate1":number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   "RepRate2":number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   "RepRate3":number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   "RepRate4":number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   "RepRate5":number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   "RepSales1":number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   "RepSales2":number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   "RepSales3":number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   "RepSales4":number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   "RepSales5":number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   "RepSplit1":number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   "RepSplit2":number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   "RepSplit3":number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   "RepSplit4":number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   "RepSplit5":number,
      /**  Indicates if the Credit Memo is for a Rebate  */  
   "CMType":string,
      /**  Address used during AVS validation for credit transactions  */  
   "CCStreetAddr":string,
      /**  Zip used during AVS validation in credit transactions  */  
   "CCZip":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   "EDIReady":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  Rounding in Customer currency  */  
   "DocRounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DepositCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DepositCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DepositCredit":number,
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
   "Rpt1PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt2PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt3PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt1PayDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2PayDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3PayDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnpostedBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnpostedBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnpostedBal":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Amount of deposit applied  */  
   "DocDepApplied":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt1DepGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt2DepGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt3DepGainLoss":number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   "ApplyDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Tax point  */  
   "TaxPoint":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**  The last date finance/late charges have been calculated for this invoice.  */  
   "LastChrgCalcDate":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Total Finance Charge amount.  */  
   "TotFinChrg":number,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   "PayDiscDays":string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   "PayDiscPer":string,
      /**  Blocks certain invoice from generating finance/later charge.  */  
   "BlockedFinChrg":boolean,
      /**  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  */  
   "BlockedFinChrgReason":string,
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
      /**  Blocks certain invoice from being printed on reminder letters.  */  
   "BlockedRemLetters":boolean,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   "PayDiscPartPay":boolean,
      /**  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  */  
   "BlockedRemLettersReason":string,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   "ShipDate":string,
      /**  Currency Rate Date  */  
   "CurrRateDate":string,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   "PIPayment":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  */  
   "UseAltBillTo":boolean,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  */  
   "CorrectionInv":boolean,
      /**  Tax Rate Group Code  */  
   "TaxRateGrpCode":string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   "LockTaxRate":boolean,
      /**  Sweden Finland Localization field - Banking Reference  */  
   "SEBankRef":string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   "GUITaxTypeCode":string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   "GUIFormatCode":string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   "GUIDeductCode":string,
      /**  Reversal Doucment Amount  */  
   "ReversalDocAmount":number,
      /**  Original Due Date at posting time  */  
   "OrigDueDate":string,
      /**  The reference to CashHead.HeadNum.Used in deposit invoices  */  
   "HeadNum":number,
      /**  Letter of Credit ID.  */  
   "ARLOCID":string,
      /**  The free text field which can contain reference (such as Contract)  */  
   "ContractRef":string,
      /**  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  */  
   "OurBank":string,
      /**  Addition to Contract  */  
   "ContractDate":string,
      /**  If the invoice was generated in Project Billing then it is reference to the project.  */  
   "PBProjectID":string,
      /**  Deposit amount is transaction amount of deposit payment  */  
   "DepositAmt":number,
      /**   Taiwan Localization
Export Bill Number  */  
   "GUIExportBillNumber":string,
      /**  Deposit amount is transaction amount of deposit payment in document currency  */  
   "DocDepositAmt":number,
      /**   Taiwan Localization
Date of Export  */  
   "GUIDateOfExport":string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt1 currency  */  
   "Rpt1DepositAmt":number,
      /**   Taiwan Localization
Export Type  */  
   "GUIExportType":string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt2 currency  */  
   "Rpt2DepositAmt":number,
      /**   Taiwan Localization
Export Mark  */  
   "GUIExportMark":string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt23currency  */  
   "Rpt3DepositAmt":number,
      /**   Taiwan Localization
Export Bill Type  */  
   "GUIExportBillType":string,
      /**  Deposit unallocated amount in base currency  */  
   "DepUnallocatedAmt":number,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   "SummarizationDate":string,
      /**  Deposit unallocated amount in document currency  */  
   "DocDepUnallocatedAmt":number,
      /**  Date when a company bills the customer  */  
   "BillingDate":string,
      /**  Deposit unallocated amount in Rpt1 currency  */  
   "Rpt1DepUnallocatedAmt":number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   "BillingNumber":string,
      /**  Deposit unallocated amount in Rpt2 currency  */  
   "Rpt2DepUnallocatedAmt":number,
      /**  Only records ready to bill will be printed in the Billing Statement  */  
   "ReadyToBill":boolean,
      /**  Deposit unallocated amount in Rpt3 currency  */  
   "Rpt3DepUnallocatedAmt":number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   "OvrDefTaxDate":boolean,
      /**  Cross Reference Contract Number.  */  
   "XRefContractNum":string,
      /**  Cross Reference Contract Date.  */  
   "XRefContractDate":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Customer Agent Name  */  
   "CustAgentName":string,
      /**  Customer Agent Tax Region Number  */  
   "CustAgentTaxRegNo":string,
      /**  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  */  
   "ExportType":string,
      /**  Export Report Number  */  
   "ExportReportNo":string,
      /**  Real Estate Number  */  
   "RealEstateNo":string,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RevisionDate  */  
   "RevisionDate":string,
      /**  RevisionNum  */  
   "RevisionNum":number,
      /**  TWDeclareYear  */  
   "TWDeclareYear":number,
      /**  TWDeclarePeriod  */  
   "TWDeclarePeriod":number,
      /**  TWGenerationType  */  
   "TWGenerationType":string,
      /**  TWGUIGroup  */  
   "TWGUIGroup":string,
      /**  TWPeriodPrefix  */  
   "TWPeriodPrefix":string,
      /**  Flag that indicates if the Invoice is for Central Collection.  */  
   "CentralCollection":boolean,
      /**  Central Collection Doc Invoice Balance.  */  
   "DocCColInvBal":number,
      /**  Sub total for invoice  */  
   "SubTotal":number,
      /**  Document sub total  */  
   "DocSubTotal":number,
      /**  Total tax amount from InvcTax  */  
   "TaxAmt":number,
      /**  Document Total tax amount from InvcTax for Collection type 'Invoice'  */  
   "DocTaxAmt":number,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   "CurrencySwitch":boolean,
      /**  Currency display symbol  */  
   "DisplaySymbol":string,
      /**  1st entry in SalesRepList  */  
   "SalesRepCode1":string,
      /**  2nd entry in SalesRepList  */  
   "SalesRepCode2":string,
      /**  3rd entry in SalesRepList.  */  
   "SalesRepCode3":string,
      /**  4th entry in SalesRepList  */  
   "SalesRepCode4":string,
      /**  5th entry in SalesRepList  */  
   "SalesRepCode5":string,
      /**  Contact name  */  
   "ContactName":string,
      /**  Contact fax number  */  
   "ContactFaxNum":string,
      /**  Contact phone number  */  
   "ContactPhoneNum":string,
      /**  Bill to address in list format.  */  
   "DisplayBillAddr":string,
      /**  If true, the credit card info will come from the sales order.  */  
   "UseSOCCDefaults":boolean,
      /**  Display field for the masked credit card number  */  
   "DisplayCreditCardNum":string,
      /**  Currency label  */  
   "XRateLabel":string,
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
      /**  Deposit credit enabled flag.  */  
   "DepositCreditEnabled":boolean,
      /**  Pay schedule enabled flag  */  
   "PaySchedEnabled":boolean,
      /**  Contact email address.  */  
   "ContactEmailAddr":string,
      /**  InvoiceType description  */  
   "InvoiceTypeDesc":string,
      /**  Document display symbol  */  
   "DocDisplaySymbol":string,
      /**  Display sub total  */  
   "DspSubTotal":number,
      /**  display document sub total  */  
   "DspDocSubTotal":number,
      /**  Display invoice amount  */  
   "DspInvoiceAmt":number,
      /**  Display document invoice amount  */  
   "DspDocInvoiceAmt":number,
      /**  Pack slip number from the 1st line item.  */  
   "PackSlipNum":number,
      /**  Flag to determine if UseSOCCDefaults should be enabled.  */  
   "EnableSOCCDefaults":boolean,
      /**  Display invoice reference  */  
   "DspInvoiceRef":number,
      /**  Flag for update of InvcHead to allow when group id is "RMACRREQ"  */  
   "GenedFromRMA":boolean,
      /**  Sold to customer id  */  
   "SoldToCustID":string,
      /**  Sold to customer name.  */  
   "SoldToCustomerName":string,
      /**  Sold to address list.  */  
   "SoldToAddressList":string,
      /**  If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   "dspSoldToCustID":string,
      /**  Delimited list of available bill to customers.  */  
   "AvailBTCustList":string,
      /**  Customer ID for the bill to customer (InvcHead.CustNum).  */  
   "BTCustID":string,
      /**  Bill to customer name.  */  
   "BTCustomerName":string,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   "DispBalDN":number,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   "DocDispBalDN":number,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   "DNPmtAmt":number,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   "DocDNPmtAmt":number,
      /**  Display Invoice Balance.  */  
   "DspInvoiceBal":number,
      /**  Display document invoice balance  */  
   "DspDocInvoiceBal":number,
      /**  Display Invoice Doc Rounding  */  
   "DspDocRounding":number,
      /**  Display Rounding in Base  */  
   "DspRounding":number,
   "Rpt1DspInvoiceAmt":number,
   "Rpt2DspInvoiceAmt":number,
   "Rpt3DspInvoiceAmt":number,
   "Rpt1DspInvoiceBal":number,
   "Rpt2DspInvoiceBal":number,
   "Rpt3DspInvoiceBal":number,
   "Rpt1DspRounding":number,
   "Rpt2DspRounding":number,
   "Rpt3DspRounding":number,
   "Rpt1DspSubTotal":number,
   "Rpt2DspSubTotal":number,
   "Rpt3DspSubTotal":number,
   "Rpt1TaxAmt":number,
   "Rpt2Taxamt":number,
   "Rpt3TaxAmt":number,
   "Rpt1SubTotal":number,
   "Rpt2SubTotal":number,
   "Rpt3SubTotal":number,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  Indicates if a legal number configuration exists for ar invoices/credit memos  */  
   "HasLegNumCnfg":boolean,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  */  
   "SystemTranType":string,
      /**  This field is to display in Cash Receipt Entry the Discount Date that the payment will take.  */  
   "NextDiscDate":string,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
   "ReminderSeq":number,
   "CustAllowOTS":boolean,
   "DocDspTaxAmt":number,
   "DspTaxAmt":number,
   "Rpt1DspTaxAmt":number,
   "Rpt2DspTaxAmt":number,
   "Rpt3DspTaxAmt":number,
   "DisplayCurrencyID":string,
      /**  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  */  
   "TransApplyDate":string,
      /**  Accumulate all reversal amounts of Credit Memos with the reference to the invoice  */  
   "ReversalDocAmt":number,
      /**  It will be displayed to identify invoices automatically generated due ERS shipments.  */  
   "ERSInvoice":boolean,
   "TaxExchangeRate":number,
   "UseTaxRate":boolean,
      /**  when InvcHead.PIPayment = O then populate ARPaymentInstrumentID with a value of PI.  */  
   "ARPromNoteID":string,
      /**  Deposit balance from CashHed  */  
   "DepBal":number,
      /**  Document deposit amount from cashhead.  */  
   "DocDepBal":number,
   "Rpt1DepBal":number,
   "Rpt2DepBal":number,
   "Rpt3DepBal":number,
      /**  Display deposit balance.  */  
   "DspDepBal":number,
      /**  Display document deposit balance  */  
   "DspDocDepBal":number,
   "Rpt1DspDepBal":number,
   "Rpt2DspDepBal":number,
   "Rpt3DspDepBal":number,
      /**  Display deposit credit.  */  
   "DspDepCr":number,
      /**  Display document deposit credit.  */  
   "DspDocDepCr":number,
   "Rpt1DspDepCr":number,
   "Rpt2DspDepCr":number,
   "Rpt3DspDepCr":number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in base currency.  */  
   "Vr":number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in document currency.  */  
   "DocVr":number,
   "SATaxAmt":number,
   "DocSATaxAmt":number,
   "Rpt1SATaxAmt":number,
   "Rpt2SATaxAmt":number,
   "Rpt3SATaxAmt":number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt1 currency.  */  
   "Rpt1Vr":number,
   "WHTaxAmt":number,
   "DocWHTaxAmt":number,
   "Rpt1WHTaxAmt":number,
   "Rpt2WHTaxAmt":number,
   "Rpt3WHTaxAmt":number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt2 currency.  */  
   "Rpt2Vr":number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt3 currency.  */  
   "Rpt3Vr":number,
      /**  Display advance billing amount  */  
   "DspABAmt":number,
      /**  Display document advance billing amount  */  
   "DspDocABAmt":number,
   "Rpt1DspABAmt":number,
   "Rpt2DspABAmt":number,
   "Rpt3DspABAmt":number,
      /**  Total advanced billing amount.  */  
   "ABAmt":number,
      /**  Document Total advanced billing amount.  */  
   "DocABAmt":number,
   "Rpt1ABAmt":number,
   "Rpt2ABAmt":number,
   "Rpt3ABAmt":number,
   "CustOnCreditHold":boolean,
      /**  The flag to indicate if Invoice Header Apply Date is supposed to be Read Only  */  
   "DisableAplDate":boolean,
      /**   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  */  
   "RecalcAmts":string,
      /**  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  */  
   "CardTypeDescription":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**  Description  */  
   "CurrRateGrpDescription":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  Full description of the FOB Code.  */  
   "FOBDescription":string,
      /**  Journal  Description.  */  
   "JournalCodeJrnlDescription":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  IBAN Code  */  
   "OurBankIBANCode":string,
      /**  Payer Reference  */  
   "OurBankPayerRef":string,
      /**  Full description of the bank account.  */  
   "OurBankDescription":string,
      /**  The account number for the bank account. Used for reference only.  */  
   "OurBankCheckingAccount":string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   "PayMethodSummarizePerCustomer":boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   "PayMethodType":number,
      /**  Name of the payment method  */  
   "PayMethodName":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Full description of Project Management Code.  */  
   "ProjectDescription":string,
      /**  Description  */  
   "TaxRateGrpDescription":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionDescription":string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   "TermsCodeDescription":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
      /**  It indicates that this Invoice has taxes, for which the confirmation is required.  */  
   "NeedConfirmTaxes":boolean,
      /**  Boolean for selection of invoices in grid  */  
   "Selected":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InvcHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if invoice is "open".  */  
   "OpenInvoice":boolean,
      /**  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  */  
   "ClosedDate":string,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   "CreditMemo":boolean,
      /**  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  */  
   "UnappliedCash":boolean,
      /**   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   "CheckRef":string,
      /**  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  */  
   "InvoiceSuffix":string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  */  
   "GroupID":string,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   "Posted":boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   "InvoiceNum":number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   "InvoiceType":string,
      /**  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  */  
   "DeferredRevenue":boolean,
      /**  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  */  
   "OrderNum":number,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   "CustNum":number,
      /**  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  */  
   "PONum":string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   "EntryPerson":string,
      /**  Defaults from sales order ORderHed.FOB  */  
   "FOB":string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   "TermsCode":string,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   "InvoiceDate":string,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   "DueDate":string,
      /**  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  */  
   "FiscalYear":number,
      /**  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  */  
   "FiscalPeriod":number,
      /**  Once posted, maintenance is not allowed.  */  
   "GLPosted":boolean,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   "InvoiceAmt":number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   "DocInvoiceAmt":number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   "InvoiceBal":number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   "DocInvoiceBal":number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "UnpostedBal":number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   "DocUnpostedBal":number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   "DepositCredit":number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   "DocDepositCredit":number,
      /**  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  */  
   "SalesRepList":string,
      /**   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   "InvoiceRef":number,
      /**  Value of this field is reference to invoice which has been cancelled by current invoice.  */  
   "RefCancelled":number,
      /**  Value of this field is reference to invoice that cancelled this invoice.  */  
   "RefCancelledBy":number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   "StartUp":boolean,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   "PayDates":string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   "PayAmounts":string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   "DocPayAmounts":string,
      /**  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  */  
   "PayDiscDate":string,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   "PayDiscAmt":number,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   "DocPayDiscAmt":number,
      /**  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  */  
   "BillConNum":number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  */  
   "InvoiceHeld":boolean,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  Journal that invoice was posted to.  */  
   "JournalCode":string,
      /**  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  */  
   "LineType":string,
      /**   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   "RMANum":number,
      /**  The Site that the invoice is relate to.  */  
   "Plant":string,
      /**  The member's name on the credit card.  */  
   "CardMemberName":string,
      /**  The credit card account identifier.  */  
   "CardNumber":string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   "CardType":string,
      /**  The expiration month of the credit card.  */  
   "ExpirationMonth":number,
      /**  The expiration year of the credit card.  */  
   "ExpirationYear":number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   "CardID":string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   "CardmemberReference":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  External Identifier  */  
   "ExternalID":string,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefInvoiceNum":string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "DepGainLoss":number,
      /**  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  */  
   "DNComments":string,
      /**  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  */  
   "DNCustNbr":string,
      /**   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  */  
   "DebitNote":boolean,
      /**  This is populated from ShipHead.CustNum representing the Sold To customer.  */  
   "SoldToCustNum":number,
      /**  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  */  
   "Consolidated":boolean,
      /**  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  */  
   "BillToInvoiceAddress":boolean,
      /**  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  */  
   "SoldToInvoiceAddress":boolean,
      /**  Stores the encrypted credit card number  */  
   "ProcessCard":string,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   "RepComm1":number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   "RepComm2":number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   "RepComm3":number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   "RepComm4":number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   "RepComm5":number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   "RepRate1":number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   "RepRate2":number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   "RepRate3":number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   "RepRate4":number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   "RepRate5":number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   "RepSales1":number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   "RepSales2":number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   "RepSales3":number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   "RepSales4":number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   "RepSales5":number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   "RepSplit1":number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   "RepSplit2":number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   "RepSplit3":number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   "RepSplit4":number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   "RepSplit5":number,
      /**  Indicates if the Credit Memo is for a Rebate  */  
   "CMType":string,
      /**  Address used during AVS validation for credit transactions  */  
   "CCStreetAddr":string,
      /**  Zip used during AVS validation in credit transactions  */  
   "CCZip":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   "ReadyToCalc":boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   "EDIReady":boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   "RecalcBeforePost":boolean,
      /**  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   "Rounding":number,
      /**  Rounding in Customer currency  */  
   "DocRounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DepositCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DepositCredit":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DepositCredit":number,
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
   "Rpt1PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt2PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt3PayAmounts":string,
      /**  Reporting currency value of this field  */  
   "Rpt1PayDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2PayDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3PayDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Rounding":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnpostedBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnpostedBal":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnpostedBal":number,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Amount of deposit applied  */  
   "DocDepApplied":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt1DepGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt2DepGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt3DepGainLoss":number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   "ApplyDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Tax point  */  
   "TaxPoint":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**  The last date finance/late charges have been calculated for this invoice.  */  
   "LastChrgCalcDate":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Total Finance Charge amount.  */  
   "TotFinChrg":number,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   "PayDiscDays":string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   "PayDiscPer":string,
      /**  Blocks certain invoice from generating finance/later charge.  */  
   "BlockedFinChrg":boolean,
      /**  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  */  
   "BlockedFinChrgReason":string,
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
      /**  Blocks certain invoice from being printed on reminder letters.  */  
   "BlockedRemLetters":boolean,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   "PayDiscPartPay":boolean,
      /**  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  */  
   "BlockedRemLettersReason":string,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   "ShipDate":string,
      /**  Currency Rate Date  */  
   "CurrRateDate":string,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   "PIPayment":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  */  
   "UseAltBillTo":boolean,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  */  
   "CorrectionInv":boolean,
      /**  Tax Rate Group Code  */  
   "TaxRateGrpCode":string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   "LockTaxRate":boolean,
      /**  Sweden Finland Localization field - Banking Reference  */  
   "SEBankRef":string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   "GUITaxTypeCode":string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   "GUIFormatCode":string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   "GUIDeductCode":string,
      /**  Reversal Doucment Amount  */  
   "ReversalDocAmount":number,
      /**  Original Due Date at posting time  */  
   "OrigDueDate":string,
      /**  The reference to CashHead.HeadNum.Used in deposit invoices  */  
   "HeadNum":number,
      /**  Letter of Credit ID.  */  
   "ARLOCID":string,
      /**  The free text field which can contain reference (such as Contract)  */  
   "ContractRef":string,
      /**  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  */  
   "OurBank":string,
      /**  Addition to Contract  */  
   "ContractDate":string,
      /**  If the invoice was generated in Project Billing then it is reference to the project.  */  
   "PBProjectID":string,
      /**  Deposit amount is transaction amount of deposit payment  */  
   "DepositAmt":number,
      /**   Taiwan Localization
Export Bill Number  */  
   "GUIExportBillNumber":string,
      /**  Deposit amount is transaction amount of deposit payment in document currency  */  
   "DocDepositAmt":number,
      /**   Taiwan Localization
Date of Export  */  
   "GUIDateOfExport":string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt1 currency  */  
   "Rpt1DepositAmt":number,
      /**   Taiwan Localization
Export Type  */  
   "GUIExportType":string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt2 currency  */  
   "Rpt2DepositAmt":number,
      /**   Taiwan Localization
Export Mark  */  
   "GUIExportMark":string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt23currency  */  
   "Rpt3DepositAmt":number,
      /**   Taiwan Localization
Export Bill Type  */  
   "GUIExportBillType":string,
      /**  Deposit unallocated amount in base currency  */  
   "DepUnallocatedAmt":number,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   "SummarizationDate":string,
      /**  Deposit unallocated amount in document currency  */  
   "DocDepUnallocatedAmt":number,
      /**  Date when a company bills the customer  */  
   "BillingDate":string,
      /**  Deposit unallocated amount in Rpt1 currency  */  
   "Rpt1DepUnallocatedAmt":number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   "BillingNumber":string,
      /**  Deposit unallocated amount in Rpt2 currency  */  
   "Rpt2DepUnallocatedAmt":number,
      /**  Only records ready to bill will be printed in the Billing Statement  */  
   "ReadyToBill":boolean,
      /**  Deposit unallocated amount in Rpt3 currency  */  
   "Rpt3DepUnallocatedAmt":number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   "OvrDefTaxDate":boolean,
      /**  Cross Reference Contract Number.  */  
   "XRefContractNum":string,
      /**  Cross Reference Contract Date.  */  
   "XRefContractDate":string,
      /**  Main Site  */  
   "MainSite":boolean,
      /**  Site Code  */  
   "SiteCode":string,
      /**  Branch ID  */  
   "BranchID":string,
      /**  Customer Agent Name  */  
   "CustAgentName":string,
      /**  Customer Agent Tax Region Number  */  
   "CustAgentTaxRegNo":string,
      /**  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  */  
   "ExportType":string,
      /**  Export Report Number  */  
   "ExportReportNo":string,
      /**  Real Estate Number  */  
   "RealEstateNo":string,
      /**  Excluded  */  
   "Excluded":boolean,
      /**  Deferred  */  
   "Deferred":boolean,
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
      /**  RecurringState  */  
   "RecurringState":string,
      /**  IsRecurring  */  
   "IsRecurring":boolean,
      /**  InvoiceNumList  */  
   "InvoiceNumList":string,
      /**  IsAddedToGTI  */  
   "IsAddedToGTI":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CHISRCodeLine  */  
   "CHISRCodeLine":string,
      /**  CMReason  */  
   "CMReason":string,
      /**  THIsImmatAdjustment  */  
   "THIsImmatAdjustment":boolean,
      /**  AGAuthorizationCode  */  
   "AGAuthorizationCode":string,
      /**  AGAuthorizationDate  */  
   "AGAuthorizationDate":string,
      /**  AGUseGoodDefaultMark  */  
   "AGUseGoodDefaultMark":boolean,
      /**  AGDocumentLetter  */  
   "AGDocumentLetter":string,
      /**  AGInvoicingPoint  */  
   "AGInvoicingPoint":string,
      /**  AGLegalNumber  */  
   "AGLegalNumber":string,
      /**  AGPrintingControlType  */  
   "AGPrintingControlType":string,
      /**  RevisionDate  */  
   "RevisionDate":string,
      /**  RevisionNum  */  
   "RevisionNum":number,
      /**  TWDeclareYear  */  
   "TWDeclareYear":number,
      /**  TWDeclarePeriod  */  
   "TWDeclarePeriod":number,
      /**  TWGenerationType  */  
   "TWGenerationType":string,
      /**  TWGUIGroup  */  
   "TWGUIGroup":string,
      /**  TWPeriodPrefix  */  
   "TWPeriodPrefix":string,
      /**  Indicates if the Invoice is in Collections status  */  
   "InvInCollections":boolean,
      /**   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  */  
   "CollectionsCust":boolean,
      /**  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  */  
   "CounterARForm":number,
      /**  flag indicates if Revenue of the invoice has been already posted  */  
   "PostedRecog":boolean,
      /**  Confirmation Date  */  
   "CNConfirmDate":string,
      /**  MXSATSeal  */  
   "MXSATSeal":string,
      /**  MXSerie  */  
   "MXSerie":string,
      /**  MXTaxRcptType  */  
   "MXTaxRcptType":string,
      /**  MXFiscalFolio  */  
   "MXFiscalFolio":string,
      /**  MXTotalPayments  */  
   "MXTotalPayments":number,
      /**  MXFolio  */  
   "MXFolio":string,
      /**  MXCertifiedTimestamp  */  
   "MXCertifiedTimestamp":string,
      /**  MXSATCertificateSN  */  
   "MXSATCertificateSN":string,
      /**  MXDigitalSeal  */  
   "MXDigitalSeal":string,
      /**  MXPostedTimeStamp  */  
   "MXPostedTimeStamp":string,
      /**  MXCertificate  */  
   "MXCertificate":string,
      /**  MXApprovalYear  */  
   "MXApprovalYear":number,
      /**  MXCBB  */  
   "MXCBB":string,
      /**  MXApprovalNum  */  
   "MXApprovalNum":number,
      /**  MXOriginalStringTFD  */  
   "MXOriginalStringTFD":string,
      /**  MXPaymentNum  */  
   "MXPaymentNum":number,
      /**  MXPaidAs  */  
   "MXPaidAs":string,
      /**  MXCertificateSN  */  
   "MXCertificateSN":string,
      /**  MXOriginalAmount  */  
   "MXOriginalAmount":number,
      /**  MXAccountNumber  */  
   "MXAccountNumber":string,
      /**  MXOriginalDate  */  
   "MXOriginalDate":string,
      /**  MXOriginalSeries  */  
   "MXOriginalSeries":string,
      /**  MXOriginalFolio  */  
   "MXOriginalFolio":string,
      /**  MXTaxRegime  */  
   "MXTaxRegime":string,
      /**  MXOriginalString  */  
   "MXOriginalString":string,
      /**  MXPaymentName  */  
   "MXPaymentName":string,
      /**  EInvoice  */  
   "EInvoice":boolean,
      /**  EInvStatus  */  
   "EInvStatus":number,
      /**  EInvTimestamp  */  
   "EInvTimestamp":string,
      /**  EInvUpdatedBy  */  
   "EInvUpdatedBy":string,
      /**  EInvException  */  
   "EInvException":string,
      /**  Flagged that this invoice has taxes which were necessary or is necessary now.  */  
   "WithTaxConfirm":boolean,
      /**  UseAltBillToID  */  
   "UseAltBillToID":boolean,
      /**  MXCancelledDate  */  
   "MXCancelledDate":string,
      /**  Overpaid  */  
   "Overpaid":boolean,
      /**  OrdExchangeRate  */  
   "OrdExchangeRate":number,
      /**  PEAPPayNum  */  
   "PEAPPayNum":number,
      /**  PEBankNumber  */  
   "PEBankNumber":string,
      /**  PECharges  */  
   "PECharges":number,
      /**  PECommissions  */  
   "PECommissions":number,
      /**  PEDetTaxAmt  */  
   "PEDetTaxAmt":number,
      /**  PEDetTaxCurrencyCode  */  
   "PEDetTaxCurrencyCode":string,
      /**  PEDischargeAmt  */  
   "PEDischargeAmt":number,
      /**  PEDischargeDate  */  
   "PEDischargeDate":string,
      /**  PEInterest  */  
   "PEInterest":number,
      /**  PENoPayPenalty  */  
   "PENoPayPenalty":number,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   "PESUNATDepAmt":number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   "PESUNATDepDate":string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   "PESUNATDepNum":string,
      /**  PEBOEPosted  */  
   "PEBOEPosted":boolean,
      /**  DocPEInterest  */  
   "DocPEInterest":number,
      /**  DocPECommissions  */  
   "DocPECommissions":number,
      /**  DocPECharges  */  
   "DocPECharges":number,
      /**  DocPENoPayPenalty  */  
   "DocPENoPayPenalty":number,
      /**  DocPEDischargeAmt  */  
   "DocPEDischargeAmt":number,
      /**  DocPEDetTaxAmt  */  
   "DocPEDetTaxAmt":number,
      /**  Rpt1PEInterest  */  
   "Rpt1PEInterest":number,
      /**  Rpt1PECommissions  */  
   "Rpt1PECommissions":number,
      /**  Rpt1PECharges  */  
   "Rpt1PECharges":number,
      /**  Rpt1PENoPayPenalty  */  
   "Rpt1PENoPayPenalty":number,
      /**  Rpt1PEDischargeAmt  */  
   "Rpt1PEDischargeAmt":number,
      /**  Rpt2PEInterest  */  
   "Rpt2PEInterest":number,
      /**  Rpt2PECommissions  */  
   "Rpt2PECommissions":number,
      /**  Rpt2PECharges  */  
   "Rpt2PECharges":number,
      /**  Rpt2PENoPayPenalty  */  
   "Rpt2PENoPayPenalty":number,
      /**  Rpt2PEDischargeAmt  */  
   "Rpt2PEDischargeAmt":number,
      /**  Rpt3PEInterest  */  
   "Rpt3PEInterest":number,
      /**  Rpt3PECommissions  */  
   "Rpt3PECommissions":number,
      /**  Rpt3PECharges  */  
   "Rpt3PECharges":number,
      /**  Rpt3PENoPayPenalty  */  
   "Rpt3PENoPayPenalty":number,
      /**  Rpt3PEDischargeAmt  */  
   "Rpt3PEDischargeAmt":number,
      /**  Our Supplier Code  */  
   "OurSupplierCode":string,
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
      /**  PEGuaranteeTaxID  */  
   "PEGuaranteeTaxID":string,
      /**  PEGuaranteePhoneNum  */  
   "PEGuaranteePhoneNum":string,
      /**  PEBOEStatus  */  
   "PEBOEStatus":string,
      /**  PEBOEIsMultiGen  */  
   "PEBOEIsMultiGen":boolean,
      /**  PE Reference Document ID  */  
   "PERefDocID":string,
      /**  PE Reason Code  */  
   "PEReasonCode":string,
      /**  PE Reason Description  */  
   "PEReasonDesc":string,
      /**  TW GUI Code Seller  */  
   "TWGUIRegNumSeller":string,
      /**  TW GUI Code Buyer  */  
   "TWGUIRegNumBuyer":string,
      /**  Document Name  */  
   "TWGUIExportDocumentName":string,
      /**  Remarks  */  
   "TWGUIExportRemarks":string,
      /**  Verification  */  
   "TWGUIExportVerification":string,
      /**  PEDebitNoteReasonCode  */  
   "PEDebitNoteReasonCode":string,
      /**  PEDebitNote  */  
   "PEDebitNote":boolean,
      /**  MXPartPmt  */  
   "MXPartPmt":boolean,
      /**  Tax Invoice Type  */  
   "CNTaxInvoiceType":number,
      /**  MXExportOperationType  */  
   "MXExportOperationType":string,
      /**  MXExportCustDocCode  */  
   "MXExportCustDocCode":string,
      /**  MXExportCertOriginNum  */  
   "MXExportCertOriginNum":string,
      /**  MXExportConfNum  */  
   "MXExportConfNum":string,
      /**  MXExportCertOrigin  */  
   "MXExportCertOrigin":boolean,
      /**  MXIncoterm  */  
   "MXIncoterm":string,
      /**  AGDocConcept  */  
   "AGDocConcept":number,
      /**  Electronic Invoice reference number  */  
   "EInvRefNum":string,
      /**  Export document reference number  */  
   "ExportDocRefNum":string,
      /**  Export document date  */  
   "ExportDocDate":string,
      /**  Tax Transaction ID  */  
   "INTaxTransactionID":string,
      /**  MXMovingReasonFlag  */  
   "MXMovingReasonFlag":boolean,
      /**  MXMovingReason  */  
   "MXMovingReason":string,
      /**  MXNumRegIdTrib  */  
   "MXNumRegIdTrib":string,
      /**  MXResidenCountryNum  */  
   "MXResidenCountryNum":number,
      /**  MXPurchaseType  */  
   "MXPurchaseType":string,
      /**  MXConfirmationCode  */  
   "MXConfirmationCode":string,
      /**  MXExternalCode  */  
   "MXExternalCode":string,
      /**  This invoice was created via an integration with a third-party field service.  */  
   "ServiceInvoice":boolean,
      /**  MXDomesticTransfer  */  
   "MXDomesticTransfer":boolean,
      /**  MXCancellationMode  */  
   "MXCancellationMode":string,
      /**  Shipping Port Code  */  
   "INShippingPortCode":string,
      /**  Export Procedure  */  
   "INExportProcedure":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  DigitalSignature  */  
   "DigitalSignature":string,
      /**  SignedOn  */  
   "SignedOn":string,
      /**  SignedBy  */  
   "SignedBy":string,
      /**  FirstPrintDate  */  
   "FirstPrintDate":string,
      /**  DocCopyNum  */  
   "DocCopyNum":number,
      /**  DepositBalance  */  
   "DepositBalance":number,
      /**  DocDepositBalance  */  
   "DocDepositBalance":number,
      /**  Rpt1DepositBalance  */  
   "Rpt1DepositBalance":number,
      /**  Rpt2DepositBalance  */  
   "Rpt2DepositBalance":number,
      /**  Rpt3DepositBalance  */  
   "Rpt3DepositBalance":number,
      /**  Quote number to which this invoice record is associated with.  */  
   "QuoteNum":number,
      /**  The help desk case related to this invoice.  */  
   "HDCaseNum":number,
      /**  Indicates that the credit hold was overridden for this invoice.  */  
   "CreditOverride":boolean,
      /**  Description	Indicates that the credit hold was overridden for this invoice.	The date and time the user override the invoice credit hold.  */  
   "CreditOverrideDate":string,
      /**  The user id that override the invoice credit hold.  */  
   "CreditOverrideUserID":string,
      /**  Indicates the invoice is on credit hold.  Applicable to miscellaneous invoices only.  */  
   "CreditHold":boolean,
      /**  Peru Electronic Invoice XML Type  */  
   "PEXMLType":number,
      /**  COCreditMemoReasonCode  */  
   "COCreditMemoReasonCode":string,
      /**  CODebitMemoReasonCode  */  
   "CODebitMemoReasonCode":string,
      /**  COReasonDesc  */  
   "COReasonDesc":string,
      /**  CODebitNote  */  
   "CODebitNote":boolean,
      /**  PEDetractionTranNum  */  
   "PEDetractionTranNum":number,
      /**  PEProductCode  */  
   "PEProductCode":string,
      /**  PECollectionGroupID  */  
   "PECollectionGroupID":string,
      /**  PE Caption Code  */  
   "PECaptionCode":string,
      /**  PE Caption Code Description  */  
   "PECaption":string,
      /**  PE Reference DocumentType 1  */  
   "PERefDocumentType":string,
      /**  PE Reference Document Number 1  */  
   "PERefDocumentNumber":string,
      /**  PE Detraction good or service code  */  
   "PEDetrGoodServiceCode":string,
      /**  PE Reference DocumentType 2  */  
   "PERefDocumentType2":string,
      /**  PE Reference DocumentType 3  */  
   "PERefDocumentType3":string,
      /**  PE Reference DocumentType 4  */  
   "PERefDocumentType4":string,
      /**  PE Reference DocumentType 5  */  
   "PERefDocumentType5":string,
      /**  PE Reference Document Number 2  */  
   "PERefDocumentNumber2":string,
      /**  PE Reference Document Number 3  */  
   "PERefDocumentNumber3":string,
      /**  PE Reference Document Number 4  */  
   "PERefDocumentNumber4":string,
      /**  PE Reference Document Number 5  */  
   "PERefDocumentNumber5":string,
      /**  E-invoice  */  
   "ELIEInvoice":boolean,
      /**  Status of E-invoice (1 - Open, 2 - Generated, 3 - Sent, 4 - Error).  */  
   "ELIEInvStatus":number,
      /**  User Id of the person generated E-invoice.  */  
   "ELIEInvUpdatedBy":string,
      /**  E-invoice error description.  */  
   "ELIEInvException":string,
      /**  Date and Time of E-invoice generation.  */  
   "ELIEInvUpdatedOn":string,
      /**  COOperType  */  
   "COOperType":string,
      /**  Flag that indicates if the Invoice is for Central Collection.  */  
   "CentralCollection":boolean,
      /**  Company that created this invoice.  */  
   "CColChildCompany":string,
      /**  Central Collection company.  */  
   "CColParentCompany":string,
      /**  Order number on the invoicing company.  */  
   "CColOrderNum":number,
      /**  Invoice number on the invoicing company.  */  
   "CColChildInvoiceNum":number,
      /**  Invoice number on central collection company  */  
   "CColInvoiceNum":number,
      /**  Legal number on the invoicing company invoice.  */  
   "CColChildLegalNumber":string,
      /**  Legal number on central collection company.  */  
   "CColLegalNumber":string,
      /**  Invoice reference on the Invoicing Company.  */  
   "CColInvoiceRef":number,
      /**  Invoice Balance in the Central Collection company.  */  
   "CColInvBal":number,
      /**  Central Collection Doc Invoice Balance.  */  
   "DocCColInvBal":number,
      /**  Invoice Amount on the Invoicing Company.  */  
   "CColInvAmt":number,
      /**  Invoice Amount on the Invoicing Company.  */  
   "DocCColInvAmt":number,
      /**  Rpt 1 Parent Invoice Balance  */  
   "Rpt1CColInvBal":number,
      /**  Rpt 2 Parent Invoice Balance  */  
   "Rpt2CColInvBal":number,
      /**  Rpt 3 Parent Invoice Balance  */  
   "Rpt3CColInvBal":number,
      /**  Rpt 1 Child Invoice Amount  */  
   "Rpt1CColInvAmt":number,
      /**  Rpt 2 Child Invoice Amount  */  
   "Rpt2CColInvAmt":number,
      /**  Rpt 3 Child Invoice Amount  */  
   "Rpt3CColInvAmt":number,
      /**  Id of the netting transaction that generated this document.  */  
   "NettingID":number,
      /**  User terminal name  */  
   "ELIEInvTerminalName":string,
      /**  User terminal IP  */  
   "ELIEInvTerminalIP":string,
      /**  GL Description  */  
   "Description":string,
      /**  WithholdAcctToInterim  */  
   "WithholdAcctToInterim":boolean,
      /**  Indicates if the Central Collection parent invoice is open.  */  
   "CColOpenInvoice":boolean,
      /**  AGQRCodeData  */  
   "AGQRCodeData":string,
      /**  Exempt Reason Code  */  
   "ExemptReasonCode":string,
      /**  EInvoice ID  */  
   "ELIEInvID":string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   "CallNum":number,
      /**  this is a link to the service call line that this invoice is for.  Linetype = "CALL"  */  
   "CallLine":number,
      /**  Associates the Call Line record back its linked jobnum  */  
   "JobNum":string,
      /**  MXCancelReasonCode  */  
   "MXCancelReasonCode":string,
      /**  MXSubstInvoiceNum  */  
   "MXSubstInvoiceNum":number,
      /**  MXExportType  */  
   "MXExportType":string,
      /**  MXGlobalInvoicePeriod  */  
   "MXGlobalInvoicePeriod":string,
      /**  MXGlobalInvoiceMonth  */  
   "MXGlobalInvoiceMonth":string,
      /**  ELIEInvServiceProviderStatus  */  
   "ELIEInvServiceProviderStatus":number,
      /**  Incoterm Code  */  
   "IncotermCode":string,
      /**  Incoterm Location  */  
   "IncotermLocation":string,
      /**  CovenantDiscPercent  */  
   "CovenantDiscPercent":number,
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
      /**  Total advanced billing amount.  */  
   "ABAmt":number,
      /**  Indicates if changes can occur after the document has been printed  */  
   "AllowChgAfterPrint":boolean,
      /**  Rpt3InCovenantDiscount  */  
   "Rpt3InCovenantDiscount":number,
      /**  ARPNHead's HeadNum  */  
   "ARPNHeadNum":number,
      /**  when InvcHead.PIPayment = O then populate ARPaymentInstrumentID with a value of PI.  */  
   "ARPromNoteID":string,
      /**  Auto generate payment instruments  */  
   "AutoGenPN":boolean,
      /**  Delimited list of available bill to customers.  */  
   "AvailBTCustList":string,
      /**  Used for Bill of Exchange.  Indicates the bank to use when a payment instrument for the invoice is created.  */  
   "BankForPI":string,
   "BankForPIName":string,
      /**  Customer ID for the bill to customer (InvcHead.CustNum).  */  
   "BTCustID":string,
      /**  Bill to customer name.  */  
   "BTCustomerName":string,
      /**  The date and time that the record was last changed  */  
   "ChangeDateTime":string,
   "CNGTIAction":string,
   "CNGTIAddress":string,
   "CNGTIBankAccount":string,
   "CNGTIComment":string,
   "CNGTICustomerName":string,
   "CNGTIExportAddress":string,
      /**  CSF China, Gross Invoice Amount  */  
   "CNGTIGrossInvcAmt":number,
      /**  CSF China, Total invoice amount = InvcHead.InvoiceAmt - InvcHead.WithholdAmt  */  
   "CNGTIInvoiceAmt":number,
   "CNGTINote":string,
   "CNGTIShipToNum":string,
   "CNGTIStatus1":string,
   "CNGTIStatus2":boolean,
   "CNGTITaxCode":string,
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
      /**  Indicates if Invoice is in Collections (Peru localization)  */  
   "CollectionsInv":boolean,
      /**  Contact email address.  */  
   "ContactEmailAddr":string,
      /**  Contact fax number  */  
   "ContactFaxNum":string,
      /**  Contact name  */  
   "ContactName":string,
      /**  Contact phone number  */  
   "ContactPhoneNum":string,
      /**  record converted from deposit  */  
   "ConvertedFromDep":boolean,
   "COOperTypeDesc":string,
      /**  True if the Country set for the current company contains an Intrastat code.  */  
   "CountryIntrastat":boolean,
   "CumulativeBalance":number,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   "CurrencySwitch":boolean,
   "CurrentInstanceNum":number,
   "CustAllowOTS":boolean,
   "CustOnCreditHold":boolean,
      /**  Deposit balance from CashHed  */  
   "DepBal":number,
      /**  Deposit credit enabled flag.  */  
   "DepositCreditEnabled":boolean,
   "DirectDebiting":boolean,
      /**  The flag to indicate if Invoice Header Apply Date is supposed to be Read Only  */  
   "DisableAplDate":boolean,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   "DispBalDN":number,
      /**  Bill to address in list format.  */  
   "DisplayBillAddr":string,
      /**  Display field for the masked credit card number  */  
   "DisplayCreditCardNum":string,
   "DisplayCurrencyID":string,
      /**  Currency display symbol  */  
   "DisplaySymbol":string,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   "DNPmtAmt":number,
      /**  Document Total advanced billing amount.  */  
   "DocABAmt":number,
      /**  Financial Charge  */  
   "DocCOIFRSFinancialCharge":number,
      /**  Present Value  */  
   "DocCOIFRSPresentValue":number,
   "DocCumulativeBalance":number,
      /**  Document deposit amount from cashhead.  */  
   "DocDepBal":number,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   "DocDispBalDN":number,
      /**  Document display symbol  */  
   "DocDisplaySymbol":string,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   "DocDNPmtAmt":number,
   "DocDspPrepDeposit":number,
   "DocDspTaxAmt":number,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   "DocPESUNATDepAmt":number,
   "DocRemainTaxAmt":number,
   "DocReverseTaxAmt":number,
   "DocSATaxAmt":number,
   "DocSourceRecurBalance":number,
      /**  Document sub total  */  
   "DocSubTotal":number,
      /**  Document Total tax amount from InvcTax for Collection type 'Invoice'  */  
   "DocTaxAmt":number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in document currency.  */  
   "DocVr":number,
   "DocWHTaxAmt":number,
      /**  Display advance billing amount  */  
   "DspABAmt":number,
      /**  Display deposit balance.  */  
   "DspDepBal":number,
      /**  Display deposit credit.  */  
   "DspDepCr":number,
   "DspDigitalSignature":string,
      /**  Display document advance billing amount  */  
   "DspDocABAmt":number,
      /**  Display document deposit balance  */  
   "DspDocDepBal":number,
      /**  Display document deposit credit.  */  
   "DspDocDepCr":number,
      /**  Display document invoice amount  */  
   "DspDocInvoiceAmt":number,
      /**  Display document invoice balance  */  
   "DspDocInvoiceBal":number,
      /**  Display Invoice Doc Rounding  */  
   "DspDocRounding":number,
      /**  display document sub total  */  
   "DspDocSubTotal":number,
      /**  Display invoice amount  */  
   "DspInvoiceAmt":number,
      /**  Display Invoice Balance.  */  
   "DspInvoiceBal":number,
      /**  Display invoice reference  */  
   "DspInvoiceRef":number,
   "DspPayDiscDays":string,
   "DspPrepDeposit":number,
      /**  Display Rounding in Base  */  
   "DspRounding":number,
      /**  If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   "dspSoldToCustID":string,
      /**  Display sub total  */  
   "DspSubTotal":number,
   "DspTaxAmt":number,
      /**  Indicates if assign legal number option is available.  */  
   "EnableAssignLegNum":boolean,
   "EnableCentralCollection":boolean,
      /**  Flag to determine if UseSOCCDefaults should be enabled.  */  
   "EnableSOCCDefaults":boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   "EnableTranDocType":boolean,
      /**  Indicates if the void legal number option is available  */  
   "EnableVoidLegNum":boolean,
      /**  It will be displayed to identify invoices automatically generated due ERS shipments.  */  
   "ERSInvoice":boolean,
      /**  Indicates which date to be used to calculate the exchange rate, I for Invoice Date, A for Apply Date.  */  
   "ExchangeRateDate":string,
      /**  Flag for update of InvcHead to allow when group id is "RMACRREQ"  */  
   "GenedFromRMA":boolean,
      /**  CustBank record exists for customer  */  
   "HasBank":boolean,
      /**  Indicates if a legal number configuration exists for ar invoices/credit memos  */  
   "HasLegNumCnfg":boolean,
      /**  In case if Invoice Header Tax Liability is not assigned this flag indicates if any of Invoice lines has Tax inclusive Tax Liability assinged  */  
   "InPriceLn":boolean,
      /**  Integration invoice type.  Used for setting of InvoiceType.  */  
   "IntInvoiceType":string,
      /**  InvoiceType description  */  
   "InvoiceTypeDesc":string,
      /**  Denmark localization external field  */  
   "IsDK":boolean,
      /**  Set to true if intrastat is enabled.  */  
   "IsIntrastatSensitive":boolean,
   "IsLatestRecurrence":boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Indicates if the UR Invoice was created from an On Account PI instead of an on account cash receipt.  */  
   "IsPIUnappliedReceipt":boolean,
   "IsPMForGenPIType":boolean,
   "LatestInvoice":number,
      /**  Stores the message when a legal number is generated.  */  
   "LegalNumberMessage":string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  MXCancellationID  */  
   "MXCancellationID":string,
      /**  MXCancellationStatus  */  
   "MXCancellationStatus":string,
      /**  It indicates that this Invoice has taxes, for which the confirmation is required.  */  
   "NeedConfirmTaxes":boolean,
      /**  This field is to display in Cash Receipt Entry the Discount Date that the payment will take.  */  
   "NextDiscDate":string,
      /**  NextInvoiceDate = InvcRecurringCycle.LastDate + RecurringCycle.Interval in RecurringCycle.Modifier units  */  
   "NextInvoiceDate":string,
      /**  Pack slip number from the 1st line item.  */  
   "PackSlipNum":number,
      /**  Pay schedule enabled flag  */  
   "PaySchedEnabled":boolean,
      /**  Indicates what the user will change the status to  */  
   "PEBOEChangeStatusTo":string,
   "PEBOEStatusDesc":string,
      /**  Peru CSF: Collections date  */  
   "PECollectionsDate":string,
      /**  PE Detraction good or service code description  */  
   "PEDetrGoodServiceCodeDesc":string,
   "PEDspCurrencySymbol":string,
      /**  Peru CSF: No if the invoice is moved out of collections, Yes if the invoice is moved into colletions.  */  
   "PEInCollections":boolean,
      /**  PE Document Type Description  */  
   "PERefDocumentTypeDesc":string,
      /**  PE Document Type Description 2  */  
   "PERefDocumentTypeDesc2":string,
      /**  PE Document Type Description 3  */  
   "PERefDocumentTypeDesc3":string,
      /**  PE Document Type Description 4  */  
   "PERefDocumentTypeDesc4":string,
      /**  PE Document Type Description 5  */  
   "PERefDocumentTypeDesc5":string,
      /**  PI - Bank account  */  
   "PIBankAcctID":string,
      /**  PI Customer bank required  */  
   "PICustBankDtl":boolean,
      /**  PI Initiation - generated or received  */  
   "PIInitiation":string,
      /**  Prep Deposit enabled flag.  */  
   "PrepDepositEnabled":boolean,
      /**  The description of the proposed Tax Region  */  
   "ProposedTaxRgn":string,
      /**   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  */  
   "RecalcAmts":string,
      /**  Recurring flag  */  
   "Recurring":boolean,
   "RemainTaxAmt":number,
   "ReminderSeq":number,
      /**  Accumulate all reversal amounts of Credit Memos with the reference to the invoice  */  
   "ReversalDocAmt":number,
   "ReverseTaxAmt":number,
   "Rpt1ABAmt":number,
      /**  Financial Charge  */  
   "Rpt1COIFRSFinancialCharge":number,
      /**  Present Value  */  
   "Rpt1COIFRSPresentValue":number,
   "Rpt1CumulativeBalance":number,
   "Rpt1DepBal":number,
   "Rpt1DspABAmt":number,
   "Rpt1DspDepBal":number,
   "Rpt1DspDepCr":number,
   "Rpt1DspInvoiceAmt":number,
   "Rpt1DspInvoiceBal":number,
   "Rpt1DspPrepDeposit":number,
   "Rpt1DspRounding":number,
   "Rpt1DspSubTotal":number,
   "Rpt1DspTaxAmt":number,
   "Rpt1RemainTaxAmt":number,
   "Rpt1ReverseTaxAmt":number,
   "Rpt1SATaxAmt":number,
   "Rpt1SourceRecurBalance":number,
   "Rpt1SubTotal":number,
   "Rpt1TaxAmt":number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt1 currency.  */  
   "Rpt1Vr":number,
   "Rpt1WHTaxAmt":number,
   "Rpt2ABAmt":number,
      /**  Financial Charge  */  
   "Rpt2COIFRSFinancialCharge":number,
      /**  Present Value  */  
   "Rpt2COIFRSPresentValue":number,
   "Rpt2CumulativeBalance":number,
   "Rpt2DepBal":number,
   "Rpt2DspABAmt":number,
   "Rpt2DspDepBal":number,
   "Rpt2DspDepCr":number,
   "Rpt2DspInvoiceAmt":number,
   "Rpt2DspInvoiceBal":number,
   "Rpt2DspPrepDeposit":number,
   "Rpt2DspRounding":number,
   "Rpt2DspSubTotal":number,
   "Rpt2DspTaxAmt":number,
   "Rpt2RemainTaxAmt":number,
   "Rpt2ReverseTaxAmt":number,
   "Rpt2SATaxAmt":number,
   "Rpt2SourceRecurBalance":number,
   "Rpt2SubTotal":number,
   "Rpt2Taxamt":number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt2 currency.  */  
   "Rpt2Vr":number,
   "Rpt2WHTaxAmt":number,
   "Rpt3ABAmt":number,
      /**  Financial Charge  */  
   "Rpt3COIFRSFinancialCharge":number,
      /**  Present Value  */  
   "Rpt3COIFRSPresentValue":number,
   "Rpt3CumulativeBalance":number,
   "Rpt3DepBal":number,
   "Rpt3DspABAmt":number,
   "Rpt3DspDepBal":number,
   "Rpt3DspDepCr":number,
   "Rpt3DspInvoiceAmt":number,
   "Rpt3DspInvoiceBal":number,
   "Rpt3DspPrepDeposit":number,
   "Rpt3DspRounding":number,
   "Rpt3DspSubTotal":number,
   "Rpt3DspTaxAmt":number,
   "Rpt3RemainTaxAmt":number,
   "Rpt3ReverseTaxAmt":number,
   "Rpt3SATaxAmt":number,
   "Rpt3SourceRecurBalance":number,
   "Rpt3SubTotal":number,
   "Rpt3TaxAmt":number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt3 currency.  */  
   "Rpt3Vr":number,
   "Rpt3WHTaxAmt":number,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  1st entry in SalesRepList  */  
   "SalesRepCode1":string,
      /**  2nd entry in SalesRepList  */  
   "SalesRepCode2":string,
      /**  3rd entry in SalesRepList.  */  
   "SalesRepCode3":string,
      /**  4th entry in SalesRepList  */  
   "SalesRepCode4":string,
      /**  5th entry in SalesRepList  */  
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
   "SATaxAmt":number,
      /**  Boolean for selection of invoices in grid  */  
   "Selected":boolean,
   "SkipRecurring":boolean,
      /**  Sold to address list.  */  
   "SoldToAddressList":string,
      /**  Sold to customer id  */  
   "SoldToCustID":string,
      /**  Sold to customer name.  */  
   "SoldToCustomerName":string,
   "SourceInvoiceNum":number,
   "SourceLastDate":string,
   "SourceRecurBalance":number,
      /**  Sub total for invoice  */  
   "SubTotal":number,
      /**  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  */  
   "SystemTranType":string,
      /**  Total tax amount from InvcTax  */  
   "TaxAmt":number,
   "TaxExchangeRate":number,
      /**  The flag to indicate if the user is supposed to be asked about Tax Liability change  */  
   "TaxRgnLineChange":boolean,
   "TotalInstanceNum":number,
      /**  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  */  
   "TransApplyDate":string,
      /**  If true, the credit card info will come from the sales order.  */  
   "UseSOCCDefaults":boolean,
   "UseTaxRate":boolean,
   "VNInvDescription":string,
   "VNInvoiceType":string,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in base currency.  */  
   "Vr":number,
   "WHTaxAmt":number,
      /**  Currency label  */  
   "XRateLabel":string,
   "zEnableCreditHold":boolean,
      /**  The number of days the invoice is past due.  */  
   "AgingDays":number,
      /**   The list of prohibited statuses.for the Invoice
For examle, if contains 2 (EINVOICE_STATUS_GENERATED) then Generate E-invoice is not allowed.
if contains 2 (EINVOICE_STATUS_SENT) then Sending Invoice via Service provider is not allowed  */  
   "ELIEInvProhibitedStatuses":string,
      /**  Flag indicating whether to enable Incoterm Location  */  
   "EnableIncotermLocation":boolean,
   "BitFlag":number,
   "AGInvoicingPointDescription":string,
   "ARSystLNReqForInvc":boolean,
   "CardTypeDescription":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrRateGrpDescription":string,
   "CustomerInactive":boolean,
   "CustomerMXGeneralPublic":boolean,
   "CustomerCustID":string,
   "CustomerBTName":string,
   "CustomerName":string,
   "CustomerELISendingOption":number,
   "FOBDescription":string,
   "IncotermsDescription":string,
   "JournalCodeJrnlDescription":string,
   "MXPurchaseTypeCodeDesc":string,
   "MXSubstInvoiceMXFiscalFolio":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "OurBankPayerRef":string,
   "OurBankBankIdentifier":string,
   "OurBankTypeCode":string,
   "OurBankBankAcctID":string,
   "OurBankCheckingAccount":string,
   "OurBankBankName":string,
   "OurBankIBANCode":string,
   "OurBankLocalBIC":string,
   "OurBankDescription":string,
   "PayMethodName":string,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodType":number,
   "PlantName":string,
   "ProjectDescription":string,
   "RecurringCycleMaximumValue":boolean,
   "SoldToCustNumInactive":boolean,
   "SoldToCustNumCustID":string,
   "SoldToCustNumName":string,
   "TaxRateGrpDescription":string,
   "TaxRegionDescription":string,
   "TermsCodeDescription":string,
   "TranDocTypeDescription":string,
   "XbSystOCRCalcType":boolean,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param invoiceNum
   */  
export interface DeleteByID_input{
   invoiceNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ARInvSearchTableset{
   InvcHead:Erp_Tablesets_InvcHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InvcHeadCancellationListRow{
   InvoiceDate:string,
   RecalculateTaxes:boolean,
   ReverseSign:boolean,
   SysRowID:string,
   SystemTranType:string,
   TranDocTypeDescription:string,
   TranDocTypeID:string,
   ApplyDate:string,
   CMReason:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcHeadCancellationListTHRow{
   ApplyDate:string,
   CMReason:string,
   InvoiceDate:string,
   RecalculateTaxes:boolean,
   ReverseSign:boolean,
   SysRowID:string,
   SystemTranType:string,
   TranDocTypeDescription:string,
   TranDocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if invoice is "open".  */  
   OpenInvoice:boolean,
      /**  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  */  
   ClosedDate:string,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   CreditMemo:boolean,
      /**  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  */  
   UnappliedCash:boolean,
      /**   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  */  
   InvoiceSuffix:string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   InvoiceType:string,
      /**  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  */  
   DeferredRevenue:boolean,
      /**  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  */  
   OrderNum:number,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   CustNum:number,
      /**  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  */  
   PONum:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Defaults from sales order ORderHed.FOB  */  
   FOB:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  */  
   FiscalPeriod:number,
      /**  Once posted, maintenance is not allowed.  */  
   GLPosted:boolean,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnpostedBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   DocUnpostedBal:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DepositCredit:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DocDepositCredit:number,
      /**  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  */  
   SalesRepList:string,
      /**   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   InvoiceRef:number,
      /**  Value of this field is reference to invoice which has been cancelled by current invoice.  */  
   RefCancelled:number,
      /**  Value of this field is reference to invoice that cancelled this invoice.  */  
   RefCancelledBy:number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   StartUp:boolean,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDates:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   PayAmounts:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   DocPayAmounts:string,
      /**  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  */  
   PayDiscDate:string,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   PayDiscAmt:number,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   DocPayDiscAmt:number,
      /**  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  */  
   BillConNum:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  */  
   InvoiceHeld:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Journal that invoice was posted to.  */  
   JournalCode:string,
      /**  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  */  
   LineType:string,
      /**   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**  The Site that the invoice is relate to.  */  
   Plant:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  External Identifier  */  
   ExternalID:string,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefInvoiceNum:string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   DepGainLoss:number,
      /**  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  */  
   DNComments:string,
      /**  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  */  
   DNCustNbr:string,
      /**   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  */  
   DebitNote:boolean,
      /**  This is populated from ShipHead.CustNum representing the Sold To customer.  */  
   SoldToCustNum:number,
      /**  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  */  
   Consolidated:boolean,
      /**  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  */  
   BillToInvoiceAddress:boolean,
      /**  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  */  
   SoldToInvoiceAddress:boolean,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm1:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm2:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm3:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm4:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm5:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate1:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate2:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate3:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate4:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate5:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales1:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales2:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales3:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales4:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales5:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit1:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit2:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit3:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit4:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit5:number,
      /**  Indicates if the Credit Memo is for a Rebate  */  
   CMType:string,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding in Customer currency  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3DepositCredit:number,
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
   Rpt1PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt2PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt3PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt1PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnpostedBal:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3DepGainLoss:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Tax point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  The last date finance/late charges have been calculated for this invoice.  */  
   LastChrgCalcDate:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Total Finance Charge amount.  */  
   TotFinChrg:number,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDiscDays:string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   PayDiscPer:string,
      /**  Blocks certain invoice from generating finance/later charge.  */  
   BlockedFinChrg:boolean,
      /**  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  */  
   BlockedFinChrgReason:string,
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
      /**  Blocks certain invoice from being printed on reminder letters.  */  
   BlockedRemLetters:boolean,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PayDiscPartPay:boolean,
      /**  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  */  
   BlockedRemLettersReason:string,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  Currency Rate Date  */  
   CurrRateDate:string,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   PIPayment:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  */  
   UseAltBillTo:boolean,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden Finland Localization field - Banking Reference  */  
   SEBankRef:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Reversal Doucment Amount  */  
   ReversalDocAmount:number,
      /**  Original Due Date at posting time  */  
   OrigDueDate:string,
      /**  The reference to CashHead.HeadNum.Used in deposit invoices  */  
   HeadNum:number,
      /**  Letter of Credit ID.  */  
   ARLOCID:string,
      /**  The free text field which can contain reference (such as Contract)  */  
   ContractRef:string,
      /**  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  */  
   OurBank:string,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  If the invoice was generated in Project Billing then it is reference to the project.  */  
   PBProjectID:string,
      /**  Deposit amount is transaction amount of deposit payment  */  
   DepositAmt:number,
      /**   Taiwan Localization
Export Bill Number  */  
   GUIExportBillNumber:string,
      /**  Deposit amount is transaction amount of deposit payment in document currency  */  
   DocDepositAmt:number,
      /**   Taiwan Localization
Date of Export  */  
   GUIDateOfExport:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt1 currency  */  
   Rpt1DepositAmt:number,
      /**   Taiwan Localization
Export Type  */  
   GUIExportType:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt2 currency  */  
   Rpt2DepositAmt:number,
      /**   Taiwan Localization
Export Mark  */  
   GUIExportMark:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt23currency  */  
   Rpt3DepositAmt:number,
      /**   Taiwan Localization
Export Bill Type  */  
   GUIExportBillType:string,
      /**  Deposit unallocated amount in base currency  */  
   DepUnallocatedAmt:number,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   SummarizationDate:string,
      /**  Deposit unallocated amount in document currency  */  
   DocDepUnallocatedAmt:number,
      /**  Date when a company bills the customer  */  
   BillingDate:string,
      /**  Deposit unallocated amount in Rpt1 currency  */  
   Rpt1DepUnallocatedAmt:number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   BillingNumber:string,
      /**  Deposit unallocated amount in Rpt2 currency  */  
   Rpt2DepUnallocatedAmt:number,
      /**  Only records ready to bill will be printed in the Billing Statement  */  
   ReadyToBill:boolean,
      /**  Deposit unallocated amount in Rpt3 currency  */  
   Rpt3DepUnallocatedAmt:number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   OvrDefTaxDate:boolean,
      /**  Cross Reference Contract Number.  */  
   XRefContractNum:string,
      /**  Cross Reference Contract Date.  */  
   XRefContractDate:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Customer Agent Name  */  
   CustAgentName:string,
      /**  Customer Agent Tax Region Number  */  
   CustAgentTaxRegNo:string,
      /**  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  */  
   ExportType:string,
      /**  Export Report Number  */  
   ExportReportNo:string,
      /**  Real Estate Number  */  
   RealEstateNo:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RevisionDate  */  
   RevisionDate:string,
      /**  RevisionNum  */  
   RevisionNum:number,
      /**  TWDeclareYear  */  
   TWDeclareYear:number,
      /**  TWDeclarePeriod  */  
   TWDeclarePeriod:number,
      /**  TWGenerationType  */  
   TWGenerationType:string,
      /**  TWGUIGroup  */  
   TWGUIGroup:string,
      /**  TWPeriodPrefix  */  
   TWPeriodPrefix:string,
      /**  Flag that indicates if the Invoice is for Central Collection.  */  
   CentralCollection:boolean,
      /**  Central Collection Doc Invoice Balance.  */  
   DocCColInvBal:number,
      /**  Sub total for invoice  */  
   SubTotal:number,
      /**  Document sub total  */  
   DocSubTotal:number,
      /**  Total tax amount from InvcTax  */  
   TaxAmt:number,
      /**  Document Total tax amount from InvcTax for Collection type 'Invoice'  */  
   DocTaxAmt:number,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  1st entry in SalesRepList  */  
   SalesRepCode1:string,
      /**  2nd entry in SalesRepList  */  
   SalesRepCode2:string,
      /**  3rd entry in SalesRepList.  */  
   SalesRepCode3:string,
      /**  4th entry in SalesRepList  */  
   SalesRepCode4:string,
      /**  5th entry in SalesRepList  */  
   SalesRepCode5:string,
      /**  Contact name  */  
   ContactName:string,
      /**  Contact fax number  */  
   ContactFaxNum:string,
      /**  Contact phone number  */  
   ContactPhoneNum:string,
      /**  Bill to address in list format.  */  
   DisplayBillAddr:string,
      /**  If true, the credit card info will come from the sales order.  */  
   UseSOCCDefaults:boolean,
      /**  Display field for the masked credit card number  */  
   DisplayCreditCardNum:string,
      /**  Currency label  */  
   XRateLabel:string,
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
      /**  Deposit credit enabled flag.  */  
   DepositCreditEnabled:boolean,
      /**  Pay schedule enabled flag  */  
   PaySchedEnabled:boolean,
      /**  Contact email address.  */  
   ContactEmailAddr:string,
      /**  InvoiceType description  */  
   InvoiceTypeDesc:string,
      /**  Document display symbol  */  
   DocDisplaySymbol:string,
      /**  Display sub total  */  
   DspSubTotal:number,
      /**  display document sub total  */  
   DspDocSubTotal:number,
      /**  Display invoice amount  */  
   DspInvoiceAmt:number,
      /**  Display document invoice amount  */  
   DspDocInvoiceAmt:number,
      /**  Pack slip number from the 1st line item.  */  
   PackSlipNum:number,
      /**  Flag to determine if UseSOCCDefaults should be enabled.  */  
   EnableSOCCDefaults:boolean,
      /**  Display invoice reference  */  
   DspInvoiceRef:number,
      /**  Flag for update of InvcHead to allow when group id is "RMACRREQ"  */  
   GenedFromRMA:boolean,
      /**  Sold to customer id  */  
   SoldToCustID:string,
      /**  Sold to customer name.  */  
   SoldToCustomerName:string,
      /**  Sold to address list.  */  
   SoldToAddressList:string,
      /**  If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   dspSoldToCustID:string,
      /**  Delimited list of available bill to customers.  */  
   AvailBTCustList:string,
      /**  Customer ID for the bill to customer (InvcHead.CustNum).  */  
   BTCustID:string,
      /**  Bill to customer name.  */  
   BTCustomerName:string,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   DispBalDN:number,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   DocDispBalDN:number,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   DNPmtAmt:number,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   DocDNPmtAmt:number,
      /**  Display Invoice Balance.  */  
   DspInvoiceBal:number,
      /**  Display document invoice balance  */  
   DspDocInvoiceBal:number,
      /**  Display Invoice Doc Rounding  */  
   DspDocRounding:number,
      /**  Display Rounding in Base  */  
   DspRounding:number,
   Rpt1DspInvoiceAmt:number,
   Rpt2DspInvoiceAmt:number,
   Rpt3DspInvoiceAmt:number,
   Rpt1DspInvoiceBal:number,
   Rpt2DspInvoiceBal:number,
   Rpt3DspInvoiceBal:number,
   Rpt1DspRounding:number,
   Rpt2DspRounding:number,
   Rpt3DspRounding:number,
   Rpt1DspSubTotal:number,
   Rpt2DspSubTotal:number,
   Rpt3DspSubTotal:number,
   Rpt1TaxAmt:number,
   Rpt2Taxamt:number,
   Rpt3TaxAmt:number,
   Rpt1SubTotal:number,
   Rpt2SubTotal:number,
   Rpt3SubTotal:number,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if a legal number configuration exists for ar invoices/credit memos  */  
   HasLegNumCnfg:boolean,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  */  
   SystemTranType:string,
      /**  This field is to display in Cash Receipt Entry the Discount Date that the payment will take.  */  
   NextDiscDate:string,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   ReminderSeq:number,
   CustAllowOTS:boolean,
   DocDspTaxAmt:number,
   DspTaxAmt:number,
   Rpt1DspTaxAmt:number,
   Rpt2DspTaxAmt:number,
   Rpt3DspTaxAmt:number,
   DisplayCurrencyID:string,
      /**  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  */  
   TransApplyDate:string,
      /**  Accumulate all reversal amounts of Credit Memos with the reference to the invoice  */  
   ReversalDocAmt:number,
      /**  It will be displayed to identify invoices automatically generated due ERS shipments.  */  
   ERSInvoice:boolean,
   TaxExchangeRate:number,
   UseTaxRate:boolean,
      /**  when InvcHead.PIPayment = O then populate ARPaymentInstrumentID with a value of PI.  */  
   ARPromNoteID:string,
      /**  Deposit balance from CashHed  */  
   DepBal:number,
      /**  Document deposit amount from cashhead.  */  
   DocDepBal:number,
   Rpt1DepBal:number,
   Rpt2DepBal:number,
   Rpt3DepBal:number,
      /**  Display deposit balance.  */  
   DspDepBal:number,
      /**  Display document deposit balance  */  
   DspDocDepBal:number,
   Rpt1DspDepBal:number,
   Rpt2DspDepBal:number,
   Rpt3DspDepBal:number,
      /**  Display deposit credit.  */  
   DspDepCr:number,
      /**  Display document deposit credit.  */  
   DspDocDepCr:number,
   Rpt1DspDepCr:number,
   Rpt2DspDepCr:number,
   Rpt3DspDepCr:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in base currency.  */  
   Vr:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in document currency.  */  
   DocVr:number,
   SATaxAmt:number,
   DocSATaxAmt:number,
   Rpt1SATaxAmt:number,
   Rpt2SATaxAmt:number,
   Rpt3SATaxAmt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt1 currency.  */  
   Rpt1Vr:number,
   WHTaxAmt:number,
   DocWHTaxAmt:number,
   Rpt1WHTaxAmt:number,
   Rpt2WHTaxAmt:number,
   Rpt3WHTaxAmt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt2 currency.  */  
   Rpt2Vr:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt3 currency.  */  
   Rpt3Vr:number,
      /**  Display advance billing amount  */  
   DspABAmt:number,
      /**  Display document advance billing amount  */  
   DspDocABAmt:number,
   Rpt1DspABAmt:number,
   Rpt2DspABAmt:number,
   Rpt3DspABAmt:number,
      /**  Total advanced billing amount.  */  
   ABAmt:number,
      /**  Document Total advanced billing amount.  */  
   DocABAmt:number,
   Rpt1ABAmt:number,
   Rpt2ABAmt:number,
   Rpt3ABAmt:number,
   CustOnCreditHold:boolean,
      /**  The flag to indicate if Invoice Header Apply Date is supposed to be Read Only  */  
   DisableAplDate:boolean,
      /**   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  */  
   RecalcAmts:string,
      /**  The credit card description. For example, American Express, Visa, Master Card, Discover, etc.  */  
   CardTypeDescription:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**  Description  */  
   CurrRateGrpDescription:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  Full description of the FOB Code.  */  
   FOBDescription:string,
      /**  Journal  Description.  */  
   JournalCodeJrnlDescription:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  IBAN Code  */  
   OurBankIBANCode:string,
      /**  Payer Reference  */  
   OurBankPayerRef:string,
      /**  Full description of the bank account.  */  
   OurBankDescription:string,
      /**  The account number for the bank account. Used for reference only.  */  
   OurBankCheckingAccount:string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   PayMethodSummarizePerCustomer:boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   PayMethodType:number,
      /**  Name of the payment method  */  
   PayMethodName:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Full description of Project Management Code.  */  
   ProjectDescription:string,
      /**  Description  */  
   TaxRateGrpDescription:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionDescription:string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   TermsCodeDescription:string,
      /**  Description  */  
   TranDocTypeDescription:string,
      /**  It indicates that this Invoice has taxes, for which the confirmation is required.  */  
   NeedConfirmTaxes:boolean,
      /**  Boolean for selection of invoices in grid  */  
   Selected:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcHeadListTableset{
   InvcHeadList:Erp_Tablesets_InvcHeadListRow[],
   InvcHeadCancellationList:Erp_Tablesets_InvcHeadCancellationListRow[],
   InvcHeadCancellationListTH:Erp_Tablesets_InvcHeadCancellationListTHRow[],
   InvcHeadTransferList:Erp_Tablesets_InvcHeadTransferListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InvcHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if invoice is "open".  */  
   OpenInvoice:boolean,
      /**  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  */  
   ClosedDate:string,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   CreditMemo:boolean,
      /**  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  */  
   UnappliedCash:boolean,
      /**   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  */  
   InvoiceSuffix:string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   InvoiceType:string,
      /**  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  */  
   DeferredRevenue:boolean,
      /**  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  */  
   OrderNum:number,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   CustNum:number,
      /**  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  */  
   PONum:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Defaults from sales order ORderHed.FOB  */  
   FOB:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  */  
   FiscalPeriod:number,
      /**  Once posted, maintenance is not allowed.  */  
   GLPosted:boolean,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnpostedBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   DocUnpostedBal:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DepositCredit:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DocDepositCredit:number,
      /**  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  */  
   SalesRepList:string,
      /**   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   InvoiceRef:number,
      /**  Value of this field is reference to invoice which has been cancelled by current invoice.  */  
   RefCancelled:number,
      /**  Value of this field is reference to invoice that cancelled this invoice.  */  
   RefCancelledBy:number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   StartUp:boolean,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDates:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   PayAmounts:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   DocPayAmounts:string,
      /**  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  */  
   PayDiscDate:string,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   PayDiscAmt:number,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   DocPayDiscAmt:number,
      /**  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  */  
   BillConNum:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  */  
   InvoiceHeld:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Journal that invoice was posted to.  */  
   JournalCode:string,
      /**  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  */  
   LineType:string,
      /**   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**  The Site that the invoice is relate to.  */  
   Plant:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  External Identifier  */  
   ExternalID:string,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefInvoiceNum:string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   DepGainLoss:number,
      /**  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  */  
   DNComments:string,
      /**  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  */  
   DNCustNbr:string,
      /**   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  */  
   DebitNote:boolean,
      /**  This is populated from ShipHead.CustNum representing the Sold To customer.  */  
   SoldToCustNum:number,
      /**  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  */  
   Consolidated:boolean,
      /**  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  */  
   BillToInvoiceAddress:boolean,
      /**  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  */  
   SoldToInvoiceAddress:boolean,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm1:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm2:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm3:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm4:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm5:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate1:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate2:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate3:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate4:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate5:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales1:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales2:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales3:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales4:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales5:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit1:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit2:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit3:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit4:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit5:number,
      /**  Indicates if the Credit Memo is for a Rebate  */  
   CMType:string,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding in Customer currency  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3DepositCredit:number,
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
   Rpt1PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt2PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt3PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt1PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnpostedBal:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3DepGainLoss:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Tax point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  The last date finance/late charges have been calculated for this invoice.  */  
   LastChrgCalcDate:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Total Finance Charge amount.  */  
   TotFinChrg:number,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDiscDays:string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   PayDiscPer:string,
      /**  Blocks certain invoice from generating finance/later charge.  */  
   BlockedFinChrg:boolean,
      /**  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  */  
   BlockedFinChrgReason:string,
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
      /**  Blocks certain invoice from being printed on reminder letters.  */  
   BlockedRemLetters:boolean,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PayDiscPartPay:boolean,
      /**  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  */  
   BlockedRemLettersReason:string,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  Currency Rate Date  */  
   CurrRateDate:string,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   PIPayment:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  */  
   UseAltBillTo:boolean,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden Finland Localization field - Banking Reference  */  
   SEBankRef:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Reversal Doucment Amount  */  
   ReversalDocAmount:number,
      /**  Original Due Date at posting time  */  
   OrigDueDate:string,
      /**  The reference to CashHead.HeadNum.Used in deposit invoices  */  
   HeadNum:number,
      /**  Letter of Credit ID.  */  
   ARLOCID:string,
      /**  The free text field which can contain reference (such as Contract)  */  
   ContractRef:string,
      /**  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  */  
   OurBank:string,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  If the invoice was generated in Project Billing then it is reference to the project.  */  
   PBProjectID:string,
      /**  Deposit amount is transaction amount of deposit payment  */  
   DepositAmt:number,
      /**   Taiwan Localization
Export Bill Number  */  
   GUIExportBillNumber:string,
      /**  Deposit amount is transaction amount of deposit payment in document currency  */  
   DocDepositAmt:number,
      /**   Taiwan Localization
Date of Export  */  
   GUIDateOfExport:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt1 currency  */  
   Rpt1DepositAmt:number,
      /**   Taiwan Localization
Export Type  */  
   GUIExportType:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt2 currency  */  
   Rpt2DepositAmt:number,
      /**   Taiwan Localization
Export Mark  */  
   GUIExportMark:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt23currency  */  
   Rpt3DepositAmt:number,
      /**   Taiwan Localization
Export Bill Type  */  
   GUIExportBillType:string,
      /**  Deposit unallocated amount in base currency  */  
   DepUnallocatedAmt:number,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   SummarizationDate:string,
      /**  Deposit unallocated amount in document currency  */  
   DocDepUnallocatedAmt:number,
      /**  Date when a company bills the customer  */  
   BillingDate:string,
      /**  Deposit unallocated amount in Rpt1 currency  */  
   Rpt1DepUnallocatedAmt:number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   BillingNumber:string,
      /**  Deposit unallocated amount in Rpt2 currency  */  
   Rpt2DepUnallocatedAmt:number,
      /**  Only records ready to bill will be printed in the Billing Statement  */  
   ReadyToBill:boolean,
      /**  Deposit unallocated amount in Rpt3 currency  */  
   Rpt3DepUnallocatedAmt:number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   OvrDefTaxDate:boolean,
      /**  Cross Reference Contract Number.  */  
   XRefContractNum:string,
      /**  Cross Reference Contract Date.  */  
   XRefContractDate:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Customer Agent Name  */  
   CustAgentName:string,
      /**  Customer Agent Tax Region Number  */  
   CustAgentTaxRegNo:string,
      /**  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  */  
   ExportType:string,
      /**  Export Report Number  */  
   ExportReportNo:string,
      /**  Real Estate Number  */  
   RealEstateNo:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
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
      /**  RecurringState  */  
   RecurringState:string,
      /**  IsRecurring  */  
   IsRecurring:boolean,
      /**  InvoiceNumList  */  
   InvoiceNumList:string,
      /**  IsAddedToGTI  */  
   IsAddedToGTI:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHISRCodeLine  */  
   CHISRCodeLine:string,
      /**  CMReason  */  
   CMReason:string,
      /**  THIsImmatAdjustment  */  
   THIsImmatAdjustment:boolean,
      /**  AGAuthorizationCode  */  
   AGAuthorizationCode:string,
      /**  AGAuthorizationDate  */  
   AGAuthorizationDate:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGDocumentLetter  */  
   AGDocumentLetter:string,
      /**  AGInvoicingPoint  */  
   AGInvoicingPoint:string,
      /**  AGLegalNumber  */  
   AGLegalNumber:string,
      /**  AGPrintingControlType  */  
   AGPrintingControlType:string,
      /**  RevisionDate  */  
   RevisionDate:string,
      /**  RevisionNum  */  
   RevisionNum:number,
      /**  TWDeclareYear  */  
   TWDeclareYear:number,
      /**  TWDeclarePeriod  */  
   TWDeclarePeriod:number,
      /**  TWGenerationType  */  
   TWGenerationType:string,
      /**  TWGUIGroup  */  
   TWGUIGroup:string,
      /**  TWPeriodPrefix  */  
   TWPeriodPrefix:string,
      /**  Indicates if the Invoice is in Collections status  */  
   InvInCollections:boolean,
      /**   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  */  
   CollectionsCust:boolean,
      /**  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  */  
   CounterARForm:number,
      /**  flag indicates if Revenue of the invoice has been already posted  */  
   PostedRecog:boolean,
      /**  Confirmation Date  */  
   CNConfirmDate:string,
      /**  MXSATSeal  */  
   MXSATSeal:string,
      /**  MXSerie  */  
   MXSerie:string,
      /**  MXTaxRcptType  */  
   MXTaxRcptType:string,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  MXTotalPayments  */  
   MXTotalPayments:number,
      /**  MXFolio  */  
   MXFolio:string,
      /**  MXCertifiedTimestamp  */  
   MXCertifiedTimestamp:string,
      /**  MXSATCertificateSN  */  
   MXSATCertificateSN:string,
      /**  MXDigitalSeal  */  
   MXDigitalSeal:string,
      /**  MXPostedTimeStamp  */  
   MXPostedTimeStamp:string,
      /**  MXCertificate  */  
   MXCertificate:string,
      /**  MXApprovalYear  */  
   MXApprovalYear:number,
      /**  MXCBB  */  
   MXCBB:string,
      /**  MXApprovalNum  */  
   MXApprovalNum:number,
      /**  MXOriginalStringTFD  */  
   MXOriginalStringTFD:string,
      /**  MXPaymentNum  */  
   MXPaymentNum:number,
      /**  MXPaidAs  */  
   MXPaidAs:string,
      /**  MXCertificateSN  */  
   MXCertificateSN:string,
      /**  MXOriginalAmount  */  
   MXOriginalAmount:number,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  MXOriginalDate  */  
   MXOriginalDate:string,
      /**  MXOriginalSeries  */  
   MXOriginalSeries:string,
      /**  MXOriginalFolio  */  
   MXOriginalFolio:string,
      /**  MXTaxRegime  */  
   MXTaxRegime:string,
      /**  MXOriginalString  */  
   MXOriginalString:string,
      /**  MXPaymentName  */  
   MXPaymentName:string,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  EInvStatus  */  
   EInvStatus:number,
      /**  EInvTimestamp  */  
   EInvTimestamp:string,
      /**  EInvUpdatedBy  */  
   EInvUpdatedBy:string,
      /**  EInvException  */  
   EInvException:string,
      /**  Flagged that this invoice has taxes which were necessary or is necessary now.  */  
   WithTaxConfirm:boolean,
      /**  UseAltBillToID  */  
   UseAltBillToID:boolean,
      /**  MXCancelledDate  */  
   MXCancelledDate:string,
      /**  Overpaid  */  
   Overpaid:boolean,
      /**  OrdExchangeRate  */  
   OrdExchangeRate:number,
      /**  PEAPPayNum  */  
   PEAPPayNum:number,
      /**  PEBankNumber  */  
   PEBankNumber:string,
      /**  PECharges  */  
   PECharges:number,
      /**  PECommissions  */  
   PECommissions:number,
      /**  PEDetTaxAmt  */  
   PEDetTaxAmt:number,
      /**  PEDetTaxCurrencyCode  */  
   PEDetTaxCurrencyCode:string,
      /**  PEDischargeAmt  */  
   PEDischargeAmt:number,
      /**  PEDischargeDate  */  
   PEDischargeDate:string,
      /**  PEInterest  */  
   PEInterest:number,
      /**  PENoPayPenalty  */  
   PENoPayPenalty:number,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   PESUNATDepAmt:number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   PESUNATDepDate:string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   PESUNATDepNum:string,
      /**  PEBOEPosted  */  
   PEBOEPosted:boolean,
      /**  DocPEInterest  */  
   DocPEInterest:number,
      /**  DocPECommissions  */  
   DocPECommissions:number,
      /**  DocPECharges  */  
   DocPECharges:number,
      /**  DocPENoPayPenalty  */  
   DocPENoPayPenalty:number,
      /**  DocPEDischargeAmt  */  
   DocPEDischargeAmt:number,
      /**  DocPEDetTaxAmt  */  
   DocPEDetTaxAmt:number,
      /**  Rpt1PEInterest  */  
   Rpt1PEInterest:number,
      /**  Rpt1PECommissions  */  
   Rpt1PECommissions:number,
      /**  Rpt1PECharges  */  
   Rpt1PECharges:number,
      /**  Rpt1PENoPayPenalty  */  
   Rpt1PENoPayPenalty:number,
      /**  Rpt1PEDischargeAmt  */  
   Rpt1PEDischargeAmt:number,
      /**  Rpt2PEInterest  */  
   Rpt2PEInterest:number,
      /**  Rpt2PECommissions  */  
   Rpt2PECommissions:number,
      /**  Rpt2PECharges  */  
   Rpt2PECharges:number,
      /**  Rpt2PENoPayPenalty  */  
   Rpt2PENoPayPenalty:number,
      /**  Rpt2PEDischargeAmt  */  
   Rpt2PEDischargeAmt:number,
      /**  Rpt3PEInterest  */  
   Rpt3PEInterest:number,
      /**  Rpt3PECommissions  */  
   Rpt3PECommissions:number,
      /**  Rpt3PECharges  */  
   Rpt3PECharges:number,
      /**  Rpt3PENoPayPenalty  */  
   Rpt3PENoPayPenalty:number,
      /**  Rpt3PEDischargeAmt  */  
   Rpt3PEDischargeAmt:number,
      /**  Our Supplier Code  */  
   OurSupplierCode:string,
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
      /**  PEGuaranteeTaxID  */  
   PEGuaranteeTaxID:string,
      /**  PEGuaranteePhoneNum  */  
   PEGuaranteePhoneNum:string,
      /**  PEBOEStatus  */  
   PEBOEStatus:string,
      /**  PEBOEIsMultiGen  */  
   PEBOEIsMultiGen:boolean,
      /**  PE Reference Document ID  */  
   PERefDocID:string,
      /**  PE Reason Code  */  
   PEReasonCode:string,
      /**  PE Reason Description  */  
   PEReasonDesc:string,
      /**  TW GUI Code Seller  */  
   TWGUIRegNumSeller:string,
      /**  TW GUI Code Buyer  */  
   TWGUIRegNumBuyer:string,
      /**  Document Name  */  
   TWGUIExportDocumentName:string,
      /**  Remarks  */  
   TWGUIExportRemarks:string,
      /**  Verification  */  
   TWGUIExportVerification:string,
      /**  PEDebitNoteReasonCode  */  
   PEDebitNoteReasonCode:string,
      /**  PEDebitNote  */  
   PEDebitNote:boolean,
      /**  MXPartPmt  */  
   MXPartPmt:boolean,
      /**  Tax Invoice Type  */  
   CNTaxInvoiceType:number,
      /**  MXExportOperationType  */  
   MXExportOperationType:string,
      /**  MXExportCustDocCode  */  
   MXExportCustDocCode:string,
      /**  MXExportCertOriginNum  */  
   MXExportCertOriginNum:string,
      /**  MXExportConfNum  */  
   MXExportConfNum:string,
      /**  MXExportCertOrigin  */  
   MXExportCertOrigin:boolean,
      /**  MXIncoterm  */  
   MXIncoterm:string,
      /**  AGDocConcept  */  
   AGDocConcept:number,
      /**  Electronic Invoice reference number  */  
   EInvRefNum:string,
      /**  Export document reference number  */  
   ExportDocRefNum:string,
      /**  Export document date  */  
   ExportDocDate:string,
      /**  Tax Transaction ID  */  
   INTaxTransactionID:string,
      /**  MXMovingReasonFlag  */  
   MXMovingReasonFlag:boolean,
      /**  MXMovingReason  */  
   MXMovingReason:string,
      /**  MXNumRegIdTrib  */  
   MXNumRegIdTrib:string,
      /**  MXResidenCountryNum  */  
   MXResidenCountryNum:number,
      /**  MXPurchaseType  */  
   MXPurchaseType:string,
      /**  MXConfirmationCode  */  
   MXConfirmationCode:string,
      /**  MXExternalCode  */  
   MXExternalCode:string,
      /**  This invoice was created via an integration with a third-party field service.  */  
   ServiceInvoice:boolean,
      /**  MXDomesticTransfer  */  
   MXDomesticTransfer:boolean,
      /**  MXCancellationMode  */  
   MXCancellationMode:string,
      /**  Shipping Port Code  */  
   INShippingPortCode:string,
      /**  Export Procedure  */  
   INExportProcedure:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  DigitalSignature  */  
   DigitalSignature:string,
      /**  SignedOn  */  
   SignedOn:string,
      /**  SignedBy  */  
   SignedBy:string,
      /**  FirstPrintDate  */  
   FirstPrintDate:string,
      /**  DocCopyNum  */  
   DocCopyNum:number,
      /**  DepositBalance  */  
   DepositBalance:number,
      /**  DocDepositBalance  */  
   DocDepositBalance:number,
      /**  Rpt1DepositBalance  */  
   Rpt1DepositBalance:number,
      /**  Rpt2DepositBalance  */  
   Rpt2DepositBalance:number,
      /**  Rpt3DepositBalance  */  
   Rpt3DepositBalance:number,
      /**  Quote number to which this invoice record is associated with.  */  
   QuoteNum:number,
      /**  The help desk case related to this invoice.  */  
   HDCaseNum:number,
      /**  Indicates that the credit hold was overridden for this invoice.  */  
   CreditOverride:boolean,
      /**  Description	Indicates that the credit hold was overridden for this invoice.	The date and time the user override the invoice credit hold.  */  
   CreditOverrideDate:string,
      /**  The user id that override the invoice credit hold.  */  
   CreditOverrideUserID:string,
      /**  Indicates the invoice is on credit hold.  Applicable to miscellaneous invoices only.  */  
   CreditHold:boolean,
      /**  Peru Electronic Invoice XML Type  */  
   PEXMLType:number,
      /**  COCreditMemoReasonCode  */  
   COCreditMemoReasonCode:string,
      /**  CODebitMemoReasonCode  */  
   CODebitMemoReasonCode:string,
      /**  COReasonDesc  */  
   COReasonDesc:string,
      /**  CODebitNote  */  
   CODebitNote:boolean,
      /**  PEDetractionTranNum  */  
   PEDetractionTranNum:number,
      /**  PEProductCode  */  
   PEProductCode:string,
      /**  PECollectionGroupID  */  
   PECollectionGroupID:string,
      /**  PE Caption Code  */  
   PECaptionCode:string,
      /**  PE Caption Code Description  */  
   PECaption:string,
      /**  PE Reference DocumentType 1  */  
   PERefDocumentType:string,
      /**  PE Reference Document Number 1  */  
   PERefDocumentNumber:string,
      /**  PE Detraction good or service code  */  
   PEDetrGoodServiceCode:string,
      /**  PE Reference DocumentType 2  */  
   PERefDocumentType2:string,
      /**  PE Reference DocumentType 3  */  
   PERefDocumentType3:string,
      /**  PE Reference DocumentType 4  */  
   PERefDocumentType4:string,
      /**  PE Reference DocumentType 5  */  
   PERefDocumentType5:string,
      /**  PE Reference Document Number 2  */  
   PERefDocumentNumber2:string,
      /**  PE Reference Document Number 3  */  
   PERefDocumentNumber3:string,
      /**  PE Reference Document Number 4  */  
   PERefDocumentNumber4:string,
      /**  PE Reference Document Number 5  */  
   PERefDocumentNumber5:string,
      /**  E-invoice  */  
   ELIEInvoice:boolean,
      /**  Status of E-invoice (1 - Open, 2 - Generated, 3 - Sent, 4 - Error).  */  
   ELIEInvStatus:number,
      /**  User Id of the person generated E-invoice.  */  
   ELIEInvUpdatedBy:string,
      /**  E-invoice error description.  */  
   ELIEInvException:string,
      /**  Date and Time of E-invoice generation.  */  
   ELIEInvUpdatedOn:string,
      /**  COOperType  */  
   COOperType:string,
      /**  Flag that indicates if the Invoice is for Central Collection.  */  
   CentralCollection:boolean,
      /**  Company that created this invoice.  */  
   CColChildCompany:string,
      /**  Central Collection company.  */  
   CColParentCompany:string,
      /**  Order number on the invoicing company.  */  
   CColOrderNum:number,
      /**  Invoice number on the invoicing company.  */  
   CColChildInvoiceNum:number,
      /**  Invoice number on central collection company  */  
   CColInvoiceNum:number,
      /**  Legal number on the invoicing company invoice.  */  
   CColChildLegalNumber:string,
      /**  Legal number on central collection company.  */  
   CColLegalNumber:string,
      /**  Invoice reference on the Invoicing Company.  */  
   CColInvoiceRef:number,
      /**  Invoice Balance in the Central Collection company.  */  
   CColInvBal:number,
      /**  Central Collection Doc Invoice Balance.  */  
   DocCColInvBal:number,
      /**  Invoice Amount on the Invoicing Company.  */  
   CColInvAmt:number,
      /**  Invoice Amount on the Invoicing Company.  */  
   DocCColInvAmt:number,
      /**  Rpt 1 Parent Invoice Balance  */  
   Rpt1CColInvBal:number,
      /**  Rpt 2 Parent Invoice Balance  */  
   Rpt2CColInvBal:number,
      /**  Rpt 3 Parent Invoice Balance  */  
   Rpt3CColInvBal:number,
      /**  Rpt 1 Child Invoice Amount  */  
   Rpt1CColInvAmt:number,
      /**  Rpt 2 Child Invoice Amount  */  
   Rpt2CColInvAmt:number,
      /**  Rpt 3 Child Invoice Amount  */  
   Rpt3CColInvAmt:number,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  User terminal name  */  
   ELIEInvTerminalName:string,
      /**  User terminal IP  */  
   ELIEInvTerminalIP:string,
      /**  GL Description  */  
   Description:string,
      /**  WithholdAcctToInterim  */  
   WithholdAcctToInterim:boolean,
      /**  Indicates if the Central Collection parent invoice is open.  */  
   CColOpenInvoice:boolean,
      /**  AGQRCodeData  */  
   AGQRCodeData:string,
      /**  Exempt Reason Code  */  
   ExemptReasonCode:string,
      /**  EInvoice ID  */  
   ELIEInvID:string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   CallNum:number,
      /**  this is a link to the service call line that this invoice is for.  Linetype = "CALL"  */  
   CallLine:number,
      /**  Associates the Call Line record back its linked jobnum  */  
   JobNum:string,
      /**  MXCancelReasonCode  */  
   MXCancelReasonCode:string,
      /**  MXSubstInvoiceNum  */  
   MXSubstInvoiceNum:number,
      /**  MXExportType  */  
   MXExportType:string,
      /**  MXGlobalInvoicePeriod  */  
   MXGlobalInvoicePeriod:string,
      /**  MXGlobalInvoiceMonth  */  
   MXGlobalInvoiceMonth:string,
      /**  ELIEInvServiceProviderStatus  */  
   ELIEInvServiceProviderStatus:number,
      /**  Incoterm Code  */  
   IncotermCode:string,
      /**  Incoterm Location  */  
   IncotermLocation:string,
      /**  CovenantDiscPercent  */  
   CovenantDiscPercent:number,
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
      /**  Total advanced billing amount.  */  
   ABAmt:number,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  ARPNHead's HeadNum  */  
   ARPNHeadNum:number,
      /**  when InvcHead.PIPayment = O then populate ARPaymentInstrumentID with a value of PI.  */  
   ARPromNoteID:string,
      /**  Auto generate payment instruments  */  
   AutoGenPN:boolean,
      /**  Delimited list of available bill to customers.  */  
   AvailBTCustList:string,
      /**  Used for Bill of Exchange.  Indicates the bank to use when a payment instrument for the invoice is created.  */  
   BankForPI:string,
   BankForPIName:string,
      /**  Customer ID for the bill to customer (InvcHead.CustNum).  */  
   BTCustID:string,
      /**  Bill to customer name.  */  
   BTCustomerName:string,
      /**  The date and time that the record was last changed  */  
   ChangeDateTime:string,
   CNGTIAction:string,
   CNGTIAddress:string,
   CNGTIBankAccount:string,
   CNGTIComment:string,
   CNGTICustomerName:string,
   CNGTIExportAddress:string,
      /**  CSF China, Gross Invoice Amount  */  
   CNGTIGrossInvcAmt:number,
      /**  CSF China, Total invoice amount = InvcHead.InvoiceAmt - InvcHead.WithholdAmt  */  
   CNGTIInvoiceAmt:number,
   CNGTINote:string,
   CNGTIShipToNum:string,
   CNGTIStatus1:string,
   CNGTIStatus2:boolean,
   CNGTITaxCode:string,
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
      /**  Indicates if Invoice is in Collections (Peru localization)  */  
   CollectionsInv:boolean,
      /**  Contact email address.  */  
   ContactEmailAddr:string,
      /**  Contact fax number  */  
   ContactFaxNum:string,
      /**  Contact name  */  
   ContactName:string,
      /**  Contact phone number  */  
   ContactPhoneNum:string,
      /**  record converted from deposit  */  
   ConvertedFromDep:boolean,
   COOperTypeDesc:string,
      /**  True if the Country set for the current company contains an Intrastat code.  */  
   CountryIntrastat:boolean,
   CumulativeBalance:number,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
   CurrentInstanceNum:number,
   CustAllowOTS:boolean,
   CustOnCreditHold:boolean,
      /**  Deposit balance from CashHed  */  
   DepBal:number,
      /**  Deposit credit enabled flag.  */  
   DepositCreditEnabled:boolean,
   DirectDebiting:boolean,
      /**  The flag to indicate if Invoice Header Apply Date is supposed to be Read Only  */  
   DisableAplDate:boolean,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   DispBalDN:number,
      /**  Bill to address in list format.  */  
   DisplayBillAddr:string,
      /**  Display field for the masked credit card number  */  
   DisplayCreditCardNum:string,
   DisplayCurrencyID:string,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   DNPmtAmt:number,
      /**  Document Total advanced billing amount.  */  
   DocABAmt:number,
      /**  Financial Charge  */  
   DocCOIFRSFinancialCharge:number,
      /**  Present Value  */  
   DocCOIFRSPresentValue:number,
   DocCumulativeBalance:number,
      /**  Document deposit amount from cashhead.  */  
   DocDepBal:number,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   DocDispBalDN:number,
      /**  Document display symbol  */  
   DocDisplaySymbol:string,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   DocDNPmtAmt:number,
   DocDspPrepDeposit:number,
   DocDspTaxAmt:number,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   DocPESUNATDepAmt:number,
   DocRemainTaxAmt:number,
   DocReverseTaxAmt:number,
   DocSATaxAmt:number,
   DocSourceRecurBalance:number,
      /**  Document sub total  */  
   DocSubTotal:number,
      /**  Document Total tax amount from InvcTax for Collection type 'Invoice'  */  
   DocTaxAmt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in document currency.  */  
   DocVr:number,
   DocWHTaxAmt:number,
      /**  Display advance billing amount  */  
   DspABAmt:number,
      /**  Display deposit balance.  */  
   DspDepBal:number,
      /**  Display deposit credit.  */  
   DspDepCr:number,
   DspDigitalSignature:string,
      /**  Display document advance billing amount  */  
   DspDocABAmt:number,
      /**  Display document deposit balance  */  
   DspDocDepBal:number,
      /**  Display document deposit credit.  */  
   DspDocDepCr:number,
      /**  Display document invoice amount  */  
   DspDocInvoiceAmt:number,
      /**  Display document invoice balance  */  
   DspDocInvoiceBal:number,
      /**  Display Invoice Doc Rounding  */  
   DspDocRounding:number,
      /**  display document sub total  */  
   DspDocSubTotal:number,
      /**  Display invoice amount  */  
   DspInvoiceAmt:number,
      /**  Display Invoice Balance.  */  
   DspInvoiceBal:number,
      /**  Display invoice reference  */  
   DspInvoiceRef:number,
   DspPayDiscDays:string,
   DspPrepDeposit:number,
      /**  Display Rounding in Base  */  
   DspRounding:number,
      /**  If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   dspSoldToCustID:string,
      /**  Display sub total  */  
   DspSubTotal:number,
   DspTaxAmt:number,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
   EnableCentralCollection:boolean,
      /**  Flag to determine if UseSOCCDefaults should be enabled.  */  
   EnableSOCCDefaults:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  It will be displayed to identify invoices automatically generated due ERS shipments.  */  
   ERSInvoice:boolean,
      /**  Indicates which date to be used to calculate the exchange rate, I for Invoice Date, A for Apply Date.  */  
   ExchangeRateDate:string,
      /**  Flag for update of InvcHead to allow when group id is "RMACRREQ"  */  
   GenedFromRMA:boolean,
      /**  CustBank record exists for customer  */  
   HasBank:boolean,
      /**  Indicates if a legal number configuration exists for ar invoices/credit memos  */  
   HasLegNumCnfg:boolean,
      /**  In case if Invoice Header Tax Liability is not assigned this flag indicates if any of Invoice lines has Tax inclusive Tax Liability assinged  */  
   InPriceLn:boolean,
      /**  Integration invoice type.  Used for setting of InvoiceType.  */  
   IntInvoiceType:string,
      /**  InvoiceType description  */  
   InvoiceTypeDesc:string,
      /**  Denmark localization external field  */  
   IsDK:boolean,
      /**  Set to true if intrastat is enabled.  */  
   IsIntrastatSensitive:boolean,
   IsLatestRecurrence:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Indicates if the UR Invoice was created from an On Account PI instead of an on account cash receipt.  */  
   IsPIUnappliedReceipt:boolean,
   IsPMForGenPIType:boolean,
   LatestInvoice:number,
      /**  Stores the message when a legal number is generated.  */  
   LegalNumberMessage:string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  MXCancellationID  */  
   MXCancellationID:string,
      /**  MXCancellationStatus  */  
   MXCancellationStatus:string,
      /**  It indicates that this Invoice has taxes, for which the confirmation is required.  */  
   NeedConfirmTaxes:boolean,
      /**  This field is to display in Cash Receipt Entry the Discount Date that the payment will take.  */  
   NextDiscDate:string,
      /**  NextInvoiceDate = InvcRecurringCycle.LastDate + RecurringCycle.Interval in RecurringCycle.Modifier units  */  
   NextInvoiceDate:string,
      /**  Pack slip number from the 1st line item.  */  
   PackSlipNum:number,
      /**  Pay schedule enabled flag  */  
   PaySchedEnabled:boolean,
      /**  Indicates what the user will change the status to  */  
   PEBOEChangeStatusTo:string,
   PEBOEStatusDesc:string,
      /**  Peru CSF: Collections date  */  
   PECollectionsDate:string,
      /**  PE Detraction good or service code description  */  
   PEDetrGoodServiceCodeDesc:string,
   PEDspCurrencySymbol:string,
      /**  Peru CSF: No if the invoice is moved out of collections, Yes if the invoice is moved into colletions.  */  
   PEInCollections:boolean,
      /**  PE Document Type Description  */  
   PERefDocumentTypeDesc:string,
      /**  PE Document Type Description 2  */  
   PERefDocumentTypeDesc2:string,
      /**  PE Document Type Description 3  */  
   PERefDocumentTypeDesc3:string,
      /**  PE Document Type Description 4  */  
   PERefDocumentTypeDesc4:string,
      /**  PE Document Type Description 5  */  
   PERefDocumentTypeDesc5:string,
      /**  PI - Bank account  */  
   PIBankAcctID:string,
      /**  PI Customer bank required  */  
   PICustBankDtl:boolean,
      /**  PI Initiation - generated or received  */  
   PIInitiation:string,
      /**  Prep Deposit enabled flag.  */  
   PrepDepositEnabled:boolean,
      /**  The description of the proposed Tax Region  */  
   ProposedTaxRgn:string,
      /**   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  */  
   RecalcAmts:string,
      /**  Recurring flag  */  
   Recurring:boolean,
   RemainTaxAmt:number,
   ReminderSeq:number,
      /**  Accumulate all reversal amounts of Credit Memos with the reference to the invoice  */  
   ReversalDocAmt:number,
   ReverseTaxAmt:number,
   Rpt1ABAmt:number,
      /**  Financial Charge  */  
   Rpt1COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt1COIFRSPresentValue:number,
   Rpt1CumulativeBalance:number,
   Rpt1DepBal:number,
   Rpt1DspABAmt:number,
   Rpt1DspDepBal:number,
   Rpt1DspDepCr:number,
   Rpt1DspInvoiceAmt:number,
   Rpt1DspInvoiceBal:number,
   Rpt1DspPrepDeposit:number,
   Rpt1DspRounding:number,
   Rpt1DspSubTotal:number,
   Rpt1DspTaxAmt:number,
   Rpt1RemainTaxAmt:number,
   Rpt1ReverseTaxAmt:number,
   Rpt1SATaxAmt:number,
   Rpt1SourceRecurBalance:number,
   Rpt1SubTotal:number,
   Rpt1TaxAmt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt1 currency.  */  
   Rpt1Vr:number,
   Rpt1WHTaxAmt:number,
   Rpt2ABAmt:number,
      /**  Financial Charge  */  
   Rpt2COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt2COIFRSPresentValue:number,
   Rpt2CumulativeBalance:number,
   Rpt2DepBal:number,
   Rpt2DspABAmt:number,
   Rpt2DspDepBal:number,
   Rpt2DspDepCr:number,
   Rpt2DspInvoiceAmt:number,
   Rpt2DspInvoiceBal:number,
   Rpt2DspPrepDeposit:number,
   Rpt2DspRounding:number,
   Rpt2DspSubTotal:number,
   Rpt2DspTaxAmt:number,
   Rpt2RemainTaxAmt:number,
   Rpt2ReverseTaxAmt:number,
   Rpt2SATaxAmt:number,
   Rpt2SourceRecurBalance:number,
   Rpt2SubTotal:number,
   Rpt2Taxamt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt2 currency.  */  
   Rpt2Vr:number,
   Rpt2WHTaxAmt:number,
   Rpt3ABAmt:number,
      /**  Financial Charge  */  
   Rpt3COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt3COIFRSPresentValue:number,
   Rpt3CumulativeBalance:number,
   Rpt3DepBal:number,
   Rpt3DspABAmt:number,
   Rpt3DspDepBal:number,
   Rpt3DspDepCr:number,
   Rpt3DspInvoiceAmt:number,
   Rpt3DspInvoiceBal:number,
   Rpt3DspPrepDeposit:number,
   Rpt3DspRounding:number,
   Rpt3DspSubTotal:number,
   Rpt3DspTaxAmt:number,
   Rpt3RemainTaxAmt:number,
   Rpt3ReverseTaxAmt:number,
   Rpt3SATaxAmt:number,
   Rpt3SourceRecurBalance:number,
   Rpt3SubTotal:number,
   Rpt3TaxAmt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt3 currency.  */  
   Rpt3Vr:number,
   Rpt3WHTaxAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  1st entry in SalesRepList  */  
   SalesRepCode1:string,
      /**  2nd entry in SalesRepList  */  
   SalesRepCode2:string,
      /**  3rd entry in SalesRepList.  */  
   SalesRepCode3:string,
      /**  4th entry in SalesRepList  */  
   SalesRepCode4:string,
      /**  5th entry in SalesRepList  */  
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
   SATaxAmt:number,
      /**  Boolean for selection of invoices in grid  */  
   Selected:boolean,
   SkipRecurring:boolean,
      /**  Sold to address list.  */  
   SoldToAddressList:string,
      /**  Sold to customer id  */  
   SoldToCustID:string,
      /**  Sold to customer name.  */  
   SoldToCustomerName:string,
   SourceInvoiceNum:number,
   SourceLastDate:string,
   SourceRecurBalance:number,
      /**  Sub total for invoice  */  
   SubTotal:number,
      /**  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  */  
   SystemTranType:string,
      /**  Total tax amount from InvcTax  */  
   TaxAmt:number,
   TaxExchangeRate:number,
      /**  The flag to indicate if the user is supposed to be asked about Tax Liability change  */  
   TaxRgnLineChange:boolean,
   TotalInstanceNum:number,
      /**  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  */  
   TransApplyDate:string,
      /**  If true, the credit card info will come from the sales order.  */  
   UseSOCCDefaults:boolean,
   UseTaxRate:boolean,
   VNInvDescription:string,
   VNInvoiceType:string,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in base currency.  */  
   Vr:number,
   WHTaxAmt:number,
      /**  Currency label  */  
   XRateLabel:string,
   zEnableCreditHold:boolean,
      /**  The number of days the invoice is past due.  */  
   AgingDays:number,
      /**   The list of prohibited statuses.for the Invoice
For examle, if contains 2 (EINVOICE_STATUS_GENERATED) then Generate E-invoice is not allowed.
if contains 2 (EINVOICE_STATUS_SENT) then Sending Invoice via Service provider is not allowed  */  
   ELIEInvProhibitedStatuses:string,
      /**  Flag indicating whether to enable Incoterm Location  */  
   EnableIncotermLocation:boolean,
   BitFlag:number,
   AGInvoicingPointDescription:string,
   ARSystLNReqForInvc:boolean,
   CardTypeDescription:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrRateGrpDescription:string,
   CustomerInactive:boolean,
   CustomerMXGeneralPublic:boolean,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerName:string,
   CustomerELISendingOption:number,
   FOBDescription:string,
   IncotermsDescription:string,
   JournalCodeJrnlDescription:string,
   MXPurchaseTypeCodeDesc:string,
   MXSubstInvoiceMXFiscalFolio:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   OurBankPayerRef:string,
   OurBankBankIdentifier:string,
   OurBankTypeCode:string,
   OurBankBankAcctID:string,
   OurBankCheckingAccount:string,
   OurBankBankName:string,
   OurBankIBANCode:string,
   OurBankLocalBIC:string,
   OurBankDescription:string,
   PayMethodName:string,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodType:number,
   PlantName:string,
   ProjectDescription:string,
   RecurringCycleMaximumValue:boolean,
   SoldToCustNumInactive:boolean,
   SoldToCustNumCustID:string,
   SoldToCustNumName:string,
   TaxRateGrpDescription:string,
   TaxRegionDescription:string,
   TermsCodeDescription:string,
   TranDocTypeDescription:string,
   XbSystOCRCalcType:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcHeadTransferListRow{
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates the type of document. Yes = credit memo, No = Invoice. This value can't be cahgned after the record has been created. Credit memos affect the way detail quantities and amounts are stored in the database. They will always be sotred with a negative sign but will be entered as positive.  */  
   CreditMemo:boolean,
      /**  CurrencyCode  */  
   CurrencyCode:string,
      /**  A user defined external customer ID. This must be unique within the file. This ID may be used in certain screen displays or reports wehre a full customer name is nappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change it. This change is allowed because the system i snot using the Cust ID as a foreign key in any other file. Rather, it uses the CustNum field.  */  
   CustomerCustID:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records. This field has a positive  sign (credit memos are negative).  */  
   InvoiceAmt:number,
      /**  Invoice date is copied from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  Invoices thata are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld= false. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted. The manufacturing system sets this flag when creating invoices for order line items which had been flagged for "Time & material invoiceing" (OrderDtl.TMBilling).  */  
   InvoiceHeld:boolean,
      /**  If this field is left blank the system assigns teh next available number on the file or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  There are four types of invoices: "Shp" = invoice shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments and "Mis" = Miscellaneous. The setting of this field affects invoice entry.  */  
   InvoiceType:string,
      /**  The legal number for the record. This number is created based on the setup parameters in the LegalNumber table.  */  
   LegalNumber:string,
      /**  Preserves the Selected satus of the rows.  */  
   SelectedForAction:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtARInvSearchTableset{
   InvcHead:Erp_Tablesets_InvcHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param invoiceNum
      @param maxNumOfCards
   */  
export interface GetARInvoiceRelationshipMap_input{
   invoiceNum:number,
   maxNumOfCards:number,
}

export interface GetARInvoiceRelationshipMap_output{
   returnObj:string,
}

   /** Required : 
      @param invoiceNum
   */  
export interface GetByID_input{
   invoiceNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ARInvSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ARInvSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ARInvSearchTableset[],
}

   /** Required : 
      @param ipOrderNum
   */  
export interface GetInvoicesByOrder_input{
      /**  The order number used to retrieve invoices.  */  
   ipOrderNum:number,
}

export interface GetInvoicesByOrder_output{
   returnObj:Erp_Tablesets_ARInvSearchTableset[],
}

   /** Required : 
      @param invcHeadWhereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListARTaxConfirmSearch_input{
      /**  Whereclause for invcHead table.  */  
   invcHeadWhereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListARTaxConfirmSearch_output{
   returnObj:Erp_Tablesets_ARInvSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param IPCurrentGrpID
      @param InvcHeadWhereClause
      @param PageSize
      @param AbsolutePage
   */  
export interface GetListBOEReferences_input{
   IPCurrentGrpID:string,
   InvcHeadWhereClause:string,
   PageSize:number,
   AbsolutePage:number,
}

export interface GetListBOEReferences_output{
   returnObj:Erp_Tablesets_InvcHeadListTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
}
}

   /** Required : 
      @param caea
      @param year
      @param month
      @param fortnight
   */  
export interface GetListForAGCAEA_input{
   caea:string,
   year:number,
   month:number,
   fortnight:number,
}

export interface GetListForAGCAEA_output{
   returnObj:Erp_Tablesets_ARInvSearchTableset[],
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
   returnObj:Erp_Tablesets_InvcHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewInvcHead_input{
   ds:Erp_Tablesets_ARInvSearchTableset[],
}

export interface GetNewInvcHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvSearchTableset[],
}
}

   /** Required : 
      @param ipcurrentGrpID
      @param whereClause
   */  
export interface GetRefInvoicesForBOE_input{
      /**  Current Group ID  */  
   ipcurrentGrpID:string,
      /**  Where clause for Cash Receipt.  */  
   whereClause:string,
}

export interface GetRefInvoicesForBOE_output{
   returnObj:Erp_Tablesets_InvcHeadListTableset[],
}

   /** Required : 
      @param whereClauseInvcHead
      @param groupID
      @param headNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForCashReceipt_input{
   whereClauseInvcHead:string,
   groupID:string,
   headNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForCashReceipt_output{
   returnObj:Erp_Tablesets_ARInvSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseInvcHead
      @param quoteNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForQuote_input{
   whereClauseInvcHead:string,
   quoteNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForQuote_output{
   returnObj:Erp_Tablesets_ARInvSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseInvcHead
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseInvcHead:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ARInvSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtARInvSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtARInvSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ARInvSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvSearchTableset[],
}
}

