import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PODetailTrackerSearchSvc
// Description: PoDetail Tracker Search Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/$metadata", {
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
   Description: Get PODetailTrackerSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetailTrackerSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailRow
   */  
export function get_PODetailTrackerSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/PODetailTrackerSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetailTrackerSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PODetailTrackerSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/PODetailTrackerSearches", {
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
   Summary: Calls GetByID to retrieve the PODetailTrackerSearch item
   Description: Calls GetByID to retrieve the PODetailTrackerSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailTrackerSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailRow
   */  
export function get_PODetailTrackerSearches_Company_PONUM_POLine(Company:string, PONUM:string, POLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PODetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/PODetailTrackerSearches(" + Company + "," + PONUM + "," + POLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PODetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PODetailTrackerSearch for the service
   Description: Calls UpdateExt to update PODetailTrackerSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetailTrackerSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PODetailTrackerSearches_Company_PONUM_POLine(Company:string, PONUM:string, POLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/PODetailTrackerSearches(" + Company + "," + PONUM + "," + POLine + ")", {
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
   Summary: Call UpdateExt to delete PODetailTrackerSearch item
   Description: Call UpdateExt to delete PODetailTrackerSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetailTrackerSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PODetailTrackerSearches_Company_PONUM_POLine(Company:string, PONUM:string, POLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/PODetailTrackerSearches(" + Company + "," + PONUM + "," + POLine + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailListRow)
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
export function get_GetRows(whereClausePODetail:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePODetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePODetail=" + whereClausePODetail
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/GetRows" + params, {
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
export function get_GetByID(poNUM:string, poLine:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof poNUM!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "poNUM=" + poNUM
   }
   if(typeof poLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "poLine=" + poLine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetRowsByVendorNum
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the supplier tracker.
   OperationID: GetRowsByVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsByVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsByVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsByVendorNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/GetRowsByVendorNum", {
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
   Summary: Invoke method GetNewPODetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPODetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/GetNewPODetail", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PODetailListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PODetailRow[],
}

export interface Erp_Tablesets_PODetailListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  */  
   "OpenLine":boolean,
      /**   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  */  
   "VoidLine":boolean,
      /**  Purchase order number that the detail line item is linked to.  */  
   "PONUM":number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "POLine":number,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "LineDesc":string,
      /**  (Our) Unit Of Measure.  */  
   "IUM":string,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   "UnitCost":number,
      /**  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  */  
   "DocUnitCost":number,
      /**  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  */  
   "OrderQty":number,
      /**  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  */  
   "XOrderQty":number,
      /**  Taxable  */  
   "Taxable":boolean,
      /**  Purchasing UOM  */  
   "PUM":string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "CostPerCode":string,
      /**  OUR internal Part number for this item.  */  
   "PartNum":string,
      /**  Supplier Part Number  */  
   "VenPartNum":string,
      /**  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  */  
   "CommentText":string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  */  
   "ClassID":string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  */  
   "VendorNum":number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   "AdvancePayBal":number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   "DocAdvancePayBal":number,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   "Confirmed":boolean,
      /**  Indicates this line has a pending date change  */  
   "DateChgReq":boolean,
      /**  Indicates this line has a pending qty change  */  
   "QtyChgReq":boolean,
      /**  Requested pending partnumber change  */  
   "PartNumChgReq":string,
      /**  Requested pending revision change  */  
   "RevisionNumChgReq":string,
      /**  Date Supplier Confirmed the PO  */  
   "ConfirmDate":string,
      /**  Can be "web" or "client"  */  
   "ConfirmVia":string,
      /**  Requested Price change.  SRM  */  
   "PrcChgReq":number,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   "PurchCode":string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   "OrderNum":number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   "OrderLine":number,
      /**  Linked to sales order line.  */  
   "Linked":boolean,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Is this line active on the Contract Purchase Order?  */  
   "ContractActive":boolean,
      /**  Quantity for this Contract Purchase Order Line.  */  
   "ContractQty":number,
      /**  Unit Price for this Contract Purchase Order Line.  */  
   "ContractUnitCost":number,
      /**  Document Unit Price for this Contract Purchase Order Line.  */  
   "ContractDocUnitCost":number,
      /**  Advanced Payments Balance in Rpt1 currency.  */  
   "Rpt1AdvancePayBal":number,
      /**  Advanced Payments Balance in Rpt2 currency.  */  
   "Rpt2AdvancePayBal":number,
      /**  Advanced Payments Balance in Rpt3 currency.  */  
   "Rpt3AdvancePayBal":number,
      /**  Unit price in the vendors unit of measure and Rpt1 currency.  */  
   "Rpt1UnitCost":number,
      /**  Unit price in the vendors unit of measure and Rpt2 currency.  */  
   "Rpt2UnitCost":number,
      /**  Unit price in the vendors unit of measure and Rpt3 currency.  */  
   "Rpt3UnitCost":number,
      /**  Unit Of Measure of the ContractQty.  */  
   "ContractQtyUOM":string,
      /**  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  */  
   "Rpt1ContractUnitCost":number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  */  
   "Rpt2ContractUnitCost":number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  */  
   "Rpt3ContractUnitCost":number,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  */  
   "BaseQty":number,
      /**   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   "BaseUOM":string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderNum":number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderLine":number,
      /**   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   "VendorPartOpts":string,
      /**   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   "MfgPartOpts":string,
      /**   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  */  
   "SubPartOpts":string,
      /**  Manufacturer Unique ID  */  
   "MfgNum":number,
      /**  Manufacturer's Part Number.  */  
   "MfgPartNum":string,
      /**  Substitute Part Number  */  
   "SubPartNum":string,
      /**   Substitute Part Type
O = Original
S = Substitute  */  
   "SubPartType":string,
      /**   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   "ConfigUnitCost":number,
      /**  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   "ConfigBaseUnitCost":number,
      /**  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  */  
   "ConvOverRide":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  */  
   "QtyOption":string,
      /**  purchasing factor  */  
   "CalcPurchasingFactor":number,
   "CalcJobSeq":number,
   "CalcAssemblySeq":number,
   "CalcDueDate":string,
   "CalcJobNum":string,
   "CalcJobSeqType":string,
   "CurrencySwitch":boolean,
   "calcLeadTime":number,
   "calcMinOrderQty":number,
   "calcPartPUM":string,
   "CalcOurQty":number,
   "CalcVendQty":number,
   "CalcTranType":string,
   "CPFactor":number,
   "DisplaySymbol":string,
   "DocDisplaySymbol":string,
   "MultiRel":boolean,
   "CalcMfg":string,
   "CalcMfgPart":string,
   "PriceBrkBTNSensitive":boolean,
   "SetCheveron":boolean,
   "DelPoSug":boolean,
   "SubAvail":boolean,
   "POHeaderApprove":boolean,
   "ConsolidatedPO":boolean,
      /**  False if vendor or class requires inspection, otherwise true.  */  
   "EnableRcvInspectionReq":boolean,
      /**  The Chart ID component of the default G/L account.  */  
   "ExpChart":string,
      /**  The Division Component of the default expence G/L account.  */  
   "ExpDivision":string,
      /**  The Department component of the default G/L account.  */  
   "ExpGLDept":string,
      /**  Link to the related code in GlRefCod.RefCode  */  
   "ReferenceCode":string,
      /**  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  */  
   "DispExpAccount":string,
      /**  Display Account Description.  */  
   "DispAcctDescription":string,
      /**  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  */  
   "AskRefCode":boolean,
      /**  Reference Code Status  */  
   "RefCodeStatus":string,
      /**  Reference Code Description  */  
   "RefCodeDesc":string,
      /**  Purchase Point used in the Supplier Tracker.  */  
   "VendPurPoint":string,
   "CalcPurchasingFactorDirection":string,
   "ContractOrder":boolean,
   "FromPOSugChg":boolean,
   "PartQtyBearing":boolean,
   "DisablePartRevBtn":boolean,
      /**  True if there is only one release and it's open.  */  
   "PORelOneOpenRelease":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CalcMangCustNum":number,
   "CalcMangCustID":string,
   "CalcMangCustName":string,
      /**  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "CostPerCodeContract":string,
      /**  Full description of the part class.  */  
   "ClassDescription":string,
      /**  Description of the purchase type. Appears in drop-down lists for selection.  */  
   "GlPurchPurchDesc":string,
      /**  User assigned Manufacturer ID  */  
   "MfgNumMfgID":string,
      /**  Manufacturer Name  */  
   "MfgNumName":string,
      /**  defaults from the company file.  */  
   "PONUMShipName":string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   "PONUMShipToConName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PODetailRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  */  
   "OpenLine":boolean,
      /**   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  */  
   "VoidLine":boolean,
      /**  Purchase order number that the detail line item is linked to.  */  
   "PONUM":number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "POLine":number,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "LineDesc":string,
      /**  (Our) Unit Of Measure.  */  
   "IUM":string,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   "UnitCost":number,
      /**  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  */  
   "DocUnitCost":number,
      /**  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  */  
   "OrderQty":number,
      /**  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  */  
   "XOrderQty":number,
      /**  Taxable  */  
   "Taxable":boolean,
      /**  Purchasing UOM  */  
   "PUM":string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "CostPerCode":string,
      /**  OUR internal Part number for this item.  */  
   "PartNum":string,
      /**  Supplier Part Number  */  
   "VenPartNum":string,
      /**  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  */  
   "CommentText":string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  */  
   "ClassID":string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  */  
   "VendorNum":number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   "AdvancePayBal":number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   "DocAdvancePayBal":number,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   "Confirmed":boolean,
      /**  Indicates this line has a pending date change  */  
   "DateChgReq":boolean,
      /**  Indicates this line has a pending qty change  */  
   "QtyChgReq":boolean,
      /**  Requested pending partnumber change  */  
   "PartNumChgReq":string,
      /**  Requested pending revision change  */  
   "RevisionNumChgReq":string,
      /**  Date Supplier Confirmed the PO  */  
   "ConfirmDate":string,
      /**  Can be "web" or "client"  */  
   "ConfirmVia":string,
      /**  Requested Price change.  SRM  */  
   "PrcChgReq":number,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   "PurchCode":string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   "OrderNum":number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   "OrderLine":number,
      /**  Linked to sales order line.  */  
   "Linked":boolean,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Is this line active on the Contract Purchase Order?  */  
   "ContractActive":boolean,
      /**  Quantity for this Contract Purchase Order Line.  */  
   "ContractQty":number,
      /**  Unit Price for this Contract Purchase Order Line.  */  
   "ContractUnitCost":number,
      /**  Document Unit Price for this Contract Purchase Order Line.  */  
   "ContractDocUnitCost":number,
      /**  Advanced Payments Balance in Rpt1 currency.  */  
   "Rpt1AdvancePayBal":number,
      /**  Advanced Payments Balance in Rpt2 currency.  */  
   "Rpt2AdvancePayBal":number,
      /**  Advanced Payments Balance in Rpt3 currency.  */  
   "Rpt3AdvancePayBal":number,
      /**  Unit price in the vendors unit of measure and Rpt1 currency.  */  
   "Rpt1UnitCost":number,
      /**  Unit price in the vendors unit of measure and Rpt2 currency.  */  
   "Rpt2UnitCost":number,
      /**  Unit price in the vendors unit of measure and Rpt3 currency.  */  
   "Rpt3UnitCost":number,
      /**  Unit Of Measure of the ContractQty.  */  
   "ContractQtyUOM":string,
      /**  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  */  
   "Rpt1ContractUnitCost":number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  */  
   "Rpt2ContractUnitCost":number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  */  
   "Rpt3ContractUnitCost":number,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  */  
   "BaseQty":number,
      /**   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   "BaseUOM":string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderNum":number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderLine":number,
      /**   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   "VendorPartOpts":string,
      /**   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   "MfgPartOpts":string,
      /**   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  */  
   "SubPartOpts":string,
      /**  Manufacturer Unique ID  */  
   "MfgNum":number,
      /**  Manufacturer's Part Number.  */  
   "MfgPartNum":string,
      /**  Substitute Part Number  */  
   "SubPartNum":string,
      /**   Substitute Part Type
O = Original
S = Substitute  */  
   "SubPartType":string,
      /**   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   "ConfigUnitCost":number,
      /**  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   "ConfigBaseUnitCost":number,
      /**  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  */  
   "ConvOverRide":boolean,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  Direction  */  
   "Direction":string,
      /**  Per  */  
   "Per":string,
      /**  MaintainPricingUnits  */  
   "MaintainPricingUnits":boolean,
      /**  OverrideConversion  */  
   "OverrideConversion":boolean,
      /**  RowsManualFactor  */  
   "RowsManualFactor":boolean,
      /**  KeepRowsManualFactorTmp  */  
   "KeepRowsManualFactorTmp":boolean,
      /**  ShipToSupplierDate  */  
   "ShipToSupplierDate":string,
      /**  Factor  */  
   "Factor":number,
      /**  PricingQty  */  
   "PricingQty":number,
      /**  PricingUnitPrice  */  
   "PricingUnitPrice":number,
      /**  UOM  */  
   "UOM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  DocPricingUnitPrice  */  
   "DocPricingUnitPrice":number,
      /**  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  */  
   "OverridePriceList":boolean,
      /**  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  */  
   "QtyOption":string,
      /**  Contains old comments about the detail order line item. This field saves old comments about the detail line that are going to be replaced by new comments.  */  
   "OrigComment":string,
      /**  SmartString  */  
   "SmartString":string,
      /**  SmartStringProcessed  */  
   "SmartStringProcessed":boolean,
      /**  Specifies the date by which you need to receive the part. If you set the Due Date before create releases, it will act as default value when adding new releases. If you're adding lines from:  - BTO or Drop Shipments, PODetail.DueDate will take the value from OrderRel.NeedByDate. - Job Material , PODetail.DueDate  will take the value from JobMtl.ReqDate. - Subcontract Operations, PODetail.DueDate  wil take the value from JobOper.DueDate  */  
   "DueDate":string,
      /**  The identifier of the planning contract.  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   "LinkToContract":boolean,
      /**  SelCurrPricingUnitPrice  */  
   "SelCurrPricingUnitPrice":number,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date and time that the record was last changed  */  
   "ChangeDate":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  Indicates the Tax Category for this PO line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   "TaxCatID":string,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  */  
   "NoTaxRecalc":boolean,
      /**  Unit price in the vendors unit of measure inclusive of tax in base currency.  */  
   "InUnitCost":number,
      /**  Unit price in the vendors unit of measure inclusive of tax in document currency.  */  
   "DocInUnitCost":number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   "Rpt1InUnitCost":number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   "Rpt2InUnitCost":number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   "Rpt3InUnitCost":number,
      /**  Advanced Payments Balance inclusive of tax in base currency.  */  
   "InAdvancePayBal":number,
      /**  Advanced Payments Balance inclusive of tax in document currency.  */  
   "DocInAdvancePayBal":number,
      /**  Advanced Payments Balance inclusive of tax in Rpt1 currency.  */  
   "Rpt1InAdvancePayBal":number,
      /**  Advanced Payments Balance inclusive of tax in Rpt2 currency.  */  
   "Rpt2InAdvancePayBal":number,
      /**  Advanced Payments Balance inclusive of tax in Rpt3 currency.  */  
   "Rpt3InAdvancePayBal":number,
      /**  Contract unit cost inclusive of tax in base currency.  */  
   "InContractUnitCost":number,
      /**  Contract unit cost inclusive of tax in document currency.  */  
   "DocInContractUnitCost":number,
      /**  Contract unit cost inclusive of tax in Rpt1 currency.  */  
   "Rpt1InContractUnitCost":number,
      /**  Contract unit cost inclusive of tax in Rpt2 currency.  */  
   "Rpt2InContractUnitCost":number,
      /**  Contract unit cost inclusive of tax in Rpt3 currency.  */  
   "Rpt3InContractUnitCost":number,
      /**  Extended cost of the PO Line in document currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.DocUnitCost.  */  
   "DocExtCost":number,
      /**  Extended cost of the PO Line in base currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.UnitCost.  */  
   "ExtCost":number,
      /**  Extended cost of the PO Line in Rpt1 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt1UnitCost.  */  
   "Rpt1ExtCost":number,
      /**  Extended cost of the PO Line in Rpt2 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt2UnitCost.  */  
   "Rpt2ExtCost":number,
      /**  Extended cost of the PO Line in Rpt3 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt3UnitCost.  */  
   "Rpt3ExtCost":number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in document currency.  This is the sum of POMisc.DocMiscAmt for all line charges.  */  
   "DocMiscCost":number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in base currency.  This is the sum of POMisc.MiscAmt for all line charges.  */  
   "MiscCost":number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt for all line charges.  */  
   "Rpt1MiscCost":number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt for all line charges.  */  
   "Rpt2MiscCost":number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt for all line charges.  */  
   "Rpt3MiscCost":number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   "TotalTax":number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   "DocTotalTax":number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   "Rpt1TotalTax":number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   "Rpt2TotalTax":number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   "Rpt3TotalTax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   "TotalSATax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   "DocTotalSATax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalSATax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalSATax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalSATax":number,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   "TotalDedTax":number,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   "DocTotalDedTax":number,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalDedTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalDedTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalDedTax":number,
      /**  CommodityCode  */  
   "CommodityCode":string,
      /**  CNBonded  */  
   "CNBonded":boolean,
      /**  Acknowledge code received from EDI  */  
   "EDIAckCode":string,
      /**  Additional comments to send with Acknowledge  */  
   "EDIAckComment":string,
      /**  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  */  
   "AskRefCode":boolean,
   "CalcAssemblySeq":number,
   "CalcDocTotalCost":number,
   "CalcDueDate":string,
   "CalcJobNum":string,
   "CalcJobSeq":number,
   "CalcJobSeqType":string,
   "calcLeadTime":number,
   "CalcMangCustID":string,
   "CalcMangCustName":string,
   "CalcMangCustNum":number,
   "CalcMfg":string,
   "CalcMfgPart":string,
   "calcMinOrderQty":number,
   "CalcOurQty":number,
   "calcPartPUM":string,
      /**  purchasing factor  */  
   "CalcPurchasingFactor":number,
   "CalcPurchasingFactorDirection":string,
   "CalcTotalCost":number,
   "CalcTranType":string,
   "CalcVendQty":number,
   "Configured":string,
   "ConsolidatedPO":boolean,
   "ContractOrder":boolean,
      /**  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "CostPerCodeContract":string,
   "CPFactor":number,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "DelPoSug":boolean,
   "DisablePartRevBtn":boolean,
      /**  Display Account Description.  */  
   "DispAcctDescription":string,
      /**  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  */  
   "DispExpAccount":string,
   "DisplaySymbol":string,
   "DocDisplaySymbol":string,
   "DocScrUnitCost":number,
      /**  False if vendor or class requires inspection, otherwise true.  */  
   "EnableRcvInspectionReq":boolean,
      /**  The Chart ID component of the default G/L account.  */  
   "ExpChart":string,
      /**  The Division Component of the default expence G/L account.  */  
   "ExpDivision":string,
      /**  The Department component of the default G/L account.  */  
   "ExpGLDept":string,
   "FromPOSugChg":boolean,
   "LinkedSOConfig":boolean,
   "MultiRel":boolean,
   "NonMasterPart":boolean,
   "OpCode":string,
   "PartQtyBearing":boolean,
   "POHeaderApprove":boolean,
      /**  True if there is only one release and it's open.  */  
   "PORelOneOpenRelease":boolean,
   "PriceBrkBTNSensitive":boolean,
      /**  Reference Code Description  */  
   "RefCodeDesc":string,
      /**  Reference Code Status  */  
   "RefCodeStatus":string,
      /**  Link to the related code in GlRefCod.RefCode  */  
   "ReferenceCode":string,
   "Rpt1CalcTotalCost":number,
   "Rpt1ScrUnitCost":number,
   "Rpt2CalcTotalCost":number,
   "Rpt2ScrUnitCost":number,
   "Rpt3CalcTotalCost":number,
   "Rpt3ScrUnitCost":number,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   "ScrUnitCost":number,
   "SetCheveron":boolean,
   "SubAvail":boolean,
   "UpdateRelRecords":boolean,
      /**  Update PO Release Taxable Flag on Change of PO Detail Taxable Flag  */  
   "UpdateRelTaxable":boolean,
      /**  Purchase Point used in the Supplier Tracker.  */  
   "VendPurPoint":string,
   "AllowPORecon":boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   "EnableDynAttrButton":boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   "AttributeQtyMismatch":boolean,
   "CalcJobMtlSeq":number,
   "CalcJobOprSeq":number,
      /**  Flag to indicate the current PO Line has at least one Buy To Order Release  */  
   "HasBuyToOrderRelease":boolean,
      /**  The flag to indicate if PO  doc/base/rpt line amounts are recalculated  whne entered and no need to recalculate on save.  */  
   "LineAmtCalcd":boolean,
   "BitFlag":number,
   "ClassInactive":boolean,
   "ClassDescription":string,
   "CommodityCodeDescription":string,
   "GlPurchPurchDesc":string,
   "MfgNumMfgID":string,
   "MfgNumName":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumAttrClassID":string,
   "PONUMCurrencyCode":string,
   "PONUMOrderDate":string,
   "PONUMInPrice":boolean,
   "PONUMShipName":string,
   "PONUMShipToConName":string,
   "TaxCatIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "DeliveryInstructions_c":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param poNUM
      @param poLine
   */  
export interface DeleteByID_input{
   poNUM:number,
   poLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PODetailListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  */  
   OpenLine:boolean,
      /**   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  */  
   VoidLine:boolean,
      /**  Purchase order number that the detail line item is linked to.  */  
   PONUM:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   POLine:number,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   LineDesc:string,
      /**  (Our) Unit Of Measure.  */  
   IUM:string,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   UnitCost:number,
      /**  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  */  
   DocUnitCost:number,
      /**  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  */  
   OrderQty:number,
      /**  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  */  
   XOrderQty:number,
      /**  Taxable  */  
   Taxable:boolean,
      /**  Purchasing UOM  */  
   PUM:string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   CostPerCode:string,
      /**  OUR internal Part number for this item.  */  
   PartNum:string,
      /**  Supplier Part Number  */  
   VenPartNum:string,
      /**  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  */  
   CommentText:string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  */  
   ClassID:string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  */  
   VendorNum:number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   AdvancePayBal:number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   DocAdvancePayBal:number,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   Confirmed:boolean,
      /**  Indicates this line has a pending date change  */  
   DateChgReq:boolean,
      /**  Indicates this line has a pending qty change  */  
   QtyChgReq:boolean,
      /**  Requested pending partnumber change  */  
   PartNumChgReq:string,
      /**  Requested pending revision change  */  
   RevisionNumChgReq:string,
      /**  Date Supplier Confirmed the PO  */  
   ConfirmDate:string,
      /**  Can be "web" or "client"  */  
   ConfirmVia:string,
      /**  Requested Price change.  SRM  */  
   PrcChgReq:number,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   PurchCode:string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   OrderLine:number,
      /**  Linked to sales order line.  */  
   Linked:boolean,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Is this line active on the Contract Purchase Order?  */  
   ContractActive:boolean,
      /**  Quantity for this Contract Purchase Order Line.  */  
   ContractQty:number,
      /**  Unit Price for this Contract Purchase Order Line.  */  
   ContractUnitCost:number,
      /**  Document Unit Price for this Contract Purchase Order Line.  */  
   ContractDocUnitCost:number,
      /**  Advanced Payments Balance in Rpt1 currency.  */  
   Rpt1AdvancePayBal:number,
      /**  Advanced Payments Balance in Rpt2 currency.  */  
   Rpt2AdvancePayBal:number,
      /**  Advanced Payments Balance in Rpt3 currency.  */  
   Rpt3AdvancePayBal:number,
      /**  Unit price in the vendors unit of measure and Rpt1 currency.  */  
   Rpt1UnitCost:number,
      /**  Unit price in the vendors unit of measure and Rpt2 currency.  */  
   Rpt2UnitCost:number,
      /**  Unit price in the vendors unit of measure and Rpt3 currency.  */  
   Rpt3UnitCost:number,
      /**  Unit Of Measure of the ContractQty.  */  
   ContractQtyUOM:string,
      /**  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  */  
   Rpt1ContractUnitCost:number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  */  
   Rpt2ContractUnitCost:number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  */  
   Rpt3ContractUnitCost:number,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  */  
   BaseQty:number,
      /**   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   BaseUOM:string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderNum:number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderLine:number,
      /**   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   VendorPartOpts:string,
      /**   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   MfgPartOpts:string,
      /**   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  */  
   SubPartOpts:string,
      /**  Manufacturer Unique ID  */  
   MfgNum:number,
      /**  Manufacturer's Part Number.  */  
   MfgPartNum:string,
      /**  Substitute Part Number  */  
   SubPartNum:string,
      /**   Substitute Part Type
O = Original
S = Substitute  */  
   SubPartType:string,
      /**   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitCost:number,
      /**  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitCost:number,
      /**  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  */  
   ConvOverRide:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  */  
   QtyOption:string,
      /**  purchasing factor  */  
   CalcPurchasingFactor:number,
   CalcJobSeq:number,
   CalcAssemblySeq:number,
   CalcDueDate:string,
   CalcJobNum:string,
   CalcJobSeqType:string,
   CurrencySwitch:boolean,
   calcLeadTime:number,
   calcMinOrderQty:number,
   calcPartPUM:string,
   CalcOurQty:number,
   CalcVendQty:number,
   CalcTranType:string,
   CPFactor:number,
   DisplaySymbol:string,
   DocDisplaySymbol:string,
   MultiRel:boolean,
   CalcMfg:string,
   CalcMfgPart:string,
   PriceBrkBTNSensitive:boolean,
   SetCheveron:boolean,
   DelPoSug:boolean,
   SubAvail:boolean,
   POHeaderApprove:boolean,
   ConsolidatedPO:boolean,
      /**  False if vendor or class requires inspection, otherwise true.  */  
   EnableRcvInspectionReq:boolean,
      /**  The Chart ID component of the default G/L account.  */  
   ExpChart:string,
      /**  The Division Component of the default expence G/L account.  */  
   ExpDivision:string,
      /**  The Department component of the default G/L account.  */  
   ExpGLDept:string,
      /**  Link to the related code in GlRefCod.RefCode  */  
   ReferenceCode:string,
      /**  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  */  
   DispExpAccount:string,
      /**  Display Account Description.  */  
   DispAcctDescription:string,
      /**  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  */  
   AskRefCode:boolean,
      /**  Reference Code Status  */  
   RefCodeStatus:string,
      /**  Reference Code Description  */  
   RefCodeDesc:string,
      /**  Purchase Point used in the Supplier Tracker.  */  
   VendPurPoint:string,
   CalcPurchasingFactorDirection:string,
   ContractOrder:boolean,
   FromPOSugChg:boolean,
   PartQtyBearing:boolean,
   DisablePartRevBtn:boolean,
      /**  True if there is only one release and it's open.  */  
   PORelOneOpenRelease:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CalcMangCustNum:number,
   CalcMangCustID:string,
   CalcMangCustName:string,
      /**  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   CostPerCodeContract:string,
      /**  Full description of the part class.  */  
   ClassDescription:string,
      /**  Description of the purchase type. Appears in drop-down lists for selection.  */  
   GlPurchPurchDesc:string,
      /**  User assigned Manufacturer ID  */  
   MfgNumMfgID:string,
      /**  Manufacturer Name  */  
   MfgNumName:string,
      /**  defaults from the company file.  */  
   PONUMShipName:string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   PONUMShipToConName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PODetailListTableset{
   PODetailList:Erp_Tablesets_PODetailListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PODetailRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  */  
   OpenLine:boolean,
      /**   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  */  
   VoidLine:boolean,
      /**  Purchase order number that the detail line item is linked to.  */  
   PONUM:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   POLine:number,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   LineDesc:string,
      /**  (Our) Unit Of Measure.  */  
   IUM:string,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   UnitCost:number,
      /**  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  */  
   DocUnitCost:number,
      /**  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  */  
   OrderQty:number,
      /**  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  */  
   XOrderQty:number,
      /**  Taxable  */  
   Taxable:boolean,
      /**  Purchasing UOM  */  
   PUM:string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   CostPerCode:string,
      /**  OUR internal Part number for this item.  */  
   PartNum:string,
      /**  Supplier Part Number  */  
   VenPartNum:string,
      /**  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  */  
   CommentText:string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  */  
   ClassID:string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  */  
   VendorNum:number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   AdvancePayBal:number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   DocAdvancePayBal:number,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   Confirmed:boolean,
      /**  Indicates this line has a pending date change  */  
   DateChgReq:boolean,
      /**  Indicates this line has a pending qty change  */  
   QtyChgReq:boolean,
      /**  Requested pending partnumber change  */  
   PartNumChgReq:string,
      /**  Requested pending revision change  */  
   RevisionNumChgReq:string,
      /**  Date Supplier Confirmed the PO  */  
   ConfirmDate:string,
      /**  Can be "web" or "client"  */  
   ConfirmVia:string,
      /**  Requested Price change.  SRM  */  
   PrcChgReq:number,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   PurchCode:string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   OrderLine:number,
      /**  Linked to sales order line.  */  
   Linked:boolean,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Is this line active on the Contract Purchase Order?  */  
   ContractActive:boolean,
      /**  Quantity for this Contract Purchase Order Line.  */  
   ContractQty:number,
      /**  Unit Price for this Contract Purchase Order Line.  */  
   ContractUnitCost:number,
      /**  Document Unit Price for this Contract Purchase Order Line.  */  
   ContractDocUnitCost:number,
      /**  Advanced Payments Balance in Rpt1 currency.  */  
   Rpt1AdvancePayBal:number,
      /**  Advanced Payments Balance in Rpt2 currency.  */  
   Rpt2AdvancePayBal:number,
      /**  Advanced Payments Balance in Rpt3 currency.  */  
   Rpt3AdvancePayBal:number,
      /**  Unit price in the vendors unit of measure and Rpt1 currency.  */  
   Rpt1UnitCost:number,
      /**  Unit price in the vendors unit of measure and Rpt2 currency.  */  
   Rpt2UnitCost:number,
      /**  Unit price in the vendors unit of measure and Rpt3 currency.  */  
   Rpt3UnitCost:number,
      /**  Unit Of Measure of the ContractQty.  */  
   ContractQtyUOM:string,
      /**  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  */  
   Rpt1ContractUnitCost:number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  */  
   Rpt2ContractUnitCost:number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  */  
   Rpt3ContractUnitCost:number,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  */  
   BaseQty:number,
      /**   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   BaseUOM:string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderNum:number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderLine:number,
      /**   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   VendorPartOpts:string,
      /**   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   MfgPartOpts:string,
      /**   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  */  
   SubPartOpts:string,
      /**  Manufacturer Unique ID  */  
   MfgNum:number,
      /**  Manufacturer's Part Number.  */  
   MfgPartNum:string,
      /**  Substitute Part Number  */  
   SubPartNum:string,
      /**   Substitute Part Type
O = Original
S = Substitute  */  
   SubPartType:string,
      /**   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitCost:number,
      /**  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitCost:number,
      /**  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  */  
   ConvOverRide:boolean,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  Direction  */  
   Direction:string,
      /**  Per  */  
   Per:string,
      /**  MaintainPricingUnits  */  
   MaintainPricingUnits:boolean,
      /**  OverrideConversion  */  
   OverrideConversion:boolean,
      /**  RowsManualFactor  */  
   RowsManualFactor:boolean,
      /**  KeepRowsManualFactorTmp  */  
   KeepRowsManualFactorTmp:boolean,
      /**  ShipToSupplierDate  */  
   ShipToSupplierDate:string,
      /**  Factor  */  
   Factor:number,
      /**  PricingQty  */  
   PricingQty:number,
      /**  PricingUnitPrice  */  
   PricingUnitPrice:number,
      /**  UOM  */  
   UOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  DocPricingUnitPrice  */  
   DocPricingUnitPrice:number,
      /**  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  */  
   OverridePriceList:boolean,
      /**  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  */  
   QtyOption:string,
      /**  Contains old comments about the detail order line item. This field saves old comments about the detail line that are going to be replaced by new comments.  */  
   OrigComment:string,
      /**  SmartString  */  
   SmartString:string,
      /**  SmartStringProcessed  */  
   SmartStringProcessed:boolean,
      /**  Specifies the date by which you need to receive the part. If you set the Due Date before create releases, it will act as default value when adding new releases. If you're adding lines from:  - BTO or Drop Shipments, PODetail.DueDate will take the value from OrderRel.NeedByDate. - Job Material , PODetail.DueDate  will take the value from JobMtl.ReqDate. - Subcontract Operations, PODetail.DueDate  wil take the value from JobOper.DueDate  */  
   DueDate:string,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  SelCurrPricingUnitPrice  */  
   SelCurrPricingUnitPrice:number,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date and time that the record was last changed  */  
   ChangeDate:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  Indicates the Tax Category for this PO line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  */  
   NoTaxRecalc:boolean,
      /**  Unit price in the vendors unit of measure inclusive of tax in base currency.  */  
   InUnitCost:number,
      /**  Unit price in the vendors unit of measure inclusive of tax in document currency.  */  
   DocInUnitCost:number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   Rpt1InUnitCost:number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   Rpt2InUnitCost:number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   Rpt3InUnitCost:number,
      /**  Advanced Payments Balance inclusive of tax in base currency.  */  
   InAdvancePayBal:number,
      /**  Advanced Payments Balance inclusive of tax in document currency.  */  
   DocInAdvancePayBal:number,
      /**  Advanced Payments Balance inclusive of tax in Rpt1 currency.  */  
   Rpt1InAdvancePayBal:number,
      /**  Advanced Payments Balance inclusive of tax in Rpt2 currency.  */  
   Rpt2InAdvancePayBal:number,
      /**  Advanced Payments Balance inclusive of tax in Rpt3 currency.  */  
   Rpt3InAdvancePayBal:number,
      /**  Contract unit cost inclusive of tax in base currency.  */  
   InContractUnitCost:number,
      /**  Contract unit cost inclusive of tax in document currency.  */  
   DocInContractUnitCost:number,
      /**  Contract unit cost inclusive of tax in Rpt1 currency.  */  
   Rpt1InContractUnitCost:number,
      /**  Contract unit cost inclusive of tax in Rpt2 currency.  */  
   Rpt2InContractUnitCost:number,
      /**  Contract unit cost inclusive of tax in Rpt3 currency.  */  
   Rpt3InContractUnitCost:number,
      /**  Extended cost of the PO Line in document currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.DocUnitCost.  */  
   DocExtCost:number,
      /**  Extended cost of the PO Line in base currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.UnitCost.  */  
   ExtCost:number,
      /**  Extended cost of the PO Line in Rpt1 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt1UnitCost.  */  
   Rpt1ExtCost:number,
      /**  Extended cost of the PO Line in Rpt2 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt2UnitCost.  */  
   Rpt2ExtCost:number,
      /**  Extended cost of the PO Line in Rpt3 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt3UnitCost.  */  
   Rpt3ExtCost:number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in document currency.  This is the sum of POMisc.DocMiscAmt for all line charges.  */  
   DocMiscCost:number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in base currency.  This is the sum of POMisc.MiscAmt for all line charges.  */  
   MiscCost:number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt for all line charges.  */  
   Rpt1MiscCost:number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt for all line charges.  */  
   Rpt2MiscCost:number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt for all line charges.  */  
   Rpt3MiscCost:number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   TotalTax:number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   DocTotalTax:number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   Rpt1TotalTax:number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   Rpt2TotalTax:number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   Rpt3TotalTax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   TotalSATax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   DocTotalSATax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalSATax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalSATax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalSATax:number,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   TotalDedTax:number,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   DocTotalDedTax:number,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalDedTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalDedTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalDedTax:number,
      /**  CommodityCode  */  
   CommodityCode:string,
      /**  CNBonded  */  
   CNBonded:boolean,
      /**  Acknowledge code received from EDI  */  
   EDIAckCode:string,
      /**  Additional comments to send with Acknowledge  */  
   EDIAckComment:string,
      /**  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  */  
   AskRefCode:boolean,
   CalcAssemblySeq:number,
   CalcDocTotalCost:number,
   CalcDueDate:string,
   CalcJobNum:string,
   CalcJobSeq:number,
   CalcJobSeqType:string,
   calcLeadTime:number,
   CalcMangCustID:string,
   CalcMangCustName:string,
   CalcMangCustNum:number,
   CalcMfg:string,
   CalcMfgPart:string,
   calcMinOrderQty:number,
   CalcOurQty:number,
   calcPartPUM:string,
      /**  purchasing factor  */  
   CalcPurchasingFactor:number,
   CalcPurchasingFactorDirection:string,
   CalcTotalCost:number,
   CalcTranType:string,
   CalcVendQty:number,
   Configured:string,
   ConsolidatedPO:boolean,
   ContractOrder:boolean,
      /**  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   CostPerCodeContract:string,
   CPFactor:number,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   DelPoSug:boolean,
   DisablePartRevBtn:boolean,
      /**  Display Account Description.  */  
   DispAcctDescription:string,
      /**  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  */  
   DispExpAccount:string,
   DisplaySymbol:string,
   DocDisplaySymbol:string,
   DocScrUnitCost:number,
      /**  False if vendor or class requires inspection, otherwise true.  */  
   EnableRcvInspectionReq:boolean,
      /**  The Chart ID component of the default G/L account.  */  
   ExpChart:string,
      /**  The Division Component of the default expence G/L account.  */  
   ExpDivision:string,
      /**  The Department component of the default G/L account.  */  
   ExpGLDept:string,
   FromPOSugChg:boolean,
   LinkedSOConfig:boolean,
   MultiRel:boolean,
   NonMasterPart:boolean,
   OpCode:string,
   PartQtyBearing:boolean,
   POHeaderApprove:boolean,
      /**  True if there is only one release and it's open.  */  
   PORelOneOpenRelease:boolean,
   PriceBrkBTNSensitive:boolean,
      /**  Reference Code Description  */  
   RefCodeDesc:string,
      /**  Reference Code Status  */  
   RefCodeStatus:string,
      /**  Link to the related code in GlRefCod.RefCode  */  
   ReferenceCode:string,
   Rpt1CalcTotalCost:number,
   Rpt1ScrUnitCost:number,
   Rpt2CalcTotalCost:number,
   Rpt2ScrUnitCost:number,
   Rpt3CalcTotalCost:number,
   Rpt3ScrUnitCost:number,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   ScrUnitCost:number,
   SetCheveron:boolean,
   SubAvail:boolean,
   UpdateRelRecords:boolean,
      /**  Update PO Release Taxable Flag on Change of PO Detail Taxable Flag  */  
   UpdateRelTaxable:boolean,
      /**  Purchase Point used in the Supplier Tracker.  */  
   VendPurPoint:string,
   AllowPORecon:boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   EnableDynAttrButton:boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   AttributeQtyMismatch:boolean,
   CalcJobMtlSeq:number,
   CalcJobOprSeq:number,
      /**  Flag to indicate the current PO Line has at least one Buy To Order Release  */  
   HasBuyToOrderRelease:boolean,
      /**  The flag to indicate if PO  doc/base/rpt line amounts are recalculated  whne entered and no need to recalculate on save.  */  
   LineAmtCalcd:boolean,
   BitFlag:number,
   ClassInactive:boolean,
   ClassDescription:string,
   CommodityCodeDescription:string,
   GlPurchPurchDesc:string,
   MfgNumMfgID:string,
   MfgNumName:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumAttrClassID:string,
   PONUMCurrencyCode:string,
   PONUMOrderDate:string,
   PONUMInPrice:boolean,
   PONUMShipName:string,
   PONUMShipToConName:string,
   TaxCatIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   DeliveryInstructions_c:string,
}

export interface Erp_Tablesets_PODetailTrackerSearchTableset{
   PODetail:Erp_Tablesets_PODetailRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPODetailTrackerSearchTableset{
   PODetail:Erp_Tablesets_PODetailRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param poNUM
      @param poLine
   */  
export interface GetByID_input{
   poNUM:number,
   poLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PODetailTrackerSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PODetailTrackerSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PODetailTrackerSearchTableset[],
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
   returnObj:Erp_Tablesets_PODetailListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param poNUM
   */  
export interface GetNewPODetail_input{
   ds:Erp_Tablesets_PODetailTrackerSearchTableset[],
   poNUM:number,
}

export interface GetNewPODetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PODetailTrackerSearchTableset[],
}
}

   /** Required : 
      @param vendNum
      @param type
      @param fromOrderDate
      @param toOrderDate
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsByVendorNum_input{
      /**  POHeader Vendor Number  */  
   vendNum:number,
      /**  Current tab selected: All / Open / Closed.  */  
   type:string,
      /**  POHeader from OrderDate  */  
   fromOrderDate:string,
      /**  POHeader to OrderDate  */  
   toOrderDate:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetRowsByVendorNum_output{
   returnObj:Erp_Tablesets_PODetailTrackerSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePODetail
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePODetail:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PODetailTrackerSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtPODetailTrackerSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPODetailTrackerSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PODetailTrackerSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PODetailTrackerSearchTableset[],
}
}

