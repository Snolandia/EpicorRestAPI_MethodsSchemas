import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CalculatedFieldSvc
// Description: CalculateField service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/$metadata", {
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
   Summary: Invoke method GetByRelatedTo
   Description: Generic get method for any related to entity
   OperationID: GetByRelatedTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByRelatedTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByRelatedTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByRelatedTo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/GetByRelatedTo", {
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
   Summary: Invoke method GetNewCalculatedField
   Description: Generic GetNew for a CalculatedField row.
   OperationID: GetNewCalculatedField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCalculatedField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCalculatedField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCalculatedField(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/GetNewCalculatedField", {
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
   Summary: Invoke method UpdateCalculatedField
   Description: Updates CalculatedField based on user input and sets the full expressions.
   OperationID: UpdateCalculatedField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCalculatedField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCalculatedField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateCalculatedField(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/UpdateCalculatedField", {
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
   Summary: Invoke method CheckFormulaSyntax
   Description: Checks the SQL expression syntax
   OperationID: CheckFormulaSyntax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFormulaSyntax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFormulaSyntax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckFormulaSyntax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CalculatedFieldSvc/CheckFormulaSyntax", {
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
      @param fieldName
      @param ds
   */  
export interface CheckFormulaSyntax_input{
   fieldName:string,
   ds:Erp_Tablesets_CalculatedFieldTableset[],
}

export interface CheckFormulaSyntax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CalculatedFieldTableset[],
}
}

export interface Erp_Tablesets_CalculatedFieldListValuesRow{
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  ID of related Attribute.  */  
   AttributeID:string,
      /**  Code of the list value.  */  
   Code:string,
      /**  Company identifier  */  
   Company:string,
      /**  Database Field Name  */  
   DBFieldName:string,
      /**  Databse Schema Name  */  
   DBSchemaName:string,
      /**  Database Table Name  */  
   DBTableName:string,
      /**  Description of the list values.  */  
   Description:string,
      /**  Field name.  */  
   FieldName:string,
      /**  Table ID.  */  
   TableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CalculatedFieldRow{
      /**  Alias  */  
   Alias:string,
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Data Type.  */  
   DataType:string,
      /**  Database Field Name  */  
   DBFieldName:string,
      /**  Database Schema Name.  */  
   DBSchemaName:string,
      /**  Database Table Name.  */  
   DBTableName:string,
      /**  Description.  */  
   Description:string,
      /**  Field Format.  */  
   FieldFormat:string,
      /**  Field Label.  */  
   FieldLabel:string,
      /**  Field Name.  */  
   FieldName:string,
      /**  Final Expression UOM  */  
   FinalExpressionUOM:string,
      /**  Formula  */  
   Formula:string,
      /**  Full Expression.  */  
   FullExpression:string,
      /**  Is Calculated.  */  
   IsCalculated:boolean,
      /**  Is Final Expression.  */  
   IsFinalExpression:boolean,
      /**  Is Viewable.  */  
   IsViewable:boolean,
      /**  Sequence.  */  
   Seq:number,
      /**  Table ID.  */  
   TableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CalculatedFieldTableset{
   CalculatedField:Erp_Tablesets_CalculatedFieldRow[],
   CalculatedFieldListValues:Erp_Tablesets_CalculatedFieldListValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param relatedToSchemaName
      @param relatedToTableName
      @param relatedToSysRowID
      @param ds
   */  
export interface GetByRelatedTo_input{
   relatedToSchemaName:string,
   relatedToTableName:string,
   relatedToSysRowID:string,
   ds:Erp_Tablesets_CalculatedFieldTableset[],
}

export interface GetByRelatedTo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CalculatedFieldTableset[],
}
}

   /** Required : 
      @param relatedToSchemaName
      @param relatedToTableName
      @param relatedToSysRowID
      @param ds
   */  
export interface GetNewCalculatedField_input{
   relatedToSchemaName:string,
   relatedToTableName:string,
   relatedToSysRowID:string,
   ds:Erp_Tablesets_CalculatedFieldTableset[],
}

export interface GetNewCalculatedField_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CalculatedFieldTableset[],
}
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
   */  
export interface UpdateCalculatedField_input{
   ds:Erp_Tablesets_CalculatedFieldTableset[],
}

export interface UpdateCalculatedField_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CalculatedFieldTableset[],
}
}

