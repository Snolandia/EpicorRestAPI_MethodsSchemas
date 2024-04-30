import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.OrderRelSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/$metadata", {
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
   Description: Get OrderRelSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OrderRelSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderRelRow
   */  
export function get_OrderRelSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderRelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/OrderRelSearches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderRelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OrderRelSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OrderRelRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.OrderRelRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OrderRelSearches(requestBody:Erp_Tablesets_OrderRelRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/OrderRelSearches", {
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
   Summary: Calls GetByID to retrieve the OrderRelSearch item
   Description: Calls GetByID to retrieve the OrderRelSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OrderRelSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.OrderRelRow
   */  
export function get_OrderRelSearches_Company_OrderNum_OrderLine_OrderRelNum(Company:string, OrderNum:string, OrderLine:string, OrderRelNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_OrderRelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/OrderRelSearches(" + Company + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + ")", {
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
         resolve(data as Erp_Tablesets_OrderRelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update OrderRelSearch for the service
   Description: Calls UpdateExt to update OrderRelSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OrderRelSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.OrderRelRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_OrderRelSearches_Company_OrderNum_OrderLine_OrderRelNum(Company:string, OrderNum:string, OrderLine:string, OrderRelNum:string, requestBody:Erp_Tablesets_OrderRelRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/OrderRelSearches(" + Company + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + ")", {
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
   Summary: Call UpdateExt to delete OrderRelSearch item
   Description: Call UpdateExt to delete OrderRelSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OrderRelSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param OrderNum Desc: OrderNum   Required: True
      @param OrderLine Desc: OrderLine   Required: True
      @param OrderRelNum Desc: OrderRelNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_OrderRelSearches_Company_OrderNum_OrderLine_OrderRelNum(Company:string, OrderNum:string, OrderLine:string, OrderRelNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/OrderRelSearches(" + Company + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderRelListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderRelListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderRelListRow)
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
export function get_GetRows(whereClauseOrderRel:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseOrderRel!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseOrderRel=" + whereClauseOrderRel
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/GetRows" + params, {
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(orderNum:string, orderLine:string, orderRelNum:string, epicorHeaders?:Headers){
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
   if(typeof orderRelNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orderRelNum=" + orderRelNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetListByCustNum
   Description: This method returns a list of OrderRel filtered by CustNum.
   OperationID: GetListByCustNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListByCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListByCustNum(requestBody:GetListByCustNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListByCustNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/GetListByCustNum", {
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
         resolve(data as GetListByCustNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListFilterShipped
   Description: This method returns a list of open OrderRel.
   OperationID: GetListFilterShipped
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListFilterShipped_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFilterShipped_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListFilterShipped(requestBody:GetListFilterShipped_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListFilterShipped_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/GetListFilterShipped", {
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
         resolve(data as GetListFilterShipped_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewOrderRel
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOrderRel
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewOrderRel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOrderRel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewOrderRel(requestBody:GetNewOrderRel_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewOrderRel_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/GetNewOrderRel", {
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
         resolve(data as GetNewOrderRel_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderRelSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderRelListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OrderRelListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderRelRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OrderRelRow,
}

export interface Erp_Tablesets_OrderRelListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Sales Order Number  */  
   "OrderNum":number,
      /**  Sales order Line number that this order release is linked to.  */  
   "OrderLine":number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   "OrderRelNum":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   "ReqDate":string,
      /**  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   "OurReqQty":number,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
      /**  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  */  
   "ShipViaCode":string,
      /**  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   "OpenRelease":boolean,
      /**  Indicates if this release is  "FIRM". The opposite is an uncommitted release, that is when the customer gives releases that are just 'Best Guesses' of what they will require in the future, such as in blanket order situations. This type of  releases is no different to the system, except that the FirmRelease field will be printed on reports such as TimePhase requirements.  */  
   "FirmRelease":boolean,
      /**   Indicates if this requirement or any part of it will be manufactured. Default the setting to "No" if valid Part and the Part.Type is "S" or "P".

Default the setting to "Yes" if the part is not found in Part master or the Part.Type = "J".  This flag also gets set if this release gets linked to a Job via Job Entry. There is an Index on this field so that we can display releases that need have a job assigned to them. This display is part of Job Entry.  */  
   "Make":boolean,
      /**  The planned production quantity, using Our U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   "OurJobQty":number,
      /**  Actual quantity, using our U/M, shipped from the Job.  Updated via the shipping process.  */  
   "OurJobShippedQty":number,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.

When an OrderRel record is 'voided' any outstanding inventory allocations are relieved, OrderRel.OpenRelease is set to "no" and records are created/updated in the OrdJobMsg file for all the related  open OrderRel records if the OrderDtl that was tied to a Job to indicate that the line item was voided.  */  
   "VoidRelease":boolean,
      /**  Quantity, using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   "OurStockQty":number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   "WarehouseCode":string,
      /**  Actual quantity, using our U/M, shipped from Stock.  Updated via the shipping process.  */  
   "OurStockShippedQty":number,
      /**  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  */  
   "PartNum":string,
      /**  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  */  
   "RevisionNum":string,
      /**  Indicates if this customer/shipto  is exempt from sales tax for this line item. If field is non-blank it is considered exempt. Defaults from the Customer/Shipto file.  This code is totally user definable and no validation is required. This field will be printed on the Tax report if this item is reportable .  */  
   "TaxExempt":string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Enter via a DDSL fill-in for contact name. Use OrderHed.ShpConNum when the OrderRel.ShipToNum = OrderHed.ShipToNum else use ShipTo.PrimScon as a default.  */  
   "ShpConNum":number,
      /**  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  */  
   "NeedByDate":string,
      /**  EDI Reference  */  
   "Reference":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   "SellingReqQty":number,
      /**  The planned production quantity, using selling U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   "SellingJobQty":number,
      /**  Actual quantity, using selling U/M, shipped from the Job.  Updated via the shipping process.  */  
   "SellingJobShippedQty":number,
      /**  Quantity, using selling U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   "SellingStockQty":number,
      /**  Actual quantity, using selling U/M, shipped from Stock.  Updated via the shipping process.  */  
   "SellingStockShippedQty":number,
      /**  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   "SelectForPicking":boolean,
      /**  The shipping "Staging" warehouse for the release.  Defaults from the system default shipping area (Site.DefShippingWhse). This is maintainable in the Sales Allocation program.  */  
   "StagingWarehouseCode":string,
      /**  The shipping "Staging" bin for the release.  Defaults from the system default shipping area (Site.DefShippingBin). This is maintainable in the Sales Allocation program.  */  
   "StagingBinNum":string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   "PickError":string,
      /**  Quantity from last EDI update.  */  
   "CumeQty":number,
      /**  Date of last update  */  
   "CumeDate":string,
      /**  Indicates if this order release is linked to an inter-company PO release.  */  
   "Linked":boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   "ICPONum":number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ICPOLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "ICPORelNum":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  A link to the demand schedule that created/updated this OrderRel.  */  
   "ScheduleNumber":string,
      /**  The Mark For to be used for this order release record. This MUST BE VALID IN THE SHIPTO file.  */  
   "MarkForNum":string,
      /**  Full name for the drop shipment.  */  
   "DropShipName":string,
      /**  RAN Number.  Used for informational purposes.  Supplied by EDI.  */  
   "RAN":string,
      /**  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  */  
   "DemandReference":string,
      /**  Indicates if the demand schedule that created/updated this order release has been rejected.  */  
   "DemandSchedRejected":boolean,
      /**  The last date that the Material Queue Report was run for this release.  This field will be null until the Material Queue Report is run.  */  
   "DatePickTicketPrinted":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Verbal Confirmation required  */  
   "VerbalConf":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Is a Service Saturday delivery acceptable  */  
   "ServSatDelivery":boolean,
      /**  Is a Service Saturday pickup available  */  
   "ServSatPickup":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Auto POD flag  */  
   "ServPOD":boolean,
      /**  AOD  */  
   "ServAOD":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   "OverrideCarrier":boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   "OverrideService":boolean,
      /**  The dockingstation of the shipto address.  For future use.  */  
   "DockingStation":string,
      /**  The location within the customer shipto address.  For future use.  */  
   "Location":string,
      /**  The code of the transport routing/time. For future use.  */  
   "TransportID":string,
      /**  Ship the good by this time.  */  
   "ShipbyTime":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  If true, the OrderRelTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the release before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**  Indicates that the One Time ShipTO information defined for this release should be used.  */  
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
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipment country  */  
   "OTSCountryNum":number,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  */  
   "SubShipTo":string,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  */  
   "ShipRouting":string,
      /**  This field identifies Buy To Order releases.  */  
   "BuyToOrder":boolean,
      /**  The value for this field will be defaulted from the Supplier defined in the Part Site sub tab at the Part form. Used only for Buy To Order releases.  */  
   "VendorNum":number,
      /**  Supplier Purchase Point. Used only for Buy To Order releases.  */  
   "PurPoint":string,
      /**  This field identifies Drop Ship releases. Used only for Buy To Order releases.  */  
   "DropShip":boolean,
      /**  Purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   "PONum":number,
      /**  The line number of the purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   "POLine":number,
      /**  The release number of the purchase order line related to this Buy To Order release. Used only for Buy To Order releases.  */  
   "PORelNum":number,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   "OpenOrder":boolean,
      /**  Indicates if/how the OTS can be saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   "OTSSaveAs":string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   "OTSSaveCustID":string,
      /**  True if Customer or ShipTo record was created using the OTS info.  */  
   "OTSCustSaved":boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**   Unit of Measure that qualifies the "our" quantity fields.
If a valid part then it is the Base Stocking UOM (Part.IUM).
A mirror image of OrderDtl.IUM. Not directly maintainable  */  
   "IUM":string,
      /**   Selling Unit of measure. Qualifies the "Selling" quantity fields.
A mirror image of OrderDtl.SalesUM. Not directly maintainable.  */  
   "SalesUM":string,
      /**  Status of Order Release  */  
   "RelStatus":string,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  Previous Selling Quantity  */  
   "PrevSellQty":number,
      /**  Previous Part Number  */  
   "PrevPartNum":string,
      /**  Previous Customer Part Number  */  
   "PrevXPartNum":string,
      /**  Previous Need By Date  */  
   "PrevNeedByDate":string,
      /**  Previous Require Date  */  
   "PrevReqDate":string,
      /**  Previous Ship To Num  */  
   "PrevShipToNum":string,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   "MFCustNum":number,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   "UseOTMF":boolean,
      /**  One Time Mark For Name of the ShipTo.  */  
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  OTSShipToNum  */  
   "OTSShipToNum":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "OnHandQuantity":number,
   "AvailableQuantity":number,
   "ShipToAddressList":string,
   "ShipToContactName":string,
   "MakeOverride":boolean,
   "EnableMake":boolean,
   "PartExists":boolean,
   "ReleaseStatus":string,
   "CustomerCustID":string,
   "CustomerName":string,
   "VoidOrder":boolean,
      /**  The message returned when checking a customer credit limit.  */  
   "CreditLimitMessage":string,
      /**  The source that put the customer on credit hold.  */  
   "CreditLimitSource":string,
      /**  Selling Factor for display only  */  
   "SellingFactor":number,
      /**  Selling Factor Direction for display oly  */  
   "SellingFactorDirection":string,
   "ShipToContactEMailAddress":string,
   "AllowTaxCodeUpd":boolean,
      /**  Invoice Tax  */  
   "TotalTax":number,
   "DocTotalTax":number,
   "TotalJobStockShipped":number,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "SNEnable":boolean,
      /**  ExistPOSugg, external field to show/hide an epishape  */  
   "ExistPOSugg":boolean,
      /**  LinkToPONum, external field to show/hide an epishape  */  
   "LinkToPONum":boolean,
      /**  Self-Assessed Tax  */  
   "SelfAssessTax":number,
      /**  Withholding Tax  */  
   "WithholdTax":number,
   "DocWithholdTax":number,
   "DocSelfAssessTax":number,
   "HdrOTS":boolean,
   "Rpt1TotalTax":number,
   "Rpt2TotalTax":number,
   "Rpt3TotalTax":number,
   "Rpt1WithholdTax":number,
   "Rpt2WithholdTax":number,
   "Rpt3WithholdTax":number,
   "Rpt1SelfAssessTax":number,
   "Rpt2SelfAssessTax":number,
   "Rpt3SelfAssessTax":number,
      /**  BuyOverride  */  
   "BuyOverride":boolean,
      /**  DropShipOverride  */  
   "DropShipOverride":boolean,
   "ThisRelInvtyQty":number,
      /**  SalesOrderLinked  */  
   "SalesOrderLinked":boolean,
   "OTSSaved":boolean,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   "NotCompliant":boolean,
      /**  Is OTS allowed by the Sold to Customer?  */  
   "CustAllowOTS":boolean,
      /**  True when Customer allows shipping to a Third-Party  */  
   "CustomerAllowShipTo3":boolean,
      /**  OTS Tax Liability Code (Order Release)  */  
   "OTSTaxRegionCode":string,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   "EntryProcess":string,
   "MFCustID":string,
      /**  Contains the Mark For Address  */  
   "MarkForAddrList":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "OrderLineLineDesc":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  Country name  */  
   "OTMFCountryDescription":string,
      /**  Country name  */  
   "OTSCntryDescription":string,
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
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Second address line  */  
   "PurPointAddress2":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "PurPointCountry":string,
      /**  State portion of the address  */  
   "PurPointState":string,
      /**  Third address line  */  
   "PurPointAddress3":string,
      /**  Purchase Point Name...can't be blank.  */  
   "PurPointName":string,
      /**  Postal Code or Zip code portion of the address  */  
   "PurPointZip":string,
      /**  First address line  */  
   "PurPointAddress1":string,
      /**  City portion of the address  */  
   "PurPointCity":string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "PurPointPrimPCon":number,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  Full description for the Tax Region.  */  
   "TaxRegionCodeDescription":string,
      /**  The full name of the customer.  */  
   "TPShipToName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "TPShipToBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "TPShipToCustID":string,
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
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_OrderRelRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Sales Order Number  */  
   "OrderNum":number,
      /**  Sales order Line number that this order release is linked to.  */  
   "OrderLine":number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   "OrderRelNum":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   "ReqDate":string,
      /**  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   "OurReqQty":number,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
      /**  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  */  
   "ShipViaCode":string,
      /**  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   "OpenRelease":boolean,
      /**  Indicates if this release is  "FIRM". The opposite is an uncommitted release, that is when the customer gives releases that are just 'Best Guesses' of what they will require in the future, such as in blanket order situations. This type of  releases is no different to the system, except that the FirmRelease field will be printed on reports such as TimePhase requirements.  */  
   "FirmRelease":boolean,
      /**   Indicates if this requirement or any part of it will be manufactured. Default the setting to "No" if valid Part and the Part.Type is "S" or "P".

Default the setting to "Yes" if the part is not found in Part master or the Part.Type = "J".  This flag also gets set if this release gets linked to a Job via Job Entry. There is an Index on this field so that we can display releases that need have a job assigned to them. This display is part of Job Entry.  */  
   "Make":boolean,
      /**  The planned production quantity, using Our U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   "OurJobQty":number,
      /**  Actual quantity, using our U/M, shipped from the Job.  Updated via the shipping process.  */  
   "OurJobShippedQty":number,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.

When an OrderRel record is 'voided' any outstanding inventory allocations are relieved, OrderRel.OpenRelease is set to "no" and records are created/updated in the OrdJobMsg file for all the related  open OrderRel records if the OrderDtl that was tied to a Job to indicate that the line item was voided.  */  
   "VoidRelease":boolean,
      /**  Quantity, using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   "OurStockQty":number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   "WarehouseCode":string,
      /**  Actual quantity, using our U/M, shipped from Stock.  Updated via the shipping process.  */  
   "OurStockShippedQty":number,
      /**  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  */  
   "PartNum":string,
      /**  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  */  
   "RevisionNum":string,
      /**  Indicates if this customer/shipto  is exempt from sales tax for this line item. If field is non-blank it is considered exempt. Defaults from the Customer/Shipto file.  This code is totally user definable and no validation is required. This field will be printed on the Tax report if this item is reportable .  */  
   "TaxExempt":string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Enter via a DDSL fill-in for contact name. Use OrderHed.ShpConNum when the OrderRel.ShipToNum = OrderHed.ShipToNum else use ShipTo.PrimScon as a default.  */  
   "ShpConNum":number,
      /**  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  */  
   "NeedByDate":string,
      /**  EDI Reference  */  
   "Reference":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   "SellingReqQty":number,
      /**  The planned production quantity, using selling U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   "SellingJobQty":number,
      /**  Actual quantity, using selling U/M, shipped from the Job.  Updated via the shipping process.  */  
   "SellingJobShippedQty":number,
      /**  Quantity, using selling U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   "SellingStockQty":number,
      /**  Actual quantity, using selling U/M, shipped from Stock.  Updated via the shipping process.  */  
   "SellingStockShippedQty":number,
      /**  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   "SelectForPicking":boolean,
      /**  The shipping "Staging" warehouse for the release.  Defaults from the system default shipping area (Site.DefShippingWhse). This is maintainable in the Sales Allocation program.  */  
   "StagingWarehouseCode":string,
      /**  The shipping "Staging" bin for the release.  Defaults from the system default shipping area (Site.DefShippingBin). This is maintainable in the Sales Allocation program.  */  
   "StagingBinNum":string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   "PickError":string,
      /**  Quantity from last EDI update.  */  
   "CumeQty":number,
      /**  Date of last update  */  
   "CumeDate":string,
      /**  Indicates if this order release is linked to an inter-company PO release.  */  
   "Linked":boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   "ICPONum":number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "ICPOLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "ICPORelNum":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  A link to the demand schedule that created/updated this OrderRel.  */  
   "ScheduleNumber":string,
      /**  The Mark For to be used for this order release record. This MUST BE VALID IN THE SHIPTO file.  */  
   "MarkForNum":string,
      /**  Full name for the drop shipment.  */  
   "DropShipName":string,
      /**  RAN Number.  Used for informational purposes.  Supplied by EDI.  */  
   "RAN":string,
      /**  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  */  
   "DemandReference":string,
      /**  Indicates if the demand schedule that created/updated this order release has been rejected.  */  
   "DemandSchedRejected":boolean,
      /**  The last date that the Material Queue Report was run for this release.  This field will be null until the Material Queue Report is run.  */  
   "DatePickTicketPrinted":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Verbal Confirmation required  */  
   "VerbalConf":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Is a Service Saturday delivery acceptable  */  
   "ServSatDelivery":boolean,
      /**  Is a Service Saturday pickup available  */  
   "ServSatPickup":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Auto POD flag  */  
   "ServPOD":boolean,
      /**  AOD  */  
   "ServAOD":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   "OverrideCarrier":boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   "OverrideService":boolean,
      /**  The dockingstation of the shipto address.  For future use.  */  
   "DockingStation":string,
      /**  The location within the customer shipto address.  For future use.  */  
   "Location":string,
      /**  The code of the transport routing/time. For future use.  */  
   "TransportID":string,
      /**  Ship the good by this time.  */  
   "ShipbyTime":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  If true, the OrderRelTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   "TaxConnectCalc":boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the release before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   "GetDfltTaxIds":boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   "TaxRegionCode":string,
      /**  Indicates that the One Time ShipTO information defined for this release should be used.  */  
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
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipment country  */  
   "OTSCountryNum":number,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  */  
   "SubShipTo":string,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  */  
   "ShipRouting":string,
      /**  This field identifies Buy To Order releases.  */  
   "BuyToOrder":boolean,
      /**  The value for this field will be defaulted from the Supplier defined in the Part Site sub tab at the Part form. Used only for Buy To Order releases.  */  
   "VendorNum":number,
      /**  Supplier Purchase Point. Used only for Buy To Order releases.  */  
   "PurPoint":string,
      /**  This field identifies Drop Ship releases. Used only for Buy To Order releases.  */  
   "DropShip":boolean,
      /**  Purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   "PONum":number,
      /**  The line number of the purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   "POLine":number,
      /**  The release number of the purchase order line related to this Buy To Order release. Used only for Buy To Order releases.  */  
   "PORelNum":number,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   "OpenOrder":boolean,
      /**  Indicates if/how the OTS can be saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   "OTSSaveAs":string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   "OTSSaveCustID":string,
      /**  True if Customer or ShipTo record was created using the OTS info.  */  
   "OTSCustSaved":boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**   Unit of Measure that qualifies the "our" quantity fields.
If a valid part then it is the Base Stocking UOM (Part.IUM).
A mirror image of OrderDtl.IUM. Not directly maintainable  */  
   "IUM":string,
      /**   Selling Unit of measure. Qualifies the "Selling" quantity fields.
A mirror image of OrderDtl.SalesUM. Not directly maintainable.  */  
   "SalesUM":string,
      /**  Status of Order Release  */  
   "RelStatus":string,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  Previous Selling Quantity  */  
   "PrevSellQty":number,
      /**  Previous Part Number  */  
   "PrevPartNum":string,
      /**  Previous Customer Part Number  */  
   "PrevXPartNum":string,
      /**  Previous Need By Date  */  
   "PrevNeedByDate":string,
      /**  Previous Require Date  */  
   "PrevReqDate":string,
      /**  Previous Ship To Num  */  
   "PrevShipToNum":string,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   "MFCustNum":number,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   "UseOTMF":boolean,
      /**  One Time Mark For Name of the ShipTo.  */  
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
      /**  ECCPlant  */  
   "ECCPlant":string,
      /**  WIOrderLine  */  
   "WIOrderLine":string,
      /**  WIOrder  */  
   "WIOrder":string,
      /**  WebSKU  */  
   "WebSKU":string,
      /**  ShipOvers  */  
   "ShipOvers":boolean,
      /**  WIItemPrice  */  
   "WIItemPrice":number,
      /**  WIItemShipCost  */  
   "WIItemShipCost":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  EntityUseCode  */  
   "EntityUseCode":string,
      /**  PhaseID  */  
   "PhaseID":string,
      /**  OTSShipToNum  */  
   "OTSShipToNum":string,
      /**  WasRecInvoiced  */  
   "WasRecInvoiced":boolean,
      /**  The identifier of the planning contract.  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   "LinkToContract":boolean,
      /**  This flag indicates if the sales order release is ready to be fulfilled.  */  
   "ReadyToFulfill":boolean,
      /**  One Time ShipTo email address.  */  
   "OTSEMailAddress":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Unit of measure for the NumberOfPieces.  */  
   "NumberOfPiecesUOM":string,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  Indicates if the release should be added or removed from the fulfillment queue.  */  
   "PartAllocQueueAction":string,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
   "AvailableQuantity":number,
      /**  BuyOverride  */  
   "BuyOverride":boolean,
      /**  The message returned when checking a customer credit limit.  */  
   "CreditLimitMessage":string,
      /**  The source that put the customer on credit hold.  */  
   "CreditLimitSource":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  Is OTS allowed by the Sold to Customer?  */  
   "CustAllowOTS":boolean,
      /**  True when Customer allows shipping to a Third-Party  */  
   "CustomerAllowShipTo3":boolean,
   "CustomerCustID":string,
   "CustomerName":string,
   "DisablePlantWhse":boolean,
   "DocSelfAssessTax":number,
   "DocTotalTax":number,
   "DocWithholdTax":number,
      /**  DropShipOverride  */  
   "DropShipOverride":boolean,
      /**   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
'CP' = Cost Plus
The default is Customer Shipment.  */  
   "DspInvMeth":string,
      /**  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  */  
   "DspRevMethod":string,
   "EnableBuyToOrder":boolean,
   "EnableMake":boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   "EntryProcess":string,
      /**  ExistPOSugg, external field to show/hide an epishape  */  
   "ExistPOSugg":boolean,
   "HdrOTS":boolean,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
      /**  Inventory UOM that the Order Release is allocated against. It is the similare column to the OrderDtl InvtyUOM and should always has the same value as in OrderDtl  */  
   "InvtyUOM":string,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   "KitDisable":boolean,
      /**  LinkToPONum, external field to show/hide an epishape  */  
   "LinkToPONum":boolean,
   "MakeOverride":boolean,
      /**  The formatted mark for address  */  
   "MarkForAddrFormatted":string,
      /**  Contains the Mark For Address  */  
   "MarkForAddrList":string,
   "MFCustID":string,
      /**  The flag based on the user anwer if Ship To of the release is supposed be changed but Tax info is not changed because of the conflict in tax pricing  */  
   "NoRelTaxRgnChange":boolean,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   "NotCompliant":boolean,
   "OnHandQuantity":number,
   "OTSSaved":boolean,
      /**  OTS Tax Liability Code (Order Release)  */  
   "OTSTaxRegionCode":string,
   "PartExists":boolean,
      /**  If the phase has been recognized or invoiced.  */  
   "PhaseWasRecInvoiced":boolean,
   "ProjectID":string,
   "ReleaseStatus":string,
      /**  the flag to indicate if all previously creaded manually added and manual tax relcords related to Order line release should be deleted if the user populates Tax Exempt field.  */  
   "RemoveManAdTax":boolean,
   "Rpt1SelfAssessTax":number,
   "Rpt1TotalTax":number,
   "Rpt1WithholdTax":number,
   "Rpt2SelfAssessTax":number,
   "Rpt2TotalTax":number,
   "Rpt2WithholdTax":number,
   "Rpt3SelfAssessTax":number,
   "Rpt3TotalTax":number,
   "Rpt3WithholdTax":number,
      /**  SalesOrderLinked  */  
   "SalesOrderLinked":boolean,
      /**  Self-Assessed Tax  */  
   "SelfAssessTax":number,
      /**  Selling Factor for display only  */  
   "SellingFactor":number,
      /**  Selling Factor Direction for display oly  */  
   "SellingFactorDirection":string,
      /**  The formatted ship to address  */  
   "ShipToAddressFormatted":string,
   "ShipToAddressList":string,
   "ShipToContactEMailAddress":string,
   "ShipToContactName":string,
   "ShipToSelected":boolean,
   "SNEnable":boolean,
   "ThisRelInvtyQty":number,
   "TotalJobStockShipped":number,
      /**  Invoice Tax  */  
   "TotalTax":number,
   "UpdateMarkForRecords":boolean,
   "VoidOrder":boolean,
      /**  Withholding Tax  */  
   "WithholdTax":number,
   "AllowTaxCodeUpd":boolean,
      /**  Allow enable/disable for the button Attibutes in Order Release  */  
   "EnableDynAttrButton":boolean,
      /**  Attribute class is MRP Planned but AttributeSetID has not been set on release.  */  
   "AttributeMismatch":boolean,
      /**  The total allocated quantity for this release.  */  
   "AllocatedQuantity":number,
      /**  Error Status Display  */  
   "ErrorStatusDisplay":string,
      /**  True if this release is in the fulfillment queue.  */  
   "InPartAllocQueue":boolean,
      /**  Show Fulfillment Queue Actions  */  
   "ShowAllocationQueueActions":boolean,
   "BitFlag":number,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "MarkForNumInactive":boolean,
   "MFCustNumInactive":boolean,
   "OrderLineLineDesc":string,
   "OrderNumCurrencyCode":string,
   "OrderNumCardMemberName":string,
   "OTMFCountryDescription":string,
   "OTSCntryISOCode":string,
   "OTSCntryEUMember":boolean,
   "OTSCntryDescription":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumAttrClassID":string,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackLots":boolean,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PlantName":string,
   "PurPointAddress3":string,
   "PurPointZip":string,
   "PurPointName":string,
   "PurPointCountry":string,
   "PurPointAddress1":string,
   "PurPointState":string,
   "PurPointCity":string,
   "PurPointAddress2":string,
   "PurPointPrimPCon":number,
   "ShipToNumInactive":boolean,
   "ShipViaCodeWebDesc":string,
   "ShipViaCodeDescription":string,
   "TaxRegionCodeDescription":string,
   "TPShipToName":string,
   "TPShipToBTName":string,
   "TPShipToCustID":string,
   "VendorNumState":string,
   "VendorNumZIP":string,
   "VendorNumName":string,
   "VendorNumAddress2":string,
   "VendorNumCountry":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCity":string,
   "VendorNumAddress3":string,
   "VendorNumVendorID":string,
   "VendorNumDefaultFOB":string,
   "VendorNumTermsCode":string,
   "VendorNumAddress1":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "JobNum_c":string,
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
      @param orderNum
      @param orderLine
      @param orderRelNum
   */  
export interface DeleteByID_input{
   orderNum:number,
   orderLine:number,
   orderRelNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_OrderRelListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   OrderRelNum:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   ReqDate:string,
      /**  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   OurReqQty:number,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  */  
   ShipViaCode:string,
      /**  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   OpenRelease:boolean,
      /**  Indicates if this release is  "FIRM". The opposite is an uncommitted release, that is when the customer gives releases that are just 'Best Guesses' of what they will require in the future, such as in blanket order situations. This type of  releases is no different to the system, except that the FirmRelease field will be printed on reports such as TimePhase requirements.  */  
   FirmRelease:boolean,
      /**   Indicates if this requirement or any part of it will be manufactured. Default the setting to "No" if valid Part and the Part.Type is "S" or "P".

Default the setting to "Yes" if the part is not found in Part master or the Part.Type = "J".  This flag also gets set if this release gets linked to a Job via Job Entry. There is an Index on this field so that we can display releases that need have a job assigned to them. This display is part of Job Entry.  */  
   Make:boolean,
      /**  The planned production quantity, using Our U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   OurJobQty:number,
      /**  Actual quantity, using our U/M, shipped from the Job.  Updated via the shipping process.  */  
   OurJobShippedQty:number,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.

When an OrderRel record is 'voided' any outstanding inventory allocations are relieved, OrderRel.OpenRelease is set to "no" and records are created/updated in the OrdJobMsg file for all the related  open OrderRel records if the OrderDtl that was tied to a Job to indicate that the line item was voided.  */  
   VoidRelease:boolean,
      /**  Quantity, using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   WarehouseCode:string,
      /**  Actual quantity, using our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  */  
   PartNum:string,
      /**  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  */  
   RevisionNum:string,
      /**  Indicates if this customer/shipto  is exempt from sales tax for this line item. If field is non-blank it is considered exempt. Defaults from the Customer/Shipto file.  This code is totally user definable and no validation is required. This field will be printed on the Tax report if this item is reportable .  */  
   TaxExempt:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Enter via a DDSL fill-in for contact name. Use OrderHed.ShpConNum when the OrderRel.ShipToNum = OrderHed.ShipToNum else use ShipTo.PrimScon as a default.  */  
   ShpConNum:number,
      /**  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  */  
   NeedByDate:string,
      /**  EDI Reference  */  
   Reference:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   SellingReqQty:number,
      /**  The planned production quantity, using selling U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   SellingJobQty:number,
      /**  Actual quantity, using selling U/M, shipped from the Job.  Updated via the shipping process.  */  
   SellingJobShippedQty:number,
      /**  Quantity, using selling U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   SellingStockQty:number,
      /**  Actual quantity, using selling U/M, shipped from Stock.  Updated via the shipping process.  */  
   SellingStockShippedQty:number,
      /**  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The shipping "Staging" warehouse for the release.  Defaults from the system default shipping area (Site.DefShippingWhse). This is maintainable in the Sales Allocation program.  */  
   StagingWarehouseCode:string,
      /**  The shipping "Staging" bin for the release.  Defaults from the system default shipping area (Site.DefShippingBin). This is maintainable in the Sales Allocation program.  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**  Quantity from last EDI update.  */  
   CumeQty:number,
      /**  Date of last update  */  
   CumeDate:string,
      /**  Indicates if this order release is linked to an inter-company PO release.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   ICPORelNum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  A link to the demand schedule that created/updated this OrderRel.  */  
   ScheduleNumber:string,
      /**  The Mark For to be used for this order release record. This MUST BE VALID IN THE SHIPTO file.  */  
   MarkForNum:string,
      /**  Full name for the drop shipment.  */  
   DropShipName:string,
      /**  RAN Number.  Used for informational purposes.  Supplied by EDI.  */  
   RAN:string,
      /**  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  */  
   DemandReference:string,
      /**  Indicates if the demand schedule that created/updated this order release has been rejected.  */  
   DemandSchedRejected:boolean,
      /**  The last date that the Material Queue Report was run for this release.  This field will be null until the Material Queue Report is run.  */  
   DatePickTicketPrinted:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Verbal Confirmation required  */  
   VerbalConf:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Is a Service Saturday delivery acceptable  */  
   ServSatDelivery:boolean,
      /**  Is a Service Saturday pickup available  */  
   ServSatPickup:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Auto POD flag  */  
   ServPOD:boolean,
      /**  AOD  */  
   ServAOD:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   OverrideService:boolean,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  The location within the customer shipto address.  For future use.  */  
   Location:string,
      /**  The code of the transport routing/time. For future use.  */  
   TransportID:string,
      /**  Ship the good by this time.  */  
   ShipbyTime:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  If true, the OrderRelTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the release before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  Indicates that the One Time ShipTO information defined for this release should be used.  */  
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
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipment country  */  
   OTSCountryNum:number,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  */  
   SubShipTo:string,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  */  
   ShipRouting:string,
      /**  This field identifies Buy To Order releases.  */  
   BuyToOrder:boolean,
      /**  The value for this field will be defaulted from the Supplier defined in the Part Site sub tab at the Part form. Used only for Buy To Order releases.  */  
   VendorNum:number,
      /**  Supplier Purchase Point. Used only for Buy To Order releases.  */  
   PurPoint:string,
      /**  This field identifies Drop Ship releases. Used only for Buy To Order releases.  */  
   DropShip:boolean,
      /**  Purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   PONum:number,
      /**  The line number of the purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   POLine:number,
      /**  The release number of the purchase order line related to this Buy To Order release. Used only for Buy To Order releases.  */  
   PORelNum:number,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**  Indicates if/how the OTS can be saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  True if Customer or ShipTo record was created using the OTS info.  */  
   OTSCustSaved:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**   Unit of Measure that qualifies the "our" quantity fields.
If a valid part then it is the Base Stocking UOM (Part.IUM).
A mirror image of OrderDtl.IUM. Not directly maintainable  */  
   IUM:string,
      /**   Selling Unit of measure. Qualifies the "Selling" quantity fields.
A mirror image of OrderDtl.SalesUM. Not directly maintainable.  */  
   SalesUM:string,
      /**  Status of Order Release  */  
   RelStatus:string,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Previous Selling Quantity  */  
   PrevSellQty:number,
      /**  Previous Part Number  */  
   PrevPartNum:string,
      /**  Previous Customer Part Number  */  
   PrevXPartNum:string,
      /**  Previous Need By Date  */  
   PrevNeedByDate:string,
      /**  Previous Require Date  */  
   PrevReqDate:string,
      /**  Previous Ship To Num  */  
   PrevShipToNum:string,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   UseOTMF:boolean,
      /**  One Time Mark For Name of the ShipTo.  */  
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  OTSShipToNum  */  
   OTSShipToNum:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   OnHandQuantity:number,
   AvailableQuantity:number,
   ShipToAddressList:string,
   ShipToContactName:string,
   MakeOverride:boolean,
   EnableMake:boolean,
   PartExists:boolean,
   ReleaseStatus:string,
   CustomerCustID:string,
   CustomerName:string,
   VoidOrder:boolean,
      /**  The message returned when checking a customer credit limit.  */  
   CreditLimitMessage:string,
      /**  The source that put the customer on credit hold.  */  
   CreditLimitSource:string,
      /**  Selling Factor for display only  */  
   SellingFactor:number,
      /**  Selling Factor Direction for display oly  */  
   SellingFactorDirection:string,
   ShipToContactEMailAddress:string,
   AllowTaxCodeUpd:boolean,
      /**  Invoice Tax  */  
   TotalTax:number,
   DocTotalTax:number,
   TotalJobStockShipped:number,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   SNEnable:boolean,
      /**  ExistPOSugg, external field to show/hide an epishape  */  
   ExistPOSugg:boolean,
      /**  LinkToPONum, external field to show/hide an epishape  */  
   LinkToPONum:boolean,
      /**  Self-Assessed Tax  */  
   SelfAssessTax:number,
      /**  Withholding Tax  */  
   WithholdTax:number,
   DocWithholdTax:number,
   DocSelfAssessTax:number,
   HdrOTS:boolean,
   Rpt1TotalTax:number,
   Rpt2TotalTax:number,
   Rpt3TotalTax:number,
   Rpt1WithholdTax:number,
   Rpt2WithholdTax:number,
   Rpt3WithholdTax:number,
   Rpt1SelfAssessTax:number,
   Rpt2SelfAssessTax:number,
   Rpt3SelfAssessTax:number,
      /**  BuyOverride  */  
   BuyOverride:boolean,
      /**  DropShipOverride  */  
   DropShipOverride:boolean,
   ThisRelInvtyQty:number,
      /**  SalesOrderLinked  */  
   SalesOrderLinked:boolean,
   OTSSaved:boolean,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   NotCompliant:boolean,
      /**  Is OTS allowed by the Sold to Customer?  */  
   CustAllowOTS:boolean,
      /**  True when Customer allows shipping to a Third-Party  */  
   CustomerAllowShipTo3:boolean,
      /**  OTS Tax Liability Code (Order Release)  */  
   OTSTaxRegionCode:string,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   EntryProcess:string,
   MFCustID:string,
      /**  Contains the Mark For Address  */  
   MarkForAddrList:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   OrderLineLineDesc:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  Country name  */  
   OTMFCountryDescription:string,
      /**  Country name  */  
   OTSCntryDescription:string,
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
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Second address line  */  
   PurPointAddress2:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   PurPointCountry:string,
      /**  State portion of the address  */  
   PurPointState:string,
      /**  Third address line  */  
   PurPointAddress3:string,
      /**  Purchase Point Name...can't be blank.  */  
   PurPointName:string,
      /**  Postal Code or Zip code portion of the address  */  
   PurPointZip:string,
      /**  First address line  */  
   PurPointAddress1:string,
      /**  City portion of the address  */  
   PurPointCity:string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   PurPointPrimPCon:number,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  Full description for the Tax Region.  */  
   TaxRegionCodeDescription:string,
      /**  The full name of the customer.  */  
   TPShipToName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   TPShipToBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   TPShipToCustID:string,
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
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderRelListTableset{
   OrderRelList:Erp_Tablesets_OrderRelListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_OrderRelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   OrderRelNum:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   ReqDate:string,
      /**  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   OurReqQty:number,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  */  
   ShipViaCode:string,
      /**  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   OpenRelease:boolean,
      /**  Indicates if this release is  "FIRM". The opposite is an uncommitted release, that is when the customer gives releases that are just 'Best Guesses' of what they will require in the future, such as in blanket order situations. This type of  releases is no different to the system, except that the FirmRelease field will be printed on reports such as TimePhase requirements.  */  
   FirmRelease:boolean,
      /**   Indicates if this requirement or any part of it will be manufactured. Default the setting to "No" if valid Part and the Part.Type is "S" or "P".

Default the setting to "Yes" if the part is not found in Part master or the Part.Type = "J".  This flag also gets set if this release gets linked to a Job via Job Entry. There is an Index on this field so that we can display releases that need have a job assigned to them. This display is part of Job Entry.  */  
   Make:boolean,
      /**  The planned production quantity, using Our U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   OurJobQty:number,
      /**  Actual quantity, using our U/M, shipped from the Job.  Updated via the shipping process.  */  
   OurJobShippedQty:number,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.

When an OrderRel record is 'voided' any outstanding inventory allocations are relieved, OrderRel.OpenRelease is set to "no" and records are created/updated in the OrdJobMsg file for all the related  open OrderRel records if the OrderDtl that was tied to a Job to indicate that the line item was voided.  */  
   VoidRelease:boolean,
      /**  Quantity, using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   WarehouseCode:string,
      /**  Actual quantity, using our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  */  
   PartNum:string,
      /**  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  */  
   RevisionNum:string,
      /**  Indicates if this customer/shipto  is exempt from sales tax for this line item. If field is non-blank it is considered exempt. Defaults from the Customer/Shipto file.  This code is totally user definable and no validation is required. This field will be printed on the Tax report if this item is reportable .  */  
   TaxExempt:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Enter via a DDSL fill-in for contact name. Use OrderHed.ShpConNum when the OrderRel.ShipToNum = OrderHed.ShipToNum else use ShipTo.PrimScon as a default.  */  
   ShpConNum:number,
      /**  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  */  
   NeedByDate:string,
      /**  EDI Reference  */  
   Reference:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   SellingReqQty:number,
      /**  The planned production quantity, using selling U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   SellingJobQty:number,
      /**  Actual quantity, using selling U/M, shipped from the Job.  Updated via the shipping process.  */  
   SellingJobShippedQty:number,
      /**  Quantity, using selling U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   SellingStockQty:number,
      /**  Actual quantity, using selling U/M, shipped from Stock.  Updated via the shipping process.  */  
   SellingStockShippedQty:number,
      /**  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The shipping "Staging" warehouse for the release.  Defaults from the system default shipping area (Site.DefShippingWhse). This is maintainable in the Sales Allocation program.  */  
   StagingWarehouseCode:string,
      /**  The shipping "Staging" bin for the release.  Defaults from the system default shipping area (Site.DefShippingBin). This is maintainable in the Sales Allocation program.  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**  Quantity from last EDI update.  */  
   CumeQty:number,
      /**  Date of last update  */  
   CumeDate:string,
      /**  Indicates if this order release is linked to an inter-company PO release.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   ICPORelNum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  A link to the demand schedule that created/updated this OrderRel.  */  
   ScheduleNumber:string,
      /**  The Mark For to be used for this order release record. This MUST BE VALID IN THE SHIPTO file.  */  
   MarkForNum:string,
      /**  Full name for the drop shipment.  */  
   DropShipName:string,
      /**  RAN Number.  Used for informational purposes.  Supplied by EDI.  */  
   RAN:string,
      /**  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  */  
   DemandReference:string,
      /**  Indicates if the demand schedule that created/updated this order release has been rejected.  */  
   DemandSchedRejected:boolean,
      /**  The last date that the Material Queue Report was run for this release.  This field will be null until the Material Queue Report is run.  */  
   DatePickTicketPrinted:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Verbal Confirmation required  */  
   VerbalConf:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Is a Service Saturday delivery acceptable  */  
   ServSatDelivery:boolean,
      /**  Is a Service Saturday pickup available  */  
   ServSatPickup:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Auto POD flag  */  
   ServPOD:boolean,
      /**  AOD  */  
   ServAOD:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   OverrideService:boolean,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  The location within the customer shipto address.  For future use.  */  
   Location:string,
      /**  The code of the transport routing/time. For future use.  */  
   TransportID:string,
      /**  Ship the good by this time.  */  
   ShipbyTime:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  If true, the OrderRelTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the release before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  Indicates that the One Time ShipTO information defined for this release should be used.  */  
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
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipment country  */  
   OTSCountryNum:number,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  */  
   SubShipTo:string,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  */  
   ShipRouting:string,
      /**  This field identifies Buy To Order releases.  */  
   BuyToOrder:boolean,
      /**  The value for this field will be defaulted from the Supplier defined in the Part Site sub tab at the Part form. Used only for Buy To Order releases.  */  
   VendorNum:number,
      /**  Supplier Purchase Point. Used only for Buy To Order releases.  */  
   PurPoint:string,
      /**  This field identifies Drop Ship releases. Used only for Buy To Order releases.  */  
   DropShip:boolean,
      /**  Purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   PONum:number,
      /**  The line number of the purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   POLine:number,
      /**  The release number of the purchase order line related to this Buy To Order release. Used only for Buy To Order releases.  */  
   PORelNum:number,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**  Indicates if/how the OTS can be saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  True if Customer or ShipTo record was created using the OTS info.  */  
   OTSCustSaved:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**   Unit of Measure that qualifies the "our" quantity fields.
If a valid part then it is the Base Stocking UOM (Part.IUM).
A mirror image of OrderDtl.IUM. Not directly maintainable  */  
   IUM:string,
      /**   Selling Unit of measure. Qualifies the "Selling" quantity fields.
A mirror image of OrderDtl.SalesUM. Not directly maintainable.  */  
   SalesUM:string,
      /**  Status of Order Release  */  
   RelStatus:string,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Previous Selling Quantity  */  
   PrevSellQty:number,
      /**  Previous Part Number  */  
   PrevPartNum:string,
      /**  Previous Customer Part Number  */  
   PrevXPartNum:string,
      /**  Previous Need By Date  */  
   PrevNeedByDate:string,
      /**  Previous Require Date  */  
   PrevReqDate:string,
      /**  Previous Ship To Num  */  
   PrevShipToNum:string,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   UseOTMF:boolean,
      /**  One Time Mark For Name of the ShipTo.  */  
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
      /**  ECCPlant  */  
   ECCPlant:string,
      /**  WIOrderLine  */  
   WIOrderLine:string,
      /**  WIOrder  */  
   WIOrder:string,
      /**  WebSKU  */  
   WebSKU:string,
      /**  ShipOvers  */  
   ShipOvers:boolean,
      /**  WIItemPrice  */  
   WIItemPrice:number,
      /**  WIItemShipCost  */  
   WIItemShipCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  PhaseID  */  
   PhaseID:string,
      /**  OTSShipToNum  */  
   OTSShipToNum:string,
      /**  WasRecInvoiced  */  
   WasRecInvoiced:boolean,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  This flag indicates if the sales order release is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  One Time ShipTo email address.  */  
   OTSEMailAddress:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Unit of measure for the NumberOfPieces.  */  
   NumberOfPiecesUOM:string,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Indicates if the release should be added or removed from the fulfillment queue.  */  
   PartAllocQueueAction:string,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
   AvailableQuantity:number,
      /**  BuyOverride  */  
   BuyOverride:boolean,
      /**  The message returned when checking a customer credit limit.  */  
   CreditLimitMessage:string,
      /**  The source that put the customer on credit hold.  */  
   CreditLimitSource:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Is OTS allowed by the Sold to Customer?  */  
   CustAllowOTS:boolean,
      /**  True when Customer allows shipping to a Third-Party  */  
   CustomerAllowShipTo3:boolean,
   CustomerCustID:string,
   CustomerName:string,
   DisablePlantWhse:boolean,
   DocSelfAssessTax:number,
   DocTotalTax:number,
   DocWithholdTax:number,
      /**  DropShipOverride  */  
   DropShipOverride:boolean,
      /**   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
'CP' = Cost Plus
The default is Customer Shipment.  */  
   DspInvMeth:string,
      /**  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  */  
   DspRevMethod:string,
   EnableBuyToOrder:boolean,
   EnableMake:boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   EntryProcess:string,
      /**  ExistPOSugg, external field to show/hide an epishape  */  
   ExistPOSugg:boolean,
   HdrOTS:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Inventory UOM that the Order Release is allocated against. It is the similare column to the OrderDtl InvtyUOM and should always has the same value as in OrderDtl  */  
   InvtyUOM:string,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   KitDisable:boolean,
      /**  LinkToPONum, external field to show/hide an epishape  */  
   LinkToPONum:boolean,
   MakeOverride:boolean,
      /**  The formatted mark for address  */  
   MarkForAddrFormatted:string,
      /**  Contains the Mark For Address  */  
   MarkForAddrList:string,
   MFCustID:string,
      /**  The flag based on the user anwer if Ship To of the release is supposed be changed but Tax info is not changed because of the conflict in tax pricing  */  
   NoRelTaxRgnChange:boolean,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   NotCompliant:boolean,
   OnHandQuantity:number,
   OTSSaved:boolean,
      /**  OTS Tax Liability Code (Order Release)  */  
   OTSTaxRegionCode:string,
   PartExists:boolean,
      /**  If the phase has been recognized or invoiced.  */  
   PhaseWasRecInvoiced:boolean,
   ProjectID:string,
   ReleaseStatus:string,
      /**  the flag to indicate if all previously creaded manually added and manual tax relcords related to Order line release should be deleted if the user populates Tax Exempt field.  */  
   RemoveManAdTax:boolean,
   Rpt1SelfAssessTax:number,
   Rpt1TotalTax:number,
   Rpt1WithholdTax:number,
   Rpt2SelfAssessTax:number,
   Rpt2TotalTax:number,
   Rpt2WithholdTax:number,
   Rpt3SelfAssessTax:number,
   Rpt3TotalTax:number,
   Rpt3WithholdTax:number,
      /**  SalesOrderLinked  */  
   SalesOrderLinked:boolean,
      /**  Self-Assessed Tax  */  
   SelfAssessTax:number,
      /**  Selling Factor for display only  */  
   SellingFactor:number,
      /**  Selling Factor Direction for display oly  */  
   SellingFactorDirection:string,
      /**  The formatted ship to address  */  
   ShipToAddressFormatted:string,
   ShipToAddressList:string,
   ShipToContactEMailAddress:string,
   ShipToContactName:string,
   ShipToSelected:boolean,
   SNEnable:boolean,
   ThisRelInvtyQty:number,
   TotalJobStockShipped:number,
      /**  Invoice Tax  */  
   TotalTax:number,
   UpdateMarkForRecords:boolean,
   VoidOrder:boolean,
      /**  Withholding Tax  */  
   WithholdTax:number,
   AllowTaxCodeUpd:boolean,
      /**  Allow enable/disable for the button Attibutes in Order Release  */  
   EnableDynAttrButton:boolean,
      /**  Attribute class is MRP Planned but AttributeSetID has not been set on release.  */  
   AttributeMismatch:boolean,
      /**  The total allocated quantity for this release.  */  
   AllocatedQuantity:number,
      /**  Error Status Display  */  
   ErrorStatusDisplay:string,
      /**  True if this release is in the fulfillment queue.  */  
   InPartAllocQueue:boolean,
      /**  Show Fulfillment Queue Actions  */  
   ShowAllocationQueueActions:boolean,
   BitFlag:number,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   MarkForNumInactive:boolean,
   MFCustNumInactive:boolean,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   OTMFCountryDescription:string,
   OTSCntryISOCode:string,
   OTSCntryEUMember:boolean,
   OTSCntryDescription:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PlantName:string,
   PurPointAddress3:string,
   PurPointZip:string,
   PurPointName:string,
   PurPointCountry:string,
   PurPointAddress1:string,
   PurPointState:string,
   PurPointCity:string,
   PurPointAddress2:string,
   PurPointPrimPCon:number,
   ShipToNumInactive:boolean,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   TaxRegionCodeDescription:string,
   TPShipToName:string,
   TPShipToBTName:string,
   TPShipToCustID:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VendorNumName:string,
   VendorNumAddress2:string,
   VendorNumCountry:string,
   VendorNumCurrencyCode:string,
   VendorNumCity:string,
   VendorNumAddress3:string,
   VendorNumVendorID:string,
   VendorNumDefaultFOB:string,
   VendorNumTermsCode:string,
   VendorNumAddress1:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   JobNum_c:string,
}

export interface Erp_Tablesets_OrderRelSearchTableset{
   OrderRel:Erp_Tablesets_OrderRelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtOrderRelSearchTableset{
   OrderRel:Erp_Tablesets_OrderRelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param orderNum
      @param orderLine
      @param orderRelNum
   */  
export interface GetByID_input{
   orderNum:number,
   orderLine:number,
   orderRelNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_OrderRelSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_OrderRelSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_OrderRelSearchTableset[],
}

   /** Required : 
      @param whereClause
      @param custNum
      @param pageSize
      @param absolutePage
   */  
export interface GetListByCustNum_input{
      /**  The criteria  */  
   whereClause:string,
      /**  Filter by this CustNum  */  
   custNum:number,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetListByCustNum_output{
   returnObj:Erp_Tablesets_OrderRelListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param showShippedComplete
      @param pageSize
      @param absolutePage
   */  
export interface GetListFilterShipped_input{
      /**  The criteria  */  
   whereClause:string,
      /**  False = OrderRel that are open but have been flagged shipped complete on any pack will not be shown; True = show open OrderRel that have been flagged as shipped complete on any pack  */  
   showShippedComplete:boolean,
      /**  Size of a page  */  
   pageSize:number,
      /**  The absolute page  */  
   absolutePage:number,
}

export interface GetListFilterShipped_output{
   returnObj:Erp_Tablesets_OrderRelListTableset[],
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
   returnObj:Erp_Tablesets_OrderRelListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param orderNum
      @param orderLine
   */  
export interface GetNewOrderRel_input{
   ds:Erp_Tablesets_OrderRelSearchTableset[],
   orderNum:number,
   orderLine:number,
}

export interface GetNewOrderRel_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderRelSearchTableset,
}
}

   /** Required : 
      @param whereClauseOrderRel
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseOrderRel:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_OrderRelSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtOrderRelSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtOrderRelSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_OrderRelSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderRelSearchTableset,
}
}

