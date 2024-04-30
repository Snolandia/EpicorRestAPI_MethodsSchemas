import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.AttachmentTransferSvc
// Description: File Attachments
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/$metadata", {
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
   Summary: Invoke method GetFileStoreList
   Description: Get list of attachments stored as files
   OperationID: GetFileStoreList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFileStoreList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFileStoreList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFileStoreList(requestBody:GetFileStoreList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFileStoreList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/GetFileStoreList", {
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
         resolve(data as GetFileStoreList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDocTypeList
   Description: Get List of existing attachment types
   OperationID: GetDocTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDocTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDocTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDocTypeList(requestBody:GetDocTypeList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDocTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/GetDocTypeList", {
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
         resolve(data as GetDocTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteOrpanedRecords
   Description: Delete records from child table that do not have records in the parent table
   OperationID: DeleteOrpanedRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteOrpanedRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteOrpanedRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteOrpanedRecords(requestBody:DeleteOrpanedRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteOrpanedRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/DeleteOrpanedRecords", {
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
         resolve(data as DeleteOrpanedRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteRecordsWithoutFiles
   Description: Delete records that do not have correspondent files
   OperationID: DeleteRecordsWithoutFiles
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteRecordsWithoutFiles_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRecordsWithoutFiles_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRecordsWithoutFiles(requestBody:DeleteRecordsWithoutFiles_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteRecordsWithoutFiles_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/DeleteRecordsWithoutFiles", {
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
         resolve(data as DeleteRecordsWithoutFiles_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateBasePath
   Description: Change path for files to new location
   OperationID: UpdateBasePath
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateBasePath_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBasePath_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateBasePath(requestBody:UpdateBasePath_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateBasePath_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentTransferSvc/UpdateBasePath", {
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
         resolve(data as UpdateBasePath_output)
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
      @param company
      @param docType
   */  
export interface DeleteOrpanedRecords_input{
   company:string,
   docType:string,
}

export interface DeleteOrpanedRecords_output{
}

   /** Required : 
      @param company
      @param docType
   */  
export interface DeleteRecordsWithoutFiles_input{
   company:string,
   docType:string,
}

export interface DeleteRecordsWithoutFiles_output{
}

   /** Required : 
      @param Company
      @param docTypeID
   */  
export interface GetDocTypeList_input{
   Company:string,
   docTypeID:string,
}

export interface GetDocTypeList_output{
   returnObj:Ice_Tablesets_AttachmentTransferTableset[],
}

   /** Required : 
      @param Company
      @param docTypeID
      @param problemsOnly
      @param checkFileExists
   */  
export interface GetFileStoreList_input{
      /**  Company to select attachments  */  
   Company:string,
      /**  DocTypeID of attachment - or empty for default attachments  */  
   docTypeID:string,
   problemsOnly:boolean,
   checkFileExists:boolean,
}

export interface GetFileStoreList_output{
   returnObj:Ice_Tablesets_AttachmentTransferTableset[],
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

export interface Ice_Tablesets_AttachmentTransferDocTypeRow{
   Company:string,
   DocTypeID:string,
   FileTransferMode:number,
   FileTransferModeResolved:string,
   BaseURL:string,
   Status:string,
   StatusText:string,
   Description:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AttachmentTransferFileRefRow{
   Company:string,
   DocTypeID:string,
   XFileName:string,
   Status:string,
   StatusText:string,
   RelatedToFile:string,
   ForeignSysRowID:string,
   XFileRefNum:number,
   RelatedToSchemaName:string,
   StorageType:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AttachmentTransferRow{
   Company:string,
   BaseFolder:string,
   FileTransferMode:number,
   FileTransferModeResolved:string,
   Status:string,
   StatusText:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AttachmentTransferTableset{
   AttachmentTransfer:Ice_Tablesets_AttachmentTransferRow[],
   AttachmentTransferDocType:Ice_Tablesets_AttachmentTransferDocTypeRow[],
   AttachmentTransferFileRef:Ice_Tablesets_AttachmentTransferFileRefRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param company
      @param docType
      @param existingPath
      @param newBasePath
      @param batchSize
   */  
export interface UpdateBasePath_input{
   company:string,
   docType:string,
      /**  existing path  */  
   existingPath:string,
      /**  new path to use  */  
   newBasePath:string,
      /**  number of items to move in one transaction  */  
   batchSize:number,
}

export interface UpdateBasePath_output{
   returnObj:number,
}

