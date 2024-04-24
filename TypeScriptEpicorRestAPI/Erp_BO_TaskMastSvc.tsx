import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.TaskMastSvc
// Description: The Task Master main object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/$metadata", {
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
   Description: Get TaskMasts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaskMasts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskMastRow
   */  
export function get_TaskMasts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskMastRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/TaskMasts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskMastRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaskMasts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaskMastRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaskMastRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaskMasts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/TaskMasts", {
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
   Summary: Calls GetByID to retrieve the TaskMast item
   Description: Calls GetByID to retrieve the TaskMast item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaskMast
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaskMastRow
   */  
export function get_TaskMasts_Company_TaskID(Company:string, TaskID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaskMastRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/TaskMasts(" + Company + "," + TaskID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_TaskMastRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaskMast for the service
   Description: Calls UpdateExt to update TaskMast. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaskMast
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaskMastRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaskMasts_Company_TaskID(Company:string, TaskID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/TaskMasts(" + Company + "," + TaskID + ")", {
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
   Summary: Call UpdateExt to delete TaskMast item
   Description: Call UpdateExt to delete TaskMast item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaskMast
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaskID Desc: TaskID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaskMasts_Company_TaskID(Company:string, TaskID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/TaskMasts(" + Company + "," + TaskID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaskMastListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskMastListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskMastListRow)
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
export function get_GetRows(whereClauseTaskMast:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTaskMast!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaskMast=" + whereClauseTaskMast
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/GetRows" + params, {
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
export function get_GetByID(taskID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof taskID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "taskID=" + taskID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/GetList" + params, {
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
   Summary: Invoke method OnChangeTypeCode
   Description: This sets the TETaskType field when the TypeCode changes.
   OperationID: OnChangeTypeCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTypeCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTypeCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTypeCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/OnChangeTypeCode", {
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
   Summary: Invoke method GetNewTaskMast
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaskMast
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaskMast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaskMast_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaskMast(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/GetNewTaskMast", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaskMastSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskMastListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaskMastListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaskMastRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaskMastRow[],
}

export interface Erp_Tablesets_TaskMastListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifer of this task assigned by the user.  */  
   "TaskID":string,
      /**  Description of the task.  */  
   "TaskDescription":string,
      /**  RoleCd.RoleCode that is used in determining who the task will be assigned to.  */  
   "RoleCode":string,
      /**  Determines whether or not the completion of this task is required.  */  
   "Mandatory":boolean,
      /**  Completion of the task will send a Global Alert  */  
   "SendAlertComplete":boolean,
      /**  Creation of the task will send a Global Alert  */  
   "SendAlertCreate":boolean,
      /**  Valid values are 1 - 99 1 = HIGH,  99 = LOW.  Priority codes are used when displaying multiple tasks such as in the Task List.  */  
   "PriorityCode":number,
      /**  Contains comments about the Task.  */  
   "TaskComment":string,
      /**  Indicates that the Task cannot be assigned to new task sets or created manually.  */  
   "Inactive":boolean,
      /**  Defines what type of task this task is. Contains the TaskType.TypeCode value selected for this task.  */  
   "TypeCode":string,
      /**  Determines whether or not a User Login Password is required when a task with this TaskMast.TaskID is completed.  */  
   "PasswordReq":boolean,
      /**  For Time and Expense transactions, multiple persons within a Role can be assigned a Task to complete, and if ANY of these persons complete the Task, the Milestone is to be marked complete.  */  
   "AnyApprover":boolean,
      /**  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  */  
   "ApprovalSupervisorLevel":number,
      /**  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  */  
   "SubmitTask":boolean,
      /**  Marks this TaskMast as global, available to be sent out to other companies.  */  
   "GlobalTaskMast":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "RoleDescription":string,
   "TypeDescription":string,
   "StageDesc":string,
      /**  This will be true if the associated TypeCode is associated with a TaskType that has the TimeExpenseType set to true.  */  
   "TETaskType":boolean,
      /**  A description of the role.  */  
   "RoleCodeRoleDescription":string,
      /**  Full Description of the Type of task.  */  
   "TypeCodeTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaskMastRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifer of this task assigned by the user.  */  
   "TaskID":string,
      /**  Description of the task.  */  
   "TaskDescription":string,
      /**  RoleCd.RoleCode that is used in determining who the task will be assigned to.  */  
   "RoleCode":string,
      /**  Determines whether or not the completion of this task is required.  */  
   "Mandatory":boolean,
      /**  Completion of the task will send a Global Alert  */  
   "SendAlertComplete":boolean,
      /**  Creation of the task will send a Global Alert  */  
   "SendAlertCreate":boolean,
      /**  Valid values are 1 - 99 1 = HIGH,  99 = LOW.  Priority codes are used when displaying multiple tasks such as in the Task List.  */  
   "PriorityCode":number,
      /**  Contains comments about the Task.  */  
   "TaskComment":string,
      /**  Indicates that the Task cannot be assigned to new task sets or created manually.  */  
   "Inactive":boolean,
      /**  Defines what type of task this task is. Contains the TaskType.TypeCode value selected for this task.  */  
   "TypeCode":string,
      /**  Determines whether or not a User Login Password is required when a task with this TaskMast.TaskID is completed.  */  
   "PasswordReq":boolean,
      /**  For Time and Expense transactions, multiple persons within a Role can be assigned a Task to complete, and if ANY of these persons complete the Task, the Milestone is to be marked complete.  */  
   "AnyApprover":boolean,
      /**  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  */  
   "ApprovalSupervisorLevel":number,
      /**  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  */  
   "SubmitTask":boolean,
      /**  Marks this TaskMast as global, available to be sent out to other companies.  */  
   "GlobalTaskMast":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "RoleDescription":string,
   "TypeDescription":string,
   "StageDesc":string,
      /**  This will be true if the associated TypeCode is associated with a TaskType that has the TimeExpenseType set to true.  */  
   "TETaskType":boolean,
   "BitFlag":number,
   "RoleCodeRoleDescription":string,
   "TypeCodeTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param taskID
   */  
export interface DeleteByID_input{
   taskID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_TaskMastListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifer of this task assigned by the user.  */  
   TaskID:string,
      /**  Description of the task.  */  
   TaskDescription:string,
      /**  RoleCd.RoleCode that is used in determining who the task will be assigned to.  */  
   RoleCode:string,
      /**  Determines whether or not the completion of this task is required.  */  
   Mandatory:boolean,
      /**  Completion of the task will send a Global Alert  */  
   SendAlertComplete:boolean,
      /**  Creation of the task will send a Global Alert  */  
   SendAlertCreate:boolean,
      /**  Valid values are 1 - 99 1 = HIGH,  99 = LOW.  Priority codes are used when displaying multiple tasks such as in the Task List.  */  
   PriorityCode:number,
      /**  Contains comments about the Task.  */  
   TaskComment:string,
      /**  Indicates that the Task cannot be assigned to new task sets or created manually.  */  
   Inactive:boolean,
      /**  Defines what type of task this task is. Contains the TaskType.TypeCode value selected for this task.  */  
   TypeCode:string,
      /**  Determines whether or not a User Login Password is required when a task with this TaskMast.TaskID is completed.  */  
   PasswordReq:boolean,
      /**  For Time and Expense transactions, multiple persons within a Role can be assigned a Task to complete, and if ANY of these persons complete the Task, the Milestone is to be marked complete.  */  
   AnyApprover:boolean,
      /**  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  */  
   ApprovalSupervisorLevel:number,
      /**  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  */  
   SubmitTask:boolean,
      /**  Marks this TaskMast as global, available to be sent out to other companies.  */  
   GlobalTaskMast:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   RoleDescription:string,
   TypeDescription:string,
   StageDesc:string,
      /**  This will be true if the associated TypeCode is associated with a TaskType that has the TimeExpenseType set to true.  */  
   TETaskType:boolean,
      /**  A description of the role.  */  
   RoleCodeRoleDescription:string,
      /**  Full Description of the Type of task.  */  
   TypeCodeTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskMastListTableset{
   TaskMastList:Erp_Tablesets_TaskMastListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TaskMastRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifer of this task assigned by the user.  */  
   TaskID:string,
      /**  Description of the task.  */  
   TaskDescription:string,
      /**  RoleCd.RoleCode that is used in determining who the task will be assigned to.  */  
   RoleCode:string,
      /**  Determines whether or not the completion of this task is required.  */  
   Mandatory:boolean,
      /**  Completion of the task will send a Global Alert  */  
   SendAlertComplete:boolean,
      /**  Creation of the task will send a Global Alert  */  
   SendAlertCreate:boolean,
      /**  Valid values are 1 - 99 1 = HIGH,  99 = LOW.  Priority codes are used when displaying multiple tasks such as in the Task List.  */  
   PriorityCode:number,
      /**  Contains comments about the Task.  */  
   TaskComment:string,
      /**  Indicates that the Task cannot be assigned to new task sets or created manually.  */  
   Inactive:boolean,
      /**  Defines what type of task this task is. Contains the TaskType.TypeCode value selected for this task.  */  
   TypeCode:string,
      /**  Determines whether or not a User Login Password is required when a task with this TaskMast.TaskID is completed.  */  
   PasswordReq:boolean,
      /**  For Time and Expense transactions, multiple persons within a Role can be assigned a Task to complete, and if ANY of these persons complete the Task, the Milestone is to be marked complete.  */  
   AnyApprover:boolean,
      /**  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  */  
   ApprovalSupervisorLevel:number,
      /**  Indicates if this task is for submitting time or expense transactions.  Applies only to task types for time or expense.  */  
   SubmitTask:boolean,
      /**  Marks this TaskMast as global, available to be sent out to other companies.  */  
   GlobalTaskMast:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   RoleDescription:string,
   TypeDescription:string,
   StageDesc:string,
      /**  This will be true if the associated TypeCode is associated with a TaskType that has the TimeExpenseType set to true.  */  
   TETaskType:boolean,
   BitFlag:number,
   RoleCodeRoleDescription:string,
   TypeCodeTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaskMastTableset{
   TaskMast:Erp_Tablesets_TaskMastRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtTaskMastTableset{
   TaskMast:Erp_Tablesets_TaskMastRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param taskID
   */  
export interface GetByID_input{
   taskID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TaskMastTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TaskMastTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TaskMastTableset[],
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
   returnObj:Erp_Tablesets_TaskMastListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTaskMast_input{
   ds:Erp_Tablesets_TaskMastTableset[],
}

export interface GetNewTaskMast_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskMastTableset[],
}
}

   /** Required : 
      @param whereClauseTaskMast
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTaskMast:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TaskMastTableset[],
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
      @param newTypeCode
      @param ds
   */  
export interface OnChangeTypeCode_input{
      /**  The proposed TypeCode value  */  
   newTypeCode:string,
   ds:Erp_Tablesets_TaskMastTableset[],
}

export interface OnChangeTypeCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskMastTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtTaskMastTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTaskMastTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TaskMastTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaskMastTableset[],
}
}

