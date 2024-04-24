import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.SchemaSvc
// Description: This is the Schema main business object.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/$metadata", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.FileSchemaRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_FileSchemaRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_FileSchemaRow)
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
   Description: This method returns the Data Schema records
   OperationID: Get_GetRows
      @param whereClause Desc: Data Table Where Clause   Required: True   Allow empty value : True
      @param pageSize Desc: Page Size   Required: True
      @param absolutePage Desc: Absolute Page   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetRows" + params, {
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
   Summary: Invoke method GetFieldByID
   Description: This method returns a field dataset for the given table/field
   OperationID: GetFieldByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFieldByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetFieldByID", {
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
   Description: This method returns a list of fields for the given table
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetFieldList", {
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
   Summary: Invoke method ValidateTableName
   Description: This method returns true if the table name is exist
   OperationID: ValidateTableName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTableName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTableName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateTableName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/ValidateTableName", {
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
   Summary: Invoke method ValidateFieldName
   Description: This method returns true if the table name is exist
   OperationID: ValidateFieldName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFieldName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFieldName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFieldName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/ValidateFieldName", {
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
   Summary: Invoke method GetFileByID
   Description: This method returns a fileSchema dataset for the given table
   OperationID: GetFileByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFileByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFileByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFileByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetFileByID", {
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
   Summary: Invoke method GetFileList
   Description: This method returns a fileSchema dataset for the given criteria
   OperationID: GetFileList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFileList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFileList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFileList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetFileList", {
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
   Summary: Invoke method GetIndexByID
   Description: This method returns an index dataset for the given table/index
   OperationID: GetIndexByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIndexByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIndexByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIndexByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetIndexByID", {
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
   Summary: Invoke method GetIndexFieldByID
   Description: This method returns an index field dataset for the given table/index/sequence
   OperationID: GetIndexFieldByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIndexFieldByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIndexFieldByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIndexFieldByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetIndexFieldByID", {
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
   Summary: Invoke method GetIndexFieldList
   Description: This method returns a list of index fields for the given table/index
   OperationID: GetIndexFieldList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIndexFieldList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIndexFieldList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIndexFieldList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetIndexFieldList", {
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
   Summary: Invoke method GetIndexList
   Description: This method returns a list of indexes in a table
   OperationID: GetIndexList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIndexList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIndexList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIndexList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetIndexList", {
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
   Summary: Invoke method GetList
   Description: This method returns the Data Schema records
   OperationID: Get_GetList
      @param whereClause Desc: Data Table Where Clause   Required: True   Allow empty value : True
      @param pageSize Desc: Page Size   Required: True
      @param absolutePage Desc: Absolute Page   Required: True
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetList" + params, {
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
   Summary: Invoke method TableSchemaList
   Description: This method returns the Data Schema records
   OperationID: TableSchemaList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/TableSchemaList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TableSchemaList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/TableSchemaList", {
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
   Summary: Invoke method GetTableInfo
   OperationID: GetTableInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTableInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTableInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTableInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetTableInfo", {
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
   Summary: Invoke method GetDictionaryTableByID
   Description: This method returns a fileSchema dataset for the given table
   OperationID: GetDictionaryTableByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDictionaryTableByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDictionaryTableByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDictionaryTableByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetDictionaryTableByID", {
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
   Summary: Invoke method GetDictionaryTableByIDWithSortingFields
   Description: This method returns a fileSchema dataset for the given table
   OperationID: GetDictionaryTableByIDWithSortingFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDictionaryTableByIDWithSortingFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDictionaryTableByIDWithSortingFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDictionaryTableByIDWithSortingFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.SchemaSvc/GetDictionaryTableByIDWithSortingFields", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_FileSchemaRow{
   "odatametadata":string,
   "value":Ice_Tablesets_FileSchemaRow[],
}

export interface Ice_Tablesets_FileSchemaRow{
   "TableName":string,
   "PrimeIndex":number,
   "NumFields":number,
   "Description":string,
   "ValidationExp":string,
   "ValidationMsg":string,
   "Version":number,
   "TableType":string,
   "SysRowID":string,
      /**  Schema Name  */  
   "SchemaName":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param schemaName
      @param pcFile
      @param sortingFields
   */  
export interface GetDictionaryTableByIDWithSortingFields_input{
      /**  Schema name of the table  */  
   schemaName:string,
      /**  name of the table  */  
   pcFile:string,
      /**  sorting of Fields  */  
   sortingFields:number,
}

export interface GetDictionaryTableByIDWithSortingFields_output{
   returnObj:Ice_Tablesets_DictionaryTableSchemaTableset[],
}

   /** Required : 
      @param schemaName
      @param pcFile
   */  
export interface GetDictionaryTableByID_input{
      /**  Schema name of the table  */  
   schemaName:string,
      /**  name of the table  */  
   pcFile:string,
}

export interface GetDictionaryTableByID_output{
   returnObj:Ice_Tablesets_DictionaryTableSchemaTableset[],
}

   /** Required : 
      @param schemaName
      @param pcFile
      @param pcField
   */  
export interface GetFieldByID_input{
      /**  schema name of the field  */  
   schemaName:string,
      /**  name of the table  */  
   pcFile:string,
      /**  name of the field  */  
   pcField:string,
}

export interface GetFieldByID_output{
   returnObj:Ice_Tablesets_FieldSchemaTableset[],
}

   /** Required : 
      @param schemaName
      @param pcFile
   */  
export interface GetFieldList_input{
      /**  schema name of the table  */  
   schemaName:string,
      /**  name of the table  */  
   pcFile:string,
}

export interface GetFieldList_output{
   returnObj:Ice_Tablesets_FieldSchemaTableset[],
}

