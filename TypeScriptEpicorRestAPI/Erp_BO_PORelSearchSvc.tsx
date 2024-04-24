import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PORelSearchSvc
// Description: PO Release Search
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/$metadata", {
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
   Description: Get PORelSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PORelSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelRow
   */  
export function get_PORelSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/PORelSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PORelSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PORelRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PORelRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PORelSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/PORelSearches", {
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
   Summary: Calls GetByID to retrieve the PORelSearch item
   Description: Calls GetByID to retrieve the PORelSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelRow
   */  
export function get_PORelSearches_Company_PONum_POLine_PORelNum(Company:string, PONum:string, POLine:string, PORelNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PORelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/PORelSearches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PORelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PORelSearch for the service
   Description: Calls UpdateExt to update PORelSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PORelSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PORelRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PORelSearches_Company_PONum_POLine_PORelNum(Company:string, PONum:string, POLine:string, PORelNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/PORelSearches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")", {
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
   Summary: Call UpdateExt to delete PORelSearch item
   Description: Call UpdateExt to delete PORelSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PORelSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PORelSearches_Company_PONum_POLine_PORelNum(Company:string, PONum:string, POLine:string, PORelNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/PORelSearches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelListRow)
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
export function get_GetRows(whereClausePORel:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePORel!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePORel=" + whereClausePORel
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/GetRows" + params, {
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
export function get_GetByID(poNum:string, poLine:string, poRelNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof poNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "poNum=" + poNum
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
   if(typeof poRelNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "poRelNum=" + poRelNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetListWithPOLinePartNum
   Description: This method receives whereClause in format "POLinePartNum >= 'VALUE' order by POLinePartNum" which is generated in Kinetic search engine.
Then modify this where to use in ContainerPORelSearch
   OperationID: GetListWithPOLinePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListWithPOLinePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListWithPOLinePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListWithPOLinePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/GetListWithPOLinePartNum", {
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
   Summary: Invoke method GetListForContainer
   Description: Get List of PO Releases available for Container.
   OperationID: GetListForContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForContainer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/GetListForContainer", {
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
   Summary: Invoke method ContainerPORelSearch
   Description: Purpose:
Parameters:
<param name="WhereClausePoRel">PO Release search clause</param><returns>PO Rel List Data Set</returns><param name="pageSize">Page size</param><param name="absolutePage">Absolute page</param><param name="morePages">More Pages</param>
Notes:
   OperationID: ContainerPORelSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ContainerPORelSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ContainerPORelSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContainerPORelSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/ContainerPORelSearch", {
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
   Summary: Invoke method GetCloseReleaseAt
   Description: This method returns the 'Close Release At' company setting
   OperationID: GetCloseReleaseAt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCloseReleaseAt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCloseReleaseAt(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/GetCloseReleaseAt", {
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
   Summary: Invoke method GetRowsExcludeGlobal
   Description: Filter Releases from other Companies. Call normal GetRows method.
   OperationID: GetRowsExcludeGlobal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsExcludeGlobal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsExcludeGlobal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsExcludeGlobal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/GetRowsExcludeGlobal", {
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
   Summary: Invoke method GetNewPORel
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPORel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPORel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPORel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPORel(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/GetNewPORel", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PORelListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PORelRow[],
}

export interface Erp_Tablesets_PORelListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   "OpenRelease":boolean,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  */  
   "VoidRelease":boolean,
      /**  Purchase order that this release record is related to.  */  
   "PONum":number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "PORelNum":number,
      /**  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   "DueDate":string,
      /**  Order quantity for this release in our unit of measure.  */  
   "XRelQty":number,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  */  
   "PurchasingFactor":number,
      /**  Order quantity for this release in vendors unit of measure.  */  
   "RelQty":number,
      /**  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  */  
   "JobNum":string,
      /**  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  */  
   "AssemblySeq":number,
      /**   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record.  */  
   "JobSeq":number,
      /**  Warehouse that the item on this release is being purchased for.  */  
   "WarehouseCode":string,
      /**  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  */  
   "ReceivedQty":number,
      /**  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  */  
   "ExpOverride":boolean,
      /**  Requisition which generated this PORel record.  */  
   "ReqNum":number,
      /**  Requisition line which generated this PORel record.  */  
   "ReqLine":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   "PromiseDt":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   "Confirmed":boolean,
      /**  Can be "web", "client", or "rejected"  */  
   "ConfirmVia":string,
      /**   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  */  
   "ReqChgDate":string,
      /**   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  */  
   "ReqChgQty":number,
      /**  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  */  
   "LockRel":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  */  
   "RefDisplayAccount":string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "RefCodeDesc":string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   "OrderNum":number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   "OrderLine":number,
      /**  Order Release Line created for this PO Release for the Inter-Company Trading.  */  
   "OrderRelNum":number,
      /**  Linked to sales order release.  */  
   "Linked":boolean,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  */  
   "ShippedQty":number,
      /**   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  */  
   "TranType":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  */  
   "GlbPlant":string,
      /**  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  */  
   "GlbWarehouse":string,
      /**  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  */  
   "GlbCreateJobMtl":boolean,
      /**  Shipped Date  */  
   "ShippedDate":string,
      /**  ID field to the ContainerHeader table.  */  
   "ContainerID":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "PurchasingFactorDirection":string,
      /**  This field holds the previous value of Due Date.  */  
   "PreviousDueDate":string,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  */  
   "BaseQty":number,
      /**   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   "BaseUOM":string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderNum":number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderLine":number,
      /**  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderRelNum":number,
      /**  The value of this field comes from the sales order release. Used only for Buy To Order POs.  */  
   "DropShip":boolean,
      /**  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  */  
   "ShipToNum":string,
      /**  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  */  
   "SoldToNum":number,
      /**  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  */  
   "SMIRcvdQty":number,
      /**  Contains the key value for the shipping contact.  */  
   "ShpConNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  */  
   "MangCustNum":number,
      /**  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  */  
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
      /**  One Time Shipping Country Number  */  
   "OTSCountryNum":number,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  Open Purchase Release flag  */  
   "PORelOpen":boolean,
      /**  Mapping  */  
   "Mapping":boolean,
      /**  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  */  
   "PhaseID":string,
      /**  Project Phase ID  */  
   "WBSPhaseID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  */  
   "LockQty":boolean,
      /**  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  */  
   "LockDate":boolean,
   "ExpDesc":string,
   "EstUnitCost":number,
   "IUM":string,
   "Inspection":boolean,
   "DelPoSug":boolean,
      /**  Replicate PUM on detail  */  
   "PUM":string,
   "POHeaderApprove":boolean,
      /**  Indicates if Glb fields should be used in place of the non-global equivalent  */  
   "UseGlbFields":boolean,
   "ConsolidatedPO":boolean,
   "GlbPlantName":string,
   "GlbWhseName":string,
      /**  This field will be used in the UI to Lock and unLock a release.  */  
   "Lock":boolean,
      /**  Related Supplier ID  */  
   "VendorID":string,
      /**  Related Vendor Name  */  
   "VendorName":string,
   "RefCodeStatus":string,
      /**  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   "PurPoint":string,
      /**  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   "OrderHeld":boolean,
      /**  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  */  
   "EnableGLAcct":boolean,
      /**  Logical indicating if the container has been shipped.  */  
   "ContainerShipped":boolean,
   "FromPOSugChg":boolean,
      /**  Is this Release related to a Contract Purchase Order?  */  
   "ContractOrder":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
      /**  Identifies the type of PO  */  
   "POType":string,
      /**  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  */  
   "MangCustID":string,
      /**  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  */  
   "MangCustName":string,
   "ShipToAddressList":string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   "NotCompliant":boolean,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "AssemblySeqDescription":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  OUR internal Part number for this item.  */  
   "POLinePartNum":string,
      /**  Supplier Part Number  */  
   "POLineVenPartNum":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "POLineLineDesc":string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   "PONumShipToConName":string,
      /**  defaults from the company file.  */  
   "PONumShipName":string,
      /**  Full description of Project Management Code.  */  
   "ProjectIDDescription":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  */  
   "ReqLineLineDesc":string,
      /**  defaults from the company file.  */  
   "ReqNumShipName":string,
      /**  Ship to contact name.  */  
   "ReqNumShipToConName":string,
      /**  The full name of the customer.  */  
   "ShipToCustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "ShipToCustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "ShipToCustNumCustID":string,
      /**  The full name of the customer.  */  
   "SoldToNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "SoldToNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "SoldToNumCustID":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PORelRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   "OpenRelease":boolean,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  */  
   "VoidRelease":boolean,
      /**  Purchase order that this release record is related to.  */  
   "PONum":number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "PORelNum":number,
      /**  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   "DueDate":string,
      /**  Order quantity for this release in our unit of measure.  */  
   "XRelQty":number,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  */  
   "PurchasingFactor":number,
      /**  Order quantity for this release in vendors unit of measure.  */  
   "RelQty":number,
      /**  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  */  
   "JobNum":string,
      /**  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  */  
   "AssemblySeq":number,
      /**   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record.  */  
   "JobSeq":number,
      /**  Warehouse that the item on this release is being purchased for.  */  
   "WarehouseCode":string,
      /**  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  */  
   "ReceivedQty":number,
      /**  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  */  
   "ExpOverride":boolean,
      /**  Requisition which generated this PORel record.  */  
   "ReqNum":number,
      /**  Requisition line which generated this PORel record.  */  
   "ReqLine":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   "PromiseDt":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   "Confirmed":boolean,
      /**  Can be "web", "client", or "rejected"  */  
   "ConfirmVia":string,
      /**   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  */  
   "ReqChgDate":string,
      /**   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  */  
   "ReqChgQty":number,
      /**  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  */  
   "LockRel":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  */  
   "RefDisplayAccount":string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "RefCodeDesc":string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   "OrderNum":number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   "OrderLine":number,
      /**  Order Release Line created for this PO Release for the Inter-Company Trading.  */  
   "OrderRelNum":number,
      /**  Linked to sales order release.  */  
   "Linked":boolean,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  */  
   "ShippedQty":number,
      /**   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  */  
   "TranType":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  */  
   "GlbPlant":string,
      /**  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  */  
   "GlbWarehouse":string,
      /**  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  */  
   "GlbCreateJobMtl":boolean,
      /**  Shipped Date  */  
   "ShippedDate":string,
      /**  ID field to the ContainerHeader table.  */  
   "ContainerID":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "PurchasingFactorDirection":string,
      /**  This field holds the previous value of Due Date.  */  
   "PreviousDueDate":string,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  */  
   "BaseQty":number,
      /**   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   "BaseUOM":string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderNum":number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderLine":number,
      /**  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderRelNum":number,
      /**  The value of this field comes from the sales order release. Used only for Buy To Order POs.  */  
   "DropShip":boolean,
      /**  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  */  
   "ShipToNum":string,
      /**  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  */  
   "SoldToNum":number,
      /**  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  */  
   "SMIRcvdQty":number,
      /**  Contains the key value for the shipping contact.  */  
   "ShpConNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  */  
   "MangCustNum":number,
      /**  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  */  
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
      /**  One Time Shipping Country Number  */  
   "OTSCountryNum":number,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  Open Purchase Release flag  */  
   "PORelOpen":boolean,
      /**  Mapping  */  
   "Mapping":boolean,
      /**  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  */  
   "PhaseID":string,
      /**  Project Phase ID  */  
   "WBSPhaseID":string,
      /**  IsMultiRel  */  
   "IsMultiRel":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Field to track the SMIRcvdQty that has not yet been moved to stock  */  
   "SMIRemQty":number,
      /**  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  */  
   "LockQty":boolean,
      /**  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  */  
   "LockDate":boolean,
      /**  Indicates Due Date has been changed.  */  
   "DueDateChanged":boolean,
      /**  The identifier of the planning contract.  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   "LinkToContract":boolean,
      /**  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Consumed (U), Drop Shipped (D), Closed (C), Voided (V).  */  
   "Status":string,
      /**  Total quantity arrived to our site to date. In Purchasing unit of measure. This is a field maintained by the Receipt Process.  */  
   "ArrivedQty":number,
      /**  Total quantity invoiced to date. In Purchasing unit of measure. This is a field maintained by the AP Invoicing Process.  */  
   "InvoicedQty":number,
      /**  Date the PO Release is required for, this can be either from the Sales Order, Material Job, Subcontract Operation, Due Date set within Generate POSuggestions or the Purchase Order Header Date.  */  
   "NeedByDate":string,
      /**  Set to 'true' if 'NeedByDate' was derived from a valid demand.  */  
   "LockNeedByDate":boolean,
      /**  Total to date quantity that has been placed into inspection.  This is a summary maintained by the DMR process.  */  
   "InspectionQty":number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   "FailedQty":number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   "PassedQty":number,
      /**  Logical field to indicate if this record has been read by project analysis process  */  
   "ProjProcessed":boolean,
      /**  PO Line types of 'Other' have no specified warehouse / bin and what this field provides is a means of designating 'where / whom' this delivery is intended for.  */  
   "DeliverTo":string,
      /**  Taxable  */  
   "Taxable":boolean,
      /**  Indicates if this item is exempt from PO tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the PO tax info.  */  
   "TaxExempt":string,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   "NoTaxRecalc":boolean,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  When the Promise Date is changed, this is the previous PromiseDt  */  
   "ReqChgPromiseDate":string,
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
      /**  Indicates if this release is  "FIRM".  */  
   "FirmRelease":boolean,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  Name of the ship reference that is going to be stored.  */  
   "EDIShipReferenceType":string,
      /**  Data that is going to be stored as ship reference.  */  
   "EDIShipReferenceData":string,
      /**  Estimated time when the shipment will arrive.  */  
   "EDIEstimatedDockDate":string,
      /**  Quantity sent by the supplier.  */  
   "EDIShipQty":number,
      /**  Unit of Measure of the EDIShipQty.  */  
   "EDIShipQtyUOM":string,
   "ConsolidatedPO":boolean,
      /**  Is this Release related to a Contract Purchase Order?  */  
   "ContractOrder":boolean,
   "DelPoSug":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   "DocTotalDedTax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   "DocTotalSATax":number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   "DocTotalTax":number,
      /**  flag to determine whether the BTOOrderNum field can be enabled.  If a drop shipment has been Received/Shipped for this line, we cannot allow them to change the BTOOrderNum.  */  
   "EnableBTOOrderNum":boolean,
      /**  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  */  
   "EnableGLAcct":boolean,
   "EstUnitCost":number,
   "ExpDesc":string,
   "FromPOSugChg":boolean,
   "GlbPlantName":string,
   "GlbWhseName":string,
   "Inspection":boolean,
   "IUM":string,
      /**  This field will be used in the UI to Lock and unLock a release.  */  
   "Lock":boolean,
      /**  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  */  
   "MangCustID":string,
      /**  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  */  
   "MangCustName":string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   "NotCompliant":boolean,
      /**  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   "OrderHeld":boolean,
   "POHeaderApprove":boolean,
      /**  Identifies the type of PO  */  
   "POType":string,
      /**  Replicate PUM on detail  */  
   "PUM":string,
      /**  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   "PurPoint":string,
   "RefCodeStatus":string,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   "Rpt1TotalTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   "Rpt2TotalTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   "Rpt3TotalTax":number,
   "ShipToAddressList":string,
      /**  Description text of the Status field  */  
   "StatusDescription":string,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   "TotalDedTax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   "TotalSATax":number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   "TotalTax":number,
      /**   Transaction Type Description i.e. Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"), 
Stock ("PUR-STK") and Other ("PUR-UKN").  */  
   "TranTypeDesc":string,
      /**  Indicates if Glb fields should be used in place of the non-global equivalent  */  
   "UseGlbFields":boolean,
      /**  Related Supplier ID  */  
   "VendorID":string,
      /**  Related Vendor Name  */  
   "VendorName":string,
      /**  Logical indicating if the container has been shipped.  */  
   "ContainerShipped":boolean,
      /**  The formatted ship to address  */  
   "ShipToAddrFormatted":string,
      /**  ID of related Attribute Class.  */  
   "AttrClassID":string,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   "TrackInventoryAttributes":boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   "EnableDynAttrButton":boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   "AttributeQtyMismatch":boolean,
   "JobMtlSeq":number,
   "JobOprSeq":number,
   "TrackInventoryByRevision":boolean,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "ContainerHeaderPromiseDate":string,
   "ContainerHeaderDueDate":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "PlantName":string,
   "POLineRevisionNum":string,
   "POLineLineDesc":string,
   "POLineVenPartNum":string,
   "POLinePartNum":string,
   "PONumShipName":string,
   "PONumShipToConName":string,
   "ProjectIDDescription":string,
   "ReqLineLineDesc":string,
   "ReqNumShipName":string,
   "ReqNumShipToConName":string,
   "ShipToCustNumInactive":boolean,
   "ShipToCustNumBTName":string,
   "ShipToCustNumCustID":string,
   "ShipToCustNumName":string,
   "ShipToNumInactive":boolean,
   "SoldToNumCustID":string,
   "SoldToNumBTName":string,
   "SoldToNumName":string,
   "SoldToNumInactive":boolean,
   "WarehouseCodeDescription":string,
   "WBSPhaseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param WhereClausePoRel
      @param pageSize
      @param absolutePage
   */  
export interface ContainerPORelSearch_input{
   WhereClausePoRel:string,
   pageSize:number,
   absolutePage:number,
}

export interface ContainerPORelSearch_output{
   returnObj:Erp_Tablesets_PORelListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param poNum
      @param poLine
      @param poRelNum
   */  
export interface DeleteByID_input{
   poNum:number,
   poLine:number,
   poRelNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PORelListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   OpenRelease:boolean,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  */  
   VoidRelease:boolean,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   PORelNum:number,
      /**  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   DueDate:string,
      /**  Order quantity for this release in our unit of measure.  */  
   XRelQty:number,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  */  
   PurchasingFactor:number,
      /**  Order quantity for this release in vendors unit of measure.  */  
   RelQty:number,
      /**  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  */  
   JobNum:string,
      /**  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  */  
   AssemblySeq:number,
      /**   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
      /**  Warehouse that the item on this release is being purchased for.  */  
   WarehouseCode:string,
      /**  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  */  
   ReceivedQty:number,
      /**  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  */  
   ExpOverride:boolean,
      /**  Requisition which generated this PORel record.  */  
   ReqNum:number,
      /**  Requisition line which generated this PORel record.  */  
   ReqLine:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   PromiseDt:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   Confirmed:boolean,
      /**  Can be "web", "client", or "rejected"  */  
   ConfirmVia:string,
      /**   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  */  
   ReqChgDate:string,
      /**   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  */  
   ReqChgQty:number,
      /**  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  */  
   LockRel:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  */  
   RefDisplayAccount:string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   RefCodeDesc:string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   OrderLine:number,
      /**  Order Release Line created for this PO Release for the Inter-Company Trading.  */  
   OrderRelNum:number,
      /**  Linked to sales order release.  */  
   Linked:boolean,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  */  
   ShippedQty:number,
      /**   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  */  
   TranType:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  */  
   GlbPlant:string,
      /**  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  */  
   GlbWarehouse:string,
      /**  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  */  
   GlbCreateJobMtl:boolean,
      /**  Shipped Date  */  
   ShippedDate:string,
      /**  ID field to the ContainerHeader table.  */  
   ContainerID:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   PurchasingFactorDirection:string,
      /**  This field holds the previous value of Due Date.  */  
   PreviousDueDate:string,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  */  
   BaseQty:number,
      /**   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   BaseUOM:string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderNum:number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderLine:number,
      /**  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderRelNum:number,
      /**  The value of this field comes from the sales order release. Used only for Buy To Order POs.  */  
   DropShip:boolean,
      /**  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  */  
   ShipToNum:string,
      /**  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  */  
   SoldToNum:number,
      /**  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  */  
   SMIRcvdQty:number,
      /**  Contains the key value for the shipping contact.  */  
   ShpConNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  */  
   MangCustNum:number,
      /**  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  */  
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
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Open Purchase Release flag  */  
   PORelOpen:boolean,
      /**  Mapping  */  
   Mapping:boolean,
      /**  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  */  
   PhaseID:string,
      /**  Project Phase ID  */  
   WBSPhaseID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  */  
   LockQty:boolean,
      /**  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  */  
   LockDate:boolean,
   ExpDesc:string,
   EstUnitCost:number,
   IUM:string,
   Inspection:boolean,
   DelPoSug:boolean,
      /**  Replicate PUM on detail  */  
   PUM:string,
   POHeaderApprove:boolean,
      /**  Indicates if Glb fields should be used in place of the non-global equivalent  */  
   UseGlbFields:boolean,
   ConsolidatedPO:boolean,
   GlbPlantName:string,
   GlbWhseName:string,
      /**  This field will be used in the UI to Lock and unLock a release.  */  
   Lock:boolean,
      /**  Related Supplier ID  */  
   VendorID:string,
      /**  Related Vendor Name  */  
   VendorName:string,
   RefCodeStatus:string,
      /**  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   PurPoint:string,
      /**  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   OrderHeld:boolean,
      /**  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  */  
   EnableGLAcct:boolean,
      /**  Logical indicating if the container has been shipped.  */  
   ContainerShipped:boolean,
   FromPOSugChg:boolean,
      /**  Is this Release related to a Contract Purchase Order?  */  
   ContractOrder:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
      /**  Identifies the type of PO  */  
   POType:string,
      /**  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  */  
   MangCustID:string,
      /**  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  */  
   MangCustName:string,
   ShipToAddressList:string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   NotCompliant:boolean,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   AssemblySeqDescription:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  OUR internal Part number for this item.  */  
   POLinePartNum:string,
      /**  Supplier Part Number  */  
   POLineVenPartNum:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   POLineLineDesc:string,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   PONumShipToConName:string,
      /**  defaults from the company file.  */  
   PONumShipName:string,
      /**  Full description of Project Management Code.  */  
   ProjectIDDescription:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  */  
   ReqLineLineDesc:string,
      /**  defaults from the company file.  */  
   ReqNumShipName:string,
      /**  Ship to contact name.  */  
   ReqNumShipToConName:string,
      /**  The full name of the customer.  */  
   ShipToCustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   ShipToCustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   ShipToCustNumCustID:string,
      /**  The full name of the customer.  */  
   SoldToNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   SoldToNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   SoldToNumCustID:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PORelListTableset{
   PORelList:Erp_Tablesets_PORelListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PORelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   OpenRelease:boolean,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  */  
   VoidRelease:boolean,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   PORelNum:number,
      /**  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   DueDate:string,
      /**  Order quantity for this release in our unit of measure.  */  
   XRelQty:number,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  */  
   PurchasingFactor:number,
      /**  Order quantity for this release in vendors unit of measure.  */  
   RelQty:number,
      /**  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  */  
   JobNum:string,
      /**  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  */  
   AssemblySeq:number,
      /**   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
      /**  Warehouse that the item on this release is being purchased for.  */  
   WarehouseCode:string,
      /**  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  */  
   ReceivedQty:number,
      /**  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  */  
   ExpOverride:boolean,
      /**  Requisition which generated this PORel record.  */  
   ReqNum:number,
      /**  Requisition line which generated this PORel record.  */  
   ReqLine:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   PromiseDt:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   Confirmed:boolean,
      /**  Can be "web", "client", or "rejected"  */  
   ConfirmVia:string,
      /**   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  */  
   ReqChgDate:string,
      /**   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  */  
   ReqChgQty:number,
      /**  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  */  
   LockRel:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  */  
   RefDisplayAccount:string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   RefCodeDesc:string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   OrderLine:number,
      /**  Order Release Line created for this PO Release for the Inter-Company Trading.  */  
   OrderRelNum:number,
      /**  Linked to sales order release.  */  
   Linked:boolean,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  */  
   ShippedQty:number,
      /**   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  */  
   TranType:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  */  
   GlbPlant:string,
      /**  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  */  
   GlbWarehouse:string,
      /**  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  */  
   GlbCreateJobMtl:boolean,
      /**  Shipped Date  */  
   ShippedDate:string,
      /**  ID field to the ContainerHeader table.  */  
   ContainerID:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   PurchasingFactorDirection:string,
      /**  This field holds the previous value of Due Date.  */  
   PreviousDueDate:string,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  */  
   BaseQty:number,
      /**   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   BaseUOM:string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderNum:number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderLine:number,
      /**  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderRelNum:number,
      /**  The value of this field comes from the sales order release. Used only for Buy To Order POs.  */  
   DropShip:boolean,
      /**  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  */  
   ShipToNum:string,
      /**  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  */  
   SoldToNum:number,
      /**  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  */  
   SMIRcvdQty:number,
      /**  Contains the key value for the shipping contact.  */  
   ShpConNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  */  
   MangCustNum:number,
      /**  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  */  
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
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Open Purchase Release flag  */  
   PORelOpen:boolean,
      /**  Mapping  */  
   Mapping:boolean,
      /**  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  */  
   PhaseID:string,
      /**  Project Phase ID  */  
   WBSPhaseID:string,
      /**  IsMultiRel  */  
   IsMultiRel:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Field to track the SMIRcvdQty that has not yet been moved to stock  */  
   SMIRemQty:number,
      /**  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  */  
   LockQty:boolean,
      /**  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  */  
   LockDate:boolean,
      /**  Indicates Due Date has been changed.  */  
   DueDateChanged:boolean,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Consumed (U), Drop Shipped (D), Closed (C), Voided (V).  */  
   Status:string,
      /**  Total quantity arrived to our site to date. In Purchasing unit of measure. This is a field maintained by the Receipt Process.  */  
   ArrivedQty:number,
      /**  Total quantity invoiced to date. In Purchasing unit of measure. This is a field maintained by the AP Invoicing Process.  */  
   InvoicedQty:number,
      /**  Date the PO Release is required for, this can be either from the Sales Order, Material Job, Subcontract Operation, Due Date set within Generate POSuggestions or the Purchase Order Header Date.  */  
   NeedByDate:string,
      /**  Set to 'true' if 'NeedByDate' was derived from a valid demand.  */  
   LockNeedByDate:boolean,
      /**  Total to date quantity that has been placed into inspection.  This is a summary maintained by the DMR process.  */  
   InspectionQty:number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   FailedQty:number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   PassedQty:number,
      /**  Logical field to indicate if this record has been read by project analysis process  */  
   ProjProcessed:boolean,
      /**  PO Line types of 'Other' have no specified warehouse / bin and what this field provides is a means of designating 'where / whom' this delivery is intended for.  */  
   DeliverTo:string,
      /**  Taxable  */  
   Taxable:boolean,
      /**  Indicates if this item is exempt from PO tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the PO tax info.  */  
   TaxExempt:string,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   NoTaxRecalc:boolean,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  When the Promise Date is changed, this is the previous PromiseDt  */  
   ReqChgPromiseDate:string,
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
      /**  Indicates if this release is  "FIRM".  */  
   FirmRelease:boolean,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  Name of the ship reference that is going to be stored.  */  
   EDIShipReferenceType:string,
      /**  Data that is going to be stored as ship reference.  */  
   EDIShipReferenceData:string,
      /**  Estimated time when the shipment will arrive.  */  
   EDIEstimatedDockDate:string,
      /**  Quantity sent by the supplier.  */  
   EDIShipQty:number,
      /**  Unit of Measure of the EDIShipQty.  */  
   EDIShipQtyUOM:string,
   ConsolidatedPO:boolean,
      /**  Is this Release related to a Contract Purchase Order?  */  
   ContractOrder:boolean,
   DelPoSug:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   DocTotalDedTax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   DocTotalSATax:number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   DocTotalTax:number,
      /**  flag to determine whether the BTOOrderNum field can be enabled.  If a drop shipment has been Received/Shipped for this line, we cannot allow them to change the BTOOrderNum.  */  
   EnableBTOOrderNum:boolean,
      /**  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  */  
   EnableGLAcct:boolean,
   EstUnitCost:number,
   ExpDesc:string,
   FromPOSugChg:boolean,
   GlbPlantName:string,
   GlbWhseName:string,
   Inspection:boolean,
   IUM:string,
      /**  This field will be used in the UI to Lock and unLock a release.  */  
   Lock:boolean,
      /**  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  */  
   MangCustID:string,
      /**  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  */  
   MangCustName:string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   NotCompliant:boolean,
      /**  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   OrderHeld:boolean,
   POHeaderApprove:boolean,
      /**  Identifies the type of PO  */  
   POType:string,
      /**  Replicate PUM on detail  */  
   PUM:string,
      /**  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   PurPoint:string,
   RefCodeStatus:string,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   Rpt1TotalTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   Rpt2TotalTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   Rpt3TotalTax:number,
   ShipToAddressList:string,
      /**  Description text of the Status field  */  
   StatusDescription:string,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   TotalDedTax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   TotalSATax:number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   TotalTax:number,
      /**   Transaction Type Description i.e. Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"), 
Stock ("PUR-STK") and Other ("PUR-UKN").  */  
   TranTypeDesc:string,
      /**  Indicates if Glb fields should be used in place of the non-global equivalent  */  
   UseGlbFields:boolean,
      /**  Related Supplier ID  */  
   VendorID:string,
      /**  Related Vendor Name  */  
   VendorName:string,
      /**  Logical indicating if the container has been shipped.  */  
   ContainerShipped:boolean,
      /**  The formatted ship to address  */  
   ShipToAddrFormatted:string,
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   TrackInventoryAttributes:boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   EnableDynAttrButton:boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   AttributeQtyMismatch:boolean,
   JobMtlSeq:number,
   JobOprSeq:number,
   TrackInventoryByRevision:boolean,
   BitFlag:number,
   AssemblySeqDescription:string,
   ContainerHeaderPromiseDate:string,
   ContainerHeaderDueDate:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   PlantName:string,
   POLineRevisionNum:string,
   POLineLineDesc:string,
   POLineVenPartNum:string,
   POLinePartNum:string,
   PONumShipName:string,
   PONumShipToConName:string,
   ProjectIDDescription:string,
   ReqLineLineDesc:string,
   ReqNumShipName:string,
   ReqNumShipToConName:string,
   ShipToCustNumInactive:boolean,
   ShipToCustNumBTName:string,
   ShipToCustNumCustID:string,
   ShipToCustNumName:string,
   ShipToNumInactive:boolean,
   SoldToNumCustID:string,
   SoldToNumBTName:string,
   SoldToNumName:string,
   SoldToNumInactive:boolean,
   WarehouseCodeDescription:string,
   WBSPhaseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PORelSearchTableset{
   PORel:Erp_Tablesets_PORelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPORelSearchTableset{
   PORel:Erp_Tablesets_PORelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param poNum
      @param poLine
      @param poRelNum
   */  
export interface GetByID_input{
   poNum:number,
   poLine:number,
   poRelNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PORelSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PORelSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PORelSearchTableset[],
}

export interface GetCloseReleaseAt_output{
      /**  CloseReleaseAt  */  
   returnObj:string,
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListForContainer_input{
      /**  PO Release search clause  */  
   whereClause:string,
      /**  Page size  */  
   pageSize:number,
      /**  Absolute page  */  
   absolutePage:number,
}

export interface GetListForContainer_output{
   returnObj:Erp_Tablesets_PORelListTableset[],
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
export interface GetListWithPOLinePartNum_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListWithPOLinePartNum_output{
   returnObj:Erp_Tablesets_PORelListTableset[],
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
   returnObj:Erp_Tablesets_PORelListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param poNum
      @param poLine
   */  
export interface GetNewPORel_input{
   ds:Erp_Tablesets_PORelSearchTableset[],
   poNum:number,
   poLine:number,
}

export interface GetNewPORel_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PORelSearchTableset[],
}
}

   /** Required : 
      @param whereClausePoRel
      @param excludeGlobal
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsExcludeGlobal_input{
      /**  PO Release search clause  */  
   whereClausePoRel:string,
      /**  excludeGlobal  */  
   excludeGlobal:boolean,
      /**  Page size  */  
   pageSize:number,
      /**  Absolute page  */  
   absolutePage:number,
}

export interface GetRowsExcludeGlobal_output{
   returnObj:Erp_Tablesets_PORelSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePORel
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePORel:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PORelSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtPORelSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPORelSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PORelSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PORelSearchTableset[],
}
}

