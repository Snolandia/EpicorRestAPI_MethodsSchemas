import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.IntgWorkbenchSvc
// Description: Purpose:
Parameters:  none
Notes:
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/$metadata", {
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
   Description: Get IntgWorkbenches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IntgWorkbenches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IntQueInRow
   */  
export function get_IntgWorkbenches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IntQueInRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/IntgWorkbenches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IntQueInRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IntgWorkbenches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.IntQueInRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.IntQueInRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IntgWorkbenches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/IntgWorkbenches", {
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
   Summary: Calls GetByID to retrieve the IntgWorkbench item
   Description: Calls GetByID to retrieve the IntgWorkbench item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetById_IntgWorkbench
      @param IntQueID Desc: IntQueID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.IntQueInRow
   */  
export function get_IntgWorkbenches_IntQueID(IntQueID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_IntQueInRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/IntgWorkbenches(" + IntQueID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_IntQueInRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update IntgWorkbench for the service
   Description: Calls UpdateExt to update IntgWorkbench. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: UpdateExt_IntgWorkbench
      @param IntQueID Desc: IntQueID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.IntQueInRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_IntgWorkbenches_IntQueID(IntQueID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/IntgWorkbenches(" + IntQueID + ")", {
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
   Summary: Call UpdateExt to delete IntgWorkbench item
   Description: Call UpdateExt to delete IntgWorkbench item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: DeleteUpdateExt_IntgWorkbench
      @param IntQueID Desc: IntQueID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_IntgWorkbenches_IntQueID(IntQueID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/IntgWorkbenches(" + IntQueID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IntQueInListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IntQueInListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IntQueInListRow)
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
export function get_GetRows(whereClauseIntQueIn:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseIntQueIn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseIntQueIn=" + whereClauseIntQueIn
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(intQueID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof intQueID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "intQueID=" + intQueID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList for specified table and column
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/GetCodeDescList", {
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
   Summary: Invoke method ProcessIntQueIn
   Description: Process the IntQueIn record.  Either 'R'egister, 'V'alidate, or 'T'ranslate
   OperationID: ProcessIntQueIn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessIntQueIn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessIntQueIn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessIntQueIn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/ProcessIntQueIn", {
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
   Summary: Invoke method DeleteByObject
   Description: Given a list of Groups/Objects we will delete the IntQueIn and all the IM records related to each one of them.
   OperationID: DeleteByObject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByObject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByObject_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByObject(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/DeleteByObject", {
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
   Summary: Invoke method UpdateIMRecord
   Description: Update the IntQueIn record.
   OperationID: UpdateIMRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateIMRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateIMRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateIMRecord(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/UpdateIMRecord", {
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
   Summary: Invoke method GetIMHierarchy
   Description: Retrieve the IntQueIn record.
   OperationID: GetIMHierarchy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIMHierarchy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIMHierarchy_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIMHierarchy(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/GetIMHierarchy", {
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
   Summary: Invoke method GetIMRecord
   Description: Retrieve the IntQueIn record.
   OperationID: GetIMRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIMRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIMRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIMRecord(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/GetIMRecord", {
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
   Summary: Invoke method buildGenericBuffer
   Description: Retrieve the IntQueIn record.
   OperationID: buildGenericBuffer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/buildGenericBuffer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/buildGenericBuffer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_buildGenericBuffer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/buildGenericBuffer", {
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
   Summary: Invoke method GetErrorRows
   Description: To retrieve the list of errors from failed attempts to import data from external
systems.  This allows a UI to combine onto one screen the 18 browses of the separate
maintenance programs in the External Systems Integration / Operations menu in
Vantage v6.10.
Note that separate BOs are used for viewing / updating the details of each
type (table);  this BO only provides the list of rows needing attention, with
minimal description intended to be sufficient for labeling nodes in a tree view.
It should be possible for the UI to construct calls to GetByID() in the appropriate
BO to load the appropriate sheet for any of the different types.
            
There is an input parameter for each of these types, for which there should be a corresponding
checkbox.  The rows for a given type will only be fetched if its corresponding input is TRUE.
   OperationID: GetErrorRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetErrorRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetErrorRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetErrorRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/GetErrorRows", {
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
   Summary: Invoke method GetDeleteByGroupOptions
   Description: Returns a dataset to store Delete By Group options
   OperationID: GetDeleteByGroupOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeleteByGroupOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDeleteByGroupOptions(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/GetDeleteByGroupOptions", {
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
   Summary: Invoke method DeleteByGroups
   Description: Delete groups by options selected
   OperationID: DeleteByGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByGroups(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/DeleteByGroups", {
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
   Summary: Invoke method GetNewIntQueIn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIntQueIn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIntQueIn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIntQueIn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewIntQueIn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/GetNewIntQueIn", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IntgWorkbenchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IntQueInListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_IntQueInListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IntQueInRow{
   "odatametadata":string,
   "value":Erp_Tablesets_IntQueInRow[],
}

export interface Erp_Tablesets_IntQueInListRow{
      /**  The unique value for this Queue record.  A concatination of the Date (YYMMDD), Time (SSSSS), and a program generated Sequence (9999).  */  
   "IntQueID":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Code for the external package to be interfaced with  */  
   "ExtSystemID":string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   "TransferMethod":string,
      /**  The ID of the interfaced company  */  
   "ExtCompanyID":string,
      /**  The master file to which the Queue table is related to.  This field is used to properly  isolate queue tables to the masters they are related to.  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "Customer" transfer it contains the CustNum value.  */  
   "Key1":string,
      /**  2nd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "ShipTo" transfer it contains the ShipToNum value.  */  
   "Key2":string,
      /**  3rd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key3":string,
      /**  4th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key4":string,
      /**  5th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key5":string,
      /**  6th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key6":string,
      /**  7th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key7":string,
      /**  8th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key8":string,
      /**   Values are:
S = Sent
T = Transferred
P = Partially received
R = Received OK
D = Delete  */  
   "TransStatus":string,
      /**  Transaction Type  */  
   "TransType":string,
      /**  Values are: "Add", "Upd" and "Del"  */  
   "Action":string,
      /**  User Id that created the Queue record. DCDUserID.  */  
   "CreateDCDUserID":string,
      /**  For use by external interfacing software only.  */  
   "ExternalRef":string,
      /**  Is this Queue record ready to be deleted?  */  
   "Complete":boolean,
      /**  Errors exist in this Intermediate Record relating to the Intermediate Status.  */  
   "IntError":boolean,
      /**  9th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key9":string,
      /**  10th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key10":string,
      /**  11th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key11":string,
      /**  12th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key12":string,
      /**  13th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key13":string,
      /**  14th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key14":string,
      /**  15th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key15":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Description based on the TransType field.  */  
   "TransTypeDescription":string,
      /**  Derived from IntQueId when possible  */  
   "InDate":string,
      /**  Derived from IntQueId when possible.  Time of day in HH:MM format.  */  
   "InTime":string,
      /**  Holds identifier (e.g. InvoiceNum)  */  
   "Reference":string,
      /**  Identifier value of the record in the related table.  Example: if RelatedTo = Customer, Ident holds the CustID.  */  
   "Ident":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_IntQueInRow{
      /**  The unique value for this Queue record.  A concatination of the Date (YYMMDD), Time (SSSSS), and a program generated Sequence (9999).  */  
   "IntQueID":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Code for the external package to be interfaced with  */  
   "ExtSystemID":string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   "TransferMethod":string,
      /**  The ID of the interfaced company  */  
   "ExtCompanyID":string,
      /**  The master file to which the Queue table is related to.  This field is used to properly  isolate queue tables to the masters they are related to.  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "Customer" transfer it contains the CustNum value.  */  
   "Key1":string,
      /**  2nd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "ShipTo" transfer it contains the ShipToNum value.  */  
   "Key2":string,
      /**  3rd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key3":string,
      /**  4th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key4":string,
      /**  5th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key5":string,
      /**  6th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key6":string,
      /**  7th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key7":string,
      /**  8th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key8":string,
      /**   Values are:
S = Sent
T = Transferred
P = Partially received
R = Received OK
D = Delete  */  
   "TransStatus":string,
      /**  Transaction Type  */  
   "TransType":string,
      /**  Values are: "Add", "Upd" and "Del"  */  
   "Action":string,
      /**  User Id that created the Queue record. DCDUserID.  */  
   "CreateDCDUserID":string,
      /**  For use by external interfacing software only.  */  
   "ExternalRef":string,
      /**  Is this Queue record ready to be deleted?  */  
   "Complete":boolean,
      /**  Errors exist in this Intermediate Record relating to the Intermediate Status.  */  
   "IntError":boolean,
      /**  9th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key9":string,
      /**  10th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key10":string,
      /**  11th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key11":string,
      /**  12th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key12":string,
      /**  13th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key13":string,
      /**  14th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key14":string,
      /**  15th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   "Key15":string,
      /**  OptionFlags  */  
   "OptionFlags":number,
      /**  Data  */  
   "Data":string,
      /**  LastUpdated  */  
   "LastUpdated":string,
      /**  RelatedToSchemaName  */  
   "RelatedToSchemaName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Derived from IntQueId when possible.  Time of day in HH:MM format.  */  
   "InTime":string,
   "IntQueIDChar":string,
      /**  Holds identifier (e.g. InvoiceNum)  */  
   "Reference":string,
      /**  Description based on the TransType field.  */  
   "TransTypeDescription":string,
      /**  List of errors at the IntQueIn level, before reaching the child records.  */  
   "ErrorList":string,
      /**  Identifier value of the record in the related table.  Example: if RelatedTo = Customer, Ident holds the CustID.  */  
   "Ident":string,
      /**  Derived from IntQueId when possible  */  
   "InDate":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface DeleteByGroups_input{
   ds:Erp_Tablesets_IWBDeleteByGroupTableset[],
}

export interface DeleteByGroups_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IWBDeleteByGroupTableset[],
}
}

   /** Required : 
      @param intQueID
   */  
export interface DeleteByID_input{
   intQueID:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ipRelatedToFile
   */  
export interface DeleteByObject_input{
      /**  List of Groups/Objects (suing the RelatedToFile field as code) to be deleted.
            Valid Values = ABCCode,APInvHed,InvcHead,Customer,Supplier,Vendor,Part,CustCnt,POHeader,RcvHead,GLJrnHed,Currency,CurrRateGrp.  */  
   ipRelatedToFile:string,
}

export interface DeleteByObject_output{
}

export interface Erp_Tablesets_GenericIMTableset{
   GenericWorkBuffer:Erp_Tablesets_GenericWorkBufferRow[],
   IMHierarchy:Erp_Tablesets_IMHierarchyRow[],
   IntgValidationError:Erp_Tablesets_IntgValidationErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GenericWorkBufferRow{
   ColFormat:string,
   ColLabel:string,
   ColName:string,
   ColType:string,
   ColValue:string,
   Company:string,
   RelatedToFile:string,
   IntQueID:number,
      /**  SysRowID of the related record  */  
   RelatedToSysRowID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMHierarchyRow{
   IMTablename:string,
   IntQueID:number,
      /**  Errors exist in this Intermediate Record relating to the Intermediate Status.  */  
   IntError:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IWBDeleteByGroupRow{
   Company:string,
      /**  Delete AP Invoices  */  
   APInvoice:boolean,
      /**  Delete AR Invoices  */  
   ARInvoice:boolean,
      /**  Delete Customers  */  
   Customer:boolean,
      /**  Delete Suppliers  */  
   Supplier:boolean,
      /**  Delete Parts  */  
   Part:boolean,
      /**  Delete Customer Contacts  */  
   CustContact:boolean,
      /**  Delete Imports  */  
   Import:boolean,
      /**  Delete Purchase Orders  */  
   PurchaseOrder:boolean,
      /**  Delete Receipts  */  
   Receipt:boolean,
      /**  Delete GL Journals  */  
   GLJournal:boolean,
      /**  Delete Currencies  */  
   Currency:boolean,
      /**  Delete Currency Rate Groups  */  
   CurrRateGrp:boolean,
      /**  Delete Currency Exchange Rates  */  
   CurrExRate:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IWBDeleteByGroupTableset{
   IWBDeleteByGroup:Erp_Tablesets_IWBDeleteByGroupRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IntQueInListRow{
      /**  The unique value for this Queue record.  A concatination of the Date (YYMMDD), Time (SSSSS), and a program generated Sequence (9999).  */  
   IntQueID:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Code for the external package to be interfaced with  */  
   ExtSystemID:string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   TransferMethod:string,
      /**  The ID of the interfaced company  */  
   ExtCompanyID:string,
      /**  The master file to which the Queue table is related to.  This field is used to properly  isolate queue tables to the masters they are related to.  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "Customer" transfer it contains the CustNum value.  */  
   Key1:string,
      /**  2nd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "ShipTo" transfer it contains the ShipToNum value.  */  
   Key2:string,
      /**  3rd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key3:string,
      /**  4th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key4:string,
      /**  5th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key5:string,
      /**  6th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key6:string,
      /**  7th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key7:string,
      /**  8th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key8:string,
      /**   Values are:
S = Sent
T = Transferred
P = Partially received
R = Received OK
D = Delete  */  
   TransStatus:string,
      /**  Transaction Type  */  
   TransType:string,
      /**  Values are: "Add", "Upd" and "Del"  */  
   Action:string,
      /**  User Id that created the Queue record. DCDUserID.  */  
   CreateDCDUserID:string,
      /**  For use by external interfacing software only.  */  
   ExternalRef:string,
      /**  Is this Queue record ready to be deleted?  */  
   Complete:boolean,
      /**  Errors exist in this Intermediate Record relating to the Intermediate Status.  */  
   IntError:boolean,
      /**  9th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key9:string,
      /**  10th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key10:string,
      /**  11th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key11:string,
      /**  12th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key12:string,
      /**  13th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key13:string,
      /**  14th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key14:string,
      /**  15th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key15:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Description based on the TransType field.  */  
   TransTypeDescription:string,
      /**  Derived from IntQueId when possible  */  
   InDate:string,
      /**  Derived from IntQueId when possible.  Time of day in HH:MM format.  */  
   InTime:string,
      /**  Holds identifier (e.g. InvoiceNum)  */  
   Reference:string,
      /**  Identifier value of the record in the related table.  Example: if RelatedTo = Customer, Ident holds the CustID.  */  
   Ident:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IntQueInListTableset{
   IntQueInList:Erp_Tablesets_IntQueInListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IntQueInRow{
      /**  The unique value for this Queue record.  A concatination of the Date (YYMMDD), Time (SSSSS), and a program generated Sequence (9999).  */  
   IntQueID:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Code for the external package to be interfaced with  */  
   ExtSystemID:string,
      /**  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  */  
   TransferMethod:string,
      /**  The ID of the interfaced company  */  
   ExtCompanyID:string,
      /**  The master file to which the Queue table is related to.  This field is used to properly  isolate queue tables to the masters they are related to.  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "Customer" transfer it contains the CustNum value.  */  
   Key1:string,
      /**  2nd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  For example: For a "ShipTo" transfer it contains the ShipToNum value.  */  
   Key2:string,
      /**  3rd component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key3:string,
      /**  4th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key4:string,
      /**  5th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key5:string,
      /**  6th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key6:string,
      /**  7th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key7:string,
      /**  8th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key8:string,
      /**   Values are:
S = Sent
T = Transferred
P = Partially received
R = Received OK
D = Delete  */  
   TransStatus:string,
      /**  Transaction Type  */  
   TransType:string,
      /**  Values are: "Add", "Upd" and "Del"  */  
   Action:string,
      /**  User Id that created the Queue record. DCDUserID.  */  
   CreateDCDUserID:string,
      /**  For use by external interfacing software only.  */  
   ExternalRef:string,
      /**  Is this Queue record ready to be deleted?  */  
   Complete:boolean,
      /**  Errors exist in this Intermediate Record relating to the Intermediate Status.  */  
   IntError:boolean,
      /**  9th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key9:string,
      /**  10th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key10:string,
      /**  11th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key11:string,
      /**  12th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key12:string,
      /**  13th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key13:string,
      /**  14th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key14:string,
      /**  15th component of the foreign key of the related master record to be sent.  Key field to the Intermediate file set being sent.  */  
   Key15:string,
      /**  OptionFlags  */  
   OptionFlags:number,
      /**  Data  */  
   Data:string,
      /**  LastUpdated  */  
   LastUpdated:string,
      /**  RelatedToSchemaName  */  
   RelatedToSchemaName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Derived from IntQueId when possible.  Time of day in HH:MM format.  */  
   InTime:string,
   IntQueIDChar:string,
      /**  Holds identifier (e.g. InvoiceNum)  */  
   Reference:string,
      /**  Description based on the TransType field.  */  
   TransTypeDescription:string,
      /**  List of errors at the IntQueIn level, before reaching the child records.  */  
   ErrorList:string,
      /**  Identifier value of the record in the related table.  Example: if RelatedTo = Customer, Ident holds the CustID.  */  
   Ident:string,
      /**  Derived from IntQueId when possible  */  
   InDate:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IntgValidationErrorRow{
      /**  The unique value for this Queue record.  A concatination of the Date (DDMMCCYY), Time (SSSSS), and a program generated Sequence (9999999) from the IntQueCtrl table.  */  
   IntQueId:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Code for the external package to be interfaced with  */  
   ExtSystemId:string,
      /**  The ID of the interfaced company  */  
   ExtCompanyId:string,
      /**  Error sequence.  */  
   Seq:number,
      /**  Description of error encountered during attempted import.  */  
   ErrorMessage:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IntgWorkbenchTableset{
   IntQueIn:Erp_Tablesets_IntQueInRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtIntgWorkbenchTableset{
   IntQueIn:Erp_Tablesets_IntQueInRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param intQueID
   */  
export interface GetByID_input{
   intQueID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_IntgWorkbenchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_IntgWorkbenchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_IntgWorkbenchTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  specific tableName  */  
   tableName:string,
      /**  specific fieldName  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

export interface GetDeleteByGroupOptions_output{
   returnObj:Erp_Tablesets_IWBDeleteByGroupTableset[],
}

   /** Required : 
      @param pcRelatedToList
      @param whereClauseIntQueIn
      @param pageSize
      @param absolutePage
   */  
export interface GetErrorRows_input{
      /**  (optional)A tilde-delimited list of values for the RelatedTo field to match.  */  
   pcRelatedToList:string,
      /**  (optional)Where conditions for the IntQueIn* tables.  */  
   whereClauseIntQueIn:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetErrorRows_output{
   returnObj:Erp_Tablesets_IntgWorkbenchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipFileName
      @param pIntQueID
      @param extSystemID
      @param ttGenericIMTablesetDS
   */  
export interface GetIMHierarchy_input{
      /**  RelatedToFile  */  
   ipFileName:string,
      /**  IntQueID  */  
   pIntQueID:number,
      /**  extSystemID  */  
   extSystemID:string,
   ttGenericIMTablesetDS:Erp_Tablesets_GenericIMTableset[],
}

export interface GetIMHierarchy_output{
parameters : {
      /**  output parameters  */  
   ttGenericIMTablesetDS:Erp_Tablesets_GenericIMTableset[],
}
}

   /** Required : 
      @param ipRelatedToFile
      @param pIntQueID
      @param gSysRowID
      @param ttGenericIMTablesetDS
   */  
export interface GetIMRecord_input{
      /**  RelatedToFile  */  
   ipRelatedToFile:string,
      /**  IntQueID  */  
   pIntQueID:number,
      /**  SysRowID  */  
   gSysRowID:string,
   ttGenericIMTablesetDS:Erp_Tablesets_GenericIMTableset[],
}

export interface GetIMRecord_output{
parameters : {
      /**  output parameters  */  
   ttGenericIMTablesetDS:Erp_Tablesets_GenericIMTableset[],
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
   returnObj:Erp_Tablesets_IntQueInListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewIntQueIn_input{
   ds:Erp_Tablesets_IntgWorkbenchTableset[],
}

export interface GetNewIntQueIn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IntgWorkbenchTableset[],
}
}

   /** Required : 
      @param whereClauseIntQueIn
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseIntQueIn:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_IntgWorkbenchTableset[],
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
      @param pIntQueID
      @param tableName
      @param extSystemID
      @param pRunValidation
      @param pRunRegistration
      @param ttGenericIMTableset
   */  
export interface ProcessIntQueIn_input{
      /**  IntQueID  */  
   pIntQueID:number,
      /**  specific tablename  */  
   tableName:string,
      /**  type of extSystem  */  
   extSystemID:string,
      /**  flag to run validation check  */  
   pRunValidation:boolean,
      /**  flag to run registration  */  
   pRunRegistration:boolean,
   ttGenericIMTableset:Erp_Tablesets_GenericIMTableset[],
}

export interface ProcessIntQueIn_output{
parameters : {
      /**  output parameters  */  
   cErrMsgs:string,
   ttGenericIMTableset:Erp_Tablesets_GenericIMTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtIntgWorkbenchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtIntgWorkbenchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ipRelatedToFile
      @param pIntQueID
      @param gSysRowID
      @param colName
      @param ttGenericIMTablesetDS
   */  
export interface UpdateIMRecord_input{
      /**  RelatedToFile  */  
   ipRelatedToFile:string,
      /**  IntQueID  */  
   pIntQueID:number,
      /**  SysRowID  */  
   gSysRowID:string,
      /**  column Name that was updated  */  
   colName:string,
   ttGenericIMTablesetDS:Erp_Tablesets_GenericIMTableset[],
}

export interface UpdateIMRecord_output{
parameters : {
      /**  output parameters  */  
   ttGenericIMTablesetDS:Erp_Tablesets_GenericIMTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_IntgWorkbenchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_IntgWorkbenchTableset[],
}
}

   /** Required : 
      @param ipRelatedToFile
      @param pIntQueID
      @param ttGenericIMTablesetDS
   */  
export interface buildGenericBuffer_input{
      /**  RelatedToFile  */  
   ipRelatedToFile:string,
      /**  IntQueID  */  
   pIntQueID:number,
   ttGenericIMTablesetDS:Erp_Tablesets_GenericIMTableset[],
}

export interface buildGenericBuffer_output{
parameters : {
      /**  output parameters  */  
   ttGenericIMTablesetDS:Erp_Tablesets_GenericIMTableset[],
}
}

