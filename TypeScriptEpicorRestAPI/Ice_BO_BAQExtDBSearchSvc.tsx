import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.BAQExtDBSearchSvc
// Description: The BAQ external database search service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/$metadata", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQExtDSNRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDSNRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDSNRow)
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
   OperationID: GetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDSNRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDSNRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDSNList
   Description: Get full list of ODBC DSN
   OperationID: GetDSNList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDSNList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDSNList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetDSNList", {
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
   Summary: Invoke method GetList
   Description: Get full list of ODBC DSN - equal to GetDSNList. Used for ComboBox listing
   OperationID: Get_GetList
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetSqlDatabasesList
   Description: Get MS SQL server databases
   OperationID: GetSqlDatabasesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSqlDatabasesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSqlDatabasesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSqlDatabasesList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetSqlDatabasesList", {
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
   Summary: Invoke method GetProperties
   OperationID: GetProperties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetProperties_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProperties_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetProperties(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetProperties", {
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
   Summary: Invoke method GetDbProviderList
   Description: Gets the database provider list.
   OperationID: GetDbProviderList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDbProviderList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDbProviderList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetDbProviderList", {
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
   Summary: Invoke method TestConnection
   OperationID: TestConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestConnection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/TestConnection", {
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
   Summary: Invoke method TestServiceConnectivity
   OperationID: TestServiceConnectivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestServiceConnectivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestServiceConnectivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestServiceConnectivity(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/TestServiceConnectivity", {
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
   Summary: Invoke method TestDatasourceConnection
   Description: Test connection to the external data source by name
   OperationID: TestDatasourceConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestDatasourceConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestDatasourceConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestDatasourceConnection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/TestDatasourceConnection", {
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
   Summary: Invoke method GetTableListFromSearch
   Description: Get full list of tables from Recordset.Open for palette and code editor
   OperationID: GetTableListFromSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableListFromSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableListFromSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTableListFromSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetTableListFromSearch", {
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
   Summary: Invoke method GetTableList
   Description: Get full list of tables from Recordset.Open for palette and code editor
   OperationID: GetTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTableList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetTableList", {
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
   Summary: Invoke method TableExists
   Description: Checks is the table exists in the database
   OperationID: TableExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TableExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TableExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TableExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/TableExists", {
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
   Summary: Invoke method TableSchemaList
   OperationID: TableSchemaList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TableSchemaList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TableSchemaList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TableSchemaList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/TableSchemaList", {
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
   Summary: Invoke method GetFieldList
   Description: Get full list of columns for the specified table
datatableID can contain tables divided by commas
   OperationID: GetFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFieldList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetFieldList", {
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
   Summary: Invoke method GetConnectedTables
   OperationID: GetConnectedTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConnectedTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConnectedTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetConnectedTables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetConnectedTables", {
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
   Summary: Invoke method GetConnectionKeys
   OperationID: GetConnectionKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConnectionKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConnectionKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetConnectionKeys(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetConnectionKeys", {
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
   Summary: Invoke method GetFunctionList
   Description: MS SQL Functions
   OperationID: GetFunctionList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFunctionList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFunctionList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetFunctionList", {
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
   Summary: Invoke method GetTableFunctionFieldList
   Description: Get full list of columns for the specified table-value function
functionName can contain functions divided by commas
   OperationID: GetTableFunctionFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableFunctionFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableFunctionFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTableFunctionFieldList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetTableFunctionFieldList", {
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
   Summary: Invoke method GetFunctionParameterList
   Description: Get full list of paramters for the specified  function call
functionName can contain functions divided by commas
   OperationID: GetFunctionParameterList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFunctionParameterList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFunctionParameterList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFunctionParameterList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetFunctionParameterList", {
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
   Summary: Invoke method GetExecutionSettings
   Description: Execution settings required or supported by the external query system
   OperationID: GetExecutionSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExecutionSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExecutionSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExecutionSettings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BAQExtDBSearchSvc/GetExecutionSettings", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQExtDSNRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQExtDSNRow[],
}

export interface Ice_Tablesets_BAQExtDSNRow{
   "DSN":string,
   "Description":string,
   "DSNType":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param datasourceName
      @param tableSchema
      @param dataTableID
   */  
export interface GetConnectedTables_input{
   datasourceName:string,
   tableSchema:string,
   dataTableID:string,
}

export interface GetConnectedTables_output{
   returnObj:Ice_Tablesets_BAQExtConnectedTablesTableset[],
}

   /** Required : 
      @param datasourceName
      @param connectionSchema
      @param connectionID
      @param connectionType
   */  
export interface GetConnectionKeys_input{
   datasourceName:string,
   connectionSchema:string,
   connectionID:string,
   connectionType:string,
}

export interface GetConnectionKeys_output{
   returnObj:Ice_Tablesets_BAQExtConnectionKeysTableset[],
}

export interface GetDSNList_output{
   returnObj:Ice_Tablesets_BAQExtDSNTableset[],
}

export interface GetDbProviderList_output{
   returnObj:Ice_Tablesets_BAQExtDSNTableset[],
}

   /** Required : 
      @param datasourceName
   */  
export interface GetExecutionSettings_input{
   datasourceName:string,
}

export interface GetExecutionSettings_output{
   returnObj:Ice_Tablesets_BAQExtExecSettingListTableset[],
}

   /** Required : 
      @param DatasourceName
      @param catalog
      @param tableSchema
      @param dataTableID
   */  
export interface GetFieldList_input{
   DatasourceName:string,
   catalog:string,
   tableSchema:string,
   dataTableID:string,
}

export interface GetFieldList_output{
   returnObj:Ice_Tablesets_BAQExtDataFieldTableset[],
}

   /** Required : 
      @param datasourceName
      @param functionType
   */  
export interface GetFunctionList_input{
   datasourceName:string,
   functionType:number,
}

export interface GetFunctionList_output{
   returnObj:Ice_Tablesets_BAQExtDataTableTableset[],
}

   /** Required : 
      @param DatasourceName
      @param catalog
      @param tableSchema
      @param functionName
   */  
export interface GetFunctionParameterList_input{
   DatasourceName:string,
   catalog:string,
   tableSchema:string,
   functionName:string,
}

export interface GetFunctionParameterList_output{
   returnObj:Ice_Tablesets_BAQExtDataFieldTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Ice_Tablesets_BAQExtDSNTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param dbProviderType
      @param propertyGroup
   */  
export interface GetProperties_input{
   dbProviderType:string,
   propertyGroup:string,
}

export interface GetProperties_output{
   returnObj:Ice_Tablesets_BAQExtPropertiesTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_BAQExtDataTableTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param dbProviderType
      @param connStr
   */  
export interface GetSqlDatabasesList_input{
   dbProviderType:string,
   connStr:string,
}

export interface GetSqlDatabasesList_output{
   returnObj:Ice_Tablesets_BAQExtPropertiesTableset[],
}

   /** Required : 
      @param DatasourceName
      @param catalog
      @param tableSchema
      @param functionName
   */  
export interface GetTableFunctionFieldList_input{
   DatasourceName:string,
   catalog:string,
   tableSchema:string,
   functionName:string,
}

export interface GetTableFunctionFieldList_output{
   returnObj:Ice_Tablesets_BAQExtDataFieldTableset[],
}

   /** Required : 
      @param datasourceName
      @param schemaName
      @param startTableName
   */  
export interface GetTableListFromSearch_input{
   datasourceName:string,
   schemaName:string,
   startTableName:string,
}

export interface GetTableListFromSearch_output{
   returnObj:Ice_Tablesets_BAQExtDataTableTableset[],
}

   /** Required : 
      @param DatasourceName
   */  
export interface GetTableList_input{
   DatasourceName:string,
}

export interface GetTableList_output{
   returnObj:Ice_Tablesets_BAQExtDataTableTableset[],
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

export interface Ice_Tablesets_BAQExtConnectedTablesRow{
   ConnectedTableID:string,
   ConnectedTableSchema:string,
   ConnectionID:string,
   ConnectionType:string,
   DataTableID:string,
   TableSchema:string,
   SortPriority:number,
   ConnectionSchema:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtConnectedTablesTableset{
   BAQExtConnectedTables:Ice_Tablesets_BAQExtConnectedTablesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQExtConnectionKeysRow{
   FromColumn:string,
   ToColumn:string,
   Ordinal:number,
   FromIsExpr:boolean,
   ToIsExpr:boolean,
   CompOp:string,
   AndOr:string,
   Not:boolean,
   LeftP:string,
   RightP:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtConnectionKeysTableset{
   BAQExtConnectionKeys:Ice_Tablesets_BAQExtConnectionKeysRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQExtDSNRow{
   DSN:string,
   Description:string,
   DSNType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtDSNTableset{
   BAQExtDSN:Ice_Tablesets_BAQExtDSNRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQExtDataFieldRow{
   TableID:string,
   FieldName:string,
   Seq:number,
   Description:string,
   DataType:string,
   SQLDataType:string,
   CharMaxLen:number,
   NumericPrecision:number,
   NumericScale:number,
   Mandatory:boolean,
   ReadOnly:boolean,
   FieldFormat:string,
   IsPrimaryKey:boolean,
   FieldLabel:string,
   SchemaName:string,
   TableName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtDataFieldTableset{
   BAQExtDataField:Ice_Tablesets_BAQExtDataFieldRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQExtDataTableRow{
   TableID:string,
   Description:string,
   TableType:string,
   DBSchemaName:string,
   FullTableName:string,
   Catalog:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtDataTableTableset{
   BAQExtDataTable:Ice_Tablesets_BAQExtDataTableRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQExtExecSettingListRow{
   SettingID:string,
   SettingType:string,
   DefaultValue:string,
   Required:boolean,
   IsEnum:boolean,
   Description:string,
   Category:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtExecSettingListTableset{
   BAQExtExecSettingList:Ice_Tablesets_BAQExtExecSettingListRow[],
   BAQExtExecSettingValues:Ice_Tablesets_BAQExtExecSettingValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQExtExecSettingValuesRow{
   SettingID:string,
   SettingValueOrder:number,
   SettingEnumValue:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQExtPropertiesTableset{
   BAQExtProviderProperties:Ice_Tablesets_BAQExtProviderPropertiesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQExtProviderPropertiesRow{
   Name:string,
   Value:string,
   Description:string,
   Type:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param DatasourceName
      @param tableSchema
      @param dataTableID
   */  
export interface TableExists_input{
   DatasourceName:string,
   tableSchema:string,
   dataTableID:string,
}

export interface TableExists_output{
   returnObj:Ice_Tablesets_BAQExtDataTableTableset[],
}

   /** Required : 
      @param DatasourceName
   */  
export interface TableSchemaList_input{
   DatasourceName:string,
}

export interface TableSchemaList_output{
   returnObj:string,
}

   /** Required : 
      @param connStr
      @param odbcDBType
   */  
export interface TestConnection_input{
   connStr:string,
   odbcDBType:string,
}

export interface TestConnection_output{
}

   /** Required : 
      @param DatasourceName
   */  
export interface TestDatasourceConnection_input{
      /**  Name of the data source  */  
   DatasourceName:string,
}

export interface TestDatasourceConnection_output{
}

   /** Required : 
      @param url
      @param clientID
      @param pwd
      @param stringAppType
   */  
export interface TestServiceConnectivity_input{
   url:string,
   clientID:string,
   pwd:string,
   stringAppType:string,
}

export interface TestServiceConnectivity_output{
}