   /** Required : 
      @param schemaName
      @param tableName
   */  
export interface GetFileByID_input{
      /**  Schema name of the table  */  
   schemaName:string,
      /**  name of the table  */  
   tableName:string,
}

export interface GetFileByID_output{
   returnObj:Ice_Tablesets_FileSchemaTableset[],
}

   /** Required : 
      @param pcWhere
   */  
export interface GetFileList_input{
      /**  where clause  */  
   pcWhere:string,
}

export interface GetFileList_output{
   returnObj:Ice_Tablesets_FileSchemaTableset[],
}

   /** Required : 
      @param schemaName
      @param pcFile
      @param pcIndex
   */  
export interface GetIndexByID_input{
      /**  name of the table  */  
   schemaName:string,
      /**  name of the table  */  
   pcFile:string,
      /**  name of the index  */  
   pcIndex:string,
}

export interface GetIndexByID_output{
   returnObj:Ice_Tablesets_IndexSchemaTableset[],
}

   /** Required : 
      @param schemaName
      @param pcFile
      @param pcIndex
      @param piSeq
   */  
export interface GetIndexFieldByID_input{
      /**  Schema name of the table  */  
   schemaName:string,
      /**  name of the table  */  
   pcFile:string,
      /**  name of the index  */  
   pcIndex:string,
      /**  the sequence number in the index  */  
   piSeq:number,
}

export interface GetIndexFieldByID_output{
   returnObj:Ice_Tablesets_IndexFieldSchemaTableset[],
}

   /** Required : 
      @param schemaName
      @param pcFile
      @param pcIndex
   */  
export interface GetIndexFieldList_input{
      /**  Schema name of the table  */  
   schemaName:string,
      /**  name of the table  */  
   pcFile:string,
      /**  name of the index  */  
   pcIndex:string,
}

export interface GetIndexFieldList_output{
   returnObj:Ice_Tablesets_IndexFieldSchemaTableset[],
}

   /** Required : 
      @param schemaName
      @param pcFile
   */  
export interface GetIndexList_input{
      /**  Schema name of the table  */  
   schemaName:string,
      /**  name of the table  */  
   pcFile:string,
}

export interface GetIndexList_output{
   returnObj:Ice_Tablesets_IndexSchemaTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  Data Table Where Clause  */  
   whereClause:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Ice_Tablesets_FileSchemaTableset[],
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
export interface GetRows_input{
      /**  Data Table Where Clause  */  
   whereClause:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_FileSchemaTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param schemaName
      @param pcFile
   */  
export interface GetTableInfo_input{
   schemaName:string,
   pcFile:string,
}

export interface GetTableInfo_output{
   returnObj:Ice_Tablesets_DictionaryTableSchemaTableset[],
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

export interface Ice_Tablesets_DictionaryTableSchemaTableset{
   FileSchema:Ice_Tablesets_FileSchemaRow[],
   FieldSchema:Ice_Tablesets_FieldSchemaRow[],
   IndexSchema:Ice_Tablesets_IndexSchemaRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_FieldSchemaRow{
   TableName:string,
   FileRecid:number,
   FieldName:string,
   DataType:string,
   InitialValue:string,
   FieldLabel:string,
   Mandatory:boolean,
   FieldFormat:string,
   FieldDecimals:number,
   FieldSeq:number,
   FieldExtent:number,
   ValidationExp:string,
   ValidationMsg:string,
   FieldHelp:string,
   Description:string,
   ColumnLabel:string,
   ViewAs:string,
   FieldWidth:number,
   SysRowID:string,
   PrimaryKey:boolean,
   Mapping:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_FieldSchemaTableset{
   FieldSchema:Ice_Tablesets_FieldSchemaRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_FileSchemaRow{
   TableName:string,
   PrimeIndex:number,
   NumFields:number,
   Description:string,
   ValidationExp:string,
   ValidationMsg:string,
   Version:number,
   TableType:string,
   SysRowID:string,
      /**  Schema Name  */  
   SchemaName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_FileSchemaTableset{
   FileSchema:Ice_Tablesets_FileSchemaRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_IndexFieldSchemaRow{
   TableName:string,
   IndexName:string,
   IndexRecid:number,
   IndexSeq:number,
   FieldRecid:number,
   FieldName:string,
   IsAscending:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_IndexFieldSchemaTableset{
   IndexFieldSchema:Ice_Tablesets_IndexFieldSchemaRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_IndexSchemaRow{
   TableName:string,
   FileRecid:number,
   IndexName:string,
   IsPrimary:boolean,
   IsUnique:boolean,
   NumComp:number,
   IndexNum:number,
   Active:boolean,
   WordIndex:number,
   Description:string,
   SysRowID:string,
   Fields:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_IndexSchemaTableset{
   IndexSchema:Ice_Tablesets_IndexSchemaRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface TableSchemaList_output{
   returnObj:string,
}

   /** Required : 
      @param schemaName
      @param tableName
      @param fieldName
   */  
export interface ValidateFieldName_input{
      /**  Schema name of the table  */  
   schemaName:string,
      /**  name of the table  */  
   tableName:string,
      /**  name of the table  */  
   fieldName:string,
}

export interface ValidateFieldName_output{
      /**  The dataset represents the file object  */  
   returnObj:boolean,
}

   /** Required : 
      @param schemaName
      @param tableName
   */  
export interface ValidateTableName_input{
      /**  Schema name of the table  */  
   schemaName:string,
      /**  name of the table  */  
   tableName:string,
}

export interface ValidateTableName_output{
      /**  The dataset represents the file object  */  
   returnObj:boolean,
}

