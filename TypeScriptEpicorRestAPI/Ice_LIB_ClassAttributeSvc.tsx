import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.ClassAttributeSvc
// Description: Provides attributes for a service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/$metadata", {
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



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetAttributes
   Description: Get Attributes for set of class names and namespace
   OperationID: GetAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAttributes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/GetAttributes", {
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
   Summary: Invoke method GetAttributesForAllTables
   Description: Get attributes for a set of class names and namespace (including Extension tables if in the list).
   OperationID: GetAttributesForAllTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributesForAllTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributesForAllTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAttributesForAllTables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/GetAttributesForAllTables", {
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
   Summary: Invoke method GetAttributesForTable
   Description: Get Attributes for one table
   OperationID: GetAttributesForTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributesForTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributesForTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAttributesForTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/GetAttributesForTable", {
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
   Summary: Invoke method GetAllAttributesForTables
   Description: Gets the base and user defined attributes for several tables
   OperationID: GetAllAttributesForTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllAttributesForTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllAttributesForTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllAttributesForTables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/GetAllAttributesForTables", {
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
   Summary: Invoke method GetAttributesForTables
   Description: Get Attributes for several tables - must be qualified as SchemaName.DataTableID
   OperationID: GetAttributesForTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributesForTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributesForTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAttributesForTables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/GetAttributesForTables", {
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
   Summary: Invoke method GetUDColumns
   Description: Get Attributes for set of ud class names and namespace
   OperationID: GetUDColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUDColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUDColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUDColumns(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/GetUDColumns", {
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
   Summary: Invoke method GetAttributesForExtensionTable
   Description: Get attributes for the extension tables, defined for the main dataset in the class
   OperationID: GetAttributesForExtensionTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributesForExtensionTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributesForExtensionTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAttributesForExtensionTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClassAttributeSvc/GetAttributesForExtensionTable", {
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



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param dataTables
      @param propertiesFilter
   */  
export interface GetAllAttributesForTables_input{
      /**  The list of data tables. Must be qualified as SystemCode.DataTableID~DataSetID.
            The DataSetID is used to retrieve Peer Extension tables and columns. If not present, only ERP ZData based tables will be returned.  */  
   dataTables:string,
      /**  The properties to filter the results.  */  
   propertiesFilter:string,
}

export interface GetAllAttributesForTables_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param companyID
      @param classNames
      @param nameSpace
   */  
export interface GetAttributesForAllTables_input{
      /**  company ID.  */  
   companyID:string,
      /**  list of class names.  */  
   classNames:string,
      /**  Namespace (Ex: Ice, Erp).  */  
   nameSpace:string,
}

export interface GetAttributesForAllTables_output{
   returnObj:Ice_Tablesets_ClassAttributeTableset[],
}

   /** Required : 
      @param companyID
      @param classNames
      @param nameSpace
   */  
export interface GetAttributesForExtensionTable_input{
      /**  Company ID where extension table is defined. If empty, current company will be used.  */  
   companyID:string,
      /**  Class name or class names, separated by comma  */  
   classNames:string,
      /**  Namespace for the class(es)  */  
   nameSpace:string,
}

export interface GetAttributesForExtensionTable_output{
   returnObj:Ice_Tablesets_ClassAttributeTableset[],
}

   /** Required : 
      @param schemaName
      @param dataTableID
   */  
export interface GetAttributesForTable_input{
   schemaName:string,
   dataTableID:string,
}

export interface GetAttributesForTable_output{
   returnObj:Ice_Tablesets_ClassAttributeTableset[],
}

   /** Required : 
      @param dataTables
   */  
export interface GetAttributesForTables_input{
   dataTables:string,
}

export interface GetAttributesForTables_output{
   returnObj:Ice_Tablesets_ClassAttributeTableset[],
}

   /** Required : 
      @param classNames
      @param nameSpace
   */  
export interface GetAttributes_input{
   classNames:string,
   nameSpace:string,
}

export interface GetAttributes_output{
   returnObj:Ice_Tablesets_ClassAttributeTableset[],
}

   /** Required : 
      @param classNames
      @param nameSpace
   */  
export interface GetUDColumns_input{
   classNames:string,
   nameSpace:string,
}

export interface GetUDColumns_output{
   returnObj:Ice_Tablesets_ClassAttributeTableset[],
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

export interface Ice_Tablesets_ClassAttributeRow{
   DataSetID:string,
   DataTableID:string,
   FieldName:string,
   AttributeName:string,
   AttributeValue:string,
   ClassName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ClassAttributeTableset{
   ClassAttribute:Ice_Tablesets_ClassAttributeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

