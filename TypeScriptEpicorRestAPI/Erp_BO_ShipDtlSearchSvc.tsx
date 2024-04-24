import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ShipDtlSearchSvc
// Description: Packing Slip Line Search Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/$metadata", {
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
   Description: Get ShipDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipDtlSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlRow
   */  
export function get_ShipDtlSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/ShipDtlSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipDtlSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/ShipDtlSearches", {
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
   Summary: Calls GetByID to retrieve the ShipDtlSearch item
   Description: Calls GetByID to retrieve the ShipDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   */  
export function get_ShipDtlSearches_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ShipDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/ShipDtlSearches(" + Company + "," + PackNum + "," + PackLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ShipDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ShipDtlSearch for the service
   Description: Calls UpdateExt to update ShipDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ShipDtlSearches_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/ShipDtlSearches(" + Company + "," + PackNum + "," + PackLine + ")", {
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
   Summary: Call UpdateExt to delete ShipDtlSearch item
   Description: Call UpdateExt to delete ShipDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipDtlSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param PackLine Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ShipDtlSearches_Company_PackNum_PackLine(Company:string, PackNum:string, PackLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/ShipDtlSearches(" + Company + "," + PackNum + "," + PackLine + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlListRow)
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
export function get_GetRows(whereClauseShipDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseShipDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseShipDtl=" + whereClauseShipDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/GetRows" + params, {
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
export function get_GetByID(packNum:string, packLine:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof packNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packNum=" + packNum
   }
   if(typeof packLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packLine=" + packLine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetListCase
   Description: Calls the normal GetList method and then constructs a custom data set combining Hed/Dtl fields for the case entry.
   OperationID: GetListCase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListCase(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/GetListCase", {
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
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the contact tracker.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/GetRowsContactTracker", {
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
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/GetRowsCustomerTracker", {
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
   Summary: Invoke method GetNewShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewShipDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/GetNewShipDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipDtlListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ShipDtlRow[],
}

export interface Erp_Tablesets_ShipDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   "PackLine":number,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  */  
   "OrderNum":number,
      /**  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  */  
   "OrderLine":number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   "OrderRelNum":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  */  
   "OurInventoryShipQty":number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  */  
   "OurJobShipQty":number,
      /**  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  */  
   "JobNum":string,
      /**  Number of Packages  */  
   "Packages":number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  */  
   "PartNum":string,
      /**  Line Description  */  
   "LineDesc":string,
      /**  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  */  
   "IUM":string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   "RevisionNum":string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   "ShipComment":string,
      /**  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  */  
   "ShipCmpl":boolean,
      /**   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   "BinNum":string,
      /**  Indicates if this transaction affected inventory at time of creation.  */  
   "UpdatedInventory":boolean,
      /**   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  */  
   "XRevisionNum":string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  */  
   "ShpConNum":number,
      /**  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  */  
   "TMBilling":boolean,
      /**  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  */  
   "Invoiced":boolean,
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  */  
   "WUM":string,
      /**  Lot Number is for Inventory Shipments.  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  These comments will be copied into the Invoice detail.  */  
   "InvoiceComment":string,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  */  
   "CustNum":number,
      /**  The shipto number. Used for warranty validation.  */  
   "ShipToNum":string,
      /**  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  */  
   "EffectiveDate":string,
      /**  The # of days, months, years the material is covered by warranty  */  
   "MaterialDuration":number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   "LaborDuration":number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   "MiscDuration":number,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   "MaterialMod":string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   "LaborMod":string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   "MiscMod":string,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MaterialExpiration":string,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "LaborExpiration":string,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MiscExpiration":string,
      /**  The latest of the 3 warranty expiration dates  */  
   "LastExpiration":string,
      /**  Editor widget for Warranty comments.  */  
   "WarrantyComment":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  This warranty covers On site visits  */  
   "Onsite":boolean,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  */  
   "Plant":string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  */  
   "ReadyToInvoice":boolean,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  */  
   "SellingInventoryShipQty":number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  */  
   "SellingJobShipQty":number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  */  
   "SalesUM":string,
      /**  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  */  
   "TotalNetWeight":number,
      /**   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  */  
   "WIPWarehouseCode":string,
      /**   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  */  
   "WIPBinNum":string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   "HeaderShipComment":string,
      /**  The packline of the kit parent  */  
   "KitParentLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  */  
   "InventoryShipUOM":string,
      /**  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  */  
   "JobShipUOM":string,
      /**  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  */  
   "TrackSerialNum":boolean,
      /**  Lot Number is for Job Shipments.  */  
   "JobLotNum":string,
      /**  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  */  
   "BinType":string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   "NotCompliant":boolean,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  Unit price discount percent.  */  
   "DiscountPercent":number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  A flat discount amount for the line item.  It can be zero.  */  
   "Discount":number,
      /**  A flat discount amount for the line item.  */  
   "DocDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Extended Price for the invoice line item.  */  
   "ExtPrice":number,
      /**  Extended Price for the invoice line item.  */  
   "DocExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPrice":number,
      /**  Unit Price.  */  
   "UnitPrice":number,
      /**  Unit Price.  */  
   "DocUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  */  
   "PickedAutoAllocatedQty":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  A flat discount amount for the line item includes taxes.  It can be zero.  */  
   "InDiscount":number,
      /**  A flat discount amount for the line item includes taxes.  */  
   "DocInDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InDiscount":number,
      /**  Extended Price for the invoice line item including taxes.  */  
   "InExtPrice":number,
      /**  Extended Price for the invoice line item including taxes.  */  
   "DocInExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InExtPrice":number,
      /**  Unit Price including taxes.  */  
   "InUnitPrice":number,
      /**  Unit Price including taxes.  */  
   "DocInUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InUnitPrice":number,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   "MFCustNum":number,
      /**  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  */  
   "MFShipToNum":string,
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
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OurJobShipIUM":string,
   "RequestDate":string,
   "OurReqQty":number,
   "OurReqUM":string,
   "OurShippedQty":number,
   "OurShippedUM":string,
   "OurRemainQty":number,
   "OurRemainUM":string,
   "SellingReqQty":number,
   "SellingReqUM":string,
   "SellingShippedQty":number,
   "SellingShippedUM":string,
   "SellingRemainQty":number,
   "SellingRemainUM":string,
   "SellingShipmentQty":number,
   "SellingShipmentUM":string,
      /**  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  */  
   "DisplayInvQty":number,
      /**  Indicates if a detail line has errors to be corrected before leaving packing slip  */  
   "DtlError":boolean,
      /**  Indicates if Part is a stock Part  */  
   "StockPart":boolean,
   "WhseList":string,
      /**  Delimited list of available Dimension codes for line  */  
   "DimCodeList":string,
      /**  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  */  
   "InvoiceNum":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  */  
   "LegalNumber":string,
      /**  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  */  
   "ShipDate":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  */  
   "ShipViaCode":string,
      /**  The invoice legal number.  */  
   "InvLegalNumber":string,
   "OurStockShippedQty":number,
   "OurJobShippedQty":number,
   "OrderRelOurReqQty":number,
   "PartCompany":string,
   "PartPartNum":string,
      /**  Sales Kit flag.  C = 'Component'  P = 'Parent'.  */  
   "KitFlag":string,
   "KitCompIssue":boolean,
   "KitBackFlush":boolean,
   "KitCompShipComplete":boolean,
   "ExtJobNum":string,
   "LinkMsg":string,
   "PONum":string,
   "KitQtyFromInvEnabled":boolean,
   "KitParentIssue":boolean,
   "KitPartNum":string,
   "KitBinNum":string,
   "KitDescription":string,
   "KitIUM":string,
   "KitLotNum":string,
   "KitQtyFromInv":number,
   "KitSerialTracked":boolean,
   "KitTrackLots":boolean,
   "KitWarehouse":string,
   "KitWarehouseCodeDesc":string,
   "KitWhseList":string,
      /**  Used by freight web service  */  
   "PartAESExp":string,
      /**  Used by freight web service  */  
   "PartECNNumber":string,
      /**  Used by freight web service  */  
   "PartExpLicNumber":string,
      /**  Used by freight web service  */  
   "PartExpLicType":string,
      /**  Used by freight web service  */  
   "PartHazClass":string,
      /**  Used by freight web service  */  
   "PartHazGvrnmtID":string,
      /**  Used by freight web service  */  
   "PartHazItem":boolean,
      /**  Used by freight web service  */  
   "PartHazPackInstr":string,
      /**  Used by freight web service  */  
   "PartHazSub":string,
      /**  Used by freight web service  */  
   "PartHazTechName":string,
      /**  Used by freight web service  */  
   "PartHTS":string,
      /**  Used by freight web service  */  
   "PartNAFTAOrigCountry":string,
      /**  Used by freight web service  */  
   "PartNAFTAPref":string,
      /**  Used by freight web service  */  
   "PartNAFTAProd":string,
      /**  Used by freight web service  */  
   "PartOrigCountry":string,
      /**  Used by freight web service  */  
   "PartSchedBcode":string,
      /**  Used by freight web service  */  
   "PartUseHTSDesc":boolean,
   "KitMassIssue":boolean,
      /**  Individual line content value that is used by the freight web service to calculate the total order value.  */  
   "LineContentValue":number,
      /**  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  */  
   "EnableJobFields":boolean,
      /**  Indicates if Order is on Hold  */  
   "OrderHold":boolean,
   "EnableInvSerialBtn":boolean,
   "EnableMfgSerialBtn":boolean,
   "EnablePOSerialBtn":boolean,
   "LineTax":number,
   "DocLineTax":number,
   "CurrencyCode":string,
   "Rpt1LineTax":number,
   "Rpt2LineTax":number,
   "Rpt3LineTax":number,
      /**  Flag to indicate if Order/Line/Rel is Buy To Order  */  
   "BuyToOrder":boolean,
      /**  Is Drop Shipment.  */  
   "DropShip":boolean,
      /**  Packing slip for drop shipment.  */  
   "PackSlip":string,
      /**  Project of the related Order Line  */  
   "ProjectID":string,
   "MFCustID":string,
      /**  Contains the Mark For Address  */  
   "MarkForAddrList":string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   "BinNumDescription":string,
      /**  Description of the service contract.  */  
   "ContractCodeContractDescription":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  Description for the dimension code.  */  
   "DimensionDimCodeDescription":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Optional lot number description.  */  
   "LotPartLotDescription":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "OrderLineLineDesc":string,
      /**  The member's name on the credit card.  */  
   "OrderNumCardMemberName":string,
      /**  A unique code that identifies the currency.  */  
   "OrderNumCurrencyCode":string,
      /**  Country name  */  
   "OTMFCountryDescription":string,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "PackNumShipStatus":string,
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
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  Description of the warranty.  */  
   "WarrantyCodeWarrDescription":string,
      /**  Description.  */  
   "WIPWarehouseCodeDescription":string,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   "VendorNum":number,
      /**  The supplier purchase point ID.  */  
   "PurPoint":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "KitAttributeSetID":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ShipDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Packing slip number that this detail record is linked with.  */  
   "PackNum":number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   "PackLine":number,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  */  
   "OrderNum":number,
      /**  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  */  
   "OrderLine":number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   "OrderRelNum":number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   "LineType":string,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  */  
   "OurInventoryShipQty":number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  */  
   "OurJobShipQty":number,
      /**  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  */  
   "JobNum":string,
      /**  Number of Packages  */  
   "Packages":number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  */  
   "PartNum":string,
      /**  Line Description  */  
   "LineDesc":string,
      /**  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  */  
   "IUM":string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   "RevisionNum":string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   "ShipComment":string,
      /**  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  */  
   "ShipCmpl":boolean,
      /**   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   "BinNum":string,
      /**  Indicates if this transaction affected inventory at time of creation.  */  
   "UpdatedInventory":boolean,
      /**   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  */  
   "XRevisionNum":string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  */  
   "ShpConNum":number,
      /**  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  */  
   "TMBilling":boolean,
      /**  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  */  
   "Invoiced":boolean,
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  */  
   "WUM":string,
      /**  Lot Number is for Inventory Shipments.  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  These comments will be copied into the Invoice detail.  */  
   "InvoiceComment":string,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   "WarrantyCode":string,
      /**  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  */  
   "CustNum":number,
      /**  The shipto number. Used for warranty validation.  */  
   "ShipToNum":string,
      /**  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  */  
   "EffectiveDate":string,
      /**  The # of days, months, years the material is covered by warranty  */  
   "MaterialDuration":number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   "LaborDuration":number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   "MiscDuration":number,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   "MaterialMod":string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   "LaborMod":string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   "MiscMod":string,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MaterialExpiration":string,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "LaborExpiration":string,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   "MiscExpiration":string,
      /**  The latest of the 3 warranty expiration dates  */  
   "LastExpiration":string,
      /**  Editor widget for Warranty comments.  */  
   "WarrantyComment":string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   "ContractNum":number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   "ContractCode":string,
      /**  This warranty covers On site visits  */  
   "Onsite":boolean,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  */  
   "Plant":string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  */  
   "ReadyToInvoice":boolean,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  */  
   "SellingInventoryShipQty":number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  */  
   "SellingJobShipQty":number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  */  
   "SalesUM":string,
      /**  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  */  
   "TotalNetWeight":number,
      /**   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  */  
   "WIPWarehouseCode":string,
      /**   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  */  
   "WIPBinNum":string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   "HeaderShipComment":string,
      /**  The packline of the kit parent  */  
   "KitParentLine":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  */  
   "InventoryShipUOM":string,
      /**  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  */  
   "JobShipUOM":string,
      /**  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  */  
   "TrackSerialNum":boolean,
      /**  Lot Number is for Job Shipments.  */  
   "JobLotNum":string,
      /**  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  */  
   "BinType":string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   "NotCompliant":boolean,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  Unit price discount percent.  */  
   "DiscountPercent":number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "PricePerCode":string,
      /**  A flat discount amount for the line item.  It can be zero.  */  
   "Discount":number,
      /**  A flat discount amount for the line item.  */  
   "DocDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2Discount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3Discount":number,
      /**  Extended Price for the invoice line item.  */  
   "ExtPrice":number,
      /**  Extended Price for the invoice line item.  */  
   "DocExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ExtPrice":number,
      /**  Unit Price.  */  
   "UnitPrice":number,
      /**  Unit Price.  */  
   "DocUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  */  
   "PickedAutoAllocatedQty":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  A flat discount amount for the line item includes taxes.  It can be zero.  */  
   "InDiscount":number,
      /**  A flat discount amount for the line item includes taxes.  */  
   "DocInDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InDiscount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InDiscount":number,
      /**  Extended Price for the invoice line item including taxes.  */  
   "InExtPrice":number,
      /**  Extended Price for the invoice line item including taxes.  */  
   "DocInExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InExtPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InExtPrice":number,
      /**  Unit Price including taxes.  */  
   "InUnitPrice":number,
      /**  Unit Price including taxes.  */  
   "DocInUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InUnitPrice":number,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   "MFCustNum":number,
      /**  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  */  
   "MFShipToNum":string,
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
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   "RenewalNbr":number,
      /**  ShipOvers  */  
   "ShipOvers":boolean,
      /**  AllowedOvers  */  
   "AllowedOvers":number,
      /**  AllowedUnders  */  
   "AllowedUnders":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This is the quantity being shipped that was not already previously allocated, and could not be auto allocated.  */  
   "NotAllocatedQty":number,
      /**  PCID  */  
   "PCID":string,
      /**  PCID Item Sequence  */  
   "PCIDItemSeq":number,
      /**  The dockingstation of the shipto address.  For future use.  */  
   "DockingStation":string,
      /**  For future use.  */  
   "UseShipDtlInfo":boolean,
      /**  PkgCodePartNum  */  
   "PkgCodePartNum":string,
      /**  CustContainerPartNum  */  
   "CustContainerPartNum":string,
      /**  LabelType  */  
   "LabelType":string,
      /**  Indicates that the warranty will be sent to FSA  */  
   "WarrantySendToFSA":boolean,
      /**  When the shipment line is marked as "send as equipment", it will create an Installation in Epicor FSA.  */  
   "FSAEquipment":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set based on OurInventoryShipQty.  */  
   "InventoryNumberOfPieces":number,
      /**  Number of pieces for this attribute set based on OurJobShipQty.  */  
   "JobNumberOfPieces":number,
      /**  Estimated Value  */  
   "MXEstValue":number,
      /**  Estimated Value Currency  */  
   "MXEstValueCurrencyCode":string,
      /**  Hazardous Shipment  */  
   "MXHazardousShipment":boolean,
      /**  Hazardous Type  */  
   "MXHazardousType":string,
      /**  Package Type  */  
   "MXPackageType":string,
      /**  CNDeclarationBillLine  */  
   "CNDeclarationBillLine":number,
      /**  This is the quantity being shipped from manufacturing that was not already previously allocated, and could not be auto allocated.  */  
   "JobNotAllocatedQty":number,
      /**  Quantity picked from manufacturing that was not manually allocated.  */  
   "JobPickedAutoAllocatedQty":number,
      /**  Flag to indicate if Order/Line/Rel is Buy To Order  */  
   "BuyToOrder":boolean,
      /**  The date and time that the record was last changed  */  
   "ChangeDateTime":string,
   "CurrencyCode":string,
      /**  Delimited list of available Dimension codes for line  */  
   "DimCodeList":string,
      /**  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  */  
   "DisplayInvQty":number,
   "DocLineTax":number,
      /**  Is Drop Shipment.  */  
   "DropShip":boolean,
      /**  Indicates if a detail line has errors to be corrected before leaving packing slip  */  
   "DtlError":boolean,
   "EnableInvIDBtn":boolean,
   "EnableInvSerialBtn":boolean,
      /**  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  */  
   "EnableJobFields":boolean,
   "EnableKitIDBtn":boolean,
   "EnableMfgIDBtn":boolean,
   "EnableMfgSerialBtn":boolean,
   "EnableOBInvSerialBtn":boolean,
   "EnableOBMfgSerialBtn":boolean,
      /**  Boolean indicating if the package control functionality should be enabled.  */  
   "EnablePackageControl":boolean,
   "EnablePOSerialBtn":boolean,
   "ExtJobNum":string,
   "FSAInstallationCost":number,
   "FSAInstallationOrderLine":number,
   "FSAInstallationOrderNum":number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   "FSAInstallationRequired":boolean,
   "FSAInstallationType":string,
      /**  Equal to true if opening Location ID Diaglog  */  
   "GetLocIDNum":boolean,
      /**  The invoice legal number.  */  
   "InvLegalNumber":string,
      /**  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  */  
   "InvoiceNum":number,
   "KitBackFlush":boolean,
   "KitBinNum":string,
   "KitCompIssue":boolean,
   "KitCompShipComplete":boolean,
   "KitDescription":string,
      /**  Sales Kit flag.  C = 'Component'  P = 'Parent'.  */  
   "KitFlag":string,
   "KitIUM":string,
   "KitLotNum":string,
   "KitMassIssue":boolean,
   "KitParentIssue":boolean,
   "KitPartNum":string,
   "KitQtyFromInv":number,
   "KitQtyFromInvEnabled":boolean,
   "KitSerialTracked":boolean,
   "KitTrackLots":boolean,
   "KitWarehouse":string,
   "KitWarehouseCodeDesc":string,
   "KitWhseList":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  */  
   "LegalNumber":string,
      /**  Individual line content value that is used by the freight web service to calculate the total order value.  */  
   "LineContentValue":number,
   "LineTax":number,
   "LinkMsg":string,
      /**  Contains the Mark For Address  */  
   "MarkForAddrList":string,
   "MFCustID":string,
      /**  Indicates if Order is on Hold  */  
   "OrderHold":boolean,
   "OrderRelOurReqQty":number,
   "OurJobShipIUM":string,
   "OurJobShippedQty":number,
   "OurRemainQty":number,
   "OurRemainUM":string,
   "OurReqQty":number,
   "OurReqUM":string,
   "OurShippedQty":number,
   "OurShippedUM":string,
   "OurStockShippedQty":number,
      /**  Packing slip for drop shipment.  */  
   "PackSlip":string,
      /**  Used by freight web service  */  
   "PartAESExp":string,
   "PartCompany":string,
      /**  Used by freight web service  */  
   "PartECNNumber":string,
      /**  Used by freight web service  */  
   "PartExpLicNumber":string,
      /**  Used by freight web service  */  
   "PartExpLicType":string,
      /**  Used by freight web service  */  
   "PartHazClass":string,
      /**  Used by freight web service  */  
   "PartHazGvrnmtID":string,
      /**  Used by freight web service  */  
   "PartHazItem":boolean,
      /**  Used by freight web service  */  
   "PartHazPackInstr":string,
      /**  Used by freight web service  */  
   "PartHazSub":string,
      /**  Used by freight web service  */  
   "PartHazTechName":string,
      /**  Used by freight web service  */  
   "PartHTS":string,
      /**  Used by freight web service  */  
   "PartNAFTAOrigCountry":string,
      /**  Used by freight web service  */  
   "PartNAFTAPref":string,
      /**  Used by freight web service  */  
   "PartNAFTAProd":string,
      /**  Used by freight web service  */  
   "PartOrigCountry":string,
   "PartPartNum":string,
      /**  Used by freight web service  */  
   "PartSchedBcode":string,
      /**  Used by freight web service  */  
   "PartUseHTSDesc":boolean,
   "PONum":string,
      /**  Project of the related Order Line  */  
   "ProjectID":string,
      /**  The supplier purchase point ID.  */  
   "PurPoint":string,
   "RequestDate":string,
   "Rpt1LineTax":number,
   "Rpt2LineTax":number,
   "Rpt3LineTax":number,
   "SelectedLocationIDQty":number,
   "SellingRemainQty":number,
   "SellingRemainUM":string,
   "SellingReqQty":number,
   "SellingReqUM":string,
   "SellingShipmentQty":number,
   "SellingShipmentUM":string,
   "SellingShippedQty":number,
   "SellingShippedUM":string,
      /**  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  */  
   "ShipDate":string,
   "ShipToWarning":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  */  
   "ShipViaCode":string,
      /**  Indicates if Part is a stock Part  */  
   "StockPart":boolean,
   "TrackID":boolean,
   "TranLocationIDQty":number,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   "VendorNum":number,
   "WhseList":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "KitAttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  The Full Description of the Attribute Set.  */  
   "KitAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "KitAttributeSetShortDescription":string,
   "KitPartAttrClassID":string,
   "EnableAttributeSetSearch":boolean,
      /**  Mark For address formatted for kinetic.  */  
   "MarkForAddrFormatted":string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispInventoryNumberOfPieces":number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispJobNumberOfPieces":number,
   "KitRevisionNum":string,
   "CNDeclarationBill":string,
   "BitFlag":number,
   "BinNumDescription":string,
   "ContractCodeContractDescription":string,
   "CustNumSendToFSA":boolean,
   "CustNumName":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "DimensionDimCodeDescription":string,
   "JobNumPartDescription":string,
   "LotPartLotDescription":string,
   "MFShipToNumInactive":boolean,
   "OrderLineProdCode":string,
   "OrderLineLineDesc":string,
   "OrderNumPSCurrCode":string,
   "OrderNumCardMemberName":string,
   "OrderNumCurrencyCode":string,
   "OTMFCountryDescription":string,
   "PackNumUseOTS":boolean,
   "PackNumShipStatus":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumAttrClassID":string,
   "PartNumSendToFSA":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumWarrantyCode":string,
   "PartNumFSAEquipment":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PlantName":string,
   "WarehouseCodeDescription":string,
   "WarrantyCodeSendToFSA":boolean,
   "WarrantyCodeWarrDescription":string,
   "WIPWarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "PCID2_c":string,
   "PCID3_c":string,
   "PCID4_c":string,
   "PCID5_c":string,
   "PCIDType1_c":string,
   "PCIDType2_c":string,
   "PCIDType3_c":string,
   "PCIDType4_c":string,
   "PCIDType5_c":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param packNum
      @param packLine
   */  
export interface DeleteByID_input{
   packNum:number,
   packLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ShipDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  */  
   OrderLine:number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   OrderRelNum:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  */  
   OurInventoryShipQty:number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  */  
   OurJobShipQty:number,
      /**  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  */  
   JobNum:string,
      /**  Number of Packages  */  
   Packages:number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  */  
   PartNum:string,
      /**  Line Description  */  
   LineDesc:string,
      /**  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  */  
   IUM:string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   RevisionNum:string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   ShipComment:string,
      /**  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  */  
   ShipCmpl:boolean,
      /**   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   BinNum:string,
      /**  Indicates if this transaction affected inventory at time of creation.  */  
   UpdatedInventory:boolean,
      /**   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  */  
   XRevisionNum:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  */  
   ShpConNum:number,
      /**  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  */  
   TMBilling:boolean,
      /**  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  */  
   Invoiced:boolean,
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  */  
   WUM:string,
      /**  Lot Number is for Inventory Shipments.  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  These comments will be copied into the Invoice detail.  */  
   InvoiceComment:string,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  */  
   CustNum:number,
      /**  The shipto number. Used for warranty validation.  */  
   ShipToNum:string,
      /**  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  */  
   EffectiveDate:string,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   MaterialMod:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   MiscMod:string,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MaterialExpiration:string,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   LaborExpiration:string,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MiscExpiration:string,
      /**  The latest of the 3 warranty expiration dates  */  
   LastExpiration:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  */  
   Plant:string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  */  
   ReadyToInvoice:boolean,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  */  
   SellingInventoryShipQty:number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  */  
   SellingJobShipQty:number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  */  
   SalesUM:string,
      /**  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  */  
   TotalNetWeight:number,
      /**   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  */  
   WIPWarehouseCode:string,
      /**   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  */  
   WIPBinNum:string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   HeaderShipComment:string,
      /**  The packline of the kit parent  */  
   KitParentLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  */  
   InventoryShipUOM:string,
      /**  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  */  
   JobShipUOM:string,
      /**  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  */  
   TrackSerialNum:boolean,
      /**  Lot Number is for Job Shipments.  */  
   JobLotNum:string,
      /**  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  */  
   BinType:string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   NotCompliant:boolean,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Unit price discount percent.  */  
   DiscountPercent:number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  A flat discount amount for the line item.  It can be zero.  */  
   Discount:number,
      /**  A flat discount amount for the line item.  */  
   DocDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Extended Price for the invoice line item.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  */  
   DocExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPrice:number,
      /**  Unit Price.  */  
   UnitPrice:number,
      /**  Unit Price.  */  
   DocUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  */  
   PickedAutoAllocatedQty:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  A flat discount amount for the line item includes taxes.  It can be zero.  */  
   InDiscount:number,
      /**  A flat discount amount for the line item includes taxes.  */  
   DocInDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt2InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt3InDiscount:number,
      /**  Extended Price for the invoice line item including taxes.  */  
   InExtPrice:number,
      /**  Extended Price for the invoice line item including taxes.  */  
   DocInExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPrice:number,
      /**  Unit Price including taxes.  */  
   InUnitPrice:number,
      /**  Unit Price including taxes.  */  
   DocInUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InUnitPrice:number,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  */  
   MFShipToNum:string,
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
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OurJobShipIUM:string,
   RequestDate:string,
   OurReqQty:number,
   OurReqUM:string,
   OurShippedQty:number,
   OurShippedUM:string,
   OurRemainQty:number,
   OurRemainUM:string,
   SellingReqQty:number,
   SellingReqUM:string,
   SellingShippedQty:number,
   SellingShippedUM:string,
   SellingRemainQty:number,
   SellingRemainUM:string,
   SellingShipmentQty:number,
   SellingShipmentUM:string,
      /**  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  */  
   DisplayInvQty:number,
      /**  Indicates if a detail line has errors to be corrected before leaving packing slip  */  
   DtlError:boolean,
      /**  Indicates if Part is a stock Part  */  
   StockPart:boolean,
   WhseList:string,
      /**  Delimited list of available Dimension codes for line  */  
   DimCodeList:string,
      /**  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  */  
   InvoiceNum:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  */  
   LegalNumber:string,
      /**  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  */  
   ShipViaCode:string,
      /**  The invoice legal number.  */  
   InvLegalNumber:string,
   OurStockShippedQty:number,
   OurJobShippedQty:number,
   OrderRelOurReqQty:number,
   PartCompany:string,
   PartPartNum:string,
      /**  Sales Kit flag.  C = 'Component'  P = 'Parent'.  */  
   KitFlag:string,
   KitCompIssue:boolean,
   KitBackFlush:boolean,
   KitCompShipComplete:boolean,
   ExtJobNum:string,
   LinkMsg:string,
   PONum:string,
   KitQtyFromInvEnabled:boolean,
   KitParentIssue:boolean,
   KitPartNum:string,
   KitBinNum:string,
   KitDescription:string,
   KitIUM:string,
   KitLotNum:string,
   KitQtyFromInv:number,
   KitSerialTracked:boolean,
   KitTrackLots:boolean,
   KitWarehouse:string,
   KitWarehouseCodeDesc:string,
   KitWhseList:string,
      /**  Used by freight web service  */  
   PartAESExp:string,
      /**  Used by freight web service  */  
   PartECNNumber:string,
      /**  Used by freight web service  */  
   PartExpLicNumber:string,
      /**  Used by freight web service  */  
   PartExpLicType:string,
      /**  Used by freight web service  */  
   PartHazClass:string,
      /**  Used by freight web service  */  
   PartHazGvrnmtID:string,
      /**  Used by freight web service  */  
   PartHazItem:boolean,
      /**  Used by freight web service  */  
   PartHazPackInstr:string,
      /**  Used by freight web service  */  
   PartHazSub:string,
      /**  Used by freight web service  */  
   PartHazTechName:string,
      /**  Used by freight web service  */  
   PartHTS:string,
      /**  Used by freight web service  */  
   PartNAFTAOrigCountry:string,
      /**  Used by freight web service  */  
   PartNAFTAPref:string,
      /**  Used by freight web service  */  
   PartNAFTAProd:string,
      /**  Used by freight web service  */  
   PartOrigCountry:string,
      /**  Used by freight web service  */  
   PartSchedBcode:string,
      /**  Used by freight web service  */  
   PartUseHTSDesc:boolean,
   KitMassIssue:boolean,
      /**  Individual line content value that is used by the freight web service to calculate the total order value.  */  
   LineContentValue:number,
      /**  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  */  
   EnableJobFields:boolean,
      /**  Indicates if Order is on Hold  */  
   OrderHold:boolean,
   EnableInvSerialBtn:boolean,
   EnableMfgSerialBtn:boolean,
   EnablePOSerialBtn:boolean,
   LineTax:number,
   DocLineTax:number,
   CurrencyCode:string,
   Rpt1LineTax:number,
   Rpt2LineTax:number,
   Rpt3LineTax:number,
      /**  Flag to indicate if Order/Line/Rel is Buy To Order  */  
   BuyToOrder:boolean,
      /**  Is Drop Shipment.  */  
   DropShip:boolean,
      /**  Packing slip for drop shipment.  */  
   PackSlip:string,
      /**  Project of the related Order Line  */  
   ProjectID:string,
   MFCustID:string,
      /**  Contains the Mark For Address  */  
   MarkForAddrList:string,
      /**  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  */  
   BinNumDescription:string,
      /**  Description of the service contract.  */  
   ContractCodeContractDescription:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  Description for the dimension code.  */  
   DimensionDimCodeDescription:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Optional lot number description.  */  
   LotPartLotDescription:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   OrderLineLineDesc:string,
      /**  The member's name on the credit card.  */  
   OrderNumCardMemberName:string,
      /**  A unique code that identifies the currency.  */  
   OrderNumCurrencyCode:string,
      /**  Country name  */  
   OTMFCountryDescription:string,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   PackNumShipStatus:string,
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
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  Description of the warranty.  */  
   WarrantyCodeWarrDescription:string,
      /**  Description.  */  
   WIPWarehouseCodeDescription:string,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   VendorNum:number,
      /**  The supplier purchase point ID.  */  
   PurPoint:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   KitAttributeSetID:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ShipDtlListTableset{
   ShipDtlList:Erp_Tablesets_ShipDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ShipDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Packing slip number that this detail record is linked with.  */  
   PackNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  */  
   OrderLine:number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   OrderRelNum:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  */  
   OurInventoryShipQty:number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  */  
   OurJobShipQty:number,
      /**  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  */  
   JobNum:string,
      /**  Number of Packages  */  
   Packages:number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  */  
   PartNum:string,
      /**  Line Description  */  
   LineDesc:string,
      /**  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  */  
   IUM:string,
      /**  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  */  
   RevisionNum:string,
      /**   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  */  
   ShipComment:string,
      /**  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  */  
   ShipCmpl:boolean,
      /**   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  */  
   BinNum:string,
      /**  Indicates if this transaction affected inventory at time of creation.  */  
   UpdatedInventory:boolean,
      /**   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  */  
   XRevisionNum:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  */  
   ShpConNum:number,
      /**  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  */  
   TMBilling:boolean,
      /**  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  */  
   Invoiced:boolean,
      /**  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  */  
   WUM:string,
      /**  Lot Number is for Inventory Shipments.  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  These comments will be copied into the Invoice detail.  */  
   InvoiceComment:string,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  */  
   CustNum:number,
      /**  The shipto number. Used for warranty validation.  */  
   ShipToNum:string,
      /**  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  */  
   EffectiveDate:string,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  Whether the duration of warranty  is for "Days", " Months", "years".  */  
   MaterialMod:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  Whether the duration of warranty  is for "Days"," Months"," years".  */  
   MiscMod:string,
      /**  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MaterialExpiration:string,
      /**  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   LaborExpiration:string,
      /**  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  */  
   MiscExpiration:string,
      /**  The latest of the 3 warranty expiration dates  */  
   LastExpiration:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  */  
   Plant:string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  */  
   ReadyToInvoice:boolean,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  */  
   SellingInventoryShipQty:number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  */  
   SellingJobShipQty:number,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  */  
   SalesUM:string,
      /**  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  */  
   TotalNetWeight:number,
      /**   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  */  
   WIPWarehouseCode:string,
      /**   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  */  
   WIPBinNum:string,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Packing slip comments.  These are comments off of the invoice header.  */  
   HeaderShipComment:string,
      /**  The packline of the kit parent  */  
   KitParentLine:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  */  
   InventoryShipUOM:string,
      /**  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  */  
   JobShipUOM:string,
      /**  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  */  
   TrackSerialNum:boolean,
      /**  Lot Number is for Job Shipments.  */  
   JobLotNum:string,
      /**  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  */  
   BinType:string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   NotCompliant:boolean,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Unit price discount percent.  */  
   DiscountPercent:number,
      /**   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  A flat discount amount for the line item.  It can be zero.  */  
   Discount:number,
      /**  A flat discount amount for the line item.  */  
   DocDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Extended Price for the invoice line item.  */  
   ExtPrice:number,
      /**  Extended Price for the invoice line item.  */  
   DocExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPrice:number,
      /**  Unit Price.  */  
   UnitPrice:number,
      /**  Unit Price.  */  
   DocUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  */  
   PickedAutoAllocatedQty:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  A flat discount amount for the line item includes taxes.  It can be zero.  */  
   InDiscount:number,
      /**  A flat discount amount for the line item includes taxes.  */  
   DocInDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt1InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt2InDiscount:number,
      /**  Reporting currency value of this field  */  
   Rpt3InDiscount:number,
      /**  Extended Price for the invoice line item including taxes.  */  
   InExtPrice:number,
      /**  Extended Price for the invoice line item including taxes.  */  
   DocInExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPrice:number,
      /**  Unit Price including taxes.  */  
   InUnitPrice:number,
      /**  Unit Price including taxes.  */  
   DocInUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2InUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3InUnitPrice:number,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  */  
   MFShipToNum:string,
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
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
      /**  ShipOvers  */  
   ShipOvers:boolean,
      /**  AllowedOvers  */  
   AllowedOvers:number,
      /**  AllowedUnders  */  
   AllowedUnders:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This is the quantity being shipped that was not already previously allocated, and could not be auto allocated.  */  
   NotAllocatedQty:number,
      /**  PCID  */  
   PCID:string,
      /**  PCID Item Sequence  */  
   PCIDItemSeq:number,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  For future use.  */  
   UseShipDtlInfo:boolean,
      /**  PkgCodePartNum  */  
   PkgCodePartNum:string,
      /**  CustContainerPartNum  */  
   CustContainerPartNum:string,
      /**  LabelType  */  
   LabelType:string,
      /**  Indicates that the warranty will be sent to FSA  */  
   WarrantySendToFSA:boolean,
      /**  When the shipment line is marked as "send as equipment", it will create an Installation in Epicor FSA.  */  
   FSAEquipment:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set based on OurInventoryShipQty.  */  
   InventoryNumberOfPieces:number,
      /**  Number of pieces for this attribute set based on OurJobShipQty.  */  
   JobNumberOfPieces:number,
      /**  Estimated Value  */  
   MXEstValue:number,
      /**  Estimated Value Currency  */  
   MXEstValueCurrencyCode:string,
      /**  Hazardous Shipment  */  
   MXHazardousShipment:boolean,
      /**  Hazardous Type  */  
   MXHazardousType:string,
      /**  Package Type  */  
   MXPackageType:string,
      /**  CNDeclarationBillLine  */  
   CNDeclarationBillLine:number,
      /**  This is the quantity being shipped from manufacturing that was not already previously allocated, and could not be auto allocated.  */  
   JobNotAllocatedQty:number,
      /**  Quantity picked from manufacturing that was not manually allocated.  */  
   JobPickedAutoAllocatedQty:number,
      /**  Flag to indicate if Order/Line/Rel is Buy To Order  */  
   BuyToOrder:boolean,
      /**  The date and time that the record was last changed  */  
   ChangeDateTime:string,
   CurrencyCode:string,
      /**  Delimited list of available Dimension codes for line  */  
   DimCodeList:string,
      /**  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  */  
   DisplayInvQty:number,
   DocLineTax:number,
      /**  Is Drop Shipment.  */  
   DropShip:boolean,
      /**  Indicates if a detail line has errors to be corrected before leaving packing slip  */  
   DtlError:boolean,
   EnableInvIDBtn:boolean,
   EnableInvSerialBtn:boolean,
      /**  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  */  
   EnableJobFields:boolean,
   EnableKitIDBtn:boolean,
   EnableMfgIDBtn:boolean,
   EnableMfgSerialBtn:boolean,
   EnableOBInvSerialBtn:boolean,
   EnableOBMfgSerialBtn:boolean,
      /**  Boolean indicating if the package control functionality should be enabled.  */  
   EnablePackageControl:boolean,
   EnablePOSerialBtn:boolean,
   ExtJobNum:string,
   FSAInstallationCost:number,
   FSAInstallationOrderLine:number,
   FSAInstallationOrderNum:number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   FSAInstallationRequired:boolean,
   FSAInstallationType:string,
      /**  Equal to true if opening Location ID Diaglog  */  
   GetLocIDNum:boolean,
      /**  The invoice legal number.  */  
   InvLegalNumber:string,
      /**  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  */  
   InvoiceNum:number,
   KitBackFlush:boolean,
   KitBinNum:string,
   KitCompIssue:boolean,
   KitCompShipComplete:boolean,
   KitDescription:string,
      /**  Sales Kit flag.  C = 'Component'  P = 'Parent'.  */  
   KitFlag:string,
   KitIUM:string,
   KitLotNum:string,
   KitMassIssue:boolean,
   KitParentIssue:boolean,
   KitPartNum:string,
   KitQtyFromInv:number,
   KitQtyFromInvEnabled:boolean,
   KitSerialTracked:boolean,
   KitTrackLots:boolean,
   KitWarehouse:string,
   KitWarehouseCodeDesc:string,
   KitWhseList:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  */  
   LegalNumber:string,
      /**  Individual line content value that is used by the freight web service to calculate the total order value.  */  
   LineContentValue:number,
   LineTax:number,
   LinkMsg:string,
      /**  Contains the Mark For Address  */  
   MarkForAddrList:string,
   MFCustID:string,
      /**  Indicates if Order is on Hold  */  
   OrderHold:boolean,
   OrderRelOurReqQty:number,
   OurJobShipIUM:string,
   OurJobShippedQty:number,
   OurRemainQty:number,
   OurRemainUM:string,
   OurReqQty:number,
   OurReqUM:string,
   OurShippedQty:number,
   OurShippedUM:string,
   OurStockShippedQty:number,
      /**  Packing slip for drop shipment.  */  
   PackSlip:string,
      /**  Used by freight web service  */  
   PartAESExp:string,
   PartCompany:string,
      /**  Used by freight web service  */  
   PartECNNumber:string,
      /**  Used by freight web service  */  
   PartExpLicNumber:string,
      /**  Used by freight web service  */  
   PartExpLicType:string,
      /**  Used by freight web service  */  
   PartHazClass:string,
      /**  Used by freight web service  */  
   PartHazGvrnmtID:string,
      /**  Used by freight web service  */  
   PartHazItem:boolean,
      /**  Used by freight web service  */  
   PartHazPackInstr:string,
      /**  Used by freight web service  */  
   PartHazSub:string,
      /**  Used by freight web service  */  
   PartHazTechName:string,
      /**  Used by freight web service  */  
   PartHTS:string,
      /**  Used by freight web service  */  
   PartNAFTAOrigCountry:string,
      /**  Used by freight web service  */  
   PartNAFTAPref:string,
      /**  Used by freight web service  */  
   PartNAFTAProd:string,
      /**  Used by freight web service  */  
   PartOrigCountry:string,
   PartPartNum:string,
      /**  Used by freight web service  */  
   PartSchedBcode:string,
      /**  Used by freight web service  */  
   PartUseHTSDesc:boolean,
   PONum:string,
      /**  Project of the related Order Line  */  
   ProjectID:string,
      /**  The supplier purchase point ID.  */  
   PurPoint:string,
   RequestDate:string,
   Rpt1LineTax:number,
   Rpt2LineTax:number,
   Rpt3LineTax:number,
   SelectedLocationIDQty:number,
   SellingRemainQty:number,
   SellingRemainUM:string,
   SellingReqQty:number,
   SellingReqUM:string,
   SellingShipmentQty:number,
   SellingShipmentUM:string,
   SellingShippedQty:number,
   SellingShippedUM:string,
      /**  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  */  
   ShipDate:string,
   ShipToWarning:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  */  
   ShipViaCode:string,
      /**  Indicates if Part is a stock Part  */  
   StockPart:boolean,
   TrackID:boolean,
   TranLocationIDQty:number,
      /**  The supplier that drops shipped the good from their inventory to our customer.  */  
   VendorNum:number,
   WhseList:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   KitAttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set.  */  
   KitAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   KitAttributeSetShortDescription:string,
   KitPartAttrClassID:string,
   EnableAttributeSetSearch:boolean,
      /**  Mark For address formatted for kinetic.  */  
   MarkForAddrFormatted:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispInventoryNumberOfPieces:number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispJobNumberOfPieces:number,
   KitRevisionNum:string,
   CNDeclarationBill:string,
   BitFlag:number,
   BinNumDescription:string,
   ContractCodeContractDescription:string,
   CustNumSendToFSA:boolean,
   CustNumName:string,
   CustNumCustID:string,
   CustNumBTName:string,
   DimensionDimCodeDescription:string,
   JobNumPartDescription:string,
   LotPartLotDescription:string,
   MFShipToNumInactive:boolean,
   OrderLineProdCode:string,
   OrderLineLineDesc:string,
   OrderNumPSCurrCode:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   OTMFCountryDescription:string,
   PackNumUseOTS:boolean,
   PackNumShipStatus:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumSendToFSA:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumWarrantyCode:string,
   PartNumFSAEquipment:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PlantName:string,
   WarehouseCodeDescription:string,
   WarrantyCodeSendToFSA:boolean,
   WarrantyCodeWarrDescription:string,
   WIPWarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   PCID2_c:string,
   PCID3_c:string,
   PCID4_c:string,
   PCID5_c:string,
   PCIDType1_c:string,
   PCIDType2_c:string,
   PCIDType3_c:string,
   PCIDType4_c:string,
   PCIDType5_c:string,
}

export interface Erp_Tablesets_ShipDtlSearchTableset{
   ShipDtl:Erp_Tablesets_ShipDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtShipDtlSearchTableset{
   ShipDtl:Erp_Tablesets_ShipDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param packNum
      @param packLine
   */  
export interface GetByID_input{
   packNum:number,
   packLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ShipDtlSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ShipDtlSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ShipDtlSearchTableset[],
}

   /** Required : 
      @param whereClauseShipDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetListCase_input{
      /**  Whereclause for ShipDtl table.  */  
   whereClauseShipDtl:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListCase_output{
   returnObj:Erp_Tablesets_ShipDtlListTableset[],
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
   returnObj:Erp_Tablesets_ShipDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewShipDtl_input{
   ds:Erp_Tablesets_ShipDtlSearchTableset[],
   packNum:number,
}

export interface GetNewShipDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ShipDtlSearchTableset[],
}
}

   /** Required : 
      @param whereClauseShipDtl
      @param contactName
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsContactTracker_input{
      /**  Whereclause for ShipDtl table.  */  
   whereClauseShipDtl:string,
      /**  Contact to return data for.  */  
   contactName:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsContactTracker_output{
   returnObj:Erp_Tablesets_ShipDtlSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseShipDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustomerTracker_input{
      /**  Whereclause for ShipDtl table.  */  
   whereClauseShipDtl:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsCustomerTracker_output{
   returnObj:Erp_Tablesets_ShipDtlSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseShipDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseShipDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ShipDtlSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtShipDtlSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtShipDtlSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ShipDtlSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ShipDtlSearchTableset[],
}
}

