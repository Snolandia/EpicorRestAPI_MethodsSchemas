import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.UserCompSearchSvc
// Description: Queries for UserComp
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/$metadata", {
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
   Description: Get UserCompSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UserCompSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompRow
   */  
export function get_UserCompSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/UserCompSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UserCompSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UserCompRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.UserCompRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UserCompSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/UserCompSearches", {
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
   Summary: Calls GetByID to retrieve the UserCompSearch item
   Description: Calls GetByID to retrieve the UserCompSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserCompSearch
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UserCompRow
   */  
export function get_UserCompSearches_DcdUserID_Company(DcdUserID:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_UserCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/UserCompSearches(" + DcdUserID + "," + Company + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_UserCompRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update UserCompSearch for the service
   Description: Calls UpdateExt to update UserCompSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UserCompSearch
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.UserCompRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_UserCompSearches_DcdUserID_Company(DcdUserID:string, Company:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/UserCompSearches(" + DcdUserID + "," + Company + ")", {
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
   Summary: Call UpdateExt to delete UserCompSearch item
   Description: Call UpdateExt to delete UserCompSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UserCompSearch
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_UserCompSearches_DcdUserID_Company(DcdUserID:string, Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/UserCompSearches(" + DcdUserID + "," + Company + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompListRow)
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
export function get_GetRows(whereClauseUserComp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseUserComp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseUserComp=" + whereClauseUserComp
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/GetRows" + params, {
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
export function get_GetByID(dcdUserID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof dcdUserID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "dcdUserID=" + dcdUserID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/GetList" + params, {
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
   Summary: Invoke method ChangeTransactionRetrievalDays
   Description: Used when in VendorTracker the setting [UserComp].[TransactionRetrievalDays] is changed to a new value.
   OperationID: ChangeTransactionRetrievalDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTransactionRetrievalDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTransactionRetrievalDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTransactionRetrievalDays(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/ChangeTransactionRetrievalDays", {
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
   Summary: Invoke method GetTransactionRetrievalDays
   Description: In VendorTracker the TransactionRetrievalDays is needed from table [UserComp] if there is a value, else from table [XaSyst]
   OperationID: GetTransactionRetrievalDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransactionRetrievalDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransactionRetrievalDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransactionRetrievalDays(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/GetTransactionRetrievalDays", {
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
   Summary: Invoke method GetNewUserComp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUserComp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUserComp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUserComp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUserComp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/GetNewUserComp", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_UserCompListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompRow{
   "odatametadata":string,
   "value":Erp_Tablesets_UserCompRow[],
}

export interface Erp_Tablesets_UserCompListRow{
      /**  User ID  */  
   "DcdUserID":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "CurPlant":string,
      /**  List of Sites the user has access to.  */  
   "PlantList":string,
      /**  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  */  
   "PrimBuyerID":string,
      /**  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  */  
   "Name":string,
      /**  Initial height of the Overload Informer in pixels.  */  
   "OverloadInfHeight":number,
      /**  Initial overload informer sort option.  */  
   "OverloadInfSort":string,
      /**  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  */  
   "PrimSalesRepID":string,
      /**  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  */  
   "StartTaskSaleRepWB":boolean,
      /**  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  */  
   "StartTaskOppEnt":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  */  
   "StartOppSaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  */  
   "StartOrdSaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  */  
   "StartRMASaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  */  
   "StartSCallSaleRepWB":boolean,
      /**  Unique identifier of the Workstations  */  
   "WorkstationID":string,
      /**  Employee ID  */  
   "EmpID":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Company Name  */  
   "CompanyName":string,
      /**  User Name  */  
   "DCDUserIDName":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "EmpIDName":string,
      /**  Description of the station  */  
   "WorkstationIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_UserCompRow{
      /**  User ID  */  
   "DcdUserID":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "CurPlant":string,
      /**  List of Sites the user has access to.  */  
   "PlantList":string,
      /**  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  */  
   "PrimBuyerID":string,
      /**  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  */  
   "Name":string,
      /**  Initial height of the Overload Informer in pixels.  */  
   "OverloadInfHeight":number,
      /**  Initial overload informer sort option.  */  
   "OverloadInfSort":string,
      /**  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  */  
   "PrimSalesRepID":string,
      /**  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  */  
   "StartTaskSaleRepWB":boolean,
      /**  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  */  
   "StartTaskOppEnt":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  */  
   "StartOppSaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  */  
   "StartOrdSaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  */  
   "StartRMASaleRepWB":boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  */  
   "StartSCallSaleRepWB":boolean,
      /**  Unique identifier of the Workstations  */  
   "WorkstationID":string,
      /**  Employee ID  */  
   "EmpID":string,
      /**  Indicates if the user can update expense entries (EmpExpense) for any employee.  */  
   "CanUpdateExpense":boolean,
      /**  Indicates if the user can update time entries (LaborDtl) for any employee.  */  
   "CanUpdateTime":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  FWBLimitedRefresh  */  
   "FWBLimitedRefresh":boolean,
      /**  FWBUseDemandWhseOnly  */  
   "FWBUseDemandWhseOnly":boolean,
      /**  Is used by UIApps PurchaseContractScheduleEntry – it is used to set/toggle the Purchase Schedule Approval action menu item Part Schedule Shared Supplier Validation (SharedSupplierValidationToggleTool).  */  
   "SharedSupValidation":boolean,
      /**  TransactionRetrievalDays  */  
   "TransactionRetrievalDays":number,
   "BitFlag":number,
   "CompanyName":string,
   "DCDUserIDName":string,
   "EmpIDName":string,
   "WorkstationIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipNumOfDays
      @param ds
   */  
export interface ChangeTransactionRetrievalDays_input{
      /**  The amount of TransactionRetrievalDays for the current user.  */  
   ipNumOfDays:number,
   ds:Erp_Tablesets_UserCompSearchTableset[],
}

export interface ChangeTransactionRetrievalDays_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UserCompSearchTableset[],
}
}

   /** Required : 
      @param dcdUserID
   */  
export interface DeleteByID_input{
   dcdUserID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_UpdExtUserCompSearchTableset{
   UserComp:Erp_Tablesets_UserCompRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UserCompListRow{
      /**  User ID  */  
   DcdUserID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   CurPlant:string,
      /**  List of Sites the user has access to.  */  
   PlantList:string,
      /**  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  */  
   PrimBuyerID:string,
      /**  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  */  
   Name:string,
      /**  Initial height of the Overload Informer in pixels.  */  
   OverloadInfHeight:number,
      /**  Initial overload informer sort option.  */  
   OverloadInfSort:string,
      /**  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  */  
   PrimSalesRepID:string,
      /**  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  */  
   StartTaskSaleRepWB:boolean,
      /**  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  */  
   StartTaskOppEnt:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  */  
   StartOppSaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  */  
   StartOrdSaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  */  
   StartRMASaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  */  
   StartSCallSaleRepWB:boolean,
      /**  Unique identifier of the Workstations  */  
   WorkstationID:string,
      /**  Employee ID  */  
   EmpID:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Company Name  */  
   CompanyName:string,
      /**  User Name  */  
   DCDUserIDName:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   EmpIDName:string,
      /**  Description of the station  */  
   WorkstationIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UserCompListTableset{
   UserCompList:Erp_Tablesets_UserCompListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UserCompRow{
      /**  User ID  */  
   DcdUserID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   CurPlant:string,
      /**  List of Sites the user has access to.  */  
   PlantList:string,
      /**  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  */  
   PrimBuyerID:string,
      /**  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  */  
   Name:string,
      /**  Initial height of the Overload Informer in pixels.  */  
   OverloadInfHeight:number,
      /**  Initial overload informer sort option.  */  
   OverloadInfSort:string,
      /**  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  */  
   PrimSalesRepID:string,
      /**  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  */  
   StartTaskSaleRepWB:boolean,
      /**  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  */  
   StartTaskOppEnt:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  */  
   StartOppSaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  */  
   StartOrdSaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  */  
   StartRMASaleRepWB:boolean,
      /**  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  */  
   StartSCallSaleRepWB:boolean,
      /**  Unique identifier of the Workstations  */  
   WorkstationID:string,
      /**  Employee ID  */  
   EmpID:string,
      /**  Indicates if the user can update expense entries (EmpExpense) for any employee.  */  
   CanUpdateExpense:boolean,
      /**  Indicates if the user can update time entries (LaborDtl) for any employee.  */  
   CanUpdateTime:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  FWBLimitedRefresh  */  
   FWBLimitedRefresh:boolean,
      /**  FWBUseDemandWhseOnly  */  
   FWBUseDemandWhseOnly:boolean,
      /**  Is used by UIApps PurchaseContractScheduleEntry – it is used to set/toggle the Purchase Schedule Approval action menu item Part Schedule Shared Supplier Validation (SharedSupplierValidationToggleTool).  */  
   SharedSupValidation:boolean,
      /**  TransactionRetrievalDays  */  
   TransactionRetrievalDays:number,
   BitFlag:number,
   CompanyName:string,
   DCDUserIDName:string,
   EmpIDName:string,
   WorkstationIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UserCompSearchTableset{
   UserComp:Erp_Tablesets_UserCompRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param dcdUserID
   */  
export interface GetByID_input{
   dcdUserID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_UserCompSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_UserCompSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_UserCompSearchTableset[],
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
   returnObj:Erp_Tablesets_UserCompListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param dcdUserID
   */  
export interface GetNewUserComp_input{
   ds:Erp_Tablesets_UserCompSearchTableset[],
   dcdUserID:string,
}

export interface GetNewUserComp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UserCompSearchTableset[],
}
}

   /** Required : 
      @param whereClauseUserComp
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseUserComp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_UserCompSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param company
      @param dcdUserID
      @param days
   */  
export interface GetTransactionRetrievalDays_input{
      /**  The company used for the current user.  */  
   company:string,
      /**  The ID oF the current user.  */  
   dcdUserID:string,
      /**  The days from UserComp if there is any or from XaSyst.  */  
   days:number,
}

export interface GetTransactionRetrievalDays_output{
parameters : {
      /**  output parameters  */  
   days:number,
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
   ds:Erp_Tablesets_UpdExtUserCompSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtUserCompSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_UserCompSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UserCompSearchTableset[],
}
}

