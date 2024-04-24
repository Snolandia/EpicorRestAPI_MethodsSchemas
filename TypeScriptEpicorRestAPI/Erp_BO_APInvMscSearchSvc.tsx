import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.APInvMscSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/$metadata", {
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
   Description: Get APInvMscSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APInvMscSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvMscRow
   */  
export function get_APInvMscSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/APInvMscSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APInvMscSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APInvMscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APInvMscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APInvMscSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/APInvMscSearches", {
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
   Summary: Calls GetByID to retrieve the APInvMscSearch item
   Description: Calls GetByID to retrieve the APInvMscSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvMscSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param MscNum Desc: MscNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvMscRow
   */  
export function get_APInvMscSearches_Company_VendorNum_InvoiceNum_InvoiceLine_MscNum(Company:string, VendorNum:string, InvoiceNum:string, InvoiceLine:string, MscNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APInvMscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/APInvMscSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + "," + MscNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_APInvMscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APInvMscSearch for the service
   Description: Calls UpdateExt to update APInvMscSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APInvMscSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param MscNum Desc: MscNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APInvMscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APInvMscSearches_Company_VendorNum_InvoiceNum_InvoiceLine_MscNum(Company:string, VendorNum:string, InvoiceNum:string, InvoiceLine:string, MscNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/APInvMscSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + "," + MscNum + ")", {
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
   Summary: Call UpdateExt to delete APInvMscSearch item
   Description: Call UpdateExt to delete APInvMscSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APInvMscSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param InvoiceNum Desc: InvoiceNum   Required: True   Allow empty value : True
      @param InvoiceLine Desc: InvoiceLine   Required: True
      @param MscNum Desc: MscNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APInvMscSearches_Company_VendorNum_InvoiceNum_InvoiceLine_MscNum(Company:string, VendorNum:string, InvoiceNum:string, InvoiceLine:string, MscNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/APInvMscSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + "," + MscNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvMscListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvMscListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvMscListRow)
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
export function get_GetRows(whereClauseAPInvMsc:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAPInvMsc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPInvMsc=" + whereClauseAPInvMsc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/GetRows" + params, {
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(vendorNum:string, invoiceNum:string, invoiceLine:string, mscNum:string, epicorHeaders?:Headers){
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
   if(typeof mscNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "mscNum=" + mscNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewAPInvMsc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPInvMsc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPInvMsc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPInvMsc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPInvMsc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/GetNewAPInvMsc", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvMscListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APInvMscListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvMscRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APInvMscRow[],
}

export interface Erp_Tablesets_APInvMscListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  Duplicated  from the related APInvHed record.  */  
   "VendorNum":number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   "InvoiceNum":string,
      /**  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the InvcDetl record for the Invoice and the adding 1 to it.  */  
   "InvoiceLine":number,
      /**  Number automatically assigned by invoice entry which is used along with VendorNum, InvoiceNum and InvoiceLine to uniquely identify the miscellaneous record within the invoice.  */  
   "MscNum":number,
      /**  Code that relates this invoice miscellaneous charge to the PurMisc master. Entered via a DDSL widget.  */  
   "MiscCode":string,
      /**  Description of the miscellaneous charge. Defaulted from PurMisc.Description.  */  
   "Description":string,
      /**  miscellaneous amount.  */  
   "MiscAmt":number,
      /**  miscellaneous amount in the vendor currency.  */  
   "DocMiscAmt":number,
      /**  Purchase order number that this miscellaneous record is related to.  */  
   "PONum":number,
      /**  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero.  */  
   "POLine":number,
      /**  Sequence number of the Miscellaneous Charge  */  
   "SeqNum":number,
      /**   Identifies Tax Category for this Misc. item.
Defaults from PurMisc.TaxCatID.  */  
   "TaxCatID":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   "GlbInvoiceNum":string,
      /**  Global Invoice Line identifier.  Used in Consolidated Purchasing.  */  
   "GlbInvoiceLine":number,
      /**  Global Invoice Miscellaneous Charge identifier.  Used in Consolidated Purchasing.  */  
   "GlbMscNum":number,
      /**  Reporting currency value of this field  */  
   "Rpt1MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MiscAmt":number,
      /**  Reference to the APInvExp record that contains the gl distribution for this charge.  */  
   "InvExpSeq":number,
      /**  Indicates if the AP Miscellaneous Charge is for Landed Cost.  */  
   "LCFlag":boolean,
      /**  The Container Shipment ID (also known as the ContainerID).  */  
   "ContainerID":number,
      /**  The Vendors purchase point ID of the associated receipt's indirect cost.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip # of the associated receipt's indirect cost.  */  
   "PackSlip":string,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  The internal key that is used to tie back to the Vendor master file.  This field, together with the PackSlip and PurPoint, is used to link the APInvMsc to the RcvMisc record that references this misc charge as a Landed Cost's Indirect Cost.  */  
   "LCVendorNum":number,
      /**  Like PurMisc.LCDisburseMethod. Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   "LCDisburseMethod":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  */  
   "CorrectionDtl":boolean,
   "DebitMemo":boolean,
   "ScrMiscAmt":number,
   "ScrDocMiscAmt":number,
   "CurrencySwitch":boolean,
   "BaseCurrSymbol":string,
   "CurrSymbol":string,
   "RecordSource":string,
   "Posted":boolean,
   "GroupID":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "Rpt1ScrMiscAmt":number,
   "Rpt2ScrMiscAmt":number,
   "Rpt3ScrMiscAmt":number,
   "LCEnabled":boolean,
   "Selected":boolean,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   "InvoiceNumDescription":string,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   "MiscCodeLCDisburseMethod":string,
      /**  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  */  
   "MiscCodeDescription":string,
      /**  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  */  
   "MiscCodeLCAmount":number,
      /**  The Landed Cost Currency Code for this miscellaneous charge.  */  
   "MiscCodeLCCurrencyCode":string,
      /**  Supplier Part Number  */  
   "POLineVenPartNum":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "POLineLineDesc":string,
      /**  OUR internal Part number for this item.  */  
   "POLinePartNum":string,
      /**  Full description for the Sales Tax category.  */  
   "TaxCatIDDescription":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
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
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APInvMscRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  Duplicated  from the related APInvHed record.  */  
   "VendorNum":number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   "InvoiceNum":string,
      /**  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the InvcDetl record for the Invoice and the adding 1 to it.  */  
   "InvoiceLine":number,
      /**  Number automatically assigned by invoice entry which is used along with VendorNum, InvoiceNum and InvoiceLine to uniquely identify the miscellaneous record within the invoice.  */  
   "MscNum":number,
      /**  Code that relates this invoice miscellaneous charge to the PurMisc master. Entered via a DDSL widget.  */  
   "MiscCode":string,
      /**  Description of the miscellaneous charge. Defaulted from PurMisc.Description.  */  
   "Description":string,
      /**  miscellaneous amount.  */  
   "MiscAmt":number,
      /**  miscellaneous amount in the vendor currency.  */  
   "DocMiscAmt":number,
      /**  Purchase order number that this miscellaneous record is related to.  */  
   "PONum":number,
      /**  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero.  */  
   "POLine":number,
      /**  Sequence number of the Miscellaneous Charge  */  
   "SeqNum":number,
      /**   Identifies Tax Category for this Misc. item.
Defaults from PurMisc.TaxCatID.  */  
   "TaxCatID":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   "GlbVendorNum":number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   "GlbInvoiceNum":string,
      /**  Global Invoice Line identifier.  Used in Consolidated Purchasing.  */  
   "GlbInvoiceLine":number,
      /**  Global Invoice Miscellaneous Charge identifier.  Used in Consolidated Purchasing.  */  
   "GlbMscNum":number,
      /**  Reporting currency value of this field  */  
   "Rpt1MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MiscAmt":number,
      /**  Reference to the APInvExp record that contains the gl distribution for this charge.  */  
   "InvExpSeq":number,
      /**  Indicates if the AP Miscellaneous Charge is for Landed Cost.  */  
   "LCFlag":boolean,
      /**  The Container Shipment ID (also known as the ContainerID).  */  
   "ContainerID":number,
      /**  The Vendors purchase point ID of the associated receipt's indirect cost.  */  
   "PurPoint":string,
      /**  Vendors Packing Slip # of the associated receipt's indirect cost.  */  
   "PackSlip":string,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  The internal key that is used to tie back to the Vendor master file.  This field, together with the PackSlip and PurPoint, is used to link the APInvMsc to the RcvMisc record that references this misc charge as a Landed Cost's Indirect Cost.  */  
   "LCVendorNum":number,
      /**  Like PurMisc.LCDisburseMethod. Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   "LCDisburseMethod":string,
      /**  miscellaneous amount including taxes.  */  
   "InMiscAmt":number,
      /**  miscellaneous amount in the vendor currency including taxes.  */  
   "DocInMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InMiscAmt":number,
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
      /**  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  */  
   "CorrectionDtl":boolean,
      /**  NoTaxRecalc  */  
   "NoTaxRecalc":boolean,
      /**  Code1099ID  */  
   "Code1099ID":string,
      /**  FormTypeID  */  
   "FormTypeID":string,
      /**  Gen1099Code  */  
   "Gen1099Code":string,
      /**  TaxExemptReasonCode  */  
   "TaxExemptReasonCode":string,
      /**  The Plastic Packaging Tax Report ID.  */  
   "PlasticPackTaxReportID":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
   "DebitMemo":boolean,
   "DocScrTotalDedTax":number,
   "DocScrTotalSATax":number,
   "DocScrTotalTax":number,
   "GroupID":string,
   "InPrice":boolean,
   "LCEnabled":boolean,
   "Posted":boolean,
   "RecordSource":string,
   "Rpt1ScrMiscAmt":number,
   "Rpt1ScrTotalDedTax":number,
   "Rpt1ScrTotalSATax":number,
   "Rpt1ScrTotalTax":number,
   "Rpt2ScrMiscAmt":number,
   "Rpt2ScrTotalDedTax":number,
   "Rpt2ScrTotalSATax":number,
   "Rpt2ScrTotalTax":number,
   "Rpt3ScrMiscAmt":number,
   "Rpt3ScrTotalDedTax":number,
   "Rpt3ScrTotalSATax":number,
   "Rpt3ScrTotalTax":number,
   "ScrDocMiscAmt":number,
   "ScrMiscAmt":number,
   "ScrTotalDedTax":number,
   "ScrTotalSATax":number,
   "ScrTotalTax":number,
   "Selected":boolean,
   "BaseCurrSymbol":string,
   "BitFlag":number,
   "InvoiceNumDescription":string,
   "MiscCodeLCCurrencyCode":string,
   "MiscCodeLCDisburseMethod":string,
   "MiscCodeDescription":string,
   "MiscCodeLCAmount":number,
   "POLineVenPartNum":string,
   "POLineLineDesc":string,
   "POLinePartNum":string,
   "TaxCatIDDescription":string,
   "VendorNumAddress3":string,
   "VendorNumState":string,
   "VendorNumZIP":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCurrencyCode":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress2":string,
   "VendorNumAddress1":string,
   "VendorNumCity":string,
   "VendorNumName":string,
   "VendorNumVendorID":string,
   "VendorNumCountry":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param vendorNum
      @param invoiceNum
      @param invoiceLine
      @param mscNum
   */  
export interface DeleteByID_input{
   vendorNum:number,
   invoiceNum:string,
   invoiceLine:number,
   mscNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_APInvMscListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  Duplicated  from the related APInvHed record.  */  
   VendorNum:number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   InvoiceNum:string,
      /**  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the InvcDetl record for the Invoice and the adding 1 to it.  */  
   InvoiceLine:number,
      /**  Number automatically assigned by invoice entry which is used along with VendorNum, InvoiceNum and InvoiceLine to uniquely identify the miscellaneous record within the invoice.  */  
   MscNum:number,
      /**  Code that relates this invoice miscellaneous charge to the PurMisc master. Entered via a DDSL widget.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. Defaulted from PurMisc.Description.  */  
   Description:string,
      /**  miscellaneous amount.  */  
   MiscAmt:number,
      /**  miscellaneous amount in the vendor currency.  */  
   DocMiscAmt:number,
      /**  Purchase order number that this miscellaneous record is related to.  */  
   PONum:number,
      /**  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero.  */  
   POLine:number,
      /**  Sequence number of the Miscellaneous Charge  */  
   SeqNum:number,
      /**   Identifies Tax Category for this Misc. item.
Defaults from PurMisc.TaxCatID.  */  
   TaxCatID:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceNum:string,
      /**  Global Invoice Line identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceLine:number,
      /**  Global Invoice Miscellaneous Charge identifier.  Used in Consolidated Purchasing.  */  
   GlbMscNum:number,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  Reference to the APInvExp record that contains the gl distribution for this charge.  */  
   InvExpSeq:number,
      /**  Indicates if the AP Miscellaneous Charge is for Landed Cost.  */  
   LCFlag:boolean,
      /**  The Container Shipment ID (also known as the ContainerID).  */  
   ContainerID:number,
      /**  The Vendors purchase point ID of the associated receipt's indirect cost.  */  
   PurPoint:string,
      /**  Vendors Packing Slip # of the associated receipt's indirect cost.  */  
   PackSlip:string,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  The internal key that is used to tie back to the Vendor master file.  This field, together with the PackSlip and PurPoint, is used to link the APInvMsc to the RcvMisc record that references this misc charge as a Landed Cost's Indirect Cost.  */  
   LCVendorNum:number,
      /**  Like PurMisc.LCDisburseMethod. Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   LCDisburseMethod:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  */  
   CorrectionDtl:boolean,
   DebitMemo:boolean,
   ScrMiscAmt:number,
   ScrDocMiscAmt:number,
   CurrencySwitch:boolean,
   BaseCurrSymbol:string,
   CurrSymbol:string,
   RecordSource:string,
   Posted:boolean,
   GroupID:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   Rpt1ScrMiscAmt:number,
   Rpt2ScrMiscAmt:number,
   Rpt3ScrMiscAmt:number,
   LCEnabled:boolean,
   Selected:boolean,
      /**  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  */  
   InvoiceNumDescription:string,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   MiscCodeLCDisburseMethod:string,
      /**  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  */  
   MiscCodeDescription:string,
      /**  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  */  
   MiscCodeLCAmount:number,
      /**  The Landed Cost Currency Code for this miscellaneous charge.  */  
   MiscCodeLCCurrencyCode:string,
      /**  Supplier Part Number  */  
   POLineVenPartNum:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   POLineLineDesc:string,
      /**  OUR internal Part number for this item.  */  
   POLinePartNum:string,
      /**  Full description for the Sales Tax category.  */  
   TaxCatIDDescription:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
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
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvMscListTableset{
   APInvMscList:Erp_Tablesets_APInvMscListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APInvMscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Internal VendorNum that ties back to the Vendor master file.  Duplicated  from the related APInvHed record.  */  
   VendorNum:number,
      /**  Invoice Number from corresponding APInvHed record.  */  
   InvoiceNum:string,
      /**  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the InvcDetl record for the Invoice and the adding 1 to it.  */  
   InvoiceLine:number,
      /**  Number automatically assigned by invoice entry which is used along with VendorNum, InvoiceNum and InvoiceLine to uniquely identify the miscellaneous record within the invoice.  */  
   MscNum:number,
      /**  Code that relates this invoice miscellaneous charge to the PurMisc master. Entered via a DDSL widget.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. Defaulted from PurMisc.Description.  */  
   Description:string,
      /**  miscellaneous amount.  */  
   MiscAmt:number,
      /**  miscellaneous amount in the vendor currency.  */  
   DocMiscAmt:number,
      /**  Purchase order number that this miscellaneous record is related to.  */  
   PONum:number,
      /**  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero.  */  
   POLine:number,
      /**  Sequence number of the Miscellaneous Charge  */  
   SeqNum:number,
      /**   Identifies Tax Category for this Misc. item.
Defaults from PurMisc.TaxCatID.  */  
   TaxCatID:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Vendor identifier.  Used in Consolidated Purchasing.  */  
   GlbVendorNum:number,
      /**  Global Invoice identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceNum:string,
      /**  Global Invoice Line identifier.  Used in Consolidated Purchasing.  */  
   GlbInvoiceLine:number,
      /**  Global Invoice Miscellaneous Charge identifier.  Used in Consolidated Purchasing.  */  
   GlbMscNum:number,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  Reference to the APInvExp record that contains the gl distribution for this charge.  */  
   InvExpSeq:number,
      /**  Indicates if the AP Miscellaneous Charge is for Landed Cost.  */  
   LCFlag:boolean,
      /**  The Container Shipment ID (also known as the ContainerID).  */  
   ContainerID:number,
      /**  The Vendors purchase point ID of the associated receipt's indirect cost.  */  
   PurPoint:string,
      /**  Vendors Packing Slip # of the associated receipt's indirect cost.  */  
   PackSlip:string,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  The internal key that is used to tie back to the Vendor master file.  This field, together with the PackSlip and PurPoint, is used to link the APInvMsc to the RcvMisc record that references this misc charge as a Landed Cost's Indirect Cost.  */  
   LCVendorNum:number,
      /**  Like PurMisc.LCDisburseMethod. Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  */  
   LCDisburseMethod:string,
      /**  miscellaneous amount including taxes.  */  
   InMiscAmt:number,
      /**  miscellaneous amount in the vendor currency including taxes.  */  
   DocInMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InMiscAmt:number,
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
      /**  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  */  
   CorrectionDtl:boolean,
      /**  NoTaxRecalc  */  
   NoTaxRecalc:boolean,
      /**  Code1099ID  */  
   Code1099ID:string,
      /**  FormTypeID  */  
   FormTypeID:string,
      /**  Gen1099Code  */  
   Gen1099Code:string,
      /**  TaxExemptReasonCode  */  
   TaxExemptReasonCode:string,
      /**  The Plastic Packaging Tax Report ID.  */  
   PlasticPackTaxReportID:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DebitMemo:boolean,
   DocScrTotalDedTax:number,
   DocScrTotalSATax:number,
   DocScrTotalTax:number,
   GroupID:string,
   InPrice:boolean,
   LCEnabled:boolean,
   Posted:boolean,
   RecordSource:string,
   Rpt1ScrMiscAmt:number,
   Rpt1ScrTotalDedTax:number,
   Rpt1ScrTotalSATax:number,
   Rpt1ScrTotalTax:number,
   Rpt2ScrMiscAmt:number,
   Rpt2ScrTotalDedTax:number,
   Rpt2ScrTotalSATax:number,
   Rpt2ScrTotalTax:number,
   Rpt3ScrMiscAmt:number,
   Rpt3ScrTotalDedTax:number,
   Rpt3ScrTotalSATax:number,
   Rpt3ScrTotalTax:number,
   ScrDocMiscAmt:number,
   ScrMiscAmt:number,
   ScrTotalDedTax:number,
   ScrTotalSATax:number,
   ScrTotalTax:number,
   Selected:boolean,
   BaseCurrSymbol:string,
   BitFlag:number,
   InvoiceNumDescription:string,
   MiscCodeLCCurrencyCode:string,
   MiscCodeLCDisburseMethod:string,
   MiscCodeDescription:string,
   MiscCodeLCAmount:number,
   POLineVenPartNum:string,
   POLineLineDesc:string,
   POLinePartNum:string,
   TaxCatIDDescription:string,
   VendorNumAddress3:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumTermsCode:string,
   VendorNumAddress2:string,
   VendorNumAddress1:string,
   VendorNumCity:string,
   VendorNumName:string,
   VendorNumVendorID:string,
   VendorNumCountry:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APInvMscSearchTableset{
   APInvMsc:Erp_Tablesets_APInvMscRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtAPInvMscSearchTableset{
   APInvMsc:Erp_Tablesets_APInvMscRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param vendorNum
      @param invoiceNum
      @param invoiceLine
      @param mscNum
   */  
export interface GetByID_input{
   vendorNum:number,
   invoiceNum:string,
   invoiceLine:number,
   mscNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_APInvMscSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_APInvMscSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_APInvMscSearchTableset[],
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
   returnObj:Erp_Tablesets_APInvMscListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param vendorNum
      @param invoiceNum
      @param invoiceLine
   */  
export interface GetNewAPInvMsc_input{
   ds:Erp_Tablesets_APInvMscSearchTableset[],
   vendorNum:number,
   invoiceNum:string,
   invoiceLine:number,
}

export interface GetNewAPInvMsc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvMscSearchTableset[],
}
}

   /** Required : 
      @param whereClauseAPInvMsc
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAPInvMsc:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_APInvMscSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtAPInvMscSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAPInvMscSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_APInvMscSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APInvMscSearchTableset[],
}
}

