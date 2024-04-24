import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.GlbPartSearchSvc
// Description: Global Part Search object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/$metadata", {
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
   Description: Get GlbPartSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbPartSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbPartRow
   */  
export function get_GlbPartSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GlbPartSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbPartSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbPartSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GlbPartSearches", {
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
   Summary: Calls GetByID to retrieve the GlbPartSearch item
   Description: Calls GetByID to retrieve the GlbPartSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbPartSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbPartNum Desc: GlbPartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbPartRow
   */  
export function get_GlbPartSearches_Company_GlbCompany_GlbPartNum(Company:string, GlbCompany:string, GlbPartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GlbPartSearches(" + Company + "," + GlbCompany + "," + GlbPartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlbPartSearch for the service
   Description: Calls UpdateExt to update GlbPartSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbPartSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbPartNum Desc: GlbPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlbPartSearches_Company_GlbCompany_GlbPartNum(Company:string, GlbCompany:string, GlbPartNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GlbPartSearches(" + Company + "," + GlbCompany + "," + GlbPartNum + ")", {
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
   Summary: Call UpdateExt to delete GlbPartSearch item
   Description: Call UpdateExt to delete GlbPartSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbPartSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbPartNum Desc: GlbPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlbPartSearches_Company_GlbCompany_GlbPartNum(Company:string, GlbCompany:string, GlbPartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GlbPartSearches(" + Company + "," + GlbCompany + "," + GlbPartNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbPartListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPartListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPartListRow)
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
export function get_GetRows(whereClauseGlbPart:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGlbPart!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlbPart=" + whereClauseGlbPart
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(glbCompany:string, glbPartNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof glbCompany!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glbCompany=" + glbCompany
   }
   if(typeof glbPartNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glbPartNum=" + glbPartNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewGlbPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlbPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GetNewGlbPart", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPartListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbPartListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPartRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbPartRow[],
}

export interface Erp_Tablesets_GlbPartListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  */  
   "SearchWord":string,
      /**  Describes the Part.  This field can not be blank.  */  
   "PartDescription":string,
   "ClassID":string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   "IUM":string,
      /**  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  */  
   "PUM":string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   "TypeCode":string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   "NonStock":boolean,
      /**  This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.
Formula: Issue Qty * Conversion Factor = Purchased Qty.  */  
   "PurchasingFactor":number,
      /**  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  */  
   "UnitPrice":number,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PricePerCode":string,
      /**  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  */  
   "InternalUnitPrice":number,
      /**  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  */  
   "InternalPricePerCode":string,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   "ProdCode":string,
      /**  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  */  
   "MfgComment":string,
      /**  Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget. To be view-as EDITOR widget.  */  
   "PurComment":string,
      /**  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  */  
   "CostMethod":string,
      /**  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   "TaxCatID":string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   "InActive":boolean,
      /**  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  */  
   "LowLevelCode":number,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "TrackLots":boolean,
      /**  Indicates if this part is dimension tracked  */  
   "TrackDimension":boolean,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   "DefaultDim":string,
      /**  Indicates if this part is serial number tracked  */  
   "TrackSerialNum":boolean,
      /**  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  */  
   "CommodityCode":string,
      /**  Unique code for the Warranty for this part  */  
   "WarrantyCode":string,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   "PhantomBOM":boolean,
      /**  The Selling Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Sales Order entry as the default on line item details.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  The material burden rate for this part.  */  
   "MtlBurRate":number,
      /**  The Part's Unit Net Weight.  */  
   "NetWeight":number,
      /**   NOTE: NOT IMPLEMENTED ON INITIAL 5.0.300 RELEASE.
if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  */  
   "UsePartRev":boolean,
      /**  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  */  
   "PartsPerContainer":number,
      /**  Part's length.  */  
   "PartLength":number,
      /**  Part's width.  */  
   "PartWidth":number,
      /**  Part's Height.  */  
   "PartHeight":number,
      /**  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  */  
   "LotShelfLife":number,
      /**  This is a Web saleable part  */  
   "WebPart":boolean,
      /**  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  */  
   "RunOut":boolean,
      /**  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  */  
   "SubPart":string,
      /**  Part's diameter.  */  
   "Diameter":number,
      /**  Part's gravity.  */  
   "Gravity":number,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   "OnHold":boolean,
      /**  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  */  
   "OnHoldDate":string,
      /**   The reason code that links to a Reason master record, which indicates why the part has been placed on hold.
Valid only when Part.OnHold = Yes.  */  
   "OnHoldReasonCode":string,
   "AnalysisCode":string,
      /**  Owner Company Identifier.  */  
   "GlbCompany":string,
      /**  The Owner's PartNum field identifies the Part and is used as the primary key.  */  
   "GlbPartNum":string,
      /**  MtlAnalysisCode  */  
   "MtlAnalysisCode":string,
      /**  Marks the Part as a global Part, available to be sent out to other companies  */  
   "GlobalPart":boolean,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  This value is used to calculate the Supplementary Units for the Intrastat.  */  
   "ISSuppUnitsFactor":number,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   "OldCompany":string,
      /**  The Original Owner's PartNum field identifies the Part and is used as the primary key.   NOT CURRENTLY IN USE  */  
   "OldPartNum":string,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
   "SNPrefix":string,
      /**  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  */  
   "ImageFileName":string,
   "SNFormat":string,
   "SNBaseDataType":string,
      /**  This field contains the Intrastat Country of Origin Code from the Country table.  */  
   "ISOrigCountry":string,
   "Constrained":boolean,
   "UPCCode1":string,
   "UPCCode2":string,
   "UPCCode3":string,
   "EDICode":string,
      /**  Indicates if the user chose to skip this record when linking global parts.  The user can come back at a later time and choose to link a skipped part if they need to.  */  
   "Skipped":boolean,
   "ConsolidatedPurchasing":boolean,
   "WebInStock":boolean,
      /**  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "PurchasingFactorDirection":string,
      /**  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
   "MDPV":number,
   "ReturnableContainer":string,
   "NetVolume":number,
   "RecDocReq":boolean,
   "ShipDocReq":boolean,
   "QtyBearing":boolean,
   "AESExp":string,
   "ECCNNumber":string,
   "ExpLicNumber":string,
   "ExpLicType":string,
   "HazClass":string,
   "HazGvrnmtID":string,
   "HazItem":boolean,
   "HazPackInstr":string,
   "HazSub":string,
   "HazTechName":string,
   "HTS":string,
   "NAFTAOrigCountry":string,
   "NAFTAPref":string,
   "NAFTAProd":string,
   "SchedBcode":string,
   "UseHTSDesc":boolean,
   "OwnershipStatus":string,
   "RCOverThreshold":number,
   "RCUnderThreshold":number,
   "RevChargeMethod":string,
   "UOMClassID":string,
      /**  This is the ID by which the user will reference a particular serial number format mask.  */  
   "SNMask":string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   "SNMaskExample":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  */  
   "SNMaskPrefix":string,
      /**  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  */  
   "SNMaskSuffix":string,
   "LotAppendDate":string,
   "LotBatch":boolean,
   "LotBeforeDt":boolean,
   "LotCureDt":boolean,
   "LotDigits":number,
   "LotExpDt":boolean,
   "LotFirmware":boolean,
   "LotHeat":boolean,
   "LotLeadingZeros":boolean,
   "LotMfgBatch":boolean,
   "LotMfgDt":boolean,
   "LotMfgLot":boolean,
   "LotNxtNum":number,
   "LotPrefix":string,
   "LotSeqID":string,
   "LotUseGlobalSeq":boolean,
   "NetVolumeUOM":string,
   "NetWeightUOM":string,
   "SNLastUsedSeq":string,
   "UseMaskSeq":boolean,
   "BuyToOrder":boolean,
   "DropShip":boolean,
   "ExtConfig":boolean,
   "IsConfigured":boolean,
   "RefCategory":string,
   "CSFCJ5":boolean,
   "CSFLMW":boolean,
   "GrossWeight":number,
   "GrossWeightUOM":string,
   "BasePartNum":string,
   "FSAssetClassCode":string,
   "FSPricePerCode":string,
   "FSSalesUnitPrice":number,
   "RcvInspectionReq":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DispPartNum":string,
   "LinkPartNum":string,
   "TypeCodeDescription":string,
   "ProdCodeDescription":string,
   "StockPart":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbPartRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  */  
   "SearchWord":string,
      /**  Describes the Part.  This field can not be blank.  */  
   "PartDescription":string,
   "ClassID":string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   "IUM":string,
      /**  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  */  
   "PUM":string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   "TypeCode":string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   "NonStock":boolean,
      /**  This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.
Formula: Issue Qty * Conversion Factor = Purchased Qty.  */  
   "PurchasingFactor":number,
      /**  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  */  
   "UnitPrice":number,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PricePerCode":string,
      /**  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  */  
   "InternalUnitPrice":number,
      /**  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  */  
   "InternalPricePerCode":string,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   "ProdCode":string,
      /**  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  */  
   "MfgComment":string,
      /**  Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget. To be view-as EDITOR widget.  */  
   "PurComment":string,
      /**  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  */  
   "CostMethod":string,
      /**  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   "TaxCatID":string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   "InActive":boolean,
      /**  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  */  
   "LowLevelCode":number,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "TrackLots":boolean,
      /**  Indicates if this part is dimension tracked  */  
   "TrackDimension":boolean,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   "DefaultDim":string,
      /**  Indicates if this part is serial number tracked  */  
   "TrackSerialNum":boolean,
      /**  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  */  
   "CommodityCode":string,
      /**  Unique code for the Warranty for this part  */  
   "WarrantyCode":string,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   "PhantomBOM":boolean,
      /**  The Selling Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Sales Order entry as the default on line item details.  */  
   "SalesUM":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "SellingFactor":number,
      /**  The material burden rate for this part.  */  
   "MtlBurRate":number,
      /**  The Part's Unit Net Weight.  */  
   "NetWeight":number,
      /**   NOTE: NOT IMPLEMENTED ON INITIAL 5.0.300 RELEASE.
if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  */  
   "UsePartRev":boolean,
      /**  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  */  
   "PartsPerContainer":number,
      /**  Part's length.  */  
   "PartLength":number,
      /**  Part's width.  */  
   "PartWidth":number,
      /**  Part's Height.  */  
   "PartHeight":number,
      /**  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  */  
   "LotShelfLife":number,
      /**  This is a Web saleable part  */  
   "WebPart":boolean,
      /**  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  */  
   "RunOut":boolean,
      /**  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  */  
   "SubPart":string,
      /**  Part's diameter.  */  
   "Diameter":number,
      /**  Part's gravity.  */  
   "Gravity":number,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   "OnHold":boolean,
      /**  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  */  
   "OnHoldDate":string,
      /**   The reason code that links to a Reason master record, which indicates why the part has been placed on hold.
Valid only when Part.OnHold = Yes.  */  
   "OnHoldReasonCode":string,
   "AnalysisCode":string,
      /**  Owner Company Identifier.  */  
   "GlbCompany":string,
      /**  The Owner's PartNum field identifies the Part and is used as the primary key.  */  
   "GlbPartNum":string,
      /**  MtlAnalysisCode  */  
   "MtlAnalysisCode":string,
      /**  Marks the Part as a global Part, available to be sent out to other companies  */  
   "GlobalPart":boolean,
      /**  Disable this record from receiving global updates  */  
   "GlobalLock":boolean,
      /**  This value is used to calculate the Supplementary Units for the Intrastat.  */  
   "ISSuppUnitsFactor":number,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   "OldCompany":string,
      /**  The Original Owner's PartNum field identifies the Part and is used as the primary key.   NOT CURRENTLY IN USE  */  
   "OldPartNum":string,
      /**  Holds the internal object id of pdm parts.  */  
   "PDMObjID":string,
   "SNPrefix":string,
      /**  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  */  
   "ImageFileName":string,
   "SNFormat":string,
   "SNBaseDataType":string,
      /**  This field contains the Intrastat Country of Origin Code from the Country table.  */  
   "ISOrigCountry":string,
   "Constrained":boolean,
   "UPCCode1":string,
   "UPCCode2":string,
   "UPCCode3":string,
   "EDICode":string,
      /**  Indicates if the user chose to skip this record when linking global parts.  The user can come back at a later time and choose to link a skipped part if they need to.  */  
   "Skipped":boolean,
   "ConsolidatedPurchasing":boolean,
   "WebInStock":boolean,
      /**  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "PurchasingFactorDirection":string,
      /**  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "SellingFactorDirection":string,
   "MDPV":number,
   "ReturnableContainer":string,
   "NetVolume":number,
   "RecDocReq":boolean,
   "ShipDocReq":boolean,
   "QtyBearing":boolean,
   "AESExp":string,
   "ECCNNumber":string,
   "ExpLicNumber":string,
   "ExpLicType":string,
   "HazClass":string,
   "HazGvrnmtID":string,
   "HazItem":boolean,
   "HazPackInstr":string,
   "HazSub":string,
   "HazTechName":string,
   "HTS":string,
   "NAFTAOrigCountry":string,
   "NAFTAPref":string,
   "NAFTAProd":string,
   "SchedBcode":string,
   "UseHTSDesc":boolean,
   "OwnershipStatus":string,
   "RCOverThreshold":number,
   "RCUnderThreshold":number,
   "RevChargeMethod":string,
   "UOMClassID":string,
      /**  This is the ID by which the user will reference a particular serial number format mask.  */  
   "SNMask":string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   "SNMaskExample":string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  */  
   "SNMaskPrefix":string,
      /**  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  */  
   "SNMaskSuffix":string,
   "LotAppendDate":string,
   "LotBatch":boolean,
   "LotBeforeDt":boolean,
   "LotCureDt":boolean,
   "LotDigits":number,
   "LotExpDt":boolean,
   "LotFirmware":boolean,
   "LotHeat":boolean,
   "LotLeadingZeros":boolean,
   "LotMfgBatch":boolean,
   "LotMfgDt":boolean,
   "LotMfgLot":boolean,
   "LotNxtNum":number,
   "LotPrefix":string,
   "LotSeqID":string,
   "LotUseGlobalSeq":boolean,
   "NetVolumeUOM":string,
   "NetWeightUOM":string,
   "SNLastUsedSeq":string,
   "UseMaskSeq":boolean,
   "BuyToOrder":boolean,
   "DropShip":boolean,
   "ExtConfig":boolean,
   "IsConfigured":boolean,
   "RefCategory":string,
   "CSFCJ5":boolean,
   "CSFLMW":boolean,
   "GrossWeight":number,
   "GrossWeightUOM":string,
   "BasePartNum":string,
   "FSAssetClassCode":string,
   "FSPricePerCode":string,
   "FSSalesUnitPrice":number,
   "RcvInspectionReq":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ISRegion  */  
   "ISRegion":string,
      /**  INChapterID  */  
   "INChapterID":string,
      /**  EstimateID  */  
   "EstimateID":string,
      /**  EstimateOrPlan  */  
   "EstimateOrPlan":string,
      /**  DiffPrc2PrchUOM  */  
   "DiffPrc2PrchUOM":boolean,
      /**  DupOnJobCrt  */  
   "DupOnJobCrt":boolean,
      /**  PricingFactor  */  
   "PricingFactor":number,
      /**  PricingUOM  */  
   "PricingUOM":string,
      /**  MobilePart  */  
   "MobilePart":boolean,
      /**  AGUseGoodMark  */  
   "AGUseGoodMark":boolean,
      /**  AGProductMark  */  
   "AGProductMark":boolean,
      /**  CSF Peru -  SUNAT Type  */  
   "PESUNATType":string,
      /**  PESUNATUOM  */  
   "PESUNATUOM":string,
      /**  DEIsServices  */  
   "DEIsServices":boolean,
      /**  DEIsSecurityFinancialDerivative  */  
   "DEIsSecurityFinancialDerivative":boolean,
      /**  DEInternationalSecuritiesID  */  
   "DEInternationalSecuritiesID":string,
      /**  LinkToContract  */  
   "LinkToContract":boolean,
      /**  DEIsInvestment  */  
   "DEIsInvestment":boolean,
      /**  DEPayStatCode  */  
   "DEPayStatCode":string,
      /**  DEDenomination  */  
   "DEDenomination":string,
      /**  PartLengthWidthHeightUM  */  
   "PartLengthWidthHeightUM":string,
      /**  DiameterUM  */  
   "DiameterUM":string,
      /**  DiameterInside  */  
   "DiameterInside":number,
      /**  DiameterOutside  */  
   "DiameterOutside":number,
      /**  ThicknessUM  */  
   "ThicknessUM":string,
      /**  Thickness  */  
   "Thickness":number,
      /**  ThicknessMax  */  
   "ThicknessMax":number,
      /**  Durometer  */  
   "Durometer":string,
      /**  Specification  */  
   "Specification":string,
      /**  EngineeringAlert  */  
   "EngineeringAlert":string,
      /**  Condition  */  
   "Condition":string,
      /**  IsCompliant  */  
   "IsCompliant":boolean,
      /**  IsRestricted  */  
   "IsRestricted":boolean,
      /**  IsSafetyItem  */  
   "IsSafetyItem":boolean,
      /**  CommercialBrand  */  
   "CommercialBrand":string,
      /**  CommercialSubBrand  */  
   "CommercialSubBrand":string,
      /**  CommercialCategory  */  
   "CommercialCategory":string,
      /**  CommercialSubCategory  */  
   "CommercialSubCategory":string,
      /**  CommercialStyle  */  
   "CommercialStyle":string,
      /**  CommercialSize1  */  
   "CommercialSize1":string,
      /**  CommercialSize2  */  
   "CommercialSize2":string,
      /**  CommercialColor  */  
   "CommercialColor":string,
      /**  IsGiftCard  */  
   "IsGiftCard":boolean,
      /**  PhotoFile  */  
   "PhotoFile":string,
      /**  PartPhotoExists  */  
   "PartPhotoExists":boolean,
      /**  CommentText  */  
   "CommentText":string,
      /**  PartSpecificPackingUOM  */  
   "PartSpecificPackingUOM":boolean,
      /**  ImageID  */  
   "ImageID":string,
      /**  CNSpecification  */  
   "CNSpecification":string,
      /**  SyncToExternalCRM  */  
   "SyncToExternalCRM":boolean,
      /**  ExternalCRMPartID  */  
   "ExternalCRMPartID":string,
      /**  ExternalCRMLastSync  */  
   "ExternalCRMLastSync":string,
      /**  ExternalCRMSyncRequired  */  
   "ExternalCRMSyncRequired":boolean,
      /**  PESUNATTypeCode  */  
   "PESUNATTypeCode":string,
      /**  PESUNATUOMCode  */  
   "PESUNATUOMCode":string,
      /**  CNCodeVersion  */  
   "CNCodeVersion":string,
      /**  CNTaxCategoryCode  */  
   "CNTaxCategoryCode":string,
      /**  CNHasPreferentialTreatment  */  
   "CNHasPreferentialTreatment":boolean,
      /**  CNPreferentialTreatmentContent  */  
   "CNPreferentialTreatmentContent":string,
      /**  CNZeroTaxRateMark  */  
   "CNZeroTaxRateMark":string,
      /**  SubLevelCode  */  
   "SubLevelCode":number,
      /**  User the part was created by  */  
   "CreatedBy":string,
      /**  Date the part was created on  */  
   "CreatedOn":string,
      /**  AttBatch  */  
   "AttBatch":string,
      /**  AttMfgBatch  */  
   "AttMfgBatch":string,
      /**  AttMfgLot  */  
   "AttMfgLot":string,
      /**  AttHeat  */  
   "AttHeat":string,
      /**  AttFirmware  */  
   "AttFirmware":string,
      /**  AttBeforeDt  */  
   "AttBeforeDt":string,
      /**  AttMfgDt  */  
   "AttMfgDt":string,
      /**  AttCureDt  */  
   "AttCureDt":string,
      /**  AttExpDt  */  
   "AttExpDt":string,
      /**  DeferManualEntry  */  
   "DeferManualEntry":boolean,
      /**  DeferPurchaseReceipt  */  
   "DeferPurchaseReceipt":boolean,
      /**  DeferJobReceipt  */  
   "DeferJobReceipt":boolean,
      /**  DeferInspection  */  
   "DeferInspection":boolean,
      /**  DeferQtyAdjustment  */  
   "DeferQtyAdjustment":boolean,
      /**  DeferInventoryMove  */  
   "DeferInventoryMove":boolean,
      /**  DeferShipments  */  
   "DeferShipments":boolean,
      /**  DeferInventoryCounts  */  
   "DeferInventoryCounts":boolean,
      /**  DeferAssetDisposal  */  
   "DeferAssetDisposal":boolean,
      /**  DeferReturnMaterials  */  
   "DeferReturnMaterials":boolean,
      /**  MXProdServCode  */  
   "MXProdServCode":string,
      /**  Date/Time when the Part record was last updated.  */  
   "ChangedOn":string,
      /**  MXCustomsDuty  */  
   "MXCustomsDuty":string,
      /**  SendToFSA  */  
   "SendToFSA":boolean,
      /**  ExternalMESSyncRequired  */  
   "ExternalMESSyncRequired":boolean,
      /**  ExternalMESLastSync  */  
   "ExternalMESLastSync":string,
      /**  FSAItem  */  
   "FSAItem":boolean,
      /**  FSAEquipment  */  
   "FSAEquipment":boolean,
      /**  BOLClass  */  
   "BOLClass":string,
      /**  FairMarketValue  */  
   "FairMarketValue":number,
      /**  SAFTProdCategory  */  
   "SAFTProdCategory":string,
      /**  AttrClassID  */  
   "AttrClassID":string,
      /**  LocationIDNumReq  */  
   "LocationIDNumReq":boolean,
      /**  LocationTrackInv  */  
   "LocationTrackInv":boolean,
      /**  LocationMtlView  */  
   "LocationMtlView":boolean,
      /**  LCNRVReporting  */  
   "LCNRVReporting":boolean,
      /**  LCNRVEstimatedUnitPrice  */  
   "LCNRVEstimatedUnitPrice":number,
      /**  MXCustomsUMFrom  */  
   "MXCustomsUMFrom":string,
      /**  LocationFormatID  */  
   "LocationFormatID":string,
      /**  IsServices  */  
   "IsServices":boolean,
      /**  PEDetrGoodServiceCode  */  
   "PEDetrGoodServiceCode":string,
      /**  PEProductServiceCode  */  
   "PEProductServiceCode":string,
      /**  DualUOMClassID  */  
   "DualUOMClassID":string,
      /**  CNProductName  */  
   "CNProductName":string,
      /**  CNWeight  */  
   "CNWeight":number,
      /**  CNWeightUOM  */  
   "CNWeightUOM":string,
      /**  CNBonded  */  
   "CNBonded":boolean,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   "TrackInventoryAttributes":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "DefaultAttributeSetID":number,
      /**  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttISOrigCountry":string,
      /**  ExternalSchemeID  */  
   "ExternalSchemeID":string,
      /**  ExternalID  */  
   "ExternalID":string,
      /**  CommoditySchemeID  */  
   "CommoditySchemeID":string,
      /**  CommoditySchemeVersion  */  
   "CommoditySchemeVersion":string,
      /**  TrackInventoryByRevision  */  
   "TrackInventoryByRevision":boolean,
      /**  PlanningByRevision  */  
   "PlanningByRevision":boolean,
      /**  RcvInspectionReqPart  */  
   "RcvInspectionReqPart":string,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  FSMPartType  */  
   "FSMPartType":number,
      /**  UserChar1  */  
   "UserChar1":string,
      /**  UserChar2  */  
   "UserChar2":string,
      /**  UserChar3  */  
   "UserChar3":string,
      /**  UserChar4  */  
   "UserChar4":string,
      /**  UserDate1  */  
   "UserDate1":string,
      /**  UserDate2  */  
   "UserDate2":string,
      /**  UserDate3  */  
   "UserDate3":string,
      /**  UserDate4  */  
   "UserDate4":string,
      /**  UserDecimal1  */  
   "UserDecimal1":number,
      /**  UserDecimal2  */  
   "UserDecimal2":number,
   "LinkPartNum":string,
      /**  UserDecimal3  */  
   "UserDecimal3":number,
   "ProdCodeDescription":string,
      /**  UserDecimal4  */  
   "UserDecimal4":number,
   "StockPart":boolean,
   "TypeCodeDescription":string,
      /**  UserInteger1  */  
   "UserInteger1":number,
      /**  UserInteger2  */  
   "UserInteger2":number,
   "DispPartNum":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param glbCompany
      @param glbPartNum
   */  
export interface DeleteByID_input{
   glbCompany:string,
   glbPartNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GlbPartListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  */  
   SearchWord:string,
      /**  Describes the Part.  This field can not be blank.  */  
   PartDescription:string,
   ClassID:string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   IUM:string,
      /**  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  */  
   PUM:string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   TypeCode:string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   NonStock:boolean,
      /**  This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.
Formula: Issue Qty * Conversion Factor = Purchased Qty.  */  
   PurchasingFactor:number,
      /**  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  */  
   UnitPrice:number,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PricePerCode:string,
      /**  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  */  
   InternalUnitPrice:number,
      /**  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  */  
   InternalPricePerCode:string,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   ProdCode:string,
      /**  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  */  
   MfgComment:string,
      /**  Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget. To be view-as EDITOR widget.  */  
   PurComment:string,
      /**  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  */  
   CostMethod:string,
      /**  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   InActive:boolean,
      /**  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  */  
   LowLevelCode:number,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   TrackLots:boolean,
      /**  Indicates if this part is dimension tracked  */  
   TrackDimension:boolean,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   DefaultDim:string,
      /**  Indicates if this part is serial number tracked  */  
   TrackSerialNum:boolean,
      /**  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  */  
   CommodityCode:string,
      /**  Unique code for the Warranty for this part  */  
   WarrantyCode:string,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   PhantomBOM:boolean,
      /**  The Selling Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Sales Order entry as the default on line item details.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  The material burden rate for this part.  */  
   MtlBurRate:number,
      /**  The Part's Unit Net Weight.  */  
   NetWeight:number,
      /**   NOTE: NOT IMPLEMENTED ON INITIAL 5.0.300 RELEASE.
if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  */  
   UsePartRev:boolean,
      /**  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  */  
   PartsPerContainer:number,
      /**  Part's length.  */  
   PartLength:number,
      /**  Part's width.  */  
   PartWidth:number,
      /**  Part's Height.  */  
   PartHeight:number,
      /**  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  */  
   LotShelfLife:number,
      /**  This is a Web saleable part  */  
   WebPart:boolean,
      /**  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  */  
   RunOut:boolean,
      /**  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  */  
   SubPart:string,
      /**  Part's diameter.  */  
   Diameter:number,
      /**  Part's gravity.  */  
   Gravity:number,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   OnHold:boolean,
      /**  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  */  
   OnHoldDate:string,
      /**   The reason code that links to a Reason master record, which indicates why the part has been placed on hold.
Valid only when Part.OnHold = Yes.  */  
   OnHoldReasonCode:string,
   AnalysisCode:string,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  The Owner's PartNum field identifies the Part and is used as the primary key.  */  
   GlbPartNum:string,
      /**  MtlAnalysisCode  */  
   MtlAnalysisCode:string,
      /**  Marks the Part as a global Part, available to be sent out to other companies  */  
   GlobalPart:boolean,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  This value is used to calculate the Supplementary Units for the Intrastat.  */  
   ISSuppUnitsFactor:number,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  The Original Owner's PartNum field identifies the Part and is used as the primary key.   NOT CURRENTLY IN USE  */  
   OldPartNum:string,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
   SNPrefix:string,
      /**  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  */  
   ImageFileName:string,
   SNFormat:string,
   SNBaseDataType:string,
      /**  This field contains the Intrastat Country of Origin Code from the Country table.  */  
   ISOrigCountry:string,
   Constrained:boolean,
   UPCCode1:string,
   UPCCode2:string,
   UPCCode3:string,
   EDICode:string,
      /**  Indicates if the user chose to skip this record when linking global parts.  The user can come back at a later time and choose to link a skipped part if they need to.  */  
   Skipped:boolean,
   ConsolidatedPurchasing:boolean,
   WebInStock:boolean,
      /**  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   PurchasingFactorDirection:string,
      /**  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
   MDPV:number,
   ReturnableContainer:string,
   NetVolume:number,
   RecDocReq:boolean,
   ShipDocReq:boolean,
   QtyBearing:boolean,
   AESExp:string,
   ECCNNumber:string,
   ExpLicNumber:string,
   ExpLicType:string,
   HazClass:string,
   HazGvrnmtID:string,
   HazItem:boolean,
   HazPackInstr:string,
   HazSub:string,
   HazTechName:string,
   HTS:string,
   NAFTAOrigCountry:string,
   NAFTAPref:string,
   NAFTAProd:string,
   SchedBcode:string,
   UseHTSDesc:boolean,
   OwnershipStatus:string,
   RCOverThreshold:number,
   RCUnderThreshold:number,
   RevChargeMethod:string,
   UOMClassID:string,
      /**  This is the ID by which the user will reference a particular serial number format mask.  */  
   SNMask:string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   SNMaskExample:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  */  
   SNMaskPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  */  
   SNMaskSuffix:string,
   LotAppendDate:string,
   LotBatch:boolean,
   LotBeforeDt:boolean,
   LotCureDt:boolean,
   LotDigits:number,
   LotExpDt:boolean,
   LotFirmware:boolean,
   LotHeat:boolean,
   LotLeadingZeros:boolean,
   LotMfgBatch:boolean,
   LotMfgDt:boolean,
   LotMfgLot:boolean,
   LotNxtNum:number,
   LotPrefix:string,
   LotSeqID:string,
   LotUseGlobalSeq:boolean,
   NetVolumeUOM:string,
   NetWeightUOM:string,
   SNLastUsedSeq:string,
   UseMaskSeq:boolean,
   BuyToOrder:boolean,
   DropShip:boolean,
   ExtConfig:boolean,
   IsConfigured:boolean,
   RefCategory:string,
   CSFCJ5:boolean,
   CSFLMW:boolean,
   GrossWeight:number,
   GrossWeightUOM:string,
   BasePartNum:string,
   FSAssetClassCode:string,
   FSPricePerCode:string,
   FSSalesUnitPrice:number,
   RcvInspectionReq:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DispPartNum:string,
   LinkPartNum:string,
   TypeCodeDescription:string,
   ProdCodeDescription:string,
   StockPart:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbPartListTableset{
   GlbPartList:Erp_Tablesets_GlbPartListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlbPartRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  */  
   SearchWord:string,
      /**  Describes the Part.  This field can not be blank.  */  
   PartDescription:string,
   ClassID:string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   IUM:string,
      /**  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  */  
   PUM:string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   TypeCode:string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   NonStock:boolean,
      /**  This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.
Formula: Issue Qty * Conversion Factor = Purchased Qty.  */  
   PurchasingFactor:number,
      /**  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  */  
   UnitPrice:number,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PricePerCode:string,
      /**  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  */  
   InternalUnitPrice:number,
      /**  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  */  
   InternalPricePerCode:string,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   ProdCode:string,
      /**  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  */  
   MfgComment:string,
      /**  Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget. To be view-as EDITOR widget.  */  
   PurComment:string,
      /**  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  */  
   CostMethod:string,
      /**  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   InActive:boolean,
      /**  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  */  
   LowLevelCode:number,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   TrackLots:boolean,
      /**  Indicates if this part is dimension tracked  */  
   TrackDimension:boolean,
      /**  Default dimension code for the part.  Set by selecting a PartDim record as default.  */  
   DefaultDim:string,
      /**  Indicates if this part is serial number tracked  */  
   TrackSerialNum:boolean,
      /**  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  */  
   CommodityCode:string,
      /**  Unique code for the Warranty for this part  */  
   WarrantyCode:string,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   PhantomBOM:boolean,
      /**  The Selling Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Sales Order entry as the default on line item details.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  The material burden rate for this part.  */  
   MtlBurRate:number,
      /**  The Part's Unit Net Weight.  */  
   NetWeight:number,
      /**   NOTE: NOT IMPLEMENTED ON INITIAL 5.0.300 RELEASE.
if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  */  
   UsePartRev:boolean,
      /**  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  */  
   PartsPerContainer:number,
      /**  Part's length.  */  
   PartLength:number,
      /**  Part's width.  */  
   PartWidth:number,
      /**  Part's Height.  */  
   PartHeight:number,
      /**  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  */  
   LotShelfLife:number,
      /**  This is a Web saleable part  */  
   WebPart:boolean,
      /**  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  */  
   RunOut:boolean,
      /**  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  */  
   SubPart:string,
      /**  Part's diameter.  */  
   Diameter:number,
      /**  Part's gravity.  */  
   Gravity:number,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   OnHold:boolean,
      /**  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  */  
   OnHoldDate:string,
      /**   The reason code that links to a Reason master record, which indicates why the part has been placed on hold.
Valid only when Part.OnHold = Yes.  */  
   OnHoldReasonCode:string,
   AnalysisCode:string,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  The Owner's PartNum field identifies the Part and is used as the primary key.  */  
   GlbPartNum:string,
      /**  MtlAnalysisCode  */  
   MtlAnalysisCode:string,
      /**  Marks the Part as a global Part, available to be sent out to other companies  */  
   GlobalPart:boolean,
      /**  Disable this record from receiving global updates  */  
   GlobalLock:boolean,
      /**  This value is used to calculate the Supplementary Units for the Intrastat.  */  
   ISSuppUnitsFactor:number,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  The Original Owner's PartNum field identifies the Part and is used as the primary key.   NOT CURRENTLY IN USE  */  
   OldPartNum:string,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
   SNPrefix:string,
      /**  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  */  
   ImageFileName:string,
   SNFormat:string,
   SNBaseDataType:string,
      /**  This field contains the Intrastat Country of Origin Code from the Country table.  */  
   ISOrigCountry:string,
   Constrained:boolean,
   UPCCode1:string,
   UPCCode2:string,
   UPCCode3:string,
   EDICode:string,
      /**  Indicates if the user chose to skip this record when linking global parts.  The user can come back at a later time and choose to link a skipped part if they need to.  */  
   Skipped:boolean,
   ConsolidatedPurchasing:boolean,
   WebInStock:boolean,
      /**  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   PurchasingFactorDirection:string,
      /**  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
   MDPV:number,
   ReturnableContainer:string,
   NetVolume:number,
   RecDocReq:boolean,
   ShipDocReq:boolean,
   QtyBearing:boolean,
   AESExp:string,
   ECCNNumber:string,
   ExpLicNumber:string,
   ExpLicType:string,
   HazClass:string,
   HazGvrnmtID:string,
   HazItem:boolean,
   HazPackInstr:string,
   HazSub:string,
   HazTechName:string,
   HTS:string,
   NAFTAOrigCountry:string,
   NAFTAPref:string,
   NAFTAProd:string,
   SchedBcode:string,
   UseHTSDesc:boolean,
   OwnershipStatus:string,
   RCOverThreshold:number,
   RCUnderThreshold:number,
   RevChargeMethod:string,
   UOMClassID:string,
      /**  This is the ID by which the user will reference a particular serial number format mask.  */  
   SNMask:string,
      /**  BL-generated example of the serial number mask if SNBaseDataType = Mask.  */  
   SNMaskExample:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  */  
   SNMaskPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  */  
   SNMaskSuffix:string,
   LotAppendDate:string,
   LotBatch:boolean,
   LotBeforeDt:boolean,
   LotCureDt:boolean,
   LotDigits:number,
   LotExpDt:boolean,
   LotFirmware:boolean,
   LotHeat:boolean,
   LotLeadingZeros:boolean,
   LotMfgBatch:boolean,
   LotMfgDt:boolean,
   LotMfgLot:boolean,
   LotNxtNum:number,
   LotPrefix:string,
   LotSeqID:string,
   LotUseGlobalSeq:boolean,
   NetVolumeUOM:string,
   NetWeightUOM:string,
   SNLastUsedSeq:string,
   UseMaskSeq:boolean,
   BuyToOrder:boolean,
   DropShip:boolean,
   ExtConfig:boolean,
   IsConfigured:boolean,
   RefCategory:string,
   CSFCJ5:boolean,
   CSFLMW:boolean,
   GrossWeight:number,
   GrossWeightUOM:string,
   BasePartNum:string,
   FSAssetClassCode:string,
   FSPricePerCode:string,
   FSSalesUnitPrice:number,
   RcvInspectionReq:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ISRegion  */  
   ISRegion:string,
      /**  INChapterID  */  
   INChapterID:string,
      /**  EstimateID  */  
   EstimateID:string,
      /**  EstimateOrPlan  */  
   EstimateOrPlan:string,
      /**  DiffPrc2PrchUOM  */  
   DiffPrc2PrchUOM:boolean,
      /**  DupOnJobCrt  */  
   DupOnJobCrt:boolean,
      /**  PricingFactor  */  
   PricingFactor:number,
      /**  PricingUOM  */  
   PricingUOM:string,
      /**  MobilePart  */  
   MobilePart:boolean,
      /**  AGUseGoodMark  */  
   AGUseGoodMark:boolean,
      /**  AGProductMark  */  
   AGProductMark:boolean,
      /**  CSF Peru -  SUNAT Type  */  
   PESUNATType:string,
      /**  PESUNATUOM  */  
   PESUNATUOM:string,
      /**  DEIsServices  */  
   DEIsServices:boolean,
      /**  DEIsSecurityFinancialDerivative  */  
   DEIsSecurityFinancialDerivative:boolean,
      /**  DEInternationalSecuritiesID  */  
   DEInternationalSecuritiesID:string,
      /**  LinkToContract  */  
   LinkToContract:boolean,
      /**  DEIsInvestment  */  
   DEIsInvestment:boolean,
      /**  DEPayStatCode  */  
   DEPayStatCode:string,
      /**  DEDenomination  */  
   DEDenomination:string,
      /**  PartLengthWidthHeightUM  */  
   PartLengthWidthHeightUM:string,
      /**  DiameterUM  */  
   DiameterUM:string,
      /**  DiameterInside  */  
   DiameterInside:number,
      /**  DiameterOutside  */  
   DiameterOutside:number,
      /**  ThicknessUM  */  
   ThicknessUM:string,
      /**  Thickness  */  
   Thickness:number,
      /**  ThicknessMax  */  
   ThicknessMax:number,
      /**  Durometer  */  
   Durometer:string,
      /**  Specification  */  
   Specification:string,
      /**  EngineeringAlert  */  
   EngineeringAlert:string,
      /**  Condition  */  
   Condition:string,
      /**  IsCompliant  */  
   IsCompliant:boolean,
      /**  IsRestricted  */  
   IsRestricted:boolean,
      /**  IsSafetyItem  */  
   IsSafetyItem:boolean,
      /**  CommercialBrand  */  
   CommercialBrand:string,
      /**  CommercialSubBrand  */  
   CommercialSubBrand:string,
      /**  CommercialCategory  */  
   CommercialCategory:string,
      /**  CommercialSubCategory  */  
   CommercialSubCategory:string,
      /**  CommercialStyle  */  
   CommercialStyle:string,
      /**  CommercialSize1  */  
   CommercialSize1:string,
      /**  CommercialSize2  */  
   CommercialSize2:string,
      /**  CommercialColor  */  
   CommercialColor:string,
      /**  IsGiftCard  */  
   IsGiftCard:boolean,
      /**  PhotoFile  */  
   PhotoFile:string,
      /**  PartPhotoExists  */  
   PartPhotoExists:boolean,
      /**  CommentText  */  
   CommentText:string,
      /**  PartSpecificPackingUOM  */  
   PartSpecificPackingUOM:boolean,
      /**  ImageID  */  
   ImageID:string,
      /**  CNSpecification  */  
   CNSpecification:string,
      /**  SyncToExternalCRM  */  
   SyncToExternalCRM:boolean,
      /**  ExternalCRMPartID  */  
   ExternalCRMPartID:string,
      /**  ExternalCRMLastSync  */  
   ExternalCRMLastSync:string,
      /**  ExternalCRMSyncRequired  */  
   ExternalCRMSyncRequired:boolean,
      /**  PESUNATTypeCode  */  
   PESUNATTypeCode:string,
      /**  PESUNATUOMCode  */  
   PESUNATUOMCode:string,
      /**  CNCodeVersion  */  
   CNCodeVersion:string,
      /**  CNTaxCategoryCode  */  
   CNTaxCategoryCode:string,
      /**  CNHasPreferentialTreatment  */  
   CNHasPreferentialTreatment:boolean,
      /**  CNPreferentialTreatmentContent  */  
   CNPreferentialTreatmentContent:string,
      /**  CNZeroTaxRateMark  */  
   CNZeroTaxRateMark:string,
      /**  SubLevelCode  */  
   SubLevelCode:number,
      /**  User the part was created by  */  
   CreatedBy:string,
      /**  Date the part was created on  */  
   CreatedOn:string,
      /**  AttBatch  */  
   AttBatch:string,
      /**  AttMfgBatch  */  
   AttMfgBatch:string,
      /**  AttMfgLot  */  
   AttMfgLot:string,
      /**  AttHeat  */  
   AttHeat:string,
      /**  AttFirmware  */  
   AttFirmware:string,
      /**  AttBeforeDt  */  
   AttBeforeDt:string,
      /**  AttMfgDt  */  
   AttMfgDt:string,
      /**  AttCureDt  */  
   AttCureDt:string,
      /**  AttExpDt  */  
   AttExpDt:string,
      /**  DeferManualEntry  */  
   DeferManualEntry:boolean,
      /**  DeferPurchaseReceipt  */  
   DeferPurchaseReceipt:boolean,
      /**  DeferJobReceipt  */  
   DeferJobReceipt:boolean,
      /**  DeferInspection  */  
   DeferInspection:boolean,
      /**  DeferQtyAdjustment  */  
   DeferQtyAdjustment:boolean,
      /**  DeferInventoryMove  */  
   DeferInventoryMove:boolean,
      /**  DeferShipments  */  
   DeferShipments:boolean,
      /**  DeferInventoryCounts  */  
   DeferInventoryCounts:boolean,
      /**  DeferAssetDisposal  */  
   DeferAssetDisposal:boolean,
      /**  DeferReturnMaterials  */  
   DeferReturnMaterials:boolean,
      /**  MXProdServCode  */  
   MXProdServCode:string,
      /**  Date/Time when the Part record was last updated.  */  
   ChangedOn:string,
      /**  MXCustomsDuty  */  
   MXCustomsDuty:string,
      /**  SendToFSA  */  
   SendToFSA:boolean,
      /**  ExternalMESSyncRequired  */  
   ExternalMESSyncRequired:boolean,
      /**  ExternalMESLastSync  */  
   ExternalMESLastSync:string,
      /**  FSAItem  */  
   FSAItem:boolean,
      /**  FSAEquipment  */  
   FSAEquipment:boolean,
      /**  BOLClass  */  
   BOLClass:string,
      /**  FairMarketValue  */  
   FairMarketValue:number,
      /**  SAFTProdCategory  */  
   SAFTProdCategory:string,
      /**  AttrClassID  */  
   AttrClassID:string,
      /**  LocationIDNumReq  */  
   LocationIDNumReq:boolean,
      /**  LocationTrackInv  */  
   LocationTrackInv:boolean,
      /**  LocationMtlView  */  
   LocationMtlView:boolean,
      /**  LCNRVReporting  */  
   LCNRVReporting:boolean,
      /**  LCNRVEstimatedUnitPrice  */  
   LCNRVEstimatedUnitPrice:number,
      /**  MXCustomsUMFrom  */  
   MXCustomsUMFrom:string,
      /**  LocationFormatID  */  
   LocationFormatID:string,
      /**  IsServices  */  
   IsServices:boolean,
      /**  PEDetrGoodServiceCode  */  
   PEDetrGoodServiceCode:string,
      /**  PEProductServiceCode  */  
   PEProductServiceCode:string,
      /**  DualUOMClassID  */  
   DualUOMClassID:string,
      /**  CNProductName  */  
   CNProductName:string,
      /**  CNWeight  */  
   CNWeight:number,
      /**  CNWeightUOM  */  
   CNWeightUOM:string,
      /**  CNBonded  */  
   CNBonded:boolean,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   TrackInventoryAttributes:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   DefaultAttributeSetID:number,
      /**  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttISOrigCountry:string,
      /**  ExternalSchemeID  */  
   ExternalSchemeID:string,
      /**  ExternalID  */  
   ExternalID:string,
      /**  CommoditySchemeID  */  
   CommoditySchemeID:string,
      /**  CommoditySchemeVersion  */  
   CommoditySchemeVersion:string,
      /**  TrackInventoryByRevision  */  
   TrackInventoryByRevision:boolean,
      /**  PlanningByRevision  */  
   PlanningByRevision:boolean,
      /**  RcvInspectionReqPart  */  
   RcvInspectionReqPart:string,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  FSMPartType  */  
   FSMPartType:number,
      /**  UserChar1  */  
   UserChar1:string,
      /**  UserChar2  */  
   UserChar2:string,
      /**  UserChar3  */  
   UserChar3:string,
      /**  UserChar4  */  
   UserChar4:string,
      /**  UserDate1  */  
   UserDate1:string,
      /**  UserDate2  */  
   UserDate2:string,
      /**  UserDate3  */  
   UserDate3:string,
      /**  UserDate4  */  
   UserDate4:string,
      /**  UserDecimal1  */  
   UserDecimal1:number,
      /**  UserDecimal2  */  
   UserDecimal2:number,
   LinkPartNum:string,
      /**  UserDecimal3  */  
   UserDecimal3:number,
   ProdCodeDescription:string,
      /**  UserDecimal4  */  
   UserDecimal4:number,
   StockPart:boolean,
   TypeCodeDescription:string,
      /**  UserInteger1  */  
   UserInteger1:number,
      /**  UserInteger2  */  
   UserInteger2:number,
   DispPartNum:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbPartSearchTableset{
   GlbPart:Erp_Tablesets_GlbPartRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGlbPartSearchTableset{
   GlbPart:Erp_Tablesets_GlbPartRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param glbCompany
      @param glbPartNum
   */  
export interface GetByID_input{
   glbCompany:string,
   glbPartNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GlbPartSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GlbPartSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GlbPartSearchTableset[],
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
   returnObj:Erp_Tablesets_GlbPartListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param glbCompany
   */  
export interface GetNewGlbPart_input{
   ds:Erp_Tablesets_GlbPartSearchTableset[],
   glbCompany:string,
}

export interface GetNewGlbPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbPartSearchTableset[],
}
}

   /** Required : 
      @param whereClauseGlbPart
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGlbPart:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GlbPartSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtGlbPartSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGlbPartSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GlbPartSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbPartSearchTableset[],
}
}

