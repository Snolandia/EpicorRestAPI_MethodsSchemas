import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.APInvDtlSearchSvc
// Description: bo/APInvDtlSearch/APInvDtlSearch.p
           APInvDtl Search Business Object
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get APInvDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APInvDtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvDtlRow
   */  
export function get_APInvDtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/APInvDtlSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APInvDtlSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APInvDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APInvDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APInvDtlSearches(requestBody:Erp_Tablesets_APInvDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/APInvDtlSearches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APInvDtlSearch item
   Description: Calls GetByID to retrieve the APInvDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APInvDtlRow
   */  
export function get_APInvDtlSearches_Company_VendorNum_InvoiceNum_InvoiceLine(Company:string, VendorNum:string, InvoiceNum:string, InvoiceLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APInvDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/APInvDtlSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_APInvDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APInvDtlSearch for the service
   Description: Calls UpdateExt to update APInvDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APInvDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APInvDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APInvDtlSearches_Company_VendorNum_InvoiceNum_InvoiceLine(Company:string, VendorNum:string, InvoiceNum:string, InvoiceLine:string, requestBody:Erp_Tablesets_APInvDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/APInvDtlSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete APInvDtlSearch item
   Description: Call UpdateExt to delete APInvDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APInvDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APInvDtlSearches_Company_VendorNum_InvoiceNum_InvoiceLine(Company:string, VendorNum:string, InvoiceNum:string, InvoiceLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/APInvDtlSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvDtlListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseAPInvDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAPInvDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPInvDtl=" + whereClauseAPInvDtl
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRows_output)
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(vendorNum:string, invoiceNum:string, invoiceLine:string, epicorHeaders?:Headers){
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

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPInvDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPInvDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPInvDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPInvDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPInvDtl(requestBody:GetNewAPInvDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPInvDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/GetNewAPInvDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPInvDtl_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowIDs_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Update_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvDtlSearchSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APInvDtlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APInvDtlRow,
}

export interface Erp_Tablesets_APInvDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  */  
   "VendorNum":number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   "InvoiceNum":string,
      /**  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  */  
   "InvoiceLine":number,
      /**  Indicates the type of invoice line. "R" = Invoiced for Receipt of goods, "A" - Advance Billing,  "M" - Misc. Billing, "U" - Unreceived goods, "J" - Job Miscellaneous charge A/P invoice, "S" - Asset Invoice Line.  Not directly entered,  set by invoice entry by the user selecting the appropriate menu option.  */  
   "LineType":string,
      /**  item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost if related.  */  
   "UnitCost":number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   "DocUnitCost":number,
      /**  Part number used to identify line item part.  */  
   "PartNum":string,
      /**   Purchase Order Number that this invoice line item is related to. If packing slip is referenced then it is set = to RcvDtl.PONum and can't be changed.  If entered it must be a valid POHeader record.
A reference is made to the purchase order using PONUM, POLine and PORelNum fields. If any one of these fields are entered then they all must be entered and be valid.  */  
   "PONum":number,
      /**  The PO line # that invoice is for. Defaulted from the RvcDtl if referenced to packing slip document.. Only applicable when PO is referenced.  */  
   "POLine":number,
      /**  Purchase Order Release # which is being invoiced. Defaulted from RcvDtl if related to a packing slip. If entered it Must be valid.  */  
   "PORelNum":number,
      /**  Invoice line description.  */  
   "Description":string,
      /**  Job that this invoice is related to. Set to the RcvDtl.JobNum.  */  
   "JobNum":string,
      /**  Job Assembly Sequence that this invoice line is related to. Set to RcvDtl.AssemblySeq.  */  
   "AssemblySeq":number,
      /**  Indicates if this invoice line is related to a job material (jobmtl) or job subcontract (JobOper) record. Valid values are "M" = material or "S" = subcontract. This is set to RvcDtl.JobSeqType.  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record to which this line item is costed against. Defaults from the RcvDtl.JobSeq. Only applicable for a receipts to job.  */  
   "JobSeq":number,
      /**  The Vendor's purchase point ID. This is used as part of the foreign key to reference the RcvHead/RcvDtl records.  */  
   "PurPoint":string,
      /**  Vendor's packing slip that this A\P invoice detail line is associated with. This Along with PackLine provides a relationship to the receipt document detail (RcvDtl)  */  
   "PackSlip":string,
      /**  The Pack Slip line of the RcvDtl record  to which this A\P detail record is related to.  */  
   "PackLine":number,
      /**  Total Invoiced Quantity for the line item.  This is stored in the Vendors Unit of Measure.  Can be defaulted from the packing slip detail if referenced (RcvDtl.POReceiptQty)  */  
   "VendorQty":number,
      /**  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDel.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  */  
   "PUM":string,
      /**  Invoiced Quantity for the line item in our unit of measure. This can be defaulted from the packing slip detail if referenced (RcvDtl.ReceiptQty)  */  
   "OurQty":number,
      /**  Unit of Measure code for invoiced quantity in our unit of measure. Defaulted in the following hierarchy: from the RcvDel.IUM if packing slip is referenced, from PODetail.IUM if PO is referenced, from Part.IUM if valid part or finally from XaSyst.DefaultUM.  */  
   "IUM":string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the APInvDtl.VendorQty by the appropriate "per" value and then multiply by unit cost.  Use the PODetail.CostPerCode if related to a PO else use Part.PricePerCode if valid part. Else default as "E".
Valid database values are "E" = Each, "C" = per 100 or "M" = per 1,000.  */  
   "CostPerCode":string,
      /**  Vendor's part number. Optional, defaults from the RcvDtl, PODetail or blank.  */  
   "VenPartNum":string,
      /**  Extended Cost for the invoice line item. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  */  
   "ExtCost":number,
      /**  Extended Cost for the invoice line item in Vendors currency. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  */  
   "DocExtCost":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "TotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line in vendors currency.  */  
   "DocTotalMiscChrg":number,
      /**  Used to establish invoice comments about the invoice line.  */  
   "LineComment":string,
      /**  Mirror image of related RCVHead.ReceiptDate.  Only applies to LineType = U. Updated during the Invoice/Receipt match posting process if GLSyst.PostInvtyWipCos = No.  This date is used as the journal date and to determine the fiscal period when the Invoice/Receipt process is responsible for generating the GL entries. (See CaMatchingDiv description)  */  
   "MatchDate":string,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   "MatchFiscalYear":number,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   "MatchFiscalPeriod":number,
      /**  Indicates if this item is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info.  */  
   "TaxExempt":string,
      /**  Indicates the Tax Category for this line item.  Defaults from the Part Master.  */  
   "TaxCatID":string,
      /**  The amount this line item that is reduced by due to prior advanced payments.    It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  */  
   "AdvancePayAmt":number,
      /**  The amount this line item that is reduced by due to prior advanced payments.   It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  */  
   "DocAdvancePayAmt":number,
      /**  Purchase Code.  */  
   "PurchCode":string,
      /**  Discount amount for this line  */  
   "LineDiscAmt":number,
      /**  Discount amount (Vendors Currency) for this line  */  
   "DocLineDiscAmt":number,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   "GlbInvoiceNum":string,
      /**  Global Invoice Line identifier.  Used in Consolidated Purchasing.  */  
   "GlbInvoiceLine":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "AdvGainLoss":number,
      /**  Flag to indicate that G/L entries appearing under this invoice line will have multi-company journals entered at the target external company.  */  
   "MultiCompany":boolean,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line.  */  
   "RevChargeMethod":string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   "OverrideReverseCharge":boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   "RevChargeApplied":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AdvancePayAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AdvancePayAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AdvancePayAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1LineDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2LineDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3LineDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitCost":number,
      /**  Amount of advance payment applied  */  
   "DocAdvPayAppld":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt1AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt2AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt3AdvGainLoss":number,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   "MatchFiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "MatchFiscalCalendarID":string,
      /**  The Tax Region for this invoice.  */  
   "TaxRegionCode":string,
      /**  The Supplier Shipment ID (also known as the ContainerID).  */  
   "ContainerID":number,
      /**  Drop Shipment Pack Line  */  
   "DropShipPackLine":number,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  */  
   "CorrectionDtl":boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  Asset number of the linked Asset Addition transaction.  */  
   "AssetNum":string,
      /**  Addition Number or sequence of the linked Asset Addition transaction.  */  
   "AdditionNum":number,
      /**  Used in a correction invoice to store reference to the original invoice line.  */  
   "InvoiceLineRef":number,
      /**  This is the current invoice line balance (in vendor currency) left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance of this DocAssetInvoiceBal.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  */  
   "DocAssetInvoiceBal":number,
      /**  This is the Invoiced Quantity balance left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  This qty is expressed in our unit of measure.  */  
   "AssetBalOurQty":number,
      /**  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  */  
   "AssetQtyIUM":string,
      /**  The DMR Number that requires supplier credit.  */  
   "DMRNum":number,
      /**  The Action Number for the DMR that requires supplier credit.  */  
   "DMRActionNum":number,
      /**  Indicates if this invoice line was created from an EmpExpense record.  */  
   "CreatedFromExpense":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Generated 1099 Code where this invoice was calculated in the 1099 Form  */  
   "Gen1099Code":string,
      /**  Indicates if intrastat is available for the line.  */  
   "EnableIntrastat":boolean,
   "CurrencySwitch":boolean,
   "BaseCurrSymbol":string,
   "CurrSymbol":string,
   "ScrExtCost":number,
   "ScrDocExtCost":number,
   "ScrTotalMiscChrg":number,
   "ScrDocTotalMiscChrg":number,
   "ScrLineType":string,
   "DebitMemo":boolean,
   "Variance":number,
   "EnablePurchaseCode":boolean,
   "EnableDiscountAmt":boolean,
   "UsePurchaseCode":boolean,
   "LineSubtotal":number,
   "DocLineSubtotal":number,
   "LineTotal":number,
   "DocLineTotal":number,
   "ScrVendorQty":number,
   "ScrOurQty":number,
   "AllowGLDistAdd":boolean,
   "AllowGLDistAllocation":boolean,
   "AllowGLDistDelete":boolean,
   "ScrLineDiscAmt":number,
   "ScrDocLineDiscAmt":number,
   "AllowJobMiscAdd":boolean,
   "AllowJobMiscDelete":boolean,
   "AllowJobMiscUpdate":boolean,
   "AllocationID":string,
   "AllocationAmount":number,
   "RcptReceiptDate":string,
   "RcptPartNum":string,
   "RcptPartDescription":string,
   "RcptDestination":string,
   "RcptVenPartNum":string,
   "RcptVendorQty":number,
   "POPartNum":string,
   "POLineDesc":string,
   "PORelQty":number,
   "POReceivedQty":number,
   "POVenPartNum":string,
   "POUnitCost":number,
   "PODocUnitCost":number,
   "POCostPerCode":string,
      /**  The VenPartNum field for the datagrid.  For display purposes only.  */  
   "GridVenPartNum":string,
   "RcptPUM":string,
   "POPUM":string,
   "Posted":boolean,
   "LineTypeDescription":string,
   "GroupID":string,
   "AllocationDesc":string,
      /**  Indicates if Override Reverse Charge check box should be enabled.  */  
   "EnableRevCharge":boolean,
      /**  Reverse Charge Method description  */  
   "RevChargeMethodDesc":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "Rpt1ScrExtCost":number,
   "Rpt2ScrExtCost":number,
   "Rpt3ScrExtCost":number,
   "Rpt1ScrTotalMiscChrg":number,
   "Rpt2ScrTotalMiscChrg":number,
   "Rpt3ScrTotalMiscChrg":number,
   "Rpt1ScrLineDiscAmt":number,
   "Rpt2ScrLineDiscAmt":number,
   "Rpt3ScrLineDiscAmt":number,
   "Rpt1LineSubTotal":number,
   "Rpt2LineSubtotal":number,
   "Rpt3LineSubtotal":number,
   "Rpt1LineTotal":number,
   "Rpt2LineTotal":number,
   "Rpt3LineTotal":number,
      /**  Receipt Our UOM  */  
   "RcptIUM":string,
      /**  Receipt Our Quantity  */  
   "RcptOurQty":number,
      /**  PO Rel Our Quantity  */  
   "PORelOurQty":number,
      /**  PO Rel Our UOM  */  
   "PORelIUM":string,
   "Rpt1POUnitCost":number,
   "Rpt2POUnitCost":number,
   "Rpt3POUnitCost":number,
      /**  Drop Shipment  */  
   "DropShipment":boolean,
   "EnableShipmentID":boolean,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   "EnableSupplierXRef":boolean,
      /**  This is the value of the lines that have been entered. In Base Currency  */  
   "TotDistribAmt":number,
      /**  This is the value of the lines that have been entered. In Document Currency  */  
   "DocTotDistribAmt":number,
      /**  This is the value of the lines that have been entered. In Reportable currency 1.  */  
   "Rpt1TotDistribAmt":number,
      /**  This is the value of the lines that have been entered. In Reportable currency 2.  */  
   "Rpt2TotDistribAmt":number,
      /**  This is the value of the lines that have been entered. In Reportable currency 3.  */  
   "Rpt3TotDistribAmt":number,
   "EnableSubCData":boolean,
   "POWarn":string,
   "CurrencyID":string,
   "BaseCurrencyID":string,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   "AdjustmentValue":number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   "DocAdjustmentValue":number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   "Rpt1AdjustmentValue":number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   "Rpt2AdjustmentValue":number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   "Rpt3AdjustmentValue":number,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  Mandatory description of the asset.  */  
   "AssetNumAssetDescription":string,
      /**  Free form text that describes this particular container.  */  
   "ContainerIDContainerDescription":string,
      /**  Description of the purchase type. Appears in drop-down lists for selection.  */  
   "GLPurchPurchDesc":string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   "InvoiceNumDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
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
      /**  OUR internal Part number for this item.  */  
   "POLinePartNum":string,
      /**  Supplier Part Number  */  
   "POLineVenPartNum":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "POLineLineDesc":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "PORelNumRefCodeDesc":string,
      /**  Full description for the Sales Tax category.  */  
   "TaxCatIDDescription":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  defaults from the company file.  */  
   "vrPONumShipName":string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   "vrPONumShipToConName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APInvDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  */  
   "VendorNum":number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   "InvoiceNum":string,
      /**  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  */  
   "InvoiceLine":number,
      /**  Indicates the type of invoice line. "R" = Invoiced for Receipt of goods, "A" - Advance Billing,  "M" - Misc. Billing, "U" - Unreceived goods, "J" - Job Miscellaneous charge A/P invoice, "S" - Asset Invoice Line.  Not directly entered,  set by invoice entry by the user selecting the appropriate menu option.  */  
   "LineType":string,
      /**  item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost if related.  */  
   "UnitCost":number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   "DocUnitCost":number,
      /**  Part number used to identify line item part.  */  
   "PartNum":string,
      /**   Purchase Order Number that this invoice line item is related to. If packing slip is referenced then it is set = to RcvDtl.PONum and can't be changed.  If entered it must be a valid POHeader record.
A reference is made to the purchase order using PONUM, POLine and PORelNum fields. If any one of these fields are entered then they all must be entered and be valid.  */  
   "PONum":number,
      /**  The PO line # that invoice is for. Defaulted from the RvcDtl if referenced to packing slip document.. Only applicable when PO is referenced.  */  
   "POLine":number,
      /**  Purchase Order Release # which is being invoiced. Defaulted from RcvDtl if related to a packing slip. If entered it Must be valid.  */  
   "PORelNum":number,
      /**  Invoice line description.  */  
   "Description":string,
      /**  Job that this invoice is related to. Set to the RcvDtl.JobNum.  */  
   "JobNum":string,
      /**  Job Assembly Sequence that this invoice line is related to. Set to RcvDtl.AssemblySeq.  */  
   "AssemblySeq":number,
      /**  Indicates if this invoice line is related to a job material (jobmtl) or job subcontract (JobOper) record. Valid values are "M" = material or "S" = subcontract. This is set to RvcDtl.JobSeqType.  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record to which this line item is costed against. Defaults from the RcvDtl.JobSeq. Only applicable for a receipts to job.  */  
   "JobSeq":number,
      /**  The Vendor's purchase point ID. This is used as part of the foreign key to reference the RcvHead/RcvDtl records.  */  
   "PurPoint":string,
      /**  Vendor's packing slip that this A\P invoice detail line is associated with. This Along with PackLine provides a relationship to the receipt document detail (RcvDtl)  */  
   "PackSlip":string,
      /**  The Pack Slip line of the RcvDtl record  to which this A\P detail record is related to.  */  
   "PackLine":number,
      /**  Total Invoiced Quantity for the line item.  This is stored in the Vendors Unit of Measure.  Can be defaulted from the packing slip detail if referenced (RcvDtl.POReceiptQty)  */  
   "VendorQty":number,
      /**  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDel.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  */  
   "PUM":string,
      /**  Invoiced Quantity for the line item in our unit of measure. This can be defaulted from the packing slip detail if referenced (RcvDtl.ReceiptQty)  */  
   "OurQty":number,
      /**  Unit of Measure code for invoiced quantity in our unit of measure. Defaulted in the following hierarchy: from the RcvDel.IUM if packing slip is referenced, from PODetail.IUM if PO is referenced, from Part.IUM if valid part or finally from XaSyst.DefaultUM.  */  
   "IUM":string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the APInvDtl.VendorQty by the appropriate "per" value and then multiply by unit cost.  Use the PODetail.CostPerCode if related to a PO else use Part.PricePerCode if valid part. Else default as "E".
Valid database values are "E" = Each, "C" = per 100 or "M" = per 1,000.  */  
   "CostPerCode":string,
      /**  Vendor's part number. Optional, defaults from the RcvDtl, PODetail or blank.  */  
   "VenPartNum":string,
      /**  Extended Cost for the invoice line item. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  */  
   "ExtCost":number,
      /**  Extended Cost for the invoice line item in Vendors currency. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  */  
   "DocExtCost":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   "TotalMiscChrg":number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line in vendors currency.  */  
   "DocTotalMiscChrg":number,
      /**  Used to establish invoice comments about the invoice line.  */  
   "LineComment":string,
      /**  Mirror image of related RCVHead.ReceiptDate.  Only applies to LineType = U. Updated during the Invoice/Receipt match posting process if GLSyst.PostInvtyWipCos = No.  This date is used as the journal date and to determine the fiscal period when the Invoice/Receipt process is responsible for generating the GL entries. (See CaMatchingDiv description)  */  
   "MatchDate":string,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   "MatchFiscalYear":number,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   "MatchFiscalPeriod":number,
      /**  Indicates if this item is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info.  */  
   "TaxExempt":string,
      /**  Indicates the Tax Category for this line item.  Defaults from the Part Master.  */  
   "TaxCatID":string,
      /**  The amount this line item that is reduced by due to prior advanced payments.    It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  */  
   "AdvancePayAmt":number,
      /**  The amount this line item that is reduced by due to prior advanced payments.   It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  */  
   "DocAdvancePayAmt":number,
      /**  Purchase Code.  */  
   "PurchCode":string,
      /**  Discount amount for this line  */  
   "LineDiscAmt":number,
      /**  Discount amount (Vendors Currency) for this line  */  
   "DocLineDiscAmt":number,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   "GlbInvoiceNum":string,
      /**  Global Invoice Line identifier.  Used in Consolidated Purchasing.  */  
   "GlbInvoiceLine":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "AdvGainLoss":number,
      /**  Flag to indicate that G/L entries appearing under this invoice line will have multi-company journals entered at the target external company.  */  
   "MultiCompany":boolean,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line.  */  
   "RevChargeMethod":string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   "OverrideReverseCharge":boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   "RevChargeApplied":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1AdvancePayAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2AdvancePayAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3AdvancePayAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1LineDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2LineDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3LineDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitCost":number,
      /**  Amount of advance payment applied  */  
   "DocAdvPayAppld":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt1AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt2AdvGainLoss":number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   "Rpt3AdvGainLoss":number,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   "MatchFiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "MatchFiscalCalendarID":string,
      /**  The Tax Region for this invoice.  */  
   "TaxRegionCode":string,
      /**  The Supplier Shipment ID (also known as the ContainerID).  */  
   "ContainerID":number,
      /**  Drop Shipment Pack Line  */  
   "DropShipPackLine":number,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  */  
   "CorrectionDtl":boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  Asset number of the linked Asset Addition transaction.  */  
   "AssetNum":string,
      /**  Addition Number or sequence of the linked Asset Addition transaction.  */  
   "AdditionNum":number,
      /**  Used in a correction invoice to store reference to the original invoice line.  */  
   "InvoiceLineRef":number,
      /**  This is the current invoice line balance (in vendor currency) left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance of this DocAssetInvoiceBal.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  */  
   "DocAssetInvoiceBal":number,
      /**  This is the Invoiced Quantity balance left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  This qty is expressed in our unit of measure.  */  
   "AssetBalOurQty":number,
      /**  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  */  
   "AssetQtyIUM":string,
      /**  The DMR Number that requires supplier credit.  */  
   "DMRNum":number,
      /**  The Action Number for the DMR that requires supplier credit.  */  
   "DMRActionNum":number,
      /**  Indicates if this invoice line was created from an EmpExpense record.  */  
   "CreatedFromExpense":boolean,
      /**  item's unit cost in the vendors unit of measure including taxes.  */  
   "InUnitCost":number,
      /**  item's unit cost in the vendors unit of measure and currency including taxes.  */  
   "DocInUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InUnitCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InUnitCost":number,
      /**  Extended Cost for the invoice line item including taxes.  */  
   "InExtCost":number,
      /**   Extended Cost for the invoice line item in Vendors currency
including taxes  */  
   "DocInExtCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InExtCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InExtCost":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InExtCost":number,
      /**  Rolled up total of all misc. charge records for this invoice detail line including taxes.  */  
   "InTotalMiscChrg":number,
      /**  Rolled up total of all misc. charge records for this invoice detail line in vendors currency including taxes.  */  
   "DocInTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InTotalMiscChrg":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InTotalMiscChrg":number,
      /**  The amount this line item that is reduced by due to prior advanced payments (incl taxes).  */  
   "InAdvancePayAmt":number,
      /**  The amount this line item that is reduced by due to prior advanced payments (incl taxes).  */  
   "DocInAdvancePayAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InAdvancePayAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InAdvancePayAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InAdvancePayAmt":number,
      /**  Discount amount for this line including taxes  */  
   "InLineDiscAmt":number,
      /**  Discount amount (Vendors Currency) for this line including taxes  */  
   "DocInLineDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InLineDiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InLineDiscAmt":number,
   "Rpt3InLineDiscAmt":number,
      /**  Indicates if no tax recalculation by the system is  supposed to be done since with "In Price" tax calculation the tax lines were adjusted or new tax lines added manually  */  
   "NoTaxRecal":boolean,
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
      /**  Reserved for development  - logical  */  
   "DevLog1":boolean,
      /**  Reserved for development - logical  */  
   "DevLog2":boolean,
      /**  Reserved for development  - character  */  
   "DevChar1":string,
      /**  Reserved for development - character  */  
   "DevChar2":string,
      /**  Reserved for development - date  */  
   "DevDate1":string,
      /**  Reserved for development - date  */  
   "DevDate2":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Withholding Tax Amount  */  
   "ScrWithholdAmt":number,
      /**  Withholding Tax Amount in document currency  */  
   "DocScrWithholdAmt":number,
      /**  Withholding Tax Amount in reporting currency  */  
   "Rpt1ScrWithholdAmt":number,
      /**  Withholding Tax Amount in reporting currency  */  
   "Rpt2ScrWithholdAmt":number,
      /**  Withholding Tax Amount in reporting currency  */  
   "Rpt3ScrWithholdAmt":number,
      /**  Invoice Reference Number  */  
   "InvoiceRef":string,
      /**  AP Transaction Number  */  
   "APTranNo":number,
      /**  DocAdvPayAppliedAmt  */  
   "DocAdvPayAppliedAmt":number,
      /**  1099 Code, defaults from Supplier  */  
   "Code1099ID":string,
      /**  Generated 1099 Code where this invoice was calculated in the 1099 Form  */  
   "Gen1099Code":string,
      /**  FormTypeID  */  
   "FormTypeID":string,
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
      /**  DeferredExp  */  
   "DeferredExp":boolean,
      /**  DEACode  */  
   "DEACode":string,
      /**  DEAAmt  */  
   "DEAAmt":number,
      /**  DEAStartDate  */  
   "DEAStartDate":string,
      /**  DEAEndDate  */  
   "DEAEndDate":string,
      /**  DEDenomination  */  
   "DEDenomination":string,
      /**  This field is used to store the AVP Purchase Order Number.  */  
   "ExternalPONum":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  Malaysia Import Declaration Number  */  
   "MYImportNum":string,
      /**  Flag that indicates if the invoice is the final one for the last partial receipt.  */  
   "FinalInvoice":boolean,
      /**  CommodityCode  */  
   "CommodityCode":string,
      /**  Total Tax Amount  */  
   "TotalTax":number,
      /**  Total Tax Amount  */  
   "DocTotalTax":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotalTax":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotalTax":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotalTax":number,
      /**  Total Self-Assess Tax Amount  */  
   "TotalSATax":number,
      /**  Total Self-Assess Tax Amount  */  
   "DocTotalSATax":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotalSATax":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotalSATax":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotalSATax":number,
      /**  Total Deductible Tax Amount  */  
   "TotalDedTax":number,
      /**  Total Deductible Tax Amount  */  
   "DocTotalDedTax":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotalDedTax":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotalDedTax":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotalDedTax":number,
      /**  Project Billing Invoice Number  */  
   "PBInvNum":number,
      /**  Will be set to Yes if the AP Invoice Dtl was created by the Cancellation logic.  */  
   "CancellationDtl":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  TaxExemptReasonCode  */  
   "TaxExemptReasonCode":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   "ExtSysType":string,
      /**  URL for drill back to an integrated external system  */  
   "ExtSysURL":string,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   "AdjustmentValue":number,
   "AllocationAmount":number,
   "AllocationDesc":string,
   "AllocationID":string,
   "AllowGLDistAdd":boolean,
   "AllowGLDistAllocation":boolean,
   "AllowGLDistDelete":boolean,
   "AllowJobMiscAdd":boolean,
   "AllowJobMiscDelete":boolean,
   "AllowJobMiscUpdate":boolean,
   "BaseCurrencyID":string,
   "BaseCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencyID":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
   "DEACodeDesc":string,
      /**  Is Deferred Expense Amortization Scheduled  */  
   "DEAScheduled":boolean,
   "DebitMemo":boolean,
      /**  DEA Distributed Amount  */  
   "Distributed":number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   "DocAdjustmentValue":number,
   "DocAllocationAmount":number,
      /**  DEA Distributed Amount in Doc Currency  */  
   "DocDistributed":number,
   "DocDspLineTotal":number,
      /**  DEA Expense Amount in Doc Currency  */  
   "DocExpense":number,
   "DocGLLineTotal":number,
   "DocInTaxAmt":number,
   "DocLineExpenses":number,
   "DocLineSubtotal":number,
   "DocLineTotal":number,
   "DocNonDeducTaxExpense":number,
      /**  Value of original Ext Cost in document currency. Used for adjustment lines.  */  
   "DocOrgExtCost":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "DocPEDetAmt":number,
      /**  DEA Recognized Amount in Doc Currency  */  
   "DocRecognized":number,
      /**  DEA Remaining Amount in Doc Currency  */  
   "DocRemaining":number,
   "DocScrInvoiceBal":number,
   "DocScrTotalDedTax":number,
   "DocScrTotalSATax":number,
   "DocScrTotalTax":number,
   "DocScrUnitCost":number,
      /**  This is the value of the lines that have been entered. In Document Currency  */  
   "DocTotDistribAmt":number,
      /**  DEA Unrecognized Amount in Doc Currency  */  
   "DocUnrecognized":number,
   "DocVariance":number,
      /**  Drop Shipment  */  
   "DropShipment":boolean,
   "DspAllocationAmount":number,
   "DspLineTotal":number,
   "EnableDiscountAmt":boolean,
      /**  Indicates if intrastat is available for the line.  */  
   "EnableIntrastat":boolean,
      /**  Indicates if intrastat is available for to be diplayed for the line. Used by AP invoice tracker  */  
   "EnableIntrastatDsp":boolean,
   "EnablePurchaseCode":boolean,
      /**  Indicates if Override Reverse Charge check box should be enabled.  */  
   "EnableRevCharge":boolean,
   "EnableScrWithholdAmt":boolean,
   "EnableShipmentID":boolean,
   "EnableSubCData":boolean,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   "EnableSupplierXRef":boolean,
      /**  DEA Expense Amount  */  
   "Expense":number,
   "GLAccount":string,
   "GLLineTotal":number,
      /**  The VenPartNum field for the datagrid.  For display purposes only.  */  
   "GridVenPartNum":string,
   "GroupID":string,
   "InPrice":boolean,
   "InTaxAmt":number,
      /**  To determine if line have Advance Billing Line  */  
   "IsAdvance":boolean,
      /**  Japan Tax Adjustment Line  */  
   "JPTaxAdjustment":boolean,
   "LineExpenses":number,
   "LineSubtotal":number,
   "LineTotal":number,
   "LineTypeDescription":string,
   "NonDeducTaxExpense":number,
      /**  Value of original Ext Cost in base currency. Used for adjustment lines.  */  
   "OrgExtCost":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "PEDetAmt":number,
   "POCostPerCode":string,
   "PODocUnitCost":number,
   "POLineDesc":string,
   "POPartNum":string,
   "POPUM":string,
   "POReceivedQty":number,
      /**  PO Rel Our UOM  */  
   "PORelIUM":string,
      /**  PO Rel Our Quantity  */  
   "PORelOurQty":number,
   "PORelQty":number,
   "Posted":boolean,
   "POUnitCost":number,
   "POVenPartNum":string,
   "POWarn":string,
      /**  Print 1099  */  
   "Print1099":boolean,
   "RcptDestination":string,
      /**  Receipt Our UOM  */  
   "RcptIUM":string,
      /**  Receipt Our Quantity  */  
   "RcptOurQty":number,
   "RcptPartDescription":string,
   "RcptPartNum":string,
   "RcptPUM":string,
   "RcptReceiptDate":string,
   "RcptVendorQty":number,
   "RcptVenPartNum":string,
   "RecalcGLAcct":boolean,
      /**  DEA Recognized Amount  */  
   "Recognized":number,
      /**  DEA Remaining Amount  */  
   "Remaining":number,
      /**  Reverse Charge Method description  */  
   "RevChargeMethodDesc":string,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   "Rpt1AdjustmentValue":number,
   "Rpt1AllocationAmount":number,
      /**  DEA Distributed Amount in Rpt1 Currency  */  
   "Rpt1Distributed":number,
   "Rpt1DspLineTotal":number,
      /**  DEA Expense Amount in Rpt1 Currency  */  
   "Rpt1Expense":number,
   "Rpt1GLLineTotal":number,
   "Rpt1InTaxAmt":number,
   "Rpt1LineExpenses":number,
   "Rpt1LineSubTotal":number,
   "Rpt1LineTotal":number,
   "Rpt1NonDeducTaxExpense":number,
      /**  Value of original Ext Cost in reporting currency. Used for adjustment lines.  */  
   "Rpt1OrgExtCost":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt1PEDetAmt":number,
   "Rpt1POUnitCost":number,
      /**  DEA Recognized Amount in Rpt1 Currency  */  
   "Rpt1Recognized":number,
      /**  DEA Remaining Amount in Rpt1 Currency  */  
   "Rpt1Remaining":number,
   "Rpt1ScrExtCost":number,
   "Rpt1ScrInvoiceBal":number,
   "Rpt1ScrLineDiscAmt":number,
   "Rpt1ScrTotalDedTax":number,
   "Rpt1ScrTotalMiscChrg":number,
   "Rpt1ScrTotalSATax":number,
   "Rpt1ScrTotalTax":number,
   "Rpt1ScrUnitCost":number,
      /**  This is the value of the lines that have been entered. In Reportable currency 1.  */  
   "Rpt1TotDistribAmt":number,
      /**  DEA Unrecognized Amount in Rpt1 Currency  */  
   "Rpt1Unrecognized":number,
   "Rpt1Variance":number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   "Rpt2AdjustmentValue":number,
   "Rpt2AllocationAmount":number,
      /**  DEA Distributed Amount in Rpt2 Currency  */  
   "Rpt2Distributed":number,
   "Rpt2DspLineTotal":number,
      /**  DEA Expense Amount in Rpt2 Currency  */  
   "Rpt2Expense":number,
   "Rpt2GLLineTotal":number,
   "Rpt2InTaxAmt":number,
   "Rpt2LineExpenses":number,
   "Rpt2LineSubtotal":number,
   "Rpt2LineTotal":number,
   "Rpt2NonDeducTaxExpense":number,
      /**  Value of original Ext Cost in reporting currency. Used for adjustment lines.  */  
   "Rpt2OrgExtCost":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt2PEDetAmt":number,
   "Rpt2POUnitCost":number,
      /**  DEA Recognized Amount in Rpt2 Currency  */  
   "Rpt2Recognized":number,
      /**  DEA Remaining Amount in Rpt2 Currency  */  
   "Rpt2Remaining":number,
   "Rpt2ScrExtCost":number,
   "Rpt2ScrInvoiceBal":number,
   "Rpt2ScrLineDiscAmt":number,
   "Rpt2ScrTotalDedTax":number,
   "Rpt2ScrTotalMiscChrg":number,
   "Rpt2ScrTotalSATax":number,
   "Rpt2ScrTotalTax":number,
   "Rpt2ScrUnitCost":number,
      /**  This is the value of the lines that have been entered. In Reportable currency 2.  */  
   "Rpt2TotDistribAmt":number,
      /**  DEA Unrecognized Amount in Rpt2 Currency  */  
   "Rpt2Unrecognized":number,
   "Rpt2Variance":number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   "Rpt3AdjustmentValue":number,
   "Rpt3AllocationAmount":number,
      /**  DEA Distributed Amount in Rpt3 Currency  */  
   "Rpt3Distributed":number,
   "Rpt3DspLineTotal":number,
      /**  DEA Expense Amount in Rpt3 Currency  */  
   "Rpt3Expense":number,
   "Rpt3GLLineTotal":number,
   "Rpt3InTaxAmt":number,
   "Rpt3LineExpenses":number,
   "Rpt3LineSubtotal":number,
   "Rpt3LineTotal":number,
   "Rpt3NonDeducTaxExpense":number,
      /**  Value of original Ext Cost in reporting currency. Used for adjustment lines.  */  
   "Rpt3OrgExtCost":number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   "Rpt3PEDetAmt":number,
   "Rpt3POUnitCost":number,
      /**  DEA Recognized Amount in Rpt3 Currency  */  
   "Rpt3Recognized":number,
      /**  DEA Remaining Amount in Rpt3 Currency  */  
   "Rpt3Remaining":number,
   "Rpt3ScrExtCost":number,
   "Rpt3ScrInvoiceBal":number,
   "Rpt3ScrLineDiscAmt":number,
   "Rpt3ScrTotalDedTax":number,
   "Rpt3ScrTotalMiscChrg":number,
   "Rpt3ScrTotalSATax":number,
   "Rpt3ScrTotalTax":number,
   "Rpt3ScrUnitCost":number,
      /**  This is the value of the lines that have been entered. In Reportable currency 3.  */  
   "Rpt3TotDistribAmt":number,
      /**  DEA Unrecognized Amount in Rpt3 Currency  */  
   "Rpt3Unrecognized":number,
   "Rpt3Variance":number,
   "ScrDocExtCost":number,
   "ScrDocLineDiscAmt":number,
   "ScrDocTotalMiscChrg":number,
   "ScrExtCost":number,
   "ScrInvoiceBal":number,
      /**  Invoice ref for BOE  */  
   "ScrInvoiceRef":string,
   "ScrLineDiscAmt":number,
   "ScrLineType":string,
   "ScrOurQty":number,
   "ScrTotalDedTax":number,
   "ScrTotalMiscChrg":number,
   "ScrTotalSATax":number,
   "ScrTotalTax":number,
   "ScrUnitCost":number,
   "ScrVendorQty":number,
      /**  This is the value of the lines that have been entered. In Base Currency  */  
   "TotDistribAmt":number,
      /**  DEA Unrecognized Amount  */  
   "Unrecognized":number,
      /**  Indicates if line GL should be automatically created when running UpdateExt.  */  
   "UpdateExtCreateLineGL":boolean,
   "UsePurchaseCode":boolean,
   "Variance":number,
      /**  Indicates that  if LineType=R, then override standard UpdateExt logic to create APInvDtl data directly, as is done in the UI.  Before/AfterGetNew, Before/AfterUpdate will not run.  */  
   "UpdateExtOverrideRcpts":boolean,
      /**  SysRowID of the related RcvDtl row for receipt line,  LineType = R  */  
   "RelatedToRcvDtlSysRowID":string,
   "EnableAttributeSetBtn":boolean,
      /**  DEPayStatCode Description  */  
   "DEPayStatCodeDescr":string,
      /**  DEDenomination Description  */  
   "DEDenominationDescr":string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   "PORevisionNum":string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   "RcptRevisionNum":string,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "AssetNumAssetDescription":string,
   "Code1099Description":string,
   "CommodityCodeDescription":string,
   "ContainerIDContainerDescription":string,
   "FormTypeDescription":string,
   "GLPurchPurchDesc":string,
   "InvoiceNumDebitMemo":boolean,
   "InvoiceNumPosted":boolean,
   "InvoiceNumDescription":string,
   "InvoiceNumCurrencyCode":string,
   "JobNumPartDescription":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackLots":boolean,
   "PartNumPricePerCode":string,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumSalesUM":string,
   "PartNumAttrClassID":string,
   "POLineLineDesc":string,
   "POLineVenPartNum":string,
   "POLinePartNum":string,
   "TaxCatIDDescription":string,
   "VendorNumName":string,
   "VendorNumAddress2":string,
   "VendorNumCountry":string,
   "VendorNumCity":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumState":string,
   "VendorNumTermsCode":string,
   "VendorNumVendorID":string,
   "VendorNumAddress3":string,
   "VendorNumZIP":string,
   "VendorNumAddress1":string,
   "VendorPPName":string,
   "vrPONumShipToConName":string,
   "vrPONumShipName":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param vendorNum
      @param invoiceNum
      @param invoiceLine
   */  
export interface DeleteByID_input{
   vendorNum:number,
   invoiceNum:string,
   invoiceLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_APInvDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  */  
   VendorNum:number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   InvoiceNum:string,
      /**  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  */  
   InvoiceLine:number,
      /**  Indicates the type of invoice line. "R" = Invoiced for Receipt of goods, "A" - Advance Billing,  "M" - Misc. Billing, "U" - Unreceived goods, "J" - Job Miscellaneous charge A/P invoice, "S" - Asset Invoice Line.  Not directly entered,  set by invoice entry by the user selecting the appropriate menu option.  */  
   LineType:string,
      /**  item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost if related.  */  
   UnitCost:number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   DocUnitCost:number,
      /**  Part number used to identify line item part.  */  
   PartNum:string,
      /**   Purchase Order Number that this invoice line item is related to. If packing slip is referenced then it is set = to RcvDtl.PONum and can't be changed.  If entered it must be a valid POHeader record.
A reference is made to the purchase order using PONUM, POLine and PORelNum fields. If any one of these fields are entered then they all must be entered and be valid.  */  
   PONum:number,
      /**  The PO line # that invoice is for. Defaulted from the RvcDtl if referenced to packing slip document.. Only applicable when PO is referenced.  */  
   POLine:number,
      /**  Purchase Order Release # which is being invoiced. Defaulted from RcvDtl if related to a packing slip. If entered it Must be valid.  */  
   PORelNum:number,
      /**  Invoice line description.  */  
   Description:string,
      /**  Job that this invoice is related to. Set to the RcvDtl.JobNum.  */  
   JobNum:string,
      /**  Job Assembly Sequence that this invoice line is related to. Set to RcvDtl.AssemblySeq.  */  
   AssemblySeq:number,
      /**  Indicates if this invoice line is related to a job material (jobmtl) or job subcontract (JobOper) record. Valid values are "M" = material or "S" = subcontract. This is set to RvcDtl.JobSeqType.  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record to which this line item is costed against. Defaults from the RcvDtl.JobSeq. Only applicable for a receipts to job.  */  
   JobSeq:number,
      /**  The Vendor's purchase point ID. This is used as part of the foreign key to reference the RcvHead/RcvDtl records.  */  
   PurPoint:string,
      /**  Vendor's packing slip that this A\P invoice detail line is associated with. This Along with PackLine provides a relationship to the receipt document detail (RcvDtl)  */  
   PackSlip:string,
      /**  The Pack Slip line of the RcvDtl record  to which this A\P detail record is related to.  */  
   PackLine:number,
      /**  Total Invoiced Quantity for the line item.  This is stored in the Vendors Unit of Measure.  Can be defaulted from the packing slip detail if referenced (RcvDtl.POReceiptQty)  */  
   VendorQty:number,
      /**  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDel.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  */  
   PUM:string,
      /**  Invoiced Quantity for the line item in our unit of measure. This can be defaulted from the packing slip detail if referenced (RcvDtl.ReceiptQty)  */  
   OurQty:number,
      /**  Unit of Measure code for invoiced quantity in our unit of measure. Defaulted in the following hierarchy: from the RcvDel.IUM if packing slip is referenced, from PODetail.IUM if PO is referenced, from Part.IUM if valid part or finally from XaSyst.DefaultUM.  */  
   IUM:string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the APInvDtl.VendorQty by the appropriate "per" value and then multiply by unit cost.  Use the PODetail.CostPerCode if related to a PO else use Part.PricePerCode if valid part. Else default as "E".
Valid database values are "E" = Each, "C" = per 100 or "M" = per 1,000.  */  
   CostPerCode:string,
      /**  Vendor's part number. Optional, defaults from the RcvDtl, PODetail or blank.  */  
   VenPartNum:string,
      /**  Extended Cost for the invoice line item. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  */  
   ExtCost:number,
      /**  Extended Cost for the invoice line item in Vendors currency. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  */  
   DocExtCost:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   TotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line in vendors currency.  */  
   DocTotalMiscChrg:number,
      /**  Used to establish invoice comments about the invoice line.  */  
   LineComment:string,
      /**  Mirror image of related RCVHead.ReceiptDate.  Only applies to LineType = U. Updated during the Invoice/Receipt match posting process if GLSyst.PostInvtyWipCos = No.  This date is used as the journal date and to determine the fiscal period when the Invoice/Receipt process is responsible for generating the GL entries. (See CaMatchingDiv description)  */  
   MatchDate:string,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   MatchFiscalYear:number,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   MatchFiscalPeriod:number,
      /**  Indicates if this item is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info.  */  
   TaxExempt:string,
      /**  Indicates the Tax Category for this line item.  Defaults from the Part Master.  */  
   TaxCatID:string,
      /**  The amount this line item that is reduced by due to prior advanced payments.    It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  */  
   AdvancePayAmt:number,
      /**  The amount this line item that is reduced by due to prior advanced payments.   It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  */  
   DocAdvancePayAmt:number,
      /**  Purchase Code.  */  
   PurchCode:string,
      /**  Discount amount for this line  */  
   LineDiscAmt:number,
      /**  Discount amount (Vendors Currency) for this line  */  
   DocLineDiscAmt:number,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceNum:string,
      /**  Global Invoice Line identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceLine:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   AdvGainLoss:number,
      /**  Flag to indicate that G/L entries appearing under this invoice line will have multi-company journals entered at the target external company.  */  
   MultiCompany:boolean,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line.  */  
   RevChargeMethod:string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   OverrideReverseCharge:boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   RevChargeApplied:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AdvancePayAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2AdvancePayAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3AdvancePayAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1LineDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2LineDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3LineDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitCost:number,
      /**  Amount of advance payment applied  */  
   DocAdvPayAppld:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3AdvGainLoss:number,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   MatchFiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   MatchFiscalCalendarID:string,
      /**  The Tax Region for this invoice.  */  
   TaxRegionCode:string,
      /**  The Supplier Shipment ID (also known as the ContainerID).  */  
   ContainerID:number,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  */  
   CorrectionDtl:boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  Asset number of the linked Asset Addition transaction.  */  
   AssetNum:string,
      /**  Addition Number or sequence of the linked Asset Addition transaction.  */  
   AdditionNum:number,
      /**  Used in a correction invoice to store reference to the original invoice line.  */  
   InvoiceLineRef:number,
      /**  This is the current invoice line balance (in vendor currency) left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance of this DocAssetInvoiceBal.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  */  
   DocAssetInvoiceBal:number,
      /**  This is the Invoiced Quantity balance left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  This qty is expressed in our unit of measure.  */  
   AssetBalOurQty:number,
      /**  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  */  
   AssetQtyIUM:string,
      /**  The DMR Number that requires supplier credit.  */  
   DMRNum:number,
      /**  The Action Number for the DMR that requires supplier credit.  */  
   DMRActionNum:number,
      /**  Indicates if this invoice line was created from an EmpExpense record.  */  
   CreatedFromExpense:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Generated 1099 Code where this invoice was calculated in the 1099 Form  */  
   Gen1099Code:string,
      /**  Indicates if intrastat is available for the line.  */  
   EnableIntrastat:boolean,
   CurrencySwitch:boolean,
   BaseCurrSymbol:string,
   CurrSymbol:string,
   ScrExtCost:number,
   ScrDocExtCost:number,
   ScrTotalMiscChrg:number,
   ScrDocTotalMiscChrg:number,
   ScrLineType:string,
   DebitMemo:boolean,
   Variance:number,
   EnablePurchaseCode:boolean,
   EnableDiscountAmt:boolean,
   UsePurchaseCode:boolean,
   LineSubtotal:number,
   DocLineSubtotal:number,
   LineTotal:number,
   DocLineTotal:number,
   ScrVendorQty:number,
   ScrOurQty:number,
   AllowGLDistAdd:boolean,
   AllowGLDistAllocation:boolean,
   AllowGLDistDelete:boolean,
   ScrLineDiscAmt:number,
   ScrDocLineDiscAmt:number,
   AllowJobMiscAdd:boolean,
   AllowJobMiscDelete:boolean,
   AllowJobMiscUpdate:boolean,
   AllocationID:string,
   AllocationAmount:number,
   RcptReceiptDate:string,
   RcptPartNum:string,
   RcptPartDescription:string,
   RcptDestination:string,
   RcptVenPartNum:string,
   RcptVendorQty:number,
   POPartNum:string,
   POLineDesc:string,
   PORelQty:number,
   POReceivedQty:number,
   POVenPartNum:string,
   POUnitCost:number,
   PODocUnitCost:number,
   POCostPerCode:string,
      /**  The VenPartNum field for the datagrid.  For display purposes only.  */  
   GridVenPartNum:string,
   RcptPUM:string,
   POPUM:string,
   Posted:boolean,
   LineTypeDescription:string,
   GroupID:string,
   AllocationDesc:string,
      /**  Indicates if Override Reverse Charge check box should be enabled.  */  
   EnableRevCharge:boolean,
      /**  Reverse Charge Method description  */  
   RevChargeMethodDesc:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   Rpt1ScrExtCost:number,
   Rpt2ScrExtCost:number,
   Rpt3ScrExtCost:number,
   Rpt1ScrTotalMiscChrg:number,
   Rpt2ScrTotalMiscChrg:number,
   Rpt3ScrTotalMiscChrg:number,
   Rpt1ScrLineDiscAmt:number,
   Rpt2ScrLineDiscAmt:number,
   Rpt3ScrLineDiscAmt:number,
   Rpt1LineSubTotal:number,
   Rpt2LineSubtotal:number,
   Rpt3LineSubtotal:number,
   Rpt1LineTotal:number,
   Rpt2LineTotal:number,
   Rpt3LineTotal:number,
      /**  Receipt Our UOM  */  
   RcptIUM:string,
      /**  Receipt Our Quantity  */  
   RcptOurQty:number,
      /**  PO Rel Our Quantity  */  
   PORelOurQty:number,
      /**  PO Rel Our UOM  */  
   PORelIUM:string,
   Rpt1POUnitCost:number,
   Rpt2POUnitCost:number,
   Rpt3POUnitCost:number,
      /**  Drop Shipment  */  
   DropShipment:boolean,
   EnableShipmentID:boolean,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   EnableSupplierXRef:boolean,
      /**  This is the value of the lines that have been entered. In Base Currency  */  
   TotDistribAmt:number,
      /**  This is the value of the lines that have been entered. In Document Currency  */  
   DocTotDistribAmt:number,
      /**  This is the value of the lines that have been entered. In Reportable currency 1.  */  
   Rpt1TotDistribAmt:number,
      /**  This is the value of the lines that have been entered. In Reportable currency 2.  */  
   Rpt2TotDistribAmt:number,
      /**  This is the value of the lines that have been entered. In Reportable currency 3.  */  
   Rpt3TotDistribAmt:number,
   EnableSubCData:boolean,
   POWarn:string,
   CurrencyID:string,
   BaseCurrencyID:string,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   AdjustmentValue:number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   DocAdjustmentValue:number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   Rpt1AdjustmentValue:number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   Rpt2AdjustmentValue:number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   Rpt3AdjustmentValue:number,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  Mandatory description of the asset.  */  
   AssetNumAssetDescription:string,
      /**  Free form text that describes this particular container.  */  
   ContainerIDContainerDescription:string,
      /**  Description of the purchase type. Appears in drop-down lists for selection.  */  
   GLPurchPurchDesc:string,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   InvoiceNumDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
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
      /**  OUR internal Part number for this item.  */  
   POLinePartNum:string,
      /**  Supplier Part Number  */  
   POLineVenPartNum:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   POLineLineDesc:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   PORelNumRefCodeDesc:string,
      /**  Full description for the Sales Tax category.  */  
   TaxCatIDDescription:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  defaults from the company file.  */  
   vrPONumShipName:string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   vrPONumShipToConName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvDtlListTableset{
   APInvDtlList:Erp_Tablesets_APInvDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APInvDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  VendorNum duplicated from the corresponding APInvHed record.  Not directly maintainable by the operator.  */  
   VendorNum:number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   InvoiceNum:string,
      /**  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  */  
   InvoiceLine:number,
      /**  Indicates the type of invoice line. "R" = Invoiced for Receipt of goods, "A" - Advance Billing,  "M" - Misc. Billing, "U" - Unreceived goods, "J" - Job Miscellaneous charge A/P invoice, "S" - Asset Invoice Line.  Not directly entered,  set by invoice entry by the user selecting the appropriate menu option.  */  
   LineType:string,
      /**  item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost if related.  */  
   UnitCost:number,
      /**  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  */  
   DocUnitCost:number,
      /**  Part number used to identify line item part.  */  
   PartNum:string,
      /**   Purchase Order Number that this invoice line item is related to. If packing slip is referenced then it is set = to RcvDtl.PONum and can't be changed.  If entered it must be a valid POHeader record.
A reference is made to the purchase order using PONUM, POLine and PORelNum fields. If any one of these fields are entered then they all must be entered and be valid.  */  
   PONum:number,
      /**  The PO line # that invoice is for. Defaulted from the RvcDtl if referenced to packing slip document.. Only applicable when PO is referenced.  */  
   POLine:number,
      /**  Purchase Order Release # which is being invoiced. Defaulted from RcvDtl if related to a packing slip. If entered it Must be valid.  */  
   PORelNum:number,
      /**  Invoice line description.  */  
   Description:string,
      /**  Job that this invoice is related to. Set to the RcvDtl.JobNum.  */  
   JobNum:string,
      /**  Job Assembly Sequence that this invoice line is related to. Set to RcvDtl.AssemblySeq.  */  
   AssemblySeq:number,
      /**  Indicates if this invoice line is related to a job material (jobmtl) or job subcontract (JobOper) record. Valid values are "M" = material or "S" = subcontract. This is set to RvcDtl.JobSeqType.  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record to which this line item is costed against. Defaults from the RcvDtl.JobSeq. Only applicable for a receipts to job.  */  
   JobSeq:number,
      /**  The Vendor's purchase point ID. This is used as part of the foreign key to reference the RcvHead/RcvDtl records.  */  
   PurPoint:string,
      /**  Vendor's packing slip that this A\P invoice detail line is associated with. This Along with PackLine provides a relationship to the receipt document detail (RcvDtl)  */  
   PackSlip:string,
      /**  The Pack Slip line of the RcvDtl record  to which this A\P detail record is related to.  */  
   PackLine:number,
      /**  Total Invoiced Quantity for the line item.  This is stored in the Vendors Unit of Measure.  Can be defaulted from the packing slip detail if referenced (RcvDtl.POReceiptQty)  */  
   VendorQty:number,
      /**  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDel.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  */  
   PUM:string,
      /**  Invoiced Quantity for the line item in our unit of measure. This can be defaulted from the packing slip detail if referenced (RcvDtl.ReceiptQty)  */  
   OurQty:number,
      /**  Unit of Measure code for invoiced quantity in our unit of measure. Defaulted in the following hierarchy: from the RcvDel.IUM if packing slip is referenced, from PODetail.IUM if PO is referenced, from Part.IUM if valid part or finally from XaSyst.DefaultUM.  */  
   IUM:string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the APInvDtl.VendorQty by the appropriate "per" value and then multiply by unit cost.  Use the PODetail.CostPerCode if related to a PO else use Part.PricePerCode if valid part. Else default as "E".
Valid database values are "E" = Each, "C" = per 100 or "M" = per 1,000.  */  
   CostPerCode:string,
      /**  Vendor's part number. Optional, defaults from the RcvDtl, PODetail or blank.  */  
   VenPartNum:string,
      /**  Extended Cost for the invoice line item. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  */  
   ExtCost:number,
      /**  Extended Cost for the invoice line item in Vendors currency. Calculated as the (VendorQty/CostPer) * UnitCost or can be directly maintained in which case it recalculates the UnitCost value.  */  
   DocExtCost:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  */  
   TotalMiscChrg:number,
      /**  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line in vendors currency.  */  
   DocTotalMiscChrg:number,
      /**  Used to establish invoice comments about the invoice line.  */  
   LineComment:string,
      /**  Mirror image of related RCVHead.ReceiptDate.  Only applies to LineType = U. Updated during the Invoice/Receipt match posting process if GLSyst.PostInvtyWipCos = No.  This date is used as the journal date and to determine the fiscal period when the Invoice/Receipt process is responsible for generating the GL entries. (See CaMatchingDiv description)  */  
   MatchDate:string,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   MatchFiscalYear:number,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   MatchFiscalPeriod:number,
      /**  Indicates if this item is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info.  */  
   TaxExempt:string,
      /**  Indicates the Tax Category for this line item.  Defaults from the Part Master.  */  
   TaxCatID:string,
      /**  The amount this line item that is reduced by due to prior advanced payments.    It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  */  
   AdvancePayAmt:number,
      /**  The amount this line item that is reduced by due to prior advanced payments.   It is defaulted from the PODetail.AdvancePayBal.  This value reduces the PODetail.AdvancePayBal.  */  
   DocAdvancePayAmt:number,
      /**  Purchase Code.  */  
   PurchCode:string,
      /**  Discount amount for this line  */  
   LineDiscAmt:number,
      /**  Discount amount (Vendors Currency) for this line  */  
   DocLineDiscAmt:number,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceNum:string,
      /**  Global Invoice Line identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceLine:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   AdvGainLoss:number,
      /**  Flag to indicate that G/L entries appearing under this invoice line will have multi-company journals entered at the target external company.  */  
   MultiCompany:boolean,
      /**   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line.  */  
   RevChargeMethod:string,
      /**  Indicates if the user overrides the Reverse Charge Method.  */  
   OverrideReverseCharge:boolean,
      /**  Indicates if Reverse Charge tax line has been applied.  */  
   RevChargeApplied:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AdvancePayAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2AdvancePayAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3AdvancePayAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1LineDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2LineDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3LineDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitCost:number,
      /**  Amount of advance payment applied  */  
   DocAdvPayAppld:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2AdvGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3AdvGainLoss:number,
      /**  Applies only to UnReceived Lines (LineType = U). Update via the Invoice/Receipt Match program when Inventory is NOT interfaced to G/L.  */  
   MatchFiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   MatchFiscalCalendarID:string,
      /**  The Tax Region for this invoice.  */  
   TaxRegionCode:string,
      /**  The Supplier Shipment ID (also known as the ContainerID).  */  
   ContainerID:number,
      /**  Drop Shipment Pack Line  */  
   DropShipPackLine:number,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  */  
   CorrectionDtl:boolean,
      /**  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  Asset number of the linked Asset Addition transaction.  */  
   AssetNum:string,
      /**  Addition Number or sequence of the linked Asset Addition transaction.  */  
   AdditionNum:number,
      /**  Used in a correction invoice to store reference to the original invoice line.  */  
   InvoiceLineRef:number,
      /**  This is the current invoice line balance (in vendor currency) left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance of this DocAssetInvoiceBal.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  */  
   DocAssetInvoiceBal:number,
      /**  This is the Invoiced Quantity balance left to be consumed in the asset addition process.  An asset invoice line can be linked to one or more assets and each asset addition linking to this invoice line will reduce the balance qty of this AssetBalOurQty.  When this field reaches zero then this invoice line cannot be linked in the asset addition anymore.  This qty is expressed in our unit of measure.  */  
   AssetBalOurQty:number,
      /**  Unit of Measure code for asset invoiced quantity balance in our unit of measure.  */  
   AssetQtyIUM:string,
      /**  The DMR Number that requires supplier credit.  */  
   DMRNum:number,
      /**  The Action Number for the DMR that requires supplier credit.  */  
   DMRActionNum:number,
      /**  Indicates if this invoice line was created from an EmpExpense record.  */  
   CreatedFromExpense:boolean,
      /**  item's unit cost in the vendors unit of measure including taxes.  */  
   InUnitCost:number,
      /**  item's unit cost in the vendors unit of measure and currency including taxes.  */  
   DocInUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1InUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2InUnitCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3InUnitCost:number,
      /**  Extended Cost for the invoice line item including taxes.  */  
   InExtCost:number,
      /**   Extended Cost for the invoice line item in Vendors currency
including taxes  */  
   DocInExtCost:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtCost:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtCost:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtCost:number,
      /**  Rolled up total of all misc. charge records for this invoice detail line including taxes.  */  
   InTotalMiscChrg:number,
      /**  Rolled up total of all misc. charge records for this invoice detail line in vendors currency including taxes.  */  
   DocInTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt1InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt2InTotalMiscChrg:number,
      /**  Reporting currency value of this field  */  
   Rpt3InTotalMiscChrg:number,
      /**  The amount this line item that is reduced by due to prior advanced payments (incl taxes).  */  
   InAdvancePayAmt:number,
      /**  The amount this line item that is reduced by due to prior advanced payments (incl taxes).  */  
   DocInAdvancePayAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InAdvancePayAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InAdvancePayAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InAdvancePayAmt:number,
      /**  Discount amount for this line including taxes  */  
   InLineDiscAmt:number,
      /**  Discount amount (Vendors Currency) for this line including taxes  */  
   DocInLineDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InLineDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InLineDiscAmt:number,
   Rpt3InLineDiscAmt:number,
      /**  Indicates if no tax recalculation by the system is  supposed to be done since with "In Price" tax calculation the tax lines were adjusted or new tax lines added manually  */  
   NoTaxRecal:boolean,
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
      /**  Reserved for development  - logical  */  
   DevLog1:boolean,
      /**  Reserved for development - logical  */  
   DevLog2:boolean,
      /**  Reserved for development  - character  */  
   DevChar1:string,
      /**  Reserved for development - character  */  
   DevChar2:string,
      /**  Reserved for development - date  */  
   DevDate1:string,
      /**  Reserved for development - date  */  
   DevDate2:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Withholding Tax Amount  */  
   ScrWithholdAmt:number,
      /**  Withholding Tax Amount in document currency  */  
   DocScrWithholdAmt:number,
      /**  Withholding Tax Amount in reporting currency  */  
   Rpt1ScrWithholdAmt:number,
      /**  Withholding Tax Amount in reporting currency  */  
   Rpt2ScrWithholdAmt:number,
      /**  Withholding Tax Amount in reporting currency  */  
   Rpt3ScrWithholdAmt:number,
      /**  Invoice Reference Number  */  
   InvoiceRef:string,
      /**  AP Transaction Number  */  
   APTranNo:number,
      /**  DocAdvPayAppliedAmt  */  
   DocAdvPayAppliedAmt:number,
      /**  1099 Code, defaults from Supplier  */  
   Code1099ID:string,
      /**  Generated 1099 Code where this invoice was calculated in the 1099 Form  */  
   Gen1099Code:string,
      /**  FormTypeID  */  
   FormTypeID:string,
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
      /**  DeferredExp  */  
   DeferredExp:boolean,
      /**  DEACode  */  
   DEACode:string,
      /**  DEAAmt  */  
   DEAAmt:number,
      /**  DEAStartDate  */  
   DEAStartDate:string,
      /**  DEAEndDate  */  
   DEAEndDate:string,
      /**  DEDenomination  */  
   DEDenomination:string,
      /**  This field is used to store the AVP Purchase Order Number.  */  
   ExternalPONum:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  Malaysia Import Declaration Number  */  
   MYImportNum:string,
      /**  Flag that indicates if the invoice is the final one for the last partial receipt.  */  
   FinalInvoice:boolean,
      /**  CommodityCode  */  
   CommodityCode:string,
      /**  Total Tax Amount  */  
   TotalTax:number,
      /**  Total Tax Amount  */  
   DocTotalTax:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotalTax:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalTax:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalTax:number,
      /**  Total Self-Assess Tax Amount  */  
   TotalSATax:number,
      /**  Total Self-Assess Tax Amount  */  
   DocTotalSATax:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotalSATax:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalSATax:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalSATax:number,
      /**  Total Deductible Tax Amount  */  
   TotalDedTax:number,
      /**  Total Deductible Tax Amount  */  
   DocTotalDedTax:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotalDedTax:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotalDedTax:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotalDedTax:number,
      /**  Project Billing Invoice Number  */  
   PBInvNum:number,
      /**  Will be set to Yes if the AP Invoice Dtl was created by the Cancellation logic.  */  
   CancellationDtl:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  TaxExemptReasonCode  */  
   TaxExemptReasonCode:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   AdjustmentValue:number,
   AllocationAmount:number,
   AllocationDesc:string,
   AllocationID:string,
   AllowGLDistAdd:boolean,
   AllowGLDistAllocation:boolean,
   AllowGLDistDelete:boolean,
   AllowJobMiscAdd:boolean,
   AllowJobMiscDelete:boolean,
   AllowJobMiscUpdate:boolean,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencyID:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DEACodeDesc:string,
      /**  Is Deferred Expense Amortization Scheduled  */  
   DEAScheduled:boolean,
   DebitMemo:boolean,
      /**  DEA Distributed Amount  */  
   Distributed:number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   DocAdjustmentValue:number,
   DocAllocationAmount:number,
      /**  DEA Distributed Amount in Doc Currency  */  
   DocDistributed:number,
   DocDspLineTotal:number,
      /**  DEA Expense Amount in Doc Currency  */  
   DocExpense:number,
   DocGLLineTotal:number,
   DocInTaxAmt:number,
   DocLineExpenses:number,
   DocLineSubtotal:number,
   DocLineTotal:number,
   DocNonDeducTaxExpense:number,
      /**  Value of original Ext Cost in document currency. Used for adjustment lines.  */  
   DocOrgExtCost:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   DocPEDetAmt:number,
      /**  DEA Recognized Amount in Doc Currency  */  
   DocRecognized:number,
      /**  DEA Remaining Amount in Doc Currency  */  
   DocRemaining:number,
   DocScrInvoiceBal:number,
   DocScrTotalDedTax:number,
   DocScrTotalSATax:number,
   DocScrTotalTax:number,
   DocScrUnitCost:number,
      /**  This is the value of the lines that have been entered. In Document Currency  */  
   DocTotDistribAmt:number,
      /**  DEA Unrecognized Amount in Doc Currency  */  
   DocUnrecognized:number,
   DocVariance:number,
      /**  Drop Shipment  */  
   DropShipment:boolean,
   DspAllocationAmount:number,
   DspLineTotal:number,
   EnableDiscountAmt:boolean,
      /**  Indicates if intrastat is available for the line.  */  
   EnableIntrastat:boolean,
      /**  Indicates if intrastat is available for to be diplayed for the line. Used by AP invoice tracker  */  
   EnableIntrastatDsp:boolean,
   EnablePurchaseCode:boolean,
      /**  Indicates if Override Reverse Charge check box should be enabled.  */  
   EnableRevCharge:boolean,
   EnableScrWithholdAmt:boolean,
   EnableShipmentID:boolean,
   EnableSubCData:boolean,
      /**  Use this field to enable\disable the Supplier Part XRef button  */  
   EnableSupplierXRef:boolean,
      /**  DEA Expense Amount  */  
   Expense:number,
   GLAccount:string,
   GLLineTotal:number,
      /**  The VenPartNum field for the datagrid.  For display purposes only.  */  
   GridVenPartNum:string,
   GroupID:string,
   InPrice:boolean,
   InTaxAmt:number,
      /**  To determine if line have Advance Billing Line  */  
   IsAdvance:boolean,
      /**  Japan Tax Adjustment Line  */  
   JPTaxAdjustment:boolean,
   LineExpenses:number,
   LineSubtotal:number,
   LineTotal:number,
   LineTypeDescription:string,
   NonDeducTaxExpense:number,
      /**  Value of original Ext Cost in base currency. Used for adjustment lines.  */  
   OrgExtCost:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   PEDetAmt:number,
   POCostPerCode:string,
   PODocUnitCost:number,
   POLineDesc:string,
   POPartNum:string,
   POPUM:string,
   POReceivedQty:number,
      /**  PO Rel Our UOM  */  
   PORelIUM:string,
      /**  PO Rel Our Quantity  */  
   PORelOurQty:number,
   PORelQty:number,
   Posted:boolean,
   POUnitCost:number,
   POVenPartNum:string,
   POWarn:string,
      /**  Print 1099  */  
   Print1099:boolean,
   RcptDestination:string,
      /**  Receipt Our UOM  */  
   RcptIUM:string,
      /**  Receipt Our Quantity  */  
   RcptOurQty:number,
   RcptPartDescription:string,
   RcptPartNum:string,
   RcptPUM:string,
   RcptReceiptDate:string,
   RcptVendorQty:number,
   RcptVenPartNum:string,
   RecalcGLAcct:boolean,
      /**  DEA Recognized Amount  */  
   Recognized:number,
      /**  DEA Remaining Amount  */  
   Remaining:number,
      /**  Reverse Charge Method description  */  
   RevChargeMethodDesc:string,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   Rpt1AdjustmentValue:number,
   Rpt1AllocationAmount:number,
      /**  DEA Distributed Amount in Rpt1 Currency  */  
   Rpt1Distributed:number,
   Rpt1DspLineTotal:number,
      /**  DEA Expense Amount in Rpt1 Currency  */  
   Rpt1Expense:number,
   Rpt1GLLineTotal:number,
   Rpt1InTaxAmt:number,
   Rpt1LineExpenses:number,
   Rpt1LineSubTotal:number,
   Rpt1LineTotal:number,
   Rpt1NonDeducTaxExpense:number,
      /**  Value of original Ext Cost in reporting currency. Used for adjustment lines.  */  
   Rpt1OrgExtCost:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt1PEDetAmt:number,
   Rpt1POUnitCost:number,
      /**  DEA Recognized Amount in Rpt1 Currency  */  
   Rpt1Recognized:number,
      /**  DEA Remaining Amount in Rpt1 Currency  */  
   Rpt1Remaining:number,
   Rpt1ScrExtCost:number,
   Rpt1ScrInvoiceBal:number,
   Rpt1ScrLineDiscAmt:number,
   Rpt1ScrTotalDedTax:number,
   Rpt1ScrTotalMiscChrg:number,
   Rpt1ScrTotalSATax:number,
   Rpt1ScrTotalTax:number,
   Rpt1ScrUnitCost:number,
      /**  This is the value of the lines that have been entered. In Reportable currency 1.  */  
   Rpt1TotDistribAmt:number,
      /**  DEA Unrecognized Amount in Rpt1 Currency  */  
   Rpt1Unrecognized:number,
   Rpt1Variance:number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   Rpt2AdjustmentValue:number,
   Rpt2AllocationAmount:number,
      /**  DEA Distributed Amount in Rpt2 Currency  */  
   Rpt2Distributed:number,
   Rpt2DspLineTotal:number,
      /**  DEA Expense Amount in Rpt2 Currency  */  
   Rpt2Expense:number,
   Rpt2GLLineTotal:number,
   Rpt2InTaxAmt:number,
   Rpt2LineExpenses:number,
   Rpt2LineSubtotal:number,
   Rpt2LineTotal:number,
   Rpt2NonDeducTaxExpense:number,
      /**  Value of original Ext Cost in reporting currency. Used for adjustment lines.  */  
   Rpt2OrgExtCost:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt2PEDetAmt:number,
   Rpt2POUnitCost:number,
      /**  DEA Recognized Amount in Rpt2 Currency  */  
   Rpt2Recognized:number,
      /**  DEA Remaining Amount in Rpt2 Currency  */  
   Rpt2Remaining:number,
   Rpt2ScrExtCost:number,
   Rpt2ScrInvoiceBal:number,
   Rpt2ScrLineDiscAmt:number,
   Rpt2ScrTotalDedTax:number,
   Rpt2ScrTotalMiscChrg:number,
   Rpt2ScrTotalSATax:number,
   Rpt2ScrTotalTax:number,
   Rpt2ScrUnitCost:number,
      /**  This is the value of the lines that have been entered. In Reportable currency 2.  */  
   Rpt2TotDistribAmt:number,
      /**  DEA Unrecognized Amount in Rpt2 Currency  */  
   Rpt2Unrecognized:number,
   Rpt2Variance:number,
      /**  Fields to show difference in ExtCost between adjustment line and original line.  */  
   Rpt3AdjustmentValue:number,
   Rpt3AllocationAmount:number,
      /**  DEA Distributed Amount in Rpt3 Currency  */  
   Rpt3Distributed:number,
   Rpt3DspLineTotal:number,
      /**  DEA Expense Amount in Rpt3 Currency  */  
   Rpt3Expense:number,
   Rpt3GLLineTotal:number,
   Rpt3InTaxAmt:number,
   Rpt3LineExpenses:number,
   Rpt3LineSubtotal:number,
   Rpt3LineTotal:number,
   Rpt3NonDeducTaxExpense:number,
      /**  Value of original Ext Cost in reporting currency. Used for adjustment lines.  */  
   Rpt3OrgExtCost:number,
      /**  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  */  
   Rpt3PEDetAmt:number,
   Rpt3POUnitCost:number,
      /**  DEA Recognized Amount in Rpt3 Currency  */  
   Rpt3Recognized:number,
      /**  DEA Remaining Amount in Rpt3 Currency  */  
   Rpt3Remaining:number,
   Rpt3ScrExtCost:number,
   Rpt3ScrInvoiceBal:number,
   Rpt3ScrLineDiscAmt:number,
   Rpt3ScrTotalDedTax:number,
   Rpt3ScrTotalMiscChrg:number,
   Rpt3ScrTotalSATax:number,
   Rpt3ScrTotalTax:number,
   Rpt3ScrUnitCost:number,
      /**  This is the value of the lines that have been entered. In Reportable currency 3.  */  
   Rpt3TotDistribAmt:number,
      /**  DEA Unrecognized Amount in Rpt3 Currency  */  
   Rpt3Unrecognized:number,
   Rpt3Variance:number,
   ScrDocExtCost:number,
   ScrDocLineDiscAmt:number,
   ScrDocTotalMiscChrg:number,
   ScrExtCost:number,
   ScrInvoiceBal:number,
      /**  Invoice ref for BOE  */  
   ScrInvoiceRef:string,
   ScrLineDiscAmt:number,
   ScrLineType:string,
   ScrOurQty:number,
   ScrTotalDedTax:number,
   ScrTotalMiscChrg:number,
   ScrTotalSATax:number,
   ScrTotalTax:number,
   ScrUnitCost:number,
   ScrVendorQty:number,
      /**  This is the value of the lines that have been entered. In Base Currency  */  
   TotDistribAmt:number,
      /**  DEA Unrecognized Amount  */  
   Unrecognized:number,
      /**  Indicates if line GL should be automatically created when running UpdateExt.  */  
   UpdateExtCreateLineGL:boolean,
   UsePurchaseCode:boolean,
   Variance:number,
      /**  Indicates that  if LineType=R, then override standard UpdateExt logic to create APInvDtl data directly, as is done in the UI.  Before/AfterGetNew, Before/AfterUpdate will not run.  */  
   UpdateExtOverrideRcpts:boolean,
      /**  SysRowID of the related RcvDtl row for receipt line,  LineType = R  */  
   RelatedToRcvDtlSysRowID:string,
   EnableAttributeSetBtn:boolean,
      /**  DEPayStatCode Description  */  
   DEPayStatCodeDescr:string,
      /**  DEDenomination Description  */  
   DEDenominationDescr:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   PORevisionNum:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RcptRevisionNum:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   AssetNumAssetDescription:string,
   Code1099Description:string,
   CommodityCodeDescription:string,
   ContainerIDContainerDescription:string,
   FormTypeDescription:string,
   GLPurchPurchDesc:string,
   InvoiceNumDebitMemo:boolean,
   InvoiceNumPosted:boolean,
   InvoiceNumDescription:string,
   InvoiceNumCurrencyCode:string,
   JobNumPartDescription:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumAttrClassID:string,
   POLineLineDesc:string,
   POLineVenPartNum:string,
   POLinePartNum:string,
   TaxCatIDDescription:string,
   VendorNumName:string,
   VendorNumAddress2:string,
   VendorNumCountry:string,
   VendorNumCity:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumState:string,
   VendorNumTermsCode:string,
   VendorNumVendorID:string,
   VendorNumAddress3:string,
   VendorNumZIP:string,
   VendorNumAddress1:string,
   VendorPPName:string,
   vrPONumShipToConName:string,
   vrPONumShipName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvDtlSearchTableset{
   APInvDtl:Erp_Tablesets_APInvDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtAPInvDtlSearchTableset{
   APInvDtl:Erp_Tablesets_APInvDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param vendorNum
      @param invoiceNum
      @param invoiceLine
   */  
export interface GetByID_input{
   vendorNum:number,
   invoiceNum:string,
   invoiceLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_APInvDtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_APInvDtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_APInvDtlSearchTableset[],
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
   returnObj:Erp_Tablesets_APInvDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param invoiceNum
   */  
export interface GetNewAPInvDtl_input{
   ds:Erp_Tablesets_APInvDtlSearchTableset[],
   vendorNum:number,
   invoiceNum:string,
}

export interface GetNewAPInvDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvDtlSearchTableset,
}
}

   /** Required : 
      @param whereClauseAPInvDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAPInvDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_APInvDtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtAPInvDtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAPInvDtlSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_APInvDtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvDtlSearchTableset,
}
}

