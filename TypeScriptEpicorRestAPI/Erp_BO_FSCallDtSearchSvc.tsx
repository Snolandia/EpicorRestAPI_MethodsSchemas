import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.FSCallDtSearchSvc
// Description: Search for Field Service Call Detail Line
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/$metadata", {
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
   Description: Get FSCallDtSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSCallDtSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtRow
   */  
export function get_FSCallDtSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/FSCallDtSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSCallDtSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FSCallDtSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/FSCallDtSearches", {
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
   Summary: Calls GetByID to retrieve the FSCallDtSearch item
   Description: Calls GetByID to retrieve the FSCallDtSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallDtSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   */  
export function get_FSCallDtSearches_Company_CallNum_CallLine(Company:string, CallNum:string, CallLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FSCallDtRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/FSCallDtSearches(" + Company + "," + CallNum + "," + CallLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_FSCallDtRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FSCallDtSearch for the service
   Description: Calls UpdateExt to update FSCallDtSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSCallDtSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FSCallDtSearches_Company_CallNum_CallLine(Company:string, CallNum:string, CallLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/FSCallDtSearches(" + Company + "," + CallNum + "," + CallLine + ")", {
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
   Summary: Call UpdateExt to delete FSCallDtSearch item
   Description: Call UpdateExt to delete FSCallDtSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSCallDtSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CallNum Desc: CallNum   Required: True
      @param CallLine Desc: CallLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FSCallDtSearches_Company_CallNum_CallLine(Company:string, CallNum:string, CallLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/FSCallDtSearches(" + Company + "," + CallNum + "," + CallLine + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtListRow)
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
export function get_GetRows(whereClauseFSCallDt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFSCallDt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFSCallDt=" + whereClauseFSCallDt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/GetRows" + params, {
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
export function get_GetByID(callNum:string, callLine:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof callNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "callNum=" + callNum
   }
   if(typeof callLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "callLine=" + callLine
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewFSCallDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSCallDt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFSCallDt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/GetNewFSCallDt", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSCallDtListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FSCallDtRow[],
}

export interface Erp_Tablesets_FSCallDtListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   "CallNum":number,
      /**  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  */  
   "CallLine":number,
      /**  The PartNum field identifies the Part  */  
   "PartNum":string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Serial number of the part being repaired.  */  
   "SerialNumber":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   "IUM":string,
      /**  TotalCall Quantity for the line item.  */  
   "CallQty":number,
      /**  Packing slip number that this Service call is linked with.  */  
   "PackNum":number,
      /**  The packing slip line that holds the warranty information for this service call  */  
   "PackLine":number,
      /**  Unique code for the Warranty  */  
   "WarrantyCode":string,
      /**  Contract Number if this item is under a contract  */  
   "ContractNum":number,
      /**  This is the contract line the relates to the item on the service call.  */  
   "ContractLine":number,
      /**  A unique code that identifies the Contract  */  
   "ContractCode":string,
      /**  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  */  
   "CallComment":string,
      /**  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Problem reason code from the reason master table. type problem.  */  
   "ProbReasonCode":string,
      /**  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  total Labor Amount.  */  
   "TotLabor":number,
      /**  total Labor Amount. In customers currency  */  
   "DocTotLabor":number,
      /**  total Billable Labor Amount.  */  
   "TotBillLabor":number,
      /**  total Billable Labor Amount. In Customers currency.  */  
   "DocTotBillLabor":number,
      /**  total Material Amount.  */  
   "TotMaterial":number,
      /**  total Material Amount. In Customers currency  */  
   "DocTotMaterial":number,
      /**  total Billable Material Amount.  */  
   "TotBillMaterial":number,
      /**  total Billable Material Amount. In Customers Currency.  */  
   "DocTotBillMaterial":number,
      /**  total Misc. Amount.  */  
   "TotMisc":number,
      /**  total Misc. Amount. In customers currency.  */  
   "DocTotMisc":number,
      /**  total Billable Misc. Amount.  */  
   "TotBillableMisc":number,
      /**  total Billable Misc. Amount. In customer's currency.  */  
   "DocTotBillableMisc":number,
      /**  total Material Cost.  */  
   "TotMaterialCost":number,
      /**  total Misc. Cost.  */  
   "TotMiscCost":number,
      /**  Project ID of the Project table record that this FSCallDt record. Can be blank.  */  
   "ProjectID":string,
      /**  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  */  
   "JobNum":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Total Subcontract Amount.  */  
   "TotSubCont":number,
      /**  total Subcontract Amount. In customers currency  */  
   "DocTotSubCont":number,
      /**  total Billable Subcontract Amount.  */  
   "TotBillSubCont":number,
      /**  total Billable Subcontract Amount. In Customers currency.  */  
   "DocTotBillSubCont":number,
      /**  total Estimated Labor Amount.  */  
   "TotEstLabor":number,
      /**  total estimated Labor Amount. In customers currency  */  
   "DocTotEstLabor":number,
      /**  total Estimated Material Amount.  */  
   "TotEstMaterial":number,
      /**  total Estimated Material Amount. In Customers currency  */  
   "DocTotEstMaterial":number,
      /**  total Estimated Misc. Amount.  Future Use.  */  
   "TotEstMisc":number,
      /**  total Est. Misc. Amount. In customers currency. Future use  */  
   "DocTotEstMisc":number,
      /**  Total estimated Subcontract Amount.  */  
   "TotEstSubCont":number,
      /**  total Estimated Subcontract Amount. In customers currency  */  
   "DocTotEstSubCont":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillableMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillableMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillableMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotSubCont":number,
      /**  The drop shipment packing slip number that this Service call is linked with  */  
   "DropShipPackSlip":string,
      /**  The drop shipment packing slip line that holds the warranty information for this service call  */  
   "DropShipPackLine":number,
      /**  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  */  
   "VendorNum":number,
      /**  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  */  
   "PurPoint":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Reson Code Description  */  
   "ProbReasonDesc":string,
   "CurrencySwitch":boolean,
      /**  Currency.CurrSymbol of the "BASE" currency  */  
   "BaseCurrSymbol":string,
      /**  Currency.CurrSymbol of the customer's currency  */  
   "DocCurrSymbol":string,
      /**  Total Actual Call Amount for the line  */  
   "TotLineCall":number,
      /**  Total Actual Call Amount for the line in customer's currency  */  
   "DocTotLineCall":number,
      /**  Total Billable Call Amount for the line  */  
   "TotLineBillCall":number,
      /**  Total Billable Call Amount for the line in customer's currency  */  
   "DocTotLineBillCall":number,
      /**  Total Estimated Call Amount for the line  */  
   "TotLineEstCall":number,
      /**  Total Estimated Call AMount for the line in customer's currency  */  
   "DocTotLineEstCall":number,
      /**  Indicates if Contract entry should be enabled.  */  
   "EnableContract":boolean,
      /**  Indicates if Warranty entry should be enabled.  */  
   "EnableWarranty":boolean,
   "DisplayContractType":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "Rpt1TotLineBillCall":number,
   "Rpt2TotLineBillCall":number,
   "Rpt3TotLineBillCall":number,
   "Rpt1TotLineCall":number,
   "Rpt2TotLineCall":number,
   "Rpt3TotLineCall":number,
   "Rpt1TotLineEstCall":number,
   "Rpt2TotLineEstCall":number,
   "Rpt3TotLineEstCall":number,
      /**  Unit of Measure Description  */  
   "IUMDesc":string,
      /**  Description of the service contract.  */  
   "ContractCodeContractDescription":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "ContractLineLineDesc":string,
      /**  Defaults from PODetail LineDesc.  */  
   "DropShipDtlLineDesc":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobNumPartDescription":string,
      /**  Line Description  */  
   "PackLineLineDesc":string,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "PackNumShipStatus":string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Full description of Product Group.  */  
   "ProdCodeDescription":string,
      /**  Full description of Project Management Code.  */  
   "ProjectIDDescription":string,
      /**  Description of the warranty.  */  
   "WarrantyCodeWarrDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FSCallDtRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   "CallNum":number,
      /**  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  */  
   "CallLine":number,
      /**  The PartNum field identifies the Part  */  
   "PartNum":string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   "RevisionNum":string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   "LineDesc":string,
      /**  Serial number of the part being repaired.  */  
   "SerialNumber":string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   "IUM":string,
      /**  TotalCall Quantity for the line item.  */  
   "CallQty":number,
      /**  Packing slip number that this Service call is linked with.  */  
   "PackNum":number,
      /**  The packing slip line that holds the warranty information for this service call  */  
   "PackLine":number,
      /**  Unique code for the Warranty  */  
   "WarrantyCode":string,
      /**  Contract Number if this item is under a contract  */  
   "ContractNum":number,
      /**  This is the contract line the relates to the item on the service call.  */  
   "ContractLine":number,
      /**  A unique code that identifies the Contract  */  
   "ContractCode":string,
      /**  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  */  
   "CallComment":string,
      /**  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  */  
   "InvoiceComment":string,
      /**  Problem reason code from the reason master table. type problem.  */  
   "ProbReasonCode":string,
      /**  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   "XPartNum":string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   "XRevisionNum":string,
      /**  Are Material cost covered  */  
   "MatCovered":boolean,
      /**  Is Labor Cost Covered  */  
   "LabCovered":boolean,
      /**  Are misc. Costs Covered  */  
   "MiscCovered":boolean,
      /**  total Labor Amount.  */  
   "TotLabor":number,
      /**  total Labor Amount. In customers currency  */  
   "DocTotLabor":number,
      /**  total Billable Labor Amount.  */  
   "TotBillLabor":number,
      /**  total Billable Labor Amount. In Customers currency.  */  
   "DocTotBillLabor":number,
      /**  total Material Amount.  */  
   "TotMaterial":number,
      /**  total Material Amount. In Customers currency  */  
   "DocTotMaterial":number,
      /**  total Billable Material Amount.  */  
   "TotBillMaterial":number,
      /**  total Billable Material Amount. In Customers Currency.  */  
   "DocTotBillMaterial":number,
      /**  total Misc. Amount.  */  
   "TotMisc":number,
      /**  total Misc. Amount. In customers currency.  */  
   "DocTotMisc":number,
      /**  total Billable Misc. Amount.  */  
   "TotBillableMisc":number,
      /**  total Billable Misc. Amount. In customer's currency.  */  
   "DocTotBillableMisc":number,
      /**  total Material Cost.  */  
   "TotMaterialCost":number,
      /**  total Misc. Cost.  */  
   "TotMiscCost":number,
      /**  Project ID of the Project table record that this FSCallDt record. Can be blank.  */  
   "ProjectID":string,
      /**  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  */  
   "JobNum":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Total Subcontract Amount.  */  
   "TotSubCont":number,
      /**  total Subcontract Amount. In customers currency  */  
   "DocTotSubCont":number,
      /**  total Billable Subcontract Amount.  */  
   "TotBillSubCont":number,
      /**  total Billable Subcontract Amount. In Customers currency.  */  
   "DocTotBillSubCont":number,
      /**  total Estimated Labor Amount.  */  
   "TotEstLabor":number,
      /**  total estimated Labor Amount. In customers currency  */  
   "DocTotEstLabor":number,
      /**  total Estimated Material Amount.  */  
   "TotEstMaterial":number,
      /**  total Estimated Material Amount. In Customers currency  */  
   "DocTotEstMaterial":number,
      /**  total Estimated Misc. Amount.  Future Use.  */  
   "TotEstMisc":number,
      /**  total Est. Misc. Amount. In customers currency. Future use  */  
   "DocTotEstMisc":number,
      /**  Total estimated Subcontract Amount.  */  
   "TotEstSubCont":number,
      /**  total Estimated Subcontract Amount. In customers currency  */  
   "DocTotEstSubCont":number,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillableMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillableMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillableMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotBillSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotBillSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotBillSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotEstSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotEstSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotEstSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotLabor":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotMaterial":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotMisc":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TotSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TotSubCont":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TotSubCont":number,
      /**  The drop shipment packing slip number that this Service call is linked with  */  
   "DropShipPackSlip":string,
      /**  The drop shipment packing slip line that holds the warranty information for this service call  */  
   "DropShipPackLine":number,
      /**  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  */  
   "VendorNum":number,
      /**  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  */  
   "PurPoint":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  POLine  */  
   "POLine":string,
      /**  IssueTopicID1  */  
   "IssueTopicID1":string,
      /**  IssueTopicID2  */  
   "IssueTopicID2":string,
      /**  IssueTopicID3  */  
   "IssueTopicID3":string,
      /**  IssueTopicID4  */  
   "IssueTopicID4":string,
      /**  IssueTopicID5  */  
   "IssueTopicID5":string,
      /**  IssueTopicID6  */  
   "IssueTopicID6":string,
      /**  IssueTopicID7  */  
   "IssueTopicID7":string,
      /**  IssueTopicID8  */  
   "IssueTopicID8":string,
      /**  IssueTopicID9  */  
   "IssueTopicID9":string,
      /**  IssueTopicID10  */  
   "IssueTopicID10":string,
      /**  IssueTopics  */  
   "IssueTopics":string,
      /**  ResTopicID1  */  
   "ResTopicID1":string,
      /**  ResTopicID2  */  
   "ResTopicID2":string,
      /**  ResTopicID3  */  
   "ResTopicID3":string,
      /**  ResTopicID4  */  
   "ResTopicID4":string,
      /**  ResTopicID5  */  
   "ResTopicID5":string,
      /**  ResTopicID6  */  
   "ResTopicID6":string,
      /**  ResTopicID7  */  
   "ResTopicID7":string,
      /**  ResTopicID8  */  
   "ResTopicID8":string,
      /**  ResTopicID9  */  
   "ResTopicID9":string,
      /**  ResTopicID10  */  
   "ResTopicID10":string,
      /**  ResTopics  */  
   "ResTopics":string,
      /**  PartDescription  */  
   "PartDescription":string,
      /**  CommentText  */  
   "CommentText":string,
      /**  Indicates the invoice processing has been done for this call line.  */  
   "Invoiced":boolean,
      /**  Indicates that the call line can be invoiced.  */  
   "ReadyToInvoice":boolean,
      /**  Currency.CurrSymbol of the "BASE" currency  */  
   "BaseCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "DisplayContractType":string,
      /**  Currency.CurrSymbol of the customer's currency  */  
   "DocCurrSymbol":string,
      /**  Total Billable Call Amount for the line in customer's currency  */  
   "DocTotLineBillCall":number,
      /**  Total Actual Call Amount for the line in customer's currency  */  
   "DocTotLineCall":number,
      /**  Total Estimated Call AMount for the line in customer's currency  */  
   "DocTotLineEstCall":number,
      /**  Indicates if Contract entry should be enabled.  */  
   "EnableContract":boolean,
      /**  Indicates if Warranty entry should be enabled.  */  
   "EnableWarranty":boolean,
      /**  Unit of Measure Description  */  
   "IUMDesc":string,
      /**  Reson Code Description  */  
   "ProbReasonDesc":string,
   "Rpt1TotLineBillCall":number,
   "Rpt1TotLineCall":number,
   "Rpt1TotLineEstCall":number,
   "Rpt2TotLineBillCall":number,
   "Rpt2TotLineCall":number,
   "Rpt2TotLineEstCall":number,
   "Rpt3TotLineBillCall":number,
   "Rpt3TotLineCall":number,
   "Rpt3TotLineEstCall":number,
      /**  Total Billable Call Amount for the line  */  
   "TotLineBillCall":number,
      /**  Total Actual Call Amount for the line  */  
   "TotLineCall":number,
      /**  Total Estimated Call Amount for the line  */  
   "TotLineEstCall":number,
   "JobClosed":boolean,
   "BitFlag":number,
   "ContractCodeContractDescription":string,
   "ContractLineLineDesc":string,
   "DropShipDtlLineDesc":string,
   "IssueTopicID1Description":string,
   "IssueTopicID10Description":string,
   "IssueTopicID2Description":string,
   "IssueTopicID3Description":string,
   "IssueTopicID4Description":string,
   "IssueTopicID5Description":string,
   "IssueTopicID6Description":string,
   "IssueTopicID7Description":string,
   "IssueTopicID8Description":string,
   "IssueTopicID9Description":string,
   "JobNumPartDescription":string,
   "PackLineLineDesc":string,
   "PackNumShipStatus":string,
   "PartNumSalesUM":string,
   "PartNumSellingFactor":number,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "ProdCodeDescription":string,
   "ProjectIDDescription":string,
   "ResTopicID1Description":string,
   "ResTopicID10Description":string,
   "ResTopicID2Description":string,
   "ResTopicID3Description":string,
   "ResTopicID4Description":string,
   "ResTopicID5Description":string,
   "ResTopicID6Description":string,
   "ResTopicID7Description":string,
   "ResTopicID8Description":string,
   "ResTopicID9Description":string,
   "WarrantyCodeWarrDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param callNum
      @param callLine
   */  
export interface DeleteByID_input{
   callNum:number,
   callLine:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_FSCallDtListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   CallNum:number,
      /**  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  */  
   CallLine:number,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Serial number of the part being repaired.  */  
   SerialNumber:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  TotalCall Quantity for the line item.  */  
   CallQty:number,
      /**  Packing slip number that this Service call is linked with.  */  
   PackNum:number,
      /**  The packing slip line that holds the warranty information for this service call  */  
   PackLine:number,
      /**  Unique code for the Warranty  */  
   WarrantyCode:string,
      /**  Contract Number if this item is under a contract  */  
   ContractNum:number,
      /**  This is the contract line the relates to the item on the service call.  */  
   ContractLine:number,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  */  
   CallComment:string,
      /**  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Problem reason code from the reason master table. type problem.  */  
   ProbReasonCode:string,
      /**  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  total Labor Amount.  */  
   TotLabor:number,
      /**  total Labor Amount. In customers currency  */  
   DocTotLabor:number,
      /**  total Billable Labor Amount.  */  
   TotBillLabor:number,
      /**  total Billable Labor Amount. In Customers currency.  */  
   DocTotBillLabor:number,
      /**  total Material Amount.  */  
   TotMaterial:number,
      /**  total Material Amount. In Customers currency  */  
   DocTotMaterial:number,
      /**  total Billable Material Amount.  */  
   TotBillMaterial:number,
      /**  total Billable Material Amount. In Customers Currency.  */  
   DocTotBillMaterial:number,
      /**  total Misc. Amount.  */  
   TotMisc:number,
      /**  total Misc. Amount. In customers currency.  */  
   DocTotMisc:number,
      /**  total Billable Misc. Amount.  */  
   TotBillableMisc:number,
      /**  total Billable Misc. Amount. In customer's currency.  */  
   DocTotBillableMisc:number,
      /**  total Material Cost.  */  
   TotMaterialCost:number,
      /**  total Misc. Cost.  */  
   TotMiscCost:number,
      /**  Project ID of the Project table record that this FSCallDt record. Can be blank.  */  
   ProjectID:string,
      /**  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  */  
   JobNum:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Total Subcontract Amount.  */  
   TotSubCont:number,
      /**  total Subcontract Amount. In customers currency  */  
   DocTotSubCont:number,
      /**  total Billable Subcontract Amount.  */  
   TotBillSubCont:number,
      /**  total Billable Subcontract Amount. In Customers currency.  */  
   DocTotBillSubCont:number,
      /**  total Estimated Labor Amount.  */  
   TotEstLabor:number,
      /**  total estimated Labor Amount. In customers currency  */  
   DocTotEstLabor:number,
      /**  total Estimated Material Amount.  */  
   TotEstMaterial:number,
      /**  total Estimated Material Amount. In Customers currency  */  
   DocTotEstMaterial:number,
      /**  total Estimated Misc. Amount.  Future Use.  */  
   TotEstMisc:number,
      /**  total Est. Misc. Amount. In customers currency. Future use  */  
   DocTotEstMisc:number,
      /**  Total estimated Subcontract Amount.  */  
   TotEstSubCont:number,
      /**  total Estimated Subcontract Amount. In customers currency  */  
   DocTotEstSubCont:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotSubCont:number,
      /**  The drop shipment packing slip number that this Service call is linked with  */  
   DropShipPackSlip:string,
      /**  The drop shipment packing slip line that holds the warranty information for this service call  */  
   DropShipPackLine:number,
      /**  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  */  
   VendorNum:number,
      /**  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  */  
   PurPoint:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Reson Code Description  */  
   ProbReasonDesc:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol of the "BASE" currency  */  
   BaseCurrSymbol:string,
      /**  Currency.CurrSymbol of the customer's currency  */  
   DocCurrSymbol:string,
      /**  Total Actual Call Amount for the line  */  
   TotLineCall:number,
      /**  Total Actual Call Amount for the line in customer's currency  */  
   DocTotLineCall:number,
      /**  Total Billable Call Amount for the line  */  
   TotLineBillCall:number,
      /**  Total Billable Call Amount for the line in customer's currency  */  
   DocTotLineBillCall:number,
      /**  Total Estimated Call Amount for the line  */  
   TotLineEstCall:number,
      /**  Total Estimated Call AMount for the line in customer's currency  */  
   DocTotLineEstCall:number,
      /**  Indicates if Contract entry should be enabled.  */  
   EnableContract:boolean,
      /**  Indicates if Warranty entry should be enabled.  */  
   EnableWarranty:boolean,
   DisplayContractType:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   Rpt1TotLineBillCall:number,
   Rpt2TotLineBillCall:number,
   Rpt3TotLineBillCall:number,
   Rpt1TotLineCall:number,
   Rpt2TotLineCall:number,
   Rpt3TotLineCall:number,
   Rpt1TotLineEstCall:number,
   Rpt2TotLineEstCall:number,
   Rpt3TotLineEstCall:number,
      /**  Unit of Measure Description  */  
   IUMDesc:string,
      /**  Description of the service contract.  */  
   ContractCodeContractDescription:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   ContractLineLineDesc:string,
      /**  Defaults from PODetail LineDesc.  */  
   DropShipDtlLineDesc:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobNumPartDescription:string,
      /**  Line Description  */  
   PackLineLineDesc:string,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   PackNumShipStatus:string,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Full description of Product Group.  */  
   ProdCodeDescription:string,
      /**  Full description of Project Management Code.  */  
   ProjectIDDescription:string,
      /**  Description of the warranty.  */  
   WarrantyCodeWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSCallDtListTableset{
   FSCallDtList:Erp_Tablesets_FSCallDtListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FSCallDtRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   CallNum:number,
      /**  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  */  
   CallLine:number,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  */  
   RevisionNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Serial number of the part being repaired.  */  
   SerialNumber:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  TotalCall Quantity for the line item.  */  
   CallQty:number,
      /**  Packing slip number that this Service call is linked with.  */  
   PackNum:number,
      /**  The packing slip line that holds the warranty information for this service call  */  
   PackLine:number,
      /**  Unique code for the Warranty  */  
   WarrantyCode:string,
      /**  Contract Number if this item is under a contract  */  
   ContractNum:number,
      /**  This is the contract line the relates to the item on the service call.  */  
   ContractLine:number,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  */  
   CallComment:string,
      /**  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Problem reason code from the reason master table. type problem.  */  
   ProbReasonCode:string,
      /**  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  total Labor Amount.  */  
   TotLabor:number,
      /**  total Labor Amount. In customers currency  */  
   DocTotLabor:number,
      /**  total Billable Labor Amount.  */  
   TotBillLabor:number,
      /**  total Billable Labor Amount. In Customers currency.  */  
   DocTotBillLabor:number,
      /**  total Material Amount.  */  
   TotMaterial:number,
      /**  total Material Amount. In Customers currency  */  
   DocTotMaterial:number,
      /**  total Billable Material Amount.  */  
   TotBillMaterial:number,
      /**  total Billable Material Amount. In Customers Currency.  */  
   DocTotBillMaterial:number,
      /**  total Misc. Amount.  */  
   TotMisc:number,
      /**  total Misc. Amount. In customers currency.  */  
   DocTotMisc:number,
      /**  total Billable Misc. Amount.  */  
   TotBillableMisc:number,
      /**  total Billable Misc. Amount. In customer's currency.  */  
   DocTotBillableMisc:number,
      /**  total Material Cost.  */  
   TotMaterialCost:number,
      /**  total Misc. Cost.  */  
   TotMiscCost:number,
      /**  Project ID of the Project table record that this FSCallDt record. Can be blank.  */  
   ProjectID:string,
      /**  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  */  
   JobNum:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Total Subcontract Amount.  */  
   TotSubCont:number,
      /**  total Subcontract Amount. In customers currency  */  
   DocTotSubCont:number,
      /**  total Billable Subcontract Amount.  */  
   TotBillSubCont:number,
      /**  total Billable Subcontract Amount. In Customers currency.  */  
   DocTotBillSubCont:number,
      /**  total Estimated Labor Amount.  */  
   TotEstLabor:number,
      /**  total estimated Labor Amount. In customers currency  */  
   DocTotEstLabor:number,
      /**  total Estimated Material Amount.  */  
   TotEstMaterial:number,
      /**  total Estimated Material Amount. In Customers currency  */  
   DocTotEstMaterial:number,
      /**  total Estimated Misc. Amount.  Future Use.  */  
   TotEstMisc:number,
      /**  total Est. Misc. Amount. In customers currency. Future use  */  
   DocTotEstMisc:number,
      /**  Total estimated Subcontract Amount.  */  
   TotEstSubCont:number,
      /**  total Estimated Subcontract Amount. In customers currency  */  
   DocTotEstSubCont:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillableMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotBillSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotEstSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotLabor:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotMaterial:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotMisc:number,
      /**  Reporting currency value of this field  */  
   Rpt1TotSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt2TotSubCont:number,
      /**  Reporting currency value of this field  */  
   Rpt3TotSubCont:number,
      /**  The drop shipment packing slip number that this Service call is linked with  */  
   DropShipPackSlip:string,
      /**  The drop shipment packing slip line that holds the warranty information for this service call  */  
   DropShipPackLine:number,
      /**  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  */  
   VendorNum:number,
      /**  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  */  
   PurPoint:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  POLine  */  
   POLine:string,
      /**  IssueTopicID1  */  
   IssueTopicID1:string,
      /**  IssueTopicID2  */  
   IssueTopicID2:string,
      /**  IssueTopicID3  */  
   IssueTopicID3:string,
      /**  IssueTopicID4  */  
   IssueTopicID4:string,
      /**  IssueTopicID5  */  
   IssueTopicID5:string,
      /**  IssueTopicID6  */  
   IssueTopicID6:string,
      /**  IssueTopicID7  */  
   IssueTopicID7:string,
      /**  IssueTopicID8  */  
   IssueTopicID8:string,
      /**  IssueTopicID9  */  
   IssueTopicID9:string,
      /**  IssueTopicID10  */  
   IssueTopicID10:string,
      /**  IssueTopics  */  
   IssueTopics:string,
      /**  ResTopicID1  */  
   ResTopicID1:string,
      /**  ResTopicID2  */  
   ResTopicID2:string,
      /**  ResTopicID3  */  
   ResTopicID3:string,
      /**  ResTopicID4  */  
   ResTopicID4:string,
      /**  ResTopicID5  */  
   ResTopicID5:string,
      /**  ResTopicID6  */  
   ResTopicID6:string,
      /**  ResTopicID7  */  
   ResTopicID7:string,
      /**  ResTopicID8  */  
   ResTopicID8:string,
      /**  ResTopicID9  */  
   ResTopicID9:string,
      /**  ResTopicID10  */  
   ResTopicID10:string,
      /**  ResTopics  */  
   ResTopics:string,
      /**  PartDescription  */  
   PartDescription:string,
      /**  CommentText  */  
   CommentText:string,
      /**  Indicates the invoice processing has been done for this call line.  */  
   Invoiced:boolean,
      /**  Indicates that the call line can be invoiced.  */  
   ReadyToInvoice:boolean,
      /**  Currency.CurrSymbol of the "BASE" currency  */  
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   DisplayContractType:string,
      /**  Currency.CurrSymbol of the customer's currency  */  
   DocCurrSymbol:string,
      /**  Total Billable Call Amount for the line in customer's currency  */  
   DocTotLineBillCall:number,
      /**  Total Actual Call Amount for the line in customer's currency  */  
   DocTotLineCall:number,
      /**  Total Estimated Call AMount for the line in customer's currency  */  
   DocTotLineEstCall:number,
      /**  Indicates if Contract entry should be enabled.  */  
   EnableContract:boolean,
      /**  Indicates if Warranty entry should be enabled.  */  
   EnableWarranty:boolean,
      /**  Unit of Measure Description  */  
   IUMDesc:string,
      /**  Reson Code Description  */  
   ProbReasonDesc:string,
   Rpt1TotLineBillCall:number,
   Rpt1TotLineCall:number,
   Rpt1TotLineEstCall:number,
   Rpt2TotLineBillCall:number,
   Rpt2TotLineCall:number,
   Rpt2TotLineEstCall:number,
   Rpt3TotLineBillCall:number,
   Rpt3TotLineCall:number,
   Rpt3TotLineEstCall:number,
      /**  Total Billable Call Amount for the line  */  
   TotLineBillCall:number,
      /**  Total Actual Call Amount for the line  */  
   TotLineCall:number,
      /**  Total Estimated Call Amount for the line  */  
   TotLineEstCall:number,
   JobClosed:boolean,
   BitFlag:number,
   ContractCodeContractDescription:string,
   ContractLineLineDesc:string,
   DropShipDtlLineDesc:string,
   IssueTopicID1Description:string,
   IssueTopicID10Description:string,
   IssueTopicID2Description:string,
   IssueTopicID3Description:string,
   IssueTopicID4Description:string,
   IssueTopicID5Description:string,
   IssueTopicID6Description:string,
   IssueTopicID7Description:string,
   IssueTopicID8Description:string,
   IssueTopicID9Description:string,
   JobNumPartDescription:string,
   PackLineLineDesc:string,
   PackNumShipStatus:string,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   ProdCodeDescription:string,
   ProjectIDDescription:string,
   ResTopicID1Description:string,
   ResTopicID10Description:string,
   ResTopicID2Description:string,
   ResTopicID3Description:string,
   ResTopicID4Description:string,
   ResTopicID5Description:string,
   ResTopicID6Description:string,
   ResTopicID7Description:string,
   ResTopicID8Description:string,
   ResTopicID9Description:string,
   WarrantyCodeWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FSCallDtSearchTableset{
   FSCallDt:Erp_Tablesets_FSCallDtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtFSCallDtSearchTableset{
   FSCallDt:Erp_Tablesets_FSCallDtRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param callNum
      @param callLine
   */  
export interface GetByID_input{
   callNum:number,
   callLine:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_FSCallDtSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_FSCallDtSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_FSCallDtSearchTableset[],
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
   returnObj:Erp_Tablesets_FSCallDtListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param callNum
   */  
export interface GetNewFSCallDt_input{
   ds:Erp_Tablesets_FSCallDtSearchTableset[],
   callNum:number,
}

export interface GetNewFSCallDt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSCallDtSearchTableset[],
}
}

   /** Required : 
      @param whereClauseFSCallDt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFSCallDt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_FSCallDtSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtFSCallDtSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtFSCallDtSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_FSCallDtSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FSCallDtSearchTableset[],
}
}

