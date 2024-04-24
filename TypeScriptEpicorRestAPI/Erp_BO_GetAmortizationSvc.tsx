import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.GetAmortizationSvc
// Description: Get Deferred Revenue Amortization Schedules object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/$metadata", {
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
   Description: Get GetAmortizations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GetAmortizations
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRASchRow
   */  
export function get_GetAmortizations(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRASchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizations", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRASchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GetAmortizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcDtlRASchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InvcDtlRASchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAmortizations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizations", {
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
   Summary: Calls GetByID to retrieve the GetAmortization item
   Description: Calls GetByID to retrieve the GetAmortization item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GetAmortization
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param AmortSeq Desc: AmortSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcDtlRASchRow
   */  
export function get_GetAmortizations_Company_InvoiceNum_InvoiceLine_AmortSeq(Company:string, InvoiceNum:string, InvoiceLine:string, AmortSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InvcDtlRASchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizations(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + AmortSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_InvcDtlRASchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GetAmortization for the service
   Description: Calls UpdateExt to update GetAmortization. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GetAmortization
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param AmortSeq Desc: AmortSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcDtlRASchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GetAmortizations_Company_InvoiceNum_InvoiceLine_AmortSeq(Company:string, InvoiceNum:string, InvoiceLine:string, AmortSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizations(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + AmortSeq + ")", {
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
   Summary: Call UpdateExt to delete GetAmortization item
   Description: Call UpdateExt to delete GetAmortization item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GetAmortization
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param InvoiceNum Desc: InvoiceNum   Required: True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param AmortSeq Desc: AmortSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GetAmortizations_Company_InvoiceNum_InvoiceLine_AmortSeq(Company:string, InvoiceNum:string, InvoiceLine:string, AmortSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizations(" + Company + "," + InvoiceNum + "," + InvoiceLine + "," + AmortSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRaschListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRaschListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRaschListRow)
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
export function get_GetRows(whereClauseInvcDtlRASch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseInvcDtlRASch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInvcDtlRASch=" + whereClauseInvcDtlRASch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(invoiceNum:string, invoiceLine:string, amortSeq:string, epicorHeaders?:Headers){
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
   if(typeof amortSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "amortSeq=" + amortSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetList" + params, {
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
   Summary: Invoke method BuildAmortizationsLists
   Description: This method returns four possible lists of selected Deferred Revenue Amortization
Schedules (ttInvcDtlRASch).  This should be called to return a list containing the
key fields of selected InvcDtlRASch records. Since each record has three key fields
the list could potentially exceed the maximum allowed length of characters.  To avoid
this runtime error, the list will be split into four lists if needed.
   OperationID: BuildAmortizationsLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildAmortizationsLists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildAmortizationsLists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildAmortizationsLists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/BuildAmortizationsLists", {
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
   Summary: Invoke method GetAmortizations
   Description: This method returns the ttInvcDtlRASch dataset of Deferred Revenue Amortization Schedule with
some calculated columns added.
   OperationID: GetAmortizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAmortizations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAmortizations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAmortizations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizations", {
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
   Summary: Invoke method GetAmortizationsWithTotal
   Description: This method returns the ttInvcDtlRASch dataset of Deferred Revenue Amortization Schedule with
some calculated columns added.
   OperationID: GetAmortizationsWithTotal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAmortizationsWithTotal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAmortizationsWithTotal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAmortizationsWithTotal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizationsWithTotal", {
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
   Summary: Invoke method GetAmortizationRows
   Description: Returns Amortizations tableset for search
   OperationID: GetAmortizationRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAmortizationRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAmortizationRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAmortizationRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizationRows", {
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
   Summary: Invoke method GetAmortizationTotal
   Description: This method calculates the amortization total based on records in the GetAmortization tableset
   OperationID: GetAmortizationTotal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAmortizationTotal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAmortizationTotal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAmortizationTotal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetAmortizationTotal", {
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
   Description: This method returns the Base Currency
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetCurrencyBase", {
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
   Summary: Invoke method GetNewInvcDtlRASch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcDtlRASch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInvcDtlRASch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcDtlRASch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInvcDtlRASch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetNewInvcDtlRASch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GetAmortizationSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRASchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcDtlRASchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRaschListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcDtlRaschListRow[],
}

export interface Erp_Tablesets_InvcDtlRASchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Foreign key to the InvcHead.  */  
   "InvoiceNum":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   "InvoiceLine":number,
      /**  Internal identifier used to keep the records unique.  Each invoice line that is amortized will have a record for each period in which an amortization occurs.  */  
   "AmortSeq":number,
      /**  The id of the fiscal calendar this record is related to.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  This is the date when the percentage of revenue will be recognized.  */  
   "AmortDate":string,
      /**  This is the percentage of total revenue to be recognized.  */  
   "AmortPercent":number,
      /**  Amortization Amount of the invoice.  */  
   "AmortAmt":number,
      /**  The amount to be recognized in the first reporting currency.  */  
   "Rpt1AmortAmt":number,
      /**  The amortization amount in the reporting currency.  */  
   "Rpt2AmortAmt":number,
      /**  The amortization in reporting currency.  */  
   "Rpt3AmortAmt":number,
      /**  The amortization amount in document currency.  */  
   "DocAmortAmount":number,
      /**  Indicates if this amortization period is on hold.  */  
   "Hold":boolean,
      /**  Descriptive code assigned by user which uniquely identifies a reason code master record and identifies why a amortization period is on hold.  */  
   "HoldReasonCode":string,
      /**  Descriptive text further explaining why an amortization period is on hold.  */  
   "HoldText":string,
      /**  Indicates if the revenue has been recognized for this line.  */  
   "Posted":boolean,
      /**  The date when the revenue was recognized.  */  
   "PostedDate":string,
   "ContractNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Internal identifier used to Keep the records unique. Each invoice line that is amortized will have a record for each period in which an amortization occurs.  */  
   "OrgAmortSeq":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records.  */  
   "OrgInvcLine":number,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "CustID":string,
   "DocAmortAmt":number,
   "DocDspAmortAmt":number,
   "DocDspRevenueAmt":number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in document currency.  */  
   "DocRevenueAmt":number,
   "DspAmortAmt":number,
   "DspRevenueAmt":number,
   "GroupID":string,
      /**  Invoice Date is coming from the InvcHead.  */  
   "InvoiceDate":string,
   "ReadyToPost":boolean,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount).  */  
   "RevenueAmt":number,
   "Rpt1DspAmortAmt":number,
   "Rpt1DspRevenueAmt":number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   "Rpt1RevenueAmt":number,
   "Rpt2DspAmortAmt":number,
   "Rpt2DspRevenueAmt":number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   "Rpt2RevenueAmt":number,
   "Rpt3DspAmortAmt":number,
   "Rpt3DspRevenueAmt":number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   "Rpt3RevenueAmt":number,
      /**  Flag to indicate if the record has been selected for the Hold/Unhold Amortization Periods process.  */  
   "Selected":boolean,
      /**  Displays the Amortization Seq in relation to the total Duration periods (i.e. AmortSeq/Duration).  */  
   "SeqDuration":string,
      /**  Total Amortization Amount of all the periods displayed on the grid in base currency.  */  
   "TotalAmortAmt":number,
   "IsLocked":boolean,
      /**  locked means can not be posted: an Schedule line is already in review journal or in posting process.  */  
   "LockStatus":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InvcDtlRaschListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Foreign key to the InvcHead.  */  
   "InvoiceNum":number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   "InvoiceLine":number,
      /**  Internal identifier used to keep the records unique.  Each invoice line that is amortized will have a record for each period in which an amortization occurs.  */  
   "AmortSeq":number,
      /**  The id of the fiscal calendar this record is related to.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year.  */  
   "FiscalYear":number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period number in the fiscal year.  */  
   "FiscalPeriod":number,
      /**  This is the date when the percentage of revenue will be recognized.  */  
   "AmortDate":string,
      /**  This is the percentage of total revenue to be recognized.  */  
   "AmortPercent":number,
      /**  Amortization Amount of the invoice.  */  
   "AmortAmt":number,
      /**  The amount to be recognized in the first reporting currency.  */  
   "Rpt1AmortAmt":number,
      /**  The amortization amount in the reporting currency.  */  
   "Rpt2AmortAmt":number,
      /**  The amortization in reporting currency.  */  
   "Rpt3AmortAmt":number,
      /**  The amortization amount in document currency.  */  
   "DocAmortAmount":number,
      /**  Indicates if this amortization period is on hold.  */  
   "Hold":boolean,
      /**  Descriptive code assigned by user which uniquely identifies a reason code master record and identifies why a amortization period is on hold.  */  
   "HoldReasonCode":string,
      /**  Descriptive text further explaining why an amortization period is on hold.  */  
   "HoldText":string,
      /**  Indicates if the revenue has been recognized for this line.  */  
   "Posted":boolean,
      /**  The date when the revenue was recognized.  */  
   "PostedDate":string,
   "ContractNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "GroupID":string,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "DocAmortAmt":number,
   "ReadyToPost":boolean,
      /**  Flag to indicate if the record has been selected for the Hold/Unhold Amortization Periods process.  */  
   "Selected":boolean,
   "CustID":string,
      /**  Invoice Date is coming from the InvcHead.  */  
   "InvoiceDate":string,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount).  */  
   "RevenueAmt":number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in document currency.  */  
   "DocRevenueAmt":number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   "Rpt1RevenueAmt":number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   "Rpt2RevenueAmt":number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   "Rpt3RevenueAmt":number,
      /**  Total Amortization Amount of all the periods displayed on the grid in base currency.  */  
   "TotalAmortAmt":number,
      /**  Displays the Amortization Seq in relation to the total Duration periods (i.e. AmortSeq/Duration).  */  
   "SeqDuration":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param opGuid
      @param ds
   */  
export interface BuildAmortizationsLists_input{
      /**  Unique Identifier  */  
   opGuid:string,
   ds:Erp_Tablesets_GetAmortizationTableset[],
}

export interface BuildAmortizationsLists_output{
parameters : {
      /**  output parameters  */  
   opReasonMsg:string,
   ds:Erp_Tablesets_GetAmortizationTableset[],
}
}

   /** Required : 
      @param invoiceNum
      @param invoiceLine
      @param amortSeq
   */  
export interface DeleteByID_input{
   invoiceNum:number,
   invoiceLine:number,
   amortSeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GetAmortizationTableset{
   InvcDtlRASch:Erp_Tablesets_InvcDtlRASchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InvcDtlRASchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**  Internal identifier used to keep the records unique.  Each invoice line that is amortized will have a record for each period in which an amortization occurs.  */  
   AmortSeq:number,
      /**  The id of the fiscal calendar this record is related to.  */  
   FiscalCalendarID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  This is the date when the percentage of revenue will be recognized.  */  
   AmortDate:string,
      /**  This is the percentage of total revenue to be recognized.  */  
   AmortPercent:number,
      /**  Amortization Amount of the invoice.  */  
   AmortAmt:number,
      /**  The amount to be recognized in the first reporting currency.  */  
   Rpt1AmortAmt:number,
      /**  The amortization amount in the reporting currency.  */  
   Rpt2AmortAmt:number,
      /**  The amortization in reporting currency.  */  
   Rpt3AmortAmt:number,
      /**  The amortization amount in document currency.  */  
   DocAmortAmount:number,
      /**  Indicates if this amortization period is on hold.  */  
   Hold:boolean,
      /**  Descriptive code assigned by user which uniquely identifies a reason code master record and identifies why a amortization period is on hold.  */  
   HoldReasonCode:string,
      /**  Descriptive text further explaining why an amortization period is on hold.  */  
   HoldText:string,
      /**  Indicates if the revenue has been recognized for this line.  */  
   Posted:boolean,
      /**  The date when the revenue was recognized.  */  
   PostedDate:string,
   ContractNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Internal identifier used to Keep the records unique. Each invoice line that is amortized will have a record for each period in which an amortization occurs.  */  
   OrgAmortSeq:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records.  */  
   OrgInvcLine:number,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CustID:string,
   DocAmortAmt:number,
   DocDspAmortAmt:number,
   DocDspRevenueAmt:number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in document currency.  */  
   DocRevenueAmt:number,
   DspAmortAmt:number,
   DspRevenueAmt:number,
   GroupID:string,
      /**  Invoice Date is coming from the InvcHead.  */  
   InvoiceDate:string,
   ReadyToPost:boolean,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount).  */  
   RevenueAmt:number,
   Rpt1DspAmortAmt:number,
   Rpt1DspRevenueAmt:number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   Rpt1RevenueAmt:number,
   Rpt2DspAmortAmt:number,
   Rpt2DspRevenueAmt:number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   Rpt2RevenueAmt:number,
   Rpt3DspAmortAmt:number,
   Rpt3DspRevenueAmt:number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   Rpt3RevenueAmt:number,
      /**  Flag to indicate if the record has been selected for the Hold/Unhold Amortization Periods process.  */  
   Selected:boolean,
      /**  Displays the Amortization Seq in relation to the total Duration periods (i.e. AmortSeq/Duration).  */  
   SeqDuration:string,
      /**  Total Amortization Amount of all the periods displayed on the grid in base currency.  */  
   TotalAmortAmt:number,
   IsLocked:boolean,
      /**  locked means can not be posted: an Schedule line is already in review journal or in posting process.  */  
   LockStatus:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcDtlRaschListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**  Internal identifier used to keep the records unique.  Each invoice line that is amortized will have a record for each period in which an amortization occurs.  */  
   AmortSeq:number,
      /**  The id of the fiscal calendar this record is related to.  */  
   FiscalCalendarID:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  This is the date when the percentage of revenue will be recognized.  */  
   AmortDate:string,
      /**  This is the percentage of total revenue to be recognized.  */  
   AmortPercent:number,
      /**  Amortization Amount of the invoice.  */  
   AmortAmt:number,
      /**  The amount to be recognized in the first reporting currency.  */  
   Rpt1AmortAmt:number,
      /**  The amortization amount in the reporting currency.  */  
   Rpt2AmortAmt:number,
      /**  The amortization in reporting currency.  */  
   Rpt3AmortAmt:number,
      /**  The amortization amount in document currency.  */  
   DocAmortAmount:number,
      /**  Indicates if this amortization period is on hold.  */  
   Hold:boolean,
      /**  Descriptive code assigned by user which uniquely identifies a reason code master record and identifies why a amortization period is on hold.  */  
   HoldReasonCode:string,
      /**  Descriptive text further explaining why an amortization period is on hold.  */  
   HoldText:string,
      /**  Indicates if the revenue has been recognized for this line.  */  
   Posted:boolean,
      /**  The date when the revenue was recognized.  */  
   PostedDate:string,
   ContractNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   GroupID:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   DocAmortAmt:number,
   ReadyToPost:boolean,
      /**  Flag to indicate if the record has been selected for the Hold/Unhold Amortization Periods process.  */  
   Selected:boolean,
   CustID:string,
      /**  Invoice Date is coming from the InvcHead.  */  
   InvoiceDate:string,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount).  */  
   RevenueAmt:number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in document currency.  */  
   DocRevenueAmt:number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   Rpt1RevenueAmt:number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   Rpt2RevenueAmt:number,
      /**  The full revenue amount taken from the invoice line (ExtPrince - Discount) in reporting currency.  */  
   Rpt3RevenueAmt:number,
      /**  Total Amortization Amount of all the periods displayed on the grid in base currency.  */  
   TotalAmortAmt:number,
      /**  Displays the Amortization Seq in relation to the total Duration periods (i.e. AmortSeq/Duration).  */  
   SeqDuration:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcDtlRaschListTableset{
   InvcDtlRaschList:Erp_Tablesets_InvcDtlRaschListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGetAmortizationTableset{
   InvcDtlRASch:Erp_Tablesets_InvcDtlRASchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipCustList
      @param ipInvList
      @param ipContList
      @param ipApplyDate
      @param ipShowStatus
      @param ds
   */  
export interface GetAmortizationRows_input{
   ipCustList:string,
   ipInvList:string,
   ipContList:string,
   ipApplyDate:string,
   ipShowStatus:string,
   ds:Erp_Tablesets_GetAmortizationTableset[],
}

export interface GetAmortizationRows_output{
   returnObj:Erp_Tablesets_GetAmortizationTableset[],
parameters : {
      /**  output parameters  */  
   totalAmortization:number,
   baseCurrencyCode:string,
   ds:Erp_Tablesets_GetAmortizationTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetAmortizationTotal_input{
   ds:Erp_Tablesets_GetAmortizationTableset[],
}

export interface GetAmortizationTotal_output{
parameters : {
      /**  output parameters  */  
   amortizationTotal:number,
   ds:Erp_Tablesets_GetAmortizationTableset[],
}
}

   /** Required : 
      @param ipCustList
      @param ipInvList
      @param ipContList
      @param ipApplyDate
      @param ipShowStatus
      @param ds
   */  
export interface GetAmortizationsWithTotal_input{
      /**  The Customer Number list to filter the records with  */  
   ipCustList:string,
      /**  The Invoice Number list to filter the records with  */  
   ipInvList:string,
      /**  The Service Contract Number list to filter the records with  */  
   ipContList:string,
      /**  The Apply Date filter  */  
   ipApplyDate:string,
      /**  If value is 'H', show records marked as On Hold; if 'U', show records Not On Hold; if 'B', show all.  */  
   ipShowStatus:string,
   ds:Erp_Tablesets_GetAmortizationTableset[],
}

export interface GetAmortizationsWithTotal_output{
parameters : {
      /**  output parameters  */  
   totalAmortization:number,
   baseCurrencyCode:string,
   ds:Erp_Tablesets_GetAmortizationTableset[],
}
}

   /** Required : 
      @param ipCustList
      @param ipInvList
      @param ipContList
      @param ipApplyDate
      @param ipShowStatus
      @param ds
   */  
export interface GetAmortizations_input{
      /**  The Customer Number list to filter the records with  */  
   ipCustList:string,
      /**  The Invoice Number list to filter the records with  */  
   ipInvList:string,
      /**  The Service Contract Number list to filter the records with  */  
   ipContList:string,
      /**  The Apply Date filter  */  
   ipApplyDate:string,
      /**  If value is 'H', show records marked as On Hold; if 'U', show records Not On Hold; if 'B', show all.  */  
   ipShowStatus:string,
   ds:Erp_Tablesets_GetAmortizationTableset[],
}

export interface GetAmortizations_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetAmortizationTableset[],
}
}

   /** Required : 
      @param invoiceNum
      @param invoiceLine
      @param amortSeq
   */  
export interface GetByID_input{
   invoiceNum:number,
   invoiceLine:number,
   amortSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GetAmortizationTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GetAmortizationTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GetAmortizationTableset[],
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
   returnObj:Erp_Tablesets_InvcDtlRaschListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param invoiceNum
      @param invoiceLine
   */  
export interface GetNewInvcDtlRASch_input{
   ds:Erp_Tablesets_GetAmortizationTableset[],
   invoiceNum:number,
   invoiceLine:number,
}

export interface GetNewInvcDtlRASch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetAmortizationTableset[],
}
}

   /** Required : 
      @param whereClauseInvcDtlRASch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseInvcDtlRASch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GetAmortizationTableset[],
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
   ds:Erp_Tablesets_UpdExtGetAmortizationTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGetAmortizationTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GetAmortizationTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GetAmortizationTableset[],
}
}

