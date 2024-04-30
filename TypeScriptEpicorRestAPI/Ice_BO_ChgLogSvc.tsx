import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.ChgLogSvc
// Description: bo/ChgLog/ChgLog.p
           Generic Change Log - BL
           Rajesh Tapde
           06-19-2003
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ChgLogSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ChgLogSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetChgLog
   Description: Gets the related ChgLog records based on TableName,RowID
   OperationID: GetChgLog
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetChgLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChgLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetChgLog(requestBody:GetChgLog_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetChgLog_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ChgLogSvc/GetChgLog", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetChgLog_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetChgLogByClause
   Description: Gets the related ChgLog records based on where clause passed in
   OperationID: GetChgLogByClause
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetChgLogByClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChgLogByClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetChgLogByClause(requestBody:GetChgLogByClause_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetChgLogByClause_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ChgLogSvc/GetChgLogByClause", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetChgLogByClause_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ip_WhereClause
   */  
export interface GetChgLogByClause_input{
      /**  Where clause used for retrieval  */  
   ip_WhereClause:string,
}

export interface GetChgLogByClause_output{
   returnObj:Ice_Tablesets_ChgLogTableset[],
}

   /** Required : 
      @param ip_systemCode
      @param ip_tableName
      @param ip_sysRowID
   */  
export interface GetChgLog_input{
      /**  SystemCode to retrieve ChgLog records for  */  
   ip_systemCode:string,
      /**  Table name to retrieve ChgLog records for  */  
   ip_tableName:string,
      /**  RowID of the record to retrieve ChgLog records for  */  
   ip_sysRowID:string,
}

export interface GetChgLog_output{
   returnObj:Ice_Tablesets_ChgLogTableset[],
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

export interface Ice_Tablesets_ChgLogRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The identifier is used to group the changes made to related tables together. This value is assigned by the system using the value found in ZDataField.ChgLogID.  For example: Customer, ShipTo, CustBillTo, CustCnt, are all related and will have a ChgLogID = "Customer".  */  
   Identifier:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  Name of the table which was changed  */  
   TableName:string,
      /**  Major component of the foreign key of the related master record.  For example: For a "PO" change record this field would contain the related PO Number,  for a "SO" change record it would contain the related SO Number.  */  
   Key1:string,
      /**   tilde separated list of key values of the changed record
For Example a ChgLog for POREL might be something like 301~2~1. 301 is the PONum, 2 is the LineNum and 1 is the ReleaseNum  */  
   Key2:string,
      /**  Third component of the foreign key of the related master record.  For example: For a "PORel" change record this field would contain the related PO Release Number.  The usage of this field is dependent on the type of record the change record is related to.  For example: changes to "POHeader" and "PODetail" do not use this field while changes to "PORel" do.  */  
   Key3:string,
      /**  DateStampedOn  */  
   DateStampedOn:string,
      /**   Log message text.  This text may be in the following formats:
1) "New Record"
2) UserID  Time  FieldLabel/Name  OldValue "->" NewValue  */  
   LogText:string,
      /**  This field allows one record to have more than one change log for a day.  This is to fix the issue of storing more than 32K in logtext field  */  
   LogNum:number,
      /**  The User ID that created this log.  */  
   UserID:string,
      /**   Possible values D & U (Described in XbSyst.ChgLogMethod).
For value D (Daily), the DCDUserID value is blank. For value U (User), the DCDUserID is populated.  */  
   ChgLogMethod:string,
      /**   For future use.

An integer assigned by the system to uniquely identify the ChgLog record.  This integer is created by using the database sequence "ChgLogSeq".  */  
   ChgLogSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ChgLogTableset{
   ChgLog:Ice_Tablesets_ChgLogRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

