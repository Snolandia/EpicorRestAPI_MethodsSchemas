import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.AlcHedTgtStampSearchSvc
// Description: AlcHedTgtStampSearch Service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/$metadata", {
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
   Description: Get AlcHedTgtStampSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHedTgtStampSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHedTgtStampSearchRow
   */  
export function get_AlcHedTgtStampSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedTgtStampSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/AlcHedTgtStampSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedTgtStampSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHedTgtStampSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHedTgtStampSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHedTgtStampSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlcHedTgtStampSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/AlcHedTgtStampSearches", {
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
   Summary: Calls GetByID to retrieve the AlcHedTgtStampSearch item
   Description: Calls GetByID to retrieve the AlcHedTgtStampSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHedTgtStampSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHedTgtStampSearchRow
   */  
export function get_AlcHedTgtStampSearches_Company_AllocID(Company:string, AllocID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AlcHedTgtStampSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/AlcHedTgtStampSearches(" + Company + "," + AllocID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AlcHedTgtStampSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AlcHedTgtStampSearch for the service
   Description: Calls UpdateExt to update AlcHedTgtStampSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHedTgtStampSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHedTgtStampSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AlcHedTgtStampSearches_Company_AllocID(Company:string, AllocID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/AlcHedTgtStampSearches(" + Company + "," + AllocID + ")", {
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
   Summary: Call UpdateExt to delete AlcHedTgtStampSearch item
   Description: Call UpdateExt to delete AlcHedTgtStampSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHedTgtStampSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AllocID Desc: AllocID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AlcHedTgtStampSearches_Company_AllocID(Company:string, AllocID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/AlcHedTgtStampSearches(" + Company + "," + AllocID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHedTgtStampSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedTgtStampSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedTgtStampSearchListRow)
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
export function get_GetRows(whereClauseAlcHedTgtStampSearch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAlcHedTgtStampSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAlcHedTgtStampSearch=" + whereClauseAlcHedTgtStampSearch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(allocID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof allocID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "allocID=" + allocID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewAlcHedTgtStampSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHedTgtStampSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHedTgtStampSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHedTgtStampSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAlcHedTgtStampSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/GetNewAlcHedTgtStampSearch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AlcHedTgtStampSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedTgtStampSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHedTgtStampSearchListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHedTgtStampSearchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AlcHedTgtStampSearchRow[],
}

export interface Erp_Tablesets_AlcHedTgtStampSearchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Allocation code description.  */  
   "Description":string,
      /**   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  */  
   "AllocationType":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Allocation tier.  */  
   "Tier":number,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   "PriorTgtStamp":string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   "TgtStamp":string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   "SrcAllocStamp":string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   "IgnoreStamp":boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   "UseAllStamps":boolean,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   "AllocOption":number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   "PercentToAlloc":number,
      /**  Indicates if the allocation units are used.  */  
   "UseAllocUnits":boolean,
      /**  The general ledger account the allocation is to be written off.  */  
   "OffsetAcct":string,
      /**  Offset Segment Value 1  */  
   "OffsetSegVal1":string,
      /**  Offset Segment Value 2  */  
   "OffsetSegVal2":string,
      /**  Offset Segment Value 3  */  
   "OffsetSegVal3":string,
      /**  Offset Segment Value 4  */  
   "OffsetSegVal4":string,
      /**  Offset Segment Value 5  */  
   "OffsetSegVal5":string,
      /**  Offset Segment Value 6  */  
   "OffsetSegVal6":string,
      /**  Offset Segment Value 7  */  
   "OffsetSegVal7":string,
      /**  Offset Segment Value 8  */  
   "OffsetSegVal8":string,
      /**  Offset Segment Value 9  */  
   "OffsetSegVal9":string,
      /**  Offset Segment Value 10  */  
   "OffsetSegVal10":string,
      /**  Offset Segment Value 11  */  
   "OffsetSegVal11":string,
      /**  Offset Segment Value 12  */  
   "OffsetSegVal12":string,
      /**  Offset Segment Value 13  */  
   "OffsetSegVal13":string,
      /**  Offset Segment Value 14  */  
   "OffsetSegVal14":string,
      /**  Offset Segment Value 15  */  
   "OffsetSegVal15":string,
      /**  Offset Segment Value 16  */  
   "OffsetSegVal16":string,
      /**  Offset Segment Value 17  */  
   "OffsetSegVal17":string,
      /**  Offset Segment Value 18  */  
   "OffsetSegVal18":string,
      /**  Offset Segment Value 19  */  
   "OffsetSegVal19":string,
      /**  Offset Segment Value 20  */  
   "OffsetSegVal20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AlcHedTgtStampSearchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Allocation Code.  */  
   "AllocID":string,
      /**  Allocation code description.  */  
   "Description":string,
      /**   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  */  
   "AllocationType":number,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  Allocation tier.  */  
   "Tier":number,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   "PriorTgtStamp":string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   "TgtStamp":string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   "SrcAllocStamp":string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   "IgnoreStamp":boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   "UseAllStamps":boolean,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   "AllocOption":number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   "PercentToAlloc":number,
      /**  Indicates if the allocation units are used.  */  
   "UseAllocUnits":boolean,
      /**  The general ledger account the allocation is to be written off.  */  
   "OffsetAcct":string,
      /**  Offset Segment Value 1  */  
   "OffsetSegVal1":string,
      /**  Offset Segment Value 2  */  
   "OffsetSegVal2":string,
      /**  Offset Segment Value 3  */  
   "OffsetSegVal3":string,
      /**  Offset Segment Value 4  */  
   "OffsetSegVal4":string,
      /**  Offset Segment Value 5  */  
   "OffsetSegVal5":string,
      /**  Offset Segment Value 6  */  
   "OffsetSegVal6":string,
      /**  Offset Segment Value 7  */  
   "OffsetSegVal7":string,
      /**  Offset Segment Value 8  */  
   "OffsetSegVal8":string,
      /**  Offset Segment Value 9  */  
   "OffsetSegVal9":string,
      /**  Offset Segment Value 10  */  
   "OffsetSegVal10":string,
      /**  Offset Segment Value 11  */  
   "OffsetSegVal11":string,
      /**  Offset Segment Value 12  */  
   "OffsetSegVal12":string,
      /**  Offset Segment Value 13  */  
   "OffsetSegVal13":string,
      /**  Offset Segment Value 14  */  
   "OffsetSegVal14":string,
      /**  Offset Segment Value 15  */  
   "OffsetSegVal15":string,
      /**  Offset Segment Value 16  */  
   "OffsetSegVal16":string,
      /**  Offset Segment Value 17  */  
   "OffsetSegVal17":string,
      /**  Offset Segment Value 18  */  
   "OffsetSegVal18":string,
      /**  Offset Segment Value 19  */  
   "OffsetSegVal19":string,
      /**  Offset Segment Value 20  */  
   "OffsetSegVal20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if Statistical Balance of Target Account should be used as Allocation Units  */  
   "StatBalAsAllocUnits":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param allocID
   */  
export interface DeleteByID_input{
   allocID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AlcHedTgtStampSearchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Allocation code description.  */  
   Description:string,
      /**   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  */  
   AllocationType:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Allocation tier.  */  
   Tier:number,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   PriorTgtStamp:string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   TgtStamp:string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   SrcAllocStamp:string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   IgnoreStamp:boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   UseAllStamps:boolean,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   AllocOption:number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   PercentToAlloc:number,
      /**  Indicates if the allocation units are used.  */  
   UseAllocUnits:boolean,
      /**  The general ledger account the allocation is to be written off.  */  
   OffsetAcct:string,
      /**  Offset Segment Value 1  */  
   OffsetSegVal1:string,
      /**  Offset Segment Value 2  */  
   OffsetSegVal2:string,
      /**  Offset Segment Value 3  */  
   OffsetSegVal3:string,
      /**  Offset Segment Value 4  */  
   OffsetSegVal4:string,
      /**  Offset Segment Value 5  */  
   OffsetSegVal5:string,
      /**  Offset Segment Value 6  */  
   OffsetSegVal6:string,
      /**  Offset Segment Value 7  */  
   OffsetSegVal7:string,
      /**  Offset Segment Value 8  */  
   OffsetSegVal8:string,
      /**  Offset Segment Value 9  */  
   OffsetSegVal9:string,
      /**  Offset Segment Value 10  */  
   OffsetSegVal10:string,
      /**  Offset Segment Value 11  */  
   OffsetSegVal11:string,
      /**  Offset Segment Value 12  */  
   OffsetSegVal12:string,
      /**  Offset Segment Value 13  */  
   OffsetSegVal13:string,
      /**  Offset Segment Value 14  */  
   OffsetSegVal14:string,
      /**  Offset Segment Value 15  */  
   OffsetSegVal15:string,
      /**  Offset Segment Value 16  */  
   OffsetSegVal16:string,
      /**  Offset Segment Value 17  */  
   OffsetSegVal17:string,
      /**  Offset Segment Value 18  */  
   OffsetSegVal18:string,
      /**  Offset Segment Value 19  */  
   OffsetSegVal19:string,
      /**  Offset Segment Value 20  */  
   OffsetSegVal20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHedTgtStampSearchListTableset{
   AlcHedTgtStampSearchList:Erp_Tablesets_AlcHedTgtStampSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AlcHedTgtStampSearchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Allocation Code.  */  
   AllocID:string,
      /**  Allocation code description.  */  
   Description:string,
      /**   Identifies whether or not the allocaiton is balance or transaction based.  1 = Transaction and is the default value.
2 = Balance based.  */  
   AllocationType:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Allocation tier.  */  
   Tier:number,
      /**  Identifies the allocation stamp to which this allocation is to be applied.  */  
   PriorTgtStamp:string,
      /**  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  */  
   TgtStamp:string,
      /**  Identifies the allocation stamp that was processed by this allocation.  */  
   SrcAllocStamp:string,
      /**  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  */  
   IgnoreStamp:boolean,
      /**  Yes indicates that all allocation stamps are valid for the allocation code.  */  
   UseAllStamps:boolean,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  */  
   AllocOption:number,
      /**  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  */  
   PercentToAlloc:number,
      /**  Indicates if the allocation units are used.  */  
   UseAllocUnits:boolean,
      /**  The general ledger account the allocation is to be written off.  */  
   OffsetAcct:string,
      /**  Offset Segment Value 1  */  
   OffsetSegVal1:string,
      /**  Offset Segment Value 2  */  
   OffsetSegVal2:string,
      /**  Offset Segment Value 3  */  
   OffsetSegVal3:string,
      /**  Offset Segment Value 4  */  
   OffsetSegVal4:string,
      /**  Offset Segment Value 5  */  
   OffsetSegVal5:string,
      /**  Offset Segment Value 6  */  
   OffsetSegVal6:string,
      /**  Offset Segment Value 7  */  
   OffsetSegVal7:string,
      /**  Offset Segment Value 8  */  
   OffsetSegVal8:string,
      /**  Offset Segment Value 9  */  
   OffsetSegVal9:string,
      /**  Offset Segment Value 10  */  
   OffsetSegVal10:string,
      /**  Offset Segment Value 11  */  
   OffsetSegVal11:string,
      /**  Offset Segment Value 12  */  
   OffsetSegVal12:string,
      /**  Offset Segment Value 13  */  
   OffsetSegVal13:string,
      /**  Offset Segment Value 14  */  
   OffsetSegVal14:string,
      /**  Offset Segment Value 15  */  
   OffsetSegVal15:string,
      /**  Offset Segment Value 16  */  
   OffsetSegVal16:string,
      /**  Offset Segment Value 17  */  
   OffsetSegVal17:string,
      /**  Offset Segment Value 18  */  
   OffsetSegVal18:string,
      /**  Offset Segment Value 19  */  
   OffsetSegVal19:string,
      /**  Offset Segment Value 20  */  
   OffsetSegVal20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if Statistical Balance of Target Account should be used as Allocation Units  */  
   StatBalAsAllocUnits:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AlcHedTgtStampSearchTableset{
   AlcHedTgtStampSearch:Erp_Tablesets_AlcHedTgtStampSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtAlcHedTgtStampSearchTableset{
   AlcHedTgtStampSearch:Erp_Tablesets_AlcHedTgtStampSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param allocID
   */  
export interface GetByID_input{
   allocID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_AlcHedTgtStampSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_AlcHedTgtStampSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_AlcHedTgtStampSearchTableset[],
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
   returnObj:Erp_Tablesets_AlcHedTgtStampSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewAlcHedTgtStampSearch_input{
   ds:Erp_Tablesets_AlcHedTgtStampSearchTableset[],
}

export interface GetNewAlcHedTgtStampSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTgtStampSearchTableset[],
}
}

   /** Required : 
      @param whereClauseAlcHedTgtStampSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAlcHedTgtStampSearch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_AlcHedTgtStampSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtAlcHedTgtStampSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAlcHedTgtStampSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_AlcHedTgtStampSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AlcHedTgtStampSearchTableset[],
}
}

