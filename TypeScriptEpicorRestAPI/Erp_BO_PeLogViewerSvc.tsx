import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PeLogViewerSvc
// Description: PELogViewer Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/$metadata", {
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
   Summary: Invoke method GetRows
   Description: Returns a tableset that satisfy the where clause
   OperationID: Get_GetRows
      @param whereClausePeLogViewer Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePeLogViewer:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePeLogViewer!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePeLogViewer=" + whereClausePeLogViewer
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetRows" + params, {
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
   Summary: Invoke method InitPath
   Description: This procedure init path for pelog.txt file on first PELogViewer UI call
   OperationID: InitPath
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitPath_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitPath(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/InitPath", {
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
   Summary: Invoke method ClearLog
   Description: This procedure supposed to delete old logging file. (pelog.txt)
   OperationID: ClearLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearLog(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/ClearLog", {
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
   Summary: Invoke method GetPostModeList
   OperationID: GetPostModeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPostModeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPostModeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetPostModeList", {
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
   Summary: Invoke method GetCompanyList
   OperationID: GetCompanyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompanyList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetCompanyList", {
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
   Summary: Invoke method GetTransactionTypeList
   Description: The list of possible Transaction Types (ACTTypes) across available companies
   OperationID: GetTransactionTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransactionTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransactionTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetTransactionTypeList", {
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
   Summary: Invoke method GetValidList
   OperationID: GetValidList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValidList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetValidList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetValidList", {
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
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetList", {
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
   Summary: Invoke method GetPELogInfoByPostingUIDExt
   Description: This function should return dataset containing logging infromation
about requested posting process. The clone of GetPELogInfoByPostingUID which returns the requested data as the function result
   OperationID: GetPELogInfoByPostingUIDExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPELogInfoByPostingUIDExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPELogInfoByPostingUIDExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPELogInfoByPostingUIDExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetPELogInfoByPostingUIDExt", {
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
   Summary: Invoke method GetPELogInfoByPostingUID
   Description: This function should return dataset containing logging infromation
about requested posting process
   OperationID: GetPELogInfoByPostingUID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPELogInfoByPostingUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPELogInfoByPostingUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPELogInfoByPostingUID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetPELogInfoByPostingUID", {
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
   Summary: Invoke method GetActTypeList
   Description: Returns DataSet containing all Transaction types
   OperationID: GetActTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetActTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetActTypeList", {
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
   Summary: Invoke method SaveActTypeList
   Description: Applies changes in logging settings
   OperationID: SaveActTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveActTypeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveActTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveActTypeList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/SaveActTypeList", {
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
   Summary: Invoke method GetPELogInfo
   Description: This function should return dataset containing logging infromation
about requested posting process
   OperationID: GetPELogInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPELogInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPELogInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPELogInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetPELogInfo", {
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
   Summary: Invoke method FileType
   Description: File Type check
   OperationID: FileType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FileType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/FileType", {
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
   Summary: Invoke method GetDelims
   Description: Returns list delimiters
   OperationID: GetDelims
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDelims_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDelims(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetDelims", {
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
   Summary: Invoke method ExportLog
   Description: Export PE Log into the file
   OperationID: ExportLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportLog(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/ExportLog", {
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
   Summary: Invoke method ImportLog
   Description: Import PE Log file into the PE Log cache
   OperationID: ImportLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportLog(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/ImportLog", {
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
   Summary: Invoke method GetNodeById
   Description: Use the posting Guid 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 or 0ae29784-6050-40a0-8764-099439c5b09b for test purposes
   OperationID: Get_GetNodeById
      @param GPostingUID Desc: 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149   Required: True   Allow empty value : True
      @param NodeID Desc: 0 to load parent   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNodeById_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetNodeById(GPostingUID:string, NodeID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof GPostingUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "GPostingUID=" + GPostingUID
   }
   if(typeof NodeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "NodeID=" + NodeID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/GetNodeById" + params, {
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
   Summary: Invoke method FindNode
   Description: Search node in the tree by the text
   OperationID: Get_FindNode
      @param GPostingUID Desc: The posting log id (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 or 0ae29784-6050-40a0-8764-099439c5b09b for test purposes)   Required: True   Allow empty value : True
      @param searchText Desc: Search text   Required: True   Allow empty value : True
      @param direction Desc: Direction of the search: 0 - search forward, 1- search backward   Required: True
      @param currentNodeID Desc: The start point for the search (empty string - search will be performed at the beginning of the log)   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindNode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_FindNode(GPostingUID:string, searchText:string, direction:string, currentNodeID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof GPostingUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "GPostingUID=" + GPostingUID
   }
   if(typeof searchText!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "searchText=" + searchText
   }
   if(typeof direction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "direction=" + direction
   }
   if(typeof currentNodeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "currentNodeID=" + currentNodeID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeLogViewerSvc/FindNode" + params, {
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
export interface ClearLog_output{
}

export interface Erp_Tablesets_PEActTypeRow{
   Company:string,
   CompanyName:string,
   ACTTypeUID:number,
   ACTTypeName:string,
   Logging:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PEActTypeTableset{
   PEActType:Erp_Tablesets_PEActTypeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PeLogViewerListRow{
   ActType:string,
      /**  PostDate  */  
   PostDate:string,
      /**  GroupID  */  
   GroupID:string,
      /**  RvJrnUID  */  
   RJ:number,
      /**  IsValid  */  
   Valid:boolean,
      /**  XmlText  */  
   XmlText:string,
      /**  GPostingUID  */  
   GPostingUID:string,
      /**  PostMode  */  
   PostMode:string,
      /**  LineNum  */  
   LineNum:number,
      /**  ParentLineNum  */  
   ParentLineNum:number,
   Offset:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PeLogViewerListTableset{
   PeLogViewerList:Erp_Tablesets_PeLogViewerListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PeLogViewerRow{
   ActType:string,
      /**  PostDate  */  
   PostDate:string,
      /**  GroupID  */  
   GroupID:string,
      /**  RvJrnUID  */  
   RJ:number,
      /**  IsValid  */  
   Valid:boolean,
      /**  XmlText  */  
   XmlText:string,
      /**  GPostingUID  */  
   GPostingUID:string,
      /**  PostMode  */  
   PostMode:string,
      /**  LineNum  */  
   LineNum:number,
      /**  ParentLineNum  */  
   ParentLineNum:number,
   Offset:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PeLogViewerTableset{
   PeLogViewer:Erp_Tablesets_PeLogViewerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param GPostingUID
      @param ipSpecialFolder
      @param ipFileName
   */  
export interface ExportLog_input{
      /**  the UID of the PE Log  */  
   GPostingUID:string,
      /**  Special Folder  */  
   ipSpecialFolder:number,
      /**  File Name in the Special Folder  */  
   ipFileName:string,
}

export interface ExportLog_output{
parameters : {
      /**  output parameters  */  
   opFileName:string,
}
}

   /** Required : 
      @param FileInfo
   */  
export interface FileType_input{
   FileInfo:string,
}

export interface FileType_output{
   returnObj:string,
}

   /** Required : 
      @param GPostingUID
      @param searchText
      @param direction
      @param currentNodeID
   */  
export interface FindNode_input{
      /**  The posting log id (Use 0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149 or 0ae29784-6050-40a0-8764-099439c5b09b for test purposes)  */  
   GPostingUID:string,
      /**  Search text  */  
   searchText:string,
      /**  Direction of the search: 0 - search forward, 1- search backward  */  
   direction:number,
      /**  The start point for the search (empty string - search will be performed at the beginning of the log)  */  
   currentNodeID:string,
}

export interface FindNode_output{
      /**  LogNode structure with the found node and all parent ones  */  
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   foundNodeId:string,
   nextFoundNodeId:string,
}
}

export interface GetActTypeList_output{
   returnObj:Erp_Tablesets_PEActTypeTableset[],
}

export interface GetCompanyList_output{
      /**  list of posting modes  */  
   returnObj:string,
}

export interface GetDelims_output{
parameters : {
      /**  output parameters  */  
   ListDelim:string,
   SublistDelim:string,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
      @param ds
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
   ds:Erp_Tablesets_PeLogViewerListTableset[],
}

export interface GetList_output{
parameters : {
      /**  output parameters  */  
   morePages:boolean,
   ds:Erp_Tablesets_PeLogViewerListTableset[],
}
}

   /** Required : 
      @param GPostingUID
      @param NodeID
   */  
export interface GetNodeById_input{
      /**  0aaa410e-ecc2-4dcd-9e6d-0c2d0d879149  */  
   GPostingUID:string,
      /**  0 to load parent  */  
   NodeID:string,
}

export interface GetNodeById_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param GPostingUID
   */  
export interface GetPELogInfoByPostingUIDExt_input{
      /**  The Positng ID  */  
   GPostingUID:string,
}

export interface GetPELogInfoByPostingUIDExt_output{
   returnObj:Erp_Tablesets_PeLogViewerTableset[],
}

   /** Required : 
      @param GPostingUID
      @param ds
   */  
export interface GetPELogInfoByPostingUID_input{
   GPostingUID:string,
   ds:Erp_Tablesets_PeLogViewerTableset[],
}

export interface GetPELogInfoByPostingUID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PeLogViewerTableset[],
}
}

   /** Required : 
      @param inActType
      @param inPostDate
      @param inGroupID
      @param inRJ
      @param inValid
      @param inPostMode
      @param ds
   */  
export interface GetPELogInfo_input{
      /**  Act type name  */  
   inActType:string,
      /**  Posting Date  */  
   inPostDate:string,
      /**  posting group id  */  
   inGroupID:string,
      /**  review journal number  */  
   inRJ:number,
      /**  valid review journal  */  
   inValid:string,
      /**  posting process mode  */  
   inPostMode:string,
   ds:Erp_Tablesets_PeLogViewerTableset[],
}

export interface GetPELogInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PeLogViewerTableset[],
}
}

export interface GetPostModeList_output{
parameters : {
      /**  output parameters  */  
   PostModeList:string,
}
}

   /** Required : 
      @param whereClausePeLogViewer
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClausePeLogViewer:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PeLogViewerTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetTransactionTypeList_output{
   returnObj:string,
}

export interface GetValidList_output{
parameters : {
      /**  output parameters  */  
   ValidList:string,
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
      @param ipSpecialFolder
      @param ipFileName
   */  
export interface ImportLog_input{
      /**  Special Folder  */  
   ipSpecialFolder:number,
      /**  File Name in the Special Folder  */  
   ipFileName:string,
}

export interface ImportLog_output{
   returnObj:Erp_Tablesets_PeLogViewerTableset[],
}

export interface InitPath_output{
}

   /** Required : 
      @param ds
   */  
export interface SaveActTypeList_input{
   ds:Erp_Tablesets_PEActTypeTableset[],
}

export interface SaveActTypeList_output{
}

