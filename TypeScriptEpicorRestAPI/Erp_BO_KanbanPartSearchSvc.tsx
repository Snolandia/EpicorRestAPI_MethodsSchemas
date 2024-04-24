import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.KanbanPartSearchSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/$metadata", {
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
   Description: Get KanbanPartSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_KanbanPartSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.KanbanPartSearchRow
   */  
export function get_KanbanPartSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_KanbanPartSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/KanbanPartSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_KanbanPartSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_KanbanPartSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.KanbanPartSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.KanbanPartSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KanbanPartSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/KanbanPartSearches", {
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
   Summary: Calls GetByID to retrieve the KanbanPartSearch item
   Description: Calls GetByID to retrieve the KanbanPartSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_KanbanPartSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.KanbanPartSearchRow
   */  
export function get_KanbanPartSearches_Company_PartNum(Company:string, PartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_KanbanPartSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/KanbanPartSearches(" + Company + "," + PartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_KanbanPartSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update KanbanPartSearch for the service
   Description: Calls UpdateExt to update KanbanPartSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_KanbanPartSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.KanbanPartSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_KanbanPartSearches_Company_PartNum(Company:string, PartNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/KanbanPartSearches(" + Company + "," + PartNum + ")", {
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
   Summary: Call UpdateExt to delete KanbanPartSearch item
   Description: Call UpdateExt to delete KanbanPartSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_KanbanPartSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_KanbanPartSearches_Company_PartNum(Company:string, PartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/KanbanPartSearches(" + Company + "," + PartNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.KanbanPartSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_KanbanPartSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_KanbanPartSearchListRow)
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
export function get_GetRows(whereClauseKanbanPartSearch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseKanbanPartSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseKanbanPartSearch=" + whereClauseKanbanPartSearch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/GetRows" + params, {
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
export function get_GetByID(partNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewKanbanPartSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewKanbanPartSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewKanbanPartSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewKanbanPartSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewKanbanPartSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/GetNewKanbanPartSearch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanPartSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_KanbanPartSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_KanbanPartSearchListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_KanbanPartSearchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_KanbanPartSearchRow[],
}

export interface Erp_Tablesets_KanbanPartSearchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  */  
   "SearchWord":string,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   "ClassID":string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   "TypeCode":string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   "NonStock":boolean,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   "ProdCode":string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   "InActive":boolean,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "TrackLots":boolean,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "TrackDimension":boolean,
      /**  Indicates if this part is serial number tracked  */  
   "TrackSerialNum":boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   "PhantomBOM":boolean,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   "OnHold":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Contains the reason this part is not available for Kanban selection  */  
   "InvalidReason":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_KanbanPartSearchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  */  
   "SearchWord":string,
      /**  Describes the Part.  */  
   "PartDescription":string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   "ClassID":string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   "TypeCode":string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   "NonStock":boolean,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   "ProdCode":string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   "InActive":boolean,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   "Method":boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "TrackLots":boolean,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "TrackDimension":boolean,
      /**  Indicates if this part is serial number tracked  */  
   "TrackSerialNum":boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   "PhantomBOM":boolean,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   "OnHold":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Contains the reason this part is not available for Kanban selection  */  
   "InvalidReason":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "SalesCatID_c":string,
   "CustomBuyout_c":boolean,
   "NonSellable_c":boolean,
   "WebSearchable_c":boolean,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param partNum
   */  
export interface DeleteByID_input{
   partNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_KanbanPartSearchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  */  
   SearchWord:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   ClassID:string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   TypeCode:string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   NonStock:boolean,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   ProdCode:string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   InActive:boolean,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   TrackLots:boolean,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   TrackDimension:boolean,
      /**  Indicates if this part is serial number tracked  */  
   TrackSerialNum:boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   PhantomBOM:boolean,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   OnHold:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Contains the reason this part is not available for Kanban selection  */  
   InvalidReason:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_KanbanPartSearchListTableset{
   KanbanPartSearchList:Erp_Tablesets_KanbanPartSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_KanbanPartSearchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  */  
   SearchWord:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  */  
   ClassID:string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   TypeCode:string,
      /**  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  */  
   NonStock:boolean,
      /**  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  */  
   ProdCode:string,
      /**   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  */  
   InActive:boolean,
      /**  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   TrackLots:boolean,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   TrackDimension:boolean,
      /**  Indicates if this part is serial number tracked  */  
   TrackSerialNum:boolean,
      /**  A flag which indicates if this Part is a "Phantom BOM".  */  
   PhantomBOM:boolean,
      /**  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  */  
   OnHold:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Contains the reason this part is not available for Kanban selection  */  
   InvalidReason:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   SalesCatID_c:string,
   CustomBuyout_c:boolean,
   NonSellable_c:boolean,
   WebSearchable_c:boolean,
}

export interface Erp_Tablesets_KanbanPartSearchTableset{
   KanbanPartSearch:Erp_Tablesets_KanbanPartSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtKanbanPartSearchTableset{
   KanbanPartSearch:Erp_Tablesets_KanbanPartSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
   */  
export interface GetByID_input{
   partNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_KanbanPartSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_KanbanPartSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_KanbanPartSearchTableset[],
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
   returnObj:Erp_Tablesets_KanbanPartSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewKanbanPartSearch_input{
   ds:Erp_Tablesets_KanbanPartSearchTableset[],
}

export interface GetNewKanbanPartSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanPartSearchTableset[],
}
}

   /** Required : 
      @param whereClauseKanbanPartSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseKanbanPartSearch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_KanbanPartSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtKanbanPartSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtKanbanPartSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_KanbanPartSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanPartSearchTableset[],
}
}

