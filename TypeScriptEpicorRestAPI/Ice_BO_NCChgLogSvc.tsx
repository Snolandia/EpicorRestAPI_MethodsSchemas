import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.NCChgLogSvc
// Description: The change log service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/$metadata", {
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
   Description: Get NCChgLogs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NCChgLogs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.NCChgLogRow
   */  
export function get_NCChgLogs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NCChgLogRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/NCChgLogs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NCChgLogRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NCChgLogs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.NCChgLogRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.NCChgLogRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NCChgLogs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/NCChgLogs", {
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
   Summary: Calls GetByID to retrieve the NCChgLog item
   Description: Calls GetByID to retrieve the NCChgLog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NCChgLog
      @param Identifier Desc: Identifier   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param Key7 Desc: Key7   Required: True   Allow empty value : True
      @param Key8 Desc: Key8   Required: True   Allow empty value : True
      @param Key9 Desc: Key9   Required: True   Allow empty value : True
      @param Key10 Desc: Key10   Required: True   Allow empty value : True
      @param DateStamp Desc: DateStamp   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.NCChgLogRow
   */  
export function get_NCChgLogs_Identifier_TableName_Key1_Key2_Key3_Key4_Key5_Key6_Key7_Key8_Key9_Key10_DateStamp(Identifier:string, TableName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, Key7:string, Key8:string, Key9:string, Key10:string, DateStamp:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_NCChgLogRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/NCChgLogs(" + Identifier + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + Key7 + "," + Key8 + "," + Key9 + "," + Key10 + "," + DateStamp + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_NCChgLogRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update NCChgLog for the service
   Description: Calls UpdateExt to update NCChgLog. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NCChgLog
      @param Identifier Desc: Identifier   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param Key7 Desc: Key7   Required: True   Allow empty value : True
      @param Key8 Desc: Key8   Required: True   Allow empty value : True
      @param Key9 Desc: Key9   Required: True   Allow empty value : True
      @param Key10 Desc: Key10   Required: True   Allow empty value : True
      @param DateStamp Desc: DateStamp   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.NCChgLogRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_NCChgLogs_Identifier_TableName_Key1_Key2_Key3_Key4_Key5_Key6_Key7_Key8_Key9_Key10_DateStamp(Identifier:string, TableName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, Key7:string, Key8:string, Key9:string, Key10:string, DateStamp:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/NCChgLogs(" + Identifier + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + Key7 + "," + Key8 + "," + Key9 + "," + Key10 + "," + DateStamp + ")", {
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
   Summary: Call UpdateExt to delete NCChgLog item
   Description: Call UpdateExt to delete NCChgLog item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NCChgLog
      @param Identifier Desc: Identifier   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param Key7 Desc: Key7   Required: True   Allow empty value : True
      @param Key8 Desc: Key8   Required: True   Allow empty value : True
      @param Key9 Desc: Key9   Required: True   Allow empty value : True
      @param Key10 Desc: Key10   Required: True   Allow empty value : True
      @param DateStamp Desc: DateStamp   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_NCChgLogs_Identifier_TableName_Key1_Key2_Key3_Key4_Key5_Key6_Key7_Key8_Key9_Key10_DateStamp(Identifier:string, TableName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, Key7:string, Key8:string, Key9:string, Key10:string, DateStamp:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/NCChgLogs(" + Identifier + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + Key7 + "," + Key8 + "," + Key9 + "," + Key10 + "," + DateStamp + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.NCChgLogListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NCChgLogListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NCChgLogListRow)
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
export function get_GetRows(whereClauseNCChgLog:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseNCChgLog!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseNCChgLog=" + whereClauseNCChgLog
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(identifier:string, tableName:string, key1:string, key2:string, key3:string, key4:string, key5:string, key6:string, key7:string, key8:string, key9:string, key10:string, dateStamp:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof identifier!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "identifier=" + identifier
   }
   if(typeof tableName!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tableName=" + tableName
   }
   if(typeof key1!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key1=" + key1
   }
   if(typeof key2!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key2=" + key2
   }
   if(typeof key3!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key3=" + key3
   }
   if(typeof key4!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key4=" + key4
   }
   if(typeof key5!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key5=" + key5
   }
   if(typeof key6!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key6=" + key6
   }
   if(typeof key7!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key7=" + key7
   }
   if(typeof key8!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key8=" + key8
   }
   if(typeof key9!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key9=" + key9
   }
   if(typeof key10!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key10=" + key10
   }
   if(typeof dateStamp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "dateStamp=" + dateStamp
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/GetList" + params, {
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
   Summary: Invoke method GetNewNCChgLog
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNCChgLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewNCChgLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNCChgLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewNCChgLog(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/GetNewNCChgLog", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.NCChgLogSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NCChgLogListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_NCChgLogListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NCChgLogRow{
   "odatametadata":string,
   "value":Ice_Tablesets_NCChgLogRow[],
}

export interface Ice_Tablesets_NCChgLogListRow{
      /**  Identifies the source of the change text.  (i.e. PO, SO).  */  
   "Identifier":string,
      /**  Name of the table which was changed  */  
   "TableName":string,
      /**  Major component of the foreign key of the related master record.  For example: For a "PO" change record this field would contain the related PO Number,  for a "SO" change record it would contain the related SO Number.  */  
   "Key1":string,
      /**  Second component of the foreign key of the related master record.  For example: For a "PODetail" change record this field would contain the related PO Line Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" do not use this field while changes to "PODetail" and "PORel" do.  */  
   "Key2":string,
      /**  Third component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key3":string,
      /**  Fourth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key4":string,
      /**  Fifth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key5":string,
      /**  Major component of the foreign key of the related master record.  For example: For a "PO" change record this field would contain the related PO Number,  for a "SO" change record it would contain the related SO Number.  */  
   "Key6":string,
      /**  Second component of the foreign key of the related master record.  For example: For a "PODetail" change record this field would contain the related PO Line Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" do not use this field while changes to "PODetail" and "PORel" do.  */  
   "Key7":string,
      /**  Third component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key8":string,
      /**  Fourth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key9":string,
      /**  Fifth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key10":string,
      /**  Date this log record was created.  */  
   "DateStamp":string,
      /**   Log message text.  This text may be in the following formats:
1) "New Record"
2) UserID  Time  FieldLabel/Name  OldValue "->" NewValue  */  
   "LogText":string,
      /**  Database level  */  
   "DBLevel":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_NCChgLogRow{
      /**  Identifies the source of the change text.  (i.e. PO, SO).  */  
   "Identifier":string,
      /**  Name of the table which was changed  */  
   "TableName":string,
      /**  Major component of the foreign key of the related master record.  For example: For a "PO" change record this field would contain the related PO Number,  for a "SO" change record it would contain the related SO Number.  */  
   "Key1":string,
      /**  Second component of the foreign key of the related master record.  For example: For a "PODetail" change record this field would contain the related PO Line Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" do not use this field while changes to "PODetail" and "PORel" do.  */  
   "Key2":string,
      /**  Third component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key3":string,
      /**  Fourth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key4":string,
      /**  Fifth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key5":string,
      /**  Major component of the foreign key of the related master record.  For example: For a "PO" change record this field would contain the related PO Number,  for a "SO" change record it would contain the related SO Number.  */  
   "Key6":string,
      /**  Second component of the foreign key of the related master record.  For example: For a "PODetail" change record this field would contain the related PO Line Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" do not use this field while changes to "PODetail" and "PORel" do.  */  
   "Key7":string,
      /**  Third component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key8":string,
      /**  Fourth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key9":string,
      /**  Fifth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   "Key10":string,
      /**  Date this log record was created.  */  
   "DateStamp":string,
      /**   Log message text.  This text may be in the following formats:
1) "New Record"
2) UserID  Time  FieldLabel/Name  OldValue "->" NewValue  */  
   "LogText":string,
      /**  Database level  */  
   "DBLevel":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param identifier
      @param tableName
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
      @param key7
      @param key8
      @param key9
      @param key10
      @param dateStamp
   */  
export interface DeleteByID_input{
   identifier:string,
   tableName:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
   key7:string,
   key8:string,
   key9:string,
   key10:string,
   dateStamp:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param identifier
      @param tableName
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
      @param key7
      @param key8
      @param key9
      @param key10
      @param dateStamp
   */  
export interface GetByID_input{
   identifier:string,
   tableName:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
   key7:string,
   key8:string,
   key9:string,
   key10:string,
   dateStamp:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_NCChgLogTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_NCChgLogTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_NCChgLogTableset[],
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
   returnObj:Ice_Tablesets_NCChgLogListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param identifier
      @param tableName
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
      @param key7
      @param key8
      @param key9
      @param key10
   */  
export interface GetNewNCChgLog_input{
   ds:Ice_Tablesets_NCChgLogTableset[],
   identifier:string,
   tableName:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
   key7:string,
   key8:string,
   key9:string,
   key10:string,
}

export interface GetNewNCChgLog_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_NCChgLogTableset[],
}
}

   /** Required : 
      @param whereClauseNCChgLog
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseNCChgLog:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_NCChgLogTableset[],
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

export interface Ice_Tablesets_NCChgLogListRow{
      /**  Identifies the source of the change text.  (i.e. PO, SO).  */  
   Identifier:string,
      /**  Name of the table which was changed  */  
   TableName:string,
      /**  Major component of the foreign key of the related master record.  For example: For a "PO" change record this field would contain the related PO Number,  for a "SO" change record it would contain the related SO Number.  */  
   Key1:string,
      /**  Second component of the foreign key of the related master record.  For example: For a "PODetail" change record this field would contain the related PO Line Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" do not use this field while changes to "PODetail" and "PORel" do.  */  
   Key2:string,
      /**  Third component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key3:string,
      /**  Fourth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key4:string,
      /**  Fifth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key5:string,
      /**  Major component of the foreign key of the related master record.  For example: For a "PO" change record this field would contain the related PO Number,  for a "SO" change record it would contain the related SO Number.  */  
   Key6:string,
      /**  Second component of the foreign key of the related master record.  For example: For a "PODetail" change record this field would contain the related PO Line Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" do not use this field while changes to "PODetail" and "PORel" do.  */  
   Key7:string,
      /**  Third component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key8:string,
      /**  Fourth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key9:string,
      /**  Fifth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key10:string,
      /**  Date this log record was created.  */  
   DateStamp:string,
      /**   Log message text.  This text may be in the following formats:
1) "New Record"
2) UserID  Time  FieldLabel/Name  OldValue "->" NewValue  */  
   LogText:string,
      /**  Database level  */  
   DBLevel:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_NCChgLogListTableset{
   NCChgLogList:Ice_Tablesets_NCChgLogListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_NCChgLogRow{
      /**  Identifies the source of the change text.  (i.e. PO, SO).  */  
   Identifier:string,
      /**  Name of the table which was changed  */  
   TableName:string,
      /**  Major component of the foreign key of the related master record.  For example: For a "PO" change record this field would contain the related PO Number,  for a "SO" change record it would contain the related SO Number.  */  
   Key1:string,
      /**  Second component of the foreign key of the related master record.  For example: For a "PODetail" change record this field would contain the related PO Line Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" do not use this field while changes to "PODetail" and "PORel" do.  */  
   Key2:string,
      /**  Third component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key3:string,
      /**  Fourth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key4:string,
      /**  Fifth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key5:string,
      /**  Major component of the foreign key of the related master record.  For example: For a "PO" change record this field would contain the related PO Number,  for a "SO" change record it would contain the related SO Number.  */  
   Key6:string,
      /**  Second component of the foreign key of the related master record.  For example: For a "PODetail" change record this field would contain the related PO Line Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" do not use this field while changes to "PODetail" and "PORel" do.  */  
   Key7:string,
      /**  Third component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key8:string,
      /**  Fourth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key9:string,
      /**  Fifth component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key10:string,
      /**  Date this log record was created.  */  
   DateStamp:string,
      /**   Log message text.  This text may be in the following formats:
1) "New Record"
2) UserID  Time  FieldLabel/Name  OldValue "->" NewValue  */  
   LogText:string,
      /**  Database level  */  
   DBLevel:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_NCChgLogTableset{
   NCChgLog:Ice_Tablesets_NCChgLogRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtNCChgLogTableset{
   NCChgLog:Ice_Tablesets_NCChgLogRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtNCChgLogTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtNCChgLogTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_NCChgLogTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_NCChgLogTableset[],
}
}

