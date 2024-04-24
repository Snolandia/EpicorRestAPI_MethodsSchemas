import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.BORelationSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/$metadata", {
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
   Summary: Invoke method GetBODataset
   Description: Gets the BO dataset.
   OperationID: GetBODataset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBODataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBODataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBODataset(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/GetBODataset", {
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
   Summary: Invoke method GetBOTables
   Description: Gets the BO tables.
   OperationID: GetBOTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBOTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBOTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBOTables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/GetBOTables", {
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
   Summary: Invoke method GetPrimaryTable
   Description: Gets the primary table.
   OperationID: GetPrimaryTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrimaryTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimaryTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPrimaryTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/GetPrimaryTable", {
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
   Summary: Invoke method GetDatasetTables
   Description: Gets the tables from specified dataset.
   OperationID: GetDatasetTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDatasetTables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/GetDatasetTables", {
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
   Summary: Invoke method GetBOPKFields
   Description: Returns list of the BO's primary table's PK fields delimited by semicolon
   OperationID: GetBOPKFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBOPKFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBOPKFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBOPKFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.BORelationSearchSvc/GetBOPKFields", {
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
      @param systemCode
      @param boName
      @param ds
   */  
export interface GetBODataset_input{
      /**  The system code.  */  
   systemCode:string,
      /**  The BO name  */  
   boName:string,
   ds:Ice_Tablesets_BORelationSearchTableset[],
}

export interface GetBODataset_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BORelationSearchTableset[],
}
}

   /** Required : 
      @param SystemCode
      @param BOName
   */  
export interface GetBOPKFields_input{
   SystemCode:string,
      /**  name of the BO  */  
   BOName:string,
}

export interface GetBOPKFields_output{
parameters : {
      /**  output parameters  */  
   DBTableName:string,
   PKFieldsStr:string,
}
}

   /** Required : 
      @param systemCode
      @param boName
      @param ds
   */  
export interface GetBOTables_input{
      /**  The system code.  */  
   systemCode:string,
      /**  The BO name  */  
   boName:string,
   ds:Ice_Tablesets_BORelationSearchTableset[],
}

export interface GetBOTables_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BORelationSearchTableset[],
}
}

   /** Required : 
      @param systemCode
      @param boName
      @param datasetID
      @param ds
   */  
export interface GetDatasetTables_input{
   systemCode:string,
   boName:string,
   datasetID:string,
   ds:Ice_Tablesets_BORelationSearchTableset[],
}

export interface GetDatasetTables_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_BORelationSearchTableset[],
}
}

   /** Required : 
      @param systemCode
      @param boName
   */  
export interface GetPrimaryTable_input{
      /**  The system code.  */  
   systemCode:string,
      /**  Name of the BO.  */  
   boName:string,
}

export interface GetPrimaryTable_output{
      /**  Table's logical ID for BO's primary table  */  
   returnObj:string,
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

export interface Ice_Tablesets_BOFieldLinksRow{
   LinkID:number,
   Seq:number,
   TableField:string,
   ForeignTableField:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BORelationSearchTableset{
   BOTableTree:Ice_Tablesets_BOTableTreeRow[],
   BOTableParentLinks:Ice_Tablesets_BOTableParentLinksRow[],
   BOTableLinks:Ice_Tablesets_BOTableLinksRow[],
   BOFieldLinks:Ice_Tablesets_BOFieldLinksRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BOTableLinksRow{
   LinkID:number,
   SystemCode:string,
   BOName:string,
   DataTableID:string,
   ForeignTableID:string,
   ForeignSystemCode:string,
   ForeignBOName:string,
   LookupID:string,
   IsChildObject:boolean,
   DBTableName:string,
   ForeignDBTableName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BOTableParentLinksRow{
   SystemCode:string,
   BOName:string,
   Seq:number,
   ChildFieldName:string,
   ParentFieldName:string,
   DataTableID:string,
   IsLinkToConstant:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BOTableTreeRow{
   SystemCode:string,
      /**  Business object name  */  
   BOName:string,
   DataTableID:string,
   DBTableName:string,
   ParentTableID:string,
   ParentTableName:string,
   IsPrimaryTable:boolean,
   HasLinks:boolean,
   Seq:number,
   ParentRelationID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

