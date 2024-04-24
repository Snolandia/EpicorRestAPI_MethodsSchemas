import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.FileTransferSvc
// Description: File transfer service. Enables the manipulation of server files from the client
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/$metadata", {
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
   Summary: Invoke method DownloadFile
   Description: Get a file's content from the server
   OperationID: DownloadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DownloadFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/DownloadFile", {
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
   Summary: Invoke method DownloadFileForCompany
   Description: Get a file's content from the server
   OperationID: DownloadFileForCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadFileForCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFileForCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DownloadFileForCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/DownloadFileForCompany", {
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
   Summary: Invoke method DownloadFileForUser
   Description: Get a file's content from the server
   OperationID: DownloadFileForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadFileForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFileForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DownloadFileForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/DownloadFileForUser", {
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
   Summary: Invoke method UploadFile
   Description: Set a file's content on the server
   OperationID: UploadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/UploadFile", {
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
   Summary: Invoke method FileExists
   Description: Check if file exists on the server.
   OperationID: FileExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FileExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/FileExists", {
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
   Summary: Invoke method FileDelete
   Description: Deletes the specified file. If not found, nothing happens
   OperationID: FileDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FileDelete(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/FileDelete", {
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
   Summary: Invoke method GetFileDetails
   Description: Get the file detail for specific files.
   OperationID: GetFileDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFileDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFileDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFileDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/GetFileDetails", {
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
   Summary: Invoke method GetEdgeAgentCdnDetails
   Description: Get URL and version for current Edge Agent installation for the specific operating system.
   OperationID: Get_GetEdgeAgentCdnDetails
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEdgeAgentCdnDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetEdgeAgentCdnDetails(operatingSystem:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof operatingSystem!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "operatingSystem=" + operatingSystem
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.FileTransferSvc/GetEdgeAgentCdnDetails" + params, {
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
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param folder
      @param serverPath
      @param companyID
   */  
export interface DownloadFileForCompany_input{
      /**  The root of the path  */  
   folder:number,
      /**  The path of the file to get the content for  */  
   serverPath:string,
   companyID:string,
}

export interface DownloadFileForCompany_output{
      /**  File data  */  
   returnObj:string,
}

   /** Required : 
      @param folder
      @param serverPath
      @param userID
   */  
export interface DownloadFileForUser_input{
      /**  The root of the path  */  
   folder:number,
      /**  The path of the file to get the content for  */  
   serverPath:string,
   userID:string,
}

export interface DownloadFileForUser_output{
      /**  File data  */  
   returnObj:string,
}

   /** Required : 
      @param folder
      @param serverPath
   */  
export interface DownloadFile_input{
      /**  The root of the path  */  
   folder:number,
      /**  The path of the file to get the content for  */  
   serverPath:string,
}

export interface DownloadFile_output{
      /**  File data  */  
   returnObj:string,
}

   /** Required : 
      @param folder
      @param serverPath
   */  
export interface FileDelete_input{
      /**  The root of the path.  */  
   folder:number,
      /**  The path of the file to delete.  */  
   serverPath:string,
}

export interface FileDelete_output{
}

   /** Required : 
      @param folder
      @param serverPath
   */  
export interface FileExists_input{
      /**  The root of the path.  */  
   folder:number,
      /**  Path to the file on the server.  */  
   serverPath:string,
}

export interface FileExists_output{
      /**  True if exists  */  
   returnObj:boolean,
}

   /** Required : 
      @param operatingSystem
   */  
export interface GetEdgeAgentCdnDetails_input{
   operatingSystem:string,
}

export interface GetEdgeAgentCdnDetails_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param folder
      @param serverPath
   */  
export interface GetFileDetails_input{
      /**  The root of the path.  */  
   folder:number,
      /**  Path to the file on the server.  */  
   serverPath:string,
}

export interface GetFileDetails_output{
      /**  Dictionary with keys for FileInfo object: FileName, FileVersion, ProductVersion, ModifiedDate, SizeInByte.  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param folder
      @param serverPath
      @param data
   */  
export interface UploadFile_input{
      /**  The root of the path  */  
   folder:number,
      /**  The path of the file to set the content to  */  
   serverPath:string,
      /**  File data  */  
   data:string,
}

export interface UploadFile_output{
}

