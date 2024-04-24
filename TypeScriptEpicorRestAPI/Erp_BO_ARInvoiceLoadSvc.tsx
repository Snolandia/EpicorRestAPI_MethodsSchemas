import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ARInvoiceLoadSvc
// Description: ARInvoiceLoadSvc Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/$metadata", {
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
   Description: Get ARInvoiceLoads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARInvoiceLoads
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARInvoiceLoadRow
   */  
export function get_ARInvoiceLoads(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARInvoiceLoadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/ARInvoiceLoads", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARInvoiceLoadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARInvoiceLoads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARInvoiceLoadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARInvoiceLoadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARInvoiceLoads(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/ARInvoiceLoads", {
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
   Summary: Calls GetByID to retrieve the ARInvoiceLoad item
   Description: Calls GetByID to retrieve the ARInvoiceLoad item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARInvoiceLoad
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARInvoiceLoadRow
   */  
export function get_ARInvoiceLoads_Company_InvoiceNum(Company:string, InvoiceNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARInvoiceLoadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/ARInvoiceLoads(" + Company + "," + InvoiceNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ARInvoiceLoadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARInvoiceLoad for the service
   Description: Calls UpdateExt to update ARInvoiceLoad. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARInvoiceLoad
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARInvoiceLoadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARInvoiceLoads_Company_InvoiceNum(Company:string, InvoiceNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/ARInvoiceLoads(" + Company + "," + InvoiceNum + ")", {
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
   Summary: Call UpdateExt to delete ARInvoiceLoad item
   Description: Call UpdateExt to delete ARInvoiceLoad item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARInvoiceLoad
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARInvoiceLoads_Company_InvoiceNum(Company:string, InvoiceNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/ARInvoiceLoads(" + Company + "," + InvoiceNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARInvoiceLoadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARInvoiceLoadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARInvoiceLoadListRow)
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
export function get_GetRows(whereClauseARInvoiceLoad:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseARInvoiceLoad!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARInvoiceLoad=" + whereClauseARInvoiceLoad
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/GetRows" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/GetList" + params, {
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
   Summary: Invoke method AnotherInvoice
   Description: Gets another invoice with the same customer and customer defaults..
   OperationID: AnotherInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AnotherInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AnotherInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AnotherInvoice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/AnotherInvoice", {
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
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyBase(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/GetCurrencyBase", {
          method: 'post',
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
   Summary: Invoke method GetTaxTypesList
   Description: Get where clause to select tax types, related to specified Tax Liability
   OperationID: GetTaxTypesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxTypesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxTypesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxTypesList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/GetTaxTypesList", {
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
   Summary: Invoke method GetTotals
   Description: Gets the total base invoice amount for invoices available for posting.
   OperationID: GetTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTotals(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/GetTotals", {
          method: 'post',
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
   Summary: Invoke method OnChangeofApplyDate
   Description: Called when the ApplyDate field changes. Validates the ApplyDate field.
Updates the FiscalPeriod and FiscalYear fields.
   OperationID: OnChangeofApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofApplyDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofApplyDate", {
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
   Summary: Invoke method OnChangeofCreditMemo
   Description: Called when the CreditMemo field changes.  Reverses the sign of
the InvoiceBal and DocInvoiceBal fields.
   OperationID: OnChangeofCreditMemo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofCreditMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofCreditMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofCreditMemo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofCreditMemo", {
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
   Summary: Invoke method OnChangeofCurrencyCode
   Description: Called when the currency code changes.  Gets the new currency information.
Gets the xrate label and currency symbol. Recalc the DocInvoiceBal.
   OperationID: OnChangeofCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofCurrencyCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofCurrencyCode", {
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
   Summary: Invoke method OnChangeofCustomer
   Description: Gets new defaults from the Customer table.
   OperationID: OnChangeofCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofCustomer", {
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
   Summary: Invoke method OnChangeofDispInvoiceBal
   Description: Called when the DispInvoiceBal field is changed.
Updates the InvoiceBal, DocInvoiceBal, DispInvoiceBal and DocDispInvoiceBal
fields.
   OperationID: OnChangeofDispInvoiceBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofDispInvoiceBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofDispInvoiceBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofDispInvoiceBal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofDispInvoiceBal", {
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
   Summary: Invoke method OnChangeofDocDispInvoiceBal
   Description: Called when the DocDispInvoiceBal field is changed.
Updates the InvoiceBal, DocInvoiceBal, DispInvoiceBal and DocDispInvoiceBal
fields.
   OperationID: OnChangeofDocDispInvoiceBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofDocDispInvoiceBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofDocDispInvoiceBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofDocDispInvoiceBal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofDocDispInvoiceBal", {
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
   Summary: Invoke method OnChangeofDocInvoiceBal
   Description: Called when the DocInvoiceBal field is changed.
Updates the InvoiceBal, DocInvoiceBal, DispInvoiceBal, DocDispInvoiceBal
and CreditMemo fields.
   OperationID: OnChangeofDocInvoiceBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofDocInvoiceBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofDocInvoiceBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofDocInvoiceBal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofDocInvoiceBal", {
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
   Summary: Invoke method OnChangeofExchangeRate
   Description: Called when the ExchangeRate field changes. Updates the balance fields.
   OperationID: OnChangeofExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofExchangeRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofExchangeRate", {
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
   Summary: Invoke method OnChangeofFiscalPeriod
   Description: Called when the FiscalPeriod field is changed. Validates the FiscalPeriod
field.
   OperationID: OnChangeofFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofFiscalPeriod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofFiscalPeriod", {
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
   Summary: Invoke method OnChangeofFiscalYear
   Description: Called when the FiscalYear field changes. Validates the FiscalYear field.
   OperationID: OnChangeofFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofFiscalYear(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofFiscalYear", {
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
   Summary: Invoke method OnChangeofInvoiceBal
   Description: Called when the InvoiceBal field is changed.
Updates the InvoiceBal, DocInvoiceBal, DispInvoiceBal, DocDispInvoiceBal
and CreditMemo fields.
   OperationID: OnChangeofInvoiceBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofInvoiceBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofInvoiceBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofInvoiceBal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofInvoiceBal", {
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
   Summary: Invoke method OnChangeofInvoiceDate
   Description: Called when the InvoiceDate field changes. Validates the InvoiceDate field.
Updates the FiscalPeriod and FiscalYear fields and gets the correct exchange
rate.
   OperationID: OnChangeofInvoiceDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofInvoiceDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofInvoiceDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofInvoiceDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofInvoiceDate", {
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
   Summary: Invoke method OnChangeofTaxRegionCode
   Description: Called when the Tax Region Code gets changed, so the list for the tax codes
get automatically updatedTaxRgn taxRgn = this.FindFirstTaxRgn(Session.CompanyID, taxRegionCode);
   OperationID: OnChangeofTaxRegionCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofTaxRegionCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofTaxRegionCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofTaxRegionCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangeofTaxRegionCode", {
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
   Summary: Invoke method OnChangingofTax
   Description: Called when the Tax Type or Tax Rate field changes.
   OperationID: OnChangingofTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingofTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingofTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingofTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/OnChangingofTax", {
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
   Summary: Invoke method PostInvoices
   Description: Sets the posted flag on the InvcHead records.  The OK to post flag is used to
determine what to do under certain circumstances.
   OperationID: PostInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostInvoices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/PostInvoices", {
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
   Summary: Invoke method CheckforPostInvoices
   Description: Please don't use it, use CheckBeforePosting() instead
   OperationID: CheckforPostInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckforPostInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckforPostInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckforPostInvoices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/CheckforPostInvoices", {
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
   Summary: Invoke method CheckBeforePosting
   Description: Validate if GL License is available and StartUp group is created.
   OperationID: CheckBeforePosting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforePosting_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBeforePosting(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/CheckBeforePosting", {
          method: 'post',
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
   Summary: Invoke method GetNewARInvoiceLoad
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARInvoiceLoad
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARInvoiceLoad_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARInvoiceLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARInvoiceLoad(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/GetNewARInvoiceLoad", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARInvoiceLoadSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARInvoiceLoadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARInvoiceLoadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARInvoiceLoadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARInvoiceLoadRow[],
}

export interface Erp_Tablesets_ARInvoiceLoadListRow{
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
      /**  LegalNumber year.  */  
   "LegalNumberYear":number,
      /**  Legal Number Prefix List  */  
   "LegalNumberPrefixList":string,
      /**  Customer ID  */  
   "CustID":string,
      /**  Invoice balance in base currency  */  
   "BaseInvBal":number,
      /**  Legal number prefix  */  
   "LegalNumberPrefix":string,
      /**  Legal number number  */  
   "LegalNumberNumber":string,
      /**  Legal number read only fields  */  
   "LegalNumberReadOnlyFields":string,
      /**  Currency rate type  (ex: USD > GBP)  */  
   "CurrencyRateType":string,
      /**  Currency code symbol  */  
   "CurrencyCodeSymbol":string,
      /**  store invoice balance for after update.  */  
   "TempInvoiceBal":number,
      /**  Temporary doc invoice balance for after update.  */  
   "TempDocInvoiceBal":number,
      /**  flag for use of legal numbers  */  
   "UseLegalNumbers":boolean,
      /**  Document currency symbol  */  
   "DocCurrencyCodeSymbol":string,
      /**  Display field for InvoiceBal  */  
   "DispInvoiceBal":number,
      /**  Display field for DocInvoiceBal  */  
   "DocDispInvoiceBal":number,
   "Rpt1DispInvoiceBal":number,
   "Rpt2DispInvoiceBal":number,
   "Rpt3DispInvoiceBal":number,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  Description  */  
   "RateGrpCodeDescription":string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   "TermsCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARInvoiceLoadRow{
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
      /**  Invoice balance in base currency  */  
   "BaseInvBal":number,
      /**  Currency rate type  (ex: USD > GBP)  */  
   "CurrencyRateType":string,
      /**  DocInCovenantDiscount  */  
   "DocInCovenantDiscount":number,
      /**  Display field for DocInvoiceBal  */  
   "DocDispInvoiceBal":number,
      /**  Rpt1InCovenantDiscount  */  
   "Rpt1InCovenantDiscount":number,
      /**  Rpt2InCovenantDiscount  */  
   "Rpt2InCovenantDiscount":number,
      /**  Legal number number  */  
   "LegalNumberNumber":string,
      /**  Legal number prefix  */  
   "LegalNumberPrefix":string,
      /**  Rpt3InCovenantDiscount  */  
   "Rpt3InCovenantDiscount":number,
      /**  Legal Number Prefix List  */  
   "LegalNumberPrefixList":string,
      /**  Legal number read only fields  */  
   "LegalNumberReadOnlyFields":string,
      /**  LegalNumber year.  */  
   "LegalNumberYear":number,
   "Rpt1DispInvoiceBal":number,
   "Rpt2DispInvoiceBal":number,
   "Rpt3DispInvoiceBal":number,
      /**  Taxable Value 1  */  
   "TaxableAmt1":number,
      /**  Tax Value 2  */  
   "TaxAmt2":number,
      /**  Tax Value 3  */  
   "TaxAmt3":number,
      /**  Tax Value 4  */  
   "TaxAmt4":number,
      /**  Tax Type 1  */  
   "TaxCode1":string,
   "TaxCode1Description":string,
      /**  Tax Type 2  */  
   "TaxCode2":string,
   "TaxCode2Description":string,
      /**  Tax Type 3  */  
   "TaxCode3":string,
   "TaxCode3Description":string,
      /**  Tax Type 4  */  
   "TaxCode4":string,
   "TaxCode4Description":string,
      /**  Tax Rate 1  */  
   "TaxRate1":string,
   "TaxRate1Description":string,
      /**  Tax Rate 2  */  
   "TaxRate2":string,
   "TaxRate2Description":string,
      /**  Tax Rate 3  */  
   "TaxRate3":string,
   "TaxRate3Description":string,
      /**  Tax Rate 4  */  
   "TaxRate4":string,
   "TaxRate4Description":string,
      /**  Temporary doc invoice balance for after update.  */  
   "TempDocInvoiceBal":number,
      /**  store invoice balance for after update.  */  
   "TempInvoiceBal":number,
      /**  flag for use of legal numbers  */  
   "UseLegalNumbers":boolean,
      /**  Currency code symbol  */  
   "CurrencyCodeSymbol":string,
      /**  Customer ID  */  
   "CustID":string,
      /**  Display field for InvoiceBal  */  
   "DispInvoiceBal":number,
      /**  Document currency symbol  */  
   "DocCurrencyCodeSymbol":string,
      /**  Taxable Value 2  */  
   "TaxableAmt2":number,
      /**  Taxable Value 3  */  
   "TaxableAmt3":number,
      /**  Taxable Value 4  */  
   "TaxableAmt4":number,
      /**  Tax Value 1  */  
   "TaxAmt1":number,
   "BitFlag":number,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrDesc":string,
   "CustomerCustID":string,
   "CustomerBTName":string,
   "CustomerName":string,
   "RateGrpCodeDescription":string,
   "TaxRgnDescription":string,
   "TermsCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param PriorCustNum
   */  
export interface AnotherInvoice_input{
      /**  Customer number  */  
   PriorCustNum:number,
}

export interface AnotherInvoice_output{
   returnObj:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface CheckBeforePosting_output{
}

   /** Required : 
      @param OktoPost
   */  
export interface CheckforPostInvoices_input{
   OktoPost:number,
}

export interface CheckforPostInvoices_output{
parameters : {
      /**  output parameters  */  
   OktoPost:number,
}
}

   /** Required : 
      @param invoiceNum
   */  
export interface DeleteByID_input{
   invoiceNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ARInvoiceLoadListRow{
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
      /**  LegalNumber year.  */  
   LegalNumberYear:number,
      /**  Legal Number Prefix List  */  
   LegalNumberPrefixList:string,
      /**  Customer ID  */  
   CustID:string,
      /**  Invoice balance in base currency  */  
   BaseInvBal:number,
      /**  Legal number prefix  */  
   LegalNumberPrefix:string,
      /**  Legal number number  */  
   LegalNumberNumber:string,
      /**  Legal number read only fields  */  
   LegalNumberReadOnlyFields:string,
      /**  Currency rate type  (ex: USD > GBP)  */  
   CurrencyRateType:string,
      /**  Currency code symbol  */  
   CurrencyCodeSymbol:string,
      /**  store invoice balance for after update.  */  
   TempInvoiceBal:number,
      /**  Temporary doc invoice balance for after update.  */  
   TempDocInvoiceBal:number,
      /**  flag for use of legal numbers  */  
   UseLegalNumbers:boolean,
      /**  Document currency symbol  */  
   DocCurrencyCodeSymbol:string,
      /**  Display field for InvoiceBal  */  
   DispInvoiceBal:number,
      /**  Display field for DocInvoiceBal  */  
   DocDispInvoiceBal:number,
   Rpt1DispInvoiceBal:number,
   Rpt2DispInvoiceBal:number,
   Rpt3DispInvoiceBal:number,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  Description  */  
   RateGrpCodeDescription:string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   TermsCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARInvoiceLoadListTableset{
   ARInvoiceLoadList:Erp_Tablesets_ARInvoiceLoadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARInvoiceLoadRow{
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
      /**  Invoice balance in base currency  */  
   BaseInvBal:number,
      /**  Currency rate type  (ex: USD > GBP)  */  
   CurrencyRateType:string,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
      /**  Display field for DocInvoiceBal  */  
   DocDispInvoiceBal:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Legal number number  */  
   LegalNumberNumber:string,
      /**  Legal number prefix  */  
   LegalNumberPrefix:string,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  Legal Number Prefix List  */  
   LegalNumberPrefixList:string,
      /**  Legal number read only fields  */  
   LegalNumberReadOnlyFields:string,
      /**  LegalNumber year.  */  
   LegalNumberYear:number,
   Rpt1DispInvoiceBal:number,
   Rpt2DispInvoiceBal:number,
   Rpt3DispInvoiceBal:number,
      /**  Taxable Value 1  */  
   TaxableAmt1:number,
      /**  Tax Value 2  */  
   TaxAmt2:number,
      /**  Tax Value 3  */  
   TaxAmt3:number,
      /**  Tax Value 4  */  
   TaxAmt4:number,
      /**  Tax Type 1  */  
   TaxCode1:string,
   TaxCode1Description:string,
      /**  Tax Type 2  */  
   TaxCode2:string,
   TaxCode2Description:string,
      /**  Tax Type 3  */  
   TaxCode3:string,
   TaxCode3Description:string,
      /**  Tax Type 4  */  
   TaxCode4:string,
   TaxCode4Description:string,
      /**  Tax Rate 1  */  
   TaxRate1:string,
   TaxRate1Description:string,
      /**  Tax Rate 2  */  
   TaxRate2:string,
   TaxRate2Description:string,
      /**  Tax Rate 3  */  
   TaxRate3:string,
   TaxRate3Description:string,
      /**  Tax Rate 4  */  
   TaxRate4:string,
   TaxRate4Description:string,
      /**  Temporary doc invoice balance for after update.  */  
   TempDocInvoiceBal:number,
      /**  store invoice balance for after update.  */  
   TempInvoiceBal:number,
      /**  flag for use of legal numbers  */  
   UseLegalNumbers:boolean,
      /**  Currency code symbol  */  
   CurrencyCodeSymbol:string,
      /**  Customer ID  */  
   CustID:string,
      /**  Display field for InvoiceBal  */  
   DispInvoiceBal:number,
      /**  Document currency symbol  */  
   DocCurrencyCodeSymbol:string,
      /**  Taxable Value 2  */  
   TaxableAmt2:number,
      /**  Taxable Value 3  */  
   TaxableAmt3:number,
      /**  Taxable Value 4  */  
   TaxableAmt4:number,
      /**  Tax Value 1  */  
   TaxAmt1:number,
   BitFlag:number,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrDesc:string,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerName:string,
   RateGrpCodeDescription:string,
   TaxRgnDescription:string,
   TermsCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARInvoiceLoadTableset{
   ARInvoiceLoad:Erp_Tablesets_ARInvoiceLoadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtARInvoiceLoadTableset{
   ARInvoiceLoad:Erp_Tablesets_ARInvoiceLoadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param invoiceNum
   */  
export interface GetByID_input{
   invoiceNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ARInvoiceLoadTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ARInvoiceLoadTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface GetCurrencyBase_output{
parameters : {
      /**  output parameters  */  
   opCurrencyBase:string,
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
   returnObj:Erp_Tablesets_ARInvoiceLoadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewARInvoiceLoad_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface GetNewARInvoiceLoad_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param whereClauseARInvoiceLoad
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseARInvoiceLoad:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ARInvoiceLoadTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param sTaxLiability
   */  
export interface GetTaxTypesList_input{
      /**  Tax Liability.  */  
   sTaxLiability:string,
}

export interface GetTaxTypesList_output{
parameters : {
      /**  output parameters  */  
   sTaxTypesList:string,
}
}

export interface GetTotals_output{
parameters : {
      /**  output parameters  */  
   TotInvoiceAmt:number,
   CurrSymbol:string,
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
   */  
export interface OnChangeofApplyDate_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofApplyDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeofCreditMemo_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofCreditMemo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeofCurrencyCode_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeofCustomer_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofCustomer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeofDispInvoiceBal_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofDispInvoiceBal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeofDocDispInvoiceBal_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofDocDispInvoiceBal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeofDocInvoiceBal_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofDocInvoiceBal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeofExchangeRate_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofExchangeRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeofFiscalPeriod_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofFiscalPeriod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeofFiscalYear_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofFiscalYear_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeofInvoiceBal_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofInvoiceBal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeofInvoiceDate_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofInvoiceDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param taxRegionCode
      @param ds
   */  
export interface OnChangeofTaxRegionCode_input{
      /**  TaxRegionCode  */  
   taxRegionCode:string,
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangeofTaxRegionCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param iTaxNum
      @param sTaxCode
      @param sTaxRate
      @param bCheckCollectionMethod
      @param ds
   */  
export interface OnChangingofTax_input{
      /**  Sequence number of tax (1 or 2 or 3)  */  
   iTaxNum:number,
      /**  Tax Code  */  
   sTaxCode:string,
      /**  Tax Rate  */  
   sTaxRate:string,
      /**  Check tax type's collection method  */  
   bCheckCollectionMethod:boolean,
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface OnChangingofTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

   /** Required : 
      @param OktoPost
   */  
export interface PostInvoices_input{
      /**  A value of zero will be sent back to the UI when the
             open balance does not match the total invoice amount
             and an error will be thrown.
             A value of one sent by the UI means it is ok to post,
             but the open balance must match the total invoice amount.
             A value of two sent by the UI means that it is ok to post
             when the open balance does not match total invoice amount.
             In this case the business logic will not set the error flag
             to zero and the ErrMsg parameter will not be set.  */  
   OktoPost:number,
}

export interface PostInvoices_output{
parameters : {
      /**  output parameters  */  
   OktoPost:number,
   ErrMsg:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtARInvoiceLoadTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtARInvoiceLoadTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARInvoiceLoadTableset[],
}
}

