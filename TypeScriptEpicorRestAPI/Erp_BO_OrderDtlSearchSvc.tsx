import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.OrderDtlSearchSvc
// Description: Job dataset for Customer Tracker UI.
           This object does not have update capabilities.
           Only record retrieval is available.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/$metadata", {
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
   Description: Get OrderDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OrderDtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderDtlRow
   */  
export function get_OrderDtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/OrderDtlSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OrderDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OrderDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OrderDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OrderDtlSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/OrderDtlSearches", {
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
   Summary: Calls GetByID to retrieve the OrderDtlSearch item
   Description: Calls GetByID to retrieve the OrderDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OrderDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OrderDtlRow
   */  
export function get_OrderDtlSearches_Company_OrderNum_OrderLine(Company:string, OrderNum:string, OrderLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OrderDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/OrderDtlSearches(" + Company + "," + OrderNum + "," + OrderLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_OrderDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OrderDtlSearch for the service
   Description: Calls UpdateExt to update OrderDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OrderDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OrderDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OrderDtlSearches_Company_OrderNum_OrderLine(Company:string, OrderNum:string, OrderLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/OrderDtlSearches(" + Company + "," + OrderNum + "," + OrderLine + ")", {
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
   Summary: Call UpdateExt to delete OrderDtlSearch item
   Description: Call UpdateExt to delete OrderDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OrderDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OrderDtlSearches_Company_OrderNum_OrderLine(Company:string, OrderNum:string, OrderLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/OrderDtlSearches(" + Company + "," + OrderNum + "," + OrderLine + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlListRow)
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
export function get_GetRows(whereClauseOrderDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseOrderDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOrderDtl=" + whereClauseOrderDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/GetRows" + params, {
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
export function get_GetByID(orderNum:string, orderLine:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof orderNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderNum=" + orderNum
   }
   if(typeof orderLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderLine=" + orderLine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/GetList" + params, {
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
   Summary: Invoke method getBreakListCodeDesc
   Description: getBreakListCodeDesc
   OperationID: getBreakListCodeDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getBreakListCodeDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getBreakListCodeDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getBreakListCodeDesc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/getBreakListCodeDesc", {
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
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer tracker.
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsContactTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/GetRowsContactTracker", {
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
   Summary: Invoke method GetRowsCustomerActivity
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer activity.
   OperationID: GetRowsCustomerActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerActivity(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/GetRowsCustomerActivity", {
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
   Summary: Invoke method GetRowsCustomerTrackerAndSort
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer tracker.
   OperationID: GetRowsCustomerTrackerAndSort
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTrackerAndSort_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTrackerAndSort_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTrackerAndSort(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/GetRowsCustomerTrackerAndSort", {
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
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer tracker.
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustomerTracker(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/GetRowsCustomerTracker", {
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
   Summary: Invoke method GetNewOrderDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOrderDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOrderDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOrderDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOrderDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/GetNewOrderDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderDtlSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OrderDtlListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OrderDtlRow[],
}

export interface Erp_Tablesets_OrderDtlListRow{
      /**   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   "VoidLine":boolean,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   "OpenLine":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   "OrderNum":number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "OrderLine":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   "PartNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  EDI Reference  */  
   "Reference":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   "IUM":string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLine":string,
      /**  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  */  
   "Commissionable":boolean,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "UnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "DocUnitPrice":number,
      /**  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  */  
   "OrderQty":number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Discount":number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "DocDiscount":number,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   "RequestDate":string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  */  
   "OrderComment":string,
      /**  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  */  
   "ShipComment":string,
      /**  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  */  
   "InvoiceComment":string,
      /**  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  */  
   "PickListComment":string,
      /**  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  */  
   "TaxCatID":string,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  */  
   "AdvanceBillBal":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "DocAdvanceBillBal":number,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  */  
   "QuoteNum":number,
      /**  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   "QuoteLine":number,
      /**  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  */  
   "TMBilling":boolean,
      /**  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  */  
   "OrigWhyNoTax":string,
      /**   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  */  
   "NeedByDate":string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  */  
   "CustNum":number,
      /**   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  */  
   "Rework":boolean,
      /**   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  */  
   "RMANum":number,
      /**  The line item of the RMA detail that this order line item is fulfilling.  */  
   "RMALine":number,
      /**  Project ID of the Project table record that this OrderDtl record. Can be blank.  */  
   "ProjectID":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  Indicate that the item or the product group has a warranty.  */  
   "Warranty":boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  The # of days, months, years the material is covered by warranty  */  
   "MaterialDuration":number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   "LaborDuration":number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   "MiscDuration":number,
      /**  Whether the duration of warranty  is for "Days"," Months", "Years".  */  
   "MaterialMod":string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   "LaborMod":string,
      /**  Editor widget for Warranty comments.  */  
   "WarrantyComment":string,
      /**  This warranty covers On site visits  */  
   "Onsite":boolean,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  */  
   "SellingQuantity":number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   "SalesCatID":string,
      /**  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  */  
   "ShipLineComplete":boolean,
      /**  Quantity from last EDI update.  */  
   "CumeQty":number,
      /**  Date of last update  */  
   "CumeDate":string,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   "MktgCampaignID":string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   "MktgEvntSeq":number,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   "LockQty":boolean,
      /**  Indicates if this order line is linked to an inter-company PO line.  */  
   "Linked":boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   "ICPONum":number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ICPOLine":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
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
      /**  This is the Price List used to determine the starting base price.  */  
   "PriceListCode":string,
      /**  This is the Price List used to determine the break % or amount.  */  
   "BreakListCode":string,
      /**  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  */  
   "PricingQty":number,
      /**  Indicates if the price of the order line can be changed.  */  
   "LockPrice":boolean,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   "ListPrice":number,
      /**   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   "OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  */  
   "DocOrdBasedPrice":number,
      /**  This is the Price Group ID used to price the order line with.  */  
   "PriceGroupCode":string,
      /**  Indicates if the user selected a price list different from the default.  */  
   "OverridePriceList":boolean,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  */  
   "PricingValue":number,
      /**  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  */  
   "DisplaySeq":number,
      /**  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  */  
   "KitParentLine":number,
      /**  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitAllowUpdate":boolean,
      /**  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  */  
   "KitShipComplete":boolean,
      /**  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitBackFlush":boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitPrintCompsPS":boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitPrintCompsInv":boolean,
      /**  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  */  
   "KitPricing":string,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  */  
   "KitQtyPer":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate1":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate2":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate3":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate4":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate5":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit1":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit2":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit3":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit4":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit5":number,
      /**  The Demand Contract Detail record this OrderDtl is related to.  */  
   "DemandContractLine":number,
      /**  Create New Job flag  */  
   "CreateNewJob":boolean,
      /**  The date before which the order cannot be shipped.  */  
   "DoNotShipBeforeDate":string,
      /**  Get Details flag  */  
   "GetDtls":boolean,
      /**  The date after which the order cannot be shipped.  */  
   "DoNotShipAfterDate":string,
      /**  Schedule Job flag  */  
   "SchedJob":boolean,
      /**  Release Job flag  */  
   "RelJob":boolean,
      /**  Enable New Job flag  */  
   "EnableCreateNewJob":boolean,
      /**  Enable Get Details flag  */  
   "EnableGetDtls":boolean,
      /**  Enable Schedule Job flag  */  
   "EnableSchedJob":boolean,
      /**  Enable Release Job flag  */  
   "EnableRelJob":boolean,
      /**  Indicates the warehouse selected for a counter sale order line.  */  
   "CounterSaleWarehouse":string,
      /**  Identifies the Bin selected for a counter sale order line.  */  
   "CounterSaleBinNum":string,
      /**  Indicates the lot number selected for a counter sale order line.  */  
   "CounterSaleLotNum":string,
      /**  Indicates the dimension code selected for a counter sales order line.  */  
   "CounterSaleDimCode":string,
      /**  Indicates if the demand detail that created/updated this order line has been rejected.  */  
   "DemandDtlRejected":boolean,
      /**   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   "KitFlag":string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  */  
   "KitsLoaded":boolean,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   "DemandHeadSeq":number,
      /**  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  */  
   "DemandDtlSeq":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Total Number of releases for the line  */  
   "TotalReleases":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt1UnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt2UnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt3UnitPrice":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt1Discount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt2Discount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt3Discount":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "Rpt1AdvanceBillBal":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "Rpt2AdvanceBillBal":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "Rpt3AdvanceBillBal":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1ListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2ListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3ListPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3OrdBasedPrice":number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule  */  
   "ExtPriceDtl":number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   "DocExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPriceDtl":number,
      /**  Status of Order Line  */  
   "LineStatus":string,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  */  
   "InUnitPrice":number,
      /**  Same as DocUnit price except that this field contains the unit price including taxes  */  
   "DocInUnitPrice":number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  */  
   "InDiscount":number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  */  
   "DocInDiscount":number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  */  
   "InListPrice":number,
      /**   Same as List price except that this field contains the list price in
the customer currency -including taxes.  */  
   "DocInListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied. including taxes  */  
   "InOrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  */  
   "DocInOrdBasedPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt1InUnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt2InUnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt3InUnitPrice":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt1InDiscount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt2InDiscount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt3InDiscount":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1InListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2InListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3InListPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1InOrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2InOrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3InOrdBasedPrice":number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  */  
   "InExtPriceDtl":number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  */  
   "DocInExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InExtPriceDtl":number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   "OldOurOpenQty":number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   "OldSellingOpenQty":number,
      /**  Used to store open value setting assigned in product configuration programs  */  
   "OldOpenValue":number,
      /**  Used to store prod code value assigned in product configuration programs  */  
   "OldProdCode":string,
      /**  Previous Selling Quantity  */  
   "PrevSellQty":number,
      /**  Previous Part Number  */  
   "PrevPartNum":string,
      /**  Previous Customer Part Number  */  
   "PrevXPartNum":string,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   "KitCompOrigSeq":number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   "KitCompOrigPart":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
   "DiscBreakListCode":string,
   "DiscListPrice":number,
   "LockDisc":boolean,
   "OverrideDiscPriceList":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrSymbol":string,
   "BaseCurrSymbol":string,
   "CurrencySwitch":boolean,
   "OnHandQuantity":number,
   "AvailableQuantity":number,
   "TotalShipped":number,
   "ExtPrice":number,
   "MiscCharges":number,
   "TotalPrice":number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   "DocExtPrice":number,
   "DocMiscCharges":number,
   "DocTotalPrice":number,
   "Configured":string,
   "QuoteQtyNum":number,
   "WarehouseCode":string,
   "BinNum":string,
   "LotNum":string,
   "DimCode":string,
   "DimConvFactor":number,
   "DUM":string,
   "ProcessQuickEntry":boolean,
   "CounterSale":boolean,
      /**  Available Price Lists  */  
   "AvailPriceLists":string,
   "ProcessCounterSale":boolean,
   "PartTrackLots":boolean,
   "PartTrackDimension":boolean,
   "DemandQuantity":number,
   "AvailUMFromQuote":string,
   "FromQuoteLineFlag":boolean,
   "MultipleReleases":boolean,
   "PartExists":boolean,
   "SalesRepName1":string,
   "SalesRepName2":string,
   "SalesRepName3":string,
   "SalesRepName4":string,
   "SalesRepName5":string,
   "WarehouseDesc":string,
      /**  The message text returned by the credit check process.  */  
   "CreditLimitMessage":string,
      /**  The source that put the customer on credit hold.  */  
   "CreditLimitSource":string,
      /**  Kit Flag Description. "P" = Parent, "C" = Component.  */  
   "KitFlagDescription":string,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   "KitDisable":boolean,
      /**  If KitFlag = "C" and the parent kit line is configured OR if KitFlag = "P" and Configured = "On" then this field will be TRUE, otherwise it will be false.  */  
   "KitStandard":boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   "KitChangeParms":boolean,
   "PriceListCodeDesc":string,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   "EnableSellingQty":boolean,
      /**  Total tax in base currency. The sum of all the tax details for the line.  */  
   "TaxAmt":number,
      /**  Total tax in Doc currency. The sum of all the tax details for the line (OrderRelTax).  */  
   "DocTaxAmt":number,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   "EnableKitUnitPrice":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "KitOrderQtyUOM":string,
      /**  Report currency misc charges  */  
   "Rpt1MiscCharges":number,
      /**  Report currency misc charges  */  
   "Rpt2MiscCharges":number,
      /**  Report Currency misc charges  */  
   "Rpt3MiscCharges":number,
      /**  Report currency line tax amount  */  
   "Rpt1TaxAmt":number,
      /**  Report currency line tax amount  */  
   "Rpt2TaxAmt":number,
      /**  Report currency line tax amount  */  
   "Rpt3TaxAmt":number,
      /**  Report currency line total price  */  
   "Rpt1TotalPrice":number,
      /**  Report currency line total price  */  
   "Rpt2TotalPrice":number,
      /**  Report currency line total price  */  
   "Rpt3TotalPrice":number,
      /**  The Sales Order Quantity expressed in the Inventory Unit of Measure  */  
   "ThisOrderInvtyQty":number,
      /**  Inventory UOM that the Order Detail is allocated against.  */  
   "InvtyUOM":string,
      /**  Indicates whether the part has at least one Complement  */  
   "HasComplement":boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   "HasUpgrade":boolean,
      /**  Indicates whether the part has at least one Downgrade  */  
   "HasDowngrade":boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   "HasSubstitute":boolean,
      /**  Extended Price for the Order Line in Rpt1 currency  */  
   "Rpt1ExtPrice":number,
      /**  Extended Price for the orderLine in Rpt2 currency.  */  
   "Rpt2ExtPrice":number,
      /**  Extended price for the order line in Rpt3 currency  */  
   "Rpt3ExtPrice":number,
   "BaseCurrencyID":string,
   "CurrencyID":string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLineRef":string,
      /**  Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DspDiscount":number,
      /**  Document currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DocDspDiscount":number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt1DspDiscount":number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt2DspDiscount":number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt3DspDiscount":number,
      /**  Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DspUnitPrice":number,
      /**  Document currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DocDspUnitPrice":number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt1DspUnitPrice":number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt2DspUnitPrice":number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt3DspUnitPrice":number,
      /**  The flag to indicate if the Order Header Tax Liability is Tax Inclusive Pricing.  */  
   "InPrice":boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   "EntryProcess":string,
      /**  The amount of discount for display in document currency which does not include taxes  */  
   "DocLessDiscount":number,
      /**  The amount of discount for display which does not include taxes  */  
   "LessDiscount":number,
      /**  The amount of discount for display which does not include taxes (report currency)  */  
   "Rpt1LessDiscount":number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   "Rpt2LessDiscount":number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   "Rpt3LessDiscount":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in document currency  */  
   "DocInMiscCharges":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line  */  
   "InMiscCharges":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   "Rpt1InMiscCharges":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   "Rpt2InMiscCharges":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   "Rpt3InMiscCharges":number,
      /**  Description of the service contract.  */  
   "ContractCodeContractDescription":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  Description of the Marketing campaign  */  
   "MktgCampaignIDCampDescription":string,
      /**  Description.  */  
   "MktgEvntEvntDescription":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
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
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Full description of Product Group.  */  
   "ProdCodeDescription":string,
      /**  Full description of Project Management Code.  */  
   "ProjectIDDescription":string,
      /**  A unique code that identifies the currency.  */  
   "QuoteNumCurrencyCode":string,
      /**  Description of the sales category.  */  
   "SalesCatIDDescription":string,
      /**  Full description for the Sales Tax category.  */  
   "TaxCatIDDescription":string,
      /**  Description of the warranty.  */  
   "WarrantyCodeWarrDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_OrderDtlRow{
      /**   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   "VoidLine":boolean,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   "OpenLine":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   "OrderNum":number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   "OrderLine":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   "PartNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  EDI Reference  */  
   "Reference":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   "IUM":string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLine":string,
      /**  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  */  
   "Commissionable":boolean,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   "DiscountPercent":number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "UnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "DocUnitPrice":number,
      /**  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  */  
   "OrderQty":number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Discount":number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "DocDiscount":number,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   "RequestDate":string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  */  
   "OrderComment":string,
      /**  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  */  
   "ShipComment":string,
      /**  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  */  
   "InvoiceComment":string,
      /**  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  */  
   "PickListComment":string,
      /**  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  */  
   "TaxCatID":string,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  */  
   "AdvanceBillBal":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "DocAdvanceBillBal":number,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  */  
   "QuoteNum":number,
      /**  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   "QuoteLine":number,
      /**  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  */  
   "TMBilling":boolean,
      /**  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  */  
   "OrigWhyNoTax":string,
      /**   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  */  
   "NeedByDate":string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  */  
   "CustNum":number,
      /**   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  */  
   "Rework":boolean,
      /**   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  */  
   "RMANum":number,
      /**  The line item of the RMA detail that this order line item is fulfilling.  */  
   "RMALine":number,
      /**  Project ID of the Project table record that this OrderDtl record. Can be blank.  */  
   "ProjectID":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  Indicate that the item or the product group has a warranty.  */  
   "Warranty":boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  The # of days, months, years the material is covered by warranty  */  
   "MaterialDuration":number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   "LaborDuration":number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   "MiscDuration":number,
      /**  Whether the duration of warranty  is for "Days"," Months", "Years".  */  
   "MaterialMod":string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   "LaborMod":string,
      /**  Editor widget for Warranty comments.  */  
   "WarrantyComment":string,
      /**  This warranty covers On site visits  */  
   "Onsite":boolean,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  */  
   "SellingQuantity":number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   "SalesCatID":string,
      /**  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  */  
   "ShipLineComplete":boolean,
      /**  Quantity from last EDI update.  */  
   "CumeQty":number,
      /**  Date of last update  */  
   "CumeDate":string,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   "MktgCampaignID":string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   "MktgEvntSeq":number,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   "LockQty":boolean,
      /**  Indicates if this order line is linked to an inter-company PO line.  */  
   "Linked":boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   "ICPONum":number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ICPOLine":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
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
      /**  This is the Price List used to determine the starting base price.  */  
   "PriceListCode":string,
      /**  This is the Price List used to determine the break % or amount.  */  
   "BreakListCode":string,
      /**  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  */  
   "PricingQty":number,
      /**  Indicates if the price of the order line can be changed.  */  
   "LockPrice":boolean,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   "ListPrice":number,
      /**   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  */  
   "DocListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   "OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  */  
   "DocOrdBasedPrice":number,
      /**  This is the Price Group ID used to price the order line with.  */  
   "PriceGroupCode":string,
      /**  Indicates if the user selected a price list different from the default.  */  
   "OverridePriceList":boolean,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  */  
   "PricingValue":number,
      /**  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  */  
   "DisplaySeq":number,
      /**  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  */  
   "KitParentLine":number,
      /**  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitAllowUpdate":boolean,
      /**  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  */  
   "KitShipComplete":boolean,
      /**  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitBackFlush":boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitPrintCompsPS":boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   "KitPrintCompsInv":boolean,
      /**  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  */  
   "KitPricing":string,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  */  
   "KitQtyPer":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate1":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate2":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate3":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate4":number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   "RepRate5":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit1":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit2":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit3":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit4":number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   "RepSplit5":number,
      /**  The Demand Contract Detail record this OrderDtl is related to.  */  
   "DemandContractLine":number,
      /**  Create New Job flag  */  
   "CreateNewJob":boolean,
      /**  The date before which the order cannot be shipped.  */  
   "DoNotShipBeforeDate":string,
      /**  Get Details flag  */  
   "GetDtls":boolean,
      /**  The date after which the order cannot be shipped.  */  
   "DoNotShipAfterDate":string,
      /**  Schedule Job flag  */  
   "SchedJob":boolean,
      /**  Release Job flag  */  
   "RelJob":boolean,
      /**  Enable New Job flag  */  
   "EnableCreateNewJob":boolean,
      /**  Enable Get Details flag  */  
   "EnableGetDtls":boolean,
      /**  Enable Schedule Job flag  */  
   "EnableSchedJob":boolean,
      /**  Enable Release Job flag  */  
   "EnableRelJob":boolean,
      /**  Indicates the warehouse selected for a counter sale order line.  */  
   "CounterSaleWarehouse":string,
      /**  Identifies the Bin selected for a counter sale order line.  */  
   "CounterSaleBinNum":string,
      /**  Indicates the lot number selected for a counter sale order line.  */  
   "CounterSaleLotNum":string,
      /**  Indicates the dimension code selected for a counter sales order line.  */  
   "CounterSaleDimCode":string,
      /**  Indicates if the demand detail that created/updated this order line has been rejected.  */  
   "DemandDtlRejected":boolean,
      /**   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   "KitFlag":string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  */  
   "KitsLoaded":boolean,
      /**  The demand contract this demand is for.  */  
   "DemandContractNum":number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   "DemandHeadSeq":number,
      /**  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  */  
   "DemandDtlSeq":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Total Number of releases for the line  */  
   "TotalReleases":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt1UnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt2UnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt3UnitPrice":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt1Discount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt2Discount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt3Discount":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "Rpt1AdvanceBillBal":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "Rpt2AdvanceBillBal":number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   "Rpt3AdvanceBillBal":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1ListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2ListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3ListPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2OrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3OrdBasedPrice":number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule  */  
   "ExtPriceDtl":number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   "DocExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPriceDtl":number,
      /**  Status of Order Line  */  
   "LineStatus":string,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  */  
   "InUnitPrice":number,
      /**  Same as DocUnit price except that this field contains the unit price including taxes  */  
   "DocInUnitPrice":number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  */  
   "InDiscount":number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  */  
   "DocInDiscount":number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  */  
   "InListPrice":number,
      /**   Same as List price except that this field contains the list price in
the customer currency -including taxes.  */  
   "DocInListPrice":number,
      /**  This is the unit price after quantity based or order value based discounts are applied. including taxes  */  
   "InOrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  */  
   "DocInOrdBasedPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt1InUnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt2InUnitPrice":number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   "Rpt3InUnitPrice":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt1InDiscount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt2InDiscount":number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   "Rpt3InDiscount":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1InListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2InListPrice":number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3InListPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt1InOrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt2InOrdBasedPrice":number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   "Rpt3InOrdBasedPrice":number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  */  
   "InExtPriceDtl":number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  */  
   "DocInExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InExtPriceDtl":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InExtPriceDtl":number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   "OldOurOpenQty":number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   "OldSellingOpenQty":number,
      /**  Used to store open value setting assigned in product configuration programs  */  
   "OldOpenValue":number,
      /**  Used to store prod code value assigned in product configuration programs  */  
   "OldProdCode":string,
      /**  Previous Selling Quantity  */  
   "PrevSellQty":number,
      /**  Previous Part Number  */  
   "PrevPartNum":string,
      /**  Previous Customer Part Number  */  
   "PrevXPartNum":string,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   "KitCompOrigSeq":number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   "KitCompOrigPart":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
   "DiscBreakListCode":string,
   "DiscListPrice":number,
   "LockDisc":boolean,
   "OverrideDiscPriceList":boolean,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  ECCOrderNum  */  
   "ECCOrderNum":string,
      /**  ECCOrderLine  */  
   "ECCOrderLine":number,
      /**  DupOnJobCrt  */  
   "DupOnJobCrt":boolean,
      /**  UndersPct  */  
   "UndersPct":number,
      /**  Overs  */  
   "Overs":number,
      /**  Unders  */  
   "Unders":number,
      /**  OversUnitPrice  */  
   "OversUnitPrice":number,
      /**  PlanUserID  */  
   "PlanUserID":string,
      /**  PlanGUID  */  
   "PlanGUID":string,
      /**  MOMsourceType  */  
   "MOMsourceType":string,
      /**  MOMsourceEst  */  
   "MOMsourceEst":string,
      /**  DefaultOversPricing  */  
   "DefaultOversPricing":string,
      /**  ECCPlant  */  
   "ECCPlant":string,
      /**  ECCQuoteNum  */  
   "ECCQuoteNum":string,
      /**  ECCQuoteLine  */  
   "ECCQuoteLine":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MfgJobType  */  
   "MfgJobType":string,
      /**  ProFormaInvComment  */  
   "ProFormaInvComment":string,
      /**  CreateJob  */  
   "CreateJob":boolean,
      /**  The identifier of the planning contract.  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   "LinkToContract":boolean,
      /**  DocInAdvanceBillBal  */  
   "DocInAdvanceBillBal":number,
      /**  InAdvanceBillBal  */  
   "InAdvanceBillBal":number,
      /**  Rpt1InAdvanceBillBal  */  
   "Rpt1InAdvanceBillBal":number,
      /**  Rpt2InAdvanceBillBal  */  
   "Rpt2InAdvanceBillBal":number,
      /**  Rpt3InAdvanceBillBal  */  
   "Rpt3InAdvanceBillBal":number,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  CommodityCode  */  
   "CommodityCode":string,
      /**  Base price before any price breaks and discounts  */  
   "MSRP":number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   "DocMSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   "Rpt1MSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   "Rpt2MSRP":number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   "Rpt3MSRP":number,
      /**  Distributor end customer price.  */  
   "EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   "DocEndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   "Rpt1EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   "Rpt2EndCustomerPrice":number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   "Rpt3EndCustomerPrice":number,
      /**  Promotional Price offered to Dealer and Distributors.  */  
   "PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   "DocPromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   "Rpt1PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   "Rpt2PromotionalPrice":number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   "Rpt3PromotionalPrice":number,
      /**  Current status of line.  This is a maintainable status through Order Line Status maintenance.  Depending on the setting can control is line is updatable from the web.  */  
   "OrderLineStatusCode":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  */  
   "AttributeSetID":number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   "KBConfigProdID":number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   "KBOriginalConfigProdID":number,
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
   "AvailableQuantity":number,
      /**  Available Price Lists  */  
   "AvailPriceLists":string,
   "AvailUMFromQuote":string,
   "BaseCurrencyID":string,
   "BaseCurrSymbol":string,
      /**  Default calculated unit price for a particular part/customer.  Used with integrations for pre-order price validations.  */  
   "CalcUnitPrice":number,
   "ConfigType":string,
   "Configured":string,
   "CounterSale":boolean,
      /**  The message text returned by the credit check process.  */  
   "CreditLimitMessage":string,
      /**  The source that put the customer on credit hold.  */  
   "CreditLimitSource":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencyID":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
   "DemandQuantity":number,
   "DimCode":string,
   "DimConvFactor":number,
      /**  Document currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DocDspDiscount":number,
      /**  Document currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DocDspUnitPrice":number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   "DocExtPrice":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in document currency  */  
   "DocInMiscCharges":number,
      /**  The amount of discount for display in document currency which does not include taxes  */  
   "DocLessDiscount":number,
   "DocMiscCharges":number,
      /**  Total tax in Doc currency. The sum of all the tax details for the line (OrderRelTax).  */  
   "DocTaxAmt":number,
   "DocTotalPrice":number,
      /**  Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DspDiscount":number,
      /**  To display the type of job this is: MFG = Manufacturing, PRJ = Project  */  
   "DspJobType":string,
      /**  Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "DspUnitPrice":number,
   "DUM":string,
      /**  Web basket configuration related SysRowID  */  
   "ECCConfigSysRowId":string,
      /**  Additional discount calculated by ECC  */  
   "ECCDiscount":number,
      /**  Prevents Epicor repricing the unit price coming from ECC.  This usually would be a result of Epicor going off-line and order pricing was performed by ECC.  */  
   "ECCPreventRepricing":boolean,
      /**  Allow enable/disable for the button Attibutes in Order Line  */  
   "EnableDynAttrButton":boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   "EnableKitUnitPrice":boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   "EnableRenewalNbr":boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   "EnableSellingQty":boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   "EntryProcess":string,
   "ExtPrice":number,
   "FromQuoteLineFlag":boolean,
      /**  Installation price of an equipment that requires installation in Epicor FSA. This value by default is inherited from the part but it could be overridden for another value if it's necessary.  */  
   "FSAInstallationCost":number,
   "FSAInstallationOrderLine":number,
   "FSAInstallationOrderNum":number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   "FSAInstallationRequired":boolean,
      /**  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  */  
   "FSAInstallationType":string,
   "FSAInstallationTypeDescription":string,
      /**  Indicates whether the part has at least one Complement  */  
   "HasComplement":boolean,
      /**  Indicates whether the part has at least one Downgrade  */  
   "HasDowngrade":boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   "HasSubstitute":boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   "HasUpgrade":boolean,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line  */  
   "InMiscCharges":number,
      /**  The flag to indicate if the Order Header Tax Liability is Tax Inclusive Pricing.  */  
   "InPrice":boolean,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
      /**  Inventory UOM that the Order Detail is allocated against.  */  
   "InvtyUOM":string,
   "JobTypeDesc":string,
      /**  If the Job has been already created against this line.  */  
   "JobWasCreated":boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   "KitChangeParms":boolean,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   "KitDisable":boolean,
      /**  Kit Flag Description. "P" = Parent, "C" = Component.  */  
   "KitFlagDescription":string,
   "KitOrderQtyUOM":string,
      /**  If KitFlag = "C" and the parent kit line is configured OR if KitFlag = "P" and Configured = "On" then this field will be TRUE, otherwise it will be false.  */  
   "KitStandard":boolean,
      /**  The amount of discount for display which does not include taxes  */  
   "LessDiscount":number,
   "LotNum":string,
   "MiscCharges":number,
   "MultipleReleases":boolean,
   "OnHandQuantity":number,
   "PartExists":boolean,
   "PartTrackDimension":boolean,
   "PartTrackLots":boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   "POLineRef":string,
   "PriceListCodeDesc":string,
   "ProcessCounterSale":boolean,
   "ProcessQuickEntry":boolean,
   "QuoteQtyNum":number,
      /**  For this Detail line there is Release line that has Project and Phase and these Project or Phase was invoiced or used in revenue recognition.  */  
   "RelWasRecInvoiced":boolean,
      /**  Pass Credit Limit check message to the UI  */  
   "RespMessage":string,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt1DspDiscount":number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt1DspUnitPrice":number,
      /**  Extended Price for the Order Line in Rpt1 currency  */  
   "Rpt1ExtPrice":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   "Rpt1InMiscCharges":number,
      /**  The amount of discount for display which does not include taxes (report currency)  */  
   "Rpt1LessDiscount":number,
      /**  Report currency misc charges  */  
   "Rpt1MiscCharges":number,
      /**  Report currency line tax amount  */  
   "Rpt1TaxAmt":number,
      /**  Report currency line total price  */  
   "Rpt1TotalPrice":number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt2DspDiscount":number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt2DspUnitPrice":number,
      /**  Extended Price for the orderLine in Rpt2 currency.  */  
   "Rpt2ExtPrice":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   "Rpt2InMiscCharges":number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   "Rpt2LessDiscount":number,
      /**  Report currency misc charges  */  
   "Rpt2MiscCharges":number,
      /**  Report currency line tax amount  */  
   "Rpt2TaxAmt":number,
      /**  Report currency line total price  */  
   "Rpt2TotalPrice":number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt3DspDiscount":number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   "Rpt3DspUnitPrice":number,
      /**  Extended price for the order line in Rpt3 currency  */  
   "Rpt3ExtPrice":number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   "Rpt3InMiscCharges":number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   "Rpt3LessDiscount":number,
      /**  Report Currency misc charges  */  
   "Rpt3MiscCharges":number,
      /**  Report currency line tax amount  */  
   "Rpt3TaxAmt":number,
      /**  Report currency line total price  */  
   "Rpt3TotalPrice":number,
   "SalesRepName1":string,
   "SalesRepName2":string,
   "SalesRepName3":string,
   "SalesRepName4":string,
   "SalesRepName5":string,
      /**  Total tax in base currency. The sum of all the tax details for the line.  */  
   "TaxAmt":number,
      /**  The Sales Order Quantity expressed in the Inventory Unit of Measure  */  
   "ThisOrderInvtyQty":number,
   "TotalPrice":number,
   "TotalShipped":number,
   "WarehouseCode":string,
   "WarehouseDesc":string,
   "BinNum":string,
      /**  Attribute class is MRP Planned but AttributeSetID has not been set on releases.  */  
   "AttributeMismatch":boolean,
      /**  A string containing the parameters needed to run Job Manager  */  
   "JobManagerString":string,
      /**  Default calculated order value based discounts unit price for a particular part/customer.  Used with integrations for pre-order price validations.  */  
   "CalcOrdBasedPrice":number,
      /**  At least 1 OrderRel for OrderDtl has a PONum assigned.  */  
   "SalesOrderLinked":boolean,
      /**  This external column is to be used for the purpose of adding an OrderDtl for a part that has Track Inventory Attributes, allowing the AttributeSetID to be passed in with the line to be included on the OrderRel within the same update method call.  */  
   "InventoryAttributeSetID":number,
   "BitFlag":number,
   "CommodityCodeDescription":string,
   "ContractCodeContractDescription":string,
   "CustNumSendToFSA":boolean,
   "CustNumBTName":string,
   "CustNumCustID":string,
   "CustNumName":string,
   "DiscBreakListCodeListDescription":string,
   "DiscBreakListCodeEndDate":string,
   "DiscBreakListCodeStartDate":string,
   "MktgCampaignIDCampDescription":string,
   "MktgEvntEvntDescription":string,
   "OrderNumBTCustNum":number,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "PartNumSendToFSA":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumAttrClassID":string,
   "PartNumSalesUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumSellingFactor":number,
   "PartNumTrackDimension":boolean,
   "PartNumDefaultAttributeSetID":number,
   "PartNumFSAEquipment":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PriceBreakListDescription":string,
   "PriceBreakStartDate":string,
   "PriceBreakEndDate":string,
   "ProdCodeDescription":string,
   "ProjectIDDescription":string,
   "QuoteNumCurrencyCode":string,
   "SalesCatIDDescription":string,
   "TaxCatIDDescription":string,
   "WarrantyCodeWarrDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "Phase_c":string,
   "ItemID_c":string,
   "TypeCode_c":string,
   "OrigTypeCode_c":string,
   "PhaseID_c":string,
   "SalesCatID_c":string,
   "IndustryShipDate_c":string,
   "CreateDate_c":string,
   "PriceUpdateDate_c":string,
   "CreatedBy_c":string,
   "UpdatedBy_c":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param orderNum
      @param orderLine
   */  
export interface DeleteByID_input{
   orderNum:number,
   orderLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_JobCustTrkRow{
      /**  From JobProd.Company  */  
   Company:string,
      /**  From JobProd.JobNum  */  
   JobNum:string,
      /**  From JobProd.ProdQty  */  
   ProdQty:number,
      /**  From JobProd.ShippedQty  */  
   ShippedQty:number,
      /**  From JobProd.OrderNum  */  
   OrderNum:number,
      /**  From JobProd.OrderLine  */  
   OrderLine:number,
      /**  From JobProd.OrderRelNum  */  
   OrderRelNum:number,
      /**  From OrderRel.NeedByDate  */  
   NeedByDate:string,
      /**  From OrderRel.ReqDate  */  
   ReqDate:string,
      /**  From OrderRel.RevisionNum  */  
   RevisionNum:string,
      /**  From OrderRel.OurReqQty  */  
   OurReqQty:number,
      /**  From JobProd.PartNum  */  
   PartNum:string,
      /**  From JobProd.OrderLineLineDesc  */  
   LineDesc:string,
      /**  From OrderDtl.IUM  */  
   IUM:string,
      /**  From JobHead.ReqDueDate  */  
   ReqDueDate:string,
      /**  From JobHead.StartDate  */  
   StartDate:string,
      /**  From JobHead.DueDate  */  
   DueDate:string,
      /**  From JobHead.Plant  */  
   Plant:string,
      /**  From OrderDtl.CustNum  */  
   CustNum:number,
      /**  From OrderRel.OpenRelease  */  
   OpenRelease:boolean,
      /**  From JobHead.JobFirm  */  
   JobFirm:boolean,
      /**  From JobHead.JobEngineered  */  
   JobEngineered:boolean,
      /**  From JobHead.JobReleased  */  
   JobReleased:boolean,
      /**  From JobHead.JobComplete  */  
   JobComplete:boolean,
      /**  From JobHead.JobClosed  */  
   JobClosed:boolean,
      /**  From JobHead.JobHeld  */  
   JobHeld:boolean,
   ShipToNum:string,
      /**  The full customer's name.  */  
   CustomerName:string,
      /**  The name for the ship to location.  */  
   ShipToName:string,
      /**  The customer ID.  */  
   CustID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobCustTrkTableset{
   JobCustTrk:Erp_Tablesets_JobCustTrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_OrderDtlListRow{
      /**   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   VoidLine:boolean,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   OpenLine:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   OrderLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  EDI Reference  */  
   Reference:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  */  
   Commissionable:boolean,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  */  
   OrderQty:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Discount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DocDiscount:number,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   RequestDate:string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  */  
   OrderComment:string,
      /**  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  */  
   ShipComment:string,
      /**  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  */  
   InvoiceComment:string,
      /**  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  */  
   PickListComment:string,
      /**  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  */  
   TaxCatID:string,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  */  
   AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   DocAdvanceBillBal:number,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  */  
   QuoteNum:number,
      /**  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   QuoteLine:number,
      /**  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  */  
   TMBilling:boolean,
      /**  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  */  
   OrigWhyNoTax:string,
      /**   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  */  
   NeedByDate:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  */  
   CustNum:number,
      /**   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  */  
   Rework:boolean,
      /**   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  */  
   RMANum:number,
      /**  The line item of the RMA detail that this order line item is fulfilling.  */  
   RMALine:number,
      /**  Project ID of the Project table record that this OrderDtl record. Can be blank.  */  
   ProjectID:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  Indicate that the item or the product group has a warranty.  */  
   Warranty:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  Whether the duration of warranty  is for "Days"," Months", "Years".  */  
   MaterialMod:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  */  
   SellingQuantity:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  */  
   ShipLineComplete:boolean,
      /**  Quantity from last EDI update.  */  
   CumeQty:number,
      /**  Date of last update  */  
   CumeDate:string,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgCampaignID:string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgEvntSeq:number,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Indicates if this order line is linked to an inter-company PO line.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
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
      /**  This is the Price List used to determine the starting base price.  */  
   PriceListCode:string,
      /**  This is the Price List used to determine the break % or amount.  */  
   BreakListCode:string,
      /**  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  */  
   PricingQty:number,
      /**  Indicates if the price of the order line can be changed.  */  
   LockPrice:boolean,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   ListPrice:number,
      /**   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  */  
   DocOrdBasedPrice:number,
      /**  This is the Price Group ID used to price the order line with.  */  
   PriceGroupCode:string,
      /**  Indicates if the user selected a price list different from the default.  */  
   OverridePriceList:boolean,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  */  
   PricingValue:number,
      /**  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  */  
   DisplaySeq:number,
      /**  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  */  
   KitParentLine:number,
      /**  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  */  
   KitAllowUpdate:boolean,
      /**  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  */  
   KitShipComplete:boolean,
      /**  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  */  
   KitBackFlush:boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   KitPrintCompsPS:boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   KitPrintCompsInv:boolean,
      /**  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  */  
   KitPricing:string,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  */  
   KitQtyPer:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate1:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate2:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate3:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate4:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate5:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit1:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit2:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit3:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit4:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit5:number,
      /**  The Demand Contract Detail record this OrderDtl is related to.  */  
   DemandContractLine:number,
      /**  Create New Job flag  */  
   CreateNewJob:boolean,
      /**  The date before which the order cannot be shipped.  */  
   DoNotShipBeforeDate:string,
      /**  Get Details flag  */  
   GetDtls:boolean,
      /**  The date after which the order cannot be shipped.  */  
   DoNotShipAfterDate:string,
      /**  Schedule Job flag  */  
   SchedJob:boolean,
      /**  Release Job flag  */  
   RelJob:boolean,
      /**  Enable New Job flag  */  
   EnableCreateNewJob:boolean,
      /**  Enable Get Details flag  */  
   EnableGetDtls:boolean,
      /**  Enable Schedule Job flag  */  
   EnableSchedJob:boolean,
      /**  Enable Release Job flag  */  
   EnableRelJob:boolean,
      /**  Indicates the warehouse selected for a counter sale order line.  */  
   CounterSaleWarehouse:string,
      /**  Identifies the Bin selected for a counter sale order line.  */  
   CounterSaleBinNum:string,
      /**  Indicates the lot number selected for a counter sale order line.  */  
   CounterSaleLotNum:string,
      /**  Indicates the dimension code selected for a counter sales order line.  */  
   CounterSaleDimCode:string,
      /**  Indicates if the demand detail that created/updated this order line has been rejected.  */  
   DemandDtlRejected:boolean,
      /**   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   KitFlag:string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  */  
   KitsLoaded:boolean,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   DemandHeadSeq:number,
      /**  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  */  
   DemandDtlSeq:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Total Number of releases for the line  */  
   TotalReleases:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt1UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt2UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt3UnitPrice:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1Discount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2Discount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3Discount:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt1AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt2AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt3AdvanceBillBal:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1ListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2ListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3ListPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3OrdBasedPrice:number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule  */  
   ExtPriceDtl:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPriceDtl:number,
      /**  Status of Order Line  */  
   LineStatus:string,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  */  
   InUnitPrice:number,
      /**  Same as DocUnit price except that this field contains the unit price including taxes  */  
   DocInUnitPrice:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  */  
   InDiscount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  */  
   DocInDiscount:number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  */  
   InListPrice:number,
      /**   Same as List price except that this field contains the list price in
the customer currency -including taxes.  */  
   DocInListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied. including taxes  */  
   InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  */  
   DocInOrdBasedPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt1InUnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt2InUnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt3InUnitPrice:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1InDiscount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2InDiscount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3InDiscount:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1InListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2InListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3InListPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3InOrdBasedPrice:number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  */  
   InExtPriceDtl:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  */  
   DocInExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPriceDtl:number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   OldOurOpenQty:number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   OldSellingOpenQty:number,
      /**  Used to store open value setting assigned in product configuration programs  */  
   OldOpenValue:number,
      /**  Used to store prod code value assigned in product configuration programs  */  
   OldProdCode:string,
      /**  Previous Selling Quantity  */  
   PrevSellQty:number,
      /**  Previous Part Number  */  
   PrevPartNum:string,
      /**  Previous Customer Part Number  */  
   PrevXPartNum:string,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   KitCompOrigSeq:number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   KitCompOrigPart:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
   DiscBreakListCode:string,
   DiscListPrice:number,
   LockDisc:boolean,
   OverrideDiscPriceList:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrSymbol:string,
   BaseCurrSymbol:string,
   CurrencySwitch:boolean,
   OnHandQuantity:number,
   AvailableQuantity:number,
   TotalShipped:number,
   ExtPrice:number,
   MiscCharges:number,
   TotalPrice:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPrice:number,
   DocMiscCharges:number,
   DocTotalPrice:number,
   Configured:string,
   QuoteQtyNum:number,
   WarehouseCode:string,
   BinNum:string,
   LotNum:string,
   DimCode:string,
   DimConvFactor:number,
   DUM:string,
   ProcessQuickEntry:boolean,
   CounterSale:boolean,
      /**  Available Price Lists  */  
   AvailPriceLists:string,
   ProcessCounterSale:boolean,
   PartTrackLots:boolean,
   PartTrackDimension:boolean,
   DemandQuantity:number,
   AvailUMFromQuote:string,
   FromQuoteLineFlag:boolean,
   MultipleReleases:boolean,
   PartExists:boolean,
   SalesRepName1:string,
   SalesRepName2:string,
   SalesRepName3:string,
   SalesRepName4:string,
   SalesRepName5:string,
   WarehouseDesc:string,
      /**  The message text returned by the credit check process.  */  
   CreditLimitMessage:string,
      /**  The source that put the customer on credit hold.  */  
   CreditLimitSource:string,
      /**  Kit Flag Description. "P" = Parent, "C" = Component.  */  
   KitFlagDescription:string,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   KitDisable:boolean,
      /**  If KitFlag = "C" and the parent kit line is configured OR if KitFlag = "P" and Configured = "On" then this field will be TRUE, otherwise it will be false.  */  
   KitStandard:boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   KitChangeParms:boolean,
   PriceListCodeDesc:string,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   EnableSellingQty:boolean,
      /**  Total tax in base currency. The sum of all the tax details for the line.  */  
   TaxAmt:number,
      /**  Total tax in Doc currency. The sum of all the tax details for the line (OrderRelTax).  */  
   DocTaxAmt:number,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   EnableKitUnitPrice:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   KitOrderQtyUOM:string,
      /**  Report currency misc charges  */  
   Rpt1MiscCharges:number,
      /**  Report currency misc charges  */  
   Rpt2MiscCharges:number,
      /**  Report Currency misc charges  */  
   Rpt3MiscCharges:number,
      /**  Report currency line tax amount  */  
   Rpt1TaxAmt:number,
      /**  Report currency line tax amount  */  
   Rpt2TaxAmt:number,
      /**  Report currency line tax amount  */  
   Rpt3TaxAmt:number,
      /**  Report currency line total price  */  
   Rpt1TotalPrice:number,
      /**  Report currency line total price  */  
   Rpt2TotalPrice:number,
      /**  Report currency line total price  */  
   Rpt3TotalPrice:number,
      /**  The Sales Order Quantity expressed in the Inventory Unit of Measure  */  
   ThisOrderInvtyQty:number,
      /**  Inventory UOM that the Order Detail is allocated against.  */  
   InvtyUOM:string,
      /**  Indicates whether the part has at least one Complement  */  
   HasComplement:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasUpgrade:boolean,
      /**  Indicates whether the part has at least one Downgrade  */  
   HasDowngrade:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasSubstitute:boolean,
      /**  Extended Price for the Order Line in Rpt1 currency  */  
   Rpt1ExtPrice:number,
      /**  Extended Price for the orderLine in Rpt2 currency.  */  
   Rpt2ExtPrice:number,
      /**  Extended price for the order line in Rpt3 currency  */  
   Rpt3ExtPrice:number,
   BaseCurrencyID:string,
   CurrencyID:string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLineRef:string,
      /**  Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DspDiscount:number,
      /**  Document currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DocDspDiscount:number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt1DspDiscount:number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt2DspDiscount:number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt3DspDiscount:number,
      /**  Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DspUnitPrice:number,
      /**  Document currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DocDspUnitPrice:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt1DspUnitPrice:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt2DspUnitPrice:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt3DspUnitPrice:number,
      /**  The flag to indicate if the Order Header Tax Liability is Tax Inclusive Pricing.  */  
   InPrice:boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   EntryProcess:string,
      /**  The amount of discount for display in document currency which does not include taxes  */  
   DocLessDiscount:number,
      /**  The amount of discount for display which does not include taxes  */  
   LessDiscount:number,
      /**  The amount of discount for display which does not include taxes (report currency)  */  
   Rpt1LessDiscount:number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   Rpt2LessDiscount:number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   Rpt3LessDiscount:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in document currency  */  
   DocInMiscCharges:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line  */  
   InMiscCharges:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt1InMiscCharges:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt2InMiscCharges:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt3InMiscCharges:number,
      /**  Description of the service contract.  */  
   ContractCodeContractDescription:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  Description of the Marketing campaign  */  
   MktgCampaignIDCampDescription:string,
      /**  Description.  */  
   MktgEvntEvntDescription:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
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
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Full description of Product Group.  */  
   ProdCodeDescription:string,
      /**  Full description of Project Management Code.  */  
   ProjectIDDescription:string,
      /**  A unique code that identifies the currency.  */  
   QuoteNumCurrencyCode:string,
      /**  Description of the sales category.  */  
   SalesCatIDDescription:string,
      /**  Full description for the Sales Tax category.  */  
   TaxCatIDDescription:string,
      /**  Description of the warranty.  */  
   WarrantyCodeWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderDtlListTableset{
   OrderDtlList:Erp_Tablesets_OrderDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_OrderDtlRow{
      /**   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   VoidLine:boolean,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   OpenLine:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   OrderLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  EDI Reference  */  
   Reference:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  */  
   Commissionable:boolean,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  */  
   OrderQty:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Discount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DocDiscount:number,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   RequestDate:string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  */  
   OrderComment:string,
      /**  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  */  
   ShipComment:string,
      /**  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  */  
   InvoiceComment:string,
      /**  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  */  
   PickListComment:string,
      /**  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  */  
   TaxCatID:string,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  */  
   AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   DocAdvanceBillBal:number,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  */  
   QuoteNum:number,
      /**  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   QuoteLine:number,
      /**  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  */  
   TMBilling:boolean,
      /**  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  */  
   OrigWhyNoTax:string,
      /**   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  */  
   NeedByDate:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  */  
   CustNum:number,
      /**   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  */  
   Rework:boolean,
      /**   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  */  
   RMANum:number,
      /**  The line item of the RMA detail that this order line item is fulfilling.  */  
   RMALine:number,
      /**  Project ID of the Project table record that this OrderDtl record. Can be blank.  */  
   ProjectID:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  Indicate that the item or the product group has a warranty.  */  
   Warranty:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  Whether the duration of warranty  is for "Days"," Months", "Years".  */  
   MaterialMod:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  */  
   SellingQuantity:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  */  
   ShipLineComplete:boolean,
      /**  Quantity from last EDI update.  */  
   CumeQty:number,
      /**  Date of last update  */  
   CumeDate:string,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgCampaignID:string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgEvntSeq:number,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Indicates if this order line is linked to an inter-company PO line.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
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
      /**  This is the Price List used to determine the starting base price.  */  
   PriceListCode:string,
      /**  This is the Price List used to determine the break % or amount.  */  
   BreakListCode:string,
      /**  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  */  
   PricingQty:number,
      /**  Indicates if the price of the order line can be changed.  */  
   LockPrice:boolean,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   ListPrice:number,
      /**   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  */  
   DocOrdBasedPrice:number,
      /**  This is the Price Group ID used to price the order line with.  */  
   PriceGroupCode:string,
      /**  Indicates if the user selected a price list different from the default.  */  
   OverridePriceList:boolean,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  */  
   PricingValue:number,
      /**  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  */  
   DisplaySeq:number,
      /**  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  */  
   KitParentLine:number,
      /**  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  */  
   KitAllowUpdate:boolean,
      /**  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  */  
   KitShipComplete:boolean,
      /**  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  */  
   KitBackFlush:boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   KitPrintCompsPS:boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   KitPrintCompsInv:boolean,
      /**  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  */  
   KitPricing:string,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  */  
   KitQtyPer:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate1:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate2:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate3:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate4:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate5:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit1:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit2:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit3:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit4:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit5:number,
      /**  The Demand Contract Detail record this OrderDtl is related to.  */  
   DemandContractLine:number,
      /**  Create New Job flag  */  
   CreateNewJob:boolean,
      /**  The date before which the order cannot be shipped.  */  
   DoNotShipBeforeDate:string,
      /**  Get Details flag  */  
   GetDtls:boolean,
      /**  The date after which the order cannot be shipped.  */  
   DoNotShipAfterDate:string,
      /**  Schedule Job flag  */  
   SchedJob:boolean,
      /**  Release Job flag  */  
   RelJob:boolean,
      /**  Enable New Job flag  */  
   EnableCreateNewJob:boolean,
      /**  Enable Get Details flag  */  
   EnableGetDtls:boolean,
      /**  Enable Schedule Job flag  */  
   EnableSchedJob:boolean,
      /**  Enable Release Job flag  */  
   EnableRelJob:boolean,
      /**  Indicates the warehouse selected for a counter sale order line.  */  
   CounterSaleWarehouse:string,
      /**  Identifies the Bin selected for a counter sale order line.  */  
   CounterSaleBinNum:string,
      /**  Indicates the lot number selected for a counter sale order line.  */  
   CounterSaleLotNum:string,
      /**  Indicates the dimension code selected for a counter sales order line.  */  
   CounterSaleDimCode:string,
      /**  Indicates if the demand detail that created/updated this order line has been rejected.  */  
   DemandDtlRejected:boolean,
      /**   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   KitFlag:string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  */  
   KitsLoaded:boolean,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   DemandHeadSeq:number,
      /**  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  */  
   DemandDtlSeq:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Total Number of releases for the line  */  
   TotalReleases:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt1UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt2UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt3UnitPrice:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1Discount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2Discount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3Discount:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt1AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt2AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt3AdvanceBillBal:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1ListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2ListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3ListPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3OrdBasedPrice:number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule  */  
   ExtPriceDtl:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPriceDtl:number,
      /**  Status of Order Line  */  
   LineStatus:string,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  */  
   InUnitPrice:number,
      /**  Same as DocUnit price except that this field contains the unit price including taxes  */  
   DocInUnitPrice:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  */  
   InDiscount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  */  
   DocInDiscount:number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  */  
   InListPrice:number,
      /**   Same as List price except that this field contains the list price in
the customer currency -including taxes.  */  
   DocInListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied. including taxes  */  
   InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  */  
   DocInOrdBasedPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt1InUnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt2InUnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt3InUnitPrice:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1InDiscount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2InDiscount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3InDiscount:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1InListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2InListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3InListPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3InOrdBasedPrice:number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  */  
   InExtPriceDtl:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  */  
   DocInExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPriceDtl:number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   OldOurOpenQty:number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   OldSellingOpenQty:number,
      /**  Used to store open value setting assigned in product configuration programs  */  
   OldOpenValue:number,
      /**  Used to store prod code value assigned in product configuration programs  */  
   OldProdCode:string,
      /**  Previous Selling Quantity  */  
   PrevSellQty:number,
      /**  Previous Part Number  */  
   PrevPartNum:string,
      /**  Previous Customer Part Number  */  
   PrevXPartNum:string,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   KitCompOrigSeq:number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   KitCompOrigPart:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
   DiscBreakListCode:string,
   DiscListPrice:number,
   LockDisc:boolean,
   OverrideDiscPriceList:boolean,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  ECCOrderNum  */  
   ECCOrderNum:string,
      /**  ECCOrderLine  */  
   ECCOrderLine:number,
      /**  DupOnJobCrt  */  
   DupOnJobCrt:boolean,
      /**  UndersPct  */  
   UndersPct:number,
      /**  Overs  */  
   Overs:number,
      /**  Unders  */  
   Unders:number,
      /**  OversUnitPrice  */  
   OversUnitPrice:number,
      /**  PlanUserID  */  
   PlanUserID:string,
      /**  PlanGUID  */  
   PlanGUID:string,
      /**  MOMsourceType  */  
   MOMsourceType:string,
      /**  MOMsourceEst  */  
   MOMsourceEst:string,
      /**  DefaultOversPricing  */  
   DefaultOversPricing:string,
      /**  ECCPlant  */  
   ECCPlant:string,
      /**  ECCQuoteNum  */  
   ECCQuoteNum:string,
      /**  ECCQuoteLine  */  
   ECCQuoteLine:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MfgJobType  */  
   MfgJobType:string,
      /**  ProFormaInvComment  */  
   ProFormaInvComment:string,
      /**  CreateJob  */  
   CreateJob:boolean,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  DocInAdvanceBillBal  */  
   DocInAdvanceBillBal:number,
      /**  InAdvanceBillBal  */  
   InAdvanceBillBal:number,
      /**  Rpt1InAdvanceBillBal  */  
   Rpt1InAdvanceBillBal:number,
      /**  Rpt2InAdvanceBillBal  */  
   Rpt2InAdvanceBillBal:number,
      /**  Rpt3InAdvanceBillBal  */  
   Rpt3InAdvanceBillBal:number,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  CommodityCode  */  
   CommodityCode:string,
      /**  Base price before any price breaks and discounts  */  
   MSRP:number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocMSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt1MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt2MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt3MSRP:number,
      /**  Distributor end customer price.  */  
   EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocEndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt1EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt2EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt3EndCustomerPrice:number,
      /**  Promotional Price offered to Dealer and Distributors.  */  
   PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocPromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt1PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt2PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt3PromotionalPrice:number,
      /**  Current status of line.  This is a maintainable status through Order Line Status maintenance.  Depending on the setting can control is line is updatable from the web.  */  
   OrderLineStatusCode:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  */  
   AttributeSetID:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   KBOriginalConfigProdID:number,
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
   AvailableQuantity:number,
      /**  Available Price Lists  */  
   AvailPriceLists:string,
   AvailUMFromQuote:string,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
      /**  Default calculated unit price for a particular part/customer.  Used with integrations for pre-order price validations.  */  
   CalcUnitPrice:number,
   ConfigType:string,
   Configured:string,
   CounterSale:boolean,
      /**  The message text returned by the credit check process.  */  
   CreditLimitMessage:string,
      /**  The source that put the customer on credit hold.  */  
   CreditLimitSource:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencyID:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DemandQuantity:number,
   DimCode:string,
   DimConvFactor:number,
      /**  Document currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DocDspDiscount:number,
      /**  Document currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DocDspUnitPrice:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in document currency  */  
   DocInMiscCharges:number,
      /**  The amount of discount for display in document currency which does not include taxes  */  
   DocLessDiscount:number,
   DocMiscCharges:number,
      /**  Total tax in Doc currency. The sum of all the tax details for the line (OrderRelTax).  */  
   DocTaxAmt:number,
   DocTotalPrice:number,
      /**  Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DspDiscount:number,
      /**  To display the type of job this is: MFG = Manufacturing, PRJ = Project  */  
   DspJobType:string,
      /**  Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DspUnitPrice:number,
   DUM:string,
      /**  Web basket configuration related SysRowID  */  
   ECCConfigSysRowId:string,
      /**  Additional discount calculated by ECC  */  
   ECCDiscount:number,
      /**  Prevents Epicor repricing the unit price coming from ECC.  This usually would be a result of Epicor going off-line and order pricing was performed by ECC.  */  
   ECCPreventRepricing:boolean,
      /**  Allow enable/disable for the button Attibutes in Order Line  */  
   EnableDynAttrButton:boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   EnableKitUnitPrice:boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   EnableRenewalNbr:boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   EnableSellingQty:boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   EntryProcess:string,
   ExtPrice:number,
   FromQuoteLineFlag:boolean,
      /**  Installation price of an equipment that requires installation in Epicor FSA. This value by default is inherited from the part but it could be overridden for another value if it's necessary.  */  
   FSAInstallationCost:number,
   FSAInstallationOrderLine:number,
   FSAInstallationOrderNum:number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   FSAInstallationRequired:boolean,
      /**  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  */  
   FSAInstallationType:string,
   FSAInstallationTypeDescription:string,
      /**  Indicates whether the part has at least one Complement  */  
   HasComplement:boolean,
      /**  Indicates whether the part has at least one Downgrade  */  
   HasDowngrade:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasSubstitute:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasUpgrade:boolean,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line  */  
   InMiscCharges:number,
      /**  The flag to indicate if the Order Header Tax Liability is Tax Inclusive Pricing.  */  
   InPrice:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Inventory UOM that the Order Detail is allocated against.  */  
   InvtyUOM:string,
   JobTypeDesc:string,
      /**  If the Job has been already created against this line.  */  
   JobWasCreated:boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   KitChangeParms:boolean,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   KitDisable:boolean,
      /**  Kit Flag Description. "P" = Parent, "C" = Component.  */  
   KitFlagDescription:string,
   KitOrderQtyUOM:string,
      /**  If KitFlag = "C" and the parent kit line is configured OR if KitFlag = "P" and Configured = "On" then this field will be TRUE, otherwise it will be false.  */  
   KitStandard:boolean,
      /**  The amount of discount for display which does not include taxes  */  
   LessDiscount:number,
   LotNum:string,
   MiscCharges:number,
   MultipleReleases:boolean,
   OnHandQuantity:number,
   PartExists:boolean,
   PartTrackDimension:boolean,
   PartTrackLots:boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLineRef:string,
   PriceListCodeDesc:string,
   ProcessCounterSale:boolean,
   ProcessQuickEntry:boolean,
   QuoteQtyNum:number,
      /**  For this Detail line there is Release line that has Project and Phase and these Project or Phase was invoiced or used in revenue recognition.  */  
   RelWasRecInvoiced:boolean,
      /**  Pass Credit Limit check message to the UI  */  
   RespMessage:string,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt1DspDiscount:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt1DspUnitPrice:number,
      /**  Extended Price for the Order Line in Rpt1 currency  */  
   Rpt1ExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt1InMiscCharges:number,
      /**  The amount of discount for display which does not include taxes (report currency)  */  
   Rpt1LessDiscount:number,
      /**  Report currency misc charges  */  
   Rpt1MiscCharges:number,
      /**  Report currency line tax amount  */  
   Rpt1TaxAmt:number,
      /**  Report currency line total price  */  
   Rpt1TotalPrice:number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt2DspDiscount:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt2DspUnitPrice:number,
      /**  Extended Price for the orderLine in Rpt2 currency.  */  
   Rpt2ExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt2InMiscCharges:number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   Rpt2LessDiscount:number,
      /**  Report currency misc charges  */  
   Rpt2MiscCharges:number,
      /**  Report currency line tax amount  */  
   Rpt2TaxAmt:number,
      /**  Report currency line total price  */  
   Rpt2TotalPrice:number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt3DspDiscount:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt3DspUnitPrice:number,
      /**  Extended price for the order line in Rpt3 currency  */  
   Rpt3ExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt3InMiscCharges:number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   Rpt3LessDiscount:number,
      /**  Report Currency misc charges  */  
   Rpt3MiscCharges:number,
      /**  Report currency line tax amount  */  
   Rpt3TaxAmt:number,
      /**  Report currency line total price  */  
   Rpt3TotalPrice:number,
   SalesRepName1:string,
   SalesRepName2:string,
   SalesRepName3:string,
   SalesRepName4:string,
   SalesRepName5:string,
      /**  Total tax in base currency. The sum of all the tax details for the line.  */  
   TaxAmt:number,
      /**  The Sales Order Quantity expressed in the Inventory Unit of Measure  */  
   ThisOrderInvtyQty:number,
   TotalPrice:number,
   TotalShipped:number,
   WarehouseCode:string,
   WarehouseDesc:string,
   BinNum:string,
      /**  Attribute class is MRP Planned but AttributeSetID has not been set on releases.  */  
   AttributeMismatch:boolean,
      /**  A string containing the parameters needed to run Job Manager  */  
   JobManagerString:string,
      /**  Default calculated order value based discounts unit price for a particular part/customer.  Used with integrations for pre-order price validations.  */  
   CalcOrdBasedPrice:number,
      /**  At least 1 OrderRel for OrderDtl has a PONum assigned.  */  
   SalesOrderLinked:boolean,
      /**  This external column is to be used for the purpose of adding an OrderDtl for a part that has Track Inventory Attributes, allowing the AttributeSetID to be passed in with the line to be included on the OrderRel within the same update method call.  */  
   InventoryAttributeSetID:number,
   BitFlag:number,
   CommodityCodeDescription:string,
   ContractCodeContractDescription:string,
   CustNumSendToFSA:boolean,
   CustNumBTName:string,
   CustNumCustID:string,
   CustNumName:string,
   DiscBreakListCodeListDescription:string,
   DiscBreakListCodeEndDate:string,
   DiscBreakListCodeStartDate:string,
   MktgCampaignIDCampDescription:string,
   MktgEvntEvntDescription:string,
   OrderNumBTCustNum:number,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartNumSendToFSA:boolean,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumDefaultAttributeSetID:number,
   PartNumFSAEquipment:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PriceBreakListDescription:string,
   PriceBreakStartDate:string,
   PriceBreakEndDate:string,
   ProdCodeDescription:string,
   ProjectIDDescription:string,
   QuoteNumCurrencyCode:string,
   SalesCatIDDescription:string,
   TaxCatIDDescription:string,
   WarrantyCodeWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   Phase_c:string,
   ItemID_c:string,
   TypeCode_c:string,
   OrigTypeCode_c:string,
   PhaseID_c:string,
   SalesCatID_c:string,
   IndustryShipDate_c:string,
   CreateDate_c:string,
   PriceUpdateDate_c:string,
   CreatedBy_c:string,
   UpdatedBy_c:string,
}

export interface Erp_Tablesets_OrderDtlSearchTableset{
   OrderDtl:Erp_Tablesets_OrderDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtOrderDtlSearchTableset{
   OrderDtl:Erp_Tablesets_OrderDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param orderNum
      @param orderLine
   */  
export interface GetByID_input{
   orderNum:number,
   orderLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_OrderDtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_OrderDtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_OrderDtlSearchTableset[],
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
   returnObj:Erp_Tablesets_OrderDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param orderNum
   */  
export interface GetNewOrderDtl_input{
   ds:Erp_Tablesets_OrderDtlSearchTableset[],
   orderNum:number,
}

export interface GetNewOrderDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderDtlSearchTableset[],
}
}

   /** Required : 
      @param whereClauseOrderDtl
      @param whereClauseOrderRel
      @param jobWhereClause
      @param contactName
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsContactTracker_input{
      /**  Whereclause for OrderDtl table.  */  
   whereClauseOrderDtl:string,
      /**  Whereclause for OrderRel table.  */  
   whereClauseOrderRel:string,
      /**  Whereclause for Job table.  */  
   jobWhereClause:string,
      /**  Contact name to return records for.  */  
   contactName:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsContactTracker_output{
   returnObj:Erp_Tablesets_JobCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param whereClauseOrderDtl
      @param whereClauseOrderRel
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerActivity_input{
      /**  Whereclause for Job table.  */  
   whereClause:string,
      /**  Whereclause for OrderDtl table.  */  
   whereClauseOrderDtl:string,
      /**  Whereclause for OrderRel table.  */  
   whereClauseOrderRel:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerActivity_output{
   returnObj:Erp_Tablesets_JobCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseOrderDtl
      @param whereClauseOrderRel
      @param jobWhereClause
      @param sortBy
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTrackerAndSort_input{
      /**  Whereclause for OrderDtl table.  */  
   whereClauseOrderDtl:string,
      /**  Whereclause for OrderRel table.  */  
   whereClauseOrderRel:string,
      /**  Whereclause for Job table.  */  
   jobWhereClause:string,
      /**  Page size.  */  
   sortBy:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTrackerAndSort_output{
   returnObj:Erp_Tablesets_JobCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseOrderDtl
      @param whereClauseOrderRel
      @param jobWhereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTracker_input{
      /**  Whereclause for OrderDtl table.  */  
   whereClauseOrderDtl:string,
      /**  Whereclause for OrderRel table.  */  
   whereClauseOrderRel:string,
      /**  Whereclause for Job table.  */  
   jobWhereClause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTracker_output{
   returnObj:Erp_Tablesets_JobCustTrkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseOrderDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseOrderDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_OrderDtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtOrderDtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtOrderDtlSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_OrderDtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderDtlSearchTableset[],
}
}

   /** Required : 
      @param pcListCode
      @param pcPartNum
      @param pcLineWarehouse
      @param pcCurrencyCode
      @param pdtOrderDate
   */  
export interface getBreakListCodeDesc_input{
      /**  pcListCode  */  
   pcListCode:string,
      /**  pcPartNum  */  
   pcPartNum:string,
      /**  pcLineWarehouse  */  
   pcLineWarehouse:string,
      /**  pcCurrencyCode  */  
   pcCurrencyCode:string,
      /**  pdtOrderDate  */  
   pdtOrderDate:string,
}

export interface getBreakListCodeDesc_output{
      /**  A list in a string  */  
   returnObj:string,
}

